# ENGINEERING ASSESSMENT — n2-track-a-20260919

**Assessor:** Ola (Robotics Desk)
**Date:** 2026-09-19 ~01:30 ET
**Artifacts:** `reviews/2026-09-19/n2-track-a/` (INDEX, EXECUTIVE_REVIEW, DEFECT_REGISTER, ENVELOPE_GEOMETRY_AUDIT, live_geometry_audit.json, films/stills)
**Prior:** `ENGINEERING_ASSESSMENT_REVIEW_PACKET.md` (N1 Track A)

---

## Summary

N2 is an audited successor twin from preserved N1. Architecture freeze remains compliant (soft continuum 8-chamber distal, no exposed distal metal, stationary bag, rotating carrier). Track A demarcation is correctly restated: prescribed SE(3) motion only; **no strike-impulse proof**.

**Disposition:** Track A visualization pass **accepted with residuals**. Release to hardware / Feasibility gate on propulsion remains **blocked**. Next Codex pass must be a **geometry delta** on G-03/G-05 — not a replay of A-05/A-03.

---

## Findings (severity)

| ID | Prior | N2 claim | Ola disposition | Notes |
|---|---|---|---|---|
| A-05 | High | CLOSED-A; max offset 0.000489 mm vs 0.01 mm criterion | **CLOSED-A** (viz) | Numerical glove-to-soft-core registration verified across frames/scenes. Not a manufacturing or load-path attachment. Orientation/mechanical retention still unqualified (ties to B-02). |
| A-06 | Med | CLOSED-A hybrid label removed | **CLOSED-A** | Visible hybrid text cleared; historical object IDs may retain wording. |
| A-03 | High | Depiction addressed; ID OPEN | **CLOSED-A depiction / OPEN identification** | U/F/T cues + channel emphasis are qualitative only. Physical P to strain / signed T polarity stays Track B (B-05). |
| A-01/A-04 | Med | Frames / opponent bearing | **CLOSED-A viz** | Palm/carrier/opponent annotations acceptable for prescribed storytelling. |
| G-03 | High | FAIL/OPEN; 71 mm proxy min **-2.003666 mm** (L_F @ frame 1499) | **High / OPEN — primary next** | Centerline-radius proxy vs nominal cylinder. Cover-vertex sample min still +8.99 mm. Neither is triangle/loaded clearance. Inherited +4 mm claim rejected (agree). |
| G-05 / B-03 | High | FAIL/OPEN; band axial gaps **0.000 mm** | **High / OPEN — primary next** | Zero nominal Z separation on evaluated bounds. Needs retention/tolerance/padding definition before "pass by redesign" or "pass by allowance". |
| C-01 | Critical | OPEN | **Critical / OPEN** | Unchanged. No invented impulse. |
| B-06 | Critical | OPEN | **Critical / OPEN** | Root/bearing/hub incomplete. |
| B-01/02/04/05/07 | High | OPEN | **OPEN** (Track B coupons) | Correctly deferred. |

---

## Engineering recommendations

1. **Immediate Track A delta (Codex):** Remediate G-03 and G-05 with an explicit engineering decision recorded in the packet:
   - Either **geometry change** (routing / band stack / cover extents) that moves the recomputed metrics into a stated allowance, **or**
   - **Allowance freeze** with named datum, proxy definition, and residual risk owner — without inventing loaded clearance.
2. Prefer fixing the **L_F 71 mm centerline proxy** excursion (worst -2.00 mm) and the **zero band axial gaps** before more film polish.
3. Do **not** reopen A-05 registration work unless a regression appears in the successor audit JSON.
4. Keep N1 hash/lineage intact; continue N2 (or N3) successor pattern.
5. After G-03/G-05 disposition closes or is formally accepted-with-allowance, Michael should authorize **Track B System ID** planning (still no invented MPa/N/J).

---

## Test / validation gaps

- No measured P to strain to tip velocity (C-01 / Track B).
- No instrumented contact impulse (Track C).
- G-03/G-05 lack triangle intersection, padding displacement, and tolerance-stack evidence.
- B-06 structural load path undefined.

---

## Manufacturing notes

- Constraint-driven glove follow does not imply glove retention DFM.
- Band/cover zero gap flags a likely pinch / interference stack-up for textile/foam interfaces — address before tooling concepts.

---

## Open questions for Michael

1. For G-05: is zero axial band gap an intentional sliding/retained interface (needs B-03 retention design) or a modeling error to clear with a positive gap target (state mm target)?
2. For G-03: accept a revised radial **allowance** (proxy definition + min mm) or mandate cover/route remesh until proxy >= 0 (or stated positive reserve)?
3. After G-03/G-05: proceed to Track B coupon plan, or another Track A polish pass?

---

## Next brief

Written to `chats/NEXT_PROMPT.md` as **delta** pass `n2-delta-g03-g05` (ready_for_astra). Codex held until that flip (Ibrahim).
