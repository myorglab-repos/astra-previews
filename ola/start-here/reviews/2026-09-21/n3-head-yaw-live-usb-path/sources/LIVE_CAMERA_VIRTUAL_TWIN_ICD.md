# Live camera → virtual bag twin (training / test ICD)

**Owner draft:** Ola  
**Date:** 2026-09-21 (MVP simplified per Michael)  
**Status:** INTERFACE PLAN — MVP is simple; not a SOTA CV research program  
**Related:** Track A Blender SoR; C-01 Track B; START_HERE readiness checklist; proposed CV→twin agent desk

## Plain language
**MVP (Michael):** the camera mainly watches a **human / head section**. What we need to *trigger* trainer behavior is basically **body tracking / presence** — pair that with a **sensor that detects a body close to the bag**, and we’re good. Keep it simple. Full skeleton / glove CV can come later.

## MVP sensing stack (preferred)

| Channel | What it does | Why |
|---|---|---|
| **Camera — head / human ROI** | Sees the person’s head (and upper body crop) for aim / height / facing cues and for training clips | Matches product camera placement; bounded problem |
| **Near-bag body presence sensor** | Detects that someone is in the work envelope next to the bag | Simple, robust “user present / in range” gate — does not need fancy pose |
| Twin adapter | Maps `user_present` + head cues → twin overlays / height preset hints / logging | Ola + controls |

**MVP trigger logic (intent):**  
`user_present` (proximity) AND camera sees a valid human/head hypothesis → enable trainer session / twin logging.  
No presence → idle / safe (no arm play toward empty space).

## Goals
1. **Train/test** — record head-ROI video + presence timestamps + twin state for simple models.  
2. **Live overlay** — camera + presence drive the virtual bag without claiming full athletic CV.  
3. **Control (later)** — only after safety + C-01; presence remains a hard interlock forever.

## Non-goals (MVP)
- Full-body multi-joint pose as a product requirement  
- Glove tracking / punch-type classification as day-one blockers  
- Using Track A scripted films as proof of real vision  
- Actuating soft arms from unverified perception  

## Architecture

```
Protected camera (head/human ROI) ──┐
                                    ├──→ Capture / sync → Twin adapter → Blender twin + logs
Near-bag presence sensor ───────────┘         ↓
                                         Dataset (clips + presence flags → Snowflake metadata later)
```

| Block | MVP responsibility | Owner |
|---|---|---|
| Camera mount / cover | Head-height ROI, protected | Mech |
| Presence sensor | ToF / PIR / ultrasonic / mat — TBD; fail-safe “absent” | Mech + controls |
| Light perception | Head/human detect in ROI (confidence + bbox) | CV→twin agent / specialist |
| Twin adapter | `user_present`, `head_bbox`, optional facing | Ola + controls |
| Safety | No physical strike unless presence + safe_to_actuate | Safety |

## Twin adapter ICD (MVP minimum)

**Inputs:**
- `t_sync`  
- `user_present` (bool) — from proximity sensor (authoritative for “someone at the bag”)  
- `head_hypothesis` — bbox + confidence in camera ROI (optional facing later)  

**Outputs:**
- Twin overlay (head marker / presence lamp)  
- Session enable / inhibit  
- Logged episode for training  

**Acceptance tests (simple):**
- Walk into envelope → `user_present` true within declared latency  
- Walk away → false; twin goes idle  
- Empty bag, no false presence under normal gym lighting  
- Camera head ROI detects a person when present (spot-check); does not need Olympic pose accuracy  

## Staging
| Stage | Scope |
|---|---|
| S0 | Record head-ROI + presence flags offline |
| S1 | Live presence + head overlay on twin (no arm motion) |
| S2 | Twin commands simulated continuum from simple cues |
| S3 | Physical arms — only with presence interlock + C-01 + B-06 + safety |

## Agent desk implication
CV→twin agent focuses on **head ROI + presence fusion**, not a research pose stack. Human CV hire still Stephen-gated; bot desk can paper the ICD and twin hooks now.

## Snowflake
Later: metadata for clips + `user_present` timelines — not inventing a corpus today.

## Track A demarcation
Prescribed Blender punches remain teaching aids. Presence + head camera is the **first real sensing path**.
