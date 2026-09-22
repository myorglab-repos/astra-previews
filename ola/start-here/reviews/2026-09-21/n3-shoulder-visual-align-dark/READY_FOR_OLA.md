# READY FOR OLA ? n3-shoulder-visual-align-dark

status: dispositioned_accepted_a
timestamp: 2026-09-21 21:05 ET
**Ola final disposition:** ACCEPTED-A
**Track:** A visual only
**Assessment:** `ENGINEERING_ASSESSMENT_N3_SHOULDER_VISUAL_ALIGN_DARK_2026-09-21.md`

Pitch film: PASS. Fresh yaw film PASS after independent full scrub of `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4` (sha256 `9eb85a5b5f809f1fd574943dd965d408841c9f5175b48f9d0b7ab12e571df874`). Thin black collars; no cyan pad body. B-06/C-01/SAF remain OPEN.

## Ask

Accept or send back the shoulder appearance in the pitch pedagogy film and the yaw film that inherits that twin.

Pitch film PASS. Ola final disposition: ACCEPTED-A. Status is dispositioned_accepted_a (2026-09-21 21:05 ET).

## YAW_FILM_RERENDER

`N3_HEAD_TRACK_YAW_BRIDGE` pads `PEDAGOGY_L/R_CONCEPT_PADDED_ROOT.001` are slim collars on existing `I1_bag_black` (Workbench diffuse 0.014, 0.016, 0.018). No mesh still uses `PEDAGOGY_CONCEPT_SOFT_BOOT`.

The corrected composed frames were encoded first to `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4` (144 frames, 1500x900, timeline 12 fps). After the collar scrub passed, that file was copied onto `media/head_yaw_review.mp4` in the usb packet and onto `reviews/2026-09-21/n3-head-track-yaw-bridge/media/head_yaw_review.mp4`. Both copies share sha256 `9eb85a5b5f809f1fd574943dd965d408841c9f5175b48f9d0b7ab12e571df874`. `START_HERE.html` embeds the new filename.

Pitch was not re-rendered. 2026-09-19 baseline films were not touched.

Scrub of the new film against the pad meshes (screen boxes about 36-40 x 38 px, not the old bulb):

| Frame | Side | Film mean RGB | Bright-cyan pixels in the collar box |
|---|---|---|---|
| 30 head left | L | 62, 39, 43 | 0 |
| 30 head left | R | 60, 62, 68 | 0 |
| 68 head right | L | 53, 57, 63 | 0 |
| 68 head right | R | 77, 45, 47 | 0 |
| 114 stale sync | L | 96, 64, 68 | 0 |
| 114 stale sync | R | 86, 60, 65 | 0 |

Those means sit on the dark collar and the arm inside the same small box. The file comment is `YAW_FILM_RERENDER`.

## What Michael locked

Pad body is black, matching the bag. Not cyan, not light gray, not a large sphere. A thin protected cover remains so the pinch story is still visible. Teaching arrows may stay colored.

## What you are looking at

- Before: `before/pitch_short_before.png`, `before/pitch_mid_before.png`, `before/pitch_tall_before.png`, `before/yaw_head_right_before.png`
- After: `after/pitch_short.png`, `after/pitch_mid.png`, `after/pitch_tall.png`, `after/yaw_head_right_after.png`
- Films: pitch `reviews/2026-09-21/n3-b06-pitch-height-pedagogy/media/pitch_height_review.mp4` and yaw `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4`
- Front door: `START_HERE.html` embeds those films and stills

## ASSUMPTION (plain sight)

Color is the twin's existing `I1_bag_black` (Workbench diffuse 0.014, 0.016, 0.018). Collar size is a fallback: 0.076 m outer radius, 0.090 m long, because the sleeve cross-section was not recovered in the pad's local frame. See `INDEX.md`.

## Not in this pass

No new force, FPS, or accuracy numbers. No edit to the 2026-09-19 standoff, AF-01b, reach, or airflow baseline films. B-06 and C-01 stay open. Architecture freeze was not reopened.

## Accept criteria

- [x] Shoulder covers read near-black in pitch short, mid, and tall, and in the re-derived yaw film
- [x] Cover is a short collar, not the previous bulb
- [x] Soft arm, glove, and bag otherwise kept; HUD arrows kept
- [x] Before/after stills in this packet
- [x] No Critical B-06 / C-01 closure claim
