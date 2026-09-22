# Elias — HY-02 office USB L/R operator checklist (qualitative)

| Field | Value |
|---|---|
| **Title** | HY-02 gym L/R prep — office USB single-face-in-ROI operator checklist |
| **Rev** | **ACCEPTED-A (paper)** 2026-09-21 ~22:42 ET |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | **Ola ACCEPTED-A (paper)** — `OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md` — report path **Ola only** |
| **Authority** | Michael authorized $0 non-stop via Ola EXECUTE NOW 2026-09-21 ~22:34 ET |
| **Status** | **ACCEPTED-A (paper)** — HY-02 remains **OPEN** until honest evidence / honest `SKIPPED_*`. Critical C-01 / SAF-02 / P-05 remain **OPEN**. |
| **Product** | AI-Powered Boxing Training System |

> **ACCEPTED-A (paper) — 2026-09-21 ~22:42 ET.** Lead answers folded from `docs/engineering/OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. **Critical C-01 / SAF-02 / P-05 and HY-02 remain OPEN.** No PO. No NEXT_PROMPT. No invented metrics.

**Lead freeze (office USB):** Office USB webcam is **YES** for the **first** HY-02 qualitative L/R spot-check (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). Product protected camera is **not** required for this first check. **HY-02 stays OPEN** until honest gym/office evidence is recorded (or an honest skip token).

**Identical mirrors:**  
`docs/engineering/ELIAS_HY02_OFFICE_USB_LR_OPERATOR_CHECKLIST.md`  
`sor_sync/docs/engineering/ELIAS_HY02_OFFICE_USB_LR_OPERATOR_CHECKLIST.md`

**Canonical SoR citation path:** `docs/engineering/...` on repo `robotic-punching-bag`.

---

## Explicit non-claims (normative)

> **Do NOT invent PASS L/R stills, film, or numeric results.**  
> **Do NOT claim HY-02 CLOSED.**  
> **Do NOT invent FPS / accuracy / IoU / latency bars.**  
> **No webcam media recording by default** — JSON outcome only (`--log` opt-in).  
> **DIGITAL_TWIN_ONLY** — this checklist does **not** authorize physical yaw or strike.  
> Fail/skip tokens below are **Controls paper tokens**. **`CAMERA_PRESENT_NO_SINGLE_FACE`** is a **normative checklist token** (Lead ACCEPTED-A). Code emit may lag — **do not claim every token already exists in py**. Keep honest `SKIPPED_*` until face-in-ROI run; **no invented L/R**.

---

## Script / path ready (SoR / reviews)

| Role | Path (SoR-relative) | Notes |
|---|---|---|
| **Preferred operator script** | `reviews/n3-head-track-yaw-bridge/capture_head.py` | Has `--camera`, `--head-spotcheck-approved`, `--sim-present`, `--preview`, `--log`. **No webcam media recording by default.** |
| Live-USB packet folder | `reviews/n3-head-yaw-live-usb-path/` | Contains `bridge_core.py`, `demo_config.json`, `gym_spotcheck.json`, `config_template.json` |
| Current gym spot-check JSON | `reviews/n3-head-yaw-live-usb-path/gym_spotcheck.json` | Holds **`SKIPPED_NO_OPERATOR_APPROVAL`** — stills `[]`, film `null`. **Do NOT invent L/R stills/film/results.** |
| Live USB ICD | `docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` | Interface + fail-safes |
| HY-03 Lead integrate | `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` | Office USB YES; digital freeze values |

**Box absolute (this workspace):**  
`/workspace/boxing-trainer/sor_sync/reviews/n3-head-track-yaw-bridge/capture_head.py`  
`/workspace/boxing-trainer/sor_sync/reviews/n3-head-yaw-live-usb-path/`

---

## Example command shape (ASSUMPTION indices)

**ASSUMPTION:** USB index `0` is illustrative — operator confirms the correct OpenCV `VideoCapture` index for the office USB device. Index is **TBD — Lead / operator** if multiple cameras exist.

```bash
cd reviews/n3-head-track-yaw-bridge
python capture_head.py --camera 0 --head-spotcheck-approved --sim-present --preview
```

Optional JSON-only log (no webcam media recording by default):

```bash
python capture_head.py --camera 0 --head-spotcheck-approved --sim-present --preview --log hy02_office_usb.jsonl
```

| Flag | Meaning |
|---|---|
| `--camera N` | Live USB (**ASSUMPTION** index) |
| `--head-spotcheck-approved` | Operator qualitative one-face prior gate (Michael/Ola approved when camera present) |
| `--sim-present` | `presence_source = SIMULATED_BOOL_NOT_HARDWARE` — **not** ToF |
| `--preview` | Local overlay only; stop with `q` |
| `--log PATH` | Opt-in **JSONL only** — no media URI |

`performance_claim` on script stdout remains **`NONE`**.

---

## Fail / skip taxonomy (Controls paper tokens)

Align to existing where present; propose missing as named checklist tokens **without** claiming code already emits all.

| Token | Kind | Meaning | Notes |
|---|---|---|---|
| **`SKIPPED_NO_CAMERA`** | Skip (**normative; not FAIL**) | No USB device / capture path unavailable for this check | Software path continues with clip / HIL. Not a fail. |
| **`SKIPPED_NO_OPERATOR_APPROVAL`** | Skip (**existing**) | Camera may be present but operator approval flags not both set; no invented L/R media | Current `gym_spotcheck.json` holds this |
| **`CAMERA_OPEN_FAILED`** | Fail-fast (**existing concept**) | `VideoCapture` / open path failed when an index was attempted | Distinct from skip-no-camera when open was attempted and failed |
| **`CAMERA_PRESENT_NO_SINGLE_FACE`** | Outcome (**normative checklist token**) | Camera open; `face_candidates != 1` (zero faces) — head invalid | **Normative checklist token** per Lead ACCEPTED-A (`OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`); code emit may lag — do **not** claim every token already exists in py. Qualitative only; not accuracy bar |
| **`CAMERA_PRESENT_MULTI_FACE`** | Outcome | Camera open; multiple faces → invalid (no identity tracking) | Matches Haar one-face **ASSUMPTION** |
| **`HEAD_SPOTCHECK_APPROVED_ONE_FACE`** | Outcome | Operator gate **and** exactly one face — **qualitative only** | Does **not** invent PASS L/R media; does **not** close HY-02 alone without honest recorded evidence package |

**Explicit:** Do **not** invent a `PASS_LR` / filmed L/R success token in this paper. Honest JSON outcome only. HY-02 remains **OPEN** until Lead accepts recorded evidence (or honest skip).

---

## Operator steps (office USB — first HY-02 qualitative L/R)

1. **Plug** office USB webcam; confirm OS sees the device.
2. Confirm **single face alone in ROI** (no second person in frame). Empty / multi-face → record matching token; do not invent results.
3. `cd` to `reviews/n3-head-track-yaw-bridge/` (SoR) or the box mirror path above.
4. Set flags: `--camera <index>` (**ASSUMPTION**), `--head-spotcheck-approved`, `--sim-present`, optional `--preview`, optional `--log hy02_office_usb.jsonl`.
5. Run when face is in frame. Observe preview overlay if used (`SIM presence | DIGITAL TWIN ONLY`).
6. Record **honest JSON outcome only** (stdout / `--log` JSONL / operator note). **No** invented stills/film.
7. **Stop** (`q` / EOF). Do not claim HY-02 CLOSED. Hand evidence path to **Ola** (not Michael DM).

If no camera: emit / record **`SKIPPED_NO_CAMERA`** (not FAIL) and continue software path per live-USB ICD.

---

## Cross-cites

| Doc | Use |
|---|---|
| `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` | Office USB YES; HY-02 OPEN until evidence; digital freeze |
| `docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` | Live USB ↔ twin ICD |
| `docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` | MVP sensing ICD |
| `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md` | Yaw mapping support (digital) |
| `ELIAS_PRESENCE_HARDWARE_PATH_SCOUT.md` | Presence hardware scout (sim until AT) |

---

## HY-02 status (unchanged)

| Item | State |
|---|---|
| **HY-02** | **OPEN** — keep honest `SKIPPED_*` until Michael runs office USB with single face in ROI; **no invented L/R** |
| Critical C-01 / SAF-02 / P-05 | **OPEN** |
| PO / NEXT_PROMPT / SendToUser | **NONE** from this desk |

---

*Elias Controls & Perception — ACCEPTED-A (paper) 2026-09-21 ~22:42 ET per `OLA_INTEGRATE_ELIAS_EXECUTE_NOW_SIX_PACKET_2026-09-21.md`. PAPER ONLY. No invented L/R results. HY-02 OPEN. Critical OPEN.*
