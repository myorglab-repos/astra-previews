# Head tracking → N3 carrier yaw

Implemented a local OpenCV face-prior pipeline, gated UDP/JSON adapter and Blender receiver. A **synthetic translated-still clip** goes through actual decoded-image detection and actual loopback UDP into `bpy`. The 12-second film and eight stills pair the detected head rectangle with the virtual carrier. This is a digital integration demonstration; no webcam capture was performed.

Eight soft continuum chambers per arm: U1–U3, F1–F3, T1–T2; textile strain limiting, vent plus elastic return and no exposed distal metal. Bag/fill/mast stay fixed; only the shoulder carrier yaws. Protected-root cover remains an illustrative envelope.

**Verified:** 144 detector packets applied; all 32 presence/head/inhibit/E-stop/presence-fault combinations; malformed, reordered and stale input; timeout-to-home; sticky inhibit across sender rebind and receiver reconstruction; manual reset followed by separate arm. Five inherited scenes match the accepted parent by object geometry/transform/animation/material signatures; eleven ancestor hashes, including N1, match. Bag/fill/mast and camera matrix deviations are zero in the 144 saved frames.

**Disposition requested:** Ola qualitative review of direction and idle behavior, plus mapping/idle/normalization proposal. Current status is ready for review, not independent acceptance. Lead values remain null in the default config. See [README](README.html), [model audit](model_verification.json), [integration](integration_verification.json), [unit checks](unit_verification.json) and [source snapshots](source_documents.json).

**Track A does not prove strike impulse.** B-06 root hardware and C-01 pressure-to-motion-to-impact measurements remain Critical OPEN. No physical actuation, measured sensing accuracy, detector FPS, latency, durability or safety qualification is claimed.

## Assumptions and Lead decisions

| Item | Implementation proposal / demo value | Status |
|---|---|---|
| Detector | OpenCV bundled frontal-face Haar; default detector parameters; exactly one candidate | ASSUMPTION; face is a head prior, no confidence/accuracy bar |
| Qualitative validity | Candidate accepted only with explicit `--head-spotcheck-approved` | ASSUMPTION; fixture visually checked; future live scene needs its own check |
| Normalization / units / sign | Frame fraction [0,1]; degrees; signed offset = 2x−1; positive yaw turns -Y home toward +X | ASSUMPTION; camera mirroring/mount calibration TBD—Lead |
| Gain / clamp | Production template null; opt-in demo 30 degrees per signed unit, ±30-degree clamp | ASSUMPTION demo only, not an approved motion range; normative mapping TBD—Lead |
| Idle | Immediate digital home-zero; no tween or hold-last | ASSUMPTION; physical return policy TBD—Lead |
| Watchdog / poll | Demo 2-second freshness window; 0.02-second requested UI poll | ASSUMPTION software settings, not achieved latency/FPS or safety bars; Lead TBD |
| Transport | Loopback-only UDP/JSON; sender monotonic time on same machine; ordered single stream | ASSUMPTION; no network clock synchronization or remote deployment |
| Presence | Explicit simulated boolean/timeline, default absent | ASSUMPTION stub; real thresholds, debounce and wiring TBD—Lead |
| Sync | Injected ok/stale/unknown; non-ok blocks effective chase | ASSUMPTION for digital replay; physical fusion tolerance TBD—Lead |
| Timing | Film encoded at 12 frames/s; acknowledged offline UDP replay | Media construction choices, NOT processing rate or latency evidence |
| Source clip | Translated public-domain NASA still; no actual person movement | Synthetic fixture, not recorded gym/webcam validation |


## Plain-language glossary

| Term | Everyday meaning | Why it matters in this pass |
|---|---|---|
| ROI / bbox / centroid | Image region / rectangle around a detected face / its center. | Horizontal center supplies the yaw cue; no identity is inferred. |
| Head hypothesis | A tentative face detection. | One-face plus operator spot-check is a demo prior, not qualified sensing. |
| Carrier yaw | Shoulders turning around the mast. | The filled bag must remain stationary. |
| UDP / replay | Local message transport / playing saved inputs again. | Actual detector packets drive Blender; film playback is baked from those packets. |
| Presence stub | An injected yes/no signal. | This pass has no ToF/PIR/mat hardware. |
| Inhibit latch / watchdog | A stop that stays set / a check for missing fresh data. | Chase stops on a fault; manual reset and arm are separate local actions. |
| ASSUMPTION / TBD—Lead | A working demo choice / a decision still owned by Ola. | Demo angles and timeouts are not hardware limits or performance targets. |
| A-05 / A-03 | Wrist alignment / chamber-group teaching cues. | Alignment is audited; accepted U/F/T cues stay preserved. |
| G-03 / G-05 | Arm-to-bag proxy gap / carrier-to-cover axial gap. | Sampled digital geometry does not qualify loaded clearances. |
| B-06 / C-01 | Unqualified root hardware / missing propulsion and impact measurements. | Both remain Critical OPEN regardless of this film. |
| Track A / Track D | Digital visualization / perception-action engineering. | This bridge proves software integration on a synthetic clip, not real-world CV performance. |

What changed / what is still not proven: detected image position now turns the virtual shoulders with simulated gates; real camera performance, physical stops, root structure and punch power remain unproven.
