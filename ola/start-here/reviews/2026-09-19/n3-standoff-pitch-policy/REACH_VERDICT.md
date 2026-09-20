# Saved-model reach audit

Vertex inclusion checks actual evaluated surface samples. AABB overlap is broad phase only. The wrist reference is tested independently. Nearest-vertex distance is a sampled distance, not the exact triangle-to-box distance. Deepest vertex margin is the largest, over sampled vertices, of the smallest distance to any box face; it is not a manufacturing tolerance.

## Tall maximum and body L/R

| Case | Pitch deg | Vertices in policy box | Nearest vertex shortfall mm | Wrist shortfall mm | Deepest vertex margin mm | Old-box shortfall mm |
|---|---|---|---|---|---|---|
| tall_max_L_straight | 24.000 | 2501 | 0.000000 | 79.278 | 89.943832 | 0.000 |
| tall_max_R_straight | 24.000 | 2501 | 0.000000 | 79.278 | 89.943839 | 0.000 |
| tall_max_L_hook | 27.000 | 981 | 0.000000 | 88.585 | 69.687304 | 49.624 |
| tall_max_R_hook | 27.000 | 981 | 0.000000 | 88.585 | 69.687196 | 49.624 |
| tall_max_L_uppercut | 24.000 | 1415 | 0.000000 | 57.704 | 78.070623 | 33.693 |
| tall_max_R_uppercut | 24.000 | 1415 | 0.000000 | 57.705 | 78.070557 | 33.693 |
| tall_max_L_diagonal | 16.000 | 2477 | 0.000000 | 80.093 | 89.906718 | 0.000 |
| tall_max_R_diagonal | 39.000 | 2689 | 0.000000 | 72.095 | 89.980271 | 0.000 |
| body_L | -20.000 | 4682 | 0.000000 | 7.140 | 119.807590 | 0.000 |
| body_R | -20.000 | 4682 | 0.000000 | 7.140 | 119.807594 | 0.000 |

The old common box still misses tall hooks by 49.624 mm and uppercuts by 33.693 mm. The new-box successes come from the authorized changed stand-off assumption. Maximum-extension geometry has not moved.

## Partial extension

| Case | Pitch deg | Vertices in policy box | Nearest vertex shortfall mm | Wrist shortfall mm | Deepest vertex margin mm | Old-box shortfall mm |
|---|---|---|---|---|---|---|
| short_short_L_straight | 27.126 | 4 | 0.000000 | 122.939 | 0.571485 | 189.654 |
| short_mid_L_straight | 13.499 | 5170 | 0.000000 | 0.000 | 99.873801 | 0.000 |
| short_short_R_straight | 27.126 | 4 | 0.000000 | 122.939 | 0.571485 | 189.654 |
| short_mid_R_straight | 13.499 | 5170 | 0.000000 | 0.000 | 99.873799 | 0.000 |
| mid_short_L_straight | 49.181 | 4 | 0.000000 | 122.939 | 0.571485 | 290.543 |
| mid_mid_L_straight | 29.110 | 4970 | 0.000000 | 0.000 | 99.919643 | 68.401 |
| mid_short_R_straight | 49.181 | 4 | 0.000000 | 122.939 | 0.571485 | 290.543 |
| mid_mid_R_straight | 29.110 | 4970 | 0.000000 | 0.000 | 99.919643 | 68.401 |
| tall_short_L_straight | 57.000 | 4 | 0.000000 | 146.040 | 0.571485 | 342.963 |
| tall_mid_L_straight | 45.018 | 2106 | 0.000000 | 52.522 | 78.903314 | 187.457 |
| tall_short_R_straight | 57.000 | 4 | 0.000000 | 146.040 | 0.571485 | 342.963 |
| tall_mid_R_straight | 45.018 | 2106 | 0.000000 | 52.522 | 78.903309 | 187.457 |

See REACH_POLICY for the tall 50% centering residual and owners.

**Track A does not prove strike impulse.** These are prescribed geometry, motion and qualitative air cues. Measured pneumatic propulsion, contact force, durability and real CV remain unverified.