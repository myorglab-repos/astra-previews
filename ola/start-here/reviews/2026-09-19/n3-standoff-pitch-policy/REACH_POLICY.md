# Option A: strike-dependent stand-off and coupled partial aim

Coordinates are model meters: X left/right, opponent toward negative Y, Z above nominal floor. All boxes retain X=-0.260..+0.260 m. Head Z bands remain short 1.450..1.650, mid 1.620..1.820 and tall 1.780..1.960 m. Abdomen Z remains 1.000..1.240 m. These are review assumptions, not anthropometric or contact-safety bounds.

| Strike / extension | Y box, m | Rationale |
|---|---|---|
| Straight and diagonal, 100% | -0.850..-0.600 | Retain the far straight guard assumption. |
| Hook and uppercut, 100% | -0.700..-0.480 | Closer working distance for curved strokes; near face moves 120 mm closer and far face 150 mm closer. |
| Body L/R, 100% | -0.850..-0.600 | Retain the existing downward abdomen case. |
| Straight, 70% | -0.600..-0.300 | A closer opponent assumption for the shorter stroke. |
| Straight, 50% | -0.450..-0.150 | A still closer, marginal surface-reach illustration. |

The boxes differ between chapters. They do not depict one fixed opponent satisfying every strike simultaneously, nor do the closer boxes establish room for a human body. Box width in X and height bands are not enlarged to conceal misses. Every rendered target wireframe is checked against the numeric case box.

## Partial pitch rule

Keep the inherited 50/70% shape parameter q and mesh coordinates. At the inherited peak, compute the mean of evaluated glove vertices relative to the shoulder pivot. Let y,z be that vector's forward/vertical components, r=sqrt(y*y+z*z), and e=atan2(z,-y). Desired centroid height is the midpoint of the chosen head Z band. The added pitch is asin((desired_Z-root_Z)/r)-e. Add this to the inherited pitch, clip to 0..57 degrees, and round to 0.001 degree. The implementation clamps the asin input to [-1,1]; audit the result instead of assuming reachability. Only the active arm receives changed partial pitch; the other arm retains its source pose.

The 57-degree cap is a digital review constraint, not validated hardware travel. A 60-degree candidate passed nominal inclusion but left just 0.060172 mm G-03 clearance; its audit and lineage receipts are retained. Reducing the cap improves the final global minimum to 1.792008 mm (now controlled by tall 70% peaks). No additional routing bow was needed to keep the sampled proxy nonnegative.

| Head preset | 50% pitch deg | 70% pitch deg | 100% straight pitch deg |
|---|---|---|---|
| Short | 27.126 | 13.499 | 8 |
| Mid | 49.181 | 29.110 | 16 |
| Tall | 57.000 (clipped) | 45.018 | 24 |

At 100%, retain hook +3-degree trim, uppercut zero trim, diagonal L -8 / R +15 degrees relative to the head preset. Body retains its descent from +8-degree guard to -20-degree peak. Partial pitch is constant within its chapter; guard/extend/hold/vent/return shape schedules are inherited. Changes between chapters are cuts, not commanded transitions.

## RH-02 residual and acceptance boundary

All 38 policy peaks contain evaluated glove vertices. Every 50% pose contains only **four vertices**, with **0.571485 mm maximum sampled interior margin** limited by the X face. This is fragile surface inclusion, not useful target coverage or centered reach. The tall 50% unbounded centering calculation requests 77.480 degrees; the cap limits it to 57. The glove vertex centroid is Z=1770.670 mm, **9.330 mm below the band floor and 99.330 mm below its center**. Its surface still enters the band, but its wrist datum remains outside. Thus RH-02 is implemented with a documented residual, not fully closed.

The 50% box also intersects the **275 mm radius infinite bag proxy**: its closest XY point is (0,-150) mm, giving 125 mm radial encroachment. It therefore cannot be accepted as a fully separated opponent envelope. The 70% box's closest radius is 300 mm, only 25 mm beyond that proxy; this is box geometry, not human-body spacing. See policy_spatial_audit.json. The 50% box is retained as an explicitly failed spatial-policy assumption for review, not a resolved stand-off requirement. A later pass must revise that assumption or accept a quantified partial-reach failure without relaxing the bag envelope.

Owner: Ola reviews the geometric disposition; Michael owns target policy and acceptance of marginal 50% coverage. Acceptance of this residual is **pending**, not inferred from the engineering authorization. No measured loaded reach follows from the changed boxes.
**Track A does not prove strike impulse.** These are prescribed geometry, motion and qualitative air cues. Measured pneumatic propulsion, contact force, durability and real CV remain unverified.