# Defect register — n3-hy03-yaw-mapping-freeze

| ID | Severity | Observation | Disposition | Evidence |
|---|---|---|---|---|
| HY-03 | Track A | Gain, sign, clamp, idle, and watchdog were demo-only / TBD — Lead | **CLOSED-A Track A** per `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` (Elias support: `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`). sign=+1, gain_deg_per_signed_x=30.0, clamp_deg=30.0, watchdog_s=2.0, idle_policy=home_zero, signed_x=(2*cx-1), frame_fraction_0_to_1. Label stays visible: **Lead Track A freeze — NOT measured hardware limits / product bars**. NORMATIVE sign: positive image x → positive world X via +Z yaw from −Y home. Nulls still deny chase. | `config_template.json`; `frozen_config.json`; `bridge_core.py`; `unit_verification.json` |
| HY-02 | High residual | Real-gym chase is not product-closed | **OPEN.** Office USB webcam is sufficient for the first qualitative L/R check. Use `--head-spotcheck-approved` when a camera is PRESENT; otherwise `SKIPPED_NO_CAMERA` (not FAIL). This machine’s recorded grab is in `gym_spotcheck.json`. No invented L/R media. | `camera_probe.json`; `gym_spotcheck.json` |
| HY-01 | Integration | Head cue had no carrier adapter | Unchanged from parent. Protocol `head-yaw-v1` reused. Not reopened. | parent live-USB packet |
| HY-04 | Digital fault behavior | Stale, missing, or latched input must not leave chase on | Re-checked here: watchdog stale and idle paths return `yaw_cmd` 0. | `unit_verification.json` |
| B-06 | Critical | Root / pitch hardware is not measured | **OPEN.** Cannot close without measured hardware. No invented N·m. $0 / no PO. | `CRITICAL_OPEN.md` |
| C-01 | Critical | Propulsion and contact evidence is missing | **OPEN.** Cannot close without measured hardware. No pressure, force, or coupon result. | `CRITICAL_OPEN.md` |
| SAF-02 / P-05 | Critical | Physical stop and limp behavior are unqualified | **OPEN.** Digital `home_zero` and the 2 s watchdog are not an E-stop, a vent, or an independence proof. No PL/SIL. | `CRITICAL_OPEN.md` |

Presence on this path remains `SIMULATED_BOOL_NOT_HARDWARE` when a gym grab runs. This pass does not drop that tag.
