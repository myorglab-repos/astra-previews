# Note — shoulder visual align

The pedagogy blend `Punching_Bag_N3_Pitch_Height_Pedagogy.blend` was not on disk. The yaw blend is a full copy of that file and still contained scene `N3_PITCH_HEIGHT_PEDAGOGY`, so the correction was applied there and both blend paths were saved.

Objects edited, and only these:

- `PEDAGOGY_L_CONCEPT_PADDED_ROOT` and `PEDAGOGY_R_CONCEPT_PADDED_ROOT` in `N3_PITCH_HEIGHT_PEDAGOGY`
- The `.001` copies of those two objects in `N3_HEAD_TRACK_YAW_BRIDGE`

Each mesh was replaced with a rounded open band and assigned the existing material `I1_bag_black`. That material was not modified, so bag and sleeve colors in the inherited 2026-09-19 scenes stay as they were.

Script: `slim_black_pads.py`. Record: `pad_edit.json`.

## YAW_FILM_RERENDER

Ola passed the pitch film and first failed `head_yaw_review.mp4` (bright cyan bulbs still in the movie; after stills looked corrected). Final disposition of the corrected yaw film is ACCEPTED-A (2026-09-21 21:05 ET). See `READY_FOR_OLA.md`.

The yaw scene was already slim `I1_bag_black` collars. Frames 1–144 were rendered again from `N3_HEAD_TRACK_YAW_BRIDGE` and the usb-path film was encoded again from those frames. Collar boxes in the new film are about 36–40 × 38 px with no bright-cyan pixels. Pitch was not remade. 2026-09-19 baselines were not touched. Bridge `render_frames` and `composed_frames` were refreshed from the same render. The bridge packet has no separate mp4.
