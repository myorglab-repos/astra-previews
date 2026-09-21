"""HY-02 qualitative gym branch on this machine.

Michael approval 2026-09-21 authorizes --head-spotcheck-approved when a USB
camera opens. Missing camera is SKIPPED_NO_CAMERA, not FAIL.

This script never draws a face, never copies a fixture still into the gym
folder, and never labels a frame left or right unless that frame's measured
centroid says so. No FPS, accuracy, or force claim.
"""
import json
import platform
import time
from pathlib import Path

from capture_head import CameraOpenError, detect, open_camera
import cv2

from bridge_core import derive

R = Path(__file__).resolve().parent
CONFIG = json.loads((R / 'frozen_config.json').read_text(encoding='utf-8'))
MEDIA = R / 'gym_media'


def probe(indices, timeout_s):
    attempts = []
    for index in indices:
        started = time.monotonic()
        try:
            cap = open_camera(index, timeout_s=timeout_s)
            cap.release()
            attempts.append(dict(index=index, status='PRESENT', elapsed_s=round(time.monotonic() - started, 3)))
            return index, attempts
        except CameraOpenError as exc:
            attempts.append(dict(
                index=index,
                status='CAMERA_OPEN_FAILED',
                elapsed_s=round(time.monotonic() - started, 3),
                message=str(exc),
            ))
    return None, attempts


def side_name(centroid_x):
    if centroid_x < 0.4:
        return 'left'
    if centroid_x > 0.6:
        return 'right'
    return 'center'


def observe(index, max_frames, wall_s):
    """Grab live frames. Save a still only when Haar reports exactly one face."""
    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    if cascade.empty():
        raise RuntimeError('Haar model missing')
    cap = open_camera(index, timeout_s=4.0)
    samples = []
    saved = {name: None for name in ('left', 'center', 'right')}
    start = time.monotonic()
    seq = 0
    try:
        while seq < max_frames and (time.monotonic() - start) < wall_s:
            ok, frame = cap.read()
            if not ok or frame is None:
                break
            box, cx, count = detect(frame, cascade)
            sample = dict(seq=seq, face_candidates=count, head_centroid_x=cx, saved=None)
            if box is not None and cx is not None:
                yaw = derive(dict(
                    schema_rev='head-yaw-v1', scope='DIGITAL_TWIN_ONLY', t_sync=0.0,
                    sync_quality='ok', user_present=True, head_hypothesis_valid=True,
                    presence_sensor_fault=False, inhibit_latched=False, e_stop_asserted=False,
                    head_centroid_x=cx,
                ), CONFIG)['yaw_cmd']
                sample['yaw_cmd_deg_design_estimate'] = yaw
                name = side_name(cx)
                sample['observed_side'] = name
                if saved[name] is None:
                    MEDIA.mkdir(exist_ok=True)
                    canvas = frame.copy()
                    x, y, w, h = box
                    cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 255), 2)
                    cv2.putText(
                        canvas,
                        'ASSUMPTION / DESIGN ESTIMATE | DIGITAL_TWIN_ONLY',
                        (8, 24), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2,
                    )
                    cv2.putText(
                        canvas,
                        f'HY-03 frozen sign+1  observed {name}  yaw {yaw:.1f} deg',
                        (8, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 2,
                    )
                    path = MEDIA / f'observed_{name}.png'
                    if cv2.imwrite(str(path), canvas):
                        saved[name] = str(path.relative_to(R)).replace('\\', '/')
                        sample['saved'] = saved[name]
            samples.append(sample)
            seq += 1
    finally:
        cap.release()
    return samples, {k: v for k, v in saved.items() if v}


def main():
    machine = platform.node()
    found, attempts = probe([0, 1], 4.0)
    if found is None:
        camera = dict(
            status='SKIPPED_NO_CAMERA',
            machine=machine,
            attempts=attempts,
            note='No USB index opened. SKIPPED_NO_CAMERA is not a software FAIL. No gym media written.',
        )
        gym = dict(
            status='SKIPPED_NO_CAMERA',
            stills=[],
            film=None,
            head_spotcheck_approved=False,
            office_usb_webcam_sufficient=True,
            lead_disposition='docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md',
            note='Office USB webcam is sufficient for the first qualitative L/R check. None opened, so this is SKIPPED_NO_CAMERA, not FAIL. HY-02 stays OPEN.',
            performance_claim='NONE',
        )
    else:
        camera = dict(
            status='PRESENT',
            machine=machine,
            opened_index=found,
            attempts=attempts,
            note='Office USB webcam opened. It is sufficient for the first qualitative L/R check. Frames below are from this open only.',
        )
        samples, saved = observe(found, max_frames=24, wall_s=4.0)
        single = [s for s in samples if s.get('face_candidates') == 1]
        left = [s for s in single if s.get('observed_side') == 'left']
        right = [s for s in single if s.get('observed_side') == 'right']
        if not single:
            status = 'CAMERA_PRESENT_NO_SINGLE_FACE'
            note = (
                'Camera opened and --head-spotcheck-approved was authorized, '
                'but this grab did not see exactly one face. No L/R stills invented. HY-02 stays OPEN.'
            )
        elif left and right:
            status = 'QUALITATIVE_LR_OBSERVED'
            note = (
                'Live frames contained one face on both sides of the frame. '
                'Stills are those frames. This is not a product CV close. HY-02 stays OPEN.'
            )
        else:
            status = 'QUALITATIVE_PARTIAL_FACE'
            note = (
                'Live frames contained one face, but not both a left and a right observation. '
                'Only observed stills are saved. HY-02 stays OPEN.'
            )
        gym = dict(
            status=status,
            authority='Michael 2026-09-21 head-spotcheck-approved; office USB webcam sufficient per Ola integrate',
            lead_disposition='docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md',
            elias_support='docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md',
            office_usb_webcam_sufficient=True,
            head_spotcheck_approved=True,
            sim_presence='SIMULATED_BOOL_NOT_HARDWARE',
            frames_grabbed=len(samples),
            single_face_frames=len(single),
            left_frames=len(left),
            right_frames=len(right),
            stills=list(saved.values()),
            film=None,
            note=note,
            performance_claim='NONE',
            mapping_label='Lead Track A freeze — NOT measured hardware limits / product bars',
        )
        (R / 'gym_samples.json').write_text(json.dumps(samples, indent=2) + '\n', encoding='utf-8')
    (R / 'camera_probe.json').write_text(json.dumps(camera, indent=2) + '\n', encoding='utf-8')
    (R / 'gym_spotcheck.json').write_text(json.dumps(gym, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(camera=camera['status'], gym=gym['status'], machine=machine), indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
