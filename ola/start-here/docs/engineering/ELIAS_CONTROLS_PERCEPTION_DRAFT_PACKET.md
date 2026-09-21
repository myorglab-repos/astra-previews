> **Ola disposition 2026-09-21: ACCEPTED-A (paper ICD).** Critical inhibit policy remains Lead-owned OPEN. No NEXT_PROMPT. Physical strike still gated on presence + safe_to_actuate + C-01 + B-06 + safety.
>
> **Answers to open Qs:** (1) Session enable = `user_present` AND valid `head_hypothesis` AND NOT `inhibit_latched`; presence alone forever hard-interlocks physical motion/strike. (2) Presence shortlist: ToF preferred, PIR backup, mat optional; Mech mount, Controls fail-safe→absent wiring. (3) Latency stays TBD until bench. (4) Product-facing states follow Stage 0 C-05 aliases; C1 machine is implementation draft to reconcile — discard fixed-shoulder assumptions. (5) P-05 MVP fixture: monitored depressurize + allowed droop; mechanical catch before person-facing, not day-one fixture mandate. (6) F-01/F-05/F-08 confirmed on SoR `B06_ROOT_PITCH_HARDWARE_SKETCH.md` DFMEA table — use DESKTOP GitHub SoR not stale box/Pages. (7) Pitch locked + encoder valid required before pressurized strike (S3), not before all twin/yaw pedagogy. (8) S0/S1 head validity = qualitative spot-check only. (9) SAF-02 E-stop Draft A → in-progress expansion; not CLOSED. (10) Yes — expand to `docs/engineering/CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` next.
# Elias — Controls & Perception disposition packet (draft for Ola)

**Author desk:** Controls & Perception (peer under Ola / Lead Robotics)  
**Product:** AI-Powered Boxing Training System  
**Date:** 2026-09-21 (America/New_York)  
**Status:** DRAFT for Ola disposition — not Lead freeze; not NEXT_PROMPT  
**Ownership reminder:** Ola owns Critical OPEN/CLOSED, READY accept/reject, NEXT_PROMPT, and inhibit policy. This packet recommends interface language only.

---

### Summary

Pulled the MVP Live Camera → Virtual Twin ICD (identical on SoR mirror and `_pc_sync`; canonical path below), Stage 0 hazard/requirements register (boxing-trainer + richer astra-cli-setup amendment copy), C1 `control_interface.md` / `engineering_handoff.md` (pb-align), B-06 root/pitch sketch, START_HERE readiness rows (safety envelope + CV→twin), and the Controls & Perception role brief. Draft scope is **MVP only**: head/human ROI + near-bag presence fusion for twin/session enable, plus controls **inhibit / E-stop / limp / fail-safe vent** concepts grounded in existing hazard and C1 state language. No timings, FPS, pressure setpoints, latency budgets, or sensor accuracy numbers are invented — TBD or Lead-owned placeholders throughout. Critical inhibit policy and OPEN/CLOSED remain Ola-owned.

---

### Findings (severity)

- **Critical** — No Lead-frozen inhibit / E-stop / limp ICD exists yet; Stage 0 `P-05` fault vent policy and `SAF-02` independent motion-enable/stop remain OPEN. Source: `STAGE0_REQUIREMENTS_HAZARD_REGISTER.md` §§2.3, 2.6. Ola owns freeze.
- **Critical** — Physical strike gated on `presence + safe_to_actuate` + C-01 + B-06 + safety; S3 staging forbids arm actuation from unverified perception. Source: `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` §§Goals, Architecture Safety row, Staging S3.
- **Critical** — B-06 remains Critical OPEN (root/bearing/hub/pitch). Box/Pages B-06 md still lists unlabeled DFMEA starter bullets; START_HERE (21 Sep) claims “DFMEA starter sketch updated” but numbered **F-01 / F-05 / F-08** rows are **not present** on the synced md/html. Lead steering maps: **F-01** pitch-stage lock (unlock/free-fall), **F-05** yaw-encoder loss → inhibit strike, **F-08** hose/pinch at pitch hinge. Cite failure-mode bullets under B-06 “Failure modes to feed DFMEA” until SoR numbered table lands. Source: `B06_ROOT_PITCH_HARDWARE_SKETCH.md`; `START_HERE.html` §05 open items / §06 readiness.
- **High** — H-01 high-energy contact: proximity/enable interlock required before person-facing use; residual owner Michael. Source: Stage 0 §3 H-01.
- **High** — H-03 gravity sag / limp bladder on vent or power loss: fault pose policy must **not** be “open all vents” blindly; may need catch/support. Source: Stage 0 §3 H-03; C1 handoff “On loss of power… inhibited supply and monitored depressurization… not an assumed automatic retraction to guard.”
- **High** — H-04 overpressure / bladder burst: relief + monitored supply isolation; ratings TBD. Source: Stage 0 §3 H-04; Track B plan “Overpressure relief mandatory… Fail-safe vent policy drafted before multi-chamber tests.”
- **High** — H-08 pinch at rotating shoulder band; SAF-03 OPEN; B-06 hose pinch at pitch hinge (Lead F-08). Source: Stage 0 §3 H-08 / §2.6 SAF-03; B-06 failure modes.
- **High** — H-13 tracking loss → unexpected motion: confidence gate, bounded motion, fail to guard/vent; H-14 AI must not be sole motion limit — independent deterministic enable chain. Source: Stage 0 §3 H-13, H-14; C1 “AI does not issue valve duty cycles or select pressure limits.”
- **High** — Presence sensor modality TBD (ToF / PIR / ultrasonic / mat); must fail-safe to **absent**. Declared latency for walk-in/out tests is **not** set (ICD says “within declared latency”). Source: ICD §§MVP sensing stack, Acceptance tests.
- **Medium** — C-04 / H-15: handheld is **not** safety-rated E-stop; real E-stop hardware path required. Source: Stage 0 §2.5 C-04, §3 H-15.
- **Medium** — C1 state machine has BOOT_INHIBITED / FAULT_LATCHED / supply inhibit / monitored vent concepts, but is C1-era draft (fixed shoulders; pre-N3 pitch/yaw product freeze) — must be reconciled to N3+ Stage 0 / ICD MVP before freeze. Source: `pb-align/revision_c/control_interface.md` §§Logical architecture, State machine.
- **Medium** — MVP trigger is AND of `user_present` (authoritative proximity) and valid `head_hypothesis`; session enable/inhibit is an ICD output, but fusion thresholds, debounce, and inhibit latch semantics are Lead-owned TBD. Source: ICD §§MVP trigger logic, Twin adapter ICD.
- **Low** — C-05 proposes states: disabled/vented, enabled guard, fill/steer, return, fault — overlaps C1 but not reconciled. Source: Stage 0 §2.5 C-05.
- **Info** — START_HERE §06: Safety envelope (vent, pinch, limp, E-stop, proximity) OPEN; CV / live camera → virtual twin OPEN (planned). Consumer-ready requires Critical safety + C-01 + B-06 + controls closed with evidence.
- **Info** — Role scope: peer drafts only; no replace Ola on architecture freeze / Critical / READY / NEXT_PROMPT / inhibit policy. Source: `talent-desk/boxing-peers/controls-perception-engineer.md`.
- **Info** — ICD path comparison: `astra-previews/.../LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` vs `_pc_sync/...` differ only by trailing newline; same 2026-09-21 MVP content. Canonical used: Ola start-here engineering path (below).

---

### Draft A — Inhibit / E-stop / limp ICD outline

**Purpose:** Interface outline for Ola disposition. Concept-level only. **Critical language = Lead-owned placeholders.** No novel architecture beyond Stage 0, C1 control_interface, B-06, Track B gates, and MVP ICD.

#### A.0 Document control (stub)
- Title / rev / owner: **[LEAD-OWNED]**
- Applies to: soft continuum arms + carrier; MVP sensing interlocks
- Normative vs informative: outline informative until Ola marks CLOSED

#### A.1 Scope & non-goals
- In scope: supply inhibit, physical E-stop path, limp / fault-vent concepts, proximity & perception gates feeding session/motion enable
- Out of scope (MVP): full athletic pose CV; AI-selected pressures; SIL/PL certification claims; invented numerical bounds

#### A.2 Reference architecture (concept)
- Deterministic request validator + independent limit/fault monitor → **supply inhibit / monitored vent** (C1 diagram intent)
- Planner/AI advisory only; does not clear latches or set pressure limits (C1; Stage 0 H-14)
- Presence remains a **hard interlock forever** (ICD Goals #3)

#### A.3 Valve / timing interfaces (concept — no numbers)
| Interface | Intent | Placeholder |
|---|---|---|
| Per-chamber fill | Bounded fill under READY + enables | Duty / rate limits **TBD — Lead** |
| Controlled exhaust | Metered return; avoid snapback (H-02) | Exhaust profile **TBD — Lead / Track B TB-04** |
| Fault vent / dump | Monitored depressurization; not blind full-open (H-03) | Vent policy **[CRITICAL — LEAD-OWNED P-05]** |
| Master supply shutoff | Isolation on inhibit / E-stop / fault | Hardware path **[CRITICAL — LEAD-OWNED SAF-02]** |
| Mechanical relief | Independent of fill valve isolation (H-04; handoff schematic) | Setpoint **TBD** before pressurized FP |

Acceptance language stub: *“Fill commands rejected unless state==READY and all interlocks true; inhibit de-asserts fill within Lead-declared stop path; vent response validated for hose obstruction and gravity/elastic droop.”* Timings = **TBD — Lead**.

#### A.4 Inhibit
- **Sources (OR → inhibit motion / fill):** physical stop; stale required sensor; lost/ low-confidence tracking (H-13); `user_present==false` (ICD); over-limit; watchdog; leak; comms loss; commissioning incomplete; **yaw encoder invalid** (B-06 failure mode / Lead **F-05**); **pitch not confirmed locked** when strike enabled (Lead **F-01** + ICD stub intent)
- Latch: AI restart / network reconnect / pressure recovery **must not** clear (C1)
- Output: session enable/inhibit to twin adapter (ICD outputs)
- **Inhibit policy detail: [CRITICAL — OLA-OWNED]**

#### A.5 Limp mode / fault pose
- Aligns to H-03 “limp bladder” + C1 FAULT_LATCHED: inhibit supply + validated vent response
- Depressurized arm may **droop**, not auto-return to guard (C1; handoff)
- Catch/support may be required — **[LEAD-OWNED]** whether mechanical catch is MVP vs later
- Acceptance stub: *“Fault injection on guarded fixture: power loss and commanded inhibit reach defined limp/vent state without uncontrolled snapback or undocumented strike.”* Metrics **TBD**.

#### A.6 E-stop / fail-safe venting
- Independent hardware E-stop path; handheld ≠ E-stop (C-04, H-15)
- Stop path must not wait on AI service (C1)
- Fail-safe presence: sensor loss → **absent** (ICD)
- Overpressure: relief + monitored isolation (H-04, SAF-04, Track B gates)
- Acceptance stub: *“E-stop from any ACTIVE/READY state inhibits supply and executes Lead-approved vent; manual reset required; reset does not start motion.”*

#### A.7 Contact / pinch / overpressure / proximity gates (recommendations only)
| Gate | Source hook | Draft recommendation | Lead status |
|---|---|---|---|
| Proximity / `user_present` | ICD; H-01 | Authoritative for “someone at bag”; AND with head hypothesis for session enable; hard interlock for physical strike | OPEN |
| Contact energy | SAF-01; H-01 | Bound before human trials; instrumented contact on fixture first | OPEN — **Critical placeholder** |
| Pinch (band) | H-08; SAF-03 | Geometry + carrier enable interlocks + displacement tests | OPEN |
| Pinch (pitch hose) | B-06; Lead **F-08** | Keep-out / routing + inhibit if pinch sensor/limit trips (**TBD** modality) | OPEN |
| Overpressure | H-04; SAF-04 | Relief + isolation; no pressurized multi-chamber without drafted vent policy | OPEN |
| Pitch locked | B-06; Lead **F-01** | No strike enable unless pitch stage reported locked / within hard stops | **[CRITICAL — LEAD]** |
| Encoder valid | B-06; Lead **F-05** | Encoder fault → inhibit strike / carrier command | **[CRITICAL — LEAD]** |

#### A.8 Proposed state set (reconcile C-05 ↔ C1 — Lead chooses)
Stub set for disposition (not frozen): POWER_OFF → BOOT_INHIBITED → COMMISSIONING_REQUIRED → READY → ACTIVE → FAULT_LATCHED → SERVICE_ISOLATED; map Stage 0 “disabled/vented, enabled guard, fill/steer, return, fault” as aliases or replace. **Ola decides.**

#### A.9 Acceptance language stubs (controls)
1. Inhibit asserts on each listed source; fill valves commanded closed / supply inhibited — **pass criteria Lead-owned**.
2. E-stop path independent of UI/handheld and of CV service availability.
3. Limp/vent: no uncontrolled drop or snapback per P-05 intent — characterization via Track B TB-04 before multi-chamber person-facing.
4. Presence false or fail-safe absent → twin idle; no arm play toward empty space (ICD).
5. Encoder invalid or pitch unlock (F-05 / F-01) → strike inhibit — **wording Lead-owned**.

---

### Draft B — Head-ROI + near-bag presence acceptance-test outline

**MVP only — not full-body pose athletics.** Aligns to `LIVE_CAMERA_VIRTUAL_TWIN_ICD` twin hooks. No invented FPS or accuracy numbers.

#### B.1 Dataset brief stubs (S0)
| Field | Content |
|---|---|
| Clips | Head/human ROI video only (protected camera mount — Mech) |
| Labels | `user_present` timeline (proximity), `head_hypothesis` bbox + confidence, `t_sync`, twin state |
| Non-goals | Multi-joint skeleton, glove class, punch-type labels as day-one blockers |
| Privacy | Local processing default; recording off unless explicitly enabled (C1 privacy note) |
| Snowflake | Metadata later — not inventing corpus today (ICD) |
| Pass bar | Spot-check person-present detection; “does not need Olympic pose accuracy” (ICD) |

#### B.2 Twin adapter signals (normative MVP)
**Inputs:** `t_sync`, `user_present` (bool, proximity authoritative), `head_hypothesis` (bbox + confidence; optional facing later)  
**Outputs:** twin overlay (head marker / presence lamp); **session enable / inhibit**; logged episode  
**Trigger intent:** `user_present` AND valid head hypothesis → enable session / twin logging; else idle / safe

#### B.3 Acceptance tests (outline)
| ID | Test | Pass language (no fake metrics) |
|---|---|---|
| AT-P1 | Walk into work envelope | `user_present` → true within **declared latency TBD — Lead** |
| AT-P2 | Walk away | `user_present` → false; twin idle |
| AT-P3 | Empty bag, normal gym lighting | No false presence |
| AT-P4 | Presence sensor power/signal loss | Fail-safe **absent**; session inhibited |
| AT-H1 | Person in ROI, present | Head/human hypothesis asserted (spot-check); confidence gate **TBD — Lead** |
| AT-H2 | No person / empty ROI | No valid head hypothesis; session not enabled |
| AT-F1 | Fusion | Enable only if presence AND valid head hypothesis (ICD trigger) |
| AT-F2 | Presence without head / head without presence | Session remains inhibited; twin may show diagnostic overlay **[Lead UX]** |
| AT-S1 | Sync | Unknown camera–controller sync invalidates time-critical fusion (C1 timing note); S0/S1 logging still allowed with quality flag |
| AT-ST1 | Staging S1 | Live presence + head overlay on twin — **no arm motion** |
| AT-ST3 | Staging S3 gate | Physical arms only with presence interlock + C-01 + B-06 + safety (ICD) |

#### B.4 Explicit non-claims
- Not proving athletic CV, Track A films ≠ vision proof
- Not actuating soft arms from unverified perception
- Confidence/IoU/FPS/latency numbers remain **TBD** until Lead declares

---

### Draft C — One-page ICD stub (presence + head → session enable/inhibit)

```
MVP SESSION ENABLE / INHIBIT — one-page stub (Elias draft → Ola)
Rev: DRAFT 2026-09-21 | Owner freeze: OLA | Critical policy: OLA

1. Purpose
   Gate twin logging / trainer session enable from MVP sensing.
   Physical strike remains out of scope until presence + safe_to_actuate
   + C-01 + B-06 + safety (ICD Staging S3).

2. Inputs
   - t_sync
   - user_present : bool   # proximity; AUTHORITATIVE for “at bag”
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
     (B-06 failure mode “pitch unlock”; Lead F-01)
   - Yaw (and pitch if actuated) encoder VALID
     else INHIBIT strike (B-06 “loss of yaw encoder”; Lead F-05)
   - Pinch / hose hazards monitored per Lead F-08 + Stage 0 H-08
   Numeric thresholds, debounce, PL/SIL: NOT IN THIS STUB.

8. Ownership
   Ola: Critical OPEN/CLOSED, READY, inhibit policy, NEXT_PROMPT.
   Elias desk: draft language only.
```

---

### Open questions for Ola (Lead)

1. Freeze MVP trigger as hard AND (`user_present` ∧ valid `head_hypothesis`) for **session** enable, with presence alone as the forever **motion** interlock — or different split?
2. Declare presence modality shortlist (ToF / PIR / ultrasonic / mat) and fail-safe wiring owner (Mech vs Controls) for ICD normative text.
3. Set **declared latency** placeholders for AT-P1/P2 (or explicitly leave TBD until bench)?
4. Reconcile C1 state machine vs Stage 0 C-05 naming before Draft A becomes normative — which set is authoritative?
5. Freeze **P-05** fault-vent / limp policy direction: monitored depressurize + allowed droop envelope vs mandatory mechanical catch for MVP fixture?
6. Confirm Lead **F-01 / F-05 / F-08** numbering and publish numbered DFMEA table into SoR `B06_ROOT_PITCH_HARDWARE_SKETCH.md` (box copy still unlabeled bullets)?
7. Normative wording for stub §7: is “pitch locked + encoder valid” required before **any** carrier motion, or only before pressurized strike (S3)?
8. Confidence threshold / “valid head hypothesis” rule — Lead numeric or qualitative spot-check only for S0/S1?
9. SAF-02 E-stop hardware topology ownership and whether Draft A E-stop section is READY to mark OPEN→in-progress after this packet?
10. May Elias expand Draft A/B into a formal `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` under `docs/engineering/` after your disposition, or hold until Michael architecture freeze?

---

### Sources used

| Path | Why |
|---|---|
| `/workspace/astra-previews/ola/start-here/docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` | **Canonical MVP ICD** (sensing stack, twin adapter, acceptance, staging) |
| `/workspace/_pc_sync/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` | Compared; identical content (newline only) |
| `https://myorglab-repos.github.io/astra-previews/ola/start-here/docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.html` | Pages mirror check |
| `/workspace/boxing-trainer/STAGE0_REQUIREMENTS_HAZARD_REGISTER.md` | Hazards H-01…H-15, C-04/C-05, SAF-*, P-05 |
| `/workspace/astra-cli-setup/robotic-punching-bag/STAGE0_REQUIREMENTS_HAZARD_REGISTER.md` | Same + 2026-09-19 reach/pitch amendment |
| `/workspace/boxing-trainer/ENGINEERING_ASSESSMENT_REVIEW_PACKET.md` | C-01/B-06 Critical framing; handheld ≠ E-stop |
| `/workspace/pb-align/revision_c/control_interface.md` | Inhibit/vent state machine; AI independence; sync notes |
| `/workspace/pb-align/revision_c/engineering_handoff.md` | Power-loss limp/depressurize; relief/isolation schematic intent |
| `/workspace/astra-previews/ola/start-here/docs/engineering/B06_ROOT_PITCH_HARDWARE_SKETCH.md` | Pitch unlock, encoder loss, hose pinch DFMEA starters (F-01/F-05/F-08 per Lead map) |
| `/workspace/astra-previews/ola/start-here/docs/engineering/TRACK_B_SYSTEM_ID_PLAN.md` | Overpressure relief + fail-safe vent gate before multi-chamber |
| `/workspace/astra-previews/ola/start-here/START_HERE.html` (+ `/workspace/_pc_sync/START_HERE.html`) | Readiness: safety envelope OPEN; CV→twin OPEN; B-06 DFMEA note |
| `/workspace/talent-desk/boxing-peers/controls-perception-engineer.md` | Role scope / non-ownership of Critical & NEXT_PROMPT |

**ICD comparison note:** Prefer newer/complete — both local ICD copies are the 2026-09-21 MVP; used **`/workspace/astra-previews/ola/start-here/docs/engineering/LIVE_CAMERA_VIRTUAL_TWIN_ICD.md`** as canonical.

**Blocker (partial):** Numbered B-06 **F-01 / F-05 / F-08** table and §7 pitch-locked ICD text claimed on Michael SoR desktop are **not** on the box/Pages B-06 md yet — cited via unlabeled failure-mode bullets + Lead steering labels; Ola should confirm SoR sync.

---

*Elias Controls & Perception desk — draft for Ola disposition only. No NEXT_PROMPT in this packet.*
