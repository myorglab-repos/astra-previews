# NEXT_PROMPT
status: in_progress
started_at: 2026-09-21 09:40 ET
runner: cursor-cloud-agent
timestamp: 2026-09-21 09:38 ET
pass_id: n3-head-yaw-live-usb-path
from: Ola (Robotics Desk)
prior_completed: n3-head-track-yaw-bridge (ACCEPTED-A digital Track A, 2026-09-21)
authority: Michael 2026-09-21 — keep building everything external of virtual media; external camera may be needed later for gym check but do not wait on camera-in-hand

## Goal
Extend the accepted head→carrier-yaw bridge into a **live-USB-capable path** that still runs CI / packet proof with clip or synthetic fixtures when no camera is present. When a USB camera *is* available on DESKTOP-P08972I, add a qualitative gym spot-check branch (operator-approved one-face prior) — do not invent FPS, accuracy %, IoU, or latency bars.

## Constraints
- DIGITAL_TWIN_ONLY — no physical actuation, no pressurized strike, no claiming System ID.
- Keep ASSUMPTION labels on mapping/sign/gain/clamp/watchdog/idle (demo values from `demo_config.json` remain **TBD — Lead** until explicitly frozen).
- Receiver must continue to **re-derive** enable/yaw; never trust sender yaw/enable.
- Presence remains simulation stub unless Elias papers an authoritative sensor path; label SIM_PRESENCE clearly.
- Normative lock bit stay: `pitch_lock_engaged` (not `pitch_locked`) — not required for digital yaw pedagogy.
- Do **not** close B-06, C-01, SAF-02/P-05, HY-02 as “done product.” HY-02 progress = software path + optional gym qualitative only.
- $0 / no PO. No Stephen spend.
- Packet under `reviews/2026-09-21/n3-head-yaw-live-usb-path/` (or today’s date folder if Astra starts after midnight ET).
- Reuse bridge_core / blender_receiver / capture_head from `reviews/2026-09-21/n3-head-track-yaw-bridge/` — do not fork a second protocol schema without Lead.
- Films are evidence for this pass only; not a remake of virtual media pedagogy packs.

## Accept criteria
1. `--camera N` path opens USB when present; clear fail message when absent (no hang).
2. Clip / synthetic path still produces unit + integration audits PASS (cite real JSON counts; never invent).
3. Packet READY_FOR_OLA + INDEX + SOURCE_BRIEF + DEFECT_REGISTER deltas for HY-02 residual.
4. When camera present and `--head-spotcheck-approved`: qualitative L/R stills + short film with ASSUMPTION strip; bag/mast fixed; idle gates still home_zero.
5. When camera absent: packet still closes software path with clip fixture; gym branch marked SKIPPED_NO_CAMERA (not FAIL).
6. No invented FPS / accuracy / force. Glossary on READY_FOR_OLA for key terms.

## Parallel desks (do not block Astra)
- Ismael: B-06 Option B / no-PO BOM-supplier scout (paper).
- Elias: presence hardware path paper + live camera ICD interface table (paper; no PO).

## Do not
- Remake ACCEPTED-A synthetic-only bridge without deltas.
- Freeze production gain/clamp/sign without Lead.
- Close Critical hardware from this software pass.
- Write ready_for_astra for Soft Blender soft-body unless Lead asks.

## Plain-language
Build the real USB camera hook into the same shoulder-follow demo. If no camera is plugged in, the software packet still proves itself with a file clip. If a camera is there, do a quick human left/right check. Critical bag hardware (root/pitch, coupons, real presence sensor) keeps moving on paper in parallel.

## Plain-language glossary
| Term | Everyday meaning |
|---|---|
| live USB path | Code that can open a real webcam when one is plugged in |
| SKIPPED_NO_CAMERA | Gym check not run because no camera — not a software failure |
| HY-02 | Open item: real camera chase not yet product-closed |
| ASSUMPTION | Working number until Lead freezes it |
| DIGITAL_TWIN_ONLY | Moves the Blender model only — not the physical bag |
