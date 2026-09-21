"""OpenCV clip/USB -> detected face centroid -> local-only twin packets.

Same UDP/JSON schema as n3-head-track-yaw-bridge (head-yaw-v1). No second protocol.

Lead Track A freeze — NOT measured hardware limits / product bars.
Cite docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md
and docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md.
NORMATIVE sign: positive image x → positive world X via +Z yaw from −Y home.
Default config is config_template.json (sign=+1, gain 30.0, clamp 30.0,
idle home_zero, watchdog 2.0). Null gain/clamp/watchdog still deny chase.
Not a measured FPS, accuracy, force, or hardware limit.

Operator flags
--------------
--clip PATH
    CI / packet fixture path. Required when no USB camera is present.
--camera N
    Live USB device index. Fails immediately with CAMERA_OPEN_FAILED if the
    index cannot open; does not hang the process.
--camera-open-timeout-s SEC
    Upper bound for USB open + first grab (default 5 s).
--head-spotcheck-approved
    Operator attests a qualitative one-face prior for this scene. Without it,
    head_hypothesis_valid stays false (chase idles).
--sim-present
    ASSUMPTION: simulated presence boolean. NOT a ToF/PIR/mat sensor.
    Without this flag or a --timeline, user_present defaults absent.

No webcam media recording. JSON logs are opt-in. Presence is a simulation stub.
"""
import argparse
import json
import socket
import sys
import threading
import time
import uuid
from pathlib import Path

import cv2

from bridge_core import derive, validate_config

CAMERA_OPEN_TIMEOUT_S = 5.0


class CameraOpenError(RuntimeError):
    """USB index missing, busy, or timed out. Not a clip/CI failure.

    Residual token SKIPPED_NO_CAMERA is normative (Lead 2026-09-21):
    missing VideoCapture must not fail the software packet.
    """
    residual_token = 'SKIPPED_NO_CAMERA'

    def __init__(self, message):
        if 'SKIPPED_NO_CAMERA' not in message:
            message = f'{message} Residual token SKIPPED_NO_CAMERA (not a software-packet FAIL).'
        super().__init__(message)


def detect(frame, cascade):
    # ASSUMPTION: OpenCV default Haar parameters, not an accuracy/confidence bar.
    boxes = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    # ASSUMPTION: ambiguous multiple faces => invalid; no identity tracking.
    box = [int(x) for x in boxes[0]] if len(boxes) == 1 else None
    cx = (box[0] + box[2] / 2) / frame.shape[1] if box else None
    return box, cx, len(boxes)


def camera_backend():
    return cv2.CAP_DSHOW if sys.platform.startswith('win') else cv2.CAP_ANY


def open_camera(index, timeout_s=CAMERA_OPEN_TIMEOUT_S):
    """Open USB index with a hard timeout. Never block the caller indefinitely."""
    if type(index) is not int or index < 0:
        raise CameraOpenError(
            f'CAMERA_OPEN_FAILED: invalid camera index {index!r}. '
            'Use a non-negative integer or --clip for the fixture path.'
        )
    timeout_s = float(timeout_s)
    if not (0.2 <= timeout_s <= 30):
        raise CameraOpenError('CAMERA_OPEN_FAILED: --camera-open-timeout-s must be 0.2–30')
    backend = camera_backend()
    result = {}

    def worker():
        cap = None
        try:
            cap = cv2.VideoCapture(index, backend)
            try:
                cap.set(cv2.CAP_PROP_OPEN_TIMEOUT_MSEC, int(timeout_s * 1000))
            except Exception:
                pass
            if not cap.isOpened():
                result['error'] = 'not_opened'
                if cap is not None:
                    cap.release()
                return
            try:
                cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
            except Exception:
                pass
            ok = cap.grab()
            if not ok:
                cap.release()
                result['error'] = 'no_frame'
                return
            result['cap'] = cap
        except Exception as exc:
            if cap is not None:
                try:
                    cap.release()
                except Exception:
                    pass
            result['error'] = str(exc)

    thread = threading.Thread(target=worker, daemon=True, name=f'opencv-open-cam{index}')
    thread.start()
    thread.join(timeout_s)
    if thread.is_alive():
        raise CameraOpenError(
            f'CAMERA_OPEN_FAILED: index {index} did not open within {timeout_s:.1f}s '
            f'(backend={backend}). Process exits; no hang. Check device, index, and '
            'OS camera privacy. CI/packet path: use --clip. Gym qualitative is '
            'SKIPPED_NO_CAMERA, not FAIL.'
        )
    if 'cap' in result:
        return result['cap']
    raise CameraOpenError(
        f'CAMERA_OPEN_FAILED: index {index} cannot open '
        f'({result.get("error", "unknown")}). USB camera absent, busy, or wrong index. '
        'Use --clip for CI/fixture proof. Gym qualitative is SKIPPED_NO_CAMERA, not FAIL.'
    )


def open_clip(path):
    path = Path(path)
    if not path.is_file():
        raise RuntimeError(f'CLIP_OPEN_FAILED: file not found: {path}')
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise RuntimeError(f'CLIP_OPEN_FAILED: could not open readable video: {path}')
    return cap


def open_capture(args):
    if args.clip is not None:
        return open_clip(args.clip)
    return open_camera(args.camera, timeout_s=args.camera_open_timeout_s)


def build_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    inp = parser.add_mutually_exclusive_group(required=True)
    inp.add_argument('--clip', type=Path, help='Synthetic/recorded fixture (CI default)')
    inp.add_argument('--camera', type=int, help='USB camera index; fail-fast if unusable')
    parser.add_argument('--config', type=Path, default=Path(__file__).with_name('config_template.json'))
    parser.add_argument('--timeline', type=Path, help='Explicit simulated presence/fault rows, indexed by frame')
    parser.add_argument(
        '--sim-present',
        action='store_true',
        help='ASSUMPTION: simulated presence, not a hardware sensor',
    )
    parser.add_argument(
        '--head-spotcheck-approved',
        action='store_true',
        help='Operator enables qualitative one-face prior for this scene',
    )
    parser.add_argument('--send', action='store_true')
    parser.add_argument('--wait-ack', action='store_true', help='Offline digital integration test only; not live timing evidence')
    parser.add_argument('--log', type=Path, help='Opt-in local JSONL (no webcam media)')
    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--max-frames', type=int, default=0, help='Stop after N frames (0 = until EOF / operator quit)')
    parser.add_argument(
        '--camera-open-timeout-s',
        type=float,
        default=CAMERA_OPEN_TIMEOUT_S,
        help='USB open timeout seconds (default 5; process exits on expiry)',
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.wait_ack and (not args.send or args.camera is not None):
        parser.error('--wait-ack requires --send and --clip')
    if args.max_frames < 0:
        parser.error('--max-frames must be >= 0')
    config = validate_config(json.loads(args.config.read_text(encoding='utf-8-sig')))
    timeline = json.loads(args.timeline.read_text()) if args.timeline else None
    try:
        cap = open_capture(args)
    except CameraOpenError as exc:
        print(json.dumps(dict(
            residual='SKIPPED_NO_CAMERA',
            error='CAMERA_OPEN_FAILED',
            packet_fail=False,
            message=str(exc),
            performance_claim='NONE',
        )), file=sys.stderr)
        raise SystemExit(2) from exc
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if cascade.empty():
        cap.release()
        raise RuntimeError('Haar model missing')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(20)  # test harness wait only; not receiver timing requirement
    stream = str(uuid.uuid4())
    log = args.log.open('w', encoding='utf-8') if args.log else None
    start = time.monotonic()
    fps = cap.get(cv2.CAP_PROP_FPS) if args.clip else None
    if args.clip and (not fps or fps <= 0):
        cap.release()
        raise RuntimeError('Clip timebase unavailable')
    seq = 0
    try:
        while True:
            if args.max_frames and seq >= args.max_frames:
                break
            ok, frame = cap.read()
            if not ok:
                break
            box, cx, count = detect(frame, cascade)
            stim = timeline[seq] if timeline is not None and seq < len(timeline) else {}
            p = dict(
                schema_rev='head-yaw-v1',
                scope='DIGITAL_TWIN_ONLY',
                stream_id=stream,
                seq=seq,
                episode_id='synthetic-head-roi-v1' if timeline else stream,
                t_sync=seq / fps if args.clip else time.monotonic() - start,
                sync_quality=stim.get('sync_quality', 'ok'),
                user_present=stim.get('user_present', args.sim_present),
                presence_sensor_fault=stim.get('presence_sensor_fault', False),
                inhibit_latched=stim.get('inhibit_latched', False),
                e_stop_asserted=stim.get('e_stop_asserted', False),
                head_hypothesis_valid=box is not None and args.head_spotcheck_approved,
                head_centroid_x=cx,
                head_hypothesis=dict(bbox=box, confidence=None),
                face_candidates=count,
                stimulus=stim.get('case', 'camera_or_clip'),
                presence_source='SIMULATED_BOOL_NOT_HARDWARE',
                head_validity_rule='ASSUMPTION_one_face_plus_operator_spotcheck',
                source_kind='synthetic_translated_still_clip' if timeline else 'clip' if args.clip else 'USB_camera',
                recording_enabled=False,
                privacy_mode='local_default',
                media_uri=None,
            )
            p.update(derive(p, config))
            if args.clip and args.send and not args.wait_ack:
                time.sleep(max(0, start + seq / fps - time.monotonic()))
            p['sent_monotonic_s'] = time.monotonic()
            if args.send:
                sock.sendto(json.dumps(p, allow_nan=False).encode(), (config['host'], config['port']))
                if args.wait_ack:
                    ack = json.loads(sock.recvfrom(65535)[0])
                    if ack.get('seq') != seq or not ack.get('accepted'):
                        raise RuntimeError('Receiver rejected frame')
            if log:
                log.write(json.dumps(p, allow_nan=False) + '\n')
                log.flush()
            if args.preview:
                if box:
                    x, y, w, h = box
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(frame, 'SIM presence | DIGITAL TWIN ONLY', (10, 24), cv2.FONT_HERSHEY_SIMPLEX, .6, (0, 255, 255), 2)
                cv2.imshow('Head prior - q exits', frame)
                if cv2.waitKey(1) & 255 == ord('q'):
                    break
            seq += 1
    finally:
        # No last-command hold after normal EOF/exit. Crash handled by receiver watchdog.
        stop = dict(
            schema_rev='head-yaw-v1',
            scope='DIGITAL_TWIN_ONLY',
            stream_id=stream,
            seq=seq,
            t_sync=0.0,
            sync_quality='ok',
            user_present=False,
            head_hypothesis_valid=False,
            presence_sensor_fault=False,
            inhibit_latched=False,
            e_stop_asserted=False,
            head_centroid_x=None,
            sent_monotonic_s=time.monotonic(),
        )
        if args.send:
            sock.sendto(json.dumps(stop).encode(), (config['host'], config['port']))
        cap.release()
        sock.close()
        if log:
            log.close()
        if args.preview:
            cv2.destroyAllWindows()
    print(json.dumps(dict(processed_frames=seq, opencv=cv2.__version__, performance_claim='NONE')))


if __name__ == '__main__':
    main()
