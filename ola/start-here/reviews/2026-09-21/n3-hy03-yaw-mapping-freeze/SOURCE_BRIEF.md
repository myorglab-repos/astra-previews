# Source brief — n3-hy03-yaw-mapping-freeze

| Field | Value |
|---|---|
| pass_id | `n3-hy03-yaw-mapping-freeze` |
| date | 2026-09-21 |
| from | Ola Lead Track A freeze, cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` and `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md` |
| prior | `n3-head-yaw-live-usb-path` ACCEPTED-A, merged as PR #3 onto `main` (`61f96ff`) |
| machine | DESKTOP-P08972I |
| spend | $0 / no PO |

## Goal
Encode Ola’s Lead Track A freeze in config, code, and this packet. Label that must stay visible: **Lead Track A freeze — NOT measured hardware limits / product bars**. NORMATIVE sign text: positive image x → positive world X via +Z yaw from −Y home. Do not invent FPS, accuracy, IoU, or force.

## Inherited (do not remake)
- Protocol `head-yaw-v1`, loopback UDP/JSON, receiver re-derives enable and yaw.
- Live-USB fail-fast and clip CI from `reviews/2026-09-21/n3-head-yaw-live-usb-path/`.
- Elias path language in that packet’s `sources/ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` and `sources/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`, and Ola’s integrate note `sources/OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md`.
- Those papers left gain, sign, and clamp as **TBD — Lead**. This pass is the Lead answer for the **digital twin only**.

## Numbers used
Only the numbers already in the merged demo config. Nothing new was added:

- sign `+1`
- gain_deg_per_signed_x `30.0`
- clamp_deg `30.0`
- watchdog_s `2.0`
- idle_policy `home_zero`
- signed_x `(2*cx-1)` on `frame_fraction_0_to_1`
- unconfigured null gain / clamp / watchdog still deny chase

## HY-02
Office USB webcam is sufficient for the first qualitative L/R check. If a camera opens, run it with `--head-spotcheck-approved`. If no camera opens, record `SKIPPED_NO_CAMERA` and do not call that a software failure. Never invent left/right pictures. HY-02 stays OPEN until that evidence exists.

## Do not
- Close B-06, C-01, or SAF-02.
- Treat Track A yaw as strike-impulse proof.
- Change the architecture freeze (no distal metal, continuum eight-chamber layout stays).
- Spend or open a purchase order.
- Commit `chat_robotic_punching_bag.md`.

## Plain-language glossary
| Term | Everyday meaning |
|---|---|
| Lead freeze | The mapping choice is now locked for the twin instead of left blank |
| ASSUMPTION / DESIGN ESTIMATE | Locked, and still not a measurement |
| home_zero | Straight-ahead when chase is off |
| Critical OPEN | Hardware items that stay open until someone measures real hardware |
