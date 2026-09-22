# n3-soft-physics-twin-hooks-shoulder-root

Track A only. 21 Sep 2026. No spend. No measured pressure, strain, force, or cycle life.

## What shipped

1. **Soft-physics hooks** from `docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` section 6, as named Blender objects and drivers in `Punching_Bag_N3_Head_Track_Yaw.blend`.
2. **Left shoulder-root silhouette** on the yaw twin pulled toward the right-side thin `I1_bag_black` collar. The right arm and the cyan pads were not restored.

2026-09-19 baseline films were not remade. The full yaw mp4 was not re-encoded. Proof is the stills and the cue contact sheet.

## ASSUMPTION (plain sight)

Every numeric hook is a **DESIGN ESTIMATE**, **DESIGN ASSUMPTION**, or **HYPOTHESIS** copied from the paper and tagged on `SOFT_PHYS_CARD`. The twin is not System ID. Recalibrate when TB-01…04 exist.

| Hook | Tag on the object |
|---|---|
| `p_norm` in [0, 1] per chamber | ASSUMPTION teaching input. Not measured pressure. |
| `p_norm` = 1 maps to 40 kPa on the Ecoflex example | HYPOTHESIS editable constant from paper §6. Not a setpoint. |
| Ecoflex E 0.118 MPa, Dragon Skin 30 E 1.02 MPa, ratio ~8.6× | DESIGN ESTIMATE from paper §1.3. Not a coupon. |
| Textile λ_max 1.10 | DESIGN ASSUMPTION. Not measured strain. |
| Glove mass 14 oz | ASSUMPTION. Not a product measurement. |
| Return panel back at rest | DESIGN ESTIMATE order from paper §4.4. Not a measured cycle. Vent may dominate. |

Teaching order on the cue board: rest → swell (common mode) → bend (U1 or F1 ahead of its partner) → twist (T1 ahead of T2) → return to rest.

Product bladders are not a soft-body solve. B-06 and C-01 stay Critical OPEN.

## Shoulder root

The left root centerline was pulled toward the left collar axis, and the proximal tube cross-section was thinned. Slice centers of the distal path stay put. The left glove world translation did not move (still −0.209, −0.390, 1.500). The right arm was not edited.

Collar material on both pads remains `I1_bag_black` (Workbench diffuse 0.014, 0.016, 0.018). No mesh uses `PEDAGOGY_CONCEPT_SOFT_BOOT`. Bright-cyan pixels in the frame-30 and frame-68 stills: 0.

Isolated-arm root chord (top of the silhouette, median width):

| Frame | Side | Before | After |
|---|---|---|---|
| 68 head right | Left | 79 px | 67 px |
| 68 head right | Right | 40 px | 40 px |
| 30 head left | Left | 44 px | 33 px |
| 30 head left | Right | 81 px | 81 px |

At head-right the left root is the wide face. It got narrower. It is still wider than the right edge-on collar, because that yaw pose lays the left arm across the camera. The right thin collar was the reference and was left alone.

## Media

| Item | Path |
|---|---|
| L/R before-after | `after/lr_compare.png` |
| Yaw stills | `before/yaw_f030.png`, `before/yaw_f068.png`, `after/yaw_f030.png`, `after/yaw_f068.png` |
| Cue contact sheet | `cues/contact_sheet.png` |
| Blend | `reviews/2026-09-21/n3-head-yaw-live-usb-path/Punching_Bag_N3_Head_Track_Yaw.blend` |

## Named objects

Collection `SOFT_PHYSICS_TWIN_HOOKS` in scene `N3_HEAD_TRACK_YAW_BRIDGE`:

- `SOFT_PHYS_CARD`
- `SOFT_PHYS_{L|R}_{U1,U2,U3,F1,F2,F3,T1,T2}` parented to the matching `M1_chamber` object

Scene `SOFT_PHYS_CUE_SHEET` (not in the product camera):

- `SOFT_PHYS_CUE_{L|R}_{U|F|T}` with shape keys `Swell_ASSUMPTION`, `Bend_ASSUMPTION`, `Twist_ASSUMPTION`
- Swell driver: max of that section's `p_norm`
- Bend or twist driver: first chamber minus its partner

## Open

B-06 and C-01 stay Critical OPEN. This pass does not close Track B, does not authorize a PO, and does not claim System ID.
