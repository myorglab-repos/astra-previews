# Presence hardware path scout — near-bag `user_present` (fail-safe absent)

| Field | Value |
|---|---|
| **Title** | Presence hardware path scout — near-bag `user_present` (ToF preferred / PIR backup / ultrasonic class / mat optional) |
| **Rev** | DRAFT 2026-09-21 |
| **Author desk** | Elias (Controls & Perception under Ola) |
| **Disposition** | Ola (Lead Robotics) integrate |
| **Authority** | Michael execute — **PAPER ONLY**; **NO POs**; **NO NEXT_PROMPT** |
| **Status** | DRAFT — path/decision deepen of ACCEPTED-A presence language; **does not replace** `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`; Critical hardware remains **OPEN** |
| **Product** | AI-Powered Boxing Training System |

**Normative sources (read order):**
- `LIVE_CAMERA_VIRTUAL_TWIN_ICD.md` — near-bag presence as MVP on-switch; walk-in / walk-away / empty-bag acceptance intent
- `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md` — ACCEPTED-A (2)–(3): ToF preferred, PIR backup, mat optional; Controls fail-safe → absent; latency **TBD until bench**
- `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` — `user_present`, `presence_sensor_fault`; presence forever hard-interlocks physical motion/strike
- `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` — already-scouted SKUs (VL53L1X bench, Banner Q4X industrial, Adafruit PIR, Tapeswitch mat). **This paper points; it does not duplicate or freeze that BOM.**

**Session enable (ACCEPTED-A (1) — not re-asked):**
```
session_enable = user_present ∧ head_hypothesis_valid ∧ ¬ inhibit_latched
```
Presence alone forever hard-interlocks **physical motion / pressurized strike**. Session enable true is **not** sufficient for S3 actuation. This paper does **not** authorize physical actuation from presence or from perception.

**No invented numbers.** No latency, false-positive rate, FPS, accuracy, IoU, force, or PL/SIL bars. Where a prior appears it is tagged **ASSUMPTION** or **TBD — Lead** (Michael standing rule).

Identical mirrors: `docs/engineering/ELIAS_PRESENCE_HARDWARE_PATH_SCOUT.md` and `sor_sync/docs/engineering/ELIAS_PRESENCE_HARDWARE_PATH_SCOUT.md`.

---

## Summary

Near-bag `user_present` is the authoritative “someone at the bag” on-switch. The **preferred** modality remains **ToF** (ACCEPTED-A); **PIR** is backup; **floor mat** is optional; this paper **adds an ultrasonic class** (hobby bench vs industrial gym families, public product pages cited; unverified prices = **NOT IN SOURCE**) so Ola can decide the gym path without waiting on a PO. Fail-safe is normative and independent of SKU: `presence_sensor_fault` **or** loss **or** power loss → `user_present := false` (absent), **OR’d with inhibit**. Debounce / trip distance / walk-in-out latency remain **TBD — Lead**. Mech owns mount; Controls owns fail-safe→absent wiring. **No PO.** Critical presence-hardware / inhibit / SAF-02 remain **OPEN**. This scout **does not replace** `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`.

---

## Findings (severity)

| ID | Severity | Finding | Disposition |
|---|---|---|---|
| PH-C1 | **Critical — OPEN** | No frozen gym presence SKU or dual-channel topology. Paper-normative fail-safe absent does **not** close inhibit policy, SAF-02, P-05, or B-06. | Lead-owned. This draft does **not** close Critical. |
| PH-C2 | **Critical — OPEN** | Presence forever hard-interlocks physical motion/strike. Hardware path is not a license to actuate. | Do not authorize S3 from this paper. |
| PH-M1 | **Major** | Ultrasonic is listed in Twin ICD as a TBD modality but was **not** SKU-scouted in the BOM scout. Path matrix below; prices only where a public page showed a unit/net figure. | Ola pick: ToF-only vs ToF+ultrasonic A-B vs ultrasonic-as-backup. |
| PH-M2 | **Major** | Gym false-trigger / false-absent risks are **qualitative only** (bag echo, HVAC, lighting, off-mat stance). No FP/FN rates in this paper. | Bench + gym spot-check **TBD — Lead**. |
| PH-M3 | **Major** | Debounce, envelope trip distance, and walk-in/out latency remain **TBD — Lead**. Do not invent ms. | Acceptance language is qualitative until bench. |
| PH-M4 | **Major** | I²C hobby ToF (VL53L1X) vs discrete/analog industrial (Q4X / Banner ultrasonic / P+F) have different **loss-of-signal** wiring stories. Controls must still treat bus/open/power loss as absent. | Wiring freeze **TBD — Lead**. |
| PH-I1 | **Info** | VL53L1X bench, Banner Q4X, Adafruit PIR, Tapeswitch CKP already scouted — **reuse those rows**; do not treat this file as a second BOM. | Pointer only. |
| PH-I2 | **Info** | **NO PO** from Elias. Spend, if any, is Stephen/CFO after Lead routes. | Commercial control. |

---

## Draft ICD / test language

### 1. Path intent (near-bag `user_present`)

`user_present` is **authoritative** for “body in the work envelope next to the bag.” Camera head hypothesis is **aim / session AND**, not a substitute for presence. Empty bag → idle/safe; **no arm play toward empty space**.

**Fail-safe (normative — all candidate modalities):**

```
presence_sensor_fault  ∨  sensor_loss  ∨  power_loss  →  user_present := false
```

- `presence_sensor_fault` is an explicit diagnostic/watchdog bit (twin-adapter table).
- Fault/absent **OR**s into the inhibit path for **physical motion / strike** (presence forever). Session enable is independently false when `¬ user_present`.
- Debounce / glitch filter: **TBD — Lead** — **no invented ms**.
- AI / CV / planner **must not** force `user_present` true.

**Ownership**

| Owner | Owns |
|---|---|
| **Mech** | Mount, aim of the presence beam / cone, cover, floor-mat layout, mechanical protection in gym |
| **Controls** | Fail-safe→absent wiring, `presence_sensor_fault` diagnostics, OR into inhibit, power-loss behavior |
| **Safety / Lead** | Whether a modality is allowed as **sole** person-adjacent presence vs backup-only; PL/SIL **not invented** (SAF-02 OPEN) |
| **Elias** | This path/decision paper only |

### 2. Modalities — path decision matrix (qualitative)

**ASSUMPTION (working prior until Lead freezes):** ToF remains the gym **preferred** near-bag channel per ACCEPTED-A; PIR is occupancy backup; ultrasonic is a **competing proximity class** if optical ToF struggles (shiny bag, gym lighting, dust) — **not** a silent replacement; mat is optional envelope AND/OR (**TBD — Lead**).

False-trigger language below is **qualitative gym-fitness risk**, not a measured FP rate.

| Modality | Gym fitness (qualitative) | False-trigger / false-absent risks (qualitative only) | Mount (Mech) | Fail-safe wiring (Controls) | Path stance this draft |
|---|---|---|---|---|---|
| **ToF / laser distance** | Best “body in envelope” ranging class for a taught window in front of the bag; industrial housings exist | Shiny bag / sweat / dust / sun on optics; wrong teach window sees bag or misses stance; I²C hobby parts need cover + bus-loss = absent | Aim at envelope, not at bag face; protect optic | Discrete/analog preferred for gym; I²C only for bench; open/bus/power → **absent** | **Preferred** (ACCEPTED-A) |
| **PIR** | Cheap occupancy/motion backup; not a ranging window | HVAC / sun / warm bag-adjacent surfaces; motion vs still occupant; EMI near SBC; may miss a still boxer | Cover + keep cone off heaters / windows | Digital out; open wire → **absent**; not sole presence if Lead wants higher integrity | **Backup** |
| **Ultrasonic** | Sound, not light — may help if optical ToF is messy; industrial IP67 families exist | **Bag / floor / wall echo and multi-path**; other ultrasonics; temperature/humidity; dead-zone; hanging bag motion as a moving target | Keep lobe off bag skin and off floor bounce; Mech CAD after envelope | Analog/discrete industrial: cable-break / power → **absent**; hobby echo-pulse needs watchdog | **Class added here** — Lead pick vs ToF |
| **Mat (optional)** | Positive “standing in cell” if the stance is on the mat | User stands off-mat but in envelope → **false-absent**; trip/slip; mat does not see hands-at-bag if feet off | Floor layout TBD; ramp edges; cable routing | Open/fault → **absent** | **Optional** ACCEPTED-A (2) |

**Decision prior (ASSUMPTION — not a freeze):**

1. **Gym primary:** industrial ToF class (Banner Q4X family already scouted) after envelope CAD.
2. **Fixture / bench learn:** VL53L1X class already scouted — **not** the gym housing.
3. **Backup occupancy:** Adafruit PIR class already scouted (hobby) or Panasonic PaPIRs class in BOM scout.
4. **Ultrasonic:** A-B **only if** Lead wants a non-optical proximity check; do not AND-require ultrasonic + ToF for session enable unless Lead freezes that (would raise false-absent).
5. **Mat:** optional AND with ToF for person-adjacent cells — **TBD — Lead**; not a day-one session-enable blocker for digital twin.

### 3. Reuse — already-scouted SKUs (pointer, not a second BOM)

Do **not** treat the following as a new shortlist freeze. Full rows, URLs, and public bands live in `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`. Snapshot reminder only:

| Class | Example already scouted | Role in this path |
|---|---|---|
| ToF bench | ST / Adafruit **VL53L1X** breakout **3967** | Fixture / envelope experiments; I²C; Mech must protect; bus loss = absent |
| ToF bench alt | SparkFun VL53L1X Qwiic **SEN-14722** | Same die family |
| ToF industrial gym | Banner **Q4X** laser distance (ex. **Q4XFULAF610-Q8**) | Discrete/analog teach for “body in envelope”; IP69K-class housing |
| PIR backup | Adafruit PIR **189** | Hobby backup / A-B on fixture |
| PIR industrial-ish | Panasonic PaPIRs **AMN31112** | OEM PIR element class (see BOM scout notes) |
| Optional mat | Tapeswitch ControlMat **CKP 24×48** (Tapeswitch **5514**) | Floor presence; open/fault → absent |

Radar (Banner **QT50R**) appears in the BOM scout as a **non-PIR** weather-immune alternate — out of scope as a day-one presence pick here; mention only so Ola does not confuse it with PIR.

### 4. Ultrasonic class (new — public families)

**Class language (preferred on any later BOM add):** “industrial ultrasonic proximity / distance, discrete NPN/PNP or analog, teachable window, fail-safe absent on loss” + example SKU — **not** a frozen selection.

Hobby modules are **bench / envelope-learn only**, not gym industrial housings. Manufacturer range/voltage/IP figures below are **product-page class facts**, not our acceptance bars. **Do not** copy manufacturer response times into ICD latency.

| Manufacturer / family | Example SKU / series | Why it is on this path matrix | Public budgetary band (USD) | Public source URL | Notes (fail-safe, interface, gym) |
|---|---|---|---|---|---|
| SparkFun / generic | **HC-SR04** ultrasonic distance, 5 V | Cheap echo-pulse bench class to learn envelope geometry | **$5.25** (SparkFun list, 2026-09-21 fetch) | https://www.sparkfun.com/ultrasonic-distance-sensor-hc-sr04.html | Hobby; Trig/Echo; **not** IP-rated gym housing; Controls must watchdog pulse loss → **absent** |
| MaxBotix | **MB1040** LV-MaxSonar-EZ4 | Narrow-beam module class; analog + pulse-width + serial simultaneously | **$24.95** (MaxBotix list, 2026-09-21 fetch; page showed sold out) | https://maxbotix.com/products/mb1040 | Module, not industrial housing; 2.5–5.5 V; Mech cover required; cable/power loss → **absent** |
| Banner Engineering | Ultrasonic **family** (comparison lists **QS18U**, **T30UX**, **QT50U**, others) | Industrial ultrasonic class already in Banner gym-adjacent catalog (same vendor as Q4X ToF) | Unit price for a pinned QS18U / T30UX SKU this draft: **NOT IN SOURCE** (family page has no unit price) | https://www.bannerengineering.com/us/en/products/sensors/ultrasonic-sensors.html | Family comparison: QS18U min/max range class 50–500 mm; T30UX 300–2000 mm — **class only**, not an envelope freeze. Discrete/analog. Re-fetch a SKU page before any shortlist freeze. |
| Pepperl+Fuchs | **UB2000-F42-I-V15** (UB*-F42 cubic ultrasonic) | Industrial analog (4–20 mA) ultrasonic, IP67, M12, teachable limits — gym-housing class | **$222.00 USD net** on manufacturer page (page note: individual price at checkout) | https://www.pepperl-fuchs.com/en-us/products-gp25581/139360 | 10–30 Vdc; sensing-range class 60–2000 mm on that page. Analog cable-break / power → **absent**. **Not** a frozen pick. |

**Ultrasonic gym caveats (qualitative — not FP rates):**
- Boxing bag is a large, slightly moving acoustic target; a lobe aimed at the bag skin can read “present” with nobody in the envelope (**false-present**).
- Floor / wall / cage multi-path can hold a range inside a taught window (**false-present**) or punch through the window (**false-absent**).
- Multiple ultrasonics need sync/multiplex (P+F page lists sync options) — **TBD — Lead** if more than one head is mounted.

### 5. Wiring / fail-safe language (draft ICD)

**Normative draft (does not freeze schematic):**

| Condition | Required `user_present` | Inhibit / motion |
|---|---|---|
| Healthy sensor, body in taught envelope (**TBD — Lead** trip) | `true` | Presence does **not** by itself enable strike |
| Healthy sensor, envelope empty | `false` | Twin idle; **deny** physical motion/strike |
| `presence_sensor_fault == true` | **`false` (forced)** | Treat as absent; **OR** inhibit for motion/strike |
| Open wire / comms loss / watchdog miss | **`false`** | Same |
| Power loss to the presence channel | **`false`** (fail-safe absent; circuit **TBD — Lead**) | Same |
| Debounce / filter | **TBD — Lead** | Do **not** invent ms |

**OR with inhibit (informative):** `¬ user_present` is already an inhibit-source for **physical motion/strike** (Controls ICD §6). Session enable uses the ACCEPTED-A AND and goes false on absent. Do **not** allow planner/AI to override.

**Hobby I²C (VL53L1X) vs industrial discrete/analog:** bench I²C is acceptable for fixture learning only if Controls treats **any** NACK / timeout / brownout as `presence_sensor_fault`. Gym path **ASSUMPTION:** prefer discrete or analog industrial (Q4X or industrial ultrasonic) so loss-of-signal is a wiring property, not a script.

### 6. Acceptance-test outline (qualitative; latency bars TBD — Lead)

Pointer: Twin ICD walk-in / walk-away / empty-bag tests remain the sensing AT language. **Declared walk-in/out latency stays TBD — Lead.** No invented ms, no invented empty-bag false-presence rate.

| ID | Case | Pass language (qualitative) | Not claimed |
|---|---|---|---|
| AT-P-IN | Walk into envelope | `user_present` becomes **true**; twin presence lamp on; session may enable **only if** head valid ∧ ¬inhibit | No latency bar |
| AT-P-OUT | Walk away | `user_present` becomes **false**; twin idle/safe; **no** yaw chase toward empty space; **no** physical motion/strike | No latency bar |
| AT-P-EMPTY | Empty bag, normal gym lighting / typical HVAC | No **persistent** false presence under the qualitative spot-check Lead defines | No FP % |
| AT-P-FAULT | Unplug / power-down / force `presence_sensor_fault` | `user_present := false`; motion/strike denied; session not enabled | Topology **TBD — Lead** |
| AT-P-HEAD | Head hypothesis true, presence false | Session **false**; idle/safe (HIL stub AT-F2) | Camera is not presence |
| AT-P-MAT | If mat fitted: stand off-mat in envelope | Lead decides AND vs OR; this paper does **not** freeze | — |

HY-02 / USB camera gym spot-check is **out of this paper** (see live-USB ICD). Presence AT can proceed on the sensor channel **without** waiting for a USB camera.

### 7. Explicit non-claims / commercial controls

- **NO purchase orders** from Elias. This is path/decision paper. BOM dollars stay in the supplier scout; ultrasonic prices here are public snapshots only.
- **NO NEXT_PROMPT.** Ola owns ready_for_astra / desk flips.
- Does **not** replace `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`.
- Does **not** close Critical: inhibit policy, SAF-02, P-05, B-06 F-01/F-05/F-08, contact-energy SAF-01, PL/SIL.
- Does **not** authorize physical actuation.
- No invented latency, FP/FN, FPS, accuracy, IoU, force, PL/SIL.

---

## Open questions for Ola

1. **Primary gym modality freeze** — stay ToF-preferred (Q4X-class) and treat ultrasonic as optional A-B, or promote ultrasonic to co-equal / backup-only?
2. **AND vs OR** — if both ToF and ultrasonic (or mat) are fitted, is session `user_present` the **OR** (lower false-absent, higher false-present) or **AND** (stricter)? **ASSUMPTION** until answered: single authoritative channel + explicit fault bit, not a silent AND.
3. **Sole-channel integrity** — is hobby PIR or hobby ultrasonic ever allowed as **sole** person-adjacent presence, or industrial discrete/analog only?
4. **Debounce / trip window** — when will Lead bench a walk-in/out bar (still **TBD**; do not ask Elias to invent ms)?
5. **Power-loss topology** — discrete loop-powered / PNP normally-closed vs I²C watchdog: which is the gym wiring freeze?
6. **Mat** — optional AND with ToF for person-adjacent cells, or fixture-only / omit for MVP?
7. **Who runs empty-bag gym spot-check** — Mech mount, Controls wiring, or joint? (Camera HY-02 is a separate residual.)

---

## Ownership / commercial controls

| Role | Owns |
|---|---|
| **Ola (Lead Robotics)** | Integrate / disposition; Critical OPEN/CLOSED; modality freeze; **NEXT_PROMPT** |
| **Elias (Controls & Perception)** | This path/decision draft only |
| **Mech** | Mount / cover / mat layout |
| **Controls (desk)** | Fail-safe→absent wiring under Ola |
| **Safety** | Person-adjacent integrity — not waived |
| **Stephen / CFO** | Spend if Lead routes a PO later |

| Control | Rule |
|---|---|
| PO | **NONE** |
| NEXT_PROMPT | **NONE** — do not write ready_for_astra from this desk |
| Numeric bars | **No invented latency / FP / FPS / accuracy / IoU / force / PL/SIL** |
| Actuation | **Not authorized** |
| BOM scout | **Not replaced** |

---

*Elias Controls & Perception — DRAFT 2026-09-21 for Ola integrate. Identical mirror: `sor_sync/docs/engineering/ELIAS_PRESENCE_HARDWARE_PATH_SCOUT.md`. PAPER ONLY. No NEXT_PROMPT. No PO. Critical OPEN.*
