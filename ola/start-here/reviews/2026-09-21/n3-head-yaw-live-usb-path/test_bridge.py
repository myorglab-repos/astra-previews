import copy, itertools, json, unittest
from pathlib import Path
from bridge_core import derive, ReceiverState, validate_config
R=Path(__file__).resolve().parent
C=json.loads((R/'demo_config.json').read_text())


def packet(**kw):
    p=dict(schema_rev='head-yaw-v1',scope='DIGITAL_TWIN_ONLY',stream_id='test',seq=0,sent_monotonic_s=10.0,t_sync=0.0,sync_quality='ok',user_present=True,head_hypothesis_valid=True,presence_sensor_fault=False,inhibit_latched=False,e_stop_asserted=False,head_centroid_x=.8)
    p.update(kw);return p


class BridgeTests(unittest.TestCase):
    def test_all_gate_combinations(self):
        for present,valid,inhibit,stop,fault in itertools.product([False,True],repeat=5):
            p=packet(user_present=present,head_hypothesis_valid=valid,inhibit_latched=inhibit,e_stop_asserted=stop,presence_sensor_fault=fault)
            r=derive(p,C)
            self.assertEqual(r['session_enable'],present and not fault and valid and not inhibit)
            self.assertEqual(r['yaw_cmd_enable'],present and not fault and valid and not inhibit and not stop)
            self.assertEqual(r['effective_enable'],r['yaw_cmd_enable'])
            if not r['effective_enable']:self.assertEqual(r['yaw_cmd'],0)

    def test_direction_clamp_unconfigured(self):
        self.assertLess(derive(packet(head_centroid_x=.2),C)['yaw_cmd'],0)
        self.assertGreater(derive(packet(head_centroid_x=.8),C)['yaw_cmd'],0)
        c=dict(C,clamp_deg=5)
        self.assertEqual(derive(packet(head_centroid_x=1),c)['yaw_cmd'],5)
        c=json.loads((R/'config_template.json').read_text())
        self.assertFalse(derive(packet(),c)['effective_enable'])
        for flag in ('stale','unknown'):
            self.assertFalse(derive(packet(sync_quality=flag),C)['effective_enable'])

    def test_invalid_contract(self):
        for key,value in [('user_present','false'),('e_stop_asserted',0),('head_centroid_x',float('nan')),('head_centroid_x',2),('head_centroid_x',None),('t_sync',float('inf'))]:
            with self.assertRaises(ValueError):derive(packet(**{key:value}),C)
        p=packet();del p['inhibit_latched']
        with self.assertRaises(ValueError):derive(p,C)

    def test_watchdog_packet_order_and_sender_restart(self):
        s=ReceiverState(C)
        self.assertTrue(s.ingest(json.dumps(packet()),10)[1]['effective_enable'])
        self.assertEqual(s.ingest(json.dumps(packet()),10)[1]['yaw_cmd'],0)
        self.assertEqual(s.ingest(json.dumps(packet(seq=1,sent_monotonic_s=1)),10)[1]['yaw_cmd'],0)
        self.assertEqual(s.ingest(json.dumps(packet(seq=1,sent_monotonic_s=11)),10)[1]['yaw_cmd'],0)
        self.assertEqual(s.ingest(json.dumps(packet(seq=1,stream_id='new')),10)[1]['yaw_cmd'],0)
        s.ingest(json.dumps(packet(seq=2)),10)
        self.assertEqual(s.tick(13)['yaw_cmd'],0)
        self.assertEqual(s.ingest(b'{bad',13)[1]['yaw_cmd'],0)
        self.assertEqual(s.ingest(b'{"x":NaN}',13)[1]['yaw_cmd'],0)

    def test_latch_reset_arm_and_reconnect(self):
        for fault in ('inhibit_latched','e_stop_asserted'):
            s=ReceiverState(C)
            s.ingest(json.dumps(packet(**{fault:True})),10)
            with self.assertRaises(ValueError):s.manual_reset()
            s.rebind()
            s.ingest(json.dumps(packet(stream_id='restart')),10)
            self.assertTrue(s.latched)
            self.assertEqual(s.output['yaw_cmd'],0)
            s.manual_reset()
            self.assertEqual(s.output['yaw_cmd'],0)
            self.assertFalse(s.ingest(json.dumps(packet(stream_id='restart',seq=1)),10)[1]['effective_enable'])
            s.arm()
            self.assertEqual(s.output['yaw_cmd'],0)
            self.assertTrue(s.ingest(json.dumps(packet(stream_id='restart',seq=2)),10)[1]['effective_enable'])


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(BridgeTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    (R/'unit_verification.json').write_text(json.dumps(dict(status='PASS' if result.wasSuccessful() else 'FAIL',test_methods=result.testsRun,gate_combinations=32,failures=len(result.failures),errors=len(result.errors)),indent=2))
    raise SystemExit(not result.wasSuccessful())
