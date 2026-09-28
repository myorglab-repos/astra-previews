# Model B: Safety Review v1
Date: 2026-09-28 (v1: saddle + straps, no collar or ring) · Owner: Ola · Paper hazard review. Nothing is tested.

| ID | Hazard | Cause | Severity | Control | Verify |
|---|---|---|---|---|---|
| HZ-B1 | Kit falls | Strap or clip failure, ceiling mount overload | Critical | Rated hardware 5x or more, secondary retention, stated ceiling rating in manual | T-06 pull test |
| HZ-B2 | Saddle slips or turns | Low friction (sweat), strap tension loss | High | Two ratchet straps, tether carries weight | T-01 |
| HZ-B3 | Overpressure or burst | Regulator or valve failure | High | Mechanical relief valve, pressure sensor cutoff | T-04 |
| HZ-B4 | Arm keeps pushing after a fault | Software or link failure | High | Dual-channel vent, hardware watchdog, elastic return | T-05 |
| HZ-B5 | Battery damage or fire | Impact on the pack, bad pack | High | Certified tool-platform pack only, padded latched dock, battery management system | T-07 impact |
| HZ-B6 | Pinch or hard contact | Ratchet levers, root brackets | Medium | Ratchets on the rear with padded flaps, brackets inside saddle | Inspection |
| HZ-B9 | Arm hits bag or user's hand trapped between arm and bag | Clearance loss | Medium | ≥ 14 mm model clearance, soft arm | T-10 |
| HZ-B10 | Arm-body contact too hard | Pressurized arm stiffness | High | Keep Model A foam; contact limit | T-11 |
| HZ-B7 | User hit by a swinging bag or pack | Large swing | Medium | Swing-aware limits (CB-06), minimum bag weight | T-03 |
| HZ-B8 | Burns | Compressor or battery heat | Low | Vented pack, thermal cutoff | T-08 |

Gate: Model B can't move to Functional prototype until HZ-B1 through B5 each have a written control and a test protocol. Hardware tests need Stephen's approval for spend.
