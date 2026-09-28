# Model B v3: Change Notes
Date: 2026-09-27 · Owner: Ola · Replaces the v2 wide front band. Renders are in `renders_v3/` and the script is `blender/build_model_b_v3.py`. Every rating below is a target to confirm from purchased-hardware datasheets. There are no test results.

## 1. Crank ratchet tightening (replaces the v2 ladder-buckle band)
- Each front strap ends in a cargo-style crank ratchet on the side of the bag, one on the left and one on the right, just forward of the rear saddle and below the arm roots.
- How it works: the loose strap end feeds through a slotted spool. Each pump of the handle turns the spool one tooth and winds the strap onto it, and a spring pawl on the toothed wheels stops it unwinding. To release, pull the release tab and open the handle fully, and the spool free-spins.
- Why it suits heavy bags: sand, rag and fabric fills settle and compact over time, so the bag gets slightly thinner where the kit sits. With a crank ratchet you just pump it a few clicks to take up the slack without undoing anything.
- Risk: a ratchet gives a lot of leverage, so it's easy to overtighten, crush the bag cover or overload the strap. Mitigation: use a small ratchet (1 to 1.5 in class), add a printed tension witness mark on the strap, and write a "snug plus 2 clicks" rule into the instructions. The actual target tension comes from the grip estimate and bench test T-01.

## 2. Two thinner straps crossing the front (replaces the one wide band)
- A padded rear saddle carries the pack and both arm roots. It's the rear part of Model A's shoulder band.
- Two 38 mm (1.5 in) straps run from the saddle around the front in an X. Strap A starts high on the left saddle edge and runs down to the right ratchet, and strap B is the mirror image.
- Where they cross, the two straps are sewn together with a box-X stitch patch so the X stays centered and the straps can't creep up or down.
- The X sits below the arms' guard line so the gloves don't strike the hardware. There's no rigid hardware on the front, only fabric.
- Why an X: two diagonal straps grip the bag over a taller area than one flat band, and they also resist the kit twisting or tipping when an arm pushes off.

## 3. Strap material: polyester canvas
- The front X straps and all three hanger straps are heavy polyester duck canvas webbing, 38 mm for the X straps and 25 mm for the hangers. It has the look and feel of canvas and is woven flat and dense. The renders show it in a natural grey canvas color with the weave visible. The production color could be black.
- Why not 100% cotton canvas: cotton stretches when it's damp from sweat, which lets the straps lose ratchet tension. It also absorbs sweat and mildews. Polyester canvas holds tension when wet and resists rot and UV. A cotton-poly blend is a fallback if a softer feel is wanted.
- Ends are folded and bar-tacked, and a stitched stop on each loose end keeps it from pulling out of the ratchet.

## 4. Arms rebuilt to Model A geometry and articulation
- The arm roots are at the rear-left and rear-right, about 58 deg either side of the back, the same as Model A's rear-mounted arms.
- The arms use the same soft continuum build as Model A, with no pins, hinges or metal in the arm:
  - Upper section: three bladders at 120 deg (U1 to U3) inside a knit restraint sleeve with a red programmed bias region.
  - A flexible textile saddle acts as a virtual elbow. There's no elbow pin.
  - Forearm: three bladders at 120 deg (F1 to F3).
  - Soft torsion wrist, about 105 mm long, with two opposite-handed torsion cells (T1 and T2) for palm rotation.
  - Two elastic return bands per section, a textile restraint band every few centimeters, and a padded glove on a soft cuff.
- That's eight chambers per arm and 16 for the pair, the same as Model A.
- Motion is shown in a four-pose strip (guard, straight, hook, uppercut), which reuses Model A's strike studies. The poses are prescribed geometry. Nothing here proves the arm reaches or holds them under pressure (ASSUMPTION).
- A cutaway render shows the arm with its cover off: the three bladders per section, the sleeve bands, the red bias stripe, the return bands and the wrist cells.
- Scale: Model A's straight reach from shoulder to wrist is about 859 mm. The modeled straight pose here is roughly the same order, but it's geometric and not measured.

## 5. The red and black "wire" is a safety tether
- It isn't electrical. It's a secondary retention tether that runs from the pack frame up to the bag's chain ring or swivel, separate from the three hanger straps. It hangs slightly slack and only takes load if a hanger strap, cam buckle or snap hook fails, so the kit can't drop.
- It belongs in the design. v3 changes it from a thin red cord that looked like wiring to 12 mm black webbing with a red tag at the pack end.
- There's no electrical cable to the ceiling. The kit runs from the slide-in battery in the pack.

## 6. Arm roots stay fixed (decided 9/27)
- There is no rotating shoulder ring in Model B. The arm roots are fixed to the rear saddle, and the arms aim using their own soft steering (U and F sections). This keeps the kit thin and avoids putting a bearing inside a clamped strap system.

## 7. v5 (2026-09-28): copied Model A arms, 19 in bag, parallel straps, rear ratchets
- Arms: 94 Model A N1 exterior arm objects copied 1:1 (no re-model). Script `blender/build_model_b_v5.py`, source `/workspace/modelA_src/N1.blend` (LFS).
- Bag: 19 in (483 mm) large bag class (≈88% of Model A 550 mm).
- Straps: two parallel 38 mm canvas straps, 120 mm apart; ratchets moved onto rear saddle (≈±40° from back), opposite sides.
- Arm thickness homework (measured from the Model A mesh, ±5 mm because arms are curved; NOT test data):
  upper arm bladder bundle ≈69 mm vs foam contact sleeve OD ≈143 mm; forearm bundle ≈86 mm vs foam OD ≈129 mm.
  About half the visible thickness is the replaceable foam/textile laminate, not the actuator.
  Model A has no frozen soft OD and no measured pressure/force, so the only zero-risk slimming is the foam layer; actuator untouched.
  Trade: less arm-body padding means a contact-safety check (glove still carries strike impact). ASSUMPTION until tested.
