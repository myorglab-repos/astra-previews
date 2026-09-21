"""HY-03 unit locks: sign, clamp, idle home_zero, watchdog stale.

Lead Track A freeze — NOT measured hardware limits / product bars.
"""
import copy
import itertools
import json
import unittest
from pathlib import Path

from bridge_core import (
    FROZEN_CLAMP_DEG,
    FROZEN_GAIN_DEG,
    FROZEN_SIGN,
    FROZEN_WATCHDOG_S,
    HY03_LABEL,
    SIGN_NORMATIVE,
    ReceiverState,
    assert_hy03_freeze,
    clamp_yaw,
    derive,
    map_yaw,
    signed_x,
    transport_stale,
    validate_config,
)

R = Path(__file__).resolve().parent
C = json.loads((R / 'frozen_config.json').read_text(encoding='utf-8'))
T = json.loads((R / 'config_template.json').read_text(encoding='utf-8'))
U = json.loads((R / 'config_unconfigured.json').read_text(encoding='utf-8'))


def packet(**kw):
    p = dict(
        schema_rev='head-yaw-v1', scope='DIGITAL_TWIN_ONLY', stream_id='test', seq=0,
        sent_monotonic_s=10.0, t_sync=0.0, sync_quality='ok', user_present=True,
        head_hypothesis_valid=True, presence_sensor_fault=False, inhibit_latched=False,
        e_stop_asserted=False, head_centroid_x=0.8,
    )
    p.update(kw)
    return p


class Hy03FreezeTests(unittest.TestCase):
    def test_freeze_label_and_locked_numbers(self):
        validate_config(C)
        validate_config(T)
        assert_hy03_freeze(C)
        assert_hy03_freeze(T)
        self.assertEqual(C['label'], HY03_LABEL)
        self.assertIn(HY03_LABEL, C['assumptions'])
        self.assertIn(SIGN_NORMATIVE, C['sign_convention'])
        self.assertIn('ASSUMPTION', C['assumptions'])
        self.assertIn('DESIGN ESTIMATE', C['assumptions'])
        self.assertEqual(signed_x(0.0), -1.0)
        self.assertEqual(signed_x(0.5), 0.0)
        self.assertEqual(signed_x(1.0), 1.0)
        for key in ('sign', 'gain_deg_per_signed_x', 'clamp_deg', 'watchdog_s', 'idle_policy', 'normalization'):
            self.assertEqual(T[key], C[key])
            self.assertIsNotNone(T[key])
        self.assertEqual(C['sign'], FROZEN_SIGN)
        self.assertEqual(C['gain_deg_per_signed_x'], FROZEN_GAIN_DEG)
        self.assertEqual(C['clamp_deg'], FROZEN_CLAMP_DEG)
        self.assertEqual(C['watchdog_s'], FROZEN_WATCHDOG_S)
        self.assertEqual(C['idle_policy'], 'home_zero')
        self.assertEqual(C['performance_claim'], 'NONE')
        drifted = copy.deepcopy(C)
        drifted['sign'] = -1
        with self.assertRaises(ValueError):
            assert_hy03_freeze(drifted)

    def test_sign(self):
        """Image right is positive yaw. Image left is negative. Center is home."""
        right = derive(packet(head_centroid_x=0.8), C)
        left = derive(packet(head_centroid_x=0.2), C)
        center = derive(packet(head_centroid_x=0.5), C)
        self.assertGreater(right['yaw_cmd'], 0.0)
        self.assertLess(left['yaw_cmd'], 0.0)
        self.assertAlmostEqual(center['yaw_cmd'], 0.0)
        self.assertAlmostEqual(right['yaw_cmd'], FROZEN_SIGN * FROZEN_GAIN_DEG * (2 * 0.8 - 1))
        self.assertAlmostEqual(left['yaw_cmd'], FROZEN_SIGN * FROZEN_GAIN_DEG * (2 * 0.2 - 1))
        self.assertEqual(map_yaw(1.0, C)[1], FROZEN_CLAMP_DEG)
        self.assertEqual(map_yaw(0.0, C)[1], -FROZEN_CLAMP_DEG)

    def test_clamp(self):
        self.assertEqual(clamp_yaw(45.0, FROZEN_CLAMP_DEG), FROZEN_CLAMP_DEG)
        self.assertEqual(clamp_yaw(-45.0, FROZEN_CLAMP_DEG), -FROZEN_CLAMP_DEG)
        self.assertEqual(clamp_yaw(18.0, FROZEN_CLAMP_DEG), 18.0)
        raw, clamped = map_yaw(0.0, C)
        self.assertEqual(raw, -FROZEN_GAIN_DEG)
        self.assertEqual(clamped, -FROZEN_CLAMP_DEG)
        raw, clamped = map_yaw(1.0, C)
        self.assertEqual(raw, FROZEN_GAIN_DEG)
        self.assertEqual(clamped, FROZEN_CLAMP_DEG)
        self.assertLessEqual(abs(derive(packet(head_centroid_x=0.0), C)['yaw_cmd']), FROZEN_CLAMP_DEG)
        self.assertLessEqual(abs(derive(packet(head_centroid_x=1.0), C)['yaw_cmd']), FROZEN_CLAMP_DEG)

    def test_idle_home_zero(self):
        startup = ReceiverState(C)
        self.assertEqual(startup.output['yaw_cmd'], 0.0)
        self.assertEqual(startup.output['idle_policy'], 'home_zero')
        self.assertIn('startup', startup.output['quality_flags'])
        cases = [
            dict(user_present=False),
            dict(head_hypothesis_valid=False, head_centroid_x=None),
            dict(inhibit_latched=True),
            dict(e_stop_asserted=True),
            dict(presence_sensor_fault=True),
            dict(sync_quality='stale'),
            dict(sync_quality='unknown'),
        ]
        for kw in cases:
            result = derive(packet(**kw), C)
            self.assertEqual(result['yaw_cmd'], 0.0, kw)
            self.assertFalse(result['effective_enable'], kw)
            self.assertEqual(result['idle_policy'], 'home_zero')
        unconfigured = derive(packet(), U)
        self.assertEqual(unconfigured['yaw_cmd'], 0.0)
        self.assertFalse(unconfigured['effective_enable'])
        self.assertIn('mapping_or_watchdog_TBD', unconfigured['quality_flags'])

    def test_watchdog_stale(self):
        self.assertFalse(transport_stale(FROZEN_WATCHDOG_S, FROZEN_WATCHDOG_S))
        self.assertTrue(transport_stale(FROZEN_WATCHDOG_S + 0.1, FROZEN_WATCHDOG_S))
        self.assertTrue(transport_stale(-0.01, FROZEN_WATCHDOG_S))
        self.assertTrue(transport_stale(0.0, None))
        state = ReceiverState(C)
        fresh = state.ingest(json.dumps(packet(sent_monotonic_s=10.0)), 10.0)[1]
        self.assertTrue(fresh['effective_enable'])
        self.assertGreater(fresh['yaw_cmd'], 0.0)
        held = state.tick(10.0 + FROZEN_WATCHDOG_S)
        self.assertGreater(held['yaw_cmd'], 0.0)
        expired = state.tick(10.0 + FROZEN_WATCHDOG_S + 0.1)
        self.assertEqual(expired['yaw_cmd'], 0.0)
        self.assertEqual(expired['idle_policy'], 'home_zero')
        self.assertIn('transport_timeout', expired['quality_flags'])
        stale = ReceiverState(C).ingest(
            json.dumps(packet(sent_monotonic_s=10.0)),
            10.0 + FROZEN_WATCHDOG_S + 0.1,
        )[1]
        self.assertEqual(stale['yaw_cmd'], 0.0)
        self.assertIn('malformed_stale_or_reordered_packet', stale['quality_flags'])

    def test_gate_combinations_still_home_when_blocked(self):
        for present, valid, inhibit, stop, fault in itertools.product([False, True], repeat=5):
            p = packet(
                user_present=present, head_hypothesis_valid=valid, inhibit_latched=inhibit,
                e_stop_asserted=stop, presence_sensor_fault=fault,
            )
            if not valid:
                p['head_centroid_x'] = None
            result = derive(p, C)
            self.assertEqual(result['session_enable'], present and not fault and valid and not inhibit)
            self.assertEqual(
                result['yaw_cmd_enable'],
                present and not fault and valid and not inhibit and not stop,
            )
            self.assertEqual(result['effective_enable'], result['yaw_cmd_enable'])
            if not result['effective_enable']:
                self.assertEqual(result['yaw_cmd'], 0.0)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Hy03FreezeTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    report = dict(
        status='PASS' if result.wasSuccessful() else 'FAIL',
        pass_id='n3-hy03-yaw-mapping-freeze',
        test_methods=result.testsRun,
        gate_combinations=32,
        failures=len(result.failures),
        errors=len(result.errors),
        label='Lead Track A freeze — NOT measured hardware limits / product bars',
        freeze_id='HY-03-LEAD-FROZEN-2026-09-21',
        covered=['sign', 'clamp', 'idle_home_zero', 'watchdog_stale'],
        performance_claim='NONE',
    )
    (R / 'unit_verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    raise SystemExit(not result.wasSuccessful())
