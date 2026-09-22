# Elias — SAF-02 pinch geometry-first ASSUMPTION gaps (2026-09-21)

| Field | Value |
|---|---|
| **Title** | SAF-02 pinch geometry-first numeric ASSUMPTION gaps list (measure-on-mock before any PL claim) |
| **Rev** | ACCEPTED-A fold 2026-09-21 ~23:59 ET — 2026-09-21 (DIGITAL MATH / PHYSICS pack — $0 paper) |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Authority** | Michael authorized $0 paper; **NO PO**; **NO NEXT_PROMPT** |
| **Status** | **ACCEPTED-A** (paper / digital twin math — Ola) — does **not** authorize physical actuation. Critical **SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **ACCEPTED-A (Ola disposition 2026-09-21):** Cite `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md`. Paper / digital twin math only. Does **not** re-freeze Criticals (**SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**). **No PO.** No invented measured stop-time / PL/SIL / FPS / force / accuracy / IoU / measured latency.

> **Gaps list — not invented numbers.** Pinch = **geometry-first** (Lead ACCEPTED-A). Mushroom topology = **Lead TBD** (ASSUMPTION pointer only). This paper does **not** close SAF-02.

**Identical mirrors:**  
`docs/engineering/ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md`  
`sor_sync/docs/engineering/ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md`

---

## Cited freezes / dispositions (do not re-freeze Critical)

| Item | Citation |
|---|---|
| Pinch geometry-first MVP | `OLA_INTEGRATE_ELIAS_C01_SAF02_2026-09-21.md`; `OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md` |
| Mushroom mast = ASSUMPTION pointer; topology **Lead TBD** | Same + `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md` |
| No invented PL/SIL / stop-time / mm pass bars | SAF-02 qualification paper explicit non-claims |
| AT-PINCH-1 geometry inspection; criteria **TBD — Lead / Safety** | SAF-02 paper SF-3 |

---

## Explicit non-claims

> **No PL / SIL / Category invented.**  
> **Critical SAF-02 remains OPEN.**  
> **Critical P-05 remains OPEN.**  
> This gaps list does **not** assign clearance mm, pad thickness mm, aperture mm, travel mm, force N, or stop-time ms.  
> Electronic `pinch_trip` modality remains **OPEN** / optional deepen.

---

## What must be measured on mock **before any PL claim**

Each row is a **GAP** (unknown until mock / Safety assessment). Values are **not** filled in this paper.

| Gap ID | Measurand / observation needed on mock | Why before PL claim | Owner hint | Status |
|---|---|---|---|---|
| **G-PINCH-01** | Pinch **clearance / gap** at pitch hinge and rotating shoulder band (worst-case finger/soft-tissue paths) | Geometry residual cannot be Category/PL-argued without measured gap evidence | Mech / Safety | **GAP — no number invented** |
| **G-PINCH-02** | **Pad / guard thickness** and coverage at identified pinch sites | Padding effectiveness is geometry residual; thickness unmeasured | Mech / Safety | **GAP** |
| **G-PINCH-03** | **Pinch aperture** (opening that admits finger) under motion extremes | Aperture drives residual risk; no invented mm | Mech / Safety | **GAP** |
| **G-PINCH-04** | Relative **travel / stroke** through pinch zone during pitch / yaw / carrier motion | Travel × aperture → exposure time shape; not a stop-time claim | Mech / Controls | **GAP** |
| **G-PINCH-05** | Fixture / mast **reachability** of E-stop vs pinch sites (layout) | Topology still Lead TBD; layout evidence needed before independence/PL narrative | Safety / Lead | **GAP** (mushroom = ASSUMPTION pointer only) |
| **G-PINCH-06** | Whether electronic `pinch_trip` is used; if yes: sensor **modality** + fail-safe open behavior | Sensor path optional; modality OPEN | Controls / Lead | **GAP / TBD — Lead** |
| **G-PINCH-07** | Manual-reset-after-clear behavior for pinch trip (if sensor fitted) | Latch semantics Critical OPEN | Controls / Lead | **GAP** |
| **G-PINCH-08** | Interaction with presence hard-interlock and inhibit OR (priority stack) | Inhibit OR membership Lead OPEN | Controls / Lead | **GAP** |
| **G-PINCH-09** | Person-adjacent / pilot gate evidence package contents | Safety gate before person-adjacent — criteria TBD | Safety / Michael | **GAP** |
| **G-PINCH-10** | Any force / crush **class** characterization at pinch sites (fixture, not person first) | Do **not** invent N bars; measure later if Safety requires | Safety / Mech | **GAP — no N invented** |

---

## Related Critical / Major (unchanged)

| ID | Severity | Note |
|---|---|---|
| **SAF-02** | **Critical OPEN** | Independent motion-enable / stop; topology Lead TBD; **no PL/SIL** |
| **P-05** | **Critical OPEN** | Fault vent / limp; quantitative after TB-04 |
| SQ-M2 (pinch) | Major | Geometry-first residual; sensor modality TBD |
| C-01 / HY-02 | **Critical / OPEN** | Unchanged by this gaps paper |

---

## Digital twin scope reminder

Digital HIL may stim optional `pinch_trip` bool for inhibit OR V&V (**$0**). That stim does **not** close geometry gaps and does **not** authorize physical actuation.

---

## Cross-cites

- `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md` (**ACCEPTED-A** disposition)
- `OLA_INTEGRATE_ELIAS_SAF02_P05_ASSUMPTION_BOM_2026-09-21.md` (BOM triad ACCEPTED-A — parallel)
- `ELIAS_SAF02_CABLING_ASSUMPTION_SCOUT_2026-09-21.md` (cabling scout — present)
- `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md`
- `OLA_INTEGRATE_ELIAS_C01_SAF02_2026-09-21.md`
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`
- `ELIAS_CONTROLS_DIGITAL_MATH_INTEGRATE_NOTE_2026-09-21.md`

---

*Elias Controls & Perception under Ola — ACCEPTED-A fold 2026-09-21 ~23:59 ET. Cite `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md`. Gaps only. No PL/SIL. Critical SAF-02 / P-05 remain OPEN.*
