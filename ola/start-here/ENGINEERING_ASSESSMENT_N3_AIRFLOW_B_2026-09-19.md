# ENGINEERING ASSESSMENT — n3-airflow-bladder-bend-B (Amendment B)

**Assessor:** Ola | **Date:** 2026-09-19 ~15:40 ET  
**Packet:** `reviews/2026-09-19/n3-airflow-bladder-bend/`  
**Evidence:** READY/EXEC/DEFECT/AIRFLOW docs; `build_bend.py`; `swell_audit.json` (status PASS); watched `airflow_review.mp4`

## Summary
**AF-01 is NOT closed for presentation.** Mesh-level illustrative swell exists and audits PASS (emphasized cell volumes grow; all relax to guard), and stand-off atlas regression is retained. But the **delivered film fails the viewer test**: chambers read as **recolor only**, emphasis captions **conflict** with the 8-branch panel, and flow arrows are too small. Track A ≠ strike impulse. C-01/B-06 remain Critical OPEN.

## Findings
| ID | Severity | Disposition |
|---|---|---|
| AF-01 | High (presentation) | **OPEN / FAIL film** — remake required |
| AF-02 | Med | Caption vs `branch_state`/`PROFILES` mismatch (text vs sliders) |
| AF-03 | Low–Med | Flow arrows too small; uniform cyan bundle hard to parse |
| Swell mesh | Info | `swell_audit.json` PASS — radial morph real in blend, not visible enough in film |
| Policy regression | PASS as claimed | Tall hook/UC glove-in-box retained (inherited atlas) |
| RH-02/03, B-03, B-06, C-01 | OPEN | Inherited |

## Engineering interpretation
Builder creates `AMENDMENT_B_ILLUSTRATIVE_SWELL` with per-chamber shape keys (guard scale 0.65 → peak 0.65+0.85×emphasis). Audit asserts peak volume > guard and vent down to guard. Compose overlays draw schematic swell bars from PROFILES, but **3D panes do not communicate volume change** to a careful viewer. Hardcoded `descriptions={...}` in `compose_media.py` are out of sync with profile-driven sliders.

## Recommendation
Immediate Track A remake pass (**B2**): (1) camera/framing/materials so swollen cells are unmistakable vs guard; (2) differential opacity or silhouette outline on emphasized chambers; (3) generate captions from the same `PROFILES`/`branch_state` source as the panel; (4) enlarge flow particles/arrows; (5) side-by-side guard vs peak still with volume callout.

## Plain language
The model file really does puff the soft cells up in the math checks, but in the movie you mostly see color changes — so it still doesn’t teach “this bladder gets bigger, so the arm bends that way.” Captions also disagree with the side chart. We need a clearer remake, not a claim that AF-01 is done.
