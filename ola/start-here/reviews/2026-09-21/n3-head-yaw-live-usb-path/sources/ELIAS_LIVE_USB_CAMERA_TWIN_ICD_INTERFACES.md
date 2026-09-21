# Live USB camera → twin ICD interfaces (head path)

| Field | Value |
|---|---|
| **Title** | Live USB camera → virtual-bag twin ICD interfaces (head path feeding the accepted bridge) |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | Ola (Lead Robotics) integrate |
| **Authority** | Michael execute — **PAPER ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | DRAFT — ICD deepen against Twin ICD + head→yaw path + twin-adapter table; **not a code change**. Critical / HY-02 gym residual remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

**Normative sources (read order):**
- `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` — MVP camera = head/human ROI; presence = on-switch; S0–S3; no physical strike from unverified perception
- `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` — head centroid → `yaw_cmd` digital twin; Assumptions / non-goals
- `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` — signal names, fail-safes, S0/S1 vs S3
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` — session_enable; presence forever
- `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md` — digital stim / yaw enable truth cases
- Existing software (pointer only, **no edit from this desk**): `sor_sync/reviews/n3-head-track-yaw-bridge/capture_head.py` (`--camera`)

**Session enable (ACCEPTED-A (1)):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
Presence forever hard-interlocks **physical motion / pressurized strike**. This paper does **not** authorize physical actuation from perception.

**Michael 2026-09-21 09:37 ET:** keep building **outside virtual media**; USB camera **may** be needed later for gym check **but do not wait**. **HY-02 residual stays OPEN** until qualitative gym spot-check; software path proceeds with **`SKIPPED_NO_CAMERA` allowed**.

**No invented numbers.** No FPS, accuracy, IoU, latency, gain, or confidence floors. Priors tagged **ASSUMPTION** or **TBD — Lead**.

Identical mirrors: `docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` and `sor_sync/docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`.

---

## Summary

This paper deepens the **live USB head path** that feeds the accepted twin-adapter / `capture_head.py` bridge. Scope is **`DIGITAL_TWIN_ONLY`**. Packet `schema_rev` is **`head-yaw-v1`**. Live USB sets `source_kind = USB_camera`. Detector prior is **OpenCV Haar** (**ASSUMPTION** — class only, not an accuracy claim). `head_hypothesis_valid` requires **operator `--head-spotcheck-approved` AND exactly one face** (**ASSUMPTION**). Until presence hardware is on the same path, `user_present` may be **`SIMULATED_BOOL_NOT_HARDWARE`** (`--sim-present` / timeline). **No webcam media recording by default**; JSON logs are **opt-in**. S0/S1 digital twin is OK with **USB or clip**. **HY-02 residual remains OPEN** until a qualitative gym spot-check; the software path may continue under **`SKIPPED_NO_CAMERA`** and **must not block** waiting for a camera. Astra/Codex consume the signal table and fail-safes below — this file is **ICD deepen, not a code change**.

---

## Findings (severity)

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| USB-C1 | **Critical — OPEN** | Perception / USB head path does **not** authorize physical actuation, fill, or strike. `session_enable` true is not S3. | Do not close. Presence forever interlocks motion/strike. |
| USB-C2 | **Critical — OPEN** | Inhibit / SAF-02 / P-05 / B-06 F-01/F-05/F-08 remain Lead-owned. Live USB does not satisfy them. | Out of this ICD. |
| USB-M1 | **Major — HY-02 OPEN** | **HY-02 residual stays OPEN** until a **qualitative gym spot-check** (person in ROI / empty bag / walk-away idle). No numeric accuracy/FPS/IoU bar. | Gym check may use a USB camera later — **do not wait** to continue software. |
| USB-M2 | **Major** | Software continuation name: **`SKIPPED_NO_CAMERA` allowed**. Clip / HIL / simulated presence remain valid S0/S1 digital paths when no USB device is present. | Do not treat missing camera as a software blocker. |
| USB-M3 | **Major** | Live USB presence is **not hardware** until the presence scout lands. Default in `capture_head.py`: `presence_source = SIMULATED_BOOL_NOT_HARDWARE`. | Keep the tag visible on packets / logs. |
| USB-I1 | **Info** | `n3-head-track-yaw-bridge/capture_head.py --camera` already exists under reviews. Ola flipped that pass’s NEXT_PROMPT; **Elias does not write NEXT_PROMPT**. | This paper does **not** change that code. |
| USB-I2 | **Info** | Privacy: `recording_enabled = False`; `media_uri = None`; `--log` is local JSONL opt-in only. | No webcam media by default. |

---

## Draft ICD / test language

### 1. Scope of the live USB head path

```
USB camera (OpenCV VideoCapture index)
        │   ASSUMPTION: Haar frontal-face class
        ▼
capture_head.py --camera
        │   schema_rev = head-yaw-v1
        │   scope = DIGITAL_TWIN_ONLY
        │   source_kind = USB_camera
        ▼
derive()  (accepted bridge combinational layer)
        │   session_enable, yaw_cmd, yaw_cmd_enable
        ▼
Twin adapter → N3 Blender overlays / logs   (S0/S1)
        ✗  not to valves / strike
```

| Allowed now | Not allowed by this paper |
|---|---|
| S0 clip / synthetic replay | Physical yaw rotor motion |
| S1 live USB **or** clip → twin overlay / yaw pedagogy | Pressurized strike / fill |
| `SKIPPED_NO_CAMERA` software path (clip + HIL stim) | Claiming gym CV performance |
| Opt-in JSONL (`--log`) | Webcam media recording by default |
| Simulated presence until hardware | Using camera as `user_present` |

**Code pointer (ICD only):** `sor_sync/reviews/n3-head-track-yaw-bridge/capture_head.py` — `--camera <index>` mutually exclusive with `--clip`. This paper does **not** modify that tree.

### 2. Assumptions (Michael standing rule)

| Item | Label | Statement |
|---|---|---|
| Detector class (live USB path) | **ASSUMPTION** | OpenCV Haar `haarcascade_frontalface_default.xml` as implemented in `capture_head.py`. Class only — **not** a pinned accuracy, IoU, or FPS claim. Head-path paper’s MediaPipe-class remains an **alternate class**, not required for this USB ICD. |
| Multi-face | **ASSUMPTION** | `len(boxes) == 1` else invalid (no identity tracking). |
| `head_hypothesis_valid` | **ASSUMPTION** | `box is not None` **and** operator `--head-spotcheck-approved`. Qualitative S0/S1 only (ACCEPTED-A (8)). Confidence field is logged `None`. Cutoff **TBD — Lead**. |
| Presence on USB path | **ASSUMPTION** | `presence_source = SIMULATED_BOOL_NOT_HARDWARE` until hardware `user_present` is wired. `--sim-present` or `--timeline` inject the bool. |
| `head_centroid_x` | **ASSUMPTION** / **TBD — Lead** | `(x + w/2) / frame_width` in `[0,1]` as coded. Signed-offset freeze = Lead. |
| Yaw gain / clamps / units | **TBD — Lead** | `yaw_cmd = map(head_centroid_x)` via `derive` — **no invented gain**. |
| Sync tolerance | **TBD — Lead** | USB `t_sync` is monotonic-since-start; clip uses `seq/fps`. No invented ms bar. |
| FOV / mount / index | **TBD — Lead** | USB index and gym mount not frozen. Do not wait on them for software. |
| Idle hold-last vs zero | **ASSUMPTION** / **TBD — Lead** | Prefer zero/home on absent or E-stop (head-path paper). `capture_head.py` sends a stop packet (`user_present=false`, head invalid) on clean exit. |
| Twin transport | **ASSUMPTION** | Local UDP/JSON when `--send` (same as head-path default). |

### 3. Explicit signal table — live USB head path → accepted bridge

**Packet constants (live USB):**

| Field | Value on `--camera` path |
|---|---|
| `schema_rev` | `head-yaw-v1` |
| `scope` | `DIGITAL_TWIN_ONLY` |
| `source_kind` | `USB_camera` |
| `presence_source` | `SIMULATED_BOOL_NOT_HARDWARE` (until hardware) |
| `head_validity_rule` | `ASSUMPTION_one_face_plus_operator_spotcheck` |
| `recording_enabled` | `False` (no webcam media by default) |
| `privacy_mode` | `local_default` |
| `media_uri` | `None` |
| `performance_claim` | `NONE` (script stdout) |

**Map: `capture_head` packet → twin-adapter signals**

| Packet field (`capture_head.py`) | Twin-adapter signal | Direction | Type / source on live USB | Fail-safe / notes |
|---|---|---|---|---|
| `t_sync` | `t_sync` | in | USB: `monotonic - start`; clip: `seq/fps` | Stale/unknown → quality flag; time-critical fusion inhibit **TBD — Lead** (no invented ms) |
| `sync_quality` | `t_sync` quality flag | in | Default `ok`; timeline may override | Not a latency claim |
| `user_present` | `user_present` | in | `--sim-present` or timeline; **not** ToF until hardware | Fault/absent → false; **forever** hard-interlocks physical motion/strike |
| `presence_sensor_fault` | `presence_sensor_fault` | in | Timeline / default `False` | Fault → force `user_present := false` |
| `head_hypothesis` `{bbox, confidence}` | `head_hypothesis` | in | Haar bbox or `None`; `confidence=None` | Invalid/absent → session not enabled; **ASSUMPTION** detector |
| `head_hypothesis_valid` | `head_hypothesis_valid` | derived in | **one face** ∧ `--head-spotcheck-approved` | Operator flag is part of the qualitative prior — not an accuracy bar |
| `head_centroid_x` | `head_centroid_x` | derived in | Normalized `[0,1]` or `null` | Null when hypothesis invalid |
| `derive(...)` → `yaw_cmd` | `yaw_cmd` | out | Map from centroid when enable **TBD — Lead** gain | Enable false → hold-last or zero (Lead idle); paper does **not** actuate hardware |
| `derive(...)` → `yaw_cmd_enable` | `yaw_cmd_enable` | derived out | `user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched ∧ ¬ e_stop_asserted` | False → no yaw chase |
| `derive(...)` → `session_enable` | `session_enable` | out | ACCEPTED-A AND | Necessary for S0/S1 session intent; **not** S3 |
| `inhibit_latched` | `inhibit_latched` | in | Timeline / default `False` | Latch clears only on manual reset (ICD); AI must not clear |
| `e_stop_asserted` | `e_stop_asserted` | in | Timeline / default `False` | Handheld UI ≠ E-stop; stim only on this digital path |
| `--preview` overlay | `twin_overlay.head_marker` / `presence_lamp` | out (local) | OpenCV rectangle + “SIM presence \| DIGITAL TWIN ONLY” | Local preview ≠ Blender overlay; twin overlay is adapter/receiver |
| `--send` UDP JSON | twin drive | out | Host/port from config | `--wait-ack` is **clip-only** digital integration test — **not** live timing evidence |
| `--log` JSONL | `log_episode` | out | Opt-in local JSONL | **No** webcam media; quality flags on fault/stale |
| stop packet on exit | idle / safe | out | `user_present=false`, head invalid | Clean EOF; crash handled by receiver watchdog (code comment) |

`face_candidates`, `stream_id`, `seq`, `episode_id`, `stimulus` are log/diagnostics — not twin-adapter session gates.

### 4. Combinational notes (informative until Ola freezes)

```
session_enable   = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
yaw_cmd_enable   = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched ∧ ¬ e_stop_asserted
```

- `¬ user_present` → idle/safe; **no** yaw chase toward empty space; **deny** physical motion/strike regardless of Haar.
- Simulated presence **must stay tagged** `SIMULATED_BOOL_NOT_HARDWARE` so logs cannot be read as gym ToF evidence.
- Operator `--head-spotcheck-approved` is a **human qualitative gate**, not a learned confidence.

### 5. Staging and residual HY-02

| Stage | Live USB / clip | Residual |
|---|---|---|
| **S0** | Record/log head-ROI from **clip or USB**; presence flags may be simulated | Digital OK |
| **S1** | Live presence-lamp / head-marker / digital yaw on twin — USB **or** clip | Digital OK. **No arm motion.** |
| **S2** | Twin commands simulated continuum from simple cues | Still digital; not this paper’s freeze |
| **S3** | Physical arms | **Not authorized.** Presence interlock + `safe_to_actuate` + C-01 + B-06 + safety — Critical OPEN |

**HY-02 residual (named):**

| Name | State | Meaning |
|---|---|---|
| **HY-02** | **OPEN** | Qualitative **gym** head-ROI spot-check (person present / empty bag / walk-away idle) has **not** been done. No accuracy/FPS/IoU closeout. |
| **`SKIPPED_NO_CAMERA`** | **Allowed** on the **software path** | Missing USB device is **not** a blocker for clip / HIL / twin-adapter work. Continue outside virtual media using clip + stim. |
| USB camera later | Optional for gym check | Michael: **do not wait** on camera to keep building the software path. |

Software path **proceeds** with clip, `--sim-present`, and optional `--camera` when a device exists. Gym USB check, when Lead schedules it, is a **spot-check**, not a metrics campaign.

### 6. Interface notes for Astra / Codex

**Inputs this ICD expects the capture side to accept:**

| Input | Required? | Notes |
|---|---|---|
| `--camera <int>` **xor** `--clip` | Yes (existing argparse) | Live USB vs file |
| `--head-spotcheck-approved` | Yes for `head_hypothesis_valid` | Operator qualitative prior |
| `--sim-present` and/or `--timeline` | Until hardware presence | Tag `SIMULATED_BOOL_NOT_HARDWARE` |
| `--config` | Yes | Host/port + `derive` config; **TBD — Lead** gain |
| `--send` | Optional | UDP to twin |
| `--log` | Optional | JSONL opt-in |
| `--preview` | Optional | Local only |
| `--wait-ack` | Clip + `--send` only | **Not** live USB; **not** timing evidence |

**Outputs the twin adapter / receiver should consume:** the mapped signals in §3, plus stop packet on shutdown.

**Fail-safes Astra/Codex must not weaken:**
- `presence_sensor_fault` → `user_present := false`
- No actuation from `session_enable` / `yaw_cmd`
- `scope` remains `DIGITAL_TWIN_ONLY`
- No default media recording
- `SKIPPED_NO_CAMERA` is a valid software outcome, not a silent fail that should be “fixed” by inventing a camera

**ASSUMPTION tags that must remain visible in code comments / packets / docs:** Haar class; one-face rule; operator spot-check; simulated presence; no performance claim.

### 7. What is NOT claimed

- No FPS, accuracy %, IoU, confidence floor, latency budget, or yaw gain.
- Haar detect ≠ product CV; MediaPipe-class in the head-path paper is an alternate **ASSUMPTION**, not a requirement here.
- `--camera` open success ≠ gym-qualified sensing.
- Simulated presence ≠ ToF/PIR/mat.
- Digital twin yaw ≠ hardware yaw (F-05) and ≠ strike (F-01 + S3 stack).
- `--wait-ack` round-trip ≠ live timing evidence.
- Track A prescribed films ≠ vision proof.
- This ICD ≠ a PO, ≠ NEXT_PROMPT, ≠ a code patch.

### 8. Acceptance (qualitative; HY-02 remains OPEN)

| Case | Digital / USB pass language | Gym HY-02 |
|---|---|---|
| Person / face in frame, operator flag on, sim-present | `head_hypothesis_valid`; session may enable; yaw chase when `yaw_cmd_enable` — **directional only** | Still **OPEN** until gym spot-check |
| No camera | **`SKIPPED_NO_CAMERA`** — use `--clip` / HIL; software path continues | N/A |
| Walk-away / stop packet | Idle/safe; no chase | Gym walk-away **OPEN** |
| Inhibit / E-stop stim | `yaw_cmd_enable` false; session false if latched | Hardware E-stop is SAF-02 OPEN |
| Empty bag / no face | Head invalid; session false even if sim-present | Gym empty-bag **OPEN** |

Latency / FPS / IoU: **TBD — Lead** / not claimed.

---

## Open questions for Ola

1. **HY-02 gym spot-check owner / venue** — when, and is a USB webcam sufficient or is the protected product camera required? (Software must not wait.)
2. Confirm **`SKIPPED_NO_CAMERA`** as the residual token Astra/Codex should emit when `VideoCapture` cannot open, vs failing the pass.
3. When does live USB drop `SIMULATED_BOOL_NOT_HARDWARE` and consume real `user_present` from the presence path scout?
4. Freeze Haar-only for S0/S1 USB, or schedule MediaPipe-class as a later detector swap (**still ASSUMPTION**, no accuracy claim)?
5. `head_centroid_x` `[0,1]` vs signed offset — freeze for `derive`? (Also on the yaw-path paper.)
6. Idle policy on USB stop packet vs receiver watchdog — is the clean-exit stop packet (`user_present=false`) the normative digital idle?
7. Confirm this ICD is **paper-only deepen** and that `n3-head-track-yaw-bridge` code stays the implementation surface (no Elias code change).

---

## Ownership / commercial controls

| Role | Owns |
|---|---|
| **Ola (Lead Robotics)** | Integrate; HY-02 close/keep-open; **NEXT_PROMPT**; READY |
| **Elias (Controls & Perception)** | This ICD language only — **no code, no NEXT_PROMPT** |
| **Astra / Codex** | Implementation against existing `capture_head.py` + this interface table, under Ola |
| **Mech** | Later camera mount / cover |
| **Safety** | S3 / person-facing — not waived |

| Control | Rule |
|---|---|
| PO | **NONE** |
| NEXT_PROMPT | **NONE** — Ola already owns the n3 USB-path prompt; Elias does not write it |
| Code | **No change** from this paper |
| HY-02 | **OPEN** until qualitative gym spot-check |
| Software without camera | **`SKIPPED_NO_CAMERA` allowed** |
| Actuation | **Not authorized** |
| Numeric bars | **None invented** |

---

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate. Identical mirror: `sor_sync/docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`. PAPER ONLY. ICD deepen, not a code change. No NEXT_PROMPT. No PO. HY-02 OPEN. SKIPPED_NO_CAMERA allowed.*
