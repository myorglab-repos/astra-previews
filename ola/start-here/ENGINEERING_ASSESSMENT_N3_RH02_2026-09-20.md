# ENGINEERING ASSESSMENT - n3-rh02-partial-extension

**Assessor:** Ola | **Date:** 2026-09-20 ~00:50 ET  
**Packet:** `reviews/2026-09-19/n3-rh02-partial-extension/`  
**Evidence:** READY / RH02_POLICY / EXEC / DEFECT; policy_spatial_audit PASS; atlas regression (38 peaks, 26 max records, 2431 clearance samples unchanged; G-03 min +1.792008 mm, G-05 +4.999995 mm); scripts `build_policy.py` / `audit_policy.py`; stills `partial_{short,mid,tall}.png`, `qa_all_*.png`, labeled `media/stills/*`

## Summary
**RH-02 ACCEPTED (CLOSED-A, scoped Track A policy).** Codex correctly applied the authorized **non-head-target** alternative to all six 50% straight cases: amber separated diagnostic reference boxes (Y=-0.60..-0.30 m, +25 mm bag-proxy gap), explicit NON-HEAD-TARGET captions, quantified surface/wrist/centroid misses, no motion/mesh change. Six 70% straights retain head-target with glove **surface inclusion** and **centroid height** in band; tall 70% reports **6.305 mm** centroid Y shortfall behind near face (honest, not box-moved). Does **not** restore 50% head-shot capability or qualify physical clearance. C-01 / B-06 Critical OPEN. **Track A does not prove strike impulse.**

## Findings
| ID | Status | Notes |
|---|---|---|
| RH-02 | **CLOSED-A (policy)** | Six 50% NON-HEAD-TARGET + amber references; six 70% head surface+height retained |
| RH-02 capability exclusion | Unavailable | 50% head shots remain out of scope until new mechanical/policy brief |
| RH-01 | Prior CLOSED-A | Max Option A boxes unchanged (26 records) |
| G-03 / G-05 | Digital regression pass | Exact parent mins; physical OPEN |
| AF-01b | Prior CLOSED-A | Source AF-01b-2 preserved; no airflow remake |
| RH-03 / B-03 | OPEN | Routing / textile retention |
| C-01 / B-06 | Critical OPEN | Unchanged |

## Key numbers (from policy_spatial_audit + EXEC table)
- 50% short L/R: gap +25 mm; surface shortfall 0; wrist ~143 mm; centroid ~101 mm; verts_inside=4 (reference only)
- 50% mid L/R: surface shortfall **20.756 mm**; wrist ~185; centroid ~139; verts=0
- 50% tall L/R: surface shortfall **58.537 mm**; wrist ~227; centroid ~174; height shortfall ~9.3 mm; verts=0
- 70% short/mid L/R: surface 0; centroid 0; height 0; verts thousands
- 70% tall L/R: surface 0; height 0; **centroid shortfall 6.305 mm**; wrist 52.522 mm; verts 2106

## Engineering recommendations
1. Hold NEXT_PROMPT `awaiting_michael` — Track A RH/AF loop is clean enough to choose: Track B coupon ladder (C-01), B-06 paper deepen, or RH-03 routing/materials brief.
2. Keep 50% labeled NON-HEAD in any product UI / training library until a future pass re-opens that capability with new evidence.
3. Do not treat tall 70% centroid Y shortfall as a silent PASS for full-glove containment — surface inclusion ≠ centered aim.

## Test / validation gaps
- No loaded-reach or contact fixture data.
- Surface inclusion ≠ full glove volume in box.
- G-03 narrow digital margin unchanged (~1.8 mm) — not a physical clearance rating.

## Manufacturing notes
Policy-only metadata/annotation change (`build_policy.py`); no DFM delta from meshes.

## Open questions for Michael
Prefer next: **Track B System ID coupons**, **B-06 hardware deepen**, or **RH-03**?

## Plain-language glossary
| Term | Everyday meaning | Why it matters here |
|---|---|---|
| RH-02 CLOSED-A | Partial-punch aim rules accepted for the digital twin | Half-extension punches are no longer claimed as head shots |
| Non-head-target | We admit this stroke is not aiming at the head | Prevents fake head-hit claims at 50% |
| Amber reference box | Comparison volume only | Not a hit zone |
| Surface inclusion | Some glove skin points enter the box | Weaker than the whole glove inside |
| Tall centroid shortfall | Average glove center sits slightly short of the box face | Honest residual on tall 70% |
| C-01 / B-06 | Missing measured punch chain / incomplete shoulder structure | Still Critical |

What changed / what is still not proven: 50% strokes are honest non-head rehearsals with separated boxes; 70% keep head-band surface+height; real power, structure, and loaded reach remain unproven.
