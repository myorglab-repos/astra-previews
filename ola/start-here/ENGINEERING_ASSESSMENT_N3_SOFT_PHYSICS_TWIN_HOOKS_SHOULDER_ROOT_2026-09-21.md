# ENGINEERING ASSESSMENT — n3-soft-physics-twin-hooks-shoulder-root

**Date:** 2026-09-21
**Disposition:** **ACCEPTED-A** — Track A visual / teaching twin only
**Pass:** `reviews/2026-09-21/n3-soft-physics-twin-hooks-shoulder-root/`
**PR:** https://github.com/myorglab-repos/robotic-punching-bag/pull/7

## Summary

Ola ACCEPTED-A this Track A packet after an independent still review. Named chamber hooks and a cue board carry the soft-arm paper as teaching labels. The left yaw-root silhouette is slimmer. The right collar is unchanged. No spend. The twin is not System ID. Critical B-06 and C-01 stay OPEN.

## Findings

- Bright-cyan pixel count on `after/yaw_f030.png`, `after/yaw_f068.png`, and `after/lr_compare.png`: **0**. Threshold: G>180, B>180, R<100, and G+B−2R>200.
- Isolated-arm silhouette chord (alpha mask, top 28 rows of the bbox): frame 68 left 80→67 px; frame 30 left 45→34 px; frame 68 right 41→41 px; frame 30 right 83→83 px.
- Visual: left root slimmed; right unchanged; collars remain `I1_bag_black`; cue board is ASSUMPTION-labeled rest / swell / bend / twist.
- Low: `hook_report.json` `root_chord_before` / `root_chord_after` are nearly identical (stale). The silhouettes and `INDEX.md` are authoritative.
- Low residual: the full yaw mp4 was not re-encoded.
- Critical B-06 and C-01 stay OPEN. No spend. Twin is not System ID. No measured pressure, strain, force, or cycle life.

## Engineering recommendations

None for hardware. Optional $0 follow-up: re-encode the yaw film so it matches the slim stills. Do not open spend for that. Recalibrate hook constants only when coupons exist. Do not treat the cue board as a measured cycle.

## Test / validation gaps

B-06 and C-01 remain Critical OPEN. The yaw film on the front door is the pre-slim encode. `hook_report.json` chord blocks are stale relative to the silhouettes.

## Manufacturing notes

None. Collar and cue sizes are conceptual. No manufacturing release. No purchase.

## Open questions for Michael

None blocking this visual accept. Waiting on Michael only for spend, or for HY-02 when a face is in the camera region of interest.

## Plain-language glossary

| Term | Meaning |
|---|---|
| ACCEPTED-A | Ola accepts this visual teaching pass. It is not a product certificate. |
| ASSUMPTION | A labeled teaching guess from the design paper, not a lab measurement. |
| Track A | The on-screen twin only. |
| System ID | A measured model of the real arm. This twin is not that. |
| B-06 | Shoulder hardware question. Still open. |
| C-01 | Soft-arm proof question. Still open. |
| `I1_bag_black` | The thin black collar material. Cyan pads stay retired. |
| HY-02 | A real webcam check with one face in frame. Still waiting on Michael. |

*Ola — 2026-09-21. Desks → Ola → Eta.*
