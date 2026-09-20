# B-06 — Protected root / shoulder pitch / hub load-path sketch

**Owner draft:** Ola  
**Date:** 2026-09-19  
**Status:** CONCEPT SKETCH — not fab release; Critical B-06 remains OPEN until designed + analyzed  
**Related:** Stage 0 amendment (carrier yaw + shoulder pitch); Track A visualizes pitch as protected-root attitude

## Plain language
The soft arms tip up and down for tall/short fighters by rotating at the shoulder root — still behind padding, not as exposed metal in the arm. This note sketches what that root must eventually be as hardware.

## Degrees of freedom (protected)
| DOF | Function | Notes |
|---|---|---|
| Yaw | Face opponent | Existing rotating shoulder carrier about mast |
| Pitch | Height preset | Vertical aim of outbound arm axis; Michael: "vertical angle of shoulder outbound" |
| Distal continuum | Punch shape + extension | Soft; no exposed distal metal |

## Proposed mechanical concept (to detail in CAD later)
1. **Fixed hub** on mast — axial retention per bearing practice (shoulders/retainers, not slip-fit only).  
2. **Yaw rotor** — existing cartridge intent (sleeve, saddles, yoke); serviceable flange to arm.  
3. **Pitch stage** between rotor and soft-arm termination — limited range (Track A used review caps ~0..57 deg illustrative; **hardware range TBD**, not that number as rating). Options:  
   - A: Actuated pitch (motor/gear or pneumatic rotary) with hard stops + position sense  
   - B: Manual preset plates / pinned angles for MVP, upgrade to A later  
4. **Soft-arm termination** — textile eye / harness into recessed boot; metal ends here.  
5. **Services** — pneumatic branches + optional electrical through pitch joint (rotary union / flex loop TBD).

## Load path (intent)
Glove → soft wrist → continuum textiles/bladders → shoulder retention → pitch stage → yaw rotor → bearings → hub → mast → base → anchors → slab.  
Bag body impacts are a **separate** path through fill/liners — do not assign bag hits solely to the arm chain.

## Failure modes to feed DFMEA (no fake RPN)
- Pitch stage unlock / free fall under glove mass  
- Bearing axial walk-out  
- Soft termination peel under repeated punches  
- Hose pinch at pitch hinge  
- Loss of yaw encoder → mis-aimed strike (control ICD)

## Track A vs hardware
Track A pitch keys are **attitude storytelling**. They do not size shafts, welds, or motors. B-06 closure needs: envelope drawing, BOM candidates, static/fatigue load cases, and prototype fixture plan — then Stephen for any spend.

## Immediate paper next (no spend)
- One-page interface drawing: mast / hub / yaw / pitch / textile eye  
- Decide MVP: pinned presets (B) vs actuated (A)  
- List open dimensions: bearing ID/OD, pitch travel, boot keep-out

## Non-claims
No rated loads, no cycle life, no supplier selection.
