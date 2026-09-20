# Script + Doc Review — n3-standoff-pitch-policy (Option A) for Ola

**Reviewer context:** executor subagent on shared box  
**Date:** 2026-09-19 ~14:30 ET  
**Packet id:** `n3-standoff-pitch-policy`  
**Sources on box:**  
- `/workspace/n3-standoff-review/build_policy.py`  
- `/workspace/n3-standoff-review/REACH_POLICY.md`  
- `/workspace/n3-standoff-review/REACH_VERDICT.md`  
- `/workspace/n3-standoff-review/EXECUTIVE_REVIEW.md`  
- `/workspace/n3-standoff-review/atlas_review.mp4` (duration 152.0 s)  
**Cross-check corpus (parent pass):** `/workspace/n3-reach-review/{atlas_audit.json,cases.json,scripts/audit_atlas.py,REACH_VERDICT.md}`  

**DESKTOP CopyToBox:** **ListMachines / CopyToBox unavailable** to this executor (no ListMachines MCP tool; same limitation as prior n3-reach SCRIPT_REVIEW and `n3-start-here-deliver/PARENT_LISTMACHINES_COPY.md`). Requested DESKTOP paths under  
`C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-19\n3-standoff-pitch-policy\`  
were **not** copied: `audit_atlas.py`, `cases.json`, `atlas_audit.json`, `DEFECT_REGISTER.md`, `READY_FOR_OLA.md`.  
Also missing on box (cited by docs): `policy_spatial_audit.json`, successor `.blend`, lineage receipts.

---

## Verification checklist (requested claims)

| Claim | Result | Evidence |
|---|---|---|
| Stand-off changes **targets**, not chord length | **PASS (script + parent chords)** | `build_policy.py:15-17,48,53` mutates `c['target']` Y and partial `pitch_deg` only; scene policy string and lineage `method` say **no chord or mesh edit**. Parent straight chords remain **429.457 / 601.240 / 858.915 mm** (`n3-reach-review/atlas_audit.json`); EXECUTIVE cites the same triad. Max hook/uppercut **pitch unchanged** at 27° / 24° while Y box moves — geometry family preserved. |
| Tall hook / uppercut **nearest shortfall 0** under policy box | **PASS as documented; not re-audited here** | `REACH_VERDICT.md` tall table: nearest = **0.000000**, verts **981** (hook) / **1415** (uppercut). Independent recompute needs Option A `atlas_audit.json` (not on box). |
| Old-box still **~49.6 / 33.7** | **PASS (exact match to parent audit)** | Verdict + EXECUTIVE: **49.624** hook, **33.693** uppercut. Parent `atlas_audit.json` peaks: nearest **49.624322 / 49.624404** (L/R hook), **33.692502 / 33.692546** (L/R uppercut) under Y=−0.85…−0.60. |
| Max-extension geometry unchanged (stand-off only) | **PASS (numeric fingerprint)** | Parent wrist Y deficits vs far/near face: hook **208.585**, uppercut **177.704**. Policy near face moves **120 mm** (−0.60 → −0.48). Verdict wrist shortfalls under new box: **88.585** / **57.704** = exactly **208.585−120** / **177.704−120**. Proves pose unchanged; only box moved. |
| RH-02 residuals called out | **PASS** | Dedicated `REACH_POLICY.md` § RH-02; EXECUTIVE bold **RH-02 remains OPEN**; verdict points to policy for tall 50% residual. Numbers: 4 verts, **0.571485 mm** interior margin, tall centroid **9.330 mm** below band floor / **99.330 mm** below center, unclipped **77.480°** vs **57°** cap, 50% box **125 mm** bag-proxy encroachment. |
| No invented forces | **PASS** | All three docs close with **Track A does not prove strike impulse** + unverified propulsion/contact force. EXECUTIVE glossary: C-01 Critical, “no physical force claim”. `build_policy.py` has no force/pressure quantities. “Force” appears only in denial / C-01 / “contact force … unverified”. |

### Spatial arithmetic (docs-only, no JSON required)

| Check | Math | Doc claim |
|---|---|---|
| Hook/uppercut Y move | −0.85…−0.60 → −0.70…−0.48 | near (robot-side) **120 mm**, far **150 mm** closer — matches table + `build_policy.py:15` |
| 50% bag encroachment | box closest XY (0,−150) mm; proxy r=275 → **125 mm** | `REACH_POLICY.md` |
| 70% clearance past proxy | closest (0,−300); 300−275=**25 mm** | same |
| Tall 50% Z residual | band 1.780…1.960; center 1.870; Z=1.770670 → **−9.330** / **−99.330 mm** | same |
| Atlas duration | `ffprobe` **152.0 s** | EXECUTIVE “152-second atlas” |
| Parent G-03 / G-05 baselines | G-03_F min **4.321681 mm**; G-05 **4.999995 mm** | EXECUTIVE “down from parent’s +4.321681”; G-05 “remains 4.999995” |

---

## Script review (`build_policy.py`)

### What the script does (aligned with Option A)

1. **Asserts parent blend path + SHA** `c956779e…6ea0` (`:8-9`) — lineage pin.  
2. **Snapshots** `prior_pitch_deg` / `prior_target` (`:14`).  
3. **Strike-dependent Y boxes** (`:15-17`):  
   - hook/uppercut (any extension that hits the kind test): Y=**−0.70…−0.48**  
   - non-max + fraction 0.5: **−0.45…−0.15**  
   - non-max otherwise (0.7): **−0.60…−0.30**  
   - max straight/diagonal/body: **Y left at prior** (−0.85…−0.60) — matches `REACH_POLICY` table.  
4. **Coupled partial pitch only when `extension!='max'`** (`:16-28`): glove vertex-centroid vs shoulder pivot; `asin` clamped; add to prior; clip **0…57°**; round **0.001°**; records `aim_policy` / `unclipped_pitch_deg`. Matches policy § Partial pitch rule.  
5. **Active-arm-only pitch keys** (`:29-35`): inactive side keeps `prior_pitch_deg`; body multi-key **+8 → −20 → +8** schedule preserved.  
6. **Remaps Target_* wireframes** from prior box to new box (`:39-47`); updates title/label strings with policy Y/Z.  
7. **Explicit non-claims in metadata** (`:48,53`): no chord/mesh edit; airflow/schedules inherited; limitations list 57° review cap, marginal 50%, prior 68 mm bow, chapter cuts.

### Script gaps / risks (not contradictions of the written Option A story)

| Item | Severity | Note |
|---|---|---|
| No dual old/new box measurement in builder | Info | Old-box shortfalls must come from updated `audit_atlas.py` (DESKTOP, missing). Builder only writes new targets. |
| No `policy_spatial_audit.json` emission | Low | Cited by `REACH_POLICY.md`; not produced by this script. |
| Wireframe “checked against numeric case box” | Low | Claim is in POLICY prose; enforcement not in `build_policy.py` — belongs in missing verify/audit. |
| Body title uses static `pitch_deg` (−20) while early keys are +8 | Low | Inherited parent pattern; not new in Option A. |
| Cannot execute Blender on box here | Info | Script correctness inferred from source + parent audit fingerprints, not a live rebuild. |

---

## Doc consistency review

### Internal alignment (POLICY ↔ VERDICT ↔ EXECUTIVE ↔ script)

| Topic | Consistent? | Notes |
|---|---|---|
| Box table vs `build_policy` Y assigns | Yes | Hook/UC −0.70…−0.48; 70% −0.60…−0.30; 50% −0.45…−0.15; max straight/body retain far box |
| Partial pitch table (27.126 / 13.499 / 49.181 / 29.110 / 57 / 45.018) | Yes vs VERDICT column | Live Blender recompute not available |
| Tall hook/UC verts 981 / 1415 + nearest 0 | Yes EXECUTIVE ↔ VERDICT | |
| Old-box 49.624 / 33.693 | Yes all docs + parent JSON | |
| RH-02 OPEN / marginal 50% / 125 mm encroachment | Yes | EXECUTIVE does not close RH-02 |
| G-03 **+1.792008** (post 57° cap) vs 60° candidate **0.060172** | Internal doc consistency | New audit JSON not on box |
| Chords ~429.457 / 601.240 / 858.915 | Yes vs parent audit | |
| Force / impulse denial | Yes, all three docs + script lineage | |
| Acceptance pending (Ola geometry; Michael policy) | Yes | EXECUTIVE: packet completion ≠ Ola acceptance |

### Clarity caveat (partials’ “Old-box shortfall” column)

For **max** hook/uppercut, old-box shortfall ≡ parent nearest deficit (pose unchanged).  
For **partials**, pitch changed, so old-box shortfall is **new pose vs old far box**, not a reprint of parent `atlas_audit.json` (e.g. parent `tall_short_L` nearest **263.224** vs verdict old-box **342.963**). Docs do not spell this distinction in the table caption. **Does not invalidate numbers**; Ola should read the column as “far-box miss under Option A pitch.”

---

## Findings (severity + evidence)

### High
*(none)* — No script/doc contradiction that would reverse the Option A thesis (stand-off/target change + coupled partial pitch, chords/meshes unchanged, RH-02 open, no force claim).

### Medium
1. **Option A audit JSON / updated `audit_atlas.py` not on box** — Cannot independently re-stamp nearest=0, verts 981/1415, deepest margins, G-03=1.792008, A-05=0.000350, or dual old-box columns for partials. Parent JSON only proves **old-box ~49.6/33.7** and the **120 mm wrist-shortfall fingerprint**.  
   *Evidence:* missing DESKTOP copy; ListMachines unavailable; only `build_policy.py` + written verdicts present for the successor pass.

2. **“All 38 peaks contain vertices” can be over-read as RH-02 closed** — True surface inclusion coexists with OPEN centering/coverage/spatial-policy residuals. EXECUTIVE paragraph 1 states inclusion success; paragraph 2 correctly keeps RH-02 OPEN. Risk is skim-reading, not false closure in the full text.  
   *Evidence:* `EXECUTIVE_REVIEW.md:3-5`; `REACH_POLICY.md:29-35`.

3. **Rendered-target vs numeric-box check not visible in supplied script** — POLICY asserts every wireframe is checked against the case box; `build_policy.py` remaps splines but does not assert equality. Enforcement presumably in missing verify/audit receipts.  
   *Evidence:* `REACH_POLICY.md:13`; `build_policy.py:39-47`.

### Low
4. **`policy_spatial_audit.json` referenced, absent from box packet slice** — Encroachment math is reproducible from the published boxes; receipt file still needed for Ola packet completeness.  
   *Evidence:* `REACH_POLICY.md:33`.

5. **Partials’ old-box column semantics under-documented** — See clarity caveat above.  
   *Evidence:* parent vs verdict shortfall divergence on pitched partials; max hook/UC unchanged.

6. **Body HUD pitch label vs animated schedule** — Inherited; titles show `pitch_deg` (−20) while early chapter holds +8°.  
   *Evidence:* `build_policy.py:34,42`.

7. **60° candidate / G-03 0.060172 mm** — Documented as retained receipt; not present among box files for inspection.

### Informational / aligned (positive)
8. **Stand-off-not-chord thesis is script-enforced and numerically fingerprinted** — Y mutation + unchanged max hook/UC pitch + exact −120 mm wrist-deficit shift + parent chord triad.  
9. **RH-02 residual package is explicit and quantified** — 4 verts, 0.571485 mm margin, tall Z miss, 57° clip, 125 mm bag encroachment, owners + pending acceptance.  
10. **No invented force / impulse claims** — Uniform Track A banner; C-01 remains Critical OPEN.  
11. **Parent G-05 / G-03 baselines match EXECUTIVE’s “parent” citations** — supports the “margin reduced under new partial pitches” narrative even without the successor audit file.  
12. **Atlas media duration matches EXECUTIVE** — 152.0 s on box copy.

---

## Disposition for Ola

**Engineering story holds on the materials reviewed:** Option A changes **strike-dependent target stand-off** and **coupled partial root pitch**; it does **not** lengthen chords or edit meshes. Tall hook/uppercut **policy-box** inclusion is claimed with nearest shortfall **0**; **old far-box** misses remain **49.624 / 33.693 mm**, matching the parent saved-model audit. **RH-02 is correctly left OPEN** with quantified residuals. **No physical force claim** appears.

**Blocker for full numeric closure of this review:** parent should CopyToBox (when ListMachines is available) the DESKTOP packet files — especially **`atlas_audit.json`**, **`cases.json`**, successor **`audit_atlas.py`**, **`DEFECT_REGISTER.md`**, **`READY_FOR_OLA.md`**, and **`policy_spatial_audit.json`** — so Ola’s file set and this review’s Medium-1 gap can be closed without relying on written tables alone.

**Recommended Ola focus:** (1) accept/reject strike-dependent Y boxes as **changed requirements**, not fixed-box passes; (2) disposition RH-02 marginal 50% + bag-proxy conflict; (3) note reduced G-03 (**+1.792008 mm**) under the 57° cap; (4) leave C-01 / B-06 / RH-03 OPEN as stated.
