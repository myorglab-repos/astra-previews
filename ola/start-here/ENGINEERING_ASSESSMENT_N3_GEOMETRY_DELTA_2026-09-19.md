# ENGINEERING ASSESSMENT — n2-delta-g03-g05 / N3 geometry delta

**Assessor:** Ola (Robotics Desk)
**Date:** 2026-09-19 ~02:05 ET
**Artifacts:** `reviews/2026-09-19/n3-geometry-delta/` + READY_FOR_OLA @ 01:40 ET
**Prior:** ENGINEERING_ASSESSMENT_N2_TRACK_A_2026-09-19.md

---

## Summary

N3 geometry delta meets the **sampled nominal** accept criteria from the delta brief. Architecture freeze intact. Track A demarcation correct. **Disposition: accept limited CLOSED-A for G-03/G-05 proxies; physical clearance and B-03 retention remain OPEN.** No hardware / propulsion gate advance. Codex should **hold** until Michael chooses Track B planning vs further Track A.

---

## Findings (severity)

| ID | N2 | N3 claimed | Ola disposition |
|---|---|---|---|
| G-03 | FAIL −2.003666 mm | +3.954128 mm (L_F proxy, all 1920 frames) | **CLOSED-A (sampled centerline proxy)** — physical/triangle/loaded clearance still OPEN |
| G-05 | FAIL 0 mm axial | ~5.000 mm both interfaces | **CLOSED-A (nominal Z separation)** — B-03 retention/seal/pinch OPEN |
| A-05 | CLOSED-A | regression worst 0.000489 mm (15,356 obs) | **CLOSED-A retained** |
| B-03 | OPEN | concept: retained textile edges + protected overlap | **High / OPEN** — concept noted, not approved hardware |
| C-01 | Critical OPEN | unchanged | **Critical / OPEN** |
| B-06 | Critical OPEN | unchanged | **Critical / OPEN** |

**Method notes (accept with caveats):** 8 mm anchored U/F lateral bow + 5 mm outer-cover edge insets is a legitimate **geometry change**, not a fake allowance. Tradeoffs: increased lateral/arc envelope; narrower rotating band height. These are viz/envelope decisions — not textile pattern or pressure equilibrium.

---

## Engineering recommendations

1. Freeze N3 as current Track A geometry baseline (preserve N1/N2 hashes).
2. Do **not** start another Codex viz polish pass unless Michael requests envelope review of the bow/inset tradeoff.
3. Next engineering value is **Track B System ID planning** (coupon matrix: P→strain→tip; soft-wrist T1/T2; return/vent) — documentation only first; no invented numbers.
4. Parallel: B-03 interface definition (retention, tolerances, padding, pinch fixture) as DFMEA inputs — still Track A/mech docs, not Codex film work.
5. B-06 structural root remains a Critical paper gap before any fab spend (@Stephen gate).

---

## Test / validation gaps

Unchanged: measured propulsion/contact (C-01), loaded clearance, B-06 load path, B-01–B-05/B-07 coupons.

---

## Manufacturing notes

Positive nominal cover gaps help DFM storytelling but do not replace sewn retention / abrasion / pinch fixtures at the rotating band.

---

## Open questions for Michael

1. Accept N3 bow/inset tradeoff as the live Track A envelope baseline?
2. Authorize **Track B System ID planning** next (docs/coupon plan in repo — still no lab spend until Stephen)?
3. Or pause Codex entirely until you review `n3-geometry-delta/INDEX.html` stills/films?

---

## NEXT_PROMPT

Left **not** `ready_for_astra` — awaiting your answer on (2)/(3). Ibrahim: hold Codex.

---

## Plain-language glossary (for Michael — keep with this assessment)

| Term | What it means in plain words | Why it matters here |
|---|---|---|
| **Track A** | Making and checking the 3D/digital model and review videos so the design is understandable. | Proves the *story* of motion and shape — not that a real arm hits hard enough. |
| **Track B** | Lab-style tests on soft-arm pieces (coupons) to measure how air pressure changes shape and tip motion. | Needed before we can honestly talk about punch power. |
| **Track C** | Instrumented hit tests on fixtures (not people) for contact force and fault behavior. | Safety and contact claims. |
| **G-03** | A clearance check: “Does the soft arm get too close to (or into) the bag’s imaginary cylinder?” We use a simple centerline proxy in millimeters. | Negative = model says the arm centerline dips inside the keep-out. N3 fixed the *model* proxy to about +4 mm. Real padded clearance still unproven. |
| **G-05** | Gap check between the rotating band and the fixed covers above/below it (axial = up/down along the bag). | Zero gap meant faces touched in the model (pinch risk story). N3 opened ~5 mm nominal gap. Real sew/retention still open (**B-03**). |
| **CLOSED-A** | Closed for *this visualization / model-audit* purpose only. | Not the same as “ready to manufacture” or “safe in contact.” |
| **OPEN / Critical** | Still unresolved; Critical = must not pretend it’s done for Feasibility gates. | **C-01** = no measured punch impulse yet. **B-06** = shoulder root structure not fully designed. |
| **N1 / N2 / N3** | Versioned Blender successors. N1 preserved baseline; N2 fixed glove registration and cues; N3 fixed clearance/gap geometry. | We never overwrite the audited older binary; lineage stays reviewable. |
| **Proxy / audit** | An automated measurement script run on many animation frames; a stand-in metric, not a lab load test. | Good for catching model mistakes early; bad if treated as physical proof. |
| **Architecture freeze** | Soft air-filled fabric arms (not rigid metal sticks), 8 air chambers per arm, bag stays put, shoulders rotate on the mast. | Stops the team from quietly switching back to cylinders/cams mid-project. |
| **NEXT_PROMPT** | The brief Codex/Astra reads to know what to do next. `ready_for_astra` = go; `awaiting_michael` = hold. | Prevents the watcher from re-running yesterday’s job or starting Track B without you. |
| **READY_FOR_OLA** | Marker in the chat log meaning “pass settled — Ola should review.” | That should wake me immediately; missing it is why you had to chase progress. |

### N3 result in one breath
We moved the soft-arm path slightly outward (8 mm bow) and shortened the rotating band’s height (5 mm insets) so the *model’s* keep-out and gap numbers pass. That is digital housekeeping. It does **not** mean the trainer can punch safely or with known force yet.
