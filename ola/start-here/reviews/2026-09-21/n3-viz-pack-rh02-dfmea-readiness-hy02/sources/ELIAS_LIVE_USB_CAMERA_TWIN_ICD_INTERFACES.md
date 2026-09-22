# Live USB camera → twin ICD interfaces (head path)

| Field | Value |
|---|---|
| **Title** | Live USB camera → virtual-bag twin ICD interfaces (head path feeding the accepted bridge) |
| **Rev** | **ACCEPTED-A (paper) deepen** 2026-09-21 ~22:42 ET |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | **Ola ACCEPTED-A (paper)** — `OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md` |
| **Authority** | Michael execute — **PAPER ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | **ACCEPTED-A (paper) deepen** — HY-03 Lead Track A freeze applied (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`); **not a code change**. Critical / HY-02 remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **ACCEPTED-A (paper) — 2026-09-21 ~22:42 ET.** Lead answers folded from `docs/engineering/OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. **Critical C-01 / SAF-02 / P-05 and HY-02 remain OPEN.** No PO. No NEXT_PROMPT. No invented metrics.

**Normative sources (read order):**
- `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` — MVP camera = head/human ROI; presence = on-switch; S0–S3; no physical strike from unverified perception
- `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` — head centroid → `yaw_cmd` digital twin; Assumptions / non-goals
- `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` — signal names, fail-safes, S0/S1 vs S3
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` — session_enable; presence forever
- `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md` — digital stim / yaw enable truth cases
- Existing software (pointer only, **no edit from this desk**): `sor_sync/reviews/n3-head-track-yaw-bridge/capture_head.py` (`--camera`)
- `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (Lead HY-03 disposition — Track A freeze; cite by name)
- `ELIAS_HY03_YAW_MAPPING_SUPPORT.md`

**Session enable (ACCEPTED-A (1)):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
Presence forever hard-interlocks **physical motion / pressurized strike**. This paper does **not** authorize physical actuation from perception.

**Michael 2026-09-21 09:37 ET:** keep building **outside virtual media**; USB camera **may** be needed later for gym check **but do not wait**. **HY-02 residual stays OPEN** until qualitative gym spot-check; software path proceeds with **`SKIPPED_NO_CAMERA` allowed**.

**No invented numbers** beyond the Lead Track A freeze set (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). No FPS, accuracy, IoU, latency, or confidence floors. Yaw map freeze: `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0` — **NOT a measured hardware limit / NOT physical performance bar**. Other priors tagged **ASSUMPTION** or **TBD — Lead**.

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
| `head_centroid_x` | **Lead Track A freeze** / interim ACCEPTED | `(x + w/2) / frame_width` in `[0,1]` — `normalization=frame_fraction_0_to_1` (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). |
| Yaw gain / clamps / units | **Lead Track A freeze** (HY-03 ACCEPTED-A) | `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0` via `derive` — **NOT a measured hardware limit / NOT physical performance bar**; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`. |
| Sync tolerance | **TBD — Lead** | USB `t_sync` is monotonic-since-start; clip uses `seq/fps`. No invented ms bar. |
| FOV / mount / index | **TBD — Lead** | USB index and gym mount not frozen. Do not wait on them for software. |
| Idle hold-last vs zero | **ACCEPTED-A** / Lead Track A freeze | `idle_policy=home_zero`. `capture_head.py` sends a stop packet (`user_present=false`, head invalid) on clean exit. `watchdog_s=2.0` (Lead Track A freeze — **NOT a measured hardware limit / NOT physical performance bar**). |
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
| `derive(...)` → `yaw_cmd` | `yaw_cmd` | out | Map from centroid when enable — Lead Track A freeze `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0` (**NOT a measured hardware limit / NOT physical performance bar**; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) | Enable false → **`home_zero`**; `watchdog_s=2.0` (freeze); paper does **not** actuate hardware |
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
| USB camera later | Optional for gym check; **office USB YES** for first HY-02 L/R per Lead | Michael: **do not wait** on camera to keep building the software path. |

Software path **proceeds** with clip, `--sim-present`, and optional `--camera` when a device exists. Gym USB check, when Lead schedules it, is a **spot-check**, not a metrics campaign.

### 6. Interface notes for Astra / Codex

**Inputs this ICD expects the capture side to accept:**

| Input | Required? | Notes |
|---|---|---|
| `--camera <int>` **xor** `--clip` | Yes (existing argparse) | Live USB vs file |
| `--head-spotcheck-approved` | Yes for `head_hypothesis_valid` | Operator qualitative prior |
| `--sim-present` and/or `--timeline` | Until hardware presence | Tag `SIMULATED_BOOL_NOT_HARDWARE` |
| `--config` | Yes | Host/port + `derive` config; Lead Track A freeze gain/clamp/sign/watchdog (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) — **NOT a measured hardware limit / NOT physical performance bar** |
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

- No FPS, accuracy %, IoU, confidence floor, or latency budget. Yaw gain/clamp/sign/watchdog = Lead Track A freeze only — **NOT a measured hardware limit / NOT physical performance bar**.
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

1. **HY-02 gym spot-check owner / venue** — **ANSWERED (partial):** office USB webcam **YES** for first qualitative L/R per Lead (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`); protected product camera later. HY-02 remains OPEN until evidence. (Software must not wait.)
2. Confirm **`SKIPPED_NO_CAMERA`** as the residual token Astra/Codex should emit when `VideoCapture` cannot open, vs failing the pass.
3. When does live USB drop `SIMULATED_BOOL_NOT_HARDWARE` and consume real `user_present` from the presence path scout?
4. Freeze Haar-only for S0/S1 USB, or schedule MediaPipe-class as a later detector swap (**still ASSUMPTION**, no accuracy claim)?
5. `head_centroid_x` `[0,1]` vs signed offset — freeze for `derive`? — **ANSWERED** by HY-03 ACCEPTED-A: `frame_fraction_0_to_1` (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`).
6. Idle policy on USB stop packet vs receiver watchdog — is the clean-exit stop packet (`user_present=false`) the normative digital idle? — **ANSWERED**: `idle_policy=home_zero`; clean-exit stop packet normative; `watchdog_s=2.0` Lead Track A freeze (**NOT a measured hardware limit / NOT physical performance bar**).
7. Confirm this ICD is **paper-only deepen** and that `n3-head-track-yaw-bridge` code stays the implementation surface (no Elias code change).

---


## Amendment 2026-09-21 13:56 ET — HY-02 operator approval + HY-03 support pointer

- **Michael / Ola** approved operator use of `--head-spotcheck-approved` when a **camera is present** for qualitative gym L/R; honest JSON only; no invented media.
- If **no camera**, `SKIPPED_NO_CAMERA` remains **OK** (not FAIL). Software must not wait.
- Prior residual `SKIPPED_NO_OPERATOR_APPROVAL` was the pre-approval state; under this approval the operator flag may be used when a camera is present.
- **HY-02 remains OPEN** until qualitative gym spot-check evidence is recorded.
- HY-03 mapping freeze support paper (Elias paper only): `ELIAS_HY03_YAW_MAPPING_SUPPORT.md` (mirrors under `docs/engineering/` and `sor_sync/docs/engineering/`).
- Implementation remains CloudAgent / `n3-hy03-yaw-mapping-freeze` under Ola — **Elias paper only**; no Elias code; no NEXT_PROMPT write from this desk.

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| USB-M1a | **Major — HY-02 OPEN** | Operator approval for `--head-spotcheck-approved` **granted** 2026-09-21 when camera present (qualitative L/R). No camera → `SKIPPED_NO_CAMERA` OK. | HY-02 still OPEN until gym evidence; pointer: `ELIAS_HY03_YAW_MAPPING_SUPPORT.md` |

## Amendment 2026-09-21 — HY-03 Lead Track A freeze (ACCEPTED-A)

- Cite: `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (Lead disposition path).
- Frozen for Track A digital twin / HY-03 packet: `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0`, `normalization=frame_fraction_0_to_1`, `idle_policy=home_zero`.
- Label: **NOT a measured hardware limit / NOT physical performance bar**.
- Sign convention **NORMATIVE:** positive image x → positive world X via +Z yaw from −Y home.
- **Office USB webcam YES** for first HY-02 qualitative L/R per Lead (HY-02 remains OPEN until evidence).
- Mapping rows above updated from TBD / ASSUMPTION to Lead Track A freeze where applicable.
- Critical OPEN unchanged. No PO. No NEXT_PROMPT. No code.

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| USB-M4 | **Info — ANSWERED** | Yaw gain/clamp/sign/watchdog were TBD; now Lead Track A freeze | Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`; **NOT a measured hardware limit / NOT physical performance bar** |
| USB-M1b | **Major — HY-02 OPEN** | Office USB webcam **OK** for first qualitative L/R | HY-02 still OPEN until gym evidence |

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

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate; HY-03 Lead Track A freeze amended same day (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). Identical mirror: `sor_sync/docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`. PAPER ONLY. ICD deepen, not a code change. No NEXT_PROMPT. No PO. HY-02 OPEN. SKIPPED_NO_CAMERA allowed. Office USB OK for first HY-02 L/R.*


---

## Amendment 2026-09-21 ~22:35 ET — EXECUTE NOW deepen (Interfaces / AT / Fault)

**Authority:** Michael $0 non-stop via Ola EXECUTE NOW. **PAPER deepen only.** No Python mapping freeze edits from this desk. Critical / HY-02 remain **OPEN**.

### Interfaces section (strengthened)

| Interface block | Contract | Notes |
|---|---|---|
| Capture CLI | `--camera` xor `--clip`; `--head-spotcheck-approved`; `--sim-present` / `--timeline`; `--config`; `--send`; `--log`; `--preview` | Existing `capture_head.py` surface — ICD cite only |
| Packet schema | `schema_rev=head-yaw-v1`, `scope=DIGITAL_TWIN_ONLY`, `source_kind=USB_camera` on live path | Privacy: no media by default |
| Twin derive | `session_enable`, `yaw_cmd`, `yaw_cmd_enable`, `quality_flags` | Combinational; ACCEPTED-A session equation |
| Presence | `SIMULATED_BOOL_NOT_HARDWARE` until hardware AT | Cite presence scout |
| Mapping (digital freeze) | Lead Track A: `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0` (±30), `idle_policy=home_zero`, `watchdog_s=2.0`, `normalization=frame_fraction_0_to_1` | Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`. Labels: **NOT-measured-hardware-limit** / **NOT physical performance bar** |
| Sign convention | **NORMATIVE:** positive image x → positive world X via +Z yaw from −Y home (`sign=+1`) | Keep consistent with HY-03 papers |
| HY-02 operator path | Office USB YES for first qualitative L/R | Checklist: `ELIAS_HY02_OFFICE_USB_LR_OPERATOR_CHECKLIST.md` |

`session_enable` equation remains **ACCEPTED-A**. Haar / one-face+operator prior remain **ASSUMPTION**. Scope remains **DIGITAL_TWIN_ONLY**.

### Acceptance-test outline (qualitative — no numeric bars)

| AT ID | Walk / scene | Pass language (qualitative) |
|---|---|---|
| AT-USB-WALK-IN | Walk into envelope / face enters ROI with operator flag + sim-present | Head may become valid; session may enable when AND holds — **no ms bar** |
| AT-USB-WALK-OUT | Walk away / stop packet | Idle/safe; no chase; prefer `home_zero` |
| AT-USB-EMPTY | Empty bag / no face | Head invalid; session false even if sim-present |
| AT-USB-SINGLE | Single face in ROI + `--head-spotcheck-approved` | Qualitative one-face prior OK — **not** accuracy claim |
| AT-USB-MULTI | Multi-face / no single face | Head invalid (`CAMERA_PRESENT_MULTI_FACE` / **`CAMERA_PRESENT_NO_SINGLE_FACE`** = **normative checklist tokens**; code emit may lag) |
| AT-USB-NOCAM | No device | **`SKIPPED_NO_CAMERA`** — not FAIL; software continues |
| AT-USB-INHIBIT / ESTOP | Stim latch / e-stop | Session/yaw kill per ICD; digital only |
| AT-USB-STALE / WD | Stale sync / watchdog | Quality flag; idle/`home_zero`; `watchdog_s=2.0` digital freeze — **NOT measured HW limit** |

**HY-02** remains **OPEN** until honest office/gym evidence (checklist). CI may use synthetic pack: `ELIAS_SYNTHETIC_HEAD_PRESENCE_CI_EPISODE_PACK.md`.

### Fault table (digital / USB path)

| Fault / condition | Detection / stim | Required response | Label |
|---|---|---|---|
| Camera open fail | Open attempted, failed | Fail-fast / honest `CAMERA_OPEN_FAILED`; or `SKIPPED_NO_CAMERA` if none | Existing fail-fast concept |
| No face | `face_candidates=0` | Head invalid; session false | Checklist token `CAMERA_PRESENT_NO_SINGLE_FACE` (**normative checklist token**; code emit may lag) |
| Multi-face | `face_candidates>1` | Head invalid; no identity track | `CAMERA_PRESENT_MULTI_FACE` |
| Stale sync | `sync_quality=stale/unknown` | Quality flag; no effective chase | TBD—Lead sync tolerance (no invented ms) |
| Presence fault→absent | `presence_sensor_fault` | Force `user_present:=false`; idle/safe | Normative fail-safe |
| Inhibit latch | `inhibit_latched` | Session false; clear **only** manual reset after clear | AI must not clear |
| E-stop sim | `e_stop_asserted` | Kill `yaw_cmd_enable`; prefer `home_zero` | Handheld ≠ E-stop (SAF-02 OPEN) |
| Watchdog | No fresh packet beyond digital `watchdog_s=2.0` | Receiver idle/`home_zero` | Lead Track A freeze — **NOT measured hardware limit** |

### HY-03 digital freeze reminder (implement cite — paper only)

```
sign=+1
gain_deg_per_signed_x=30.0
clamp_deg=30.0   # ±30
idle_policy=home_zero
watchdog_s=2.0
normalization=frame_fraction_0_to_1
```

Cite: `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`. **Digital freeze — NOT measured hardware bars.** Prefer paper deepen; do not change Python mapping freezes in `bridge_core` / `demo_config` unless already matching.

---


---

## Amendment 2026-09-21 ~22:42 ET — ACCEPTED-A (paper) six-packet (Lead answers folded)

Cite: `docs/engineering/OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`.

| Item | Value |
|---|---|
| Disposition | **ACCEPTED-A (paper) deepen** |
| `CAMERA_PRESENT_NO_SINGLE_FACE` | **Normative checklist token** (code emit may lag; do not claim every token already in py) |
| HY-02 | Remains **OPEN** — honest `SKIPPED_*` until face-in-ROI run; **no invented L/R** |
| Critical | **C-01 / SAF-02 / P-05 OPEN** |
| PO / NEXT_PROMPT | **NONE** |

*Elias — ACCEPTED-A (paper) deepen 2026-09-21 ~22:42 ET. Critical / HY-02 OPEN.*
