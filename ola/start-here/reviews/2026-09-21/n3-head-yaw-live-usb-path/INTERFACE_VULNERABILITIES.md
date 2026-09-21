# G — Interface vulnerabilities / DFMEA inputs

Design failure mode and effects analysis (DFMEA) inputs only; no invented risk-priority numbers.

| Interface | Failure mode / effect | Digital mitigation / remaining work |
|---|---|---|
| USB camera open | Missing/busy index hangs the sender or is mistaken for a packet FAIL | Hard timeout + `CAMERA_OPEN_FAILED`; gym `SKIPPED_NO_CAMERA` is not FAIL; clip CI remains the proof path |
| Haar head prior | False face, occlusion, multiple people, image flip → wrong cue | Qualitative spot-check opt-in; multiple/zero candidates invalid; real camera dataset and calibration OPEN (HY-02) |
| Presence input | `--sim-present` mistaken for proximity proof | Source labeled SIMULATED_BOOL_NOT_HARDWARE; default absent; actual fail-safe wiring OPEN |
| UDP → HEAD_YAW_CARRIER | Lost, delayed, duplicate, malformed or reordered input | Same-machine monotonic freshness, sequence/stream validation, local watchdog; loopback only; receiver re-derives enable/yaw |
| Local inhibit | Reconnect clears stop or reset starts motion | Sticky runtime file; local reset plus separate arm; physical stop independence OPEN |
| UI / Blender process | Hang prevents home update | No hardware outputs; Blender timer is not an independent E-stop; SAF-02 OPEN |
| Home-zero return | Sudden virtual pose jump mistaken for physical stop profile | Digital-only idle assumption; physical deceleration/limp policy P-05 remains OPEN |
| Carrier/root/bearing/anchor | Unqualified load path / pinch / unlock | B-06 F-01/F-05/F-08 remain OPEN; no physical movement |

F-01 `pitch_lock_engaged` is not required for this digital yaw demo. No signal here is wired to hardware.
