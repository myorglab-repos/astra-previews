# n3-viz-pack-soft-phys-envelope-c01-saf

Track A only. 21 Sep 2026. No spend. No physical actuation.

Teaching films for work that was paper-only or stills-only. Illustration and Workbench renders. The twin is not System ID.

Deep link: this INDEX. Everyday door: `START_HERE.html`.

## Status

**READY_FOR_OLA**

Critical **B-06 stays OPEN**. Critical **C-01 stays OPEN**. Critical **SAF-02 stays OPEN**. Critical **P-05 stays OPEN**. These films do not close them.

## ASSUMPTION (plain sight)

Every number below is a **DESIGN ESTIMATE**, **DESIGN ASSUMPTION**, **HYPOTHESIS**, or an authored review-clock / pixel audit. None of them is a measured force, pressure, FPS, accuracy, or cycle life.

| Item | Label |
|---|---|
| `p_norm` in [0, 1] | ASSUMPTION teaching input. Not measured pressure. |
| `p_norm` = 1 maps to 40 kPa on the Ecoflex example | HYPOTHESIS from the soft-physics paper section 6. Not a setpoint. |
| Ecoflex E 0.118 MPa, Dragon Skin 30 E 1.02 MPa, ratio about 8.6x | DESIGN ESTIMATE from that paper section 1.3. Not a coupon. |
| Textile lambda_max 1.10 | DESIGN ASSUMPTION. Not measured strain. |
| Glove mass 14 oz | ASSUMPTION. Not a product measurement. |
| Return to rest on the cue board | DESIGN ESTIMATE order. Vent may dominate. Not a measured cycle. |
| 12 fps on every film | Authored review clock. Not a measured camera, detector, or machine rate. |
| B-06 block sizes | Drawing aids. Not CAD millimeters. Not measured clearance. |
| C-01 planning lengths in the source paper (~150-250 mm TB-01 bench span; 120-degree-class packing; TB-02 ~252-368 mm or shortened ~200-300 mm; TB-03 ~80-120 mm cuff-to-cuff) | ASSUMPTION / GEOMETRY TARGET hybrid copied from the paper. Soft OD is NOT IN SOURCE. Not product free length. |
| Twin digital watchdog_s = 2.0 | Lead Track A freeze. NOT a measured latency bar or hardware limit. |
| Bright-cyan pixels on yaw renders frame 30 and frame 68 | Pixel audit of this encode: 0. Rule: G>180, B>180, R<100, G+B-2R>200. |

## Media

| Film | Path | Clock |
|---|---|---|
| Soft-physics cues (rest, swell, bend, twist, return) | `media/soft_phys_cues_review.mp4` | 126 frames, 12 fps authored, 10.5 s, 1500x900 |
| Yaw re-encode, slim left root | `media/head_yaw_review_slim_root.mp4` | 144 frames, 12 fps authored, 12 s, 1500x900 |
| Same yaw file in the yaw packet | `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_slim_root.mp4` | copy of the same encode |
| B-06 Option B keep-out | `media/b06_envelope_keepout_review.mp4` | 96 frames, 8 s |
| C-01 coupon board | `media/c01_coupon_geometry_review.mp4` | 96 frames, 8 s |
| SAF-02 / presence-inhibit digital HIL | `media/saf02_presence_inhibit_hil_review.mp4` | 108 frames, 9 s |

Stills sit beside those films in `media/`. Cue contact sheet: `media/cue_contact_sheet.png`.

The previous yaw encode remains `reviews/2026-09-21/n3-head-yaw-live-usb-path/media/head_yaw_review_black_collars.mp4`. It was not overwritten. 2026-09-19 atlas, airflow, and exposed-blind films were not remade.

## What each film is

### A — Soft-physics cues

Source scene `SOFT_PHYS_CUE_SHEET` in `reviews/2026-09-21/n3-head-yaw-live-usb-path/Punching_Bag_N3_Head_Track_Yaw.blend`. Shape keys `Swell_ASSUMPTION`, `Bend_ASSUMPTION`, `Twist_ASSUMPTION`. Sequence: rest, swell (U and F common mode), bend (U1 and F1 ahead of the partner), twist (T1 ahead of T2), return to rest. Workbench. The blend file was not saved.

### B — Slim-root yaw

Same blend, scene `N3_HEAD_TRACK_YAW_BRIDGE`, already slimmed. Re-rendered and re-encoded. Both pedagogy pads use `I1_bag_black`. No mesh uses the retired cyan pad material. Bright-cyan pixel count on the twin renders at frame 30 and frame 68: **0**. Left-root slim stays a visual alignment, not a measured section.

### C — B-06 keep-out

ASSUMPTION illustration of the Option B stack in `docs/engineering/ISMAEL_B06_OPTION_B_ENVELOPE_DEEPEN_v2_2026-09-21.md`: mast/hub, yaw cartridge, pitch pin plate, recessed boot, textile-eye recess, continuum, soft wrist/glove, flex-loop short/mid/tall classes, pinch planes, chafe sleeve **unfrozen**. `pitch_lock_engaged` is the only normative lock bit. No invented millimeters. **B-06 stays Critical OPEN.**

### D — C-01 coupon board

Teaching board from `docs/engineering/ISMAEL_C01_SOFT_COUPON_GEOMETRY_DEEPEN_2026-09-21.md`. TB-01 with a reserved TB-01a port-boss class, TB-02-U first, TB-02-F after U, TB-03 later, TB-04 reuses a host. **No cast. No mold. No PO. C-01 stays Critical OPEN.**

### E — SAF-02 digital HIL

Schematic only, from the Elias SAF-02/P-05 paper and the digital HIL session-enable stub.

`session_enable = user_present AND head_hypothesis_valid AND NOT inhibit_latched`

Presence fault forces absent. E-stop sim latches. Manual reset does not arm and does not start motion. Tag: `SIMULATED_BOOL_NOT_HARDWARE`. **No physical actuation. SAF-02 stays OPEN. P-05 stays OPEN.**

## Open

No PO. Architecture freeze holds. Track A does not prove strike impulse.
