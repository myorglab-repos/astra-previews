## READY_FOR_OLA
status: awaiting_ola
timestamp: 2026-09-21 09:56 ET
pass_id: n3-head-yaw-live-usb-path
track: A

### Summary
Delivered a live-USB-capable head→yaw path on the accepted `head-yaw-v1` bridge without a second schema. `--camera N` fails fast (`CAMERA_OPEN_FAILED`) instead of hanging; `--clip` remains the CI proof. Unit 32/32 gates (0 failures); clip integration 144 actual UDP packets with receiver re-derive; USB fail-fast PASS (4 methods). Camera probe **PRESENT**; gym qualitative **SKIPPED_NO_OPERATOR_APPROVAL**. SKIPPED_NO_CAMERA or SKIPPED_NO_OPERATOR_APPROVAL is not a software FAIL; no invented gym L/R media. Demo mapping/sign/gain/clamp/watchdog stay ASSUMPTION. HY-02 residual remains OPEN. B-06 / C-01 / SAF-02 remain Critical OPEN. Track A does not prove strike impulse. DIGITAL_TWIN_ONLY. $0 / no PO.

### Paths
- reviews/2026-09-21/n3-head-yaw-live-usb-path/INDEX.html
- reviews/2026-09-21/n3-head-yaw-live-usb-path/README.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/SOURCE_BRIEF.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/DEFECT_REGISTER.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/camera_probe.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/gym_spotcheck.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/usb_path_verification.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/integration_verification.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/packet_verification.json
- reviews/2026-09-21/n3-head-track-yaw-bridge/ENGINEERING_ASSESSMENT_N3_HEAD_TRACK_YAW_BRIDGE_2026-09-21.md
- docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md
- docs/engineering/OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md

### Ask Ola
Disposition the USB fail-fast + clip CI delta on ACCEPTED-A. Confirm HY-02 stays OPEN (software path only). Do not freeze demo gain/clamp/sign from this pass. No physical or sensing-performance closure is requested.

### Acceptance criteria self-check
- [x] Architecture freeze intact (no distal metal / continuum 8-chamber)
- [x] No invented force/pressure/life numbers
- [x] Punch vocabulary / palm frames addressed if Track A (inherited scenes preserved; no new strike)
- [x] Demarcation stated: Track A does not prove strike impulse
- [x] `--camera N` fail-fast documented and tested; live USB path packaged
- [x] Clip path unit + integration PASS with real JSON counts
- [x] Gym branch recorded as SKIPPED_NO_OPERATOR_APPROVAL (SKIPPED_NO_CAMERA is not FAIL)
- [x] Assumptions labeled; packet, SOURCE_BRIEF, DEFECT_REGISTER, glossary supplied
- [ ] Independent Ola acceptance; HY-02 / HY-03 / B-06 / C-01 / SAF-02 remain OPEN

### Blockers
None to local digital review. Gym qualitative is SKIPPED_NO_OPERATOR_APPROVAL. Lead parameter freeze and Critical hardware remain OPEN. Git delivery result is recorded separately. This marker is a local handoff, not automatic delivery or a watcher.

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
