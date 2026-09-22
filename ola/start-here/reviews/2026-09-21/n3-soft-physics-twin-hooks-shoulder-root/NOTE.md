# Note

The yaw blend `reviews/2026-09-21/n3-head-yaw-live-usb-path/Punching_Bag_N3_Head_Track_Yaw.blend` was edited. The pitch blend file on disk was not saved over. 2026-09-19 baselines were not opened.

## Soft-physics hooks

`apply_twin_hooks.py` adds collection `SOFT_PHYSICS_TWIN_HOOKS` and scene `SOFT_PHYS_CUE_SHEET`. Sixteen empties follow the existing chamber objects (`M1_chamber` L/R × U1–U3, F1–F3, T1–T2). Cue meshes are amber teaching shapes, material `SOFT_PHYS_CUE_AMBER`. They are not in the product camera.

`rerender_cues.py` frames the board from the side. The contact sheet is `cues/contact_sheet.png`.

## Left root

`slim_rings.py` thins proximal left-arm tube rings toward their own centerline. `align_root.py` then pulls the left root centerline toward the pedagogy collar's local Y. The right arm is not in either edit. `I1_bag_black` is not modified.

The full yaw review mp4 still shows the pre-slim frames. The proof stills are in `before/` and `after/`.
