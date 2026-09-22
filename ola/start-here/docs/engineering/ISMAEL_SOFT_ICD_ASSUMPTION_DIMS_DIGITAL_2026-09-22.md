# ISMAEL — Soft ICD ASSUMPTION Dims Digital Column (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-22 ET |
| **Disposition** | PAPER — Soft ICD digital column: keep-outs + **ASSUMPTION** dims when G1 CAD missing |
| **Critical B-06** | **OPEN** |
| **Critical C-01** | **OPEN** |
| **PO** | **NONE** — $0 digital; no fab |
| **Normative lock bit** | `pitch_lock_engaged` only |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_ICD_ASSUMPTION_DIMS_DIGITAL_2026-09-22.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_ICD_ASSUMPTION_DIMS_DIGITAL_2026-09-22.md` |

**Cites (do not overwrite ACCEPTED-A sources):**  
`ISMAEL_B06_SOFT_TERMINATION_ICD.md` (**ACCEPTED-A** stack);  
`ISMAEL_B06_OPTION_B_ENVELOPE_KEEP_OUT.md`;  
`ISMAEL_B06_OPTION_B_ENVELOPE_DEEPEN_v2_2026-09-21.md` (**ACCEPTED-A** paper);  
`ISMAEL_B06_KEEP_OUT_PITCH_NUMERIC_TARGETS_2026-09-21.md`;  
`ISMAEL_B06_ABS_MOCK_BOOT_PATH.md`;  
Ola `OLA_INTEGRATE_ISMAEL_B06_ENVELOPE_2026-09-21.md` / `OLA_INTEGRATE_ISMAEL_B06_OPTION_B_2026-09-21.md` / soft EXECUTE deepen.

**Standing:** Every mm below is **ASSUMPTION** / **DESIGN TARGET** / **GEOMETRY TARGET** — **NOT measured clearance**. Soft ICD numeric freeze **pending Lead G1 CAD**. Chafe sleeve family **waits** ABS mock fit-check (**OPEN** note). Soft TB ≠ Mech OB-M5. Zero spend language. Soft idle on live `.blend`.

**Out of Soft scope (one-line):** **HY-02 live face-in-ROI** — Soft does **not** own; belongs Controls / Ola (camera-in-hand + head-track→yaw orthogonal; Soft twin deepen does not own them).

---

## Summary

Digital Soft ICD column Soft can quote while Lead G1 CAD dims are missing: keep-out **classes**, catalog bend **DESIGN TARGET** floors, GEOMETRY TARGET / coupon envelopes, and Soft-termination class language — all labeled **ASSUMPTION / DESIGN TARGET**, explicitly **not** measured hardware clearance. Chafe PN remains **OPEN** (wait mock fit-check). Critical **B-06 OPEN**. Soft ICD ≠ Critical close.

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| ICDD-01 | Critical OPEN | Paper ASSUMPTION dims ≠ FEA PASS ≠ B-06 close. |
| ICDD-02 | High (ICD) | Soft must not imply S3 strike without `pitch_lock_engaged`. |
| ICDD-03 | High (process) | Soft ICD class freeze accepted; **numeric freeze pending CAD**. |
| ICDD-04 | Med | Boot / eye / pin-plate CAD mm still TBD Lead — Soft does not invent structural dims. |
| ICDD-05 | Med | **Chafe sleeve PN waits ABS mock fit-check** — OPEN until fit-check. |
| ICDD-06 | Info | Catalog R floors = keep-out floors; flow-relevant preferred when motion+flow. |
| ICDD-07 | Info | HY-02 live face-in-ROI = Controls/Ola — Soft skips. |
| ICDD-08 | Info | Soft Blender soft-body remakes = non-gate for B-06. |

---

## Soft ICD digital column — keep-outs + ASSUMPTION dims

### A — Keep-out class stack (cite ACCEPTED-A envelope)

```
  KO_MAST_HUB → KO_YAW_CARTRIDGE → KO_PITCH_PIN_PLATE
       → KO_RECESSED_BOOT → KO_TEXTILE_EYE_RECESS → KO_CONTINUUM → KO_SOFT_WRIST_GLOVE
  SERVICES: KO_FLEX_LOOP_SHORT / _MID / _TALL
  CHAFE:    KO_CHAFE_BOOT_LIP / KO_CHAFE_EYE_HARDPOINT / KO_CHAFE_PIN_FLAG
  PINCH:    KO_PINCH_PITCH_HINGE / KO_PINCH_PIN_CHEEK / KO_PINCH_BOOT_GUARD
```

| Soft keep-out class | Soft rule | ASSUMPTION / DESIGN TARGET dim language | Tag |
|---|---|---|---|
| `KO_FLEX_LOOP_SHORT/MID/TALL` | Bundle survives pin remove/re-pin; outside pinch planes; Option A — do **not** lengthen continuum | Sized to catalog R floors (§B) + 8-branch bundle; exact volume mm³ TBD mock | **DESIGN TARGET** floor only |
| `KO_TEXTILE_EYE_RECESS` | Clear pin-flag travel + boot lip; eye/stitch pack seats without binding | ID/OD / recess depth **TBD Soft DFM + Lead CAD** — no invented Soft eye mm | **TBD CAD** |
| `KO_CHAFE_*` | Sleeve land at Soft tube ↔ metal/ABS; no tube under eye stitch; clear pin/flag | Sleeve PN **wait mock fit-check** — **OPEN** | Qualitative + catalog floor |
| `KO_PINCH_*` | Soft hose outside pinch planes | Finger-gap mm = Safety/Lead OPEN — Soft does **not** invent gap mm | Soft narrative only |
| Boot bolt circle / shell | Soft ICD couple only | Matches Lead reserved Option A/B bolt circle — Lead TBD | Soft interface note |

**ASSUMPTION:** Exact solid extents wait Lead envelope CAD (G1). Soft quotes **classes + catalog floors**, not locked structural CAD.

### B — Tube bend keep-out floors (catalog → DESIGN TARGET — not measured clearance)

| Tube class (ASSUMPTION coupon/prod) | Published figure | Soft **DESIGN TARGET** keep-out floor | Tag |
|---|---|---|---|
| NITRA PU **6 mm** | R_min **12.0 mm** | Centerline bend radius **≥ 12 mm** | **DESIGN TARGET** from catalog |
| NITRA PU **1/4″** | R_min **≈ 12.1 mm** | **≥ 12.1 mm** | **DESIGN TARGET** |
| Festo PUN **6×1** min bend | **16 mm** | **≥ 16 mm** | **DESIGN TARGET** |
| Festo PUN **6×1** flow-relevant | **26.5 mm** | Prefer **≥ 26.5 mm** when motion + flow | **DESIGN TARGET** (preferred floor) |

**ASSUMPTION:** Coupon provisional OD = NITRA 6 mm or 1/4″; production lean Festo PUN-H (OD freeze open).  
**Rule:** Loop volume at short/mid/tall must respect floors; loop **outside** pitch pinch planes.

### C — Continuum / coupon length envelopes (GEOMETRY TARGET / ASSUMPTION)

| Item | mm band | Role | Tag |
|---|---|---|---|
| Upper soft section centerline | **380–438** | Film path — **not** Soft free length | **GEOMETRY TARGET** |
| Forearm soft section centerline | **252–368** | Film path | **GEOMETRY TARGET** |
| Wrist forearm-end→glove peak | **105** | Peak only | **GEOMETRY TARGET** |
| Max shoulder→wrist chord | **≈ 859** | Not pneumatic travel | **GEOMETRY TARGET** |
| TB-01 active span | **150–250** | Bench coupon | **ASSUMPTION** / **DESIGN TARGET** fixture |
| TB-02 section (shortened OK) | **200–300** (or within 252–368) | Bench coupon | **ASSUMPTION** |
| TB-03 cuff-to-cuff | **80–120** | Soft wrist coupon | **ASSUMPTION** |

**ASSUMPTION:** GEOMETRY TARGET path lengths ≠ elastomer free lengths / Soft OD.

### D — Soft-termination ICD class (pending CAD numeric freeze)

| Soft class | Statement | Dims / ratings | Tag |
|---|---|---|---|
| Termination | Soft load path ends in textile eye / harness into **recessed boot**; last metal at boot; **no distal exposed metal** | Freeze; **no N** | Lock |
| Eye geometry (SF-01 class) | Webbing / eye-strap / D-ring **geometry analogs** — **no Soft load rating** | ID/OD **TBD CAD** | **ASSUMPTION** wait CAD |
| Stitch / harness (ST-H1…H4) | Tensile into harness/eye **not** bladder neck | Schedule TBD Soft DFM — **no invented SPI** | Class only |
| Strain-relief (ST-SR1…SR3) | Gradual textile→eye→boot; loop from **root packaging**, not continuum lengthening | Length band after mock — **no mm invented** | **ASSUMPTION** |
| Flex-loop MVP | Discrete short/mid/tall; rotary union deferred | Bend keep-out = §B catalog floors | **DESIGN TARGET** |
| `pitch_lock_engaged` | Soft services must **not** imply S3 strike without bit | Normative | Lock |

### E — Chafe OPEN note (binding)

| Item | Status |
|---|---|
| Chafe sleeve / tape family (OB-S-CHF1) | **OPEN** — **wait ABS mock fit-check** before PN freeze (Ola lock) |
| Unit $ / exact PN | **NOT IN SOURCE** until Soft DFM picks after fit-check |
| Soft action now | Keep qualitative keep-out + family pointers only — **do not freeze** |

### F — Pitch preset posture (qualitative)

| Preset | Soft rule | Numeric claim |
|---|---|---|
| Short / Mid / Tall | Discrete pin holes only; Track A angles = drawing aids | Hardware angles TBD Lead — Soft does not rate from Track A degrees |
| Flex-loop survival | Bundle survives pin remove/re-pin at each preset | Fit-check mock later — no invented travel mm |

---

## Soft ↔ Lead handoff (digital column)

| Interface item | Soft owns (digital) | Lead owns | Status |
|---|---|---|---|
| Textile eye / harness geometry class | **Yes** — class language | Consumes envelope | Class OK; mm TBD CAD |
| Stitch / harness schedule class | **Yes** | — | Soft DFM TBD |
| Strain-relief length class | **Yes** | Clearance in boot | After mock |
| Recessed boot shell / bolt circle | Interface notes | **Yes** | Lead TBD |
| Pitch pin plate / pin / flag | Chafe keep-out vs Soft | **Yes** | — |
| Flex-loop volume / bend keep-out | Catalog R floors §B | Pinch planes / packaging | DESIGN TARGET floors |
| `pitch_lock_engaged` | Soft must not imply strike without bit | Mech cam/flag | Normative |
| Pinch gap mm | Soft hose narrative | Safety / Lead | Soft does not invent |
| Chafe PN freeze | After mock observations | — | **OPEN — wait mock** |
| HY-02 live face-in-ROI | **Not Soft** | Controls / Ola | Soft skips |

---

## ASSUMPTION tables

| # | ASSUMPTION |
|---|---|
| A1 | Catalog R_min / flow-relevant = Soft keep-out floors, **not** measured fixture clearance |
| A2 | GEOMETRY TARGET path lengths ≠ Soft free lengths / Soft OD |
| A3 | Coupon free-length bands = fixture DESIGN TARGETS |
| A4 | Boot / eye / pin CAD mm TBD Lead — Soft does not invent |
| A5 | Chafe PN **wait** mock fit-check — OPEN |
| A6 | Soft ICD numeric freeze pending G1 CAD |
| A7 | Option A stand-off — no continuum lengthening |
| A8 | Soft TB ≠ Mech OB-M5 |
| A9 | Soft Blender soft-body remakes optional / non-gate |
| A10 | HY-02 face-in-ROI = Controls/Ola — Soft does not own |

---

## Draft recommendations

1. Accept this Soft ICD digital column as quoting companion while G1 CAD missing — all mm labeled ASSUMPTION / DESIGN TARGET / GEOMETRY TARGET.  
2. Prefer Festo flow-relevant floor (**≥ 26.5 mm** for 6×1 class) for product-lean routing; NITRA floors OK for coupon bench.  
3. Keep Soft ICD class language; **numeric freeze waits CAD**; chafe waits mock.  
4. Soft idle on live blend; Empty names remain ASSUMPTION / Lead-confirm.  
5. Zero spend — paper only; money-gated ABS mock / Soft TB parked per standing (no chase here).

---

## Test gaps

| Gap | Owner | Status |
|---|---|---|
| Lead G1 envelope CAD dims | Lead | OPEN — blocks Soft ICD numeric freeze |
| ABS mock cut list + fit-check | Soft + Mech (when opened) | Money-gated hardware **parked** — Soft paper only |
| Chafe PN freeze | Soft after mock | **OPEN — wait mock** |
| Pinch gap qualification mm | Safety / Lead | Soft does not invent |
| Hose flex at presets | Soft + Mech | OPEN |
| B-06 Critical close | Lead design + FEA + proto | OPEN |

---

## Open questions for Ola

1. Accept Soft ICD ASSUMPTION-dims digital column (B-06 OPEN; dims ≠ measured clearance)?  
2. Confirm preferred keep-out floor = Festo flow-relevant for prod-lean; NITRA for coupons?  
3. Confirm chafe still waits mock; Soft ICD still pending CAD?  
4. Confirm HY-02 live face-in-ROI stays Controls/Ola (Soft skip)?  
5. Soft idle after land until Lead asks — still correct?  
6. Preferred SoR land OK?

---

## Non-claims

- **No PO.** Critical **B-06 OPEN** · **C-01 OPEN**.  
- **No invented** structural CAD mm / N / MPa / FEA PASS / finger-gap / peel N.  
- DESIGN TARGET / ASSUMPTION ≠ measured clearance.  
- Soft ICD ≠ Critical close. Soft TB ≠ Mech OB-M5.  
- No spend chase · no NEXT_PROMPT · HY-02 not Soft-owned.

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Label | **ASSUMPTION / DESIGN TARGET** — not measured clearance |
| Critical B-06 / C-01 | **OPEN** |
| Chafe | **OPEN — wait mock fit-check** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-22 ET · awaiting Ola disposition —
