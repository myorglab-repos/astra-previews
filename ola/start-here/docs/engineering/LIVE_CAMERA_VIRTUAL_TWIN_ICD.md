# Live camera → virtual bag twin (training / test ICD)

**Owner draft:** Ola  
**Date:** 2026-09-21  
**Status:** INTERFACE PLAN — not a CV research paper; specialists own model training  
**Related:** Track A Blender SoR; C-01 Track B; production-readiness checklist on START_HERE

## Plain language
Later we want a **real camera** watching a person (or a physical bag) and driving or labeling the **virtual punching-bag model**, so we can train and test AI models. This note freezes how engineering should plug that in — without pretending the Blender films are real CV today.

## Goals
1. **Train** — capture synchronized video + twin state (or human labels) for perception / trainer models.  
2. **Test** — replay or live-feed camera into the twin; score detection / pose / strike events against acceptance tests.  
3. **Control (later)** — optional closed loop: perception output commands soft-arm setpoints (only after safety + C-01 gates).

## Non-goals (now)
- Freelancing SOTA CV papers or claiming product tracking works.  
- Using Track A prescribed films as proof of real vision.  
- Hitting a user with air-powered arms from unverified perception.

## Architecture (streams in parallel)

```
Camera(s) → Capture PC → Perception service → Event / pose bus → Twin adapter → Blender/digital twin
                              ↓
                         Dataset lake (Snowflake / object store) ← labels, sync metadata
```

| Block | Responsibility | Owner seat |
|---|---|---|
| Cameras / lighting / mounts | Protected cameras on product; lab rig first | Mech + CV |
| Capture PC | Time sync, recording, privacy | Platform / Ibrahim |
| Perception service | Pose, glove, strike events (black box ICD) | **CV specialist hire** |
| Twin adapter | Map events → twin DOF / overlays / logging | Ola + controls |
| Dataset | Versioned clips + labels in warehouse | Snowflake ingest (Eta/Ibrahim) |
| Safety gate | Inhibit physical actuation unless perception confidence + interlocks OK | Safety + controls |

## Twin adapter ICD (minimum)

**Inputs (from perception, versioned schema):**
- `t_sync` (UTC or PTP)  
- `user_pose` / `glove_bbox` / `strike_hypothesis` (type, side, confidence)  
- Optional: depth / skeleton keypoints  

**Outputs (to twin / trainer):**
- Overlay markers on twin  
- Commanded height preset ID (short/mid/tall) — **not** inventing pitch hardware ratings  
- Logged episode for dataset  

**Acceptance tests (examples — specialists refine):**
- Latency budget TBD measured end-to-end (capture → twin overlay)  
- Sync error < declared ms bound on clapboard / LED flash fixture  
- False-positive strike rate on still scene below threshold  
- No physical arm motion unless `safe_to_actuate==true`

## Staging
| Stage | What we run |
|---|---|
| S0 | Dataset + offline train/test on recorded video only |
| S1 | Live camera → twin **overlay only** (no arm motion) |
| S2 | Live camera → twin + **simulated** continuum commands |
| S3 | Live camera → physical soft arms (after C-01, B-06, safety) |

## Hiring implication
CV / perception contractor or FTE is a first-wave seat for S0–S1. Courtland shortlists only after Michael + Stephen approve spend. Eta/Art advising platforms.

## Snowflake
Use warehouse for **versioned training artifacts metadata** (paths, hashes, label schemas) — not as a substitute for video object storage. Ingest procedures stay with Eta/Platform write MCP; Ola consumes via `search_documents` / linked SoR paths.

## Track A demarcation
Prescribed Blender punches remain teaching aids. Live-camera work is a **separate stream** with its own READY packets and never closes C-01 by itself.
