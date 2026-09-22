# ENGINEERING ASSESSMENT — n3-viz-pack-soft-phys-envelope-c01-saf

**Disposition:** ACCEPTED-A (Track A teaching films / illustration only)  
**Date:** 2026-09-21 (ET)  
**PR:** https://github.com/myorglab-repos/robotic-punching-bag/pull/8  
**Packet:** `reviews/2026-09-21/n3-viz-pack-soft-phys-envelope-c01-saf/`  
**Branch:** `cursor/n3-viz-pack-soft-phys-envelope-c01-saf-412a`

## Summary

Five teaching films close the visualization gap for recent paper/stills-only work: soft-physics cue sequence, slim-root yaw re-encode, B-06 Option B keep-out illustration, C-01 coupon board, and SAF-02 / presence-inhibit digital HIL schematic. START_HERE embeds all five and still resolves atlas, airflow, exposed-blind, pitch, and prior black-collar yaw. Critical B-06, C-01, SAF-02, and P-05 stay OPEN. No spend. Twin is not System ID.

## Findings (evidence)

1. **Film scrub (independent watchVideo)** — soft_phys: rest → swell → bend → twist → return with ASSUMPTION HUD; yaw: black collars / cyan retired, slim left root, Criticals OPEN on card; B-06 / C-01 / SAF: schematic illustration only; no measured claims; no closed Criticals.
2. **Bright-cyan pixel count (independent)** — yaw_slim_head_left/right, cue_contact_sheet, b06_stack, c01_tb01, saf_happy: **0**.
3. **ffprobe** — five mp4s present at 1500x900; 12 fps authored clock as labeled (not detector rate).
4. **START_HERE** — all new `src` paths resolve; prior atlas / airflow / exposed_blind / pitch / black_collar yaw resolve.
5. **Labels** — INDEX + on-film HUDs keep DESIGN ESTIMATE / ASSUMPTION / HYPOTHESIS and Critical OPEN language in plain sight.

## Engineering recommendations

- Accept and merge PR #8.
- START_HERE everyday yaw player is `head_yaw_review_slim_root.mp4`. The black-collar encode remains as history.
- Recalibrate soft-phys hook constants only when TB-01…04 exist.
- Do not treat B-06 blocks as CAD mm or SAF-02 schematic as hardware acceptance.

## Test / validation gaps

- B-06 / C-01 / SAF-02 / P-05 remain Critical OPEN (hardware).
- HY-02 office USB face-in-ROI still operator-gated.
- No measured pressure, strain, force, cycle life, FPS, or accuracy from this pack.

## Manufacturing notes

None. No cast, mold, or PO.

## Open questions for Michael

None required to accept. Spend gate (Soft TB / Mech mock / E-stop-ToF) remains with Stephen when ready.

## Glossary

- **Teaching film** — Prescribed / illustrated motion for review, not a lab measurement.
- **ASSUMPTION HUD** — On-screen labels that mark design guesses vs measured facts.
- **Keep-out block** — Drawing aid for reserved volume; not measured clearance.
- **Digital HIL schematic** — Logic story for presence/inhibit; not physical actuation.
