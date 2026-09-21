# Elias — HY-03 yaw mapping freeze support (paper only)

> **STATUS BANNER — ACCEPTED-A / Lead freeze applied (2026-09-21).** Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (Lead disposition path). Demo ASSUMPTION values from `demo_config.json` are now **Lead Track A freeze** for Track A digital twin / HY-03 packet, with labels **NOT a measured hardware limit / NOT physical performance bar**. Open questions 1–2 **ANSWERED**. Critical (physical / SAF-02 / B-06 / C-01) remain **OPEN**. Elias still does **not** write NEXT_PROMPT or code.

| Field | Value |
|---|---|
| **Title** | HY-03 yaw mapping freeze — Elias support paper (digital contract language for Lead) |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | **ACCEPTED-A** — Ola / Lead HY-03 Track A freeze applied (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) |
| **Authority** | Michael approved all lanes 2026-09-21 via Ola — **PAPER ONLY** support for HY-03; **NO PO**; **NO NEXT_PROMPT**; Report to **Ola only** |
| **Status** | **ACCEPTED-A / Lead freeze applied** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`); demo ASSUMPTION values → Lead Track A freeze (**NOT a measured hardware limit / NOT physical performance bar**); CloudAgent builds `n3-hy03-yaw-mapping-freeze` under Ola; Elias paper-only |
| **Product** | AI-Powered Boxing Training System |

**Normative sources (read order — Elias read-only where noted):**
- `sor_sync/chats/NEXT_PROMPT.md` (pass `n3-hy03-yaw-mapping-freeze`) — **READ ONLY; Elias does not edit**
- `sor_sync/reviews/n3-head-yaw-live-usb-path/config_template.json` — null gain/clamp/watchdog → deny chase
- `sor_sync/reviews/n3-head-yaw-live-usb-path/demo_config.json` — **ASSUMPTION** illustrative values only
- `sor_sync/reviews/n3-head-yaw-live-usb-path/bridge_core.py` — `derive` formula (**DIGITAL_TWIN_ONLY**)
- `docs/engineering/ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md`
- `docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md`
- `sor_sync/docs/engineering/OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md`
- `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (Lead HY-03 disposition — cite by name)

Identical mirrors: `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md` and `sor_sync/docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`.

---

## Summary

This paper gave Lead the **digital contract language** for HY-03 (head centroid → carrier yaw mapping). **Lead Track A freeze is now applied** (ACCEPTED-A; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`): `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0`, `normalization=frame_fraction_0_to_1`, `idle_policy=home_zero`, with labels **NOT a measured hardware limit / NOT physical performance bar**. Sign convention text is **NORMATIVE** (positive image x → positive world X via +Z yaw from −Y home). Template nulls remain deny-chase until config is loaded with the freeze. Implementation remains CloudAgent / packet `n3-hy03-yaw-mapping-freeze` under Ola. Scope is **`DIGITAL_TWIN_ONLY`**. **No physical actuation.** **No PO.** **No NEXT_PROMPT write.** **No invented FPS / accuracy / IoU.** Report path: **Ola only**. Critical paths (SAF-02 / B-06 / C-01 / physical yaw) remain **OPEN**.

Parallel (same Michael approval; do not block HY-03): HY-02 gym spot-check may use `--head-spotcheck-approved` when a camera is present (qualitative L/R); if no camera, `SKIPPED_NO_CAMERA` remains OK (not FAIL). **Office USB webcam YES** for first HY-02 qualitative L/R per Lead. See § HY-02 and twin ICD amendments.

---

## Findings (severity)

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| HY03-C1 | **Critical — OPEN** | Perception / mapping path does **not** authorize physical yaw rotor, fill, or strike. Frozen digital numbers ≠ hardware READY. | Do not close from this paper. |
| HY03-C2 | **Critical — OPEN** | Inhibit / SAF-02 / P-05 / B-06 F-01/F-05/F-08 remain Lead-owned. Mapping freeze does not satisfy them. | Out of Elias paper scope. |
| HY03-M1 | **Major — ANSWERED (Lead Track A freeze)** | Demo values `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0` are now **Lead Track A freeze** (ACCEPTED-A; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) — **NOT a measured hardware limit / NOT physical performance bar**. | Keep freeze set; do not invent alternate numbers. |
| HY03-M2 | **Major** | Unconfigured template nulls (`gain`/`clamp`/`watchdog` = null) → `mapping_or_watchdog_TBD`; `effective_enable` false; `yaw_cmd=0` until config loads Lead Track A freeze (`config_template.json` + `bridge_core.derive`). | Deny-chase until configured with freeze set. |
| HY03-M3 | **Major — HY-02 OPEN** | HY-02 gym qualitative residual stays **OPEN** until L/R spot-check evidence is recorded. Operator approval for `--head-spotcheck-approved` is **granted** when camera present (2026-09-21). No camera → `SKIPPED_NO_CAMERA` OK (not FAIL). | Software must not wait. |
| HY03-I1 | **Info** | Idle policy `home_zero` is already Lead **ACCEPTED-A** digital idle (Ola integrate 2026-09-21). Clean-exit stop packet normative. | Do not re-open idle choice in this paper. |
| HY03-I2 | **Info** | Elias lane = **paper only**. CloudAgent builds `n3-hy03-yaw-mapping-freeze`. Elias does **not** write NEXT_PROMPT or change code. | Report READY_FOR_OLA path owned by implementer → Ola. |

---

## Draft ICD / mapping table language

### Scope

```
head_centroid_x (frame fraction)  →  signed_x  →  yaw_cmd (degrees)
        │                              │              │
        │   DIGITAL_TWIN_ONLY          │              │  only when gates + config OK
        ▼                              ▼              ▼
  bridge_core.derive(p, c)     clamp(sign * gain * signed_x, ±clamp)
        ✗  not to valves / hardware yaw / strike
```

Packet / code surface (pointer only — **no Elias edit**): `sor_sync/reviews/n3-head-yaw-live-usb-path/` (`bridge_core.py`, `config_template.json`, `demo_config.json`). HY-03 freeze packet target (under Ola / CloudAgent): `reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/`.

### Mapping table (working priors for Lead freeze)

Lead Track A freeze values below are **ACCEPTED-A** for Track A digital twin / HY-03 packet (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). Label: **NOT a measured hardware limit / NOT physical performance bar**. Do **not** treat them as measured hardware limits or physical performance bars. FPS / accuracy / IoU remain uninvented.

| Parameter | Working prior | Label |
|---|---|---|
| `normalization` | `frame_fraction_0_to_1` (`head_centroid_x` in `[0,1]`) | **Lead Track A freeze** / interim ACCEPTED (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) |
| `signed_x` | `(2*cx - 1)` | **ASSUMPTION** (matches `bridge_core.derive`) |
| `sign` | `+1` (positive image x → positive world X via +Z yaw from −Y home) | **Lead Track A freeze** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`; was `demo_config.json` `"sign": 1`) — **NOT a measured hardware limit / NOT physical performance bar** |
| `gain_deg_per_signed_x` | `30.0` | **Lead Track A freeze** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) — **NOT a measured hardware limit / NOT physical performance bar** |
| `clamp_deg` | `30.0` | **Lead Track A freeze** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) — **NOT a measured hardware limit / NOT physical performance bar** |
| `idle_policy` | `home_zero` | Already Lead **ACCEPTED-A** digital idle |
| `watchdog_s` | `2.0` | **Lead Track A freeze** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) — **NOT a measured hardware limit / NOT physical performance bar** |
| Unconfigured nulls | `config_template.json`: `gain_deg_per_signed_x` / `clamp_deg` / `watchdog_s` = `null` → flag `mapping_or_watchdog_TBD`; `effective_enable` false; `yaw_cmd=0` | **Normative until config loads Lead Track A freeze** |

**`demo_config.json` assumptions text (historical cite):** values are now **Lead Track A freeze** (ACCEPTED-A; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`) with label **NOT a measured hardware limit / NOT physical performance bar**. Sign convention text is **NORMATIVE:** *Positive image x maps to positive world X via +Z yaw from −Y home.*

**`config_template.json` assumptions text (cite):** *UNCONFIGURED until loaded with Lead Track A freeze. Null values deny chase.*

### Formula (cite `bridge_core.derive`, DIGITAL_TWIN_ONLY)

```
yaw_cmd = clamp( sign * gain_deg_per_signed_x * (2*cx - 1), ±clamp_deg )
```

only when:

```
user_present
  ∧ ¬ presence_sensor_fault
  ∧ head_hypothesis_valid
  ∧ ¬ inhibit_latched
  ∧ ¬ e_stop_asserted
  ∧ sync_quality == ok
  ∧ gain / clamp / watchdog configured (all non-null)
```

Else `yaw_cmd = 0.0` (`home_zero`).

As coded in `bridge_core.py` (informative — Lead owns freeze):

```
present   = user_present ∧ ¬ presence_sensor_fault
session   = present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
formula   = session ∧ ¬ e_stop_asserted
configured = gain_deg_per_signed_x ∧ clamp_deg ∧ watchdog_s all non-null
enabled   = formula ∧ sync_quality==ok ∧ configured
yaw       = clamp(sign * gain * (2*cx-1), ±clamp) if enabled else 0.0
```

**Watchdog / transport:** stale packet or unconfigured `watchdog_s` → idle `home_zero` (`malformed_stale_or_reordered_packet` / `transport_timeout` paths in `ReceiverState`). **Clean-exit stop packet** (`user_present=false`, head invalid) remains **normative** digital idle (Ola integrate + live USB ICD).

**Explicit:** Lead Track A freeze **applied** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). Elias paper-only. CloudAgent builds `n3-hy03-yaw-mapping-freeze`. **No physical actuation.** Critical remains **OPEN**.

### Sign convention text (NORMATIVE for HY-03 packet)

**Lead Track A freeze — NORMATIVE:** With `sign = +1`, increasing `head_centroid_x` (image right) increases commanded yaw in the positive sense that maps positive image x → positive world X via **+Z yaw from −Y home** (demo_config assumptions string; confirmed in `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`).

### What stays TBD — Lead (post freeze)

- Any measured FPS / accuracy / IoU / latency bar — **none invented**; not in scope of this support paper.
- Hardware yaw / F-05 / S3 — **not authorized**.
- Track A freeze numbers remain digital twin contract only — **NOT a measured hardware limit / NOT physical performance bar**.

---

## HY-02 gym language

**Michael approved 2026-09-21** (via Ola / NEXT_PROMPT pass `n3-hy03-yaw-mapping-freeze`):

- Operator approval is **granted** for `--head-spotcheck-approved` when a **camera is present**, for the **qualitative L/R gym branch**; record **honest JSON**; **no invented media**.
- If **no camera**: `SKIPPED_NO_CAMERA` is **OK** (not FAIL).
- Prior residual `SKIPPED_NO_OPERATOR_APPROVAL` was the **pre-approval** state; under this approval the operator flag **may be used** when a camera is present.
- **HY-02 remains OPEN** until qualitative gym spot-check evidence is recorded — **software must not wait**.

This section does **not** invent L/R media, FPS, or accuracy. **Office USB webcam YES** for first HY-02 qualitative L/R per Lead (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` / prior presence integrate).

---

## Open questions for Ola

1. Confirm freeze of demo **ASSUMPTION** values (`sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0`) as **Lead freeze**, or replace with different Lead numbers? — **ANSWERED** by HY-03 ACCEPTED-A: Lead Track A freeze applied as those values — **NOT a measured hardware limit / NOT physical performance bar** (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`).
2. Confirm sign convention text (positive image x → positive world X via +Z yaw from −Y home) as **normative** for the HY-03 packet? — **ANSWERED** by HY-03 ACCEPTED-A: **NORMATIVE**.
3. HY-02 gym L/R: is an **office USB webcam** sufficient for the first spot-check under this approval? — **ANSWERED** by Lead: **YES** (office USB OK for first qualitative L/R; HY-02 remains OPEN until evidence).
4. After freeze, should Elias amend twin-adapter / head-track papers to drop TBD on these fields, or wait for an Ola disposition file? — **ANSWERED**: amend papers to Lead Track A freeze; cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (disposition path).

---

## Explicit non-claims

- **No** invented FPS, accuracy %, IoU, confidence floor, or latency budget.
- **No** PO / parts order / Stephen spend from this paper.
- **No** NEXT_PROMPT write (Ola owns `n3-hy03-yaw-mapping-freeze`).
- **No** code change from Elias.
- Lead Track A freeze gains/clamps/watchdog are digital twin contract values — **NOT a measured hardware limit / NOT physical performance bar** — not product certification / not measured hardware limits.
- Digital twin yaw ≠ hardware yaw rotor ≠ pressurized strike.
- Report path: **Ola only** (not Michael).

---

## Ownership / commercial controls

| Role | Owns |
|---|---|
| **Ola (Lead Robotics)** | HY-03 freeze; NEXT_PROMPT; READY disposition; HY-02 close/keep-open |
| **Elias (Controls & Perception)** | This support paper only — **no code, no NEXT_PROMPT, no freeze** |
| **CloudAgent / Astra / Codex** | Build `n3-hy03-yaw-mapping-freeze` under Ola against Lead freeze + this language |
| **Safety / Mech** | S3 / person-facing / mount — not waived |

| Control | Rule |
|---|---|
| PO | **NONE** |
| NEXT_PROMPT | **NONE** from Elias — do not touch `chats/NEXT_PROMPT.md` |
| Code | **No change** from Elias |
| HY-03 freeze | **Lead / Ola ACCEPTED-A applied** — Elias paper amends only |
| HY-02 | **OPEN** until qualitative gym evidence; operator flag OK when camera present; `SKIPPED_NO_CAMERA` OK |
| Actuation | **Not authorized** |
| Numeric bars | Cite Lead Track A freeze + packet; **NOT a measured hardware limit / NOT physical performance bar**; no FPS/IoU invent |

---

*Elias Controls & Perception — DRAFT 2026-09-21; ACCEPTED-A / Lead Track A freeze applied same day (cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`). Identical mirror: `sor_sync/docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`. PAPER ONLY. No NEXT_PROMPT. No PO. No invented numbers beyond freeze set. Report to Ola only.*
