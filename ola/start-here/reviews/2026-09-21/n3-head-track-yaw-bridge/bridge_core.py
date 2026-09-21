"""Digital-only signal contract. No hardware output; standard library only."""
import json
import math
import time

BOOLS = ('user_present', 'head_hypothesis_valid', 'presence_sensor_fault',
         'inhibit_latched', 'e_stop_asserted')


def number(x):
    return type(x) in (int, float) and math.isfinite(x)


def validate_config(c):
    assert c['scope'] == 'DIGITAL_TWIN_ONLY'
    assert c['host'] == '127.0.0.1', 'Loopback only'
    assert type(c['port']) is int and 1024 <= c['port'] <= 65535
    assert c['normalization'] == 'frame_fraction_0_to_1'
    assert c['idle_policy'] == 'home_zero'
    for k in ('gain_deg_per_signed_x', 'clamp_deg', 'watchdog_s'):
        if c[k] is not None:
            assert number(c[k]) and c[k] > 0, k
    assert c['sign'] in (-1, 1)
    return c


def derive(p, c):
    """Strict validation; never trust sender-computed enable or yaw."""
    if not isinstance(p, dict) or any(type(p.get(k)) is not bool for k in BOOLS):
        raise ValueError('Missing/non-boolean gate')
    if p.get('schema_rev') != 'head-yaw-v1' or p.get('scope') != 'DIGITAL_TWIN_ONLY':
        raise ValueError('Wrong protocol/scope')
    if p.get('sync_quality') not in ('ok', 'stale', 'unknown'):
        raise ValueError('Invalid sync quality')
    if not number(p.get('t_sync')) or p['t_sync'] < 0:
        raise ValueError('Invalid capture time')
    cx = p.get('head_centroid_x')
    if cx is not None and (not number(cx) or not 0 <= cx <= 1):
        raise ValueError('Invalid centroid')
    if p['head_hypothesis_valid'] and cx is None:
        raise ValueError('Valid head requires centroid')
    present = p['user_present'] and not p['presence_sensor_fault']
    session = present and p['head_hypothesis_valid'] and not p['inhibit_latched']
    formula = session and not p['e_stop_asserted']
    configured = all(c[k] is not None for k in ('gain_deg_per_signed_x', 'clamp_deg', 'watchdog_s'))
    enabled = formula and p['sync_quality'] == 'ok' and configured
    yaw = max(-c['clamp_deg'], min(c['clamp_deg'], c['sign'] * c['gain_deg_per_signed_x'] * (2*cx-1))) if enabled else 0.0
    flags = []
    if not configured: flags.append('mapping_or_watchdog_TBD')
    if not present: flags.append('absent')
    if p['presence_sensor_fault']: flags.append('presence_sensor_fault')
    if not p['head_hypothesis_valid']: flags.append('head_invalid_or_unchecked')
    if p['inhibit_latched']: flags.append('inhibit')
    if p['e_stop_asserted']: flags.append('e_stop_sim')
    if p['sync_quality'] != 'ok': flags.append('sync_'+p['sync_quality'])
    return dict(user_present=present, session_enable=session, yaw_cmd_enable=formula,
                effective_enable=enabled, yaw_cmd=yaw, yaw_units='degrees', quality_flags=flags)


class ReceiverState:
    """Sticky simulated inhibit, fresh-packet watchdog and ordered single stream.

    Manual reset / arm are local operator calls, never network commands.
    A new sender stream needs a local rebind; rebind does not clear the latch.
    """
    def __init__(self, config):
        self.config = validate_config(config)
        self.stream = None
        self.seq = -1
        self.last_rx = None
        self.last_inputs = None
        self.latched = False
        self.armed = True  # explicit local start() is the initial digital enable
        self.output = self.idle('startup')

    def idle(self, reason):
        self.output = dict(user_present=False, session_enable=False, yaw_cmd_enable=False,
                           effective_enable=False, yaw_cmd=0.0, yaw_units='degrees',
                           quality_flags=[reason], receiver_latched=self.latched)
        return self.output

    def ingest(self, raw, now=None):
        now = time.monotonic() if now is None else now
        try:
            p = json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
            result = derive(p, self.config)
            if type(p.get('seq')) is not int or p['seq'] < 0:
                raise ValueError('Invalid sequence')
            if not isinstance(p.get('stream_id'), str) or not 1 <= len(p['stream_id']) <= 80:
                raise ValueError('Invalid stream')
            if not number(p.get('sent_monotonic_s')):
                raise ValueError('Missing local clock')
            age = now - p['sent_monotonic_s']
            if self.config['watchdog_s'] is None or age < 0 or age > self.config['watchdog_s']:
                raise ValueError('Stale transport or unconfigured watchdog')
            if self.stream not in (None, p['stream_id']) or p['seq'] <= self.seq:
                raise ValueError('Wrong stream or reordered packet')
            self.stream, self.seq, self.last_rx, self.last_inputs = p['stream_id'], p['seq'], now, p
            self.latched = self.latched or p['inhibit_latched'] or p['e_stop_asserted']
            if self.latched or not self.armed:
                result.update(effective_enable=False, yaw_cmd=0.0)
                result['quality_flags'].append('receiver_latched' if self.latched else 'manual_arm_required')
            result['receiver_latched'] = self.latched
            self.output = result
            return p, result
        except (ValueError, TypeError, KeyError, OverflowError):
            self.last_inputs = None
            return None, self.idle('malformed_stale_or_reordered_packet')

    def tick(self, now=None):
        now = time.monotonic() if now is None else now
        if self.last_rx is None or self.config['watchdog_s'] is None or now-self.last_rx > self.config['watchdog_s']:
            self.last_inputs = None
            return self.idle('transport_timeout')
        return self.output

    def manual_reset(self):
        p = self.last_inputs
        if not p or p['inhibit_latched'] or p['e_stop_asserted']:
            raise ValueError('Clear source fault and receive a fresh packet first')
        self.latched = False
        self.armed = False
        self.idle('manual_reset_requires_arm')

    def arm(self):
        if self.latched:
            raise ValueError('Manual reset required')
        self.armed = True
        self.idle('armed_waiting_for_fresh_packet')

    def rebind(self):
        self.stream, self.seq, self.last_rx, self.last_inputs = None, -1, None, None
        self.idle('rebind_waiting_for_fresh_packet')
