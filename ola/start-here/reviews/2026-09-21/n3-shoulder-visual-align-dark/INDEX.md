# n3-shoulder-visual-align-dark

Track A visual only. 21 Sep 2026. No force, accuracy, or machine-rate claim.

## What changed

Protected-shoulder teaching props in the pitch pedagogy twin, and in the yaw scene copied from it, were oversized blue-gray spheres (`PEDAGOGY_*_CONCEPT_PADDED_ROOT`, material `PEDAGOGY_CONCEPT_SOFT_BOOT`, diffuse 0.18, 0.25, 0.28, about 0.25 × 0.36 × 0.30 m).

They are now thin collars parented to the same pitch roots, using the twin's existing `I1_bag_black` material unchanged.

HUD pitch arrows, white datums, and angle arcs were not recolored.

2026-09-19 standoff, AF-01b, reach, and airflow films were not remade.

## ASSUMPTION

Pad color is the existing material `I1_bag_black`:

- Workbench diffuse RGB 0.014, 0.016, 0.018 (this is the color the bag shows in Workbench)
- Principled base RGB 0.006, 0.007, 0.008

No new finish was invented. Sleeve measurement at the joint did not return a usable cross-section in pad-local space, so the collar radius uses a fallback arm radius of 0.062 m plus a 0.014 m cover (outer 0.076 m), length 0.090 m, rim round 0.010 m.

## Media

| Item | Path |
|---|---|
| Pitch film | `reviews/2026-09-21/n3-b06-pitch-height-pedagogy/media/pitch_height_review.mp4` (376 frames, timeline 12 fps, 1600×900) |
| SHORT / MID / TALL | `pitch_short.png`, `pitch_mid.png`, `pitch_tall.png` (holds at frames 18, 78, 132) |
| Pitch blend | `reviews/2026-09-21/n3-b06-pitch-height-pedagogy/Punching_Bag_N3_Pitch_Height_Pedagogy.blend` (rebuilt from the yaw full-copy; the earlier pedagogy file was missing on disk) |
| Yaw film | `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4` (same bytes also at `media/head_yaw_review.mp4` and the bridge `media/` copy). YAW_FILM_RERENDER. Pitch film was not remade. |
| Yaw blend | `reviews/2026-09-21/n3-head-yaw-live-usb-path/Punching_Bag_N3_Head_Track_Yaw.blend` |
| Before / after | `before/`, `after/` |

The 12 fps figures are the saved Blender timeline, not a measured camera or punch rate.

## Pixel check (pitch side view, frame 145)

| Cover | Pixels that differ from the arm with the cover hidden | Bounding box |
|---|---|---|
| Previous sphere | 4348 | 238 × 102 px |
| New collar | 722 | 48 × 40 px |

Collar pixels are dark (minimum about 16, 16, 16; most under 45). The bag body in the same frame sits near 21, 22, 24. SHORT / MID / TALL cards no longer contain a cyan pad body. Yaw `head_right` pane cyan count on a coarse thumbnail went from 9 to 0.

## Open

B-06 and C-01 stay Critical OPEN. The collar is a conceptual pinch cover, not a hardware release.
