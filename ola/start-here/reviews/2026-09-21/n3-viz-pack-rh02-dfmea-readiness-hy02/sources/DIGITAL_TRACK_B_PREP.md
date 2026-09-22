# Digital Track B prep — what we run before physical coupons

**Owner:** Ola (Lead) · **Date:** 2026-09-21  
**Status:** EXECUTE — maximize digital V&V before buy; **does not close C-01 / B-06**  
**Authority:** Michael — push Track B / CV / virtual durability before build; no further approvals

## Plain language
We will simulate and paper-bound everything we can. Soft punch force, real durability, and gym CV still need coupons and a camera bench — otherwise we’d invent numbers.

## Streams (parallel)

| Stream | Digital now (no PO) | Still needs hardware |
|---|---|---|
| Soft continuum | Datasheet-provisional P–strain bands; virtual test matrix; mass method | TB-01…04 coupons → System ID |
| Root Option B | FEA *scope* + assumed load cases labeled | Pin plate fab + lock switch + strength test |
| Controls | Twin-adapter HIL stub (sim presence/head → session_enable) | Real ToF / E-stop / encoders |
| CV | Synthetic/head-ROI dataset plan + logging schema | Physical camera + presence sensor |
| Durability / force / weight | Stack-up from BOM densities; qualitative return hypotheses | Measured cycles, impulse fixture (Track C) |

## Non-claims
- No invented MPa, N, joules, cycle life, or “virtual System ID PASS.”
- Track A films remain pedagogy only.
- Peer drafts: `ISMAEL_DIGITAL_TRACK_B_PREP.md`, `ELIAS_CV_SYNTHETIC_DATASET_PLAN.md` (incoming).

## Next physical (when spend opens)
TB-01 + TB-02 cast kits first — then any honest force/flexibility model gets recalibrated to coupons.


## Peer status
- Ismael Soft digital prep: **ACCEPTED-A** (`ISMAEL_DIGITAL_TRACK_B_PREP.md`).
- Elias CV synthetic plan + HIL stub: **ACCEPTED-A** (``ELIAS_CV_SYNTHETIC_DATASET_PLAN.md``, ``ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md``).

## Soft virtual physics (2026-09-21)
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` — Lead **ACCEPTED-A**. DESIGN ESTIMATE gate closed for Soft paper V&V. Physical TB-01…04 still required for System ID.
