# Model B (Architecture & Requirements v1)
Status: DRAFT v1 · 2026-09-28 · Owner: Ola · Stage: Feasibility · $0 digital only
Replaces v0. Shape locked by Michael on 2026-09-28 (v5 renders). ASSUMPTION marks unverified numbers. No test results exist yet.

Public pages (Oct 2026): this kit is Model A, the universal bag. The original integrated trainer is Model B. This file is not renamed. In the sections below, "Model B" means this kit and "Model A" means the original integrated trainer. IDs such as MB-08 are unchanged.

## 1. What it is
A bag add-on kit that turns a customer's chain-hung heavy bag into an interactive trainer. It has no pole, no floor unit and no rotating ring. It uses the same app and handheld as Model A.

Kit contents:
1. A rear padded saddle wrapping about 170° of the back of the bag.
2. Two parallel 38 mm polyester canvas straps, 120 mm apart, one crank ratchet each. The ratchets sit on the rear saddle about 31° either side of back center, next to the pack. The D-ring anchors are at about 24°. The front of the bag has no hardware.
3. Two soft arms copied 1:1 from Model A (N1). The arm design, bladders, sleeves, foam, wrist and glove are unchanged. Only the root mounting is new.
4. A rear pack (compressor, small tank, valve block, pressure sensors, board, IMU, cameras) with a slide-in battery below it.
5. A vertical webbing tether from the saddle to the chain ring as secondary retention.
6. The handheld and app shared with Model A.

## 2. Arm mounting (locked geometry from the v5 Blender model)
| Item | Value | Basis |
|---|---|---|
| Arm roots | Back ±56° (rear-left, rear-right), fixed, no yaw | v5 model |
| Root center height | About 1.56 m, 0.39 m below bag top | v5 model |
| Root center standoff | About 150 mm from a 19 in bag surface | v5 model, set by clearance check |
| Arm scale | 100% Model A | Michael: no shrink without proof of no performance loss |

## 3. Arm-to-bag clearance (measured in the model, not a physical test)
- Method: every 8th frame of the full Model A strike animation (frames 1 to 1920), with arm meshes checked against a rigid 19 in cylinder.
- At the first mounting distance the arms cut into the bag by 8 to 13 mm at guard and up to 28 mm in strikes. Roots were moved out 46.5 mm.
- Result: minimum clearance is 14.1 mm (left, frame 1081) and 16.4 mm (right, frame 1273). Model A's own figure is about 4 mm.
- Not covered: cover bulge under strap tension, bag deformation from user punches, arm sag and motion scatter. T-10 closes this.

## 4. Compatibility (customer bag)
| Req | Value | Basis |
|---|---|---|
| Hanging | Chain-hung with top ring or swivel | Design choice |
| Diameter | 16 to 19 in at launch; 19 in is the design point | Bag survey; 19 in is the widest standard cylindrical bag found |
| Smaller bags (13 to 15 in) | Later, with a root spacer so arm geometry stays the same | ASSUMPTION |
| Minimum weight | 80 lb required, 100 lb+ recommended (most 16 to 19 in bags are 100 to 250 lb) | Survey + tilt estimate |
| Minimum length | 42 in | Strap zone plus strike zone, ASSUMPTION |
| Shape | Cylindrical only | Survey |
Freestanding bags remain out of scope at launch.

## 5. Mass budget (ASSUMPTION)
| Item | lb |
|---|---|
| Saddle, straps, ratchets, tether | 4 |
| Two Model A arms including root boots | 8 (full-size arms, not yet weighed; was 6 in v0) |
| Pack | 10 |
| Battery | 1.5 |
| **Total** | **23.5** (ceiling 30) |

## 6. Power, tilt and loads
Same method as v0; see ESTIMATES v1. Runtime is still 1.0 to 2.4 h per pack on paper.

## 7. Safety requirements
- SAF-B1 Mechanical relief valve below bladder burst rating.
- SAF-B2 Arms vent on e-stop, fault, lost link and low battery.
- SAF-B3 Certified tool-platform battery under a padded, latched cover.
- SAF-B4 All rigid parts (arm flange, carrier tube, manifold, ratchets) behind padding or on the rear, away from the user's side. Ratchet levers get a padded flap.
- SAF-B5 Rated straps and ratchets, plus the vertical tether so one strap failure can't drop the kit.
- SAF-B6 Saddle liner must not damage the bag cover.
- SAF-B7 Arm foam stays at Model A thickness until an arm-body contact test (T-11) supports any change.

## 8. Critical items
| ID | Item | Severity | Status |
|---|---|---|---|
| MB-01 | Saddle turning or slipping under arm reaction | High | Open, paper margin in E1 |
| MB-02 | Tilt and balance | Medium | Open |
| MB-03 | Tracking on a swinging bag | High | Open (Controls) |
| MB-04 | Runtime | Medium | Open |
| MB-05 | Pack impact and vibration | High | Open |
| MB-06 | Strap, ratchet and tether loads | Medium | Open |
| MB-07 | Cover wear | Low | Open |
| MB-08 | Arm clearance to bag | High | Closed in model (14 mm min); physical check T-10 |
| MB-09 | Root standoff bending load (150 mm) | Medium | New, open |

## 9. Open questions for Michael
None right now.
