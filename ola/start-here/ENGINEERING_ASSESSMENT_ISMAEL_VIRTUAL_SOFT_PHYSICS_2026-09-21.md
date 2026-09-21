# ENGINEERING_ASSESSMENT — Ismael virtual soft-arm physics (2026-09-21)

**Owner:** Ola (Lead)  
**Source:** `docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md`  
**Disposition:** **ACCEPTED-A** (paper DESIGN ESTIMATE)

## Summary
Soft desk delivered TDS-grounded hyperelastic estimates (Ecoflex 00-30 / Dragon Skin 30), sleeved ΔP HYPOTHESIS bands, tip deflection and snapback τ under an explicit 14 oz glove ASSUMPTION. Assumption-label table matches Michael standing rule. Accept as Soft virtual physics paper gate.

## Findings
| ID | Severity | Finding |
|---|---|---|
| VSP-01 | Info | DESIGN ESTIMATE ≠ System ID; TB-01…04 still required before manufacturing release claims |
| VSP-02 | Info | Bare thin-wall vs sleeved bands are HYPOTHESIS — do not treat as working P setpoints |
| VSP-03 | Low | Blender soft-body / shape-key hook optional; twin morph ≠ ID |

## Engineering recommendations
1. Keep Soft lane idle until Lead asks for Blender soft-body hook or a new physics question.
2. Recalibrate all numeric bands when TB-01…04 coupons exist.
3. Head-track → yaw Codex (`n3-head-track-yaw-bridge`) continues in parallel — orthogonal to Soft physics.

## Test / validation gaps
Physical coupons TB-01…04; no PO from this paper.

## Manufacturing notes
None — paper only.

## Open questions for Michael
None for this paper gate.

## Plain-language glossary
- **DESIGN ESTIMATE** — math from datasheets + stated assumptions; not a lab certificate.
- **ASSUMPTION** — a number or idealization we chose on purpose and labeled.
- **HYPOTHESIS band** — planning pressure range until coupons teach the real curve.
- **Snapback τ** — rough return-time scale from mass/stiffness; not a measured cycle time.
