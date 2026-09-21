# HY-03 — digital yaw mapping freeze

| Field | Value |
|---|---|
| **Pass** | `n3-hy03-yaw-mapping-freeze` |
| **Date** | 2026-09-21 |
| **Authority** | Ola Lead Track A freeze. Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` and `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`. $0. No PO. |
| **Scope** | `DIGITAL_TWIN_ONLY` |
| **Label** | **Lead Track A freeze — NOT measured hardware limits / product bars** |
| **Protocol** | `head-yaw-v1` unchanged. Receiver re-derives enable and yaw. |
| **Normative config** | `reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/frozen_config.json` |
| **Code** | `reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/bridge_core.py` |

The live-USB packet merged in PR #3 kept these numbers as an opt-in demo and left the production template null (**TBD — Lead**). This note locks that same design for the digital twin. It does not add a new gain, a new angle, or a performance bar.

## Locked map

```
signed_offset = 2 * head_centroid_x - 1     # frame fraction [0,1]; center = 0
yaw_deg       = clamp(sign * 30 * signed_offset, ±30)
```

| Item | Locked value | What it is |
|---|---|---|
| Normalization | `frame_fraction_0_to_1` | Horizontal face-center as a fraction of the frame |
| Sign | **+1** | **NORMATIVE:** positive image x → positive world X via +Z yaw from −Y home |
| Positive yaw | home world **−Y** toward world **+X** | Local +Z yaw on the carrier. Bag and mast stay fixed |
| Gain | **30 deg** per signed unit | Design estimate for the twin, not a measured motion range |
| Clamp | **±30 deg** | Same design estimate. Not a hardware stop and not SAF-02 |
| Idle | **`home_zero`** | Any gate fail, inhibit, E-stop stim, or watchdog expiry → `yaw_cmd = 0` |
| Watchdog | **2 s** | Same-machine monotonic age. `age > 2` is stale. Not a latency or FPS claim |

`performance_claim = NONE`. No FPS, accuracy %, IoU, force, or pressure is stated or implied by these numbers.

A mirrored camera preview is an installation fact to correct before this map. This freeze does not add a second, silent sign.

## What stays open

| ID | Status | Why it stays open |
|---|---|---|
| HY-02 | **OPEN** | Gym qualitative on DESKTOP-P08972I opened USB index 0 and saw no single face in 24 frames. No L/R media was invented. Not a product CV close. |
| B-06 | **Critical OPEN** | Cannot close without measured hardware. Option B pinned pitch is an interface prior only. No bearing, fatigue, or load measurement. No invented N·m. |
| C-01 | **Critical OPEN** | Cannot close without measured hardware. No pressure-to-motion-to-impact result and no coupon result in this pass. |
| SAF-02 | **Critical OPEN** | Cannot close without measured hardware. `home_zero` and the 2 s watchdog are digital twin gates. They are not an E-stop circuit, a vent, or an independence proof. No PL/SIL. |

Track A carrier yaw does **not** prove strike impulse. Architecture freeze stays: eight soft continuum chambers per arm (U1–U3, F1–F3, T1–T2), textile strain limiting, no exposed distal metal. Normative pitch lock bit remains `pitch_lock_engaged` and is not required for this digital yaw pedagogy.

## Plain-language glossary

| Term | Everyday meaning |
|---|---|
| Lead Track A freeze — NOT measured hardware limits / product bars | A locked working choice for the on-screen twin. Not a lab measurement and not a product limit. |
| home_zero | Shoulders return to the straight-ahead digital pose when chase is not allowed. |
| Watchdog | If fresh head data stops arriving, the twin stops chasing and goes home. |
| HY-03 | The mapping lock this note records. |
| HY-02 | Real-gym head chase. Still open. |
