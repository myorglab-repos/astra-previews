# ENGINEERING ASSESSMENT - n3-af01b-exposed-arm-swell-2

**Assessor:** Ola | **Date:** 2026-09-19 ~23:55 ET  
**Packet:** `reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/`  
**Evidence:** READY/EXEC/DEFECT/AIRFLOW_PEDAGOGY; swell_audit PASS; exposed_render_audit PASS (2048 chamber-frame samples, max_radius_error_m=0, constant-neutral materials); caption_audit PASS; scripts `build_bend.py` / `render_media.py` / `airflow_cues.py`; watched `exposed_blind_review.mp4` + `airflow_review.mp4`; freeze-frame guard vs hold from blind film; dual-angle `guard_peak_*.png` + `decoded_blind_*.png`

## Summary
**AF-01b CLOSED-A** for Track A visualization on the **exposed left-arm panes**. Remake uses two-tier radial shape keys (guard 0.45 → fill-more ≈1.8 / fill-less ≈0.55), constant-neutral cell materials in exposed renders, opposite Side A/B cameras, and a board-free blind clip. Continuous playback alone can understate silhouette change (video model reported thickness-constant); **freeze-frame guard→hold and dual-angle guard/peak sheets contradict that** — differential chamber diameter is readable without color emphasis. Same adjudication pattern as B2 (stills override motion-only miss). AF-02 retained. AF-01b-occ Medium residual (assembled occlusion / some label ambiguity under motion). C-01 / B-06 Critical OPEN. **Track A does not prove strike impulse.**

## Findings
| ID | Status | Notes |
|---|---|---|
| AF-01b | **CLOSED-A** | Exposed-pane geometric swell accepted via stills + dual-angle sheets + scripted radial morph; not packaging / P-V / System ID |
| AF-01 | CLOSED-A | Prior B2 board retained as supplement |
| AF-02 | CLOSED | Shared profile drives captions / morph; caption_audit PASS |
| AF-01b-occ | Med residual | Opposite view helps; not all surfaces always readable in motion |
| RH-02 | **queued next** | Partial-extension aim policy |
| C-01 / B-06 | Critical OPEN | Unchanged |

## Engineering recommendations
1. Issue `n3-rh02-partial-extension` NEXT_PROMPT immediately (coupled pitch + shape weights OR declare partials non-head-target; re-audit bag-proxy encroachment).
2. Keep educational radial endpoints documented as dimensionless drawing choices — never quote as strain or pressure.
3. Optional later polish: brief hold freeze or silhouette outline cue if Michael wants continuous-playback-first readability without still scrubbing.

## Test / validation gaps
- No physical chamber packaging, self-contact, or textile strain qualification on swollen educational surfaces.
- No measured P→strain→bend→impulse (C-01).
- Independent human playback without freeze-frame remains a softer bar than freeze-frame + sheets (document both).

## Manufacturing notes
None from this remake. Swollen meshes are illustrative only — do not freeze DFM off exaggerated radial morph.

## Open questions for Michael
None blocking RH-02. Optional: prefer continuous-playback silhouette cue polish later, or proceed RH-02 only.

## Plain-language glossary
| Term | Everyday meaning | Why it matters here |
|---|---|---|
| AF-01b CLOSED-A | Cutaway arm tubes look fatter when "filled," accepted for model review | Closes your exposed-arm swell request for Track A films |
| Radial morph | Drawing the tube thicker/thinner | Teaching aid — not real bladder pressure |
| Opposite views | Two cameras on opposite sides | Helps see cells hidden from one side |
| Freeze-frame vs playback | Pausing vs watching full speed | Motion can hide thickness; stills prove it |
| RH-02 | Partial punches aiming wrong height / clipping bag | Next software policy pass |
| C-01 / B-06 | Missing measured punch chain / incomplete shoulder structure | Still Critical; films cannot close |

What changed / what is still not proven: exposed arm now shows geometric fill swell in stills and dual-angle sheets with neutral materials; real air bend, punch power, durability, and root structure remain unproven.
