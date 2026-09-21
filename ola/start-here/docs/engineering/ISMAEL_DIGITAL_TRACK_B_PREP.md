> **Ola integrate 2026-09-21: ACCEPTED-A (digital Soft Track B paper gate).** Provisional TDS bands allowed for planning only — never substitute for TB-01…04. Soft Track B paper gate = this doc + TRACK_B_SYSTEM_ID_PLAN. Physical coupons still required before any System ID claim.

# Track B — PAPER-ONLY Digital V&V Prep (Ismael / Soft Robotics)

**Author:** Ismael (Soft Robotics Desk) · MYORGLAB AI boxing trainer  
**Date:** 2026-09-21 ET  
**Disposition:** DRAFT paper prep for Ola — **not** coupon System ID; **not** a purchase order; **not** a freeze change  
**SoR staging target:** `docs/engineering/ISMAEL_DIGITAL_TRACK_B_PREP.md`  
**Upstream plans:** `docs/engineering/TRACK_B_SYSTEM_ID_PLAN.md` (skimmed from box mirror of SoR); continuum / envelope docs cited below  

### Disposition locks (do not re-ask)
- **Freeze:** 8 chambers/arm (U1–U3, F1–F3, T1–T2); textile strain limit; elastic return; soft wrist; **no distal metal**; **Option A stand-off** (no arm lengthening)
- **First coupons:** TB-01 / TB-02 = **in-house Smooth-On Ecoflex / Dragon Skin cast path** (when Stephen spend opens — this paper authorizes **no PO**)
- Prefer **TB-*** IDs; Track A films **never** close System ID
- Soft-termination = **ICD notes only**; **Critical B-06 stays Lead (Ola)**
- Coupon tube **provisional:** NITRA 6 mm or 1/4″; production preference **Festo PUN-H** (context only — not a buy)
- Do **not** overwrite `chats/NEXT_PROMPT.md`

---

## Purpose

Define what digital / literature preparatory work can bound Soft Track B **before** physical coupons, without inventing measured System ID, working pressures for the boxing arm, or product-arm mass.

**This document = digital prep.**  
**Digital prep ≠ Track B close.**  
**Digital prep ≠ Track C contact.**

---

## 1) Virtual test matrix — flexibility / elastic return / chamber coupling

### 1.1 What can be *simulated or bounded* from public elastomer datasheets (FEA / analytic / order-of-magnitude)

All rows below use **unconstrained ASTM coupon-class properties** from Smooth-On technical bulletins (Shore, 100% modulus, tensile, elongation @ break, specific gravity). They support **planning envelopes and relative ranking**, not identified P→ε for textile-sleeved pneumatic chambers.

| Row ID | Phenomenon | Digital method (paper) | Datasheet inputs usable | Bound / output class | Maps to physical TB |
|---|---|---|---|---|---|
| V-FLEX-01 | Relative elastomer compliance ranking (Ecoflex class vs Dragon Skin class) | Analytic compare of Shore + 100% modulus; optional hyperelastic (Neo-Hookean / Mooney–Rivlin) **parameter estimation from TDS 100% modulus + elongation only as sensitivity study** | Shore; 100% modulus; elongation @ break | Relative stiffness band — **PROVISIONAL — not coupon System ID** | Informs material choice for TB-01 cast path |
| V-FLEX-02 | Order-of-magnitude solid-wall membrane strain under **arbitrary** internal pressure (unconstrained tube / plate idealizations) | Thin-wall / thick-wall Lamé or FEA of **generic** sleeved-bladder *geometry class* once coupon mold dims exist | Tensile; 100% modulus; elongation @ break as failure screen | **Sensitivity only** — must re-run with measured coupon geometry | TB-01 prep (does **not** replace TB-01) |
| V-COUP-01 | Qualitative multi-chamber coupling topology | Kinematic / free-body sketch: common-mode axial vs differential bend; isolated branch topology (no serial U→F air) | Architecture freeze only (not TDS) | Topology checklist for FEA mesh / sensor plan | TB-02 design intent |
| V-RET-01 | Elastic return **concept** bound | Stored-strain argument: return work from stretched textile/elastomer, not suction; limp bladder cannot pull | TDS “rebounds to original form without distortion” (qualitative Ecoflex series language) + continuum intent | Qualitative fault/vent narrative — **no τ_return invented** | TB-04 prep narrative |
| V-MASS-01 | Soft-module mass **method** (see §3) | \( m = V \times \rho \) with TDS specific gravity | Specific gravity / density | Symbolic or GEOMETRY-TARGET envelope only | BOM / fixture load planning — not System ID |
| V-GEO-01 | Coupon length envelope from SoR **GEOMETRY TARGET** path lengths | Use envelope audit centerline ranges as **targets for coupon fixture length**, not as measured strain | Envelope audit lengths (see §3) | Coupon fixture sizing only | TB-01…TB-03 coupon envelopes |

**Explicit digital limits**
- Smooth-On TDS gives **bulk elastomer ASTM properties**, not pneumatic-actuator pressure→strain maps.
- Textile sleeve registration, fiber angle, neck bond, return-band preload, gravity, and glove-like tip load are **NOT IN SOURCE** on the TDS → FEA without those layers is **illustrative**.
- Do **not** publish a boxing-arm working pressure, tip velocity, or impulse from digital prep alone.

### 1.2 What **requires** physical TB-01…TB-04 coupons (and why)

| Physical ID | Objective (from Track B plan) | Why digital / TDS cannot close | First-coupon material path |
|---|---|---|---|
| **TB-01** | P → axial strain on one sleeved bladder; vent return characterized | Actuator geometry + textile restraint dominate; TDS has **no** P→ε for sleeved bladders (**NOT IN SOURCE** for actuator P–ε) | In-house **Smooth-On Ecoflex / Dragon Skin** cast bladder + textile sleeve |
| **TB-02** | Differential 3-chamber section bend (U or F); tip angle / curvature vs ΔP; coupling noted | Chamber–chamber mechanical and pneumatic coupling, registration, and buckling under gravity are manufacturing- and fixture-specific | Same cast path for section coupon |
| **TB-03** | Soft wrist T1/T2 twist under glove-like load; no metal shaft | Torsion polarity, hysteresis, unwanted length change — not on elastomer TDS | Soft cuff / opposite-handed torsion coupon (cast + textile); **after** TB-01/TB-02 first band unless Ola reorders |
| **TB-04** | Elastic return / snapback on vent; fault-vent policy inputs | Time history of tip return depends on return bands + vent conductance + mass distribution — **not** TDS rebound sentence | Instrumented vent on prior coupons / return-band sample |

**Ladder reminder (Track B plan):** single sleeved bladder → 3-chamber section → soft torsion wrist → (optional) two-section continuum on guarded fixture. Advancement to Track C only after TB-01…TB-04 evidence packages exist.

### 1.3 Matrix map — virtual rows → TB coupons

| Virtual row | Closes digitally? | Feeds physical |
|---|---|---|
| V-FLEX-01 | Partial (material ranking only) | **TB-01** material selection |
| V-FLEX-02 | No — sensitivity only | **TB-01** FEA prep / fixture pressure-range *hypothesis* (must be overwritten by measured ID) |
| V-COUP-01 | Topology only | **TB-02** instrumentation & registration plan |
| V-RET-01 | Narrative only | **TB-04** test protocol framing |
| V-MASS-01 | Method only | Fixture / handling; not TB close |
| V-GEO-01 | GEOMETRY TARGET sizing | Coupon free length envelopes for **TB-01 / TB-02 / TB-03** |

---

## 2) Provisional pressure/strain literature bands (Ecoflex / Dragon Skin class)

**Rule:** Cite **Smooth-On TDS only**. Every numeric property below is **PROVISIONAL — not coupon System ID**.  
**Do not invent working pressures for the boxing arm.**

### 2.1 Sources fetched (official Smooth-On)

| Product / bulletin | URL fetched |
|---|---|
| Ecoflex™ Series Technical Bulletin (PDF) | https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf |
| Ecoflex™ 00-30 product page (Data At-A-Glance) | https://www.smooth-on.com/products/Ecoflex-00-30/ |
| Dragon Skin™ Series Technical Bulletin (PDF) | https://www.smooth-on.com/tb/files/DRAGON_SKIN_SERIES_TB.pdf |
| Dragon Skin™ 30 product page (Data At-A-Glance) | https://www.smooth-on.com/products/dragon-skin-30/ |

TDS note (both series): *All values measured after 7 days at 73°F/23°C* (ASTM coupon conditions — **not** pneumatic actuator coupons).

### 2.2 Extracted TDS properties (as published)

#### Ecoflex™ 00-30 (primary soft cast candidate for TB-01/TB-02)

| Property | Value on TDS / product page | Tag |
|---|---|---|
| Mix ratio | 1A:1B by volume or weight | PROVISIONAL process — not System ID |
| Pot life | 45 min | PROVISIONAL process |
| Cure time | 4 hours | PROVISIONAL process |
| Shore hardness | **00-30** (Shore 00) | **PROVISIONAL — not coupon System ID** |
| Specific gravity | **1.07 g/cc** | **PROVISIONAL — not coupon System ID** |
| Specific volume | 26.0 cu. in./lb. | PROVISIONAL |
| Mixed viscosity | 3,000 cps | PROVISIONAL process |
| Tensile strength | **200 psi** | **PROVISIONAL — not coupon System ID** |
| **100% modulus** | **10 psi** | **PROVISIONAL — not coupon System ID** |
| Elongation @ break | **900%** | **PROVISIONAL — not coupon System ID** |
| Die B tear strength | 38 pli | PROVISIONAL |
| Shrinkage | < .001 in./in. | PROVISIONAL |
| Useful temperature range | −65°F to 450°F (−53°C to 232°C) | PROVISIONAL service envelope (material), not actuator duty cycle |

#### Dragon Skin™ 30 (stiffer cast candidate / comparative)

| Property | Value on TDS / product page | Tag |
|---|---|---|
| Mix ratio | 1A:1B by volume or weight | PROVISIONAL process |
| Pot life | 45 min | PROVISIONAL process |
| Cure time | 16 hours | PROVISIONAL process |
| Shore hardness | **30A** | **PROVISIONAL — not coupon System ID** |
| Specific gravity | **1.08 g/cc** | **PROVISIONAL — not coupon System ID** |
| Specific volume | 25.7 cu. in./lb. | PROVISIONAL |
| Mixed viscosity | 20,000 cps | PROVISIONAL process |
| Tensile strength | **500 psi** | **PROVISIONAL — not coupon System ID** |
| **100% modulus** | **86 psi** | **PROVISIONAL — not coupon System ID** |
| Elongation @ break | **364%** | **PROVISIONAL — not coupon System ID** |
| Die B tear strength | 108 pli | PROVISIONAL |
| Shrinkage | < .001 in./in. | PROVISIONAL |
| Useful temperature range | −65°F to +450°F (−53°C to +232°C) | PROVISIONAL |

#### Ecoflex series context rows (same series TB; optional cast variants — not selected)

| Grade (series TB) | Shore | Spec. gravity | Tensile | 100% mod. | Elongation | Tag |
|---|---|---|---|---|---|---|
| Ecoflex™ 00-20 | 00-20 | 1.07 | 160 psi | 8 psi | 845% | PROVISIONAL — not coupon System ID |
| Ecoflex™ 00-50 | 00-50 | 1.07 | 315 psi | 12 psi | 980% | PROVISIONAL — not coupon System ID |
| Ecoflex™ 5 | 5A | 1.07 | 350 psi | 15 psi | 1000% | PROVISIONAL — not coupon System ID |

### 2.3 What the TDS does **not** give (explicit)

| Claim type | Status |
|---|---|
| Pneumatic actuator **pressure → strain** (P–ε) for sleeved / textile-limited chambers | **NOT IN SOURCE** for actuator P–ε |
| Recommended working pressure for Ecoflex / Dragon Skin **as soft robot actuators** | **NOT IN SOURCE** |
| Boxing-arm branch working P, relief setpoints, air demand, cycle life | **NOT IN SOURCE** (Stage 0 P-01…P-07 remain OPEN) |
| Tip velocity, contact force, impulse | **NOT IN SOURCE** (Track C / C-01) |
| Textile sleeve constitutive law | **NOT IN SOURCE** on Smooth-On elastomer TDS |

**Therefore:** any “literature band” for actuator strain vs pressure must wait for **TB-01…TB-04**. Digital prep may only use TDS moduli / elongation as **material ranking and FEA sensitivity inputs**, tagged **PROVISIONAL — not coupon System ID**.

### 2.4 Order-of-magnitude interpretation (non-claiming)

- Ecoflex 00-30 **100% modulus 10 psi** vs Dragon Skin 30 **100% modulus 86 psi** → Ecoflex class is substantially more compliant at 100% stretch **in unconstrained ASTM tension** (**PROVISIONAL** ranking).
- High Ecoflex elongation (900%) vs Dragon Skin 30 (364%) suggests Ecoflex class tolerates larger free stretch before break **in TDS coupon tension** — still **not** a textile-limited chamber ID.
- **No bar / MPa working pressure** is assigned to the product arm from these numbers.

---

## 3) Mass estimate method for soft module

### 3.1 Method

\[
m_{\text{elastomer}} = V_{\text{elastomer}} \times \rho
\]

where \(\rho\) is taken from TDS **specific gravity** (g/cc ≈ g/cm³ at stated conditions):

| Material | \(\rho\) from TDS | Tag |
|---|---|---|
| Ecoflex™ 00-30 | **1.07 g/cc** | **PROVISIONAL — not coupon System ID** |
| Dragon Skin™ 30 | **1.08 g/cc** | **PROVISIONAL — not coupon System ID** |

Add textile sleeve, return bands, soft cuffs, and proximal fittings **only when their volumes/areal densities are known** — otherwise mark **NOT IN SOURCE**.

### 3.2 Unknowns → NOT IN SOURCE

| Quantity | Status |
|---|---|
| Manufactured soft-arm elastomer volume \(V\) (product) | **NOT IN SOURCE** — do **not** invent arm volume |
| Measured soft-module mass | **NOT IN SOURCE** |
| Textile / return-band mass | **NOT IN SOURCE** (no fabric areal density in Smooth-On elastomer TDS) |
| Glove + retention harness contribution | **NOT IN SOURCE** for Soft mass close |

### 3.3 Optional worked *symbolic* example only

\[
m = V \times \rho \quad\text{(e.g. Ecoflex path: } m = V \times 1.07\,\mathrm{g/cc}\text{)}
\]

No fake mm³ or grams for the **product arm** are stated here.

### 3.4 SoR GEOMETRY TARGET lengths (envelope / continuum — **not** measured mass)

From `revision_n/review_packet/ENVELOPE_GEOMETRY_AUDIT.md` (N1 live mesh audit — **prescribed film geometry**, not pneumatic travel). Use as **GEOMETRY TARGET** for coupon / fixture envelopes only:

| Item | GEOMETRY TARGET (mm) | Notes |
|---|---|---|
| Upper soft section centerline (live range) | **380.492 – 437.846** | Path length; G-02 drift vs older 403–438 doc band |
| Forearm soft section centerline (live range) | **252.171 – 368.112** | Path length |
| Soft wrist forearm-end→glove-rig at strike peaks | **105.000** | Peak only; full-frame range wider (A-05) |
| Max shoulder→wrist chord (peaks) | **≈ 858.9** | Not loaded reach / not pneumatic travel |
| Eight chambers/arm inventory | U1–U3, F1–F3, T1–T2 | Confirmed as object count — not sealed topology proof |

**These lengths are not elastomer volumes.** Converting them to \(V\) would require wall thickness, chamber OD, textile packing, and voids — **NOT IN SOURCE** → **no product-arm mass number**.

Option A stand-off: Soft DFM must **not** lengthen the arm to “fix” clearance; mass estimates must not assume a lengthened envelope.

---

## 4) Clear demarcation

| Track / artifact | Closes System ID? | Closes contact / impulse? | Role of this digital prep |
|---|---|---|---|
| **Track A** films / N1 pedagogy / twin media | **Never** | **Never** | Motion intelligibility only |
| **This digital prep** (literature + virtual matrix) | **No** | **No** | Bounds FEA inputs; plans coupons; TDS extract |
| **Track B** physical TB-01…TB-04 | **Yes — when measured** | No | Coupon P→motion ID |
| **Track C** instrumented fixture contact | No (uses B) | **Yes — when measured** | Contact / fault on fixture (no person) |
| Soft-termination ICD notes (Ismael) | No | No | Supports **Critical B-06**; **Lead retains B-06** |
| Critical **C-01** | Requires B→C | Requires C | Remains OPEN |

**One-liners for board / Stephen**
- Track A films never close these.
- Digital prep ≠ Track B close.
- Digital prep ≠ Track C contact.

---

## 5) Soft-termination ICD notes only (B-06 support — Lead retains Critical)

Paper support only — **no load ratings invented**:

1. Soft load path ends in **textile eye / soft harness** into **recessed boot**; last hard fittings stay **proximal / protected** (no distal metal per freeze).
2. ICD should name: textile-eye geometry *class*, strain-relief keep-out, hose loop keep-out at pitch hinge, peel/pull-out coupon intent when spend opens.
3. Hose pinch at pitch + textile-eye peel remain **test cases**; they **support** Critical B-06 and **do not close** it.
4. Coupon bench tube class (**provisional**): AutomationDirect **NITRA** PU **6 mm or 1/4″**; production preference **Festo PUN-H** (context from supplier scout — **no PO** from this paper).

---

## 6) ask_ola / non-claims / sources

### 6.1 ask_ola

1. Accept this paper as Soft Robotics **digital Track B prep** (literature + virtual matrix) without treating any TDS number as System ID?
2. Confirm first paid coupons remain **TB-01 + TB-02** on **in-house Smooth-On Ecoflex/Dragon Skin cast path** (vs custom molded RFQ)?
3. Confirm Ismael owns soft-termination **ICD notes only** while **Critical B-06 stays Lead**?
4. Any freeze delta to chamber count / return / Option A stand-off since rh02 continuum intent?
5. Preferred SoR landing: `docs/engineering/ISMAEL_DIGITAL_TRACK_B_PREP.md` (this file) OK?
6. Authorize digital FEA sensitivity studies using **only** TDS 100% modulus / elongation as material inputs — still tagged PROVISIONAL?

### 6.2 Non-claims

- No invented measured System ID (no P→ε curves, no tip velocity, no impulse).
- No working pressure / relief / air-demand assignment for the boxing arm.
- No purchase orders, UEI/CAGE, or budget authorization.
- No Critical B-06 or C-01 close.
- No `chats/NEXT_PROMPT.md` overwrite.
- No product soft-arm mass in grams (volume **NOT IN SOURCE**).
- Track A ≠ System ID ≠ contact qualification.

### 6.3 Sources with URLs fetched

**Smooth-On TDS (primary for §2)**  
1. https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf  
2. https://www.smooth-on.com/products/Ecoflex-00-30/  
3. https://www.smooth-on.com/tb/files/DRAGON_SKIN_SERIES_TB.pdf  
4. https://www.smooth-on.com/products/dragon-skin-30/  

**SoR / box mirrors used for locks & GEOMETRY TARGET (not measured actuator ID)**  
5. `docs/engineering/TRACK_B_SYSTEM_ID_PLAN.md` (box mirror under astra-previews ola start-here)  
6. `revision_n/review_packet/CONTINUUM_PNEUMATIC_INTENT.md` / boxing-trainer review_packet copy  
7. `revision_n/review_packet/ENVELOPE_GEOMETRY_AUDIT.md` / boxing-trainer review_packet copy  
8. Prior Ismael drafts: `ISMAEL_SOFT_ACTUATOR_FEASIBILITY_RISK_DRAFT*`, `ISMAEL_SOFT_ROBOTICS_OPEN_ITEMS_BRIEF_v2.md`, `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` (tube context only)

**Tube context only (not a buy; not System ID)**  
9. NITRA PU tubing catalog PDF — https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf  
10. Festo PUN / PUN-H family doc — https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF  

---

**— end PAPER-ONLY digital Track B prep — awaiting Ola disposition —**
