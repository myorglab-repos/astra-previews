# Twin-adapter signal table (MVP) — Elias draft

| Field | Value |
|---|---|
| **Title** | Twin-adapter signal table (presence / head / inhibit → session enable) |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | Ola (Lead Robotics) integrate |
| **Authority** | Michael authorized execute without further approvals — **PAPER + SUPPLIER SCOUT ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | DRAFT — aligned to ACCEPTED-A ICDs; Critical hardware / inhibit policy remain **Lead-owned OPEN** |
| **Product** | AI-Powered Boxing Training System |

**Normative sources (read order):**
- `docs/engineering/CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` (also `sor_sync/` twin)
- `ELIAS_CONTROLS_PERCEPTION_ICD_STUB.md`
- `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` (Ola start-here engineering)
- `sor_sync/B06_ROOT_PITCH_HARDWARE_SKETCH.md` (F-01 / F-05 / F-08)

**Session enable (ACCEPTED-A (1)):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
Presence alone forever hard-interlocks **physical motion / pressurized strike**. Session enable true is **not** sufficient for S3 actuation.

**No invented numbers** in this table (no FPS, IoU, confidence bars, latencies, PL/SIL). Where ICDs leave TBD / Lead-owned, Fail-safe and Notes say so.

**Assumptions / TBD (Michael standing rule):** Camera detector class, FOV, presence thresholds, yaw gain/mapping, confidence cutoffs, and sync tolerances are **ASSUMPTION** or **TBD — Lead** as tagged in rows below and in `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` § Assumptions. **No quiet accuracy claims.**


---

## 1. Signal table

| Signal name | Direction | Type | Source | Consumer | Fail-safe | Staging applicability (S0/S1 session vs S3 strike) | BOM relevance note |
|---|---|---|---|---|---|---|---|
| `t_sync` | in | timestamp / sync quality flag | Capture clock / controller timebase (Twin ICD) | Twin adapter; episode logger; fusion quality gate | Stale / unknown sync → inhibit **time-critical** fusion use; S0/S1 logging may continue with quality flag (ICD stub §5; Draft B AT-S1); sync tolerance **TBD — Lead** (no invented ms) | **S0/S1:** logging + live overlay quality. **S3:** required for any time-critical fusion used toward actuation gates — bar **TBD — Lead** | Soft: clock / capture stack; not a discrete sensor SKU |
| `user_present` | in | bool | Near-bag presence (ToF preferred; PIR backup; mat optional) — Mech mount, Controls wiring (ACCEPTED-A (2)); trip thresholds **TBD — Lead** | Twin adapter; session_enable; motion/strike hard interlock | Sensor fault / loss / power loss → **`user_present := false` (absent)** | **S0/S1:** authoritative “at bag” for session AND. **All stages:** alone forever hard-interlocks physical motion/strike | **BOM:** industrial or MVP ToF class (+ optional PIR / mat) — see supplier scout |
| `head_hypothesis` | in | struct `{ bbox, confidence }` (+ optional facing later) | Protected camera head/human ROI CV (Twin ICD); detector class **ASSUMPTION** (MediaPipe-class / OpenCV fallback) — FOV **TBD — Lead** | Twin adapter; `head_hypothesis_valid`; overlays; logs | Invalid / absent hypothesis → session not enabled; confidence cutoff **TBD — Lead** (no invented floor) | **S0/S1:** qualitative spot-check only (ACCEPTED-A (8)). **S3:** still advisory for CV; does **not** replace presence or hardware interlocks | **BOM:** camera mount / cover (Mech); CV compute path — not in sensing BOM scout |
| `head_hypothesis_valid` | derived in | bool | Twin adapter / light perception validity rule | `session_enable` AND | Validity rule **TBD — Lead**; MVP = qualitative spot-check | **S0/S1 session.** Not a standalone S3 strike gate | Soft / config; no SKU |
| `head_centroid_x` | derived in | normalized float (**TBD — Lead** convention) or null | From `head_hypothesis` bbox horizontal centroid | Twin adapter; `yaw_cmd` map | Null / invalid when hypothesis invalid | **S0/S1:** aim cue for twin yaw. **S3:** advisory toward carrier aim when used — does not replace presence or F-05 | Soft; no SKU |
| `yaw_cmd` | out | angle command (units / range / gain **TBD — Lead** — **no invented gain**) or null | Twin adapter map(`head_centroid_x`) when `yaw_cmd_enable` (**ASSUMPTION:** linear map until Lead freezes) | N3 Blender / CAD twin carrier yaw joint; later hardware yaw language under Lead READY | When enable false → **hold-last or zero** (idle policy TBD — Lead); E-stop/absent prefer zero / home-idle | **S0/S1/S2 digital twin / pedagogy.** Hardware yaw only with presence + inhibit policy + Lead READY — **not authorized by paper alone**. F-01 not required for digital twin yaw; F-05 applies when yaw used toward strike aim | Soft command; hardware rotor / encoder BOM later (F-05 scout) |
| `yaw_cmd_enable` | derived out | bool | `user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched ∧ ¬ e_stop_asserted` | Gates whether `yaw_cmd` is passed to twin | False → no yaw chase | **Digital twin path.** Necessary for chase; **not** sufficient for physical actuation | Soft |
| `inhibit_latched` | in | bool (latch) | Controls inhibit OR-bus (E-stop, faults, F-01/F-05, etc.) — ICD §6 | Twin adapter; `session_enable`; supply inhibit path | Latch clears only on **manual reset**; AI restart / network / pressure recovery must **not** clear (ICD §4). Reset does not start motion | **S0/S1:** blocks session_enable. **S3:** blocks fill / strike with supply inhibit | Soft latch + **BOM:** E-stop hardware class, limit/encoder inputs feeding OR sources |
| `session_enable` | out | bool | Twin adapter combinational intent | Trainer session / twin logging enable; UX | False if any AND term fails; if `¬ user_present` → idle/safe (no arm play toward empty space) | **S0/S1 primary.** Necessary but **not sufficient** for S3 physical strike | Soft output; drives logging/UI — no SKU |
| `twin_overlay.presence_lamp` | out | display / lamp state | Twin adapter from `user_present` | Blender twin / live overlay | Prefer show **absent** / idle on sensor loss | **S0/S1.** Pedagogy overlays OK without S3 gates | Soft / UI |
| `twin_overlay.head_marker` | out | display / marker from bbox | Twin adapter from `head_hypothesis` | Blender twin / live overlay | Hide or flag invalid when hypothesis invalid | **S0/S1.** Not required for S3 strike enable | Soft / UI |
| `log_episode` | out | clip + flags (`user_present` timeline, head hyp, `t_sync`, twin state, quality flags) | Twin adapter + capture | Dataset / later Snowflake metadata | Quality flag on stale sync / sensor loss; privacy: recording off unless explicitly enabled (informative) | **S0** offline record; **S1** live+log. **S3** may log but strike gated elsewhere | Soft / storage |
| `e_stop_asserted` | in | bool (hardware path) | Industrial E-stop button/station → safety / controls stop circuit (**SAF-02 in-progress**) | Inhibit OR; supply shutoff / monitored vent path | Assert → inhibit + Lead-approved vent; **handheld UI ≠ E-stop** (C-04 / H-15) | All stages once hardware present; **normative for person-adjacent / S3**. Independent of CV/AI availability | **BOM:** industrial E-stop operator + contact blocks / station class |
| `pitch_lock_engaged` | in | bool (pin/flag / limit) | Option B pitch pin + limit switch / visual flag (B-06 **F-01** detection intent) | Strike inhibit gate; pneumatics “no fill while unlock” | False / unknown → **inhibit pressurized strike (S3)**; do not invent debounce | **Not required for S0/S1 twin/yaw pedagogy.** **Required before pressurized strike (S3)** (ACCEPTED-A (7)) | **BOM:** limit/pin switch class for Option B lock |
| `yaw_encoder_valid` | in | bool (fault bit inverse) | Yaw encoder / limit channel (B-06 **F-05**) | Strike inhibit; carrier aim when used for strike | Encoder/limit loss → fault bit → **inhibit strike** | **S3 pressurized strike** (and carrier command when used for strike aim). Twin pedagogy may proceed without freeze | **BOM:** encoder + optional redundant limit class |
| `pitch_encoder_valid` | in | bool | Pitch position sense if Option A actuated (B-06); Option B may be discrete preset ID only | Strike / fill inhibit when pitch attitude unknown | Invalid → inhibit strike / no fill while moving unlock (ICD §11) | Option A path; **S3**. Option B MVP lean uses `pitch_lock_engaged` + preset ID | **BOM:** only if Option A chosen — TBD Lead/Mech |
| `safe_to_actuate` | in | bool (Lead / Safety) | Aggregated safety + C-01 + B-06 readiness (Twin ICD S3) | Physical arm enable | False → no physical strike | **S3 only.** Critical OPEN — Lead | Soft / safety stack; not a single SKU |
| `supply_inhibit` | out / internal | bool / hardware coil | Controls validator + inhibit OR + E-stop | Fill valves / master supply shutoff | Fail toward **isolated / inhibited** — topology **SAF-02 Lead TBD** | Armed once pneumatics present; **S3** critical | **BOM:** valves / shutoff (Pneum — out of this scout’s sensing focus); E-stop feeds this |
| `presence_sensor_fault` | in | bool | Presence channel diagnostics / watchdog | Forces `user_present` false; may set inhibit source | Fault → absent (normative) | All stages using presence | Wiring / diagnostics; same presence BOM |
| `pinch_trip` | in | bool (modality TBD) | Pitch-hinge pinch / proximity (**F-08** / H-08) — sensor vs geometry-only **OPEN** | Inhibit if sensor path chosen | Trip → inhibit / stop per Safety | Person-adjacent / pitch stage; pilot gate | **BOM TBD** if sensor modality chosen; else geometry/guards (Mech/Safety) |
| `overpressure_trip` | in | bool | Independent relief monitor / pressure trip (H-04; SAF-04) | Inhibit + isolation | Trip → isolate; setpoints **TBD — Lead** | Fill / strike paths | **BOM:** Track B pressure transducer class (later) + relief (Pneum) |
| `comms_watchdog_ok` | in | bool | Required sensor / controller heartbeat | Inhibit OR if false | Loss → inhibit (ICD §6) | When control path live | Soft / network |
| `commissioning_complete` | in | bool | Controls commissioning gate (C1 reconcile) | Inhibit OR if incomplete | Incomplete → inhibit | Pre-READY | Soft / process |

---

## 2. Combinational notes (informative until Ola freezes)

| Rule | Intent |
|---|---|
| Session | `session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched` |
| Digital yaw chase | `yaw_cmd_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched ∧ ¬ e_stop_asserted`; false → hold-last/zero (Lead idle policy); **does not authorize physical actuation** |
| Idle | `¬ user_present` → twin idle / safe; no arm play toward empty space |
| Motion/strike forever | `¬ user_present` **or** fail-safe absent → deny physical motion / pressurized strike regardless of head hypothesis |
| S3 strike extras | `pitch_lock_engaged` ∧ `yaw_encoder_valid` (and Lead `safe_to_actuate` + C-01 + B-06 + safety) **before** pressurized strike — **not** before all twin/yaw pedagogy |
| AI | Planner/AI does not clear `inhibit_latched`, issue valve duty, or select pressure limits |

---

## 3. BOM hooks (pointer)

Discrete sensing / safety SKUs that feed this table are scouted in:

`docs/engineering/ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`  
(mirror: `sor_sync/ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`)

| Signal / gate | Scout category |
|---|---|
| `user_present` | ToF presence; PIR backup; optional presence mat |
| `e_stop_asserted` | Industrial E-stop hardware class (handheld ≠ E-stop) |
| `pitch_lock_engaged` | Limit/pin switches Option B |
| `yaw_encoder_valid` | Encoder / limit class for yaw |
| `overpressure_trip` / Track B | Basic pressure transducers class (later) |

---

## 4. Explicit non-claims

- No invented confidence, IoU, FPS, latency, force, pressure, or PL/SIL numbers.
- Does not close Critical: inhibit policy, SAF-02, P-05, B-06 F-01/F-05/F-08, contact-energy SAF-01.
- No PO authority; no NEXT_PROMPT in this draft.
- Head→yaw Blender path: `ELIAS_HEAD_TRACK_YAW_BLENDER_PATH.md` (also `sor_sync/`).

---

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate. Mirror also at `sor_sync/ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md`.*
