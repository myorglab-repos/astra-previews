# Live-USB-capable head → N3 carrier yaw

This pass extends the **ACCEPTED-A** digital Track A bridge (`n3-head-track-yaw-bridge`, 2026-09-21) with a **live-USB-capable** sender path. Protocol `head-yaw-v1` is unchanged. `bridge_core.py` and `blender_receiver.py` are reused without a second schema. The Blender successor and 12-second synthetic film are **inherited, not remade**. Normative interface language is Elias `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` as integrated by Ola (`OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md`): `SKIPPED_NO_CAMERA` is not a software FAIL; `presence_source = SIMULATED_BOOL_NOT_HARDWARE` until hardware; Haar + one-face + `--head-spotcheck-approved`; digital idle `home_zero` + clean-exit stop packet; HY-02 gym qualitative stays OPEN even if the software path PASSes.

`--camera N` now fails fast with `CAMERA_OPEN_FAILED` when the index cannot open (no hang). `--clip` remains the CI / packet path. `--head-spotcheck-approved` and `--sim-present` are documented operator flags. The receiver still **re-derives** enable/yaw and never trusts sender-computed fields.

**Verified this pass (cite JSON only):** unit 32/32 gate combinations, 0 failures (`unit_verification.json` PASS); clip integration 144 actual UDP packets, receiver_rederived=True (`integration_verification.json` PASS); USB fail-fast 4 methods, 0 failures (`usb_path_verification.json` PASS); camera probe **PRESENT**; gym qualitative **SKIPPED_NO_OPERATOR_APPROVAL**. Inherited model audit: bag/camera matrix deviation 0.0; yaw replay max error ~7.8e-07°; 5 inherited scenes / 11 ancestor hashes.

**Disposition requested:** Accept the software USB path + clip CI as a delta on ACCEPTED-A. HY-02 remains OPEN (not product-closed). Do not freeze demo gain/clamp/sign. B-06 / C-01 / SAF-02 remain Critical OPEN.

Eight soft continuum chambers per arm: U1–U3, F1–F3, T1–T2; textile strain limiting, vent plus elastic return and no exposed distal metal. Bag/fill/mast stay fixed; only the shoulder carrier yaws. Protected-root cover remains an illustrative envelope.

**Track A does not prove strike impulse.** B-06 root hardware and C-01 pressure-to-motion-to-impact measurements remain Critical OPEN. No physical actuation, measured sensing accuracy, detector FPS, latency, durability or safety qualification is claimed. DIGITAL_TWIN_ONLY.

## Assumptions and Lead decisions

| Item | Implementation proposal / demo value | Status |
|---|---|---|
| Detector | OpenCV bundled frontal-face Haar; default detector parameters; exactly one candidate | ASSUMPTION; face is a head prior, no confidence/accuracy bar |
| Qualitative validity | Candidate accepted only with explicit `--head-spotcheck-approved` | ASSUMPTION; fixture visually checked; live scene needs its own operator check |
| Normalization / units / sign | Frame fraction [0,1]; degrees; signed offset = 2x−1; positive yaw turns -Y home toward +X | ASSUMPTION; camera mirroring/mount calibration TBD—Lead |
| Gain / clamp | Production template null; opt-in demo 30 degrees per signed unit, ±30-degree clamp | ASSUMPTION demo only, not an approved motion range; normative mapping TBD—Lead |
| Idle | Immediate digital home-zero; no tween or hold-last | ASSUMPTION; physical return policy TBD—Lead |
| Watchdog / poll | Demo 2-second freshness window; 0.02-second requested UI poll | ASSUMPTION software settings, not achieved latency/FPS or safety bars; Lead TBD |
| Transport | Loopback-only UDP/JSON `head-yaw-v1`; sender monotonic time on same machine; ordered single stream | ASSUMPTION; no second schema; no network clock synchronization |
| Presence | Explicit `--sim-present` or timeline; default absent | ASSUMPTION stub; real thresholds, debounce and wiring TBD—Lead |
| Sync | Injected ok/stale/unknown; non-ok blocks effective chase | ASSUMPTION for digital replay; physical fusion tolerance TBD—Lead |
| Timing | Inherited film encoded at 12 frames/s; acknowledged offline UDP replay | Media construction choices, NOT processing rate or latency evidence |
| Source clip | Translated public-domain NASA still; no actual person movement | Synthetic fixture, not recorded gym/webcam validation |
| USB open | DirectShow on Windows + hard timeout (default 5 s); clear CAMERA_OPEN_FAILED | Fail-fast software behavior; not a camera quality bar |


## Plain-language glossary

| Term | Everyday meaning | Why it matters in this pass |
|---|---|---|
| live USB path | Code that can open a real webcam when one is plugged in. | This pass hardens `--camera N` so a missing device fails clearly instead of hanging. |
| SKIPPED_NO_CAMERA | Gym check not run because no camera — not a software failure. | CI / packet proof uses the clip fixture and still PASSes. |
| SKIPPED_NO_OPERATOR_APPROVAL | Camera opened, but no person attested a one-face gym prior. | Device-present is not gym L/R evidence; no invented stills/film. |
| ROI / bbox / centroid | Image region / rectangle around a detected face / its center. | Horizontal center supplies the yaw cue; no identity is inferred. |
| Head hypothesis | A tentative face detection. | One-face plus operator spot-check is a demo prior, not qualified sensing. |
| Carrier yaw | Shoulders turning around the mast. | The filled bag must remain stationary. |
| UDP / replay | Local message transport / playing saved inputs again. | Actual detector packets drive the receiver; the film is inherited ACCEPTED-A evidence. |
| Presence stub | An injected yes/no signal (`--sim-present` or timeline). | This pass has no ToF/PIR/mat hardware. |
| Inhibit latch / watchdog | A stop that stays set / a check for missing fresh data. | Chase stops on a fault; manual reset and arm are separate local actions. |
| ASSUMPTION / TBD—Lead | A working demo choice / a decision still owned by Ola. | Demo angles and timeouts are not hardware limits or performance targets. |
| HY-02 | Open item: real camera chase not yet product-closed. | Software path + optional gym qualitative only; not done product. |
| A-05 / A-03 | Wrist alignment / chamber-group teaching cues. | Alignment is audited; accepted U/F/T cues stay preserved. |
| G-03 / G-05 | Arm-to-bag proxy gap / carrier-to-cover axial gap. | Sampled digital geometry does not qualify loaded clearances. |
| B-06 / C-01 | Unqualified root hardware / missing propulsion and impact measurements. | Both remain Critical OPEN regardless of this USB path. |
| Track A / Track D | Digital visualization / perception-action engineering. | This packet proves clip CI + USB fail-fast, not real-world CV performance. |

What changed / what is still not proven: the same shoulder-follow demo can open a USB camera without hanging, and still proves itself from a file clip when no camera is present. Real-gym chase, physical stops, root structure and punch power remain unproven.
