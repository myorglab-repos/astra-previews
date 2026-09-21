> **Ola disposition 2026-09-21: ACCEPTED-A (paper ICD).** Critical inhibit policy remains Lead-owned OPEN. No NEXT_PROMPT. Physical strike still gated on presence + safe_to_actuate + C-01 + B-06 + safety.
>
> **Answers to open Qs:** (1) Session enable = `user_present` AND valid `head_hypothesis` AND NOT `inhibit_latched`; presence alone forever hard-interlocks physical motion/strike. (2) Presence shortlist: ToF preferred, PIR backup, mat optional; Mech mount, Controls fail-safe→absent wiring. (3) Latency stays TBD until bench. (4) Product-facing states follow Stage 0 C-05 aliases; C1 machine is implementation draft to reconcile — discard fixed-shoulder assumptions. (5) P-05 MVP fixture: monitored depressurize + allowed droop; mechanical catch before person-facing, not day-one fixture mandate. (6) F-01/F-05/F-08 confirmed on SoR `B06_ROOT_PITCH_HARDWARE_SKETCH.md` DFMEA table — use DESKTOP GitHub SoR not stale box/Pages. (7) Pitch locked + encoder valid required before pressurized strike (S3), not before all twin/yaw pedagogy. (8) S0/S1 head validity = qualitative spot-check only. (9) SAF-02 E-stop Draft A → in-progress expansion; not CLOSED. (10) Yes — expand to `docs/engineering/CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` next.
# Controls & Perception ICD stub — MVP session enable/inhibit

**Author:** Elias (Controls & Perception) · **Disposition:** Ola (Lead)  
**Status:** DRAFT 2026-09-21 · not Lead freeze · not NEXT_PROMPT  
**Canonical sensing ICD:** `docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md`  
**Related:** `B06_ROOT_PITCH_HARDWARE_SKETCH.md` · `STAGE0_REQUIREMENTS_HAZARD_REGISTER.md`

```
MVP SESSION ENABLE / INHIBIT — one-page stub (Elias draft → Ola)
Rev: DRAFT 2026-09-21 | Owner freeze: OLA | Critical policy: OLA

1. Purpose
   Gate twin logging / trainer session enable from MVP sensing.
   Physical strike remains out of scope until presence + safe_to_actuate
   + C-01 + B-06 + safety (ICD Staging S3).

2. Inputs
   - t_sync
   - user_present : bool   # proximity; AUTHORITATIVE for "at bag"
   - head_hypothesis : { bbox, confidence }  # camera head/human ROI

3. Outputs
   - session_enable : bool
   - twin_overlay : { presence_lamp, head_marker }
   - log_episode : clip + flags

4. Combinational intent (informative until Ola freezes)
   session_enable = user_present
                    AND head_hypothesis_valid   # validity rule TBD — Lead
                    AND NOT inhibit_latched     # controls ICD
   If NOT user_present → idle/safe (no arm play toward empty space).

5. Fail-safes
   - Presence sensor fault → user_present := false
   - Stale t_sync / unknown clock sync → inhibit time-critical use
   - Handheld UI ≠ E-stop

6. Acceptance (quote ICD; numbers Lead-owned)
   - Walk-in → present within declared latency TBD
   - Walk-away → false; twin idle
   - Empty bag → no false presence (normal gym lighting)
   - Head ROI spot-check when present (not Olympic pose)

7. Pitch locked / inhibit strike  [CRITICAL — LEAD-OWNED; B-06]
   Before any physical strike enable (post-MVP S3):
   - Pitch stage reported LOCKED / within hard stops
     (B-06 failure mode "pitch unlock"; Lead F-01)
   - Yaw (and pitch if actuated) encoder VALID
     else INHIBIT strike (B-06 "loss of yaw encoder"; Lead F-05)
   - Pinch / hose hazards monitored per Lead F-08 + Stage 0 H-08
   Numeric thresholds, debounce, PL/SIL: NOT IN THIS STUB.

8. Ownership
   Ola: Critical OPEN/CLOSED, READY, inhibit policy, NEXT_PROMPT.
   Elias desk: draft language only.
```

Supporting disposition packet (Draft A inhibit/E-stop/limp, Draft B acceptance tests, Findings, 10 open questions):  
`/workspace/boxing-trainer/ELIAS_CONTROLS_PERCEPTION_DRAFT_PACKET.md`
