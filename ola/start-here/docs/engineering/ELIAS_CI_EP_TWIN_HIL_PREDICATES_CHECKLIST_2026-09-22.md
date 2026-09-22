# Elias — CI-EP twin/HIL predicates ready checklist (2026-09-22)

| Field | Value |
|---|---|
| **Title** | CI-EP boolean predicates ready checklist for twin/HIL — pass/fail checkboxes (synthetic only) |
| **Rev** | 2026-09-22 (America/New_York) — $0 ASSUMPTION / synthetic checklist |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Authority** | Michael authorized $0 paper via Ola; **NO PO**; **NO NEXT_PROMPT**; **NO SendToUser** |
| **Status** | **Optional companion checklist** — aligns to CI-EP-* normative gates. Synthetic only. Does **not** authorize physical actuation. Critical **SAF-02 / P-05 / C-01 / HY-02** remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **Cite ACCEPTED-A math:** `ELIAS_CI_EP_ACCEPTANCE_MATH_2026-09-21.md` (predicates normative).  
> **Cite pack:** `ELIAS_SYNTHETIC_HEAD_PRESENCE_CI_EPISODE_PACK.md`, `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md`.  
> This checklist is **operator/HIL ready-state** boxes — **not** measured FPS/accuracy/IoU/latency bars. Checkboxes start unchecked until twin/HIL run records honest pass/fail.

**Identical mirrors:**  
`docs/engineering/ELIAS_CI_EP_TWIN_HIL_PREDICATES_CHECKLIST_2026-09-22.md`  
`sor_sync/docs/engineering/ELIAS_CI_EP_TWIN_HIL_PREDICATES_CHECKLIST_2026-09-22.md`

---

## Shared definitions (cited — do not re-freeze)

```text
session_enable := user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
IF presence_sensor_fault THEN user_present := false
watchdog_s := 2.0   # Lead Track A DIGITAL freeze — NOT measured HW latency bar
idle_policy := home_zero
```

**Pass:** predicate true on episode end. **Fail:** predicate false or required idle/`home_zero` not observed.

---

## Normative set G — ready / pass / fail checkboxes (synthetic)

| Gate | Stim intent (short) | Predicate ready (docs/stim wired) | PASS ☐ | FAIL ☐ | Notes / log path |
|---|---|---|---|---|---|
| **CI-EP-EMPTY** | `user_present=false`; head invalid | ☐ | ☐ | ☐ | |
| **CI-EP-WALK-IN** | presence false→true then valid head | ☐ | ☐ | ☐ | qualitative timeline — no FPS |
| **CI-EP-WALK-AWAY** | presence true→false | ☐ | ☐ | ☐ | no chase toward empty |
| **CI-EP-SINGLE-FACE-ROI** | one face / head stim true + present | ☐ | ☐ | ☐ | **NO** accuracy/IoU bar |
| **CI-EP-MULTI-FACE-INVALID** | `face_candidates>1` / head invalid | ☐ | ☐ | ☐ | session_enable false |
| **CI-EP-PRESENCE-FAULT-ABSENT** | `presence_sensor_fault=true` | ☐ | ☐ | ☐ | forced absent |
| **CI-EP-INHIBIT-LATCHED** | `inhibit_latched=true` + present+head | ☐ | ☐ | ☐ | manual reset after clear only |
| **CI-EP-ESTOP-SIM** | `e_stop_asserted=true` | ☐ | ☐ | ☐ | yaw_cmd_enable false; prefer home_zero |
| **CI-EP-STALE-SYNC** | `sync_quality ∈ {stale,unknown}` | ☐ | ☐ | ☐ | no effective yaw chase |
| **CI-EP-WATCHDOG-IDLE** | gap > digital `watchdog_s=2.0` | ☐ | ☐ | ☐ | digital freeze — not HW bar |

```text
PACK_PASS  ⟺  ∀ g ∈ G: PASS(g) = true
```

| Aggregate | Ready | PASS ☐ | FAIL ☐ |
|---|---|---|---|
| **PACK_PASS** (all of G) | ☐ | ☐ | ☐ |

Optional companion stims (present+no-head; head-without-presence; inhibit+manual-reset) — **not** required for `PACK_PASS` unless Lead expands G:

| Optional stim | Ready ☐ | PASS ☐ | FAIL ☐ |
|---|---|---|---|
| Present + no head | ☐ | ☐ | ☐ |
| Head without presence | ☐ | ☐ | ☐ |
| Inhibit + manual-reset-after-clear | ☐ | ☐ | ☐ |

---

## Pre-flight (twin/HIL only)

| Item | Ready ☐ |
|---|---|
| Digital HIL / twin stim path available ($0) | ☐ |
| `session_enable` formula implemented per stub | ☐ |
| Inhibit latch: AI/network/pressure-recovery cannot clear | ☐ |
| E-stop sim kills chase / prefers `home_zero` | ☐ |
| Watchdog idle uses digital `watchdog_s=2.0` | ☐ |
| Debounce ms **not** treated as frozen (TBD — Lead) | ☐ |
| No physical actuation / fill / strike armed | ☐ |

---

## Explicit non-claims

| Claim type | Status |
|---|---|
| FPS / accuracy / IoU / confidence / measured latency | **Forbidden — none** |
| PL / SIL / stop-time / force | **Forbidden — none** |
| Invented L/R gym results | **Forbidden — none** |
| Close Critical SAF-02 / P-05 / C-01 / HY-02 | **No — remain OPEN** |
| Physical actuation authorization | **No** |

---

## Cross-cites

- `ELIAS_CI_EP_ACCEPTANCE_MATH_2026-09-21.md` (**ACCEPTED-A**)
- `ELIAS_SYNTHETIC_HEAD_PRESENCE_CI_EPISODE_PACK.md`
- `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md`
- `ELIAS_PRESENCE_INHIBIT_SESSION_ENABLE_TIMING_ASSUMPTION_2026-09-21.md`
- `ELIAS_DEBOUNCE_MS_ASSUMPTION_SENSITIVITY_2026-09-22.md` (debounce TBD — Lead)
- `OLA_INTEGRATE_ELIAS_DIGITAL_MATH_PACK_2026-09-21.md`
- `OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`

---

*Elias Controls & Perception under Ola — 2026-09-22. Synthetic twin/HIL checklist only. Aligns to CI-EP-* math. Critical OPEN. No PO. No NEXT_PROMPT. No SendToUser.*
