# B-06 Option B — Soft-side DFMEA deepen + Soft-facing BOM scout deepen

| Field | Value |
|---|---|
| **Title** | Soft-side + interface DFMEA starter deepen; Soft-facing + mock-boot BOM scout deepen (no PO) |
| **Author** | Ismael (Soft Robotics desk draft for Ola disposition) |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Status** | **DRAFT — ready for Lead review** |
| **Critical B-06** | **OPEN** |
| **PO** | **NONE** — catalog scout language only |
| **Normative lock bit** | `pitch_lock_engaged` only |
| **Canonical SoR target (parent CopyFromBox)** | `C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\docs\engineering\ISMAEL_B06_OPTION_B_DFMEA_BOM_DEEPEN.md` · machineId `c9e3c1b7-3db3-4333-a063-5b46c67938f9` |
| **Box staging** | `/workspace/boxing-trainer/drafts/` · `/workspace/boxing-trainer/docs/engineering/` · `/workspace/boxing-trainer/sor_sync/` |

**Companions:** `B06_ROOT_PITCH_HARDWARE_SKETCH.md` §5 DFMEA starter (F-01…F-10); `ISMAEL_B06_OPTION_B_PATH_AND_BOM_SCOUT.md` OB-M1…M7 + OB-S1; Soft `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md`; Elias sensing scout §5 (cite, do not re-primary switch pricing).

---

## Structured findings

### Summary
Deepens DFMEA for **Soft-side + interface rows only** (extend F-01 / F-03 / F-04 / F-08 class + Soft peel/chafe/pinch). **No RPN. No invented severity numbers.** Deepens Soft-facing + mock-boot BOM classes (ABS sheet, mock fasteners, textile-eye hardware, chafe sleeve/tape, flex-loop tube pointer). Cross-refs Mech **OB-M1…M7** and Elias **OB-S1** — does **not** re-own structural or switch pricing as primary. Critical B-06 OPEN. No PO.

### Findings

| Severity | Finding |
|---|---|
| **High (process)** | DFMEA remains starter — blank S/O/D until analysis; no fake RPN. |
| **Med** | Soft-facing catalog $ cited only where public this session; else **NOT IN SOURCE**. |
| **Info** | Mech OB-M* spend band separate from Soft TB-01/02 when Stephen opens — no PO now. |

---

## 1. DFMEA deepen — Soft-side + interface only

**Method:** Extend root sketch F-01 / F-03 / F-04 / F-08 class with Soft-owned detail rows. Severity / occurrence / detection stay **blank**. No invented loads.

### 1.1 Extended Soft / interface rows

| ID | Function | Failure mode | Local effect | System effect | Potential cause | Current prevention (intent) | Detection (intent) | Recommended action | Owner |
|---|---|---|---|---|---|---|---|---|---|
| **F-01** *(interface note)* | Hold pitch under gravity + punch reaction | Pitch unlock / free fall | Arm drops | Mis-aim; pinch; user surprise | Pin not engaged; flag not home | Detent/ball-lock + visual flag (prefer); hard stops | Limit/plunger → **`pitch_lock_engaged`**; visual flag | Soft must not imply S3 without bit; Mech CAD cam/flag | Mech primary; Soft ICD couple |
| **F-03** | Soft termination retention | Textile eye peel / pull-out | Soft arm detaches at root | Loss of arm; exposed hardware risk | Undersized eye, abrasion, wrong stitch | Recessed boot; strain-relief; harness primary (ST-H1) | Coupon pull later; visual fray | Soft DFM + Lead boot; Stephen coupon when spend opens | Soft + Mech/Matl |
| **F-03a** *(Soft deepen)* | Soft termination retention | Stitch unravel / harness fray | Progressive loosen | Same as F-03 | Wrong stitch schedule; chafe at eye | ST-H2 schedule class; inspectable edge | Visual inspection schedule (TBD — no life #) | Soft DFM freeze stitch class | **Soft** |
| **F-03b** *(Soft deepen)* | Soft termination retention | Tensile into **bladder neck** not harness | Neck peel / seal fail | Soft detach / leak path | Harness load path missing | ST-H1; ties B-01 / H-05 | Coupon + neck inspection | Keep Soft coupon order; Soft ICD | **Soft** |
| **F-04** | Route air at pitch hinge | Hose pinch / fatigue crack | Chamber limp or stuck | Wrong punch shape; leak | Bend &lt; published R_min; sharp edge; pinch plane | Flex-loop; catalog R_min (Festo PUN / NITRA); edge radius; outside pinch planes | Pressure decay later; visual chafe | Soft keep-out Empties + Lead pinch review | Soft + Mech/Pneum |
| **F-04a** *(Soft deepen)* | Route air at pitch hinge | Hose **chafe** at boot lip / eye / pin flag | Wall wear → leak | Chamber limp | No sleeve; sharp lip; flag abrasion | Chafe sleeve/tape class; KO_CHAFE_* | Visual chafe | Specify sleeve class before mock fit | **Soft** |
| **F-04b** *(Soft deepen)* | Route air at pitch hinge | Flex-loop volume insufficient at a preset | Forced kink at short/mid/tall | Leak / shape error | Keep-out undersized; continuum lengthened (forbidden) | Discrete preset Empties; Option A stand-off | Fit-check mock | Iterate Soft ICD after ABS mock | **Soft** + Lead |
| **F-08** | User proximity | Pinch at pitch hinge | Soft-tissue injury | Safety incident | Gap &lt; finger; no cover; hose in pinch | Padding + guards; Soft hose outside pinch | Risk assessment | Safety gate before pilot; Soft keep-outs support | Safety primary; Soft support |
| **F-08a** *(Soft deepen)* | User proximity / service | Operator pinch during pin change with Soft services present | Finger injury; hose crush | Safety + Soft F-04 | Hose routed through cheek gap | Service routing clear of pin path; procedure | Procedure review | Soft service narrative + Lead DFA | Soft + Mech |

**Intentionally not re-owned here (Lead / other):** F-02 bearing walk-out; F-05 encoder; F-06 bumper energy (Mech after mass props); F-07 service cartridge; F-09 corrosion; F-10 over-pressure Soft reaction (Pneum / C-01 lane — **not expanded in this packet**).

### 1.2 Soft DFMEA non-claims

- **No RPN**, no severity / occurrence / detection scores.  
- **No invented** N, MPa, N·m, cycle life.  
- Soft rows **support** Critical B-06; they do **not** close it.

---

## 2. BOM scout deepen — Soft-facing + mock-boot classes

**Method:** Public catalog language 2026-09-21 ET where available; else **NOT IN SOURCE**. Candidates only. **No PO.**

Cross-ref rule: Mech **OB-M1…M7** and Elias **OB-S1** remain primary for structural pin/plate/bushing/bumper/fastener-band and switch pricing — Soft deepens Soft-facing classes and **pointers**.

| Soft class ID | Part class | Example catalog family (candidate) | Role | Public $ OR NOT IN SOURCE | Public lead-time OR NOT IN SOURCE | Source / pointer | Notes / ASSUMPTIONS |
|---|---|---|---|---|---|---|---|
| **OB-S-MB1** | ABS / sheet mock boot material class | TAP Plastics Primex ABS cut-to-size; ePlastics ABS engineering plate; Clearly Plastic ABS | Mock recessed boot shell for Soft fit-check | TAP public **“From $15.00”** cut-to-size language; ePlastics example **0.500″×12″×12″ ~$45.05** (1–2 band, session search); Clearly Plastic example **$24.12** family. Exact mock net $: **NOT IN SOURCE** until cut list | TAP: **1–2 business days** cut language; others: confirm at checkout / **NOT IN SOURCE** fixed days | https://www.tapplastics.com/product/plastics/cut_to_size_plastic/abs_sheets/524 · https://www.eplastics.com/sheets/abs/engineering-plate · https://www.clearlyplastic.com/products/abs-sheets | Deepens Mech **OB-M5**. Molded later after envelope CAD. **No PO.** |
| **OB-S-MB2** | Fastener class for **mock** (non-structural) | Button/socket head screw class — ADC FATH band cited in Mech scout (ex. 161100 M8 pack); nylon screw / standoff class for mock only | Hold ABS mock panels / Soft fixtures | Mech scout: ADC FATH **~$1.00–$8.25/10** pack band publicly listed. Exact mock BOM: **NOT IN SOURCE** until hole pattern | ADC free 2-day small-package language when stocked (site-wide; confirm) | Mech path scout **OB-M6**; https://cdn.automationdirect.com/static/specs/fathfasteners.pdf | **ASSUMPTION:** mock fasteners ≠ structural root fasteners. Do not re-own OB-M6 as primary. |
| **OB-S-EYE1** | Textile-eye hardware class | Soft SM-C6 — Sailmaker’s Supply 1″ welded D-ring; Bainbridge sail hardware family | Geometry-class eye into recessed boot | Soft scout: Sailmaker’s **$0.78** ea publicly listed. Bainbridge unit: **NOT PUBLICLY LISTED** | Sailmaker’s ship: **NOT IN SOURCE** this deepen (re-check Soft scout / live page before any future buy) | Soft `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` SM-C6 · https://www.sailmakerssupply.com/product/1-inch-welded-d-ring/webbing-accessories | **No Soft load rating.** Metal at boot only. |
| **OB-S-EYE2** | Webbing / harness textile class | Mood PowerNet / webbing analogs from Soft scout SM-C2 | Harness into eye | Soft scout: Mood PowerNet **$13.96/yd** publicly listed (session of Soft scout) | **NOT IN SOURCE** fixed Soft harness length $ | Soft SM-C2 | Geometry / textile class only — no peel N |
| **OB-S-CHF1** | Chafe sleeve / abrasion tape class | Expandable PET braid sleeve class; self-fusing silicone tape class; cloth friction tape class (industrial catalog families) | Protect Soft tube at boot lip / eye / pin adjacency | Unit $ this deepen session: **NOT IN SOURCE** (no live PN price re-fetched in this packet — do not invent) | **NOT IN SOURCE** | Family pointers only until Soft DFM picks PN | **ASSUMPTION:** sleeve required at KO_CHAFE_*; PN TBD Soft DFM. Qualitative keep-out already Soft §3. |
| **OB-S-TUB1** | Flex-loop tube + fittings pointer | Soft SM-C4 / Mech **OB-M7** — NITRA PU coupon; prefer Festo PUN-H prod | 8 independent branches through root flex-loop | NITRA public (Soft/Mech scouts): PU6MBLK100 **$34.00**/100 ft; PU14BLK100 **$32.00**/100 ft; US6M/US14 **$10.00**/5 pk; TC-12 **$5.75**. Festo PUN-H unit $: **NOT PUBLICLY LISTED** (datasheet) | ADC free 2-day small-package language when stocked; Festo lead **NOT PUBLICLY LISTED** | Soft scout SM-C4 · Mech **OB-M7** · Festo PUN PDF · NITRA tubing PDF | Cite Soft for bend-radius keep-outs. **Do not re-price as new primary** — pointer deepen. 8 branches never serial U→F. |
| **OB-S-SW1** | Pitch lock sense switch | **Pointer to Elias OB-S1 / Elias §5** — Omron D4N / Honeywell BZ | Assert `pitch_lock_engaged` | **Do not re-price as primary** | See Elias | `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` §5 | Soft ICD couples bit only |
| **OB-S-PIN1** | Pin / flag hardware | **Pointer to Mech OB-M1** | Discrete presets + visual flag | See Mech scout (Freer detent example etc.) | See Mech | Path scout **OB-M1** | Soft chafe keep-out only |

### Price found vs NOT IN SOURCE (this deepen)

| Rows | With public $ example this packet | NOT IN SOURCE / pointer-only |
|---|---|---|
| OB-S-MB1, MB2, EYE1, EYE2, CHF1, TUB1, SW1, PIN1 | MB1 (catalog From/$ examples); MB2 (ADC FATH band via Mech); EYE1 ($0.78); EYE2 (PowerNet via Soft); TUB1 (NITRA via Soft/Mech) | **CHF1** unit $ NOT IN SOURCE this session; **SW1/PIN1** pointer-only; Festo PUN-H unit $ NOT PUBLICLY LISTED; exact mock net $ NOT IN SOURCE |

---

## 3. Cross-ref map (do not re-own)

| Mechanical / Controls ID | Soft relationship |
|---|---|
| OB-M1 Pin class | Soft: chafe keep-out vs pin/flag only |
| OB-M2 Pitch plate | Soft: hose pinch / flag travel keep-out |
| OB-M3 Bushing/bearing | Soft: none primary — wait FEA (Lead) |
| OB-M4 Bumper | Soft: none primary — Mech after mass props |
| OB-M5 Boot shell | Soft deepens **mock path** OB-S-MB1; Lead owns structure |
| OB-M6 Fasteners | Soft mock fasteners OB-S-MB2; structural stays Mech |
| OB-M7 Flex-loop tube | Soft OB-S-TUB1 pointer + bend keep-outs |
| OB-S1 Switch (Elias) | Soft bit coupling only |

**Spend reminder (Lead):** When Stephen opens spend, Mech fixture kit (OB-M1…M7 samples) is a **separate** band from Soft TB-01/TB-02. **No PO from this paper.**

---

## 4. ASSUMPTIONS (plain sight)

1. **ASSUMPTION:** DFMEA S/O/D remain blank until Lead analysis path.  
2. **ASSUMPTION:** Chafe sleeve PN class TBD Soft DFM — family only here.  
3. **ASSUMPTION:** Public $ snapshots may change; re-verify before any future requisition.  
4. **ASSUMPTION:** Soft Blender soft-body remakes are not required for DFMEA/BOM deepen.  
5. **ASSUMPTION:** C-01 Soft coupon lane is parallel and **out of scope** for this packet.

---

## 5. Non-claims

- **No PO.** Critical **B-06 OPEN**.  
- **No RPN / no invented severity.**  
- **No invented** force / pressure / life / N·m / FEA PASS.  
- Does not re-primary Elias switch or Mech structural pricing.  
- Does not touch NEXT_PROMPT.  
- Does not expand into C-01 Soft coupon spend.

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT — ready for Lead review |
| Critical B-06 | **OPEN** |
| PO | **None** |
| Research date | 2026-09-21 ET |

— Ismael · Soft Robotics Desk · MYORGLAB · draft for Ola disposition
