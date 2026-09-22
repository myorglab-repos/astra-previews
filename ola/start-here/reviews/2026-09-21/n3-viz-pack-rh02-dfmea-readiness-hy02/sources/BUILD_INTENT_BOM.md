# Build-intent BOM (integrated — paper only, no PO)

**Owner:** Ola (Lead) · **Date:** 2026-09-21  
**Status:** Soft + Controls/sensing scouts **ACCEPTED-A** and merged.  
**Michael:** execute without further approvals — quotes/scouting only; no POs from this doc.

## Soft modules (Ismael — ACCEPTED-A)
Source: `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` (SM-C1…C7).

| Lead lock | Choice |
|---|---|
| TB-01/TB-02 path | In-house cast Smooth-On Ecoflex / Dragon Skin first |
| Custom bladder RFQ | After cast learning (Dynamic / ARC / Eutsler) |
| Coupon manifold | Discrete/paired NITRA/SMC |
| Production manifold | Custom or Twintec-class 8-branch after tube OD freeze |
| Coupon tube | Provisional NITRA 6 mm or 1/4″ |
| Production tube | Prefer Festo PUN-H |

**Public price examples (scout):** Ecoflex trial ~$33; Dragon Skin trial ~$38; Mood PowerNet ~$14/yd; NITRA PU 100 ft ~$22–$34; Sailmaker D-ring ~$0.78. Custom rubber houses NOT PUBLICLY LISTED.

## Controls & sensing (Elias — ACCEPTED-A)
Sources: `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md`, `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md`.

| Class | Lead shortlist (example SKU class) | Public band (scout) |
|---|---|---|
| ToF presence (bench) | Adafruit 3967 / SparkFun VL53L1X | ~$15 / ~$30 |
| ToF presence (industrial) | Banner Q4X family | ~$681–$692 |
| PIR backup | Adafruit PIR / Panasonic PaPIRs | ~$10 / ~$27@MOQ |
| Presence mat (optional) | Tapeswitch ControlMat class | ~$604 (24×48) |
| E-stop | IDEM ES-P station / Schmersal NDRZ50RT + blocks / Schneider XB4 | ~$38–$121 |
| Option B pitch lock | Omron D4N / Honeywell BZ | ~$22–$45 |
| Yaw encoder | CUI AMT102-V class | ~$27.50 |

Twin signals: see Elias signal table (`user_present`, `session_enable`, `pitch_lock_engaged`, `yaw_encoder_valid`, `e_stop_asserted`, …).

## Root / Option B (Lead)
`B06_OPTION_B_INTERFACE_FREEZE.md` — pinned presets, recessed boot, flex-loop services.

## Explicit
- **No purchase orders** from this document.
- Critical **B-06** / **C-01** / **SAF-02** remain OPEN until designed, analyzed, and (when Stephen opens) purchased/tested.
- Track A films ≠ System ID.
