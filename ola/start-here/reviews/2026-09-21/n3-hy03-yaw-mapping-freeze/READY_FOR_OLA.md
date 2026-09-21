## READY_FOR_OLA
status: awaiting_ola
timestamp: 2026-09-21 14:03 ET
pass_id: n3-hy03-yaw-mapping-freeze
track: A

### Summary
Ola’s Lead Track A freeze is encoded for the digital twin. Cite `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md` and `docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md`. Locked values: sign=+1, gain_deg_per_signed_x=30.0, clamp_deg=30.0, watchdog_s=2.0, idle_policy=home_zero, signed_x=(2*cx-1), normalization=frame_fraction_0_to_1. NORMATIVE sign text: positive image x → positive world X via +Z yaw from −Y home. Label kept visible: **Lead Track A freeze — NOT measured hardware limits / product bars**. ASSUMPTION / DESIGN ESTIMATE stays in the assumptions text. The freeze-packet template carries these non-null values. Unconfigured nulls still deny chase. Protocol `head-yaw-v1` unchanged. Receiver still re-derives enable and yaw. Unit verification is `unit_verification.json` (re-run with this encoding). Office USB webcam is sufficient for the first HY-02 qualitative L/R check: `--head-spotcheck-approved` when the camera is PRESENT, otherwise `SKIPPED_NO_CAMERA` (not FAIL). No invented L/R media. HY-02 stays OPEN. B-06, C-01, and SAF-02 stay Critical OPEN. Track A does not prove strike impulse. DIGITAL_TWIN_ONLY. $0 / no PO. No FPS, accuracy, IoU, force, or pressure claim.

### Paths
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/INDEX.html
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/README.md
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/SOURCE_BRIEF.md
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/DEFECT_REGISTER.md
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/CRITICAL_OPEN.md
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/config_template.json
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/frozen_config.json
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/config_unconfigured.json
- docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md
- docs/engineering/ELIAS_HY03_YAW_MAPPING_SUPPORT.md
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/bridge_core.py
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/unit_verification.json
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/packet_verification.json
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/camera_probe.json
- reviews/2026-09-21/n3-hy03-yaw-mapping-freeze/gym_spotcheck.json
- docs/engineering/HY03_YAW_MAPPING_FREEZE_2026-09-21.md

### Ask Ola
Accept this packet as the encoding of the Lead Track A freeze already written in `docs/engineering/OLA_INTEGRATE_ELIAS_HY03_2026-09-21.md`. HY-02 stays OPEN until honest gym L/R evidence exists. Do not close B-06, C-01, or SAF-02 from this pass. No physical actuation and no sensing-performance closure is requested.

### Acceptance criteria self-check
- [x] Architecture freeze intact (eight soft chambers, textile limit, no exposed distal metal)
- [x] No invented force, pressure, FPS, accuracy, or IoU
- [x] Track A demarcation stated: this pass does not prove strike impulse
- [x] Mapping, sign, gain, clamp, idle=`home_zero`, and watchdog locked in config, code, and docs
- [x] Label visible: Lead Track A freeze — NOT measured hardware limits / product bars
- [x] NORMATIVE sign: positive image x → positive world X via +Z yaw from −Y home
- [x] Cites Ola integrate and Elias HY-03 support
- [x] Unconfigured nulls still deny chase
- [x] Unit tests cover sign, clamp, idle, and watchdog stale (6 methods, 0 failures)
- [x] USB camera probed on DESKTOP-P08972I; gym branch recorded without invented L/R media
- [x] B-06 / C-01 / SAF-02 remain Critical OPEN
- [ ] Independent Ola acceptance

### Blockers
None for local digital review. HY-02 gym L/R was not observed in this grab. Critical hardware remains OPEN. This marker is a handoff to Ola, not a product certification and not a purchase.

## Plain-language glossary

| Term | Everyday meaning | Why it matters in this pass |
|---|---|---|
| Lead Track A freeze — NOT measured hardware limits / product bars | The locked on-screen map. Not a lab measurement and not a product limit. | 30 deg and 2 s are the twin contract, not measured accuracy or a hardware stop. |
| NORMATIVE sign | The required direction sentence for this packet. | positive image x → positive world X via +Z yaw from −Y home. |
| Gain | How many degrees of shoulder turn per full step from center to the frame edge. | Frozen at 30. Not a hardware travel limit. |
| Clamp | The farthest digital yaw this map will command. | Frozen at ±30 deg. Not an E-stop. |
| home_zero | Straight-ahead digital pose. | Used whenever chase is not allowed, including stale data. |
| Watchdog | A timer that gives up if new head data stops arriving. | Frozen at 2 seconds of same-machine age. Not a latency score. |
| HY-03 | The mapping lock. | This pass freezes it for the twin. |
| HY-02 | Real-gym head chase. | Camera opened; no single face this time; still open. |
| SKIPPED_NO_CAMERA | Gym check skipped because no webcam opened. | Would not fail the software packet. This run was not that case. |
| CAMERA_PRESENT_NO_SINGLE_FACE | Webcam opened, Haar saw no exactly-one face. | Honest residual. No fake left/right pictures. |
| Carrier yaw | Shoulders turning around the mast. | The filled bag stays put. |
| B-06 / C-01 / SAF-02 | Root hardware, punch-power evidence, and the real stop circuit. | All stay Critical OPEN until measured hardware exists. |
| Track A | The on-screen teaching model. | Following a head on screen does not prove a strike. |
| DIGITAL_TWIN_ONLY | Moves the Blender model only. | No valves, no pressurized punch, no purchase. |

What changed: the twin's shoulder-follow map is now a locked design estimate instead of an unlabeled demo. What is still not proven: real-gym left/right chase, the physical stop, the root structure, and punch power.
