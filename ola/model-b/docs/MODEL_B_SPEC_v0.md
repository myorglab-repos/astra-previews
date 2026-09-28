# Model B (Architecture & Requirements v0)
Name locked: "Model B". Shares the same app and handheld as Model A (decided 2026-09-27).
Status: DRAFT v0 · 2026-09-27 · Owner: Ola · Stage: Feasibility · $0 digital only
All numbers marked ASSUMPTION are unverified estimates, not measurements. No test results exist yet.

## 1. What it is
A retrofit kit that turns a customer's existing chain-hung heavy bag into an interactive trainer. No pole, no floor unit, no separate box.

Kit contents:
1. Clamp collar: adjustable segmented ratchet band, high-grip liner, carries a rotating shoulder ring.
2. Two soft pneumatic arms on the ring (same soft-arm family as Model A, re-rooted to the collar).
3. Back pack between the arm roots: compressor, small air tank, valve block, pressure sensors, main board, IMU, cameras, dock for a removable battery.
4. 3 or 4 adjustable load straps that clip to the chain top ring or swivel (not the bag D-rings), with leveling adjusters.
5. Removable rechargeable battery (power-tool-class 18/20 V platform) plus a desktop charger.
6. Handheld touchscreen and app, shared with Model A.

## 2. Compatibility requirements (customer bag)
| Req | Value | Basis |
|---|---|---|
| Hanging style | Standard chain-hung with top ring or swivel | Design choice |
| Minimum bag weight | 80 lb required, 100 lb+ recommended | Bag survey v0 + tilt estimate; 80 lb floor ASSUMPTION pending swing estimate |
| Diameter range | 13 to 19 in, two collar sizes (13-15, 16-19) | Bag survey v0 (published maker specs) |
| Length | 42 in minimum | ASSUMPTION pending Blender layout |
| Shape | Cylindrical only; no water/aqua or shaped bags | Bag survey v0 |
| Ceiling mount rating | Must cover bag plus kit with margin | Customer responsibility, stated in manual |
Freestanding bags: out of scope at launch (decided 2026-09-27). Planned as a later follow-up.

## 3. Mass budget (ASSUMPTION, all unverified)
| Item | lb |
|---|---|
| Collar + rotating ring | 6 |
| Two soft arms | 6 |
| Pack (compressor, tank, valves, board, cameras, housing) | 10 |
| Battery | 1.5 |
| Straps + clips | 1.5 |
| **Total kit** | **25** |

## 4. Tilt estimate (ASSUMPTION inputs)
The bag settles so the combined center of mass is under the chain. Shift = off-center mass x offset / (bag + kit). Tilt is about atan(shift / pivot-to-CoM distance).
Inputs: net off-center mass of 13 lb (pack 11.5 lb at the back minus partial offset from the arms) at 8 in from the axis. Pivot to center of mass is 30 in.
| Bag lb | CoM shift (in) | Tilt |
|---|---|---|
| 80 | 1.0 | ~1.9 deg |
| 100 | 0.8 | ~1.6 deg |
| 150 | 0.6 | ~1.1 deg |
Conclusion: tilt is small and can be trimmed with the strap adjusters. It has to be confirmed in the Blender physics model and later with a physical bag.

## 5. Strap and clip loads (ASSUMPTION)
- Static kit load: 25 lb.
- Dynamic factor from punches and swing: 3x (ASSUMPTION). Peak is 75 lb spread over 3 straps, so 25 lb per strap.
- Requirement: each strap and clip rated at 5x the peak or more, so a working load limit of 125 lb or more per strap. Use purchased rated hardware.
- The ceiling mount sees the bag plus 25 lb static.

## 6. Power and runtime (ASSUMPTION)
- Battery: 18 V x 5 Ah = 90 Wh nominal, about 72 Wh usable at 80%.
- Compressor draw 60 to 120 W, running 30 to 50% of the time, averages 20 to 60 W. Add about 10 W for electronics and cameras.
- Average draw is 30 to 70 W, so runtime is about **1.0 to 2.4 h per pack**.
- Dual-pack dock for hot-swap is recommended. Validate on the bench (MB-04).

## 7. Safety requirements
- SAF-B1: Mechanical pressure relief valve on the manifold, set below the bladder burst rating.
- SAF-B2: Arms vent automatically on e-stop, fault, lost link, and low battery.
- SAF-B3: Battery latches with a positive latch and sits under a padded cover. Certified pack and battery management system only; no custom lithium.
- SAF-B4: Pinch guards at the rotating ring and collar segments.
- SAF-B5: Rated strap hardware (section 5), plus a secondary retention so a single clip failure can't drop the kit.
- SAF-B6: Collar liner must not damage the bag cover (wear test).

## 8. Model B critical items (all OPEN)
| ID | Item | Severity | How to close |
|---|---|---|---|
| MB-01 | Collar turning or slipping under punch torque and arm reaction | High | Paper estimate, then bench test |
| MB-02 | Tilt and balance | Medium | Blender physics, then physical bag |
| MB-03 | Camera tracking on a swinging bag (IMU compensation) | High | Controls spec, then recorded-video test |
| MB-04 | Runtime per pack | Medium | Paper estimate, then bench test |
| MB-05 | Pack survives impacts, compressor vibration isolation | High | Design, then drop and impact test |
| MB-06 | Strap and clip loads | Medium | Rated hardware plus pull test |
| MB-07 | Bag cover wear from collar | Low | Wear test |

## 9. $0 workstreams (parity with Model A)
1. Bag compatibility survey (sets min weight and diameter range). Ola.
2. Soft arm interface spec for collar mounting. Soft desk (Ismael), reports to Ola.
3. Controls spec: IMU-compensated tracking, venting logic, power states. Controls desk (Elias), reports to Ola.
4. Blender model, renders, physics films (tilt, swing, arm reaction). Ola plus viz pass.
5. BOM with assumptions labeled, DFM notes, test plan. Ola.
6. Start Here: Model A / Model B tab plus Model B section. Pages (Ibrahim).
7. Board: B-ROBO-ALT set to active, $0. Eta.
Hardware tests stay parked, and Stephen gates any spend.

## 10. Open questions for Michael
1. (Closed) Name is Model B.
2. (Closed) Shares the Model A app and handheld.
3. (Closed) Hanging bags only at launch. Freestanding support comes later.

No open questions right now.
