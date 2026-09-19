# Reach definition and tall design case

World X is left/right, opponent is toward negative Y, and nominal floor is Z=0; source model meters are reported as millimeters. The common target box spans X=-260..260 mm and Y=-850..-600 mm. Short head Z=1450..1650, mid=1620..1820, tall=1780..1960 mm. The tall band is an explicit review assumption for a 6'3"-6'5" (1905-1955.8 mm) stature design case, **not an anthropometric fit model**. Abdomen Z=1000..1240 mm uses the same X/Y box.

The saved glove coordinate frame is at the wrist datum. We report point-in-box for that datum, count actual evaluated glove vertices inside the box, and measure nearest sampled vertex-to-box distance when none is inside. Glove AABB overlap is retained in JSON only as a broad-phase test and is not substituted for vertex evidence. Positive vertex inclusion proves those sampled surface points enter the box, not contact, loaded reach or coverage of its entire volume.

## Tall maximum-extension peaks

| Case | Pitch deg | Wrist shortfall mm | Glove vertices inside | Nearest glove vertex shortfall mm | Verdict |
|---|---|---|---|---|---|
| tall_max_L_straight | 24 | 79.278 | 2501 | 0.000 | PASS sampled glove inclusion; datum short |
| tall_max_R_straight | 24 | 79.278 | 2501 | 0.000 | PASS sampled glove inclusion; datum short |
| tall_max_L_hook | 27 | 208.585 | 0 | 49.624 | SHORT / RH-01 |
| tall_max_R_hook | 27 | 208.585 | 0 | 49.624 | SHORT / RH-01 |
| tall_max_L_uppercut | 24 | 177.704 | 0 | 33.693 | SHORT / RH-01 |
| tall_max_R_uppercut | 24 | 177.705 | 0 | 33.693 | SHORT / RH-01 |
| tall_max_L_diagonal | 16 | 80.093 | 2477 | 0.000 | PASS sampled glove inclusion; datum short |
| tall_max_R_diagonal | 39 | 72.095 | 2689 | 0.000 | PASS sampled glove inclusion; datum short |

## Options for another authorized pass

Pitch trades forward reach for height. Increasing pitch alone is not a universal fix. Yaw reorients the carrier but does not add chord length; keep the bag fixed. A strike-dependent guard/stand-off policy can move the assumed target nearer for hook and uppercut, but must be reviewed as a changed target requirement rather than a passed fixed-box test. Alternatively, a longer continuum changes arc length, textile strain, mass, hose routing and return behavior and must be re-audited and eventually identified with coupons.

For scale only, extending the current **straight shoulder-to-wrist ray** until its wrist meets Y=-600 mm requires:

| Prescribed ray | Current chord mm | Ray-scaled chord mm | Added chord mm |
|---|---|---|---|
| straight | 858.915 | 954.722 | 95.808 |
| hook | 720.077 | 978.409 | 258.331 |
| uppercut | 770.103 | 993.608 | 223.504 |

This is an endpoint-ray construction, not a proposed actuator length, validated trajectory or pressure/force result. The final model does not perform this lengthening. Partial 50/70% poses show the same root preset but do not automatically preserve head-band height; RH-02 asks for a coupled pitch/shape policy.

**Track A does not prove strike impulse.** Motion, color emphasis and timing are prescribed illustrations. No measured propulsion, pressure response, contact force, durability or real CV is claimed.