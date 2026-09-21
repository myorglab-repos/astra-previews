# NEXT_PROMPT
status: in_progress
started_at: 2026-09-21 08:01 ET
runner: codex-cli
timestamp: 2026-09-21
pass_id: n3-head-track-yaw-bridge
from: Ola (Robotics Desk)
source: ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md ACCEPTED-A + Michael correction (head track → carrier yaw)

## Goal
Implement a **Track A digital twin bridge**: camera (live USB or recorded clip) → head bbox/centroid → **carrier yaw** on the N3 Blender twin. Presence = on-switch; head drives aim yaw. Follow `docs/engineering/ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md`.

### In scope
1. Python path: OpenCV/MediaPipe-class head/face prior → normalized `head_centroid_x` → `yaw_cmd` (tunable gain/clamp — **ASSUMPTION/TBD placeholders**, no fake accuracy claims).
2. Blender receiver: UDP/JSON (or file/OSC) → drive **carrier yaw** joint/object on accepted N3 twin (start from AF-01b-2 / pitch pedagogy successor as needed).
3. Presence gate stub: if `user_present` false (or sim flag), yaw to idle/home — do not invent ToF hardware.
4. Demo: recorded clip OR webcam → visible twin yaw follow; packet with scripts, README, short film/stills, READY_FOR_OLA.
5. Label every assumption per Michael standing rule.

### Constraints
- Architecture freeze; Track A ≠ strike impulse; no physical actuation; no invented FPS/accuracy.
- Do not close B-06/C-01; do not overwrite Soft physics docs.
- Packet under `reviews/2026-09-21/n3-head-track-yaw-bridge/` (or dated folder).

### Accept criteria
- [ ] Head move L/R in frame → twin carrier yaw follows (demo film/stills)
- [ ] Absent/invalid head → safe idle behavior documented
- [ ] Assumptions labeled; READY_FOR_OLA + glossary

### Out of scope
PO, real E-stop hardware, full pose athletics CV, Soft FEA numbers as System ID

## Plain-language
Hook a camera to the Blender bag so when a person’s head moves left/right, the shoulders turn to follow.

