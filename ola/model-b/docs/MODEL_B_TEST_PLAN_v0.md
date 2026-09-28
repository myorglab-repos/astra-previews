# Model B: Test Plan v0 (all PARKED, needs Stephen approval for spend)
Date: 2026-09-27 · Owner: Ola · Protocols only, no results.

| Test | Closes | What | Pass criterion (ASSUMPTION, to finalize) |
|---|---|---|---|
| T-01 Collar torque | MB-01, HZ-B2 | Torque the clamped collar on vinyl and leather covers, dry and wet | Slip torque of 3x the max arm torque (150 N·m) or more when wet |
| T-02 Tilt & level | MB-02 | Hang the kit on 80/100/150 lb bags, measure tilt before and after trim | 1 deg or less after trim |
| T-03 Swing tracking | MB-03, HZ-B7 | Record tracking accuracy while the bag swings by hand and from arm pushes | Meets Model A accuracy at 30 cm / 10 deg |
| T-04 Overpressure | HZ-B3 | Force the regulator open, confirm the relief valve and cutoff | Pressure stays under the SI-B3 limit |
| T-05 Fault venting | HZ-B4, B6 | E-stop, link loss, low battery, watchdog | Arms vented within the Model A vent-time target |
| T-06 Strap pull | MB-06, HZ-B1 | Pull test on the strap and clip set, then single-clip failure | 5x the peak load, no drop on single failure |
| T-07 Pack impact | MB-05, HZ-B5 | Repeated punches and drops on the pack with a dummy battery | No latch release, no housing crack |
| T-08 Runtime & thermal | MB-04, HZ-B8 | Scripted training session until the pack is empty | 1 h or more per pack, temperatures within limits |
| T-09 Cover wear | MB-07 | Cycle the collar on sample covers | No visible damage after N cycles |

Order when funded: T-06, then T-01, then T-05 and T-04, then the rest.
