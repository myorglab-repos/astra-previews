# Ola Lead integrate — Elias HY-03 yaw mapping support (2026-09-21)

| Field | Value |
|---|---|
| **Disposition** | **ACCEPTED-A (paper support)** + **Lead Track A freeze** for HY-03 digital mapping |
| **Authority** | Ola (Lead Robotics); Michael approved all lanes 2026-09-21 |
| **Sources** | `ELIAS_HY03_YAW_MAPPING_SUPPORT.md`; live-USB `bridge_core.py` / `demo_config.json` / `config_template.json`; amended `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` |
| **Scope** | DIGITAL_TWIN_ONLY. No physical yaw. No PO. Critical B-06 / C-01 / SAF-02 remain OPEN. |

## Summary

Elias HY-03 support paper is **ACCEPTED-A (paper)**. Lead freezes the Track A digital mapping contract below for packet `n3-hy03-yaw-mapping-freeze`. Numbers remain labeled **Lead Track A freeze — NOT measured hardware limits / product bars**. CloudAgent implements; Elias does not freeze and does not write NEXT_PROMPT.

## Lead answers to Elias open questions

1. **Freeze demo values** as Lead Track A freeze (do not replace): `sign=+1`, `gain_deg_per_signed_x=30.0`, `clamp_deg=30.0`, `watchdog_s=2.0`. Keep ASSUMPTION / DESIGN ESTIMATE wording that these are **not** measured performance or physical motion limits.
2. **Sign convention text is NORMATIVE** for the HY-03 packet: positive image x → positive world X via +Z yaw from −Y home (`sign=+1`).
3. **Office USB webcam is sufficient** for the first HY-02 qualitative L/R spot-check under Michael 2026-09-21 approval. Product protected camera not required for this first check. HY-02 stays OPEN until honest gym evidence is recorded (or SKIPPED_NO_CAMERA if none).
4. **Yes — after this disposition**, Elias may amend twin-adapter / head-track papers to drop TBD on these four fields and cite this integrate file. Do not invent FPS/accuracy.

## Lead freeze table (Track A)

| Parameter | Lead freeze | Label that must stay visible |
|---|---|---|
| normalization | `frame_fraction_0_to_1` | Lead Track A freeze |
| signed_x | `(2*cx - 1)` | Lead Track A freeze (matches `bridge_core.derive`) |
| sign | `+1` | Lead Track A freeze — NOT hardware limit |
| gain_deg_per_signed_x | `30.0` | Lead Track A freeze — DESIGN ESTIMATE / NOT measured |
| clamp_deg | `30.0` | Lead Track A freeze — NOT measured hardware stop |
| idle_policy | `home_zero` | Prior ACCEPTED-A (unchanged) |
| watchdog_s | `2.0` | Lead Track A freeze — NOT measured latency bar |
| unconfigured nulls | deny chase (`yaw_cmd=0`) | Normative until config filled |

Formula (unchanged): `yaw_cmd = clamp(sign * gain * (2*cx-1), ±clamp)` only when session gates + configured; else `0.0`.

## Findings

| ID | Severity | Note |
|---|---|---|
| HY03-C1/C2 | Critical OPEN | Mapping freeze ≠ physical yaw / SAF-02 / B-06 close |
| HY03-M1 | CLOSED-A Track A | Demo numbers now Lead-frozen for digital twin only |
| HY03-M2 | CLOSED-A Track A | After freeze, template must carry non-null Lead values in freeze packet |
| HY03-M3 | OPEN | HY-02 until gym evidence |
| HY03-I1 | Info | idle `home_zero` kept |

## Engineering recommendations

- CloudAgent `n3-hy03-yaw-mapping-freeze`: encode this freeze in config + tests + packet docs; cite this file.
- Elias: amend twin/head-track ICDs to replace TBD on these fields with Lead Track A freeze 2026-09-21 + pointer here.
- Do not close Critical from this paper.

## Test / validation gaps

- HY-02 gym qualitative still required for residual close (office USB OK).
- No measured FPS / accuracy / IoU — none invented.
- Hardware yaw / inhibit AT / B-06 / C-01 still OPEN.

## Manufacturing notes

None. $0 / no PO.

## Open questions

None blocking HY-03 implement. C-01 / SAF-02 papers still in flight separately.

*Ola — 2026-09-21. Report path: desks → Ola → Eta digest; no routine Michael DM.*
