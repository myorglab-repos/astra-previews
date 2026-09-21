"""Digital-only signal contract. No hardware output; standard library only.

Lead Track A freeze — NOT measured hardware limits / product bars.
Cite docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md
and docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md.

NORMATIVE sign: positive image x → positive world X via +Z yaw from −Y home.

    signed_x = (2*cx - 1)                         # frame_fraction_0_to_1
    yaw_cmd  = clamp(sign * gain * signed_x, ±clamp) when gates and config are set
    else yaw_cmd = 0.0                             # home_zero; nulls deny chase

    sign = +1
    gain_deg_per_signed_x = 30.0
    clamp_deg = 30.0
    watchdog_s = 2.0
    idle_policy = home_zero

ASSUMPTION / DESIGN ESTIMATE. Not a measured FPS, accuracy, force, or hardware stop.
"""
import json
import math
import time

BOOLS = ('user_present', 'head_hypothesis_valid', 'presence_sensor_fault',
         'inhibit_latched', 'e_stop_asserted')

# Locked digital design. Do not retune these in this packet.
HY03_FREEZE_ID = 'HY-03-LEAD-FROZEN-2026-09-21'
HY03_LABEL = 'Lead Track A freeze — NOT measured hardware limits / product bars'
SIGN_NORMATIVE = 'positive image x → positive world X via +Z yaw from −Y home'
FROZEN_SIGN = 1
FROZEN_GAIN_DEG = 30.0
FROZEN_CLAMP_DEG = 30.0
FROZEN_WATCHDOG_S = 2.0
FROZEN_IDLE = 'home_zero'
FROZEN_NORMALIZATION = 'frame_fraction_0_to_1'


def number(x):
    return type(x) in (int, float) and math.isfinite(x)


def signed_x(centroid_x):
    """signed_x = (2*cx - 1). frame_fraction_0_to_1. Center is 0. Image right is positive."""
    return 2.0 * centroid_x - 1.0


signed_offset = signed_x


def clamp_yaw(raw_deg, clamp_deg):
    """Symmetric digital clamp. Lead Track A freeze — NOT measured hardware limits / product bars."""
    return max(-clamp_deg, min(clamp_deg, raw_deg))


def map_yaw(centroid_x, config):
    """Return (unclamped_deg, clamped_deg) for a valid centroid. Sign is in config."""
    raw = config['sign'] * config['gain_deg_per_signed_x'] * signed_x(centroid_x)
    return raw, clamp_yaw(raw, config['clamp_deg'])


def assert_hy03_freeze(c):
    """Reject a freeze-labeled config that drifts from the locked design estimate."""
    if c.get('mapping_freeze') != HY03_FREEZE_ID:
        raise ValueError('HY-03 freeze id mismatch')
    if c.get('label') != HY03_LABEL:
        raise ValueError('HY-03 label must stay visible: ' + HY03_LABEL)
    text = c.get('assumptions') or ''
    if HY03_LABEL not in text or 'ASSUMPTION' not in text or 'DESIGN ESTIMATE' not in text:
        raise ValueError('HY-03 assumptions must keep the Lead Track A freeze label visible')
    if SIGN_NORMATIVE not in (c.get('sign_convention') or ''):
        raise ValueError('Sign text must stay NORMATIVE: ' + SIGN_NORMATIVE)
    if c.get('performance_claim') != 'NONE':
        raise ValueError('HY-03 freeze carries no performance claim')
    if c['sign'] != FROZEN_SIGN:
        raise ValueError('Frozen sign is +1')
    if c['gain_deg_per_signed_x'] != FROZEN_GAIN_DEG:
        raise ValueError('Frozen gain is the 30 deg design estimate')
    if c['clamp_deg'] != FROZEN_CLAMP_DEG:
        raise ValueError('Frozen clamp is the ±30 deg design estimate')
    if c['watchdog_s'] != FROZEN_WATCHDOG_S:
        raise ValueError('Frozen watchdog is the 2 s design estimate')
    if c['idle_policy'] != FROZEN_IDLE:
        raise ValueError('Frozen idle is home_zero')
    if c['normalization'] != FROZEN_NORMALIZATION:
        raise ValueError('Frozen normalization is frame_fraction_0_to_1')
    return c


def transport_stale(age_s, watchdog_s):
    """True when the freshness window is unset or the same-machine age is outside it.

    age == watchdog_s is still fresh. This is a design-estimate gate, not a latency bar.
    """
    if watchdog_s is None or not number(age_s):
        return True
    return age_s < 0 or age_s > watchdog_s


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
    if c.get('mapping_freeze') is not None:
        assert_hy03_freeze(c)
    return c


def derive(p, c):
    """Strict validation; never trust sender-computed enable or yaw.

    Idle policy home_zero: every disabled path returns yaw_cmd 0.
    """
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
    yaw = map_yaw(cx, c)[1] if enabled else 0.0
    flags = []
    if not configured:
        flags.append('mapping_or_watchdog_TBD')
    if not present:
        flags.append('absent')
    if p['presence_sensor_fault']:
        flags.append('presence_sensor_fault')
    if not p['head_hypothesis_valid']:
        flags.append('head_invalid_or_unchecked')
    if p['inhibit_latched']:
        flags.append('inhibit')
    if p['e_stop_asserted']:
        flags.append('e_stop_sim')
    if p['sync_quality'] != 'ok':
        flags.append('sync_' + p['sync_quality'])
    return dict(user_present=present, session_enable=session, yaw_cmd_enable=formula,
                effective_enable=enabled, yaw_cmd=yaw, yaw_units='degrees', quality_flags=flags,
                idle_policy=c['idle_policy'])


class ReceiverState:
    """Sticky simulated inhibit, fresh-packet watchdog and ordered single stream.

    Manual reset / arm are local operator calls, never network commands.
    A new sender stream needs a local rebind; rebind does not clear the latch.
    Watchdog expiry and rejected packets idle at home_zero (yaw_cmd 0).
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
                           quality_flags=[reason], receiver_latched=self.latched,
                           idle_policy=self.config['idle_policy'])
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
            if transport_stale(age, self.config['watchdog_s']):
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
        if self.last_rx is None or transport_stale(now - self.last_rx, self.config['watchdog_s']):
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
