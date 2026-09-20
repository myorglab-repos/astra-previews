# ENGINEERING ASSESSMENT — n3-standoff-pitch-policy (Option A)

**Assessor:** Ola | **Date:** 2026-09-19 ~14:30 ET  
**Packet:** `reviews/2026-09-19/n3-standoff-pitch-policy/`  
**Standard:** docs + scripts + atlas_audit.json (film watch completing in parallel)

## Summary
**ACCEPT Option A for RH-01 (policy-box criterion).** Stand-off moves the assumed opponent closer for hooks/uppercuts; max-extension arm geometry unchanged. Tall hook/uppercut **nearest glove shortfall = 0** under new boxes (981 / 1415 verts). Old far-box shorts **49.624 / 33.693 mm** retained on purpose. RH-02 remains OPEN (50% partial spatial policy). G-03 margin reduced (~4.32 → ~1.79 mm) but still nonnegative sampled. C-01/B-06 Critical OPEN. Track A ≠ strike impulse.

## Findings
| ID | Status | Notes |
|---|---|---|
| RH-01 | CLOSED-A under **policy** boxes | Far-box failure archived; acceptance = accepting nearer stand-off for hook/UC |
| RH-02 | High OPEN | Coupled pitch on; 50% coverage/encroachment residuals |
| RH-03 | OPEN physical | No new bow this pass |
| G-03 | Sampled PASS / margin thinner | Review if 1.79 mm proxy is enough digitally |
| G-05 / A-05 | Retained | ~5 mm gaps; registration OK |
| B-06 / C-01 | Critical OPEN | Unchanged |

## Script/data verification
- `build_policy.py`: mutates target Y (+ partial pitch); no chord/mesh lengthening.
- Wrist shortfall fingerprint: −120 mm exactly with near-face move → poses unchanged.
- `atlas_audit.json` re-checked on DESKTOP copy: tall_max_*_hook/uppercut nearest = 0.0.

## Plain language
We did not make the soft arms longer. We said hooks and uppercuts assume the opponent stands a bit closer, and under that rule the gloves reach the tall target boxes. Half-length punches still need more aim policy work. Real punch force is still unproven.

## Next
Amendment B (`n3-airflow-bladder-bend-B`) already queued for bladder swell→bend films. START_HERE should become sole front door pointing at this packet as baseline (pending Michael confirm to rebuild).


## Film watch (completed)
tlas_review.mp4 watched: stand-off boxes visible per strike; tall hook/UC gloves enter cyan policy volumes; pitch arrows and amber body targets clear. No major clarity issues. Supports ACCEPT disposition.

