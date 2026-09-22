# ISMAEL — Soft-Arm Neo-Hookean / Chamber P→Strain→Bend Pack (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Disposition** | PAPER — **DESIGN ESTIMATE** / pedagogy equations only |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** (Lead) |
| **PO** | **NONE** — $0 |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md` |

**Cites (do not overwrite ACCEPTED-A sources):**  
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` (ACCEPTED-A DESIGN ESTIMATE);  
`ENGINEERING_ASSESSMENT_ISMAEL_VIRTUAL_SOFT_PHYSICS_2026-09-21.md` (Ola ACCEPTED-A);  
`ISMAEL_VIRTUAL_SOFT_ARM_TWIN_DEEPEN_2026-09-21.md`;  
`ISMAEL_DIGITAL_TRACK_B_PREP.md`.

**Standing rule:** Every numeric prediction tagged **ASSUMPTION** / **DESIGN ESTIMATE** / **HYPOTHESIS** in plain sight. DESIGN ESTIMATE ≠ System ID. Catalog TDS + masses OK when cited. Do **not** invent measured lab pressure/strain/force/cycle life.

**Architecture locks honored:** 8 chambers (U1–U3, F1–F3, T1–T2); textile strain limit; elastic return; no distal metal; Option A stand-off; Option B pitch; Soft TB ≠ Mech OB-M5.

---

## Summary

Pedagogy pack that maps Smooth-On **TDS ASSUMPTION** elastomer params → Neo-Hookean shear modulus μ → chamber pressure → wall stretch → continuum bend curvature under explicit free-body idealizations. Extends ACCEPTED-A Ecoflex 00-30 / Dragon Skin 30 map with **Dragon Skin 10 MEDIUM** and **Dragon Skin 20** TDS rows (access 2026-09-21 ET). Includes twin `p_norm` map and tip force/impulse **ORDER-OF-MAGNITUDE HYPOTHESIS** under glove-mass **ASSUMPTION**. **No System ID PASS. No PO. C-01 and B-06 remain OPEN.**

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| NH-01 | Critical OPEN | No measured P→ε — C-01 stays OPEN; this pack is DESIGN ESTIMATE only. |
| NH-02 | High (process) | TDS 100% modulus → Neo-Hookean μ is an **ASSUMPTION** bridge (ACCEPTED-A §1.3), not a lab fit. |
| NH-03 | Med | Textile-limited strain clamps useful stretch; bare-elastomer ΔP bands understate sleeved ΔP **HYPOTHESIS**. |
| NH-04 | Med | Force / impulse rows are **HYPOTHESIS** order-of-magnitude — **not** Track C System ID. |
| NH-05 | Info | DS10 / DS20 added as comparative TDS ranking; primary cast path remains Ecoflex 00-30 + optional DS30 (prior Soft locks). |
| NH-06 | Info | Soft TB ≠ Mech OB-M5; twin morph ≠ ID (Ola VSP-01/03). |

---

## Equations (markdown / KaTeX-friendly)

### E1 — Unit conversion (**ASSUMPTION** arithmetic constant)

\[
1\,\mathrm{psi} = 6894.757\,\mathrm{Pa}
\]

### E2 — Neo-Hookean uniaxial engineering stress (**ASSUMPTION** constitutive bridge)

Incompressible Neo-Hookean:

\[
\sigma_{\mathrm{eng}} = 2 C_1 \left(\lambda - \lambda^{-2}\right),\qquad \mu = 2 C_1
\]

At TDS “100% modulus” stretch \(\lambda = 2\):

\[
\sigma_{\mathrm{eng}}(100\%) = 3.5\,C_1 \quad\Rightarrow\quad C_1 = \frac{\sigma_{\mathrm{eng}}}{3.5},\quad \mu = 2 C_1,\quad E \approx 3\mu
\]

**ASSUMPTION:** Smooth-On “100% modulus” = engineering stress at \(\lambda=2\) on unconstrained ASTM coupon (not sleeved actuator).

### E3 — Thin-wall hoop idealization (**ASSUMPTION** — bare tube, no textile)

\[
\sigma_{\mathrm{hoop}} = \Delta P\,\frac{r}{t}\quad\Rightarrow\quad \Delta P = \sigma\,\frac{t}{r}
\]

### E4 — Pneumatic moment → curvature → tip bend (**ASSUMPTION** continuum free-body)

\[
M = \Delta P\, A_{\mathrm{ch}}\, e,\qquad A_{\mathrm{ch}}=\pi r_{\mathrm{ch}}^{2},\qquad e = 0.55\,R_{\mathrm{sec}}
\]

\[
EI_{\mathrm{eff}} = \eta\, E\, I,\qquad I = \frac{\pi}{4} R_{\mathrm{sec}}^{4},\qquad \eta \in [0.20, 0.35]
\]

\[
\kappa = \frac{M}{EI_{\mathrm{eff}}},\qquad \theta = \kappa L,\qquad \delta = R_{\mathrm{curv}}(1-\cos\theta),\quad R_{\mathrm{curv}}=1/\kappa
\]

### E5 — Wall stretch estimate under membrane stress (**DESIGN ESTIMATE** pedagogy)

For small-to-moderate stretch, engineering strain order:

\[
\varepsilon_{\mathrm{eng}} \sim \frac{\sigma_{\mathrm{hoop}}}{E_{\mathrm{eff}}},\qquad \lambda \approx 1 + \varepsilon_{\mathrm{eng}}
\]

With textile: clamp \(\lambda \le \lambda_{\max}\) (**DESIGN ASSUMPTION** planning 1.10 baseline; also 1.05 / 1.15).

### E6 — Twin `p_norm` map (**HYPOTHESIS** editable constant — not product working P)

\[
\Delta P = p_{\mathrm{norm}} \cdot \Delta P_{\mathrm{map}},\qquad p_{\mathrm{norm}}\in[0,1]
\]

Planning maps (from ACCEPTED-A twin deepen / physics §6): Ecoflex-class \(\Delta P_{\mathrm{map}}\approx 40\,\mathrm{kPa}\); DS30-class \(\approx 100\,\mathrm{kPa}\).

### E7 — Tip force / impulse **ORDER-OF-MAGNITUDE HYPOTHESIS** (not System ID)

Cantilever tip stiffness and quasi-static tip force at deflection \(\delta\):

\[
k_{\mathrm{eff}} \approx \frac{3\,EI_{\mathrm{eff}}}{L^{3}},\qquad F_{\mathrm{tip}} \sim k_{\mathrm{eff}}\,\delta
\]

Impulse order if contact duration \(t_c\) (**ASSUMPTION** contact time class — **not** measured):

\[
J \sim F_{\mathrm{tip}}\, t_c \quad\text{or}\quad J \sim m_{\mathrm{glove}}\, \Delta v
\]

**Explicit:** rows below are **HYPOTHESIS** for planning envelopes only — **not** Track C ID, **not** FEA PASS.

---

## Material params from Smooth-On TDS (**TDS ASSUMPTION** / **DESIGN ESTIMATE**)

**Sources + access date 2026-09-21 ET:**

| Bulletin / page | URL |
|---|---|
| Ecoflex™ Series TB (PDF) | https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf |
| Ecoflex™ 00-30 Data At-A-Glance | https://www.smooth-on.com/products/Ecoflex-00-30/ |
| Dragon Skin™ Series TB (PDF) | https://www.smooth-on.com/tb/files/DRAGON_SKIN_SERIES_TB.pdf |
| Dragon Skin™ 10 MEDIUM | https://www.smooth-on.com/products/dragon-skin-10-medium/ |
| Dragon Skin™ 20 | https://www.smooth-on.com/products/dragon-skin-20/ |
| Dragon Skin™ 30 (ACCEPTED-A primary comparative) | https://www.smooth-on.com/products/dragon-skin-30/ |

**ASSUMPTION:** All TDS values = unconstrained ASTM coupons after 7 days at 73°F/23°C — **not** sleeved pneumatic actuator P→ε.

| Material | Shore (TDS) | Specific gravity (TDS) | 100% modulus (TDS) | \(\sigma_{\mathrm{eng}}\) SI | \(C_1\) | \(\mu\) | \(E\approx 3\mu\) | Tag |
|---|---|---|---|---|---|---|---|---|
| Ecoflex™ 00-30 | 00-30 | **1.07 g/cc** | **10 psi** | 68.948 kPa | 19.699 kPa | **39.399 kPa** | **0.118 MPa** | **DESIGN ESTIMATE** from TDS |
| Dragon Skin™ 10 MEDIUM | 10A | **1.07 g/cc** | **22 psi** | 151.685 kPa | 43.338 kPa | **86.677 kPa** | **0.260 MPa** | **DESIGN ESTIMATE** from TDS |
| Dragon Skin™ 20 | 20A | **1.08 g/cc** | **49 psi** | 337.843 kPa | 96.527 kPa | **193.053 kPa** | **0.579 MPa** | **DESIGN ESTIMATE** from TDS |
| Dragon Skin™ 30 | 30A | **1.08 g/cc** | **86 psi** | 592.949 kPa | 169.4 kPa | **338.8 kPa** | **1.02 MPa** | **DESIGN ESTIMATE** (ACCEPTED-A) |

**DESIGN ESTIMATE ranking:** \(E_{\mathrm{DS30}}/E_{\mathrm{Eco}}\approx 8.6\times\); \(E_{\mathrm{DS20}}/E_{\mathrm{Eco}}\approx 4.9\times\); \(E_{\mathrm{DS10}}/E_{\mathrm{Eco}}\approx 2.2\times\).

**NOT IN SOURCE on TDS:** Mooney–Rivlin \(C_2\), Prony viscoelasticity, textile composite law, actuator working P, cycle life.

---

## Chamber pressure → wall stretch → bend (**DESIGN ESTIMATE**)

### Geometry inputs (**ASSUMPTION** / **GEOMETRY TARGET** — not measured Soft OD)

From ACCEPTED-A physics / digital prep:

| Item | Value | Tag |
|---|---|---|
| Mid lengths | \(L_U=0.410\,\mathrm{m}\), \(L_F=0.310\,\mathrm{m}\), \(L_{U+F}=0.720\,\mathrm{m}\) | **ASSUMPTION** arithmetic mid of GEOMETRY TARGET paths |
| Section radius class | \(R_{\mathrm{sec}}\in\{35,45,55\}\,\mathrm{mm}\); baseline **45 mm** | **ASSUMPTION** |
| Chamber packing | \(r_{\mathrm{ch}}=R_{\mathrm{sec}}/2.2\); \(e=0.55\,R_{\mathrm{sec}}\); \(\eta\in[0.20,0.35]\) | **ASSUMPTION** |
| Bladder \((r,t)\) cases | (20/3), (30/4), (40/5) mm | **ASSUMPTION** planning geometry class |
| Textile \(\lambda_{\max}\) | 1.05 / **1.10** / 1.15 | **DESIGN ASSUMPTION** |

### Bare thin-wall ΔP @ mid \((r,t)=(30,4)\) mm — **DESIGN ESTIMATE**

Target \(\sigma \in \{0.25,0.5,1.0\}\times\) (TDS 100% modulus):

| Material | σ @ 0.5×mod100 | ΔP mid | Tag |
|---|---|---|---|
| Ecoflex 00-30 | 34.5 kPa | **~4.6 kPa (0.67 psi)** | **DESIGN ESTIMATE** |
| DS10 MEDIUM | 75.8 kPa | **~10.1 kPa** | **DESIGN ESTIMATE** |
| DS20 | 169 kPa | **~22.5 kPa** | **DESIGN ESTIMATE** |
| DS30 | 296 kPa | **~40 kPa** | **DESIGN ESTIMATE** (ACCEPTED-A) |

### Sleeved / textile-limited ΔP **HYPOTHESIS** (raise vs bare; **not** product working P)

| Candidate | Planning ΔP **HYPOTHESIS** | Tag |
|---|---|---|
| Ecoflex 00-30 + textile | **~10–80 kPa (~1.5–12 psi)** | **HYPOTHESIS / DESIGN ESTIMATE** — overwrite TB-01 |
| DS10 / DS20 + textile | **~20–120 kPa** (interpolate Eco↔DS30 ranks) | **HYPOTHESIS** — overwrite TB-01 |
| Dragon Skin 30 + textile | **~30–150 kPa (~4–22 psi)** | **HYPOTHESIS / DESIGN ESTIMATE** (ACCEPTED-A) |

### Wall stretch at ASSUMPTION pressures — **DESIGN ESTIMATE**

| Case | Idealization | Result | Tag |
|---|---|---|---|
| Bare Ecoflex, ΔP=5 kPa, (30/4) | \(\sigma=P r/t=37.5\,\mathrm{kPa}\); \(\varepsilon\sim\sigma/E\) | \(\varepsilon\sim 0.32\) (\(\lambda\sim 1.32\)) — **outside** textile clamp | **DESIGN ESTIMATE** pedagogy |
| Textile clamp | \(\lambda\le 1.10\) | Useful axial ≤ ~10% regardless of bare prediction | **DESIGN ASSUMPTION** |
| Sleeved Ecoflex @ 40 kPa map | Fiber-limited; bend from differential P | Tip δ order from E4 beam analog | **DESIGN ESTIMATE** (physics §4.3) |

**Baseline bend analog (ACCEPTED-A, \(R_{\mathrm{sec}}=45\,\mathrm{mm}\), \(\eta=0.35\)) — DESIGN ESTIMATE:**

| Material | ΔP | Forearm \(L=310\,\mathrm{mm}\): \(\theta\), \(\delta\) |
|---|---|---|
| Ecoflex 00-30 | 5 kPa | **~22°, ~58 mm** |
| Ecoflex 00-30 | 15 kPa | **~65°, ~158 mm** |
| DS30 | 50 kPa | **~25°, ~67 mm** |
| DS30 | 100 kPa | **~50°, ~128 mm** |

Large \(\theta\) rows strain the linear beam analog — order-of-magnitude only; recalibrate TB-02.

### `p_norm` map (twin / pedagogy)

| `mat_class` | `dp_map_kPa` @ `p_norm=1` | Tag |
|---|---|---|
| 0 Ecoflex-class | **40** | **HYPOTHESIS / DESIGN ESTIMATE** — editable; not certified |
| 1 DS30-class | **100** | **HYPOTHESIS / DESIGN ESTIMATE** |
| (optional) DS10/20 | **60 / 80** (rank interpolate) | **HYPOTHESIS** Soft proposal |

---

## Force / impulse ORDER-OF-MAGNITUDE (**HYPOTHESIS** — not System ID)

**ASSUMPTION (glove mass):** baseline **14 oz = 0.397 kg** (public sporting-goods class; ACCEPTED-A §3). Sensitivity 12 oz = 0.340 kg; 16 oz = 0.454 kg.

**ASSUMPTION (section):** \(L=L_{U+F}=0.720\,\mathrm{m}\), \(R_{\mathrm{sec}}=45\,\mathrm{mm}\), \(\eta=0.35\).

| Material | \(EI_{\mathrm{eff}}\) | \(k_{\mathrm{eff}}\) | \(\delta\) example | \(F_{\mathrm{tip}}\sim k\delta\) | Tag |
|---|---|---|---|---|---|
| Ecoflex 00-30 | ~0.133 N·m² | ~1.07 N/m | 50 mm | **~0.05 N** | **HYPOTHESIS** OOM |
| Ecoflex 00-30 | same | same | 150 mm | **~0.16 N** | **HYPOTHESIS** OOM |
| DS30 | ~1.15 N·m² | ~9.2 N/m | 50 mm | **~0.46 N** | **HYPOTHESIS** OOM |
| DS30 | same | same | 150 mm | **~1.4 N** | **HYPOTHESIS** OOM |

**Impulse HYPOTHESIS:** if contact duration class \(t_c \in \{5, 20, 50\}\,\mathrm{ms}\) (**ASSUMPTION** — not measured):

\[
J \sim F_{\mathrm{tip}}\, t_c \quad\Rightarrow\quad \text{Ecoflex @ 0.16 N · 20 ms} \sim \mathbf{0.003\,N\cdot s};\quad \text{DS30 @ 1.4 N · 20 ms} \sim \mathbf{0.028\,N\cdot s}
\]

Alternate momentum form \(J\sim m_{\mathrm{glove}}\Delta v\): with \(\Delta v=0.5\,\mathrm{m/s}\) (**ASSUMPTION** tip-speed class — **not** measured) → \(J\sim 0.20\,\mathrm{N\cdot s}\) @ 14 oz — **different regime**; shows OOM spread until Track C instrumentation exists.

**Explicit non-claim:** These are **not** product strike force, **not** System ID, **not** FEA PASS, **not** cycle life.

---

## ASSUMPTION tables

| # | Item | Tag |
|---|---|---|
| A1 | TDS 100% modulus → Neo-Hookean μ bridge (E2) | **ASSUMPTION** |
| A2 | Densities: Eco/DS10 = 1.07 g/cc; DS20/DS30 = 1.08 g/cc | **TDS** |
| A3 | Textile \(\lambda_{\max}=1.10\) baseline | **DESIGN ASSUMPTION** |
| A4 | \(R_{\mathrm{sec}}=45\,\mathrm{mm}\), \(\eta=0.20–0.35\), packing \(r_{\mathrm{ch}}=R/2.2\) | **ASSUMPTION** |
| A5 | Glove mass baseline 14 oz = 0.397 kg | **ASSUMPTION** (catalog/public oz) |
| A6 | Sleeved ΔP bands | **HYPOTHESIS** |
| A7 | Tip force / impulse rows | **HYPOTHESIS** OOM — not System ID |
| A8 | Contact time / tip Δv classes | **ASSUMPTION** — not measured |
| A9 | Gravity, multi-chamber coupling, return-band preload omitted in bend table | **ASSUMPTION** |
| A10 | Soft TB ≠ Mech OB-M5 | Lock |

---

## Draft recommendations

1. Accept this pack as Soft **DESIGN ESTIMATE** companion deepening ACCEPTED-A virtual physics (Neo-Hookean + bend + OOM force).  
2. Keep Ecoflex 00-30 primary cast; DS10/20 as optional intermediate ranking; DS30 comparative stiff end.  
3. Recalibrate all ΔP / κ / F / J bands when TB-01…04 exist.  
4. Twin may use `p_norm` maps as editable constants only — stamp **twin ≠ ID**.  
5. Do **not** treat OOM tip force as Track C contact qualification.

---

## Test gaps

| Gap | Status |
|---|---|
| TB-01 measured P→axial strain | OPEN — C-01 |
| TB-02 κ(ΔP) / coupling | OPEN |
| TB-03 soft wrist torsion | OPEN |
| TB-04 return time history | OPEN (see vent-time pack) |
| Track C impulse / force ID | OUT OF SCOPE this Soft paper |
| Soft product-arm mass | V **NOT IN SOURCE** |

---

## Open questions for Ola

1. Accept Neo-Hookean / P→strain→bend pack as Soft DESIGN ESTIMATE deepen of ACCEPTED-A physics?  
2. Keep DS10/DS20 as comparative TDS ranking only (cast primary still Ecoflex + optional DS30)?  
3. Authorize publishing OOM tip force/impulse rows **only** as labeled HYPOTHESIS (never as System ID)?  
4. Any freeze delta to 8-chamber / Option A / elastic return / distal-metal?  
5. Preferred SoR land path OK?

---

## Non-claims

- No PO · **C-01 OPEN** · **B-06 OPEN**  
- No invented measured lab P / strain / force / cycle life  
- DESIGN ESTIMATE ≠ System ID · twin ≠ ID  
- Soft TB ≠ Mech OB-M5 · no NEXT_PROMPT write

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Label | **DESIGN ESTIMATE** |
| Critical C-01 / B-06 | **OPEN** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-21 ET · awaiting Ola disposition —
