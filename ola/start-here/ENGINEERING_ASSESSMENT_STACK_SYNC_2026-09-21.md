# ENGINEERING_ASSESSMENT — Stack sync completeness & accuracy (2026-09-21)

**Owner:** Ola (Lead)  
**Authority:** Michael — review and confirm completeness/accuracy; math + durability + practical sync  
**Status:** LEAD SYNC PASS — digital/paper stack only; does **not** close C-01 / B-06 / SAF-02

## Summary
The desks are **directionally synchronized** for Track A digital V&V and paper build-intent: Soft TDS math, Controls session/yaw ICD, Option B B-06 freeze, and integrated BOM point at the same architecture. They are **not** yet synchronized as a manufacturing-ready product. Durability and strike force remain **DESIGN ESTIMATE / HYPOTHESIS**, correctly labeled — not missing by accident.

**Verdict:** Completeness for *digital + paper execute* = **GOOD with named gaps**. Completeness for *consumer / production* = **NOT READY** (Critical B-06, C-01, SAF-02 still OPEN). Accuracy of what is claimed = **ACCEPTABLE** where assumption tags are present; one signal-name mismatch to freeze.

---

## A) Mathematics — completeness & accuracy

| Stack | Status | Accuracy note |
|---|---|---|
| Soft Neo-Hookean E from Smooth-On 100% modulus | ACCEPTED-A | Ecoflex ~0.118 MPa; DS30 ~1.02 MPa — arithmetic consistent with stated λ=2 bridge **ASSUMPTION** |
| Sleeved ΔP bands | HYPOTHESIS | ~10–80 / ~30–150 kPa — **not** working setpoints; overwrite on TB-01 |
| Tip δ / κ beam analog | DESIGN ESTIMATE | Order-of-magnitude only; large-θ rows correctly flagged invalid |
| Snapback τ ~ √(m/k) @ 14 oz glove | DESIGN ESTIMATE | Elastic lower-bound; vent-limited return deferred to TB-04 |
| Glove mass | ASSUMPTION locked | Baseline **14 oz (0.397 kg)**; band 12–16 oz — matches VIRTUAL_VV_POSTURE |
| Head → yaw map | TBD placeholders | Gain/clamp **not invented** — correct for Codex pass |

**Accuracy confirmation:** Soft paper math is internally consistent with its stated assumptions. It does **not** prove punch impulse, fatigue life, or gym CV accuracy.

**Math gap (Medium):** Tip δ table omits glove gravity / tip load (called out); snapback includes glove mass. Intentional, but twin soft-body hook must not mix those models silently.

---

## B) Durability — honesty check

| Claim type | Present? | Lead judgment |
|---|---|---|
| Cycle life / fatigue life number | **No** | Correct — **NOT IN SOURCE** on TDS; needs TB coupons + structural FEA |
| Material ranking (Ecoflex vs DS30) | Yes | Relative stiffness ~8.6× DESIGN ESTIMATE — useful for material downselect |
| Consumer durability cert | Explicitly refused | VIRTUAL_VV_POSTURE stamps DESIGN ESTIMATE ≠ System ID ≠ cert |
| TB-01…04 ladder | Documented | TRACK_B_SYSTEM_ID_PLAN + Soft digital prep — aligned |

**Verdict:** Durability posture is **accurate and incomplete by design**. We can estimate stiffness and return time-scales; we **cannot** truthfully sync a durability life number until physical coupons + B-06 fatigue analysis exist. Do not invent cycle counts.

---

## C) Practical / build sync

| Interface | Soft | Controls | Lead B-06 | Sync |
|---|---|---|---|---|
| 8 chambers / arm | Locked | Manifold scout 8-branch production | Soft boot outboard of pin plate | **Aligned** |
| Option A stand-off (no lengthen) | Locked | Reach policy RH-02 CLOSED-A | Freeze cites Option A | **Aligned** |
| Option B pinned pitch | Soft-term ICD only | `pitch_lock_engaged` in BOM + signal table | Interface freeze | **Aligned intent**; see naming gap |
| Session enable | — | `user_present ∧ head ∧ ¬inhibit` | Twin ICD same | **Aligned** |
| Cast path Ecoflex/DS30 | Soft BOM + physics | — | BUILD_INTENT_BOM | **Aligned** |
| Flex hose loop (finite yaw) | Soft keep-out notes | — | B-06 freeze | **Aligned** |
| Tube OD | Coupon provisional NITRA 6 mm / ¼″ | — | Production prefer Festo PUN-H | **Aligned provisional** |

**Naming mismatch (Medium — freeze now):**
- B-06 freeze uses `pitch_locked`
- Elias signal table / BOM use `pitch_lock_engaged`
Lead freezes normative name: **`pitch_lock_engaged`**. Update B-06 freeze on next touch.

**Still OPEN (Critical — not sync bugs, missing work):**
1. **B-06** structural design + FEA + prototype (scope only exists)
2. **C-01** pressure→motion→contact System ID (needs TB-01…04)
3. **SAF-02** E-stop / supply inhibit topology (ICD language only; no PL/SIL invented)

---

## D) CAD / where the model lives (Michael Q)

| Lane | Platform | Where |
|---|---|---|
| Twin / films / kinematics / airflow pedagogy | **Blender (keep)** | SoR checkout below |
| Fab drawings / FEA / DFM for root pitch | **Production CAD later** (SW / Creo / Inventor) — parallel, not a Blender kill | Same SoR docs + future CAD pack |
| Authoritative SoR | Git | `C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag` on `DESKTOP-P08972I` → `myorglab-repos/robotic-punching-bag` |

---

## E) What is synchronized enough to keep

1. Soft virtual physics ACCEPTED-A with assumption tags (Michael standing rule met).
2. Controls inhibit / session_enable / twin signal table — same Boolean architecture across ICD stubs.
3. BUILD_INTENT_BOM merges Soft + Controls scouts; no PO.
4. Option B pinned presets + recessed soft boot + no distal metal — consistent Soft↔Lead.
5. Codex `n3-head-track-yaw-bridge` in flight to close the camera→yaw digital demonstration.

---

## F) Ranked gaps to make the stack *practically* come together

| Sev | Gap | Next action |
|---|---|---|
| Critical | B-06 not designed/analyzed | FEA scope exists → hand calc / CAD when Stephen opens; keep Option B freeze |
| Critical | C-01 / soft System ID | TB-01+TB-02 first band when spend opens; digital estimates stay labeled |
| Critical | SAF-02 topology | Keep paper ICD; no PL claim until hardware design |
| High | Head-track yaw not yet demoed | Await Codex READY_FOR_OLA; disposition with films/scripts |
| High | Soft twin not yet driven by physics estimates | Optional: Blender soft-body / shape-key hook (Ismael idle until Lead asks) |
| Medium | `pitch_locked` vs `pitch_lock_engaged` | Lead freezes `pitch_lock_engaged` |
| Medium | Tip δ vs snapback load model split | Document in twin hook brief when opened |
| Low | Pages may lag latest START_HERE Soft physics links | Ibrahim refresh |

---

## G) Codex status
`chats/NEXT_PROMPT.md`: **in_progress** `n3-head-track-yaw-bridge` (Codex sole runner).

## Plain-language glossary
- **DESIGN ESTIMATE** — math from datasheets + labeled assumptions; not a lab certificate.
- **System ID** — measured P→motion→force on real coupons; closes C-01.
- **Option B** — manual pinned height presets at the shoulder root (not a live pitch motor for MVP).
- **session_enable** — software OK to run a training/logging session; still not permission to strike.
- **SoR** — Source of Record (the GitHub checkout that owns truth).

## Open questions for Michael
None required to continue. Lead will (1) freeze signal name `pitch_lock_engaged`, (2) disposition head-track packet when READY, (3) open Blender soft-body hook only if you want physics estimates visible in the twin next.
