> **2026-09-21:** MVP path frozen to **Option B pinned presets** — see `docs/engineering/B06_OPTION_B_INTERFACE_FREEZE.md`. Actuated Option A remains upgrade path.

# B-06 — Protected root / shoulder pitch / hub load-path (DFMEA-oriented sketch)

**Owner draft:** Ola  
**Date:** 2026-09-21 (deepened from 2026-09-19 concept)  
**Status:** CONCEPT + DFMEA STARTER — not fab release; Critical B-06 remains OPEN until designed, analyzed, and prototype-qualified  
**Related:** Stage 0 (carrier yaw + shoulder pitch); Track A films visualize pitch as protected-root attitude; RH-01 / RH-02 aim policy

## Plain language
The soft arms tip up and down for tall/short fighters by rotating at the **shoulder root** — metal stays behind padding, not out on the exposed soft arm. This note is the hardware story: what that joint must eventually be, how loads travel, and which failure modes we must design against. Numbers here are **placeholders or Track A review caps**, not rated hardware.

---

## 1. Degrees of freedom (protected)

| DOF | Function | Track A today | Hardware intent |
|---|---|---|---|
| Yaw | Face opponent | Rotating shoulder carrier about mast | Existing cartridge / sleeve / yoke intent |
| Pitch | Height preset (short / mid / tall) | Prescribed root attitude; review caps ~0…57° illustrative | Limited-range pitch stage between yaw rotor and soft-arm boot |
| Distal continuum | Punch shape + extension | Soft 8-chamber arm; no distal metal | Unchanged architecture freeze |

Michael’s definition: pitch = **vertical angle of the outbound shoulder axis** (not a second “Z twist” of the soft arm).

---

## 2. Stack architecture (paper interface)

Order from mast outboard:

1. **Mast / fixed hub** — axial retention by bearings + retainers (not slip-fit only); torque reaction into mast/base.  
2. **Yaw rotor / cartridge** — sleeve, saddles, serviceable flange. Encoder / limit switches ICD TBD.  
3. **Pitch stage** — between yaw flange and soft-arm termination boot.  
4. **Soft-arm termination** — textile eye / harness into **recessed boot**; last metal ends here.  
5. **Services** — eight independent pneumatic branches (+ optional electrical) through pitch joint via rotary union and/or flex-loop umbilical.

### Pitch stage options (MVP decision still open)

| Option | Description | Pros | Cons |
|---|---|---|---|
| **A — Actuated** | Motor/gear or pneumatic rotary actuator, hard stops, position sense | Live height change between rounds | Cost, sealing, fail-safe design |
| **B — Manual preset (MVP lean)** | Pinned plates / detents at short/mid/tall | Simple, inspectable, cheap | Operator changeover; no mid-session auto |

**Recommendation for early prototype:** Option **B** for first fixture, keep interface geometry ready for Option **A** upgrade (same bolt circle / boot keep-out).

---

## 3. Load path (intent)

**Arm strike chain:**  
glove → soft wrist → continuum textiles/bladders → shoulder retention / textile eye → pitch stage → yaw rotor → bearings → hub → mast → base → anchors → slab.

**Bag body impacts:** separate path through fill / liners / mast — **do not** assign bag hits solely to the arm chain.

**Design implication:** pitch stage sees glove + arm mass inertia, continuum reaction, and hose tension — not the full ~200 lb bag mass as a normal case.

---

## 4. Envelopes & open dimensions (TBD — do not invent ratings)

| Item | Track A / note | Hardware open |
|---|---|---|
| Pitch travel | Review storytelling used up to ~57° | Hard-stop range TBD by anthropometry + boot keep-out |
| Height presets | short / mid / tall discrete attitudes | Pin angles or servo setpoints TBD |
| Bearing size | — | ID/OD, axial capacity TBD after load cases |
| Boot keep-out | Soft covers hide root | Envelope for padding + service access |
| Hose bend radius | RH-03 later | Min bend at pitch hinge TBD |
| Mass at glove (fixture) | Prescribed motion only | Prototype mass property TBD — no fake kg |

---

## 5. DFMEA starter (no fake RPN / severity scores)

Severity / occurrence / detection stay **blank until analysis**. Use this as the living list.

| ID | Function | Failure mode | Local effect | System effect | Potential cause | Current prevention (intent) | Detection (intent) | Recommended action | Owner |
|---|---|---|---|---|---|---|---|---|---|
| F-01 | Hold pitch under gravity + punch reaction | Pitch unlock / free fall | Arm drops | Mis-aim; pinch; user surprise | Detent wear, pin not engaged, actuator brake fail | Hard stops + positive lock / spring detent; Option B pin with flag | Limit switch “locked”; visual pin flag | Specify lock architecture before fab | Mech |
| F-02 | Support axial / moment at hub | Bearing axial walk-out | Play, noise | Loss of aim; binding | Retainer omitted, wrong stack | Shoulders + snap rings + documented stack | End-play check in assembly | Drawing note + torque/stack procedure | Mech |
| F-03 | Soft termination retention | Textile eye peel / pull-out | Soft arm detaches at root | Loss of arm; exposed hardware risk | Undersized eye, abrasion, wrong stitch | Recessed boot; strain-relief; B-03 retention coupon | Pull test on coupon; visual fray | Couple to B-03 textile plan | Mech/Matl |
| F-04 | Route air at pitch hinge | Hose pinch / fatigue crack | Chamber limp or stuck | Wrong punch shape; leak | Bend radius < min; sharp edge | Flex loop or rotary union; edge radius | Pressure decay test; visual chafe | RH-03 bend-radius table | Mech/Pneum |
| F-05 | Yaw / pitch position knowledge | Encoder / limit loss | Wrong attitude | Mis-aimed strike | Cable break, EMI, uncalibrated | Redundant limits; safe-state “fold” | Fault bit → inhibit strike | Control ICD + safe state | Controls |
| F-06 | Hard-stop energy | Shock at stop | Tooth / pin shear | Sudden stop, debris | No soft stop, high rate | Elastomer bumper or ramp | Event log on stop hit | Size bumper after mass props | Mech |
| F-07 | Service access | Cannot remove cartridge | Long downtime | Field unserviceable | Buried fasteners | Flange service from outboard | Maintenance time trial | DFA review | Mech/Mfg |
| F-08 | User proximity | Pinch at pitch hinge | Soft-tissue injury | Safety incident | Gap < finger; no cover | Padding + gap standard; guards | Risk assessment | Safety gate before pilot | Safety |
| F-09 | Corrosion / sweat | Seizure of pitch | Stuck height | Cannot change preset | Bare steel in humid gym | Coatings / stainless candidates | Periodic exercise of joint | Materials note | Mech |
| F-10 | Over-pressure soft arm reaction | Pitch overload | Bent bracket | Permanent misalignment | Blocked vent + hit | Overpressure relief upstream (pneumatics) | Pressure trip | Tie to C-01 / manifold DFMEA later | Pneum |

**Non-claims:** no RPN numbers, no “safe for users” claim, no cycle life.

---

## 6. Verification ladder (paper → fixture → proto)

| Gate | Evidence required | Spend |
|---|---|---|
| G0 Paper | This sketch + interface sketch + DFMEA rows owned | None |
| G1 Envelope CAD | Mast/hub/yaw/pitch/boot keep-out solids (SW/Creo/Inventor as chosen) | Tooling license only if already owned |
| G2 Static load cases | Documented glove+arm mass assumptions; FEA or hand calc on pitch bracket / pins | Analyst time; Stephen if paid FEA |
| G3 Fixture | Pitch stage mockup with hard stops + lock; cycle without soft arm first | Stephen for fab |
| G4 Soft-arm integration | Textile eye pull + hose flex at pitch | Coupons; Stephen |
| G5 Safety | Pinch / guard / safe-state review | Before any user-adjacent demo |

Track A films (pitch pedagogy) support **communication only** — they do not close G2–G5.

---

## 7. Interface ICD stubs (controls / pneumatics)

- **Pitch commanded vs actual** — discrete preset ID (short/mid/tall) or continuous deg; report locked/unlocked.  
- **Inhibit strike** if pitch not locked or encoder fault.  
- **Pneumatic**: no chamber fill command while pitch is moving (Option A) or while unlock detected (Option B).  
- **Yaw + pitch** not claimed simultaneous high-rate motion in MVP.

---

## 8. Track A vs hardware (hard line)

| Track A may show | Hardware must still prove |
|---|---|
| Pitch angle storytelling for height presets | Shaft, bearing, lock sizing |
| Soft covers hiding metal root | Boot strength, pinch gaps |
| Policy boxes / reach films | Loaded reach, fatigue |

**Critical B-06 stays OPEN** until G2+ evidence exists. No invented N·m, MPa, or cycle counts.

---

## 9. Immediate next paper actions (no spend)

1. One-page interface sketch: mast / hub / yaw / pitch / textile eye / hose loop (CAD or Blender block diagram OK).  
2. Decide MVP: **pinned B** vs **actuated A** (recommend B for first fixture).  
3. List open dimensions table owners (bearing, travel, boot, hose R_min).  
4. Expand F-01…F-10 with owners after Michael / Stephen confirm path.  
5. Film pass (separate NEXT_PROMPT): show pitch presets + yaw vs soft-arm motion on START_HERE — **pedagogy only**.

## Non-claims
No rated loads, no cycle life, no supplier selection, no consumer-ready root.
