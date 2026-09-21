# n3-hy03-yaw-mapping-freeze

Digital Track A only. Protocol `head-yaw-v1` is unchanged from the ACCEPTED-A live-USB path (PR #3). Ola’s Lead freeze is in. Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` and `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`.

**Label, in plain sight: Lead Track A freeze — NOT measured hardware limits / product bars.**

**NORMATIVE sign:** positive image x → positive world X via +Z yaw from −Y home.

| Locked item | Value |
|---|---|
| Normalization | frame fraction `[0,1]` |
| Signed offset | `signed_x = (2*cx - 1)` on `frame_fraction_0_to_1` |
| Sign | `+1` (NORMATIVE: positive image x → positive world X via +Z yaw from −Y home) |
| Gain | 30 deg per signed unit |
| Clamp | ±30 deg |
| Idle | `home_zero` (`yaw_cmd = 0` whenever chase is off) |
| Watchdog | 2 s same-machine monotonic age (`age > 2` is stale) |

Positive yaw turns home (world −Y) toward world +X about local +Z. The bag and mast stay fixed. These degrees are not a hardware envelope, not a camera accuracy bar, and not a force.

The receiver still recomputes enable and yaw. Sender yaw and enable fields are not trusted. `config_template.json` in this packet carries the non-null Lead values. `config_unconfigured.json` keeps null gain, clamp, and watchdog, and those nulls still deny chase until a config is filled with this freeze.

## Run

```
python test_hy03_freeze.py
python run_hy02_gym.py
python verify_packet.py
```

Unit result is `unit_verification.json`. Gym result is `camera_probe.json` and `gym_spotcheck.json`. A missing camera would be `SKIPPED_NO_CAMERA`, not FAIL. This machine opened a camera and did not see one face; no left/right pictures were created.

## Architecture

Eight soft continuum chambers per arm: U1–U3, F1–F3, T1–T2. Textile strain limiting. No exposed distal metal. **Track A does not prove strike impulse.**

## Plain-language glossary

| Term | Everyday meaning |
|---|---|
| Lead Track A freeze — NOT measured hardware limits / product bars | The locked twin map. Not a lab measurement and not a product limit |
| home_zero | Digital shoulders go straight ahead when chase is not allowed |
| Watchdog | Stale head data stops the chase |
| HY-03 | This mapping lock |
| HY-02 | Real-gym chase, still open |
| SKIPPED_NO_CAMERA | No webcam, so the gym check is skipped and the software packet is not failed |
