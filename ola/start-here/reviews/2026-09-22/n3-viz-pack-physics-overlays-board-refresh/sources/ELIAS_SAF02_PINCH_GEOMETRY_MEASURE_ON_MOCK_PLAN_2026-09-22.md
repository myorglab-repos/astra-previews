# Elias — SAF-02 pinch geometry **measure-on-mock** plan (2026-09-22)

| Field | Value |
|---|---|
| **Title** | SAF-02 pinch geometry-first measure-on-mock plan — blank ASSUMPTION fields for mock fill-in (no invented mm; no PL) |
| **Rev** | 2026-09-22 (America/New_York) — $0 ASSUMPTION paper |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Authority** | Michael authorized $0 paper via Ola; **NO PO**; **NO NEXT_PROMPT**; **NO SendToUser** |
| **Status** | **ASSUMPTION paper** — geometry-first before any PL claim. Does **not** authorize physical actuation. Critical **SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **Cite ACCEPTED-A gaps list:** `ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md`. This plan turns those gaps into **blank measure-on-mock fields**. It does **not** invent clearance / pad / aperture / travel mm. It does **not** invent PL/SIL / Category / stop-time / force. Geometry residual evidence must exist **before** any PL claim.

> Critical **SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**. Mushroom / E-stop topology remains **Lead TBD** (ASSUMPTION pointer only — cite `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md`, `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`).

**Identical mirrors:**  
`docs/engineering/ELIAS_SAF02_PINCH_GEOMETRY_MEASURE_ON_MOCK_PLAN_2026-09-22.md`  
`sor_sync/docs/engineering/ELIAS_SAF02_PINCH_GEOMETRY_MEASURE_ON_MOCK_PLAN_2026-09-22.md`

---

## Explicit non-claims

| Claim type | Status |
|---|---|
| Invented measured mm (clearance, pad, aperture, travel, reach) | **Forbidden — blanks only** |
| PL / SIL / Category | **Forbidden — none** |
| Measured stop-time / force N / crush bars | **Forbidden — none** |
| Close Critical SAF-02 / P-05 / C-01 / HY-02 | **No — remain OPEN** |
| Physical actuation / pressurized strike authorization | **No** |

---

## How to use this plan

1. Build / stage **Mech ABS mock** (or Lead-named fixture) — cite Ismael B06 / OB-M5 path as needed; this paper does not invent fixture mm.
2. For each field below: record **unit**, **method**, **who measured**, **date (ET)**, and **value** on the mock run sheet — **not** in this paper until measured.
3. Keep every unfilled cell labeled **ASSUMPTION — measure on mock (blank)**.
4. **Do not** argue Category/PL from empty fields. Geometry-first (Lead ACCEPTED-A).

---

## Measure-on-mock field sheet (blank ASSUMPTION)

Each row = **ASSUMPTION — measure on mock**. Value cells intentionally empty.

| Field ID | Measurand (blank for mock fill-in) | Unit (when filled) | Why it matters (geometry-first) | Gap cite | Mock value | Method / notes | Measured? |
|---|---|---|---|---|---|---|---|
| **M-PINCH-01** | Pinch **clearance / gap** at pitch hinge (worst-case finger / soft-tissue path) | mm (when filled — **not invented here**) | Residual pinch risk cannot be Category/PL-argued without measured gap evidence | G-PINCH-01 | ________ | caliper / feeler / photo scale — **TBD — Mech** | ☐ |
| **M-PINCH-02** | Pinch **clearance / gap** at rotating shoulder band (worst-case path) | mm (when filled) | Same as M-PINCH-01 at second site | G-PINCH-01 | ________ | same class | ☐ |
| **M-PINCH-03** | **Pad / guard thickness** at identified pitch-hinge pinch site | mm (when filled) | Padding residual is geometry; thickness unmeasured until mock | G-PINCH-02 | ________ | section / caliper — **TBD — Mech** | ☐ |
| **M-PINCH-04** | **Pad / guard thickness** at shoulder-band pinch site | mm (when filled) | Coverage + thickness residual | G-PINCH-02 | ________ | same class | ☐ |
| **M-PINCH-05** | **Pad / guard coverage** extent along pinch site (qualitative map OK if mm TBD) | mm or annotated photo map (when filled) | Incomplete coverage → residual aperture | G-PINCH-02 | ________ | photo + mark-up | ☐ |
| **M-PINCH-06** | Pinch **aperture** (opening that admits finger) under motion extreme — pitch | mm (when filled) | Aperture drives residual risk; **no invented mm** | G-PINCH-03 | ________ | gauge / photo — extremes **TBD — Mech** | ☐ |
| **M-PINCH-07** | Pinch **aperture** under motion extreme — yaw / carrier | mm (when filled) | Same for yaw/carrier envelope | G-PINCH-03 | ________ | same class | ☐ |
| **M-PINCH-08** | Relative **travel / stroke** through pinch zone (pitch) | mm (when filled) | Travel × aperture → exposure shape; **not** a stop-time claim | G-PINCH-04 | ________ | dial / encoder mock — **TBD** | ☐ |
| **M-PINCH-09** | Relative **travel / stroke** through pinch zone (yaw / carrier) | mm (when filled) | Same for yaw/carrier | G-PINCH-04 | ________ | same class | ☐ |
| **M-PINCH-10** | Fixture / mast **reachability** of E-stop vs pinch sites (layout distances / sightlines) | mm or qualitative layout note (when filled) | Topology still Lead TBD; layout evidence before independence narrative | G-PINCH-05 | ________ | tape / layout sketch — mushroom = **ASSUMPTION pointer only** | ☐ |
| **M-PINCH-11** | Electronic `pinch_trip` used? (**yes / no / TBD**) | enum | Sensor path optional; modality OPEN | G-PINCH-06 | ________ | Lead decision | ☐ |
| **M-PINCH-12** | If yes: sensor **modality** + fail-safe open behavior (qualitative) | text | Fail-safe open narrative for inhibit OR | G-PINCH-06 | ________ | Controls / Lead | ☐ |
| **M-PINCH-13** | Manual-reset-after-clear behavior for pinch trip (if fitted) | text / procedure ID | Latch semantics Critical OPEN | G-PINCH-07 | ________ | cite ICD latch rule | ☐ |
| **M-PINCH-14** | Interaction with presence hard-interlock and inhibit OR (priority stack note) | text | Inhibit OR membership Lead OPEN | G-PINCH-08 | ________ | cite timing paper + ICD | ☐ |
| **M-PINCH-15** | Person-adjacent / pilot gate evidence package contents (checklist IDs) | text | Safety gate before person-adjacent — criteria TBD | G-PINCH-09 | ________ | Safety / Michael | ☐ |
| **M-PINCH-16** | Force / crush **class** characterization needed? (**yes / no / TBD**) — if yes, fixture-first; **no N invented here** | enum + blank N cell if later required | Do **not** invent N bars | G-PINCH-10 | ________ / N: ________ | Safety / Mech — later if required | ☐ |

**Rule:** Any filled numeric cell must be labeled **MEASURED ON MOCK** with date (ET) and method. Until then, leave blank and keep **ASSUMPTION — measure on mock**.

---

## Geometry-first gate (before any PL claim)

```text
GEOMETRY_EVIDENCE_READY  ⟺
    M-PINCH-01..09 measured on mock (or Lead-waived with written rationale)
  ∧ M-PINCH-10 layout note complete (topology still Lead TBD)
  ∧ M-PINCH-11..14 Lead notes recorded for sensor/latch/OR (may remain TBD)
  ∧ NO PL / SIL / Category asserted from empty fields

PL_CLAIM_ALLOWED  ⟺  GEOMETRY_EVIDENCE_READY ∧ Safety/Lead assessment (OUT OF SCOPE HERE)
```

This paper does **not** assert `PL_CLAIM_ALLOWED`. Critical **SAF-02** stays **OPEN**.

---

## Digital twin reminder

Digital HIL may stim optional `pinch_trip` bool for inhibit OR V&V (**$0**). That stim does **not** fill M-PINCH-* blanks and does **not** authorize physical actuation. Cite `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md`, `ELIAS_CI_EP_ACCEPTANCE_MATH_2026-09-21.md`.

---

## Related Critical / Major (unchanged)

| ID | Severity | Note |
|---|---|---|
| **SAF-02** | **Critical OPEN** | Independent motion-enable / stop; topology Lead TBD; **no PL/SIL** |
| **P-05** | **Critical OPEN** | Fault vent / limp; quantitative after TB-04 |
| SQ-M2 (pinch) | Major | Geometry-first residual; sensor modality TBD |
| **C-01 / HY-02** | **Critical / OPEN** | Unchanged |

---

## Cross-cites

- `ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md` (**ACCEPTED-A** gaps — parent of this plan)
- `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md` (AT-PINCH-1; SF-3; topology Lead TBD)
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`
- `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md`
- `OLA_INTEGRATE_ELIAS_C01_SAF02_2026-09-21.md`
- `ELIAS_SAF02_DUAL_CHANNEL_ESTOP_TOPOLOGY_ASSUMPTION_TREE_2026-09-22.md` (companion topology ASSUMPTION tree — Lead TBD)

---

*Elias Controls & Perception under Ola — 2026-09-22. $0 ASSUMPTION measure-on-mock plan. Blank fields only. No invented mm. No PL/SIL. Critical SAF-02 / P-05 / C-01 / HY-02 remain OPEN. No PO. No NEXT_PROMPT. No SendToUser.*
