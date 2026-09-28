# Model B: Controls & Perception Spec v0 (for Controls desk review)
Date: 2026-09-27 · Drafted by Ola for Elias (Controls) review · Same app and handheld as Model A.

## What's new vs Model A
1. The cameras sit on a moving, swinging base (the collar pack), not a fixed frame.
2. Everything runs off a battery, so it needs power states and a low-battery safe state.
3. The ring rotation and arms are referenced to the bag, not to the room.

## Requirements
- CB-01 IMU on the collar board, fused with the camera feed, so tracking corrects for bag motion up to about 30 cm and 10 deg tilt (E3, ASSUMPTION).
- CB-02 Tracking accuracy targets are the same as Model A, measured while the bag swings (test T-03).
- CB-03 Arm commands are timed from where the user is relative to the bag, not the room.
- CB-04 Power states: off, standby, training and low battery. At low battery the arms vent and park, and the handheld shows a warning. Fuel gauge on the handheld.
- CB-05 Safety venting (dual channel, same as Model A): vent on e-stop, lost handheld link, fault, overpressure or low battery. A hardware watchdog vents without software.
- CB-06 Swing-aware arm limits: arm motion is blocked or softened when bag swing goes over a threshold (ASSUMPTION, to be set).
- CB-07 Ring rotation: the ring is powered or passive (open question). If powered, it needs a stall and pinch torque limit.
- CB-08 Handheld and app: shared with Model A. The app detects the model and shows Model B settings (bag size and weight entry for calibration).

## Open for Controls
1. Is IMU plus camera enough, or does Model B need a second view point?
2. Where should the camera go on the pack so it sees the user around the bag?
3. Should the ring be powered, or passive and turned by the arms?
