# Elias — SAF-02 dual-channel E-stop topology ASSUMPTION decision tree (2026-09-22)

| Field | Value |
|---|---|
| **Title** | Dual-channel E-stop topology options — ASSUMPTION decision tree (Lead TBD — not a freeze) |
| **Rev** | 2026-09-22 (America/New_York) — $0 ASSUMPTION paper |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Authority** | Michael authorized $0 paper via Ola; **NO PO**; **NO NEXT_PROMPT**; **NO SendToUser** |
| **Status** | **ASSUMPTION decision tree** — Lead TBD — **not a freeze**. Does **not** invent PL/SIL / Category / stop-time. Critical **SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **Cite:** `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md` (topology Lead TBD; mushroom mast = ASSUMPTION pointer only).  
> **Cite:** `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` (SAF-02 in-progress; handheld ≠ E-stop).  
> **Cite:** `ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md` / measure-on-mock plan (geometry-first before PL).

> Every branch below is **ASSUMPTION — candidate for Lead discussion**. Selecting a branch in this paper does **not** freeze SAF-02. **No catalog SKUs.** **No PL/SIL invented.**

**Identical mirrors:**  
`docs/engineering/ELIAS_SAF02_DUAL_CHANNEL_ESTOP_TOPOLOGY_ASSUMPTION_TREE_2026-09-22.md`  
`sor_sync/docs/engineering/ELIAS_SAF02_DUAL_CHANNEL_ESTOP_TOPOLOGY_ASSUMPTION_TREE_2026-09-22.md`

---

## Explicit non-claims

| Claim type | Status |
|---|---|
| PL / SIL / Category | **Forbidden — none** |
| Measured stop-time / force | **Forbidden — none** |
| Catalog SKU / part number freeze | **Forbidden — none** |
| SAF-02 CLOSED / topology freeze | **No — Lead TBD — OPEN** |
| Handheld / portable touchscreen = E-stop | **Forbidden** (C-04 / H-15) |

---

## Root (normative reminders — not freezes of topology)

```text
SAF-02_TOPOLOGY          := TBD — Lead
MUSHROOM_MAST_POINTER    := ASSUMPTION pointer only (single visible mushroom on fixture mast — NOT a Category claim)
HANDHELD_NE_ESTOP        := true   # portable touchscreen ≠ E-stop
INDEPENDENCE_FROM_UI_CV  := required intent (stop path must not wait on UI or CV/AI)
RESET_RULE               := manual reset after clear; reset does not start motion; AI/network/pressure-recovery must not clear latch
```

---

## Decision tree (ASSUMPTION branches — Lead TBD)

### Branch A — Station count

```text
A0  How many operator-reachable E-stop stations on MVP fixture?
    ├─ A1  SINGLE station (ASSUMPTION candidate)
    │       • One reachable actuator (mushroom ASSUMPTION pointer common)
    │       • Layout reachability still measure-on-mock (M-PINCH-10)
    │       • Dual-channel wiring may still apply INSIDE the single station (see Branch B)
    │       • Freeze status: NOT frozen — Lead TBD
    │
    └─ A2  DUAL stations (ASSUMPTION candidate)
            • Two reachable actuators (e.g. mast + alternate approach side) — qualitative only
            • Improves approach coverage narrative; does NOT invent PL
            • Independence / common-cause between stations: Lead TBD
            • Freeze status: NOT frozen — Lead TBD
```

| Node | Label | Note |
|---|---|---|
| A1 | **ASSUMPTION — candidate** | Aligns with prior mushroom-mast ASSUMPTION pointer language |
| A2 | **ASSUMPTION — candidate** | Dual physical reach points — not a freeze |

**Lead pick:** ________ (blank — not filled by Elias)

---

### Branch B — Channel count (wiring / contact architecture — qualitative)

```text
B0  Channel count on the stop path (qualitative architecture — NOT Category/PL)
    ├─ B1  SINGLE-channel path (ASSUMPTION candidate)
    │       • Simpler wiring narrative
    │       • Common-cause / single-fault residual: Lead / Safety TBD
    │       • Does NOT authorize a PL claim from simplicity
    │
    ├─ B2  DUAL-CHANNEL path (ASSUMPTION candidate)  ← tree title focus
    │       • Two channels whose disagreement / open fails safe (qualitative intent)
    │       • Cross-monitor / discrepancy → inhibit/latch narrative: Lead TBD
    │       • Does NOT invent Category / PL / SIL from “dual”
    │
    └─ B3  Dual-channel + monitored feedback (ASSUMPTION candidate)
            • Adds feedback verification of contactor / valve / vent state (qualitative)
            • Feedback criteria TBD — Lead / Safety
            • Still NOT a PL freeze
```

| Node | Label | Freeze status |
|---|---|---|
| B1 | **ASSUMPTION — candidate** | **Not frozen** |
| B2 | **ASSUMPTION — candidate** | **Not frozen** |
| B3 | **ASSUMPTION — candidate** | **Not frozen** |

**Lead pick:** ________

---

### Branch C — Latch / reset semantics (ties to ICD — Critical OPEN detail)

```text
C0  Latch / reset after E-stop assert
    ├─ C1  Latch on assert; clear only after fault/stop clear AND manual reset
    │       (ASSUMPTION candidate — aligns with ICD latch rule narrative)
    │       • Reset ≠ arm; arm is separate deliberate action
    │       • AI / network / pressure-recovery MUST NOT clear
    │
    ├─ C2  Separate E-stop release vs inhibit latch reset (ASSUMPTION candidate)
    │       • Physical button release may be necessary but not sufficient
    │       • Explicit second reset step — procedure TBD — Lead
    │
    └─ C3  (Forbidden narrative) Auto-clear on power cycle / AI restart / network recover
            • REJECT for product safety narrative — cite ICD / H-14
```

| Node | Label | Status |
|---|---|---|
| C1 | **ASSUMPTION — candidate** (ICD-aligned) | Critical OPEN detail — **not frozen by this paper** |
| C2 | **ASSUMPTION — candidate** | Lead TBD procedure |
| C3 | **Rejected narrative** | Must not clear |

**Lead pick:** ________

---

### Branch D — Fail-safe vent relation (qualitative — P-05 OPEN)

```text
D0  Relation of E-stop path to fail-safe vent / limp (P-05 — quantitative after TB-04)
    ├─ D1  E-stop asserts supply inhibit AND commands Lead-approved vent path (ASSUMPTION candidate)
    │       • Qualitative intent only — no invent droop / stop-time / pressure bars
    │
    ├─ D2  E-stop asserts supply inhibit; vent ownership separate but concurrent policy (ASSUMPTION candidate)
    │       • Coordination timing TBD — Lead; no invented ms
    │
    └─ D3  E-stop UI-only / soft-only without supply/vent path
            • REJECT for SAF-02 independence intent — handheld ≠ E-stop already
```

| Node | Label | Note |
|---|---|---|
| D1 | **ASSUMPTION — candidate** | P-05 remains **OPEN**; no quantitative bars |
| D2 | **ASSUMPTION — candidate** | Coordination TBD — Lead |
| D3 | **Rejected narrative** | Conflicts with independence intent |

**Lead pick:** ________

---

## Composite ASSUMPTION sketch (example only — not a freeze)

```text
EXAMPLE_COMPOSITE (ASSUMPTION sketch for discussion — NOT Lead freeze):
  A1 (single station) + B2 (dual-channel wiring) + C1 (latch + manual reset) + D1 (inhibit + vent)
```

Any other A×B×C×D combination remains discussable. **Only Lead** freezes via integrate / ICD amendment.

---

## Independence checklist (qualitative — blanks for Lead)

| Check | Intent | Lead note |
|---|---|---|
| Stop path independent of handheld UI | Required intent | ________ |
| Stop path independent of CV/AI service | Required intent | ________ |
| Common-cause between dual channels addressed | If B2/B3 chosen | ________ |
| Layout reachability vs pinch sites | Measure-on-mock | cite M-PINCH-10 |
| Person-adjacent gate before relying on topology narrative | Safety / Michael | ________ |

---

## Related Critical (unchanged)

| ID | Status |
|---|---|
| **SAF-02** | **OPEN** — topology Lead TBD |
| **P-05** | **OPEN** — vent/limp quantitative after TB-04 |
| **C-01** | **OPEN** |
| **HY-02** | **OPEN** |

---

## Cross-cites

- `ELIAS_SAF02_P05_SAFETY_QUALIFICATION_PAPER.md`
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`
- `ELIAS_SAF02_PINCH_GEOMETRY_ASSUMPTION_GAPS_2026-09-21.md`
- `ELIAS_SAF02_PINCH_GEOMETRY_MEASURE_ON_MOCK_PLAN_2026-09-22.md`
- `ELIAS_PRESENCE_INHIBIT_SESSION_ENABLE_TIMING_ASSUMPTION_2026-09-21.md`
- `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md`
- `OLA_INTEGRATE_ELIAS_C01_SAF02_2026-09-21.md`

---

*Elias Controls & Perception under Ola — 2026-09-22. $0 ASSUMPTION decision tree. Lead TBD — not a freeze. No PL/SIL. No catalog SKUs. Critical SAF-02 / P-05 / C-01 / HY-02 remain OPEN. No PO. No NEXT_PROMPT. No SendToUser.*
