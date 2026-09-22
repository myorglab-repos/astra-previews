# Live camera → virtual bag twin (training / test ICD)

| Field | Value |
|---|---|
| **Owner draft** | Ola (original MVP) + Elias Controls deepen under Ola |
| **Date** | 2026-09-21 (MVP simplified per Michael); **ACCEPTED-A (paper)** deepen 2026-09-21 ~22:42 ET |
| **Status** | **ACCEPTED-A (paper)** INTERFACE PLAN / ICD deepen — MVP is simple; **DIGITAL_TWIN_ONLY**. Cite `OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. Critical / HY-02 **OPEN**. Not a SOTA CV research program |
| **Related** | Track A Blender SoR; C-01 Track B; `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`; HY-03 integrate; START_HERE readiness |

> **ACCEPTED-A (paper) — 2026-09-21 ~22:42 ET.** Lead answers folded from `docs/engineering/OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. **Critical C-01 / SAF-02 / P-05 and HY-02 remain OPEN.** No PO. No NEXT_PROMPT. No invented metrics.

**Identical mirrors:**  
`docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md`  
`sor_sync/docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md`

**Normative companions:** `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`, `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md`, `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`, `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md`, `OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`.

---

## Plain language

**MVP (Michael):** the camera mainly watches a **human / head section**. What we need to *trigger* trainer behavior is basically **body tracking / presence** — pair that with a **sensor that detects a body close to the bag**, and we're good. Keep it simple. Full skeleton / glove CV can come later.

**Session enable (ACCEPTED-A):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
Presence forever hard-interlocks **physical motion / pressurized strike**. This ICD does **not** authorize physical actuation from perception.

---

## MVP sensing stack (preferred)

| Channel | What it does | Why |
|---|---|---|
| **Camera — head / human ROI** | Sees the person's head (and upper body crop) for aim / height / facing cues and for training clips | Matches product camera placement; bounded problem |
| **Near-bag body presence sensor** | Detects that someone is in the work envelope next to the bag | Simple, robust "user present / in range" gate — does not need fancy pose |
| Twin adapter | Maps `user_present` + head cues → twin overlays / height preset hints / logging | Ola + controls |

**MVP trigger logic (intent):**  
`user_present` (proximity) AND camera sees a valid human/head hypothesis → enable trainer session / twin logging.  
No presence → idle / safe (no arm play toward empty space).

**ASSUMPTION (live USB interim):** Detector class may be OpenCV Haar; `head_hypothesis_valid` may require **one face + operator spot-check** — qualitative S0/S1 only. Presence on digital path may be **`SIMULATED_BOOL_NOT_HARDWARE`** until hardware AT (cite presence scout / live-USB ICD).

---

## Goals

1. **Train/test** — record head-ROI video + presence timestamps + twin state for simple models.  
2. **Live overlay** — camera + presence drive the virtual bag without claiming full athletic CV.  
3. **Control (later)** — only after safety + C-01; presence remains a hard interlock forever.

## Non-goals (MVP)

- Full-body multi-joint pose as a product requirement  
- Glove tracking / punch-type classification as day-one blockers  
- Using Track A scripted films as proof of real vision  
- Actuating soft arms from unverified perception  
- Invented FPS / accuracy / IoU / latency / force bars  

---

## Architecture

```
Protected camera (head/human ROI) ──┐
                                    ├──→ Capture / sync → Twin adapter → Blender twin + logs
Near-bag presence sensor ───────────┘         ↓
                                         Dataset (clips + presence flags → Snowflake metadata later)
```

| Block | MVP responsibility | Owner |
|---|---|---|
| Camera mount / cover | Head-height ROI, protected | Mech |
| Presence sensor | ToF preferred / PIR backup / mat optional — TBD; fail-safe "absent" | Mech + controls |
| Light perception | Head/human detect in ROI (confidence + bbox) — confidence cutoff **TBD — Lead** | CV→twin agent / specialist |
| Twin adapter | `user_present`, `head_bbox`, optional facing | Ola + controls |
| Safety | No physical strike unless presence + safe_to_actuate | Safety |

**Live USB interim path (office / gym spot-check):** see `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` and HY-02 checklist. Office USB **YES** for first HY-02 qualitative L/R per Lead (`OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). HY-02 remains **OPEN**.

---

## Interfaces (deepen)

| Interface | Direction | Contract |
|---|---|---|
| Camera / clip capture | in | OpenCV index or clip; packet `schema_rev=head-yaw-v1` when using accepted bridge |
| Presence | in | Hardware ToF preferred later; until then simulated bool tagged |
| Twin adapter inputs | in | `t_sync`, `user_present`, `head_hypothesis` / validity, inhibit / e-stop stim |
| Twin adapter outputs | out | Overlay; `session_enable`; `yaw_cmd` (digital); `log_episode` |
| Mapping (digital) | config | Lead Track A freeze — see HY-03 table below |
| Privacy | out | `recording_enabled=False` default; JSON log opt-in |

### HY-03 Lead Track A digital freeze (cite — NOT measured hardware bars)

Cite: `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`.

| Parameter | Lead freeze | Label |
|---|---|---|
| `normalization` | `frame_fraction_0_to_1` | Lead Track A freeze |
| `sign` | `+1` | **NORMATIVE** sign: positive image x → +Z yaw from −Y home |
| `gain_deg_per_signed_x` | `30.0` | **NOT-measured-hardware-limit** / NOT physical performance bar |
| `clamp_deg` | `30.0` (±30) | **NOT-measured-hardware-limit** |
| `idle_policy` | `home_zero` | ACCEPTED-A / freeze |
| `watchdog_s` | `2.0` | **NOT-measured-hardware-limit** / NOT latency product bar |

Formula (digital): `yaw_cmd = clamp(sign * gain * (2*cx-1), ±clamp)` only when session gates + configured; else `0.0`.

---

## Twin adapter ICD (MVP minimum)

**Inputs:**
- `t_sync`  
- `user_present` (bool) — from proximity sensor (authoritative for "someone at the bag")  
- `head_hypothesis` — bbox + confidence in camera ROI (optional facing later)  
- `inhibit_latched`, `e_stop_asserted`, `presence_sensor_fault`, `sync_quality` (controls / HIL)

**Outputs:**
- Twin overlay (head marker / presence lamp)  
- Session enable / inhibit  
- Logged episode for training  
- Digital `yaw_cmd` / `yaw_cmd_enable` when head path enabled (S0/S1 twin only)

---

## Acceptance-test outline (qualitative — no numeric bars)

| Case | Intent | Pass language |
|---|---|---|
| Walk-in | Enter envelope | `user_present` becomes true (latency **TBD — Lead** — do not invent ms) |
| Walk-away | Leave envelope | `user_present` false; twin idle / `home_zero` |
| Empty bag | No person | No false presence under normal gym lighting — **qualitative**; FP rate **TBD — Lead** |
| Single-face ROI | Person present | Head hypothesis spot-check valid when operator prior used — **not** Olympic accuracy |
| Multi-face / no face | Invalid head | Session not enabled from head path |
| Presence fault | Fault bit | Force absent |
| Inhibit / E-stop stim | Digital HIL | Session/yaw kill; latch manual reset only after clear |
| Stale sync / watchdog | Digital | Quality flag; idle/`home_zero`; `watchdog_s=2.0` digital freeze — **NOT measured HW limit** |

CI synthetic pack: `ELIAS_SYNTHETIC_HEAD_PRESENCE_CI_EPISODE_PACK.md`.

---

## Fault table

| Fault | Response | Notes |
|---|---|---|
| Camera open fail | Fail-fast or `SKIPPED_NO_CAMERA` | Not a silent invent-camera |
| No face | Head invalid | Session false from head AND |
| Multi-face | Head invalid | ASSUMPTION one-face rule |
| Stale sync | Quality flag; no chase | Tolerance TBD—Lead |
| Presence fault→absent | `user_present:=false` | Forever interlock for motion/strike |
| Inhibit latch | Session false | Manual reset after clear only |
| E-stop sim | Kill yaw enable; idle | SAF-02 hardware topology Lead TBD |
| Watchdog | Idle `home_zero` | Digital `2.0 s` freeze — NOT measured HW limit |

---

## Staging

| Stage | Scope |
|---|---|
| S0 | Record head-ROI + presence flags offline |
| S1 | Live presence + head overlay on twin (no arm motion) |
| S2 | Twin commands simulated continuum from simple cues |
| S3 | Physical arms — only with presence interlock + C-01 + B-06 + safety |

---

## Agent desk implication

CV→twin agent focuses on **head ROI + presence fusion**, not a research pose stack. Human CV hire still Stephen-gated; bot desk can paper the ICD and twin hooks now.

## Snowflake

Later: metadata for clips + `user_present` timelines — not inventing a corpus today.

## Track A demarcation

Prescribed Blender punches remain teaching aids. Presence + head camera is the **first real sensing path**.

---

## Amendment 2026-09-21 ~22:35 ET — Elias EXECUTE NOW deepen

- Added Interfaces, Acceptance-test outline, Fault table.
- Baked HY-03 Lead Track A digital freeze with **NOT-measured-hardware-limit** labels.
- Sign convention **NORMATIVE** (positive image x → +Z yaw from −Y home).
- `session_enable` ACCEPTED-A retained; Haar / one-face+operator = **ASSUMPTION**.
- **DIGITAL_TWIN_ONLY**; no physical actuation; Critical / HY-02 remain **OPEN**.
- Cross-cite live-USB ICD, Digital HIL stub, HY-02 checklist, synthetic CI pack.

---


---

## Amendment 2026-09-21 ~22:42 ET — ACCEPTED-A (paper) six-packet

Cite: `docs/engineering/OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. **ACCEPTED-A (paper)** on EXECUTE NOW six-packet set. Critical **C-01 / SAF-02 / P-05** and **HY-02** remain **OPEN**. `CAMERA_PRESENT_NO_SINGLE_FACE` = normative checklist token where taxonomy applies (code emit may lag).

---

*Ola MVP ICD + Elias ACCEPTED-A (paper) deepen 2026-09-21 ~22:42 ET. PAPER ONLY. No PO. No NEXT_PROMPT. Critical OPEN.*
