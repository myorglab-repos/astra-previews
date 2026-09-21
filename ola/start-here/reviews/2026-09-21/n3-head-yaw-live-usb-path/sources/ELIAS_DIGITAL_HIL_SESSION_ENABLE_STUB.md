# Elias — Digital HIL stub: session_enable (presence + head + inhibit)

| Field | Value |
|---|---|
| **Title** | Digital HIL stub — simulate presence + head (+ inhibit) → `session_enable` for virtual controls test |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | Ola (Lead Robotics) integrate |
| **Authority** | Michael authorized — **PAPER / DIGITAL V&V ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | DRAFT one-pager — companion to `ELIAS_CV_SYNTHETIC_DATASET_PLAN.md` + `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` |
| **Product** | AI-Powered Boxing Training System |

**Normative equation (ACCEPTED-A (1)):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```

**Signal authority:** `docs/engineering/ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` (also `sor_sync/`).  
**Controls ICD:** `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`.  
**Sensing ICD:** `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md`.

---

## Purpose

Digital hardware-in-the-loop **stub**: inject simulated `user_present`, `head_hypothesis_valid`, and `inhibit_latched` (plus optional `presence_sensor_fault` / sync quality) into the twin-adapter combinational path so **virtual controls / twin** can test session enable **without** camera, ToF, or pneumatics.

Michael push: maximize digital V&V of the enable chain **before** physical build.

---

## Explicit non-authorization

> **This stub does NOT authorize physical actuation.**  
> `session_enable == true` is **necessary for S0/S1 trainer session / twin logging intent** and is **not sufficient** for S3 physical motion or pressurized strike.  
> Presence alone forever hard-interlocks physical motion/strike. S3 still requires presence interlock + `safe_to_actuate` + C-01 + B-06 + safety (Twin ICD Staging S3) — Critical OPEN, Lead-owned.

No invented FPS, IoU, accuracy, latency, or confidence numeric bars. Head validity in S0/S1 = **qualitative** (ACCEPTED-A (8)). Latency **TBD until bench**.

---

## Stimuli → outputs (MVP)

| Stim (in) | Meaning | Fail-safe |
|---|---|---|
| `user_present` | Near-bag presence (sim of ToF preferred / PIR backup / mat optional) | Fault → **absent** |
| `head_hypothesis_valid` | Qualitative valid head/human ROI hypothesis | Invalid → session not enabled |
| `inhibit_latched` | Controls inhibit latch | Clears only on **manual reset** (sim); AI must not clear |
| `presence_sensor_fault` (optional) | Forces `user_present := false` | Normative fail-safe |
| `t_sync` quality (optional) | ok / stale / unknown | Stale → quality flag; inhibit **time-critical** fusion use |

| Out | Meaning |
|---|---|
| `session_enable` | Combinational AND above |
| `twin_overlay.presence_lamp` / `head_marker` | Idle/safe when absent or invalid |
| Log row | Same fields as dataset plan §3.3 / twin-adapter `log_episode` |

---

## Truth table — key cases

| Case | `user_present` | `head_hypothesis_valid` | `inhibit_latched` | Notes | Expected `session_enable` | Twin intent |
|---|---|---|---|---|---|---|
| Present + head | true | true | false | Happy path | **true** | Session / logging may enable; overlays OK |
| Present, no head | true | false | false | AT-F2 | **false** | Diagnostic overlay OK; session inhibited |
| Absent + head | false | true | false | Head without presence; AT-F2 | **false** | Idle/safe — **no arm play toward empty space**; presence still denies motion/strike |
| Inhibit latched | true | true | true | Latch blocks session | **false** | Session inhibited; latch holds until simulated manual reset |
| Presence fault → absent | false (forced) | true or false | false | `presence_sensor_fault` | **false** | Treat as absent; idle/safe |
| All false | false | false | false | Empty / idle | **false** | Idle |
| Inhibit + absent | false | * | true | Double inhibit | **false** | Idle + latched |

`*` = don’t care for session_enable (already false from presence or latch).

**Physical motion / strike (informative reminder — not driven by this stub):** denied whenever `user_present` is false or fail-safe absent, **regardless** of head hypothesis or `session_enable`.

---

## How to use (digital only)

1. Drive stim rows from unit tests, synthetic episode replay, or a simple HIL panel.  
2. Assert truth-table outcomes and overlay idle rules.  
3. Inject latch: confirm AI restart / network / pressure-recovery **sim** does **not** clear `inhibit_latched`.  
4. Log episodes per `ELIAS_CV_SYNTHETIC_DATASET_PLAN.md` schemas for regression.  
5. **Do not** wire this stub’s `session_enable` to fill valves, supply enable, or strike paths.

---


---

## Digital yaw command test (companion to head→yaw Blender path)

**Pointer:** `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` (docs/engineering + sor_sync).  
**Intent:** Digital V&V of **`yaw_cmd` enable / kill** for N3 Blender twin carrier yaw — **not** physical actuation.


### Assumptions (yaw path — Michael standing rule)

| Item | Label | Note |
|---|---|---|
| Detector / camera prior | **ASSUMPTION** | MediaPipe-class / OpenCV fallback — class only; no accuracy claim in HIL |
| Presence thresholds | **TBD — Lead** | Stimuli are simulated bools here; real ToF/PIR/mat thresholds not set by this stub |
| Yaw gain / mapping | **TBD — Lead** | HIL may inject `yaw_cmd` directly; map gain not invented |
| Confidence cutoffs | **TBD — Lead** | `head_hypothesis_valid` stim is qualitative / injected |
| Sync tolerances | **TBD — Lead** | Optional `t_sync` quality only; no invented ms bar |
| Idle hold-last vs zero | **ASSUMPTION** / **TBD — Lead** | Prefer zero on absent/E-stop until Lead freezes |


### Enable formula (informative digital)

```
yaw_cmd_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched ∧ ¬ e_stop_asserted
```

When `yaw_cmd_enable` is false → twin yaw path uses **hold-last or zero** (idle policy **TBD — Lead**; recommendation in path paper: prefer **zero / home-idle** on absent or E-stop). This stub does **not** freeze hold-last vs zero.

**Stimuli (add):** `head_centroid_x` (normalized, optional for enable logic), `yaw_cmd` (mapped command), `e_stop_asserted` (optional kill).  
**Out (add):** `yaw_cmd_enable`, effective twin yaw command (`yaw_cmd` passed through when enabled; else hold-last/zero).

### Truth / cases — yaw_cmd enable vs hold-last/zero

| Case | `user_present` | `head_hypothesis_valid` | `inhibit_latched` | `e_stop_asserted` | Expected `yaw_cmd_enable` | Twin yaw intent |
|---|---|---|---|---|---|---|
| Chase happy | true | true | false | false | **true** | Pass `yaw_cmd` → carrier yaw follows (directional) |
| Present, head invalid | true | false | false | false | **false** | Hold-last or zero — **no chase** on invalid head |
| Absent (+ head or not) | false | * | false | false | **false** | **Zero / idle** preferred — **no yaw chase** toward empty space |
| Inhibit latched | true | true | true | false | **false** | Kill chase — hold-last or zero |
| E-stop asserted | true | true | false | true | **false** | Kill chase — prefer **zero / home-idle** |
| Presence fault → absent | false (forced) | * | false | false | **false** | Treat as absent; idle |
| Session happy but recall | true | true | false | false | true | `session_enable` may also be true; still **not** S3 actuation |

`*` = don’t care for `yaw_cmd_enable` once presence or latch/E-stop already forces false.

**Keep prior `session_enable` truth table above unchanged.** Yaw chase is an additional digital twin path gated by the same presence / head / inhibit family.

### Explicit non-authorization (yaw)

> **Digital yaw command test does NOT authorize physical yaw rotor motion or pressurized strike.**  
> Twin carrier yaw under these cases is **digital V&V / pedagogy** only. Hardware handoff requires presence + inhibit policy + **Lead READY**. F-01 pitch lock is **not** required for digital twin yaw; F-01 + F-05 remain required before pressurized strike (S3) per ACCEPTED-A.

No invented FPS, accuracy, IoU, latency, or gain numbers — mapping gain **TBD — Lead**. Presence thresholds, confidence cutoffs, and sync tolerances likewise **TBD — Lead** (see Assumptions above).

## Pointers

| Doc | Use |
|---|---|
| `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` | Full signal list, fail-safes, S0/S1 vs S3 applicability |
| `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` | Head → carrier yaw Blender path; Assumptions / `yaw_cmd` |
| `ELIAS_CV_SYNTHETIC_DATASET_PLAN.md` | Dataset / logging / digital vs bench split |
| `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` | Inhibit sources, presence forever, limp/E-stop concepts |
| Draft B AT-F1/F2, AT-P4, AT-S1 | Acceptance language (latency TBD) |

---

## Ownership

| Role | Owns |
|---|---|
| **Ola** | Integrate; Critical; READY; **NEXT_PROMPT** |
| **Elias** | This stub language only |

**NO PO. NO NEXT_PROMPT.** Critical hardware remains OPEN.

---

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate. Identical mirror: `sor_sync/ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md`. Does not authorize physical actuation.*
