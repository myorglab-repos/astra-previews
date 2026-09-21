# A — Punch path and palm conventions

No new punch is commanded. This pass does not remake the ACCEPTED-A yaw scene. Inherited mid-height guard pose and palm conventions stand. U/F/T teaching intent remains qualitative.

| Item | Result | Evidence / defect |
|---|---|---|
| Saved inherited strike scenes | PASS, unchanged (inherited ACCEPTED-A) | model_verification.json; lineage.json |
| Clip L/R → yaw (software path re-run) | PASS on synthetic clip | udp_received.json frames 30 / 68 |
| Absent/invalid/fault/sync/inhibit/E-stop → idle | PASS digital samples / tests | unit_verification.json; integration idle chapters |
| USB fail-fast / clip CI | PASS | usb_path_verification.json; camera_probe.json |
| Gym qualitative L/R | See gym_spotcheck.json (SKIPPED is not FAIL) | gym_spotcheck.json |
| Wrist–glove alignment | PASS sampled inherited scene | A-05; ENVELOPE_GEOMETRY_AUDIT |
| Strike propulsion / impact | OPEN | C-01; Track A does not prove strike impulse |

RH-02 inherited policy remains. No head-tracking result upgrades those reach claims.
