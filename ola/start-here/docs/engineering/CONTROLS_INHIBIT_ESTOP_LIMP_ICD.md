# Controls — Inhibit / E-stop / Limp ICD (MVP)

| Field | Value |
|---|---|
| **Title** | Controls Inhibit, E-stop & Limp Interface Control Document |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception) |
| **Disposition** | Ola (Lead Robotics) |
| **Status** | **DRAFT** — expansion of Elias Draft A/B per Ola ACCEPTED-A (2026-09-21). **Not CLOSED.** Critical language remains Lead-owned OPEN or in-progress. |
| **Product** | AI-Powered Boxing Training System |

**Normative for this draft:** Ola ACCEPTED-A answers (1)–(10) from `ELIAS_CONTROLS_PERCEPTION_DRAFT_PACKET.md` disposition header. Critical inhibit policy, READY accept/reject, and OPEN/CLOSED remain **Ola-owned**. Elias drafts interface language only.

---

## 1. Scope / non-goals

### In scope (MVP)
- Deterministic **session enable / inhibit** chain fed by proximity presence, head/human ROI hypothesis, and controls inhibit latch.
- **Physical motion / strike hard interlock** on presence (forever).
- Inhibit sources (OR-combined), limp / fault-vent concepts (P-05), E-stop / fail-safe venting concepts (SAF-02 — **in-progress**, not CLOSED).
- Gate applicability for proximity, contact energy, pinch (incl. B-06 F-08), overpressure, pitch lock (F-01), encoder validity (F-05).
- Valve / timing **concept** interfaces with Lead TBD placeholders (no invented numbers).

### Non-goals
- Full athletic pose CV / multi-joint skeleton / glove class as day-one product requirements.
- Track A prescribed films as strike-impulse or vision proof.
- Invented timings, FPS, force, pressure setpoints, latency budgets, contact-energy limits, or SIL/PL certification claims.
- Closing any Critical defect (B-06, P-05, SAF-02, inhibit policy, etc.).

---

## 2. References

| Ref | Path / ID | Use |
|---|---|---|
| Twin ICD | `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` (Ola start-here engineering) | MVP sensing stack, twin adapter, staging S0–S3 |
| Stage 0 | `STAGE0_REQUIREMENTS_HAZARD_REGISTER.md` | C-04/C-05, P-05, SAF-01…05, H-01…H-15 |
| B-06 SoR | `B06_ROOT_PITCH_HARDWARE_SKETCH.md` (DESKTOP SoR sync) | Numbered DFMEA F-01 / F-05 / F-08 |
| Stub | `ELIAS_CONTROLS_PERCEPTION_ICD_STUB.md` | One-page session enable stub (superseded in detail by this ICD) |
| Packet | `ELIAS_CONTROLS_PERCEPTION_DRAFT_PACKET.md` | Draft A/B + Ola ACCEPTED-A disposition |
| C1 ctrl | `pb-align/revision_c/control_interface.md` | Implementation draft only — reconcile; **drop fixed-shoulder assumptions** |
| C1 handoff | `pb-align/revision_c/engineering_handoff.md` | Power-loss limp / monitored depressurize intent (informative) |

---

## 3. Architecture

```
Presence (ToF/PIR/mat) ──┐
Head ROI (camera) ───────┤──→ Twin adapter → session_enable / overlay / log
Controls inhibit latch ──┘         │
                                   ▼
Deterministic validator + independent limit/fault monitor
                                   │
                    supply inhibit / monitored vent / E-stop path
                                   │
                              Fill / exhaust valves
```

| Principle | Normative intent |
|---|---|
| Deterministic enable chain | Request validator + independent limit/fault monitor drive supply inhibit / monitored vent. Stop path must not wait on AI service. |
| AI advisory only | Planner/AI does not issue valve duty cycles, select pressure limits, or clear inhibit latches (Stage 0 H-14; C1 intent). |
| Presence forever | `user_present == false` (or fail-safe absent) **hard-interlocks physical motion and strike** for all staging. Presence alone is sufficient to deny motion/strike regardless of head hypothesis. |
| Perception staging | S0/S1: twin/logging only. S3 physical arms require presence interlock + `safe_to_actuate` + C-01 + B-06 + safety (Twin ICD). |

---

## 4. State model (product-facing)

**Authoritative product-facing aliases (Stage 0 C-05):**

| C-05 alias | Intent |
|---|---|
| disabled / vented | Supply isolated or fault-vented; no fill |
| enabled guard | Armed / guarded pose; no automatic strike |
| fill / steer | Bounded fill under READY + all interlocks |
| return | Metered return / exhaust trajectory |
| fault | Latched inhibit + validated vent response |

**C1 machine** (`POWER_OFF` → `BOOT_INHIBITED` → `COMMISSIONING_REQUIRED` → `READY` → `ACTIVE` → `FAULT_LATCHED` → `SERVICE_ISOLATED`) is an **implementation draft to reconcile** to C-05 aliases. **Drop fixed-shoulder assumptions** from C1 (`Z=1.360 m` fixed mounts; no pitch/yaw product freeze). N3+ Stage 0 / Twin ICD MVP naming wins for product-facing language until Ola freezes a single set.

Latch rule (informative from C1, retained): AI restart, network reconnect, and pressure recovery **must not** clear `inhibit_latched`. Manual reset required; reset does not start motion.

---

## 5. Session enable vs motion / strike interlock

### 5.1 Session enable (twin / logging / trainer session)

Per Ola ACCEPTED-A (1):

```
session_enable = user_present
               ∧ head_hypothesis_valid
               ∧ ¬ inhibit_latched
```

- `user_present` — proximity authoritative for “someone at the bag.”
- `head_hypothesis_valid` — S0/S1: **qualitative spot-check only** (ACCEPTED-A (8)); no invented confidence/IoU thresholds in this draft.
- `inhibit_latched` — controls inhibit latch (this ICD).

If `¬ user_present` → twin idle / safe; **no arm play toward empty space**.

### 5.2 Physical motion / strike interlock

**Presence alone forever hard-interlocks physical motion and pressurized strike.** Session enable being true is **not** sufficient for S3 actuation.

Additional S3 strike gates (ACCEPTED-A (7)): **pitch locked** and **encoder valid** are required **before pressurized strike (S3)** — **not** before all twin overlay or yaw pedagogy (S0/S1/S2 twin).

Physical strike still gated on: presence + `safe_to_actuate` + C-01 + B-06 + safety (Twin ICD Staging S3). **Critical — Lead-owned OPEN.**

---

## 6. Inhibit sources (OR → inhibit)

Any true source asserts inhibit (motion/fill denied; latch semantics Lead-owned detail — **Critical OPEN**):

| Source | Hook | Notes |
|---|---|---|
| Physical stop / E-stop path | SAF-02 | Independent hardware path; see §9 |
| `user_present == false` or fail-safe absent | Twin ICD; H-01 | Forever hard interlock for motion/strike |
| Stale required sensor / watchdog / comms loss | C1 intent; H-13 | |
| Lost / low-confidence tracking when used for control | H-13 | MVP S0/S1: qualitative; no numeric bar here |
| Over-limit / leak / commissioning incomplete | C1; H-04 | |
| Encoder / limit invalid (yaw; pitch if actuated) | **B-06 F-05** | Inhibit strike — see §10 |
| Pitch not confirmed locked when strike enabled | **B-06 F-01** | Required for pressurized strike (S3) — see §10 |
| Pinch / proximity at pitch hinge trip (modality TBD) | **B-06 F-08**; H-08 | See §10 |
| Corrupted configuration / disallowed trajectory | C1 | |

**Inhibit policy detail: [CRITICAL — OLA-OWNED OPEN].** This ICD does not freeze debounce, priority, or PL/SIL.

---

## 7. Presence sensing

Per Ola ACCEPTED-A (2)–(3):

| Item | Normative draft |
|---|---|
| Preferred modality | **ToF** preferred |
| Backup | **PIR** |
| Optional | Floor **mat** |
| Mech ownership | Mount / mechanical integration |
| Controls ownership | Fail-safe wiring: sensor fault or loss → **`user_present := false` (absent)** |
| Latency | **TBD until bench** — do not invent declared walk-in/out latency in this draft |

Acceptance pointer: Twin ICD walk-in / walk-away / empty-bag / sensor-loss tests; latency remains TBD — Lead.

---

## 8. Limp / P-05 fault vent

Per Ola ACCEPTED-A (5); Stage 0 P-05 remains **OPEN** (Hazard H-03 / H-02):

| Element | Draft direction (not CLOSED) |
|---|---|
| MVP fixture intent | **Monitored depressurize** + **allowed droop** envelope |
| Mechanical catch | Required **before person-facing** use — **not** a day-one fixture mandate |
| Non-policy | Do **not** “open all vents” blindly; depressurized arm may droop rather than auto-return to guard (C1 / handoff intent) |
| Snapback | Metered / validated exhaust (H-02); characterization via Track B before multi-chamber person-facing |

**P-05: [CRITICAL — LEAD-OWNED OPEN].** Acceptance stub: fault injection on guarded fixture reaches defined limp/vent state without uncontrolled snapback or undocumented strike — metrics **TBD — Lead**.

---

## 9. E-stop / SAF-02 (in-progress)

Per Ola ACCEPTED-A (9): Elias Draft A E-stop language → **in-progress expansion** in this ICD. **SAF-02 is not CLOSED.**

| Requirement | Intent |
|---|---|
| Independent path | Hardware motion-enable / stop independent of UI and of CV/AI service availability (SAF-02; H-14; C1) |
| Handheld ≠ E-stop | Stage 0 C-04 / H-15 — portable touchscreen is UX/enable only, **not** safety-rated E-stop |
| Fail-safe presence | Sensor loss → absent (§7) |
| Overpressure | Independent mechanical relief + monitored supply isolation (H-04; SAF-04) — setpoints **TBD** |
| Reset | Manual reset after latch; reset does not start motion |

**SAF-02: [CRITICAL — LEAD-OWNED — OPEN / in-progress].** Topology, performance level, and stop-path timings remain Lead TBD — **no invented numbers**.

Acceptance stub: E-stop from any ACTIVE/READY-equivalent state inhibits supply and executes Lead-approved vent; manual reset required.

---

## 10. Gates table (applicability)

Cite B-06 SoR DFMEA rows **verbatim** for F-01 / F-05 / F-08 (from `B06_ROOT_PITCH_HARDWARE_SKETCH.md` §5):

### 10.1 SoR DFMEA excerpts (normative citations)

| ID | Function | Failure mode | Local effect | System effect | Potential cause | Current prevention (intent) | Detection (intent) | Recommended action | Owner |
|---|---|---|---|---|---|---|---|---|---|
| **F-01** | Hold pitch under gravity + punch reaction | Pitch unlock / free fall | Arm drops | Mis-aim; pinch; user surprise | Detent wear, pin not engaged, actuator brake fail | Hard stops + positive lock / spring detent; Option B pin with flag | Limit switch “locked”; visual pin flag | Specify lock architecture before fab | Mech |
| **F-05** | Yaw / pitch position knowledge | Encoder / limit loss | Wrong attitude | Mis-aimed strike | Cable break, EMI, uncalibrated | Redundant limits; safe-state “fold” | Fault bit → inhibit strike | Control ICD + safe state | Controls |
| **F-08** | User proximity | Pinch at pitch hinge | Soft-tissue injury | Safety incident | Gap < finger; no cover | Padding + gap standard; guards | Risk assessment | Safety gate before pilot | Safety |

### 10.2 Control gates

| Gate | Source | Draft control intent | Applicability | Lead status |
|---|---|---|---|---|
| Proximity / `user_present` | Twin ICD; H-01 | Authoritative “at bag”; AND with head for **session**; alone forever hard-interlocks **motion/strike** | Session + all physical motion/strike | OPEN |
| Contact energy | SAF-01; H-01 | Bound before human trials; instrumented contact on fixture first | Person-facing / S3 | OPEN — **Critical placeholder** |
| Pinch (rotating band) | H-08; SAF-03 | Geometry + carrier enable interlocks + displacement tests | Carrier motion | OPEN |
| Pinch (pitch hinge) | **F-08** (table above); H-08 | Padding/gap/guards; inhibit if pinch sensor/limit trips (**modality TBD**) | Pitch stage / person-adjacent | OPEN — Safety gate before pilot |
| Overpressure | H-04; SAF-04 | Relief + monitored isolation; no pressurized multi-chamber without drafted vent policy | Fill / strike | OPEN |
| Pitch locked | **F-01** (table above) | No **pressurized strike (S3)** unless pitch stage reported locked / within hard stops | **S3 pressurized strike only** — not all twin/yaw pedagogy | **[CRITICAL — LEAD OPEN]** |
| Encoder valid | **F-05** (table above) | Encoder/limit fault → **inhibit strike** | **S3 pressurized strike** (and carrier command when used for strike aim) | **[CRITICAL — LEAD OPEN]** |

B-06 Critical remains **OPEN** until designed, analyzed, and prototype-qualified (SoR B-06 status). This ICD does not close F-01/F-05/F-08.

---

## 11. Valve / timing interfaces (concept)

No invented duty cycles, rates, pressures, or stop times.

| Interface | Intent | Placeholder |
|---|---|---|
| Per-chamber fill | Bounded fill under READY-equivalent + all interlocks true | Duty / rate limits **TBD — Lead** |
| Controlled exhaust | Metered return; avoid snapback (H-02) | Exhaust profile **TBD — Lead / Track B** |
| Fault vent / dump | Monitored depressurization; not blind full-open (H-03; P-05) | Vent policy **[CRITICAL — LEAD-OWNED P-05 OPEN]** |
| Master supply shutoff | Isolation on inhibit / E-stop / fault | Hardware path **[CRITICAL — LEAD-OWNED SAF-02 in-progress]** |
| Mechanical relief | Independent of fill-valve isolation (H-04) | Setpoint **TBD** before pressurized FP |
| Pitch moving / unlock | No chamber fill while pitch unlocking/moving (B-06 §7 intent) | Lock/encoder bits **TBD — Lead / Mech** |

---

## 12. Acceptance language stubs

Controls stubs (pass criteria **Lead-owned**; latency **TBD until bench**):

1. Inhibit asserts on each listed source; fill valves commanded closed / supply inhibited.
2. E-stop path independent of handheld UI and of CV/AI service availability; handheld ≠ E-stop.
3. Limp/vent (P-05 direction): monitored depressurize + allowed droop on MVP fixture; mechanical catch before person-facing — no uncontrolled snapback per Lead characterization.
4. `user_present` false or fail-safe absent → twin idle; no physical motion/strike.
5. Encoder invalid (**F-05**) or pitch unlock (**F-01**) → **strike inhibit** for pressurized S3 — wording of pass bar Lead-owned.
6. Session enable only when presence ∧ valid head hypothesis ∧ ¬inhibit_latched; S0/S1 head validity = qualitative spot-check only.

**MVP AT outline pointer:** Elias Draft B (`ELIAS_CONTROLS_PERCEPTION_DRAFT_PACKET.md` § Draft B) — AT-P1…P4, AT-H1/H2, AT-F1/F2, AT-S1, AT-ST1/ST3. Twin ICD acceptance tests remain normative for sensing; declared latency stays **TBD**.

---

## 13. Open items for Ola (residual after ACCEPTED-A)

Only residuals — ACCEPTED-A (1)–(10) are baked above and are **not** re-asked:

1. **Inhibit latch semantics** — debounce, priority among OR sources, clear/reset procedure detail (**Critical OPEN**).
2. **SAF-02 hardware topology** — stop-circuit architecture, independence evidence plan (in-progress; not CLOSED).
3. **P-05 droop envelope** — how “allowed droop” is documented for MVP fixture vs person-facing catch (**Critical OPEN**).
4. **C-05 ↔ C1 naming freeze** — when to collapse aliases into one normative state set (direction given: C-05 product-facing; C1 reconcile).
5. **F-08 pinch modality** — sensor vs geometry-only for pitch hinge before pilot.
6. **Pitch Option A vs B** (B-06) — when lock/encoder bits become wiring-normative for S3.
7. **Contact-energy (SAF-01) / overpressure setpoints** — remain OPEN; out of numeric scope here.

---

## 14. Ownership

| Role | Owns |
|---|---|
| **Ola (Lead Robotics)** | Critical OPEN/CLOSED; READY accept/reject; inhibit policy; SAF-02 / P-05 disposition; B-06 Critical; architecture freeze coordination |
| **Elias (Controls & Perception)** | This draft ICD language only; Draft A/B expansion; twin adapter signal recommendations |
| **Mech** | Presence mount; B-06 pitch lock architecture (F-01 prevention); pinch geometry (F-08) |
| **Controls (desk)** | Fail-safe→absent presence wiring; encoder fault → inhibit (F-05 detection path); ICD maintenance under Ola disposition |
| **Safety** | F-08 risk assessment / pilot gate; SAF-* closure evidence |

**This file is draft → Ola disposition.** It expands Elias Draft A/B per ACCEPTED-A (10). It does **not** close Critical defects. Status remains **DRAFT**, not CLOSED.

---

*Elias Controls & Perception desk — DRAFT 2026-09-21 for Ola disposition. No invented timings/FPS/force/pressure/latency numbers.*
