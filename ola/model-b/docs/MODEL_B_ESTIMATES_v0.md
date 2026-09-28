# Model B: Paper Estimates v0 (every input is an ASSUMPTION)
Date: 2026-09-27 · Owner: Ola · No measurements exist. These estimates decide what to test first. They don't replace testing.

## E1. Collar grip against turning (MB-01)
- Model: a tensioned band on a cylinder. Total normal force is about 2 pi x band tension. Friction torque = mu x normal force x radius.
- ASSUMPTION: band tension 1000 N (ratchet), liner-to-cover friction mu 0.5 (rubberized liner on vinyl or leather).
- Grip torque: about 560 N·m on a 14 in bag, about 750 N·m on a 19 in bag.
- Load: arm reaction of 100 N (ASSUMPTION, soft-arm contact limit) at a 0.5 m lever gives 50 N·m.
- **Margin is about 11x on paper.** Risks not covered: sweaty or oily covers (mu could drop a lot), cover creep, direct punches to the collar, and a bag that's softer at collar height. Straps carry the vertical load, so this only covers turning.
- Close by: a bench torque test on real bag covers, dry and wet (T-01).

## E2. Tilt (MB-02)
13 lb net offset at 8 in, pivot-to-CoM 30 in. Tilt is 1.9 deg at 80 lb, 1.6 deg at 100 lb and 1.1 deg at 150 lb. The strap adjusters trim it out. See spec section 4.

## E3. Swing from arm reaction (MB-03 input)
- Pendulum length 1.5 m (ASSUMPTION: chain plus half the bag). One arm push of 100 N for 0.2 s (ASSUMPTION).
- Swing amplitude is about 17 cm on an 80 lb bag, 14 cm on 100 lb and 10 cm on 150 lb (bag plus 25 lb kit).
- Punches will swing the bag more than the arms do. **The tracking requirement is to hold accuracy with the camera base moving up to about 30 cm and tilting up to 10 deg** (ASSUMPTION, for Controls to confirm).

## E4. Strap loads (MB-06)
25 lb static, 3x dynamic factor, 3 straps: 25 lb peak per strap. Rated working load of 125 lb or more per strap and clip, plus secondary retention.

## E5. Runtime (MB-04)
90 Wh pack with 72 Wh usable. Average draw 30 to 70 W gives **1.0 to 2.4 h per pack**. The biggest unknown is compressor duty cycle.

## E6. Kit mass (all MBs)
25 lb total (breakdown in spec section 3). Target is 25 lb or less and the hard ceiling is 30 lb, because above that tilt, swing and strap loads all get worse together.
