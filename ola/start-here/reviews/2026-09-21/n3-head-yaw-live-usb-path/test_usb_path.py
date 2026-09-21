"""USB fail-fast + clip open proofs. Missing camera is not a test failure."""
import json
import subprocess
import sys
import time
import unittest
from pathlib import Path

from capture_head import CameraOpenError, open_camera, open_clip

R = Path(__file__).resolve().parent
PY = sys.executable


class UsbPathTests(unittest.TestCase):
    def test_missing_clip_fails_clearly(self):
        missing = R / 'media' / 'does_not_exist.avi'
        with self.assertRaises(RuntimeError) as ctx:
            open_clip(missing)
        self.assertIn('CLIP_OPEN_FAILED', str(ctx.exception))

    def test_fixture_clip_opens(self):
        cap = open_clip(R / 'media' / 'input_synthetic.avi')
        try:
            self.assertTrue(cap.isOpened())
            ok, frame = cap.read()
            self.assertTrue(ok)
            self.assertIsNotNone(frame)
        finally:
            cap.release()

    def test_invalid_camera_index_fails_fast(self):
        started = time.monotonic()
        with self.assertRaises(CameraOpenError) as ctx:
            open_camera(99, timeout_s=3.0)
        elapsed = time.monotonic() - started
        self.assertIn('CAMERA_OPEN_FAILED', str(ctx.exception))
        self.assertIn('SKIPPED_NO_CAMERA', str(ctx.exception))
        self.assertLess(elapsed, 8.0)

    def test_capture_head_camera_cli_exits(self):
        started = time.monotonic()
        proc = subprocess.run(
            [PY, str(R / 'capture_head.py'), '--camera', '99', '--camera-open-timeout-s', '3', '--config', str(R / 'demo_config.json')],
            capture_output=True,
            text=True,
        )
        elapsed = time.monotonic() - started
        self.assertNotEqual(proc.returncode, 0)
        combined = (proc.stdout or '') + (proc.stderr or '')
        self.assertIn('CAMERA_OPEN_FAILED', combined)
        self.assertIn('SKIPPED_NO_CAMERA', combined)
        self.assertLess(elapsed, 10.0)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(UsbPathTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    (R / 'usb_path_verification.json').write_text(json.dumps(dict(
        status='PASS' if result.wasSuccessful() else 'FAIL',
        test_methods=result.testsRun,
        failures=len(result.failures),
        errors=len(result.errors),
        notes='Invalid index 99 must fail fast. Clip fixture must open. No camera required.',
        performance_claim='NONE',
    ), indent=2), encoding='utf-8')
    raise SystemExit(not result.wasSuccessful())
