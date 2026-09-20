# NEXT_PROMPT
status: in_progress
started_at: 2026-09-19 13:26 ET
runner: codex-cli
timestamp: 2026-09-19 13:30 ET
pass_id: n3-standoff-pitch-policy
from: Ola (Robotics Desk)
source: Michael decision Option A (2026-09-19) + ENGINEERING_ASSESSMENT_N3_REACH_HEIGHT_BODY_2026-09-19.md

## Goal
Track A on the **n3-reach-height-body** lineage (preserve N1/N2/N3 hashes; version a successor packet). Implement **Option A only**: strike-dependent **stand-off + coupled pitch/shape policy** so tall hooks and uppercuts meet the revised target definition without a large continuum lengthening.

### In scope (ordered)
1. **Document policy** in REACH_POLICY.md (or update REACH_VERDICT.md):
   - Keep tall head / abdomen volume definitions explicit (X/Y/Z boxes).
   - Define **strike-dependent stand-off** (different Y or box for hook vs straight vs uppercut vs body) with rationale (hooks/uppercuts work closer / different guard geometry than long straights).
   - Coupled **pitch + partial-extension** rule so 50/70% strokes do not silently drop out of the intended band (closes RH-02 intent for review).
2. **Apply in Blender** on the atlas twin: adjust prescribed trajectories / root pitch trims / target probes per the written policy — **do not** add ~200 mm continuum chord as the primary fix (Option B out of scope).
3. **Re-audit** tall max cases: straight, hook, uppercut, diagonal, body L/R — report glove-in-box and nearest-vertex shortfall under the **new** boxes/policy.
4. **Clearance regression** G-03/G-05 (and A-05 spot-check) after any path/pitch change; extra routing bow only if required to keep sampled proxy >= 0, and document RH-03 impact.
5. Refresh atlas stills + atlas_review film for policy cases; keep prior airflow pedagogy unless a path change breaks readability (Amendment A still applies if you touch airflow scenes).
6. Packet under `reviews/2026-09-19/n3-standoff-pitch-policy/` (or dated sibling); A-J updates; append `## READY_FOR_OLA`.

### Out of scope
- Option B longer continuum family as primary fix
- Track B/C, invented force/pressure/impulse
- Closing C-01 / B-06 hardware

## Constraints
- Soft continuum freeze; pitch stays protected-root attitude; yaw = mast face-opponent when used
- Prefer Blender 3.6.x CLI; append-only chat log; Ibrahim/org push if PC gh blocked
- Track A ≠ strike-impulse proof
- Plain-language glossary mandatory in EXECUTIVE_REVIEW + READY_FOR_OLA

## Accept criteria
- [ ] Written strike-dependent stand-off + pitch/partial policy checked into packet
- [ ] Tall hook and uppercut meet **policy** glove-in-box (or residual shortfall quantified and accepted in register with owner)
- [ ] Straight/diagonal/body still meet their policy boxes
- [ ] RH-02 addressed with coupled partial-extension aim rule (pass or documented residual)
- [ ] G-03/G-05 sampled regression status reported; A-05 not regressed
- [ ] READY_FOR_OLA + films/stills; no invented force numbers

## Plain-language glossary
| Term | Everyday meaning |
|---|---|
| **Option A / stand-off policy** | Change how far away we assume the opponent stands for each punch type, instead of making the soft arm much longer. |
| **Pitch** | Tipping the shoulder aim up/down for height. |
| **RH-01** | Hooks/uppercuts did not reach the old tall guard box. |
| **Track A** | Digital review model and films — not real punch force. |

## Notes
Michael chose A at 13:25 ET. Ola recommendation: stand-off/pitch before lengthening. Airflow CLOSED-A pedagogy retained unless paths break clarity.

