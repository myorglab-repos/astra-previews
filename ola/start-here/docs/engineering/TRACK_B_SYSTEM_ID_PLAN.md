# Track B — Soft-actuator System Identification Plan (docs only)

**Owner draft:** Ola (Robotics Desk)  
**Date:** 2026-09-19  
**Status:** PLAN — no lab spend authorized; no invented measured values  
**SoR:** robotic-punching-bag · architecture freeze: soft continuum 8-chamber distal (U1-U3, F1-F3, T1-T2)

## Purpose
Close the measurement path toward **C-01** (pressure to motion to contact) without claiming force/impulse from Track A films. Track B produces **coupon System ID**; Track C later does instrumented contact on fixtures.

## Plain language
We still do not know how much air pressure makes the soft arm stretch, bend, or twist in the real world. Track B is the test plan to measure that on small pieces first, then a full arm section — not on a person.

## Objectives (measurable later)
| ID | Objective | Closure criterion (when lab exists) |
|---|---|---|
| TB-01 | P to axial strain on one sleeved bladder | Identified curve + uncertainty; vent return characterized |
| TB-02 | Differential 3-chamber section bend (U or F) | Tip angle / curvature vs differential P; coupling noted |
| TB-03 | Soft wrist T1/T2 twist under glove-like load | Signed rotation vs differential P; no metal shaft |
| TB-04 | Elastic return / snapback on vent | Time history of tip return; fault vent policy inputs |
| TB-05 | Interface to Track C | Document required tip velocity / contact setup for fixture (no person) |

## Coupon ladder (build order)
1. Single bladder + textile sleeve + strain limit sample  
2. Three-chamber section (U-class) with saddle registration  
3. Soft torsion wrist (T1/T2) with soft cuff retention  
4. Two-section continuum (U+F) on guarded bench fixture  
5. Optional: full arm module on mast mock (still Track B, not user contact)

## Instrumentation (to specify with suppliers — no purchase yet)
- Regulated air, relief, gauges / transducers on each branch  
- Motion: markers or jointless tip pose (stereo / MoCap)  
- Optional: soft strain sensors during development only  
- Data: time-synced P(t), tip pose, temperature notes

## Safety / gates
- No person-facing contact in Track B  
- Overpressure relief mandatory before any pressurized run  
- Fail-safe vent policy drafted before multi-chamber tests  
- Advancement to Track C only after TB-01..TB-04 evidence packages exist

## Deliverables (this docs pass)
- This plan  
- Open BOM / fixture sketch list (non-priced) for Stephen when spend is approved  
- Interface notes for Track C fixture ICD

## Explicit non-claims
No newton, joule, MPa, bar, or cycle-life numbers are assigned here. N1/N3 films remain prescribed motion only.

## Open questions for Michael / Stephen
1. First coupon fab path: in-house textile shop vs soft-robotics supplier?  
2. Budget band for first ladder (Stephen) — not requested yet.  
3. Prefer TB-01+TB-02 only for first paid engagement?
