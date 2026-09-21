# Soft-arm / continuum inventory (SoR) — DRAFT for Ola

**Author:** Ismael (Soft Robotics)  
**Date:** 2026-09-21 ET  
**Canonical SoR:** `C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag` on DESKTOP-P08972I (`myorglab-repos/robotic-punching-bag`)  
**Access note:** This executor had no ListMachines / machineId Shell; content mirrored SoR-layout trees were used for reading. Citations below are **SoR relative paths**. Box `/workspace/boxing-trainer` is not SoR.  
**Rule:** Cite SoR only. No invented P/force/life. Do not overwrite `chats/NEXT_PROMPT.md`.

## Sources read this pass
| SoR path | Soft-arm / pneumatic / continuum (one line) |
|---|---|
| `reviews/2026-09-19/n3-rh02-partial-extension/CONTINUUM_PNEUMATIC_INTENT.md` | 8 chambers/arm (U1–U3, F1–F3, T1–T2); textile strain limit; vent + elastic return; soft wrist; no exposed distal metal; Track A ≠ impulse |
| `reviews/2026-09-19/n3-rh02-partial-extension/DOF_MECHANISM.md` | Bag/mast fixed; carrier yaw + protected-root pitch distinct; B-06 root still concept; Track A ≠ impulse |
| `reviews/2026-09-19/n3-standoff-pitch-policy/DOF_MECHANISM.md` | Same freeze; Option A policy boxes; yaw vs protected pitch; prescribed geometry only |
| `reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/DOF_MECHANISM.md` | Same 8-chamber freeze; swelling/bend prescribed illustrations, not pneumatic solution |
| `revision_n/review_packet/CONTINUUM_PNEUMATIC_INTENT.md` | Full qualitative intent: isolated parallel branches; fill→steer→vent→elastic return; limp bladder cannot pull; manifold is envelope |
| `revision_n/review_packet/DEFECT_REGISTER.md` | B-01 neck/seal, B-02 retention through wrist, B-04 textile ID, B-05 wrist polarity, B-06 Critical root, B-07 return/fault, C-01 Critical |
| `revision_n/review_packet/INTERFACE_VULNERABILITIES.md` | DFMEA-input callouts C1–C9 (bladder neck, knit, return bands, wrist, textile eye, flange/hub, band pinch, manifold/hoses, covers) |
| `docs/engineering/TRACK_B_SYSTEM_ID_PLAN.md` | TB-01…TB-05 coupon ladder; P→strain→tip; no person contact; no numbers assigned |
| `docs/engineering/B06_ROOT_PITCH_HARDWARE_SKETCH.md` | Soft termination = textile eye / harness into recessed boot; soft-termination peel; hose pinch at pitch hinge; hardware range TBD |
| `STAGE0_REQUIREMENTS_HAZARD_REGISTER.md` (+ Amendment 2026-09-19) | Soft reqs P-01…P-07 OPEN; hazards H-01…H-07 soft-relevant; §5 coupon order; pitch DOF proposed under B-06 |
| `START_HERE.html` | Baseline = n3-standoff-pitch-policy + n3-airflow-bladder-bend-B2; Option A; no arm lengthening; C-01/B-06 Critical OPEN |
| `chats/NEXT_PROMPT.md` | **READ ONLY** — awaiting_michael (historical stand-off vs lengthen choice); not overwritten |

## Frozen construction (Lead freeze + SoR intent)
- Soft continuum distal; **8 chambers/arm**, 16/pair; **isolated** supply/exhaust branches (air does **not** flow serially U→F)  
- Textile/fiber strain limiting; **elastic return** from stored strain (not suction)  
- Soft torsion wrist T1/T2; **no exposed distal metal**  
- **Option A stand-off** (no arm lengthening) — START_HERE + Lead standing rule  
- Stationary bag fill **target** ~200 lb; rotating shoulder carrier; protected-root pitch (B-06 concept, not fab-closed)  
- Track A films = prescribed motion / pedagogy only

## Twin-path pedagogy (what Track A may show)
- Qualitative chamber groups U / F / T; common vs differential intent  
- Vent + elastic return narrative; illustrative swell (AF pedagogy)  
- Soft covers hiding metal root; Option A closer boxes for hook/UC  
**Must not claim:** measured propulsion, durability, loaded reach, CV, or consumer performance

## Soft Robotics lane vs Lead Critical
| Item | Owner lane | Status |
|---|---|---|
| Bladder/textile/chamber System ID (TB-01…04 ↔ B-01/B-04/B-05/B-07) | Ismael draft → Ola disposition; Stephen for spend | OPEN — plan exists, no lab numbers |
| Module DFM (wear modules, seams, replaceable sleeves) | Ismael paper | OPEN |
| B-02 / B-03 retention notes | Ismael support notes | OPEN |
| Soft termination textile eye / boot ICD (B06 sketch) | Ismael support Ola B-06 | OPEN — Critical B-06 stays Lead |
| C-01 / strike impulse | Out of Soft-only close; Track B→C | Critical OPEN |

## Gaps (inventory)
- Working pressure, relief, air demand, cycle life: **NOT IN SOURCE** (OPEN)  
- Branch polarity / steering map under load: requires Track B coupons  
- Manifold ports / valve count / rotary union vs finite yaw: OPEN architecture (Stage 0 P-06)  
- Prefer future drafts from live DESKTOP/GitHub SoR after parent CopyToBox or machineId read  
