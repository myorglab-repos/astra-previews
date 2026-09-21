"""Probe USB camera availability. Missing camera is SKIPPED_NO_CAMERA, not FAIL.

Optional gym qualitative stills/film require --head-spotcheck-approved AND a
live face in front of the camera. This agent path does not invent that check.
"""
import argparse
import json
import time
from pathlib import Path

from capture_head import CameraOpenError, open_camera

R = Path(__file__).resolve().parent


def probe_indices(indices, timeout_s):
    attempts = []
    for index in indices:
        started = time.monotonic()
        try:
            cap = open_camera(index, timeout_s=timeout_s)
            cap.release()
            elapsed = time.monotonic() - started
            attempts.append(dict(index=index, status='PRESENT', elapsed_s=round(elapsed, 3)))
            return index, attempts
        except CameraOpenError as exc:
            elapsed = time.monotonic() - started
            attempts.append(dict(
                index=index,
                status='CAMERA_OPEN_FAILED',
                elapsed_s=round(elapsed, 3),
                message=str(exc),
            ))
    return None, attempts


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--indices', default='0,1', help='Comma-separated USB indices to try')
    parser.add_argument('--camera-open-timeout-s', type=float, default=4.0)
    parser.add_argument('--head-spotcheck-approved', action='store_true')
    parser.add_argument('--run-gym', action='store_true', help='Reserved; requires operator-approved live face')
    args = parser.parse_args(argv)
    indices = [int(x) for x in args.indices.split(',') if x.strip() != '']
    found, attempts = probe_indices(indices, args.camera_open_timeout_s)
    if found is None:
        camera = dict(
            status='SKIPPED_NO_CAMERA',
            machine='DESKTOP-P08972I',
            attempts=attempts,
            note='No USB index opened. Packet software path uses --clip. Not a FAIL.',
        )
        gym = dict(
            status='SKIPPED_NO_CAMERA',
            stills=[],
            film=None,
            note='Gym qualitative L/R not run; USB camera absent.',
        )
    else:
        camera = dict(
            status='PRESENT',
            machine='DESKTOP-P08972I',
            opened_index=found,
            attempts=attempts,
            note='Device opened. Qualitative one-face gym still requires operator approval.',
        )
        if args.run_gym and args.head_spotcheck_approved:
            gym = dict(
                status='NOT_RUN_IN_THIS_INVOCATION',
                note='Operator-approved gym capture is a separate capture_head --camera session; this probe only confirms the device.',
            )
        else:
            gym = dict(
                status='SKIPPED_NO_OPERATOR_APPROVAL',
                stills=[],
                film=None,
                opened_index=found,
                note='Camera present but --head-spotcheck-approved/--run-gym not both set. No invented L/R gym media.',
            )
    (R / 'camera_probe.json').write_text(json.dumps(camera, indent=2), encoding='utf-8')
    (R / 'gym_spotcheck.json').write_text(json.dumps(gym, indent=2), encoding='utf-8')
    print(json.dumps(dict(camera=camera['status'], gym=gym['status']), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
