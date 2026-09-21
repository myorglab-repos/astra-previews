# G — Interface vulnerabilities / DFMEA inputs

Design failure mode and effects analysis (DFMEA) inputs only; no invented risk-priority numbers.

| Interface | Failure mode / effect | Digital mitigation / remaining work |
|---|---|---|
| Haar head prior | False face, occlusion, multiple people, image flip → wrong cue | Qualitative spot-check opt-in; multiple/zero candidates invalid; real camera dataset and calibration OPEN |
| Presence input | Sim flag mistaken for proximity proof | Source labeled SIMULATED_BOOL_NOT_HARDWARE; default absent; actual fail-safe wiring OPEN |
| UDP → HEAD_YAW_CARRIER | Lost, delayed, duplicate, malformed or reordered input | Same-machine monotonic freshness, sequence/stream validation, local watchdog; loopback only; no authenticated hardware protocol |
| Local inhibit | Reconnect clears stop or reset starts motion | Sticky runtime file; corrupt state latches; local reset plus separate arm; physical stop independence OPEN |
| UI / Blender process | Hang prevents home update | No hardware outputs; Blender timer is not an independent E-stop; SAF-02 OPEN |
| Home-zero return | Sudden virtual pose jump mistaken for physical stop profile | Digital-only idle assumption; physical deceleration/limp policy P-05 remains OPEN |
| Carrier/root/bearing/anchor | Unqualified load path / pinch / unlock | B-06 F-01/F-05/F-08 remain OPEN; no physical movement |
| Distal textile / hose routing | Fatigue, leakage, retention or abrasion | B-03/RH-03 and Track B coupons remain OPEN |

F-01 pitch lock is not required for this digital yaw demo; F-01/F-05 and full S3 readiness remain required before pressurized strike. No signal here is wired to hardware.
