# B-06 — Option B pinned pitch interface freeze (build-intent)

**Owner:** Ola (Lead)  
**Date:** 2026-09-21  
**Status:** INTERFACE FREEZE for quoting / twin pedagogy — **not** fab release; Critical B-06 remains OPEN until designed + analyzed + prototype  
**Michael direction:** execute BOM/supplier scout; finalize design intent toward build (no further user approvals)

## Plain language
For the first hardware path we freeze **manual pinned height presets** (short / mid / tall), not a live motorized pitch joint. Metal stays in the protected root; soft arm still does the punch.

## Frozen decisions
| Item | Freeze |
|---|---|
| Pitch architecture | **Option B — pinned presets** (detent / pin + flag). Option A actuated = later upgrade, same boot bolt circle reserved |
| Height set | Discrete **short / mid / tall** (Track A teaching angles are drawing aids, not hardware ratings) |
| Soft termination | Textile eye / harness into **recessed boot**; last exposed distal metal forbidden |
| Services through pitch | MVP **flex hose loop** (finite yaw); rotary union only if continuous spin later |
| Lock bit (controls) | Pin/flag engaged → `pitch_lock_engaged` for S3 strike inhibit (see CONTROLS_INHIBIT ICD) |
| Stand-off | **Option A** reach policy — no continuum lengthening |

## Interface stack (outboard)
Mast hub → yaw cartridge → **pitch pin plate** → recessed soft boot → textile eye → continuum.

## Quoting classes (no PO)
Pin plate / detent hardware; limit or flag switch; textile eye / webbing; boot shell; hose loop fittings; yaw bearing cartridge (existing intent). Soft modules and sensing priced in peer BOM scouts.

## Still OPEN (Critical)
Bearing sizing, load cases, fatigue, pinch gap qualification, fab drawings, measured loads — **no invented N·m**.

## Non-claims
Not consumer-ready. Not a release drawing pack.
