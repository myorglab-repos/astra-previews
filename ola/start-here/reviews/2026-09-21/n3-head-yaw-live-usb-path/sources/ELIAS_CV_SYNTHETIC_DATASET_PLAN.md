> **Ola integrate 2026-09-21: ACCEPTED-A (digital CV / HIL paper gate).** Completes Soft+CV digital Track B prep pack with Ismael ACCEPTED-A. Does not authorize physical actuation or claim gym CV accuracy.

# Elias — CV synthetic dataset plan (S0 twin train/test)

| Field | Value |
|---|---|
| **Title** | CV synthetic / real-capture dataset plan for S0 twin train/test (MVP sensing) |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | Ola (Lead Robotics) integrate |
| **Authority** | Michael authorized execute without further approvals — **PAPER ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | DRAFT — aligned to ACCEPTED-A ICDs; Critical hardware / inhibit policy / declared latency remain **Lead-owned OPEN** |
| **Product** | AI-Powered Boxing Training System |
| **Michael push** | Maximize **digital V&V** of session-enable fusion, schemas, and synthetic coverage **before** physical camera+presence build |

**Normative sources (read order):**
- `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` (Ola start-here engineering) — MVP sensing, twin adapter, S0–S3 staging, walk-in/out/empty-bag acceptance language
- `docs/engineering/CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` — session_enable equation; presence forever hard-interlock
- `docs/engineering/ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` — signal names, fail-safes, staging applicability
- `ELIAS_CONTROLS_PERCEPTION_ICD_STUB.md` / `ELIAS_CONTROLS_PERCEPTION_DRAFT_PACKET.md` Draft B — AT outline (AT-P*, AT-H*, AT-F*, AT-S1)
- `docs/engineering/ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` — **presence modality context only** (ToF preferred / PIR backup / mat optional); no SKU freeze here

**ACCEPTED-A norms baked (not re-asked):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
- Presence alone forever hard-interlocks **physical motion / pressurized strike**.
- S0/S1 head validity = **qualitative spot-check only** (ACCEPTED-A (8)).
- Latency = **TBD until bench** — do not invent declared walk-in/out latency.
- Presence modality: **ToF preferred / PIR backup / mat optional**.
- MVP only: **head/human ROI + near-bag presence** — **not** full pose / glove athletics CV.

**No invented numbers** in this plan (no FPS, IoU, accuracy %, confidence floors, latency budgets). Where ICDs leave TBD / Lead-owned, this plan says so.

---

## 1. Doc control

| Item | Value |
|---|---|
| Status | **DRAFT** |
| Integrate path | Elias → Ola (Lead Robotics) |
| Date | **2026-09-21** (America/New_York) |
| Scope class | Paper / digital V&V planning only |
| PO | **None** |
| NEXT_PROMPT | **None** — Ola owns |

Identical mirrors: `docs/engineering/` and `sor_sync/`.

---

## 2. Scope / non-goals

### In scope (MVP)
- Plan for **S0** offline record of **head/human ROI** clips + **near-bag presence** timelines + twin-adapter flags for train/test of light perception and **session_enable** fusion logic.
- Conceptual synthetic generation approaches (procedural / composited head ROI, empty-bag negatives, lighting variants) — **not** claiming a specific tool chain or corpus size.
- Real-capture protocol **stubs** (protected camera, gym-like lighting, walk-in/out).
- Episode / clip **schemas** aligned to twin-adapter signals.
- Label taxonomy for present/absent, head valid/invalid (**qualitative**), sync quality.
- Acceptance language = **qualitative** per ACCEPTED-A (8) and Twin ICD walk-in / walk-away / empty-bag wording — **no invented numeric bars**.
- Privacy defaults (local; recording off unless enabled).
- Mapping of twin-adapter signals → log fields for digital V&V and later training join keys.
- Explicit split: what **can** be claimed digitally vs what **must** wait for camera+ToF/mat bench.

### Non-goals
- Full-body multi-joint pose, glove tracking, punch-type classification as day-one blockers (Twin ICD non-goals).
- Using **Track A** prescribed Blender films as **proof of real vision** (Twin ICD Track A demarcation).
- Invented FPS, IoU, mAP, confidence thresholds, declared latency, PL/SIL, or “SOTA CV” research program claims.
- Closing Critical: inhibit latch policy, SAF-02, P-05, B-06 F-01/F-05/F-08, contact-energy SAF-01.
- Authorizing physical actuation, POs, or NEXT_PROMPT.
- Cloud training / cloud corpus claims unless Lead explicitly says so.
- Freezing presence SKU from the supplier scout (modality class only).

---

## 3. Dataset plan for S0 twin train/test

### 3.1 Synthetic generation approaches (conceptual)

Purpose: maximize **digital** coverage of positives / negatives / lighting stress **before** hardware so fusion logic, schemas, and qualitative spot-check harnesses can be exercised in sim / offline replay.

| Approach | Intent | Notes (non-claims) |
|---|---|---|
| Procedural / composited **head ROI** positives | Place head/upper-body crops into bag-facing ROI frames with varied scale, offset, partial occlusion | Conceptual — no claimed generator, no claimed count, no claimed accuracy bar |
| **Empty-bag negatives** | Bag + background with **no** person in ROI; exercise “no valid head hypothesis” and idle twin | Aligns Twin ICD empty-bag / AT-H2 language |
| Lighting variants | Gym-like bright / dim / side / backlight / flicker composites | Stress qualitative detectability; **not** a declared lux or FPS bar |
| Presence timeline synthesis | Pair frames with synthetic `user_present` true/false and optional `presence_sensor_fault` | Supports AT-F1/F2 fusion cases digitally |
| Inhibit / sync fault inject | Overlay `inhibit_latched`, stale `t_sync` quality flags in episode metadata | Digital V&V of session_enable AND-chain and AT-S1 quality flag — **not** hardware proof |

**Explicit:** Synthetic data supports **logic, schema, and coverage checks**. It does **not** prove real-gym false-presence rates, industrial sensor fail-safe wiring, or declared latency.

### 3.2 Real-capture protocol stubs

Stubs only — pass bars Lead-owned; latency **TBD until bench**.

| Stub | Protocol intent | ICD / AT pointer |
|---|---|---|
| Protected camera | Head-height ROI mount / cover (Mech); capture head/human crop only | Twin ICD Architecture; Draft B B.1 |
| Gym-like lighting | Record under normal gym lighting conditions for empty-bag and walk cases | Twin ICD acceptance: empty bag, no false presence under normal gym lighting |
| Walk-in | Subject enters work envelope → expect `user_present` true within **declared latency TBD — Lead** | Twin ICD; AT-P1 |
| Walk-out | Subject leaves → `user_present` false; twin idle / safe | Twin ICD; AT-P2 |
| Empty bag | No subject; no false presence under normal gym lighting | Twin ICD; AT-P3 |
| Sensor loss | Power/signal loss on presence channel → fail-safe **absent** | AT-P4; ACCEPTED-A fail-safe |
| Head spot-check | When present, head/human hypothesis asserted by **qualitative** spot-check (not Olympic pose) | Twin ICD; AT-H1; ACCEPTED-A (8) |
| Empty ROI | No person → no valid head hypothesis; session not enabled | AT-H2 |
| Recording enable | Capture only when recording explicitly enabled (privacy) | §3.6 |

Presence modality on bench: **ToF preferred / PIR backup / mat optional** (ACCEPTED-A (2); scout for class context only).

### 3.3 Schemas for clips / episodes (aligned to twin adapter)

**Episode** = contiguous capture window with shared `episode_id` and timebase. **Clip** = media segment within an episode (head-ROI video). **Sample / frame row** = time-aligned signal row for fusion / training join.

#### Episode metadata (informative schema stub)

| Field | Type | Notes |
|---|---|---|
| `episode_id` | string | Primary join key |
| `t_start` / `t_end` | timestamp | Capture window |
| `capture_site` | string | Fixture / gym stub label |
| `recording_enabled` | bool | Must be true for media; default false in product UX intent |
| `privacy_mode` | enum | `local_default` \| … — cloud training **off** unless Lead says |
| `modality_notes` | string | e.g. ToF / PIR / mat used on that capture — TBD |
| `schema_rev` | string | Ties to this draft rev |

#### Per-sample / timeline row (join to twin adapter)

| Field | Type | Twin-adapter signal | Fail-safe / quality |
|---|---|---|---|
| `episode_id` | string | join key | — |
| `t_sync` | timestamp + sync quality flag | `t_sync` | Stale / unknown → quality flag; inhibit **time-critical** fusion use; S0/S1 logging may continue (AT-S1) |
| `user_present` | bool | `user_present` | Fault / loss → **false (absent)** |
| `presence_sensor_fault` | bool | `presence_sensor_fault` | Forces absent |
| `head_hypothesis.bbox` | struct (x,y,w,h or equiv.) | `head_hypothesis` | Absent / invalid → no session |
| `head_hypothesis.confidence` | float or null | `head_hypothesis` | **Logged raw if available**; **validity rule TBD — Lead**; **no invented floor in this plan** |
| `head_hypothesis_valid` | bool | derived | S0/S1 = **qualitative spot-check** rule until Lead freezes |
| `inhibit_latched` | bool | `inhibit_latched` | Manual reset only; AI must not clear |
| `session_enable` | bool | `session_enable` | AND of presence ∧ valid head ∧ ¬inhibit |
| `twin_overlay.presence_lamp` | state | out | Prefer absent/idle on sensor loss |
| `twin_overlay.head_marker` | state | out | Hide/flag when invalid |
| `quality_flags` | set | sync stale, sensor loss, recording off, etc. | Required for AT-S1 / privacy |
| `media_uri` / `clip_id` | string | `log_episode` | Local path default |

Snowflake: metadata **later** — not inventing a corpus today (Twin ICD).

### 3.4 Label taxonomy

| Label | Values | Use |
|---|---|---|
| Presence | `present` / `absent` | Aligns `user_present`; fault → treat as absent |
| Head validity (S0/S1) | `valid` / `invalid` / `unchecked` | **Qualitative** spot-check only — ACCEPTED-A (8); not IoU/confidence bars |
| Sync quality | `ok` / `stale` / `unknown` | AT-S1; time-critical fusion gate |
| Session outcome | `enabled` / `inhibited` | Derived; for fusion unit tests |
| Scene class (informative) | `walk_in` / `walk_out` / `empty_bag` / `person_in_roi` / `empty_roi` / `fault_inject` | Coverage tags for digital + bench suites |
| Non-labels (MVP) | — | **Do not** require multi-joint skeleton, glove class, or punch-type as day-one blockers |

### 3.5 Acceptance = qualitative per ACCEPTED-A (8)

Cite Twin ICD / Draft B language **without inventing numbers**:

| Case | Pass language (no fake metrics) |
|---|---|
| Walk-in | `user_present` → true within **declared latency TBD — Lead** (Twin ICD; AT-P1) |
| Walk-away | `user_present` → false; twin idle / safe (AT-P2) |
| Empty bag | No false presence under **normal gym lighting** (AT-P3) |
| Sensor loss | Fail-safe **absent**; session inhibited (AT-P4) |
| Head when present | Head/human hypothesis asserted by **qualitative spot-check**; does **not** need Olympic pose accuracy (Twin ICD; AT-H1; ACCEPTED-A (8)) |
| Empty ROI | No valid head hypothesis; session not enabled (AT-H2) |
| Fusion | `session_enable` only if presence ∧ valid head ∧ ¬`inhibit_latched` (ACCEPTED-A (1); AT-F1) |
| Split cases | Presence without head / head without presence → session remains inhibited (AT-F2) |
| Sync | Unknown / stale sync → quality flag; invalidate time-critical fusion; S0/S1 logging allowed with flag (AT-S1) |

**Confidence / IoU / FPS / latency numeric bars:** **TBD — Lead**. Not set in this draft.

### 3.6 Privacy

| Rule | Intent |
|---|---|
| Local default | Processing / storage default **local** |
| Recording off unless enabled | Product UX: recording **off** unless explicitly enabled (C1 / Draft B privacy note) |
| No cloud training claims | Do **not** claim cloud training or cloud corpus unless Lead says |
| Dataset access | Training clips treated as sensitive; Lead / Safety / privacy policy govern sharing |
| Synthetic preference for early V&V | Prefer synthetic + fixture captures before broad gym recording |

---

## 4. Logging twin-adapter signals for model training

Map each ACCEPTED-A / twin-adapter table signal used for MVP session sensing to **log field**, **episode join key**, and **fail-safe value**. Full table authority: `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md`.

| Signal | Log field(s) | Episode join key | Fail-safe / default when bad |
|---|---|---|---|
| `t_sync` | `t_sync`, `sync_quality` | `episode_id` + `t_sync` | Stale/unknown → quality flag; inhibit time-critical fusion; logging may continue |
| `user_present` | `user_present` | same | Fault/loss → **`false` (absent)** |
| `presence_sensor_fault` | `presence_sensor_fault` | same | True → force `user_present` false |
| `head_hypothesis` | `head_hypothesis.bbox`, `.confidence` (optional `.facing` later) | same | Invalid/absent → do not enable session; **no invented confidence floor** |
| `head_hypothesis_valid` | `head_hypothesis_valid` | same | False if qualitative rule fails / unchecked; rule **TBD — Lead** for freeze |
| `inhibit_latched` | `inhibit_latched` | same | Remains latched until **manual reset**; AI/network/pressure recovery must not clear |
| `session_enable` | `session_enable` (derived, logged) | same | False if any AND term fails; `¬ user_present` → idle/safe |
| `twin_overlay.presence_lamp` | `twin_overlay.presence_lamp` | same | Prefer show absent/idle on sensor loss |
| `twin_overlay.head_marker` | `twin_overlay.head_marker` | same | Hide/flag when hypothesis invalid |
| `log_episode` | `clip_id` / `media_uri` + flag bundle | `episode_id` | Quality flag on stale sync / sensor loss; no media if recording off |

**S3-only / strike-path signals** (`e_stop_asserted`, `pitch_lock_engaged`, `yaw_encoder_valid`, `pitch_encoder_valid`, `safe_to_actuate`, `supply_inhibit`, `pinch_trip`, `overpressure_trip`, etc.) may be logged when available for controls V&V but are **out of scope** as MVP CV dataset labels. They do **not** replace presence hard-interlock. See twin-adapter table for staging applicability.

**Training join recipe (informative):** join clip frames to timeline rows on `(episode_id, t_sync)` within Lead-declared sync tolerance (**TBD**); drop or flag rows with `sync_quality != ok` for any time-critical experiment.

---

## 5. Digital V&V claims vs physical bench needs

Michael push: claim what digital can honestly prove; leave the rest for camera+presence bench.

### 5.1 What CAN be claimed digitally (pre-hardware / sim / offline)

| Claim class | Examples |
|---|---|
| **session_enable fusion logic** | Truth-table unit tests: present+valid head+¬inhibit → enable; any term fail → inhibit (see companion HIL stub) |
| **Inhibit latch behavior in sim** | Latch stays set across AI restart / network reconnect / pressure recovery inject; clear only on simulated manual reset; reset does not start motion |
| **Schema completeness** | Episode/clip/timeline fields cover twin-adapter MVP inputs/outputs; join keys stable; quality flags present |
| **Synthetic positive/negative coverage checks** | Empty-bag / empty-ROI / walk tags / fault-inject tags present in suite; AT-F1/F2 case coverage in replay |
| **Overlay idle rules** | `¬ user_present` → idle/safe overlay path exercised without claiming real sensor timing |
| **Privacy flags** | Recording-off episodes produce no media URI; local_default documented |

Digital claims are **logic / schema / coverage** claims — **not** real-world sensing performance claims.

### 5.2 What MUST wait for camera + ToF/mat bench

| Must wait | Why |
|---|---|
| **Declared latency** (walk-in/out) | ACCEPTED-A (3) / Twin ICD — **TBD until bench**; Lead-owned |
| **False presence in real gym lighting** | Empty-bag AT-P3 needs real optical/EMI/environment; synthetic lighting variants are stress aids only |
| **Industrial sensor fail-safe wiring** | Open-wire / power-loss → absent must be proven on real ToF/PIR/mat + Controls wiring |
| **S3 gates** | Physical arms only with presence interlock + `safe_to_actuate` + C-01 + B-06 + safety — out of S0 dataset scope |
| **Head validity numeric freeze** | If Lead later sets confidence/IoU bars, that is post-spot-check; S0/S1 remain qualitative until Lead says otherwise |
| **SAF-02 / P-05 / inhibit policy closure** | Critical OPEN — Lead; not dataset-owned |

Companion one-pager: `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md` — digital HIL for presence + head + inhibit → `session_enable` (does **not** authorize physical actuation).

---

## 6. Open questions for Ola (short)

Residuals only — ACCEPTED-A norms above are **not** re-asked:

1. **Episode schema freeze** — accept §3.3 field names as normative for S0 logging, or rename before first fixture capture?
2. **Qualitative spot-check procedure** — who signs AT-H1/H2 spot-check (CV desk vs Controls vs Lead) before any numeric validity rule?
3. **Synthetic toolchain** — may Elias paper a *recommended* (still non-normative) generator path later, or keep strictly conceptual until Lead picks?
4. **Fixture vs gym recording gate** — when is first real-capture allowed relative to privacy + Mech protected-camera mount?
5. **Snowflake metadata** — earliest useful episode fields for later ingest (still no corpus invent today)?
6. **Companion HIL stub** — treat `ELIAS_DIGITAL_HIL_SESSION_ENABLE_STUB.md` as normative digital AT harness outline under this plan?

---

## 7. Ownership / commercial controls

| Role | Owns |
|---|---|
| **Ola (Lead Robotics)** | Integrate / disposition; Critical OPEN/CLOSED; declared latency; validity-rule freeze; READY; **NEXT_PROMPT** |
| **Elias (Controls & Perception)** | This draft plan language only; twin-adapter log mapping; digital V&V outline |
| **Mech** | Protected camera mount/cover; presence sensor mechanical integration |
| **Controls** | Fail-safe → absent wiring; inhibit latch logging hooks |
| **CV→twin / specialist** | Light head/human ROI perception (when Stephen-gated hire / bot desk paper) |
| **Safety / privacy** | Recording policy; person-facing gates |

| Control | Rule |
|---|---|
| PO | **NONE** from this desk |
| NEXT_PROMPT | **NONE** in this draft — Ola owns |
| Critical hardware | Remains **OPEN** |
| Numeric bars | **No invented FPS / accuracy / IoU / latency / confidence floors** |

---

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate. Identical mirror: `sor_sync/ELIAS_CV_SYNTHETIC_DATASET_PLAN.md`. PAPER ONLY. No NEXT_PROMPT. No PO.*
