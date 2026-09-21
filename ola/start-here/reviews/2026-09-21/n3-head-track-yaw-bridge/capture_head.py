"""OpenCV clip/USB -> detected face centroid -> local-only twin packets.

No webcam media recording. JSON logs are opt-in. Presence is a simulation stub.
"""
import argparse
import json
import socket
import time
import uuid
from pathlib import Path
import cv2
from bridge_core import derive, validate_config


def detect(frame, cascade):
    # ASSUMPTION: OpenCV default Haar parameters, not an accuracy/confidence bar.
    boxes = cascade.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    # ASSUMPTION: ambiguous multiple faces => invalid; no identity tracking.
    box = [int(x) for x in boxes[0]] if len(boxes) == 1 else None
    cx = (box[0]+box[2]/2)/frame.shape[1] if box else None
    return box, cx, len(boxes)


def main():
    a = argparse.ArgumentParser(description=__doc__)
    inp = a.add_mutually_exclusive_group(required=True)
    inp.add_argument('--clip', type=Path)
    inp.add_argument('--camera', type=int)
    a.add_argument('--config', type=Path, default=Path(__file__).with_name('config_template.json'))
    a.add_argument('--timeline', type=Path, help='Explicit simulated presence/fault rows, indexed by frame')
    a.add_argument('--sim-present', action='store_true', help='ASSUMPTION: simulated presence, not a sensor')
    a.add_argument('--head-spotcheck-approved', action='store_true', help='Operator enables qualitative one-face prior')
    a.add_argument('--send', action='store_true')
    a.add_argument('--wait-ack', action='store_true', help='Offline digital integration test only; not live timing evidence')
    a.add_argument('--log', type=Path, help='Opt-in local JSONL (no webcam media)')
    a.add_argument('--preview', action='store_true')
    args = a.parse_args()
    if args.wait_ack and (not args.send or args.camera is not None):
        a.error('--wait-ack requires --send and --clip')
    config = validate_config(json.loads(args.config.read_text(encoding='utf-8-sig')))
    timeline = json.loads(args.timeline.read_text()) if args.timeline else None
    cap = cv2.VideoCapture(str(args.clip) if args.clip else args.camera)
    if not cap.isOpened(): raise RuntimeError('Capture could not open')
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    if cascade.empty(): raise RuntimeError('Haar model missing')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(20)  # test harness wait only; not receiver timing requirement
    stream = str(uuid.uuid4())
    log = args.log.open('w', encoding='utf-8') if args.log else None
    start = time.monotonic()
    fps = cap.get(cv2.CAP_PROP_FPS) if args.clip else None
    if args.clip and (not fps or fps <= 0): raise RuntimeError('Clip timebase unavailable')
    seq = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok: break
            box, cx, count = detect(frame, cascade)
            stim = timeline[seq] if timeline is not None and seq < len(timeline) else {}
            p = dict(schema_rev='head-yaw-v1', scope='DIGITAL_TWIN_ONLY', stream_id=stream, seq=seq,
                     episode_id='synthetic-head-roi-v1' if timeline else stream,
                     t_sync=seq/fps if args.clip else time.monotonic()-start,
                     sync_quality=stim.get('sync_quality', 'ok'),
                     user_present=stim.get('user_present', args.sim_present),
                     presence_sensor_fault=stim.get('presence_sensor_fault', False),
                     inhibit_latched=stim.get('inhibit_latched', False),
                     e_stop_asserted=stim.get('e_stop_asserted', False),
                     head_hypothesis_valid=box is not None and args.head_spotcheck_approved,
                     head_centroid_x=cx, head_hypothesis=dict(bbox=box, confidence=None),
                     face_candidates=count, stimulus=stim.get('case', 'camera_or_clip'),
                     presence_source='SIMULATED_BOOL_NOT_HARDWARE',
                     head_validity_rule='ASSUMPTION_one_face_plus_operator_spotcheck',
                     source_kind='synthetic_translated_still_clip' if timeline else 'clip' if args.clip else 'USB_camera',
                     recording_enabled=False, privacy_mode='local_default', media_uri=None)
            p.update(derive(p, config))
            if args.clip and args.send and not args.wait_ack:
                time.sleep(max(0, start+seq/fps-time.monotonic()))
            p['sent_monotonic_s'] = time.monotonic()
            if args.send:
                sock.sendto(json.dumps(p, allow_nan=False).encode(), (config['host'], config['port']))
                if args.wait_ack:
                    ack = json.loads(sock.recvfrom(65535)[0])
                    if ack.get('seq') != seq or not ack.get('accepted'): raise RuntimeError('Receiver rejected frame')
            if log:
                log.write(json.dumps(p, allow_nan=False)+'\n'); log.flush()
            if args.preview:
                if box:
                    x,y,w,h = box; cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                cv2.putText(frame, 'SIM presence | DIGITAL TWIN ONLY', (10,24), cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,255),2)
                cv2.imshow('Head prior - q exits',frame)
                if cv2.waitKey(1)&255 == ord('q'): break
            seq += 1
    finally:
        # No last-command hold after normal EOF/exit. Crash handled by receiver watchdog.
        stop = dict(schema_rev='head-yaw-v1', scope='DIGITAL_TWIN_ONLY', stream_id=stream, seq=seq,
                    t_sync=0.0, sync_quality='ok', user_present=False, head_hypothesis_valid=False,
                    presence_sensor_fault=False, inhibit_latched=False, e_stop_asserted=False,
                    head_centroid_x=None, sent_monotonic_s=time.monotonic())
        if args.send: sock.sendto(json.dumps(stop).encode(), (config['host'],config['port']))
        cap.release(); sock.close()
        if log: log.close()
        if args.preview: cv2.destroyAllWindows()
    print(json.dumps(dict(processed_frames=seq,opencv=cv2.__version__,performance_claim='NONE')))


if __name__ == '__main__': main()
