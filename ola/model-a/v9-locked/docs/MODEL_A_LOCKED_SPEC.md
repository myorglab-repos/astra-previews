# Model A — locked v9 design, v10 media

Model A is the main product: a universal-bag-kit concept that attaches two soft pneumatic arms and a shallow rear equipment cover to a customer's hanging bag. Michael locked the v9 appearance on 2026-10-06. “Universal” describes the product intent; actual fit, retention and operation have not been qualified. Model B is the original integrated trainer. Engineering part and defect IDs are unchanged.

The locked design uses plain black narrow shoulder covers, black Model B/N1 arm padding and red gloves. The source is [Model_A_Mount_v9_Narrow_Shoulders.blend](../model-a-mount-v9-narrow-shoulders/Model_A_Mount_v9_Narrow_Shoulders.blend). This packet changes visibility, camera position and ghost materials only. No product part is moved, resized or redesigned. The bag and all product parts stay stationary during the camera orbits.

Each arm retains eight soft chambers: U1–U3 in the upper arm, F1–F3 in the forearm and T1–T2 at the soft wrist. Textile limits strain, with venting and elastic textile return as the operating intent. No distal metal, rigid elbow, wrist cam or bearing is introduced. The exposed root metal is a diagnostic padding-off view, not a proposed uncovered operating configuration. Guard palms remain inward, thumbs up and fists toward the fighter. Cross palm-down, hook palm-inward and uppercut palm-up remain the conventions; these films do not animate strikes.

## Engineering dimensions and assumptions

Values below describe nominal CAD geometry or inherited assumptions, not measured hardware. “Reach” here means rear shoulder-cover projection beyond the rear shell plane, not punch reach.

| Item | Locked specification / assumption | Evidence / limit |
|---|---|---|
| Central shell standoff | **ASSUMPTION: 78 mm** at both endpoints | v9 geometry audit; does not include shoulder projection |
| Bag diameter range | **ASSUMPTION: 356–483 mm**, approximately 14–19 in | Two modeled endpoints; intervening sizes and compliant bags unverified |
| Rear shoulder-cover reach | **ASSUMPTION: 81.694 mm / 81.700 mm** at 483 / 356 mm | v9 saved-file audit; below the 82 mm design target |
| Each shoulder cover width | **ASSUMPTION: 298.150 mm** | Both sides, both endpoints; complete cover width, not arm diameter |
| Central shell width | **ASSUMPTION: 423.757 mm** at 483 mm bag | Evaluated source mesh bounding width; separate from shoulder width |
| Shoulder cover / bag minimum gap | **ASSUMPTION: 3.199 mm / 5.998 mm** at 483 / 356 mm | Static polygon-to-nominal-cylinder gap; not tolerance allowance |
| Distal arm / bag minimum gap | **ASSUMPTION: 45.997 mm / 125.204 mm** | Conservative static bound from v9 audit |
| Arm / central-shell sampled minimum gap | **ASSUMPTION: 89.339 mm / 99.004 mm** | Vertex/surface sampling; lower bounds 80.405 / 89.961 mm; not dynamic clearance |
| Battery placeholder | **ASSUMPTION: 110 × 40 × 140 mm** (width × depth × height) | No selected battery, capacity or runtime |
| Mass estimate | **ASSUMPTION: v9 packaging subset ≈4.70 kg / 4.75 kg** at 483 / 356 mm, including 0.65 kg assigned battery | Surface/volume-density scenario only; excludes arms and missing equipment. Complete v9 mass unknown |

The [v9 mass arithmetic](mass_assumptions.json) reuses the assumptions from the [v5 mass estimate](../../2026-10-05/model-a-mount-v5-slim/MASS_ESTIMATE.md): cover surfaces × 2 mm equivalent skin × 1100 kg/m³; rear mounting solids × 2700 kg/m³; straps × 350 kg/m³; backing × 250 kg/m³; polymer dock × 1100 kg/m³; battery assigned 0.65 kg. The central shell uses its outer base surface, avoiding the duplicate inner Solidify skin. Both shoulder envelopes use their evaluated surface areas. Interfaces can overlap and actual foam/laminate construction is undefined, so this is a rough scenario, not a manufacturing bill of materials.

It excludes arms/root assemblies, filled bag, suspension, pump/reservoir, controllers, wiring, unmodeled fasteners and undefined foam stacks. Reusing it as a measured weight or complete product mass would be incorrect. The historical v5 estimate was 5.14 kg for its own packaging geometry; no measured weight saving is claimed. No pressure, force, impulse or life result is inferred in this pass.

## What is actually beneath the padding

The complete named-object inventory is [source_inventory.json](source_inventory.json). The native v9 endpoint scene has these parts:

- Twelve sealed flexible bladder meshes, each with a programmed-knit restraint sleeve and a short soft pigtail (six per arm).
- Four opposed soft wrist torsion cells, each with a short soft feed (two per arm).
- Upper/forearm proximal and distal textile saddles, elastic return strips, continuous retention webbing, soft wrist shear cores and textile/elastomer wrist cuffs.
- Two rounded root anchor eyes, two welded eye tabs and two eight-channel manifold blocks. These are schematic root hardware, not a completed qualified shoulder mechanism.
- Three thin curved rear mounting segments, two tapered rear webs, three flexible backing pieces, two soft bag straps and two low-profile rear buckles.
- One compact battery volume and one polymer dock volume beneath the rear shell. The battery is a packaging placeholder, not an internal cell model.
- Customer bag and suspension chains; these are context, not kit hardware.

Padding-off views hide both v9 shoulder covers, all four upper/forearm contact sleeves, their eight decorative seam meshes and both wrist covers. The v9 shoulder covers already integrate the root-boot form; there is no separate root-boot object to hide. Structural programmed-knit sleeves, textile saddles, straps, return bands and gloves remain. Their presence must not be mistaken for unremoved contact padding. The shell remains opaque in ordinary exposed views and is ghosted with the bag in x-ray views and the shoulder orbit.

**ASSUMPTION / missing:** no compressor, tank/reservoir, control board, power electronics, full supply plumbing, complete wiring, connectors, engineered shell opening or complete fastener/seal details exist in the locked endpoint scenes. Individual soft feeds and the manifold blocks exist, but a routed operating pneumatic circuit does not. No internal/yaw clamp or new yoke is invented: the visible rear segments, webs, straps and root eyes are the existing external mounting concept. Geometry in older scenes is not silently imported to fill these gaps.

## Design history

- **v1:** compared three external rear-mount concepts using intact N1 arms; concept B established the rear-outrigger direction.
- **v2:** restored the Model B materials and look; the 356 mm endpoint exposed a fit issue.
- **v3:** rounded and smoothed the rear battery shell; retained battery size prevented the suggested slim depth.
- **v4:** combined the rear cover and shoulder transitions into one shell; central standoff remained 178.5 mm.
- **v5:** introduced the 78 mm slim shell, segmented rear mount and smaller battery assumption; modeled both endpoint bags.
- **v6:** restored exact Model B arm padding and rounded shoulder boots/adapters.
- **v7:** tucked the shoulder covers; fixed manifolds prevented the 30 mm rear-cover target.
- **v8:** made the shoulders rounder and smoother, with wider covers.
- **v9:** narrowed each cover by about 36.72 mm to 298.15 mm while preserving other parts; Michael locked this design.

## Verification boundary

The source v9 and audited N1 hashes are preserved. Geometry fingerprints check that camera and visibility work does not alter product meshes or transforms. The videos are ten-second, 24 fps camera orbits, not physical arm motion. Render-only ghost materials do not represent real transparency or a manufactured section.

Track A does not prove strike impulse, pneumatic propulsion, contact force, durability or CV. C-01 and B-06 remain OPEN. Physical fit, dynamic clearance, manufacturing thickness, retention and system packaging remain unqualified. The existing authorized Model A external accessory layout is preserved; the original Model B retains stationary fill and carrier-only yaw. No product rotation or new drive is introduced here.
