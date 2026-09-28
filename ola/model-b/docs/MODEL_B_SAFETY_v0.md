# Model B: Safety Review v0
Date: 2026-09-27 · Owner: Ola · Paper hazard review. Nothing is tested.

| ID | Hazard | Cause | Severity | Control | Verify |
|---|---|---|---|---|---|
| HZ-B1 | Kit falls | Strap or clip failure, ceiling mount overload | Critical | Rated hardware 5x or more, secondary retention, stated ceiling rating in manual | T-06 pull test |
| HZ-B2 | Collar slips or turns | Low friction (sweat), tension loss | High | Ratchet band with visible tension indicator, straps carry weight | T-01 |
| HZ-B3 | Overpressure or burst | Regulator or valve failure | High | Mechanical relief valve, pressure sensor cutoff | T-04 |
| HZ-B4 | Arm keeps pushing after a fault | Software or link failure | High | Dual-channel vent, hardware watchdog, elastic return | T-05 |
| HZ-B5 | Battery damage or fire | Impact on the pack, bad pack | High | Certified tool-platform pack only, padded latched dock, battery management system | T-07 impact |
| HZ-B6 | Pinch | Rotating ring, collar segments | Medium | Guards, soft boot, torque limit if powered | Inspection plus T-05 |
| HZ-B7 | User hit by a swinging bag or pack | Large swing | Medium | Swing-aware limits (CB-06), minimum bag weight | T-03 |
| HZ-B8 | Burns | Compressor or battery heat | Low | Vented pack, thermal cutoff | T-08 |

Gate: Model B can't move to Functional prototype until HZ-B1 through B5 each have a written control and a test protocol. Hardware tests need Stephen's approval for spend.
