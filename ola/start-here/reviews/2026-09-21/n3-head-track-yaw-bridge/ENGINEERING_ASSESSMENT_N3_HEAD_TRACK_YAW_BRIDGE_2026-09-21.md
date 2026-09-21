# ENGINEERING ASSESSMENT — n3-head-track-yaw-bridge

**Assessor:** Ola (Lead Robotics)  
**Date:** 2026-09-21 ~09:00 ET  
**Disposition:** **ACCEPTED-A** — digital Track A head→carrier-yaw bridge demo only  
**Packet (SoR):** `reviews/2026-09-21/n3-head-track-yaw-bridge/`  
**Film:** `media/head_yaw_review.mp4` (12.000 s container; film encode 12 fps construction choice — **not** processing-rate evidence)

**Evidence reviewed (standing depth):** READY_FOR_OLA, README, EXECUTIVE_REVIEW, DEFECT_REGISTER, CHANGELOG_OPEN_ITEMS, INTERFACE_VULNERABILITIES, ENVELOPE_GEOMETRY_AUDIT, SOURCE_BRIEF, demo_config + config_template, unit/integration/model/media/packet/visual verification JSON, bridge_core.py, blender_receiver.py, capture_head.py (skim), audit_bridge.log, stills/contact sheet, and full film scrub.

**Normative lock bit name:** `pitch_lock_engaged` (not required for this digital yaw pedagogy).

---

## Summary

**ACCEPTED-A** for the **digital Track A integration demo**: synthetic translated NASA still → OpenCV Haar head prior → loopback UDP/JSON → Blender N3 carrier yaw, with simulated presence / fault gates idle to home-zero.

Film scrub confirms:
- L/R FOLLOW: labeled effective yaw **−15.52°** / **+14.48°** under **ASSUMPTION** demo mapping; bag + mast fixed.
- Six idle chapters (presence absent, head invalid, presence fault, sync stale, inhibit latch, sim E-stop) snap/hold **HOME / IDLE 0.00°**.
- Persistent ASSUMPTION strip: demo mapping only; gain/clamp/idle/timing TBD — Lead; no force / real-gym / hardware-stop proof.

Digital audits claim **PASS** (unit 32/32 gates, 0 failures; integration 144 packets actual UDP; model bag/camera matrix deviation 0.0, yaw replay error ~1e−6°; packet PASS_WITH_ENGINEERING_RESIDUALS). Receiver **does not trust** sender-computed yaw/enable; loopback-only; sticky latch + separate manual reset/arm.

**Not closed:** B-06, C-01, SAF-02/P-05, HY-02 (real camera), HY-03 (Lead freeze), live USB path, System ID / strike impulse. Demo angles are **not** frozen gains.

---

## Findings (severity)

| ID / topic | Severity | Status | Notes |
|---|---|---|---|
| Head L/R → carrier yaw (digital) | — | **CLOSED-A (demo)** | Film + stills + integration PASS |
| Presence / invalid / fault / stale / latch / E-stop → idle | — | **CLOSED-A (demo)** | Film chapters + unit 32 combos |
| UDP loopback twin drive | — | **CLOSED-A (demo)** | Actual UDP; receiver re-derives enable/yaw |
| Inherited scenes / baselines | — | **PASS (digital)** | 5 scenes, 11 hashes preserved |
| HY-01 | Integration | **CLOSED-A (this pass)** | Adapter implemented; synthetic digital PASS |
| HY-02 | High residual | **OPEN** | Synthetic only; real-gym sensing needed |
| HY-03 | High residual | **OPEN — Ask Michael** | Gain/sign/clamp/idle/timeouts not frozen |
| HY-04 | Digital fault | **CLOSED-A (software)** | Latch/reset/arm/watchdog exercised; software scope |
| A-05 / A-03 / G-03 / G-05 | High baseline | **Unchanged** | Sampled digital; loaded clearance OPEN |
| B-06 / C-01 | Critical | **OPEN** | Unchanged |
| SAF-02 / P-05 | Critical residual | **OPEN** | GUI home-zero ≠ hardware stop/vent |

---

## Engineering recommendations

1. **Accept (A)** this pass as Track A digital V&V of the Elias head-track→yaw path — pedagogy and software integration only.
2. Keep **ASSUMPTION** labels on START_HERE / Pages embeds; never cite −15.52° / +14.48° as frozen map.
3. Leave `config_template.json` **null** for production; `demo_config.json` stays opt-in illustrative (30°/±30°/2 s) until Lead freeze.
4. **Lead provisional digital conventions** (normative freeze still Michael-gated): signed offset `2x−1`; positive image-x → positive +Z yaw from −Y home as demoed; digital idle = **home_zero**; chase blocked on non-ok sync / latch / E-stop / timeout. **Do not** promote demo gain 30° into production until Michael confirms.
5. Next engineering pass options (Michael pick): live USB + real-person motion; authoritative presence bench; or continue Critical B-06 / C-01.
6. Ibrahim: fold assessment + ACCEPTED-A into Pages / START_HERE; keep webhook hardening.

---

## Test / validation gaps

| Gap | Why it matters |
|---|---|
| Live USB / gym webcam | Not exercised this pass |
| Real presence (ToF/PIR/mat) | Simulated timeline only |
| Detector accuracy / FPS / latency | Explicitly **NONE** claimed |
| Lead mapping freeze | HY-03 OPEN |
| Loaded clearance / durability | Out of scope; not inventable |
| Physical stop / limp (SAF-02) | Digital latch ≠ industrial stop |

---

## Manufacturing notes

- **No DFM / BOM change** from this Track A demo.
- Camera mount, FOV/mirror calibration, presence mount, yaw encoder (F-05), Option B `pitch_lock_engaged` hardware remain Mech / Lead.
- Soft continuum / Soft physics docs untouched.

---

## Open questions for Michael

1. **Freeze mapping/sign** as demoed (positive image-x → positive carrier yaw), or reverse for final mount?
2. **Freeze gain/clamp** now (use 30° demo as starting ASSUMPTION) or hold null until live camera?
3. Confirm digital **idle = home_zero** (vs hold-last) as normative twin policy?
4. Confirm **watchdog 2 s** demo as interim digital freshness bar, or set another value?
5. **Next priority:** live USB gym check, presence hardware scout, or B-06 / C-01?

---

## Disposition table

| Scope | Disposition |
|---|---|
| Digital Track A head→carrier-yaw bridge (synthetic + sim presence + UDP→Blender) | **ACCEPTED-A** |
| Live USB, real presence, frozen production gains | **OPEN** |
| HY-02, HY-03, B-06, C-01, SAF-02/P-05 | **Remain OPEN** |
| System ID / strike impulse | **Not in scope** |

---

## Plain-language glossary

| Term | Everyday meaning | Why it matters here |
|---|---|---|
| **UDP loopback** | PC sends short messages to itself into Blender | Head cues actually drove the twin over local UDP |
| **Carrier yaw** | Shoulder ring turns about the mast | Bag/fill/mast must stay fixed |
| **Presence gate** | “Someone is here” on-switch | Without it, chase must idle |
| **Sticky latch** | Fault that stays on until a person clears it | Inhibit / E-stop need manual reset then separate arm |
| **Watchdog** | Freshness check on packets | Stale/missing data → home-zero |
| **Track A** | Digital twin / teaching V&V | Not punch force or System ID |
| **`pitch_lock_engaged`** | Option B pitch pin locked | Required before pressurized strike; not for this yaw demo |

---

## Key audit citations (from SoR JSON — not invented)

- `unit_verification.json`: PASS — 32 gate combinations, 0 failures
- `integration_verification.json`: PASS — 144 packets, actual loopback UDP; performance claim NONE
- `model_verification.json`: PASS — fixed bag/camera 0.0; yaw replay max error ~7.8e−7°; interactive latch/reset/watchdog PASS; 5 inherited scenes / 11 baselines
- `packet_verification.json`: PASS_WITH_ENGINEERING_RESIDUALS — independent Ola acceptance was PENDING (this document closes it for digital demo scope)
- `visual_review.json`: PASS_WITH_LIMITATIONS — Codex visual; Ola film scrub agrees
- `demo_config.json`: ASSUMPTION opt-in 30° gain / ±30 clamp / 2 s watchdog / home_zero

*Signed Lead disposition. No PO. No invented FPS/accuracy/force. Track A ≠ strike impulse.*
