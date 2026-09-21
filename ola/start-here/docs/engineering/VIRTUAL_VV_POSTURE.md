# Virtual V&V posture (Lead) — after Michael 2026-09-21 correction

**Status:** EXECUTE — maximize physics + camera-in-the-loop before buy  
**Does not replace** eventual TB coupons for manufacturing release — but **does** authorize design-estimate math and head-track→yaw now.

## CV (simplified)
- Head tracking → **carrier yaw** (common model).
- Test with **camera + Blender** on the N3 twin.
- Presence = session/on-switch; head = aim.

## Soft continuum (physics estimates allowed)
- Use TDS hyperelastic props + textile strain-limit assumption.
- Glove: **industry-standard boxing glove mass** (public 12–16 oz class), parametric weight.
- Publish DESIGN ESTIMATE curves/deflections; recalibrate when coupons exist — do not refuse the estimate.

## Still honest
- Stamp DESIGN ESTIMATE ≠ System ID PASS ≠ consumer durability cert.

## Standing rule (Michael 2026-09-21)
**Highlight assumptions wherever needed, whenever we can.** Every estimate lists glove mass, TDS source, camera prior, textile idealization, etc. in plain sight. No quiet numbers.

## Soft virtual physics (landed 2026-09-21)
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` — **ACCEPTED-A** DESIGN ESTIMATE (TDS Neo-Hookean E, sleeved ΔP HYPOTHESIS bands, tip δ, snapback τ @ 14 oz glove ASSUMPTION). Recalibrate on TB-01…04. Not System ID.

## Head-track → yaw (in flight)
`ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` — **ACCEPTED-A**. Codex pass `n3-head-track-yaw-bridge` in progress (camera → head centroid → carrier yaw).
