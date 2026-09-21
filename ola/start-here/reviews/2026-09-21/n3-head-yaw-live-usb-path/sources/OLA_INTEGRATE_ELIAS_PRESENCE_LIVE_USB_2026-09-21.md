# Ola integrate — Elias presence scout + live USB ICD (2026-09-21)

| Field | Value |
|---|---|
| **Disposition** | **ACCEPTED-A (paper)** — Controls path language integrated |
| **Author** | Ola (Lead Robotics) |
| **Inputs** | `ELIAS_PRESENCE_HARDWARE_PATH_SCOUT.md`, `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` |
| **Authority** | Michael 2026-09-21 — keep building outside virtual media; camera optional for gym check |
| **PO / actuation** | **NONE** — Critical hardware remains **OPEN** |

## Summary

Both Elias papers are **ACCEPTED-A as Controls path language** for S0/S1 digital twin and for future gym sensing. They do **not** close SAF-02, P-05, B-06, C-01, or HY-02 gym residual. Software continues under **`SKIPPED_NO_CAMERA`**. Live USB implementation surface remains the yaw-bridge / `n3-head-yaw-live-usb-path` packet under Ola (CloudAgent already running) — Elias made **no code change**, correctly.

## Findings (Lead)

| ID | Severity | Finding | Lead disposition |
|---|---|---|---|
| PH-C1/C2 | Critical OPEN | No frozen gym presence SKU; presence ≠ actuate | **Keep OPEN** — confirmed |
| USB-C1/C2 | Critical OPEN | USB path ≠ S3 / inhibit close | **Keep OPEN** — confirmed |
| USB-M1 HY-02 | Major OPEN | Gym qualitative spot-check not done | **Keep OPEN** — do not wait for software |
| USB-M2 | Major | `SKIPPED_NO_CAMERA` | **CONFIRMED** normative residual token |

## Lead answers — presence open questions

1. **Primary gym modality** — **ToF preferred** (industrial Q4X-class after envelope CAD). Ultrasonic = **optional A-B only if optical ToF struggles** — not co-equal day-one, not silent replacement.
2. **AND vs OR** — **Confirm Elias ASSUMPTION:** single authoritative channel + explicit `presence_sensor_fault`. No silent AND for session enable. Dual topology later is a separate Lead freeze.
3. **Sole-channel integrity** — Hobby PIR / hobby ultrasonic **never** sole person-adjacent gym presence. Gym sole channel = **industrial discrete/analog** class. Hobby OK for **bench/fixture learn only**.
4. **Debounce / trip** — Stay **TBD — Lead** until bench hardware exists (Stephen gate for spend). Do not invent ms.
5. **Power-loss topology** — Gym freeze prior: **discrete/analog industrial** loss-of-signal as wiring property. I²C watchdog = bench only.
6. **Mat** — **Omit for MVP** digital twin / day-one session enable. Optional later AND — not a blocker.
7. **Empty-bag gym spot-check** — **Joint** Controls wiring + Mech mount when hardware is on desk; **Ola owns accept**. Not a software gate. Separate from HY-02 camera residual.

## Lead answers — live USB ICD open questions

1. **HY-02 owner / venue** — First qualitative gym check may use a **USB webcam** on the office desk; protected product camera later. Owner: **Ola + Elias** when a camera is available. Software **must not wait**.
2. **`SKIPPED_NO_CAMERA`** — **CONFIRMED.** Astra/Codex/CloudAgent must emit this residual when `VideoCapture` cannot open — **not** a packet FAIL for the software path.
3. **Drop `SIMULATED_BOOL_NOT_HARDWARE`** — Only after presence hardware is wired **and** qualitative AT-P cases pass. Until then keep the tag visible on packets/logs.
4. **Detector** — **Haar-only** for S0/S1 USB now. MediaPipe-class remains alternate ASSUMPTION for a later swap — no accuracy claim.
5. **`head_centroid_x`** — Keep coded **`[0,1]` frame fraction** as interim ASSUMPTION. Signed-offset / gain/clamp production freeze stays **TBD — Lead** (demo `demo_config.json` values remain ASSUMPTION).
6. **Idle** — Digital idle = **`home_zero`**; clean-exit stop packet (`user_present=false`, head invalid) is **normative** for digital path (matches yaw-bridge ACCEPTED-A).
7. **Paper-only** — **CONFIRMED.** Implementation surface = existing `capture_head.py` / live-USB packet under Ola. Elias lane may stay idle unless another Controls slice is asked.

## Engineering recommendations

- Point CloudAgent / Astra `n3-head-yaw-live-usb-path` at `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` as normative interface deepen.
- Keep `presence_source = SIMULATED_BOOL_NOT_HARDWARE` tagged until hardware AT.
- Do not route Stephen spend from these papers.
- Ismael B-06 Option B scout remains parallel Critical track.

## Test / validation gaps

- HY-02 gym qualitative (person / empty / walk-away) — OPEN
- Presence AT-P walk-in/out / fault — OPEN until hardware
- Debounce / trip distance / latency bars — TBD — Lead (no invent)
- Mapping/sign/gain freeze — TBD — Lead

## Manufacturing notes

- No SKU freeze. Reuse Elias BOM scout rows; presence scout does not replace BOM scout.
- Gym housing: industrial ToF class preferred; VL53L1X = bench only.

## Open questions for Michael (non-blocking)

- When Stephen opens spend: first presence bench buy = industrial ToF vs dual ToF+ultrasonic A-B kit?
- Prefer USB webcam gym HY-02 this week vs wait for protected product camera mount?

## Plain-language glossary

| Term | Everyday meaning |
|---|---|
| ACCEPTED-A (paper) | Lead accepts the Controls write-up as the working path language, not as product certification |
| ToF | Distance sensor using light timing — preferred “someone near the bag” sensor class |
| `SKIPPED_NO_CAMERA` | Software packet OK without a webcam; gym camera check deferred |
| `SIMULATED_BOOL_NOT_HARDWARE` | Presence flag is fake/stim for twin tests — not a real sensor |
| Fail-safe absent | If the sensor breaks or loses power, the system treats the user as **not** present |

---

*Ola Lead Robotics — integrate 2026-09-21 ~09:45 ET. Critical OPEN. No PO. No actuation.*
