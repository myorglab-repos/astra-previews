# DISPOSITION (Ola Lead) — ACCEPTED-A 2026-09-21
Paper **DESIGN ESTIMATE** only. Assumption-label rule applied — acceptable Soft virtual physics gate.
Does **not** close C-01 / Track B; does **not** authorize PO; recalibrate on TB-01…04.
Lead locks: Ecoflex 00-30 / Dragon Skin 30 TDS path; 14 oz glove mass ASSUMPTION baseline (12–16 oz band); optional Blender soft-body / shape-key hook later if Lead asks.
Soft lane idle until Lead asks for Blender soft-body hook or new physics question.
---
# ISMAEL — Virtual Soft-Arm PHYSICS ESTIMATES (PAPER)

**Author:** Ismael (Soft Robotics Desk) · MYORGLAB AI boxing trainer  
**Date:** 2026-09-21 ET  
**Disposition:** PAPER **DESIGN ESTIMATE** only — **not** coupon System ID; **not** a purchase order; **not** a freeze change  
**SoR staging target:** `docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md`  
**Box drafts:** `/workspace/boxing-trainer/drafts/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md`  
**PC sync mirror:** `/workspace/_pc_sync/docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md`  
**Upstream:** `ISMAEL_DIGITAL_TRACK_B_PREP.md` (ACCEPTED-A digital prep geometry / TDS tables); envelope audit N1

---

## STANDING RULE (Michael / Ola) — highlight assumptions

**Highlight assumptions wherever needed, whenever we can.** Every numeric prediction below is tagged in plain sight:

| Tag | Meaning |
|---|---|
| **ASSUMPTION:** | Conversion, idealization, geometry class, or load hypothesis stated explicitly |
| **DESIGN ESTIMATE:** | Numeric prediction from arithmetic on TDS + assumptions — **recalibrate when TB-01…04 exist** |
| **DESIGN ASSUMPTION:** | Planning hypothesis not measured on this product |
| **GEOMETRY TARGET:** | Digital-prep / film path length — **not** measured soft free length or strain |
| **NOT IN SOURCE:** | Absent from Smooth-On TDS or public glove specs as used here |
| **HYPOTHESIS:** | Pressure / time band for planning only — **not** product working P |

**Never claim System ID PASS.** Track A films ≠ ID. Coupons are **not** a blocker for these estimates, but estimates **do not** close Track B.

---

## Disposition locks (do not re-ask)

- **8 chambers/arm:** U1–U3, F1–F3, T1–T2  
- **Option A stand-off** (no arm lengthening)  
- **Elastic return**; **no distal metal**; soft-term **ICD only** (Critical **B-06 Lead = Ola**)  
- Prefer **TB-*** IDs; Track A ≠ System ID  
- First cast path: **TB-01 / TB-02** in-house Smooth-On Ecoflex / Dragon Skin (this paper authorizes **no PO**)  
- Do **not** overwrite `chats/NEXT_PROMPT.md`

---

## 1) Hyperelastic continuum estimate from Smooth-On TDS

### 1.1 Sources fetched (official)

| Bulletin | URL |
|---|---|
| Ecoflex™ Series Technical Bulletin (PDF) | https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf |
| Dragon Skin™ Series Technical Bulletin (PDF) | https://www.smooth-on.com/tb/files/DRAGON_SKIN_SERIES_TB.pdf |

**ASSUMPTION:** TDS values are **unconstrained ASTM coupon** properties after 7 days at 73°F/23°C — **not** sleeved pneumatic actuator P→ε.

### 1.2 Primary candidates (TB-01/02 cast path)

| Property | Ecoflex™ 00-30 | Dragon Skin™ 30 | Tag |
|---|---:|---:|---|
| Shore | 00-30 | 30A | TDS (source URLs above) |
| Specific gravity | 1.07 | 1.08 | TDS |
| Tensile strength | **200 psi** | **500 psi** | TDS |
| **100% modulus** | **10 psi** | **86 psi** | TDS |
| Elongation @ break | 900% | 364% | TDS |

**Conversion used everywhere below:**

\[
1\,\mathrm{psi} = 6894.757\,\mathrm{Pa}
\]

| Material | 100% modulus (TDS) | SI |
|---|---:|---|
| Ecoflex 00-30 | 10 psi | **DESIGN ESTIMATE:** \(10 \times 6894.757 = \mathbf{68.948\,\mathrm{kPa}}\) engineering stress at 100% elongation |
| Dragon Skin 30 | 86 psi | **DESIGN ESTIMATE:** \(86 \times 6894.757 = \mathbf{592.949\,\mathrm{kPa}}\) |

### 1.3 Neo-Hookean map — **ASSUMPTION** stated

**ASSUMPTION (Neo-Hookean / small-strain bridge):**

1. Smooth-On “100% modulus” = **engineering stress** \(\sigma_{\mathrm{eng}}\) at stretch \(\lambda = 2\) (100% elongation).  
2. Incompressible Neo-Hookean uniaxial law:
   \[
   \sigma_{\mathrm{eng}} = 2 C_1 \left(\lambda - \lambda^{-2}\right)
   \]
   At \(\lambda=2\): \(\sigma_{\mathrm{eng}} = 2 C_1 (2 - 1/4) = 3.5\,C_1\) ⇒ \(C_1 = \sigma_{\mathrm{eng}}/3.5\).  
3. Shear modulus \(\mu = 2 C_1\).  
4. Incompressible small-strain Young’s modulus \(E \approx 3\mu\).

**Worked — Ecoflex 00-30**

\[
\begin{aligned}
\sigma_{\mathrm{eng}}(100\%) &= 68.948\,\mathrm{kPa} \\
C_1 &= 68.948 / 3.5 = \mathbf{19.699\,\mathrm{kPa}} \quad \text{(**DESIGN ESTIMATE**)} \\
\mu &= 2 C_1 = \mathbf{39.399\,\mathrm{kPa}} \quad \text{(**DESIGN ESTIMATE**)} \\
E &\approx 3\mu = \mathbf{118.2\,\mathrm{kPa}} = \mathbf{0.118\,\mathrm{MPa}} \quad \text{(**DESIGN ESTIMATE**)}
\end{aligned}
\]

**Worked — Dragon Skin 30**

\[
\begin{aligned}
\sigma_{\mathrm{eng}}(100\%) &= 592.949\,\mathrm{kPa} \\
C_1 &= 592.949 / 3.5 = \mathbf{169.4\,\mathrm{kPa}} \quad \text{(**DESIGN ESTIMATE**)} \\
\mu &= 2 C_1 = \mathbf{338.8\,\mathrm{kPa}} \quad \text{(**DESIGN ESTIMATE**)} \\
E &\approx 3\mu = \mathbf{1016\,\mathrm{kPa}} = \mathbf{1.02\,\mathrm{MPa}} \quad \text{(**DESIGN ESTIMATE**)}
\end{aligned}
\]

**DESIGN ESTIMATE:** stiffness ratio \(E_{\mathrm{DS30}} / E_{\mathrm{Ecoflex}} \approx \mathbf{8.6\times}\) (same conversion assumptions).

**NOT IN SOURCE:** Mooney–Rivlin \(C_2\), viscoelastic Prony series, textile–elastomer composite law, or actuator P→ε.

---

## 2) Textile as strain-limiting shell

**ASSUMPTION (textile idealization):** circumferential / helical fibers are **much stiffer** than the elastomer → anisotropic shell: hoop nearly inextensible; elastomer provides soft axial / bending compliance between fiber lock-up.

**DESIGN ASSUMPTION (not measured):** fiber-limited max axial extension ratio on a sleeved chamber

| \(\lambda_{\max}\) hypothesis | Engineering \(\varepsilon_{\mathrm{axial}}\) | Tag |
|---:|---:|---|
| 1.05 | ~5% | **DESIGN ASSUMPTION** |
| 1.10 | ~10% | **DESIGN ASSUMPTION** (baseline planning) |
| 1.15 | ~15% | **DESIGN ASSUMPTION** |

**NOT IN SOURCE on Smooth-On TDS:** fabric areal density, braid angle, weave lock-up, sleeve registration, return-band preload.

**Qualitative effect:** without textile, Ecoflex could stretch hundreds of percent (TDS elongation 900%); **with** textile, useful chamber strain is **fiber-limited**, so tip bend comes from **differential chamber pressure** and geometry, not bulk free stretch. EI_eff rises vs bare elastomer → **higher ΔP** needed for the same tip motion than bare thin-wall hoop estimates alone.

---

## 3) Industry-standard boxing glove mass

### 3.1 Public sporting-goods band (12–16 oz)

Labeled glove “oz” = **total glove mass** (padding + shell + lining + closure), not padding alone.

| Label | Mass (exact oz→g) | **DESIGN ESTIMATE** SI | Typical use (public guides) |
|---|---:|---:|---|
| 12 oz | 340.2 g | **0.340 kg** | bag / pads / lighter training |
| 14 oz | 396.9 g | **0.397 kg** | general training |
| 16 oz | 453.6 g | **0.454 kg** | sparring / conditioning standard in many gyms |

Conversion: \(1\,\mathrm{oz} = 28.3495\,\mathrm{g}\).

**Cites (public):**

- https://muaythai-world.com/ounces-boxing-gloves-weight-sizes/ — 12 oz ≈ 340.2 g; 16 oz ≈ 453.6 g  
- https://fitset.com.au/blogs/news/12oz-vs-16oz-boxing-gloves-guide — ~340 g vs ~450 g; 4 oz ≈ 113 g difference  
- https://www.boxfituk.com/blogs/blog/understanding-boxing-glove-sizes-and-weights — 8 oz ≈ 227 g; 16 oz ≈ 454 g  
- https://blogs.rdxsports.com/what-does-the-oz-mean-in-boxing-gloves/ — 16 oz ≈ 454 g  

**ASSUMPTION (glove mass for all tip dynamics below):** parametric tip mass \(m_{\mathrm{glove}}\) with **baseline 14 oz = 0.397 kg** unless a row says otherwise. Product retention harness / soft wrist mass is **NOT IN SOURCE** — optional add-on called out separately.

### 3.2 Sensitivity (lighter / heavier)

| \(m_{\mathrm{glove}}\) | Mass | Relative to 14 oz |
|---|---:|---:|
| 8 oz (sensitivity) | 0.227 kg | 0.57× |
| **12 oz** | **0.340 kg** | 0.86× |
| **14 oz (baseline)** | **0.397 kg** | 1.00× |
| **16 oz** | **0.454 kg** | 1.14× |
| 18 oz (sensitivity) | 0.510 kg | 1.29× |

---

## 4) Virtual outputs — all **DESIGN ESTIMATE** / recalibrate at TB-01…04

### 4.1 Geometry inputs (TARGETS — not measured soft lengths)

From ACCEPTED-A digital prep / N1 envelope audit (`ENVELOPE_GEOMETRY_AUDIT.md`, mirrored in `ISMAEL_DIGITAL_TRACK_B_PREP.md`):

| Item | **GEOMETRY TARGET** | Tag |
|---|---|---|
| Upper soft section centerline | **380–438 mm** (live 380.492–437.846) | path length — **not** elastomer free length |
| Forearm soft section centerline | **252–368 mm** (live 252.171–368.112) | path length |
| Wrist forearm-end→glove-rig at strike peaks | **105 mm** | peak only; inter-peak wider (A-05) |
| Max shoulder→wrist chord | **≈ 859 mm** (858.915) | not loaded reach / not pneumatic travel |
| Chamber inventory | 8/arm (U1–U3, F1–F3, T1–T2) | object count ≠ sealed topology proof |

**ASSUMPTION (arithmetic mid-lengths used below):** \(L_U = 0.410\,\mathrm{m}\), \(L_F = 0.310\,\mathrm{m}\), \(L_W = 0.105\,\mathrm{m}\), continuum \(L_{U+F} = 0.720\,\mathrm{m}\).

**ASSUMPTION (section radius class — NOT measured soft OD):** continuum core \(R_{\mathrm{sec}} \in \{35, 45, 55\}\,\mathrm{mm}\); baseline rows use **\(R_{\mathrm{sec}} = 45\,\mathrm{mm}\)**.

**ASSUMPTION (3-chamber packing):** chamber radius \(r_{\mathrm{ch}} = R_{\mathrm{sec}}/2.2\); moment arm \(e = 0.55\,R_{\mathrm{sec}}\); stiffness knockdown \(\eta \in [0.20, 0.35]\) for voids + textile (planning band).

### 4.2 Chamber pressure band **HYPOTHESES** (useful membrane stress order)

Thin-wall hoop idealization (**ASSUMPTION** — unconstrained tube, no textile yet):

\[
\sigma_{\mathrm{hoop}} = \Delta P \,\frac{r}{t} \quad\Rightarrow\quad \Delta P = \sigma \,\frac{t}{r}
\]

**ASSUMPTION:** “useful” membrane stress targets \(\sigma \in \{0.25, 0.5, 1.0\} \times\) (TDS 100% modulus).  
**ASSUMPTION:** bladder \((r,t)\) cases (20/3), (30/4), (40/5) mm — **planning geometry class**, not cast mold dims.

#### Bare-elastomer thin-wall ΔP (**DESIGN ESTIMATE** arithmetic)

| Material | Target σ | Mid case \(r=30\,\mathrm{mm},\,t=4\,\mathrm{mm}\) ΔP |
|---|---|---|
| Ecoflex 00-30 | 0.25× mod100 (17.2 kPa) | **~2.3 kPa (0.33 psi)** |
| Ecoflex 00-30 | 0.5× mod100 (34.5 kPa) | **~4.6 kPa (0.67 psi)** |
| Ecoflex 00-30 | 1.0× mod100 (68.9 kPa) | **~9.2 kPa (1.3 psi)** |
| Dragon Skin 30 | 0.25× mod100 (148 kPa) | **~20 kPa (2.9 psi)** |
| Dragon Skin 30 | 0.5× mod100 (296 kPa) | **~40 kPa (5.7 psi)** |
| Dragon Skin 30 | 1.0× mod100 (593 kPa) | **~79 kPa (11.5 psi)** |

Full \(r,t\) sweep (same formulas): Ecoflex bare band **~2–10 kPa**; DS30 bare band **~19–89 kPa** across the three geometries and three σ targets.

**HYPOTHESIS — sleeved / textile-limited planning bands** (raise ΔP vs bare because EI_eff↑ and fiber lock limits stretch; **still NOT product working P**):

| Candidate | Planning ΔP **HYPOTHESIS** | Tag |
|---|---|---|
| Ecoflex 00-30 + textile | **~10–80 kPa (~1.5–12 psi)** | **HYPOTHESIS / DESIGN ESTIMATE** — overwrite with TB-01 |
| Dragon Skin 30 + textile | **~30–150 kPa (~4–22 psi)** | **HYPOTHESIS / DESIGN ESTIMATE** — overwrite with TB-01 |

**Explicit:** these are **not** Stage 0 P-01…P-07 setpoints and **not** boxing-arm certified working pressures. **NOT IN SOURCE** as Smooth-On recommended actuator pressures.

### 4.3 Tip deflection / bend under ΔP — continuum / beam analog

**ASSUMPTION (pneumatic moment, one chamber of a 3-chamber section):**

\[
M = \Delta P \, A_{\mathrm{ch}} \, e,\qquad A_{\mathrm{ch}}=\pi r_{\mathrm{ch}}^{2},\qquad e=0.55\,R_{\mathrm{sec}}
\]

**ASSUMPTION (effective bending stiffness):**

\[
EI_{\mathrm{eff}} = \eta \, E \, I,\qquad I = \frac{\pi}{4} R_{\mathrm{sec}}^{4}
\]

with \(E\) from §1.3 Neo-Hookean map; \(\eta\) = void/textile knockdown.

Curvature and tip motion (circular-arc analog):

\[
\kappa = \frac{M}{EI_{\mathrm{eff}}},\qquad \theta = \kappa L,\qquad \delta = R_{\mathrm{curv}}\bigl(1-\cos\theta\bigr),\quad R_{\mathrm{curv}}=1/\kappa
\]

#### Baseline section \(R_{\mathrm{sec}}=45\,\mathrm{mm}\), \(\eta=0.35\) — **DESIGN ESTIMATE**

| Material | ΔP | \(M\) | \(\kappa\) | Forearm \(L=310\,\mathrm{mm}\): \(\theta\), \(\delta\) | \(L_{U+F}=720\,\mathrm{mm}\): \(\theta\), \(\delta\) |
|---|---:|---:|---:|---|---|
| Ecoflex 00-30 | 5 kPa | 0.16 N·m | 1.22 /m | **~22°, ~58 mm** | **~50°, ~297 mm** |
| Ecoflex 00-30 | 15 kPa | 0.49 N·m | 3.66 /m | **~65°, ~158 mm** | **~151°, ~512 mm** (large-angle; model strained) |
| Ecoflex 00-30 | 40 kPa | 1.30 N·m | 9.77 /m | **~174°, ~204 mm** | wraps — **outside linear beam validity** |
| Dragon Skin 30 | 20 kPa | 0.65 N·m | 0.57 /m | **~10°, ~27 mm** | **~23°, ~145 mm** |
| Dragon Skin 30 | 50 kPa | 1.63 N·m | 1.42 /m | **~25°, ~67 mm** | **~59°, ~337 mm** |
| Dragon Skin 30 | 100 kPa | 3.25 N·m | 2.84 /m | **~50°, ~128 mm** | **~117°, ~513 mm** |

**DESIGN ESTIMATE (planning takeaway):** under Option A envelope lengths, **Ecoflex-class** continuum reaches **tens–hundreds of mm** tip/arc deflection at **~5–15 kPa** differential in this analog; **DS30-class** needs **~20–100 kPa** for comparable angles. Large \(\theta\) rows show the beam analog **breaking down** — treat as order-of-magnitude only; **recalibrate with TB-02**.

**ASSUMPTION:** gravity, glove tip load, multi-chamber coupling, and return-band preload **omitted** in the table (would reduce net tip travel).

### 4.4 Return / snapback time-scale

**ASSUMPTION:** after vent, tip returns as undamped mass–spring order-of-magnitude with cantilever tip stiffness

\[
k_{\mathrm{eff}} \approx \frac{3\,EI_{\mathrm{eff}}}{L^{3}},\qquad \tau \sim \sqrt{\frac{m}{k_{\mathrm{eff}}}}
\]

(\(\pi\tau\) ≈ half-period scale). **ASSUMPTION:** \(L = L_{U+F} = 0.720\,\mathrm{m}\); \(R_{\mathrm{sec}}=45\,\mathrm{mm}\); glove mass from §3.

#### Elastic \(\tau\) only — **DESIGN ESTIMATE** (vent conductance **not** included)

| Material | \(\eta\) | \(EI_{\mathrm{eff}}\) | \(k_{\mathrm{eff}}\) | \(m\) | \(\tau=\sqrt{m/k}\) |
|---|---:|---:|---:|---:|---:|
| Ecoflex 00-30 | 0.20 | 0.076 N·m² | 0.61 N/m | 12 oz (0.340 kg) | **~750 ms** |
| Ecoflex 00-30 | 0.20 | 0.076 | 0.61 | **14 oz (0.397)** | **~810 ms** |
| Ecoflex 00-30 | 0.20 | 0.076 | 0.61 | 16 oz (0.454) | **~860 ms** |
| Ecoflex 00-30 | 0.35 | 0.133 | 1.07 | 14 oz | **~610 ms** |
| Dragon Skin 30 | 0.20 | 0.655 | 5.26 | 14 oz | **~275 ms** |
| Dragon Skin 30 | 0.35 | 1.15 | 9.21 | 14 oz | **~210 ms** |

**Sensitivity (Ecoflex \(\eta=0.20\)):** 8 oz → \(\tau\sim 610\,\mathrm{ms}\); 18 oz → \(\tau\sim 910\,\mathrm{ms}\).  
**Sensitivity (DS30 \(\eta=0.35\)):** 8 oz → \(\tau\sim 160\,\mathrm{ms}\); 18 oz → \(\tau\sim 240\,\mathrm{ms}\).

**Optional DESIGN ASSUMPTION:** add distal soft mass \(+0.25\,\mathrm{kg}\) to 14 oz → Ecoflex \(\eta=0.25\): \(\tau\sim 920\,\mathrm{ms}\); DS30: \(\tau\sim 310\,\mathrm{ms}\).

**Critical caveat — ASSUMPTION / NOT product ID:** real snapback is often **vent-conductance limited** (orifice, tube, valve), not pure elastic \(\tau\). Elastic \(\tau\) is a **lower-bound hypothesis** for stored-energy return after pressure is gone. **TB-04** must measure tip return time history. Limp bladder **cannot pull** — return work is elastomer + textile + return bands (continuum intent).

---

## 5) What still gets better with TB-01…04 coupons

| Coupon | Closes / improves | What this PAPER cannot claim |
|---|---|---|
| **TB-01** | Measured **P → axial strain** on sleeved bladder; overwrite §4.2 ΔP **HYPOTHESIS** | TDS has **no** actuator P–ε (**NOT IN SOURCE**) |
| **TB-02** | Differential 3-chamber **κ(ΔP)**, tip angle, chamber coupling; overwrite §4.3 beam analog | Beam/η/packing are **DESIGN ASSUMPTIONS** |
| **TB-03** | Soft wrist T1/T2 twist under glove-like load; no metal shaft | Torsion polarity / hysteresis **NOT IN SOURCE** on TDS |
| **TB-04** | Elastic return / snapback time history + fault-vent inputs; overwrite §4.4 \(\tau\) | Vent-limited dynamics **NOT IN SOURCE** |

**No System ID PASS** until those packages exist. Digital twin / this paper ≠ Track B close.

---

## 6) Optional twin hook (Astra) — Blender soft-body / pressure morph

**Explicit:** digital twin animation ≠ System ID. Use estimates only as **shape-key / attribute drivers**, then replace with TB curves.

**Recipe sketch (geometry-driven, not ID):**

1. **Mesh:** soft arm sections from N1 envelope (**GEOMETRY TARGET** lengths); 8 chamber attribute islands (U1–U3, F1–F3, T1–T2).  
2. **Shape keys / pressure attribute:** per chamber scalar `p_norm ∈ [0,1]` mapped to **HYPOTHESIS** ΔP bands (§4.2): e.g. Ecoflex map `p_norm=1 → 40 kPa` (editable constant, not certified).  
3. **Morph:** differential inflation → bend shape keys on upper/forearm; opposite T1/T2 → twist key on wrist; common-mode → slight axial key **clamped** by textile \(\lambda_{\max}\) **DESIGN ASSUMPTION** (e.g. 1.10).  
4. **Soft-body (optional):** goal strengths from \(E\) ranking (§1.3) — Ecoflex softer than DS30 (~8.6×); **do not** treat Blender soft-body as continuum FEA.  
5. **Return:** on vent, animate shape keys to rest with time constant on order of §4.4 \(\tau\) **or** longer if modeling orifice lag — label clip metadata **DESIGN ESTIMATE / twin ≠ ID**.  
6. **Glove tip mass:** rigid body / vertex group mass = parametric \(m_{\mathrm{glove}}\) (§3) for preview inertia only.

---

## 7) Blockers / non-claims

| Item | Status |
|---|---|
| Coupon System ID PASS | **Not claimed** — TB-01…04 open |
| Product working pressure / Stage 0 P-01…P-07 | **NOT closed by this paper** |
| Soft-module product mass | **NOT IN SOURCE** (volume unknown; only \(\rho\) from TDS) |
| Textile constitutive law | **NOT IN SOURCE** on elastomer TDS |
| Tip impulse / Track C contact | **Out of scope** (digital prep ≠ Track C) |
| PO / spend | **None** — coupons not required to write estimates |
| `NEXT_PROMPT.md` | **Not overwritten** |

---

## 8) Key **DESIGN ESTIMATE** number card (recalibrate at TB)

| Quantity | Ecoflex 00-30 | Dragon Skin 30 | Basis |
|---|---|---|---|
| \(E\) (Neo-Hookean from 100% mod) | **0.118 MPa** | **1.02 MPa** | §1.3 **ASSUMPTION** |
| Bare thin-wall ΔP @ mid geom, σ≈0.5×mod100 | **~4.6 kPa** | **~40 kPa** | §4.2 |
| Sleeved ΔP **HYPOTHESIS** band | **~10–80 kPa** | **~30–150 kPa** | §4.2 + textile |
| Forearm tip \(\delta\) analog @ baseline R=45 mm, η=0.35 | **~58 mm @ 5 kPa** | **~67 mm @ 50 kPa** | §4.3 |
| Snapback \(\tau\sim\sqrt{m/k}\) @ 14 oz, η=0.35 | **~610 ms** | **~210 ms** | §4.4; vent may dominate |
| Glove mass baseline | **14 oz = 0.397 kg** | same | §3 cites |

---

## References

1. Smooth-On Ecoflex™ Series TB: https://www.smooth-on.com/tb/files/ECOFLEX_SERIES_TB.pdf  
2. Smooth-On Dragon Skin™ Series TB: https://www.smooth-on.com/tb/files/DRAGON_SKIN_SERIES_TB.pdf  
3. Envelope / GEOMETRY TARGETS: `revision_n/review_packet/ENVELOPE_GEOMETRY_AUDIT.md` (N1 live audit)  
4. Digital prep: `docs/engineering/ISMAEL_DIGITAL_TRACK_B_PREP.md`  
5. Glove mass public guides: muaythai-world.com; fitset.com.au; boxfituk.com; blogs.rdxsports.com (URLs in §3.1)

---

*End of PAPER. All numeric predictions = DESIGN ESTIMATE. No System ID PASS. No PO.*
