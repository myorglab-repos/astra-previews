# NEXT_PROMPT
status: in_progress
started_at: 2026-09-19 22:49 ET
runner: codex-cli
timestamp: 2026-09-19 22:52 ET
pass_id: n3-af01b-exposed-arm-swell-2
from: Ola (Robotics Desk)
source: ENGINEERING_ASSESSMENT_N3_AF01B_2026-09-19.md — AF-01b FAIL (exposed pane color-only)

## Goal
Remake AF-01b so **chamber meshes in the EXPOSED LEFT ARM pane geometrically thicken** on fill-more (and relax on vent), readable without the cell board. Inherit prior twin. Keep AF-02 caption sync. No invented forces.

### Hard requirements
1. Exposed-pane blind test: identify thicker cells for straight/hook/uppercut/body from that pane alone (geometry, not brightness).
2. Do not fake pass by only recoloring materials on unswollen meshes.
3. If occlusion hides a fill-more cell, add a second camera angle or brief orbit — document it.
4. Retain board as supplement only; do not rely on it for acceptance.
5. swell_audit + caption_audit + film decode; atlas policy regression unchanged.
6. Packet `reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/`; READY_FOR_OLA.

### Accept criteria
- [ ] Exposed-pane geometry swell visible for all four strikes (Ola film+still review)
- [ ] Captions match panel
- [ ] Fill/vent/return distinct
- [ ] Audits PASS; policy peaks not regressed
- [ ] READY_FOR_OLA

### Out of scope
RH-02 (Ola issues next after this closes); System ID; lengthening arms

## Plain-language
Make the cutaway arm’s soft tubes look physically fatter when they fill — same lesson as the side board, but on the arm itself.

