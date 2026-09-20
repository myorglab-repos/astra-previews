# NEXT_PROMPT
status: in_progress
started_at: 2026-09-19 23:56 ET
runner: codex-cli
timestamp: 2026-09-19 23:55 ET
pass_id: n3-rh02-partial-extension
from: Ola (Robotics Desk)
source: ENGINEERING_ASSESSMENT_N3_AF01B2_2026-09-19.md (AF-01b CLOSED-A) + docs/engineering/RH02_PARTIAL_EXTENSION_STAGED.md

## Goal
Close **RH-02**: partial-extension (≈50%/70%) strokes must keep declared head-band aim **or** be explicitly declared non-head-target, without bag-proxy encroachment. Inherit Option A stand-off / pitch policy twin. No continuum lengthening. No invented forces.

### In scope
1. Document partial-extension aim policy (coupled root pitch + continuum shape weights, OR declare partials as non-head-band for named cases).
2. Apply in Blender for short/mid/tall × 50%/70% (and existing max cases regression).
3. Re-audit spatial policy: declared head boxes must not clip / overlap bag proxy; report shortfall mm honestly.
4. Film or atlas stills showing partials under the new policy; clearance regression on G-03/G-05 proxies unchanged-or-better.
5. Packet `reviews/2026-09-19/n3-rh02-partial-extension/`; READY_FOR_OLA with plain-language glossary.

### Constraints
- Architecture freeze (soft 8-chamber continuum; no distal metal; Option A — no arm lengthening).
- Track A does not prove strike impulse.
- No invented pressure / force / life numbers.
- Preserve prior accepted atlas peaks unless intentionally superseded and called out.

### Accept criteria
- [ ] Written RH-02 policy in packet (plain + engineering terms)
- [ ] Partial cases re-audited; head-band inclusion or explicit non-head declaration
- [ ] No bag-proxy encroachment for declared head boxes
- [ ] Film/atlas evidence + audits; READY_FOR_OLA
- [ ] Glossary in READY_FOR_OLA

### Out of scope
AF-01 remakes; System ID / C-01 coupons; B-06 hardware fab; RH-03 routing materials deep dive

## Plain-language
When the arms only punch part-way out, the glove should still aim where we say it aims (or we must admit that partial punch is not a head shot). Do not make the soft arms longer.

