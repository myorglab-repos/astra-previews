# ISMAEL — Soft Physics Math INTEGRATE Note (packets 1–4)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Disposition** | PAPER integrate — equation + master ASSUMPTION index |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** |
| **PO** | **NONE** |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_PHYSICS_MATH_INTEGRATE_2026-09-21.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_PHYSICS_MATH_INTEGRATE_2026-09-21.md` |

**Prior ACCEPTED-A / deepen cites (do not overwrite):**  
- `ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` + Ola `ENGINEERING_ASSESSMENT_ISMAEL_VIRTUAL_SOFT_PHYSICS_2026-09-21.md` (**ACCEPTED-A**)  
- `ISMAEL_VIRTUAL_SOFT_ARM_TWIN_DEEPEN_2026-09-21.md`  
- `ISMAEL_DIGITAL_TRACK_B_PREP.md`  
- C-01 specimen + geometry deepen; B-06 envelope keep-out + deepen v2  

**This-session packets:**

| # | Packet | Box path |
|---|---|---|
| 1 | Neo-Hookean / P→strain→bend | `.../ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md` |
| 2 | C-01 coupon sizing math | `.../ISMAEL_C01_COUPON_SIZING_MATH_2026-09-21.md` |
| 3 | B-06 keep-out / pitch numeric DESIGN TARGETS | `.../ISMAEL_B06_KEEP_OUT_PITCH_NUMERIC_TARGETS_2026-09-21.md` |
| 4 | Soft return / vent time-order | `.../ISMAEL_SOFT_RETURN_VENT_TIME_ORDER_2026-09-21.md` |

---

## Summary

Single integrate index of **every pedagogy equation** and a **master ASSUMPTION table** across Soft physics-math packets 1–4. Critical **C-01** and **B-06** remain **OPEN**. DESIGN ESTIMATE ≠ System ID. Soft TB ≠ Mech OB-M5.

---

## Master equation list

| ID | Packet | Equation (short) | Role |
|---|---|---|---|
| E1 | 1 | \(1\,\mathrm{psi}=6894.757\,\mathrm{Pa}\) | Unit convert |
| E2 | 1 | \(\sigma_{\mathrm{eng}}=2C_1(\lambda-\lambda^{-2})\); \(\mu=2C_1\); at \(\lambda=2\): \(C_1=\sigma/3.5\) | Neo-Hookean bridge |
| E3 | 1 | \(\sigma_{\mathrm{hoop}}=\Delta P\,r/t\) | Thin-wall hoop |
| E4 | 1 | \(M=\Delta P A_{\mathrm{ch}} e\); \(\kappa=M/EI_{\mathrm{eff}}\); \(\theta=\kappa L\); \(\delta=R(1-\cos\theta)\) | Bend free-body |
| E5 | 1 | \(\varepsilon\sim\sigma/E\); \(\lambda\le\lambda_{\max}\) textile clamp | Wall stretch pedagogy |
| E6 | 1 | \(\Delta P=p_{\mathrm{norm}}\cdot\Delta P_{\mathrm{map}}\) | Twin p_norm |
| E7 | 1 | \(k_{\mathrm{eff}}\approx 3EI/L^{3}\); \(F\sim k\delta\); \(J\sim F t_c\) or \(m\Delta v\) | Force/impulse **HYPOTHESIS** OOM |
| E8 | 2 | \(V_{\mathrm{wall}}=\pi L(2rt+t^{2})\); \(m=V\rho\) | Coupon fill mass |
| E9 | 2 | \(V_{\mathrm{lumen}}=\pi r^{2} L\) | Air volume |
| E10 | 4 | \(\tau_{\mathrm{el}}\sim\sqrt{m/k_{\mathrm{eff}}}\) | Elastic return |
| E11 | 4 | \(Q\approx C_d A_o\sqrt{2\Delta P/\rho_{\mathrm{air}}}\); \(\tau_{\mathrm{vent}}\sim V/Q\) | Vent discharge |
| E12 | 4 | \(\tau_{\mathrm{return,plan}}\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) | Combined planning |
| — | 3 | Catalog \(R_{\min}\) / flow-relevant floors (no new constitutive eq.) | Keep-out DESIGN TARGETS |

---

## Master ASSUMPTION / DESIGN ESTIMATE kit

### Material (TDS ASSUMPTION → DESIGN ESTIMATE μ)

| Material | Shore | \(\rho\) (TDS) | 100% mod (TDS) | \(\mu\) **DESIGN ESTIMATE** | \(E\approx 3\mu\) |
|---|---|---|---|---|---|
| Ecoflex 00-30 | 00-30 | **1.07 g/cc** | 10 psi | **39.399 kPa** | **0.118 MPa** |
| Dragon Skin 10 MEDIUM | 10A | **1.07 g/cc** | 22 psi | **86.677 kPa** | **0.260 MPa** |
| Dragon Skin 20 | 20A | **1.08 g/cc** | 49 psi | **193.053 kPa** | **0.579 MPa** |
| Dragon Skin 30 | 30A | **1.08 g/cc** | 86 psi | **338.8 kPa** | **1.02 MPa** |

**TDS URLs + access 2026-09-21 ET:** Smooth-On Ecoflex / Dragon Skin product pages + series TBs (see packet 1).

### Geometry / load ASSUMPTIONS (shared)

| Key | Value | Tag |
|---|---|---|
| Chambers | U1–U3, F1–F3, T1–T2 (8/arm) | Lock |
| \(R_{\mathrm{sec}}\) baseline | 45 mm | **ASSUMPTION** |
| \(\eta\) knockdown | 0.20–0.35 | **ASSUMPTION** |
| \(\lambda_{\max}\) textile | 1.10 baseline (1.05/1.15 sens.) | **DESIGN ASSUMPTION** |
| Glove mass | **14 oz = 0.397 kg** | **ASSUMPTION** |
| TB-01 mid bladder | \(L=200\,\mathrm{mm}\), \((r,t)=(30,4)\,\mathrm{mm}\) | **ASSUMPTION** |
| Sleeved ΔP Ecoflex | ~10–80 kPa | **HYPOTHESIS** |
| Sleeved ΔP DS30 | ~30–150 kPa | **HYPOTHESIS** |
| `dp_map_kPa` Eco / DS30 | 40 / 100 | **HYPOTHESIS** |
| Tube OD provisional | NITRA 6 mm or 1/4″ | **ASSUMPTION** |
| Vent orifice \(d_o\) | 1.0 / 1.5 mm; \(C_d=0.60\) | **ASSUMPTION** |
| Bend keep-out floor (6 mm class) | NITRA ≥12 mm; Festo flow-rel. prefer ≥26.5 mm | **DESIGN TARGET** from catalog |
| Tip force / impulse | OOM only | **HYPOTHESIS** — not System ID |
| Return time | vent often dominates elastic | **DESIGN ESTIMATE** — not cycle life |

---

## Cross-packet dependency map

```
ACCEPTED-A virtual physics ──► Packet 1 (Neo-Hookean deepen + OOM force)
         │                         │
         ├─► twin deepen (p_norm) ─┘
         │
         ├─► Packet 2 (coupon V, m, predicted observables) ──► C-01 OPEN
         │
         ├─► Packet 4 (vent vs elastic τ) ◄── Packet 2 lumen V
         │
         └─► Packet 3 (B-06 DESIGN TARGET floors) ──► B-06 OPEN
                    ▲
                    └── Soft BOM scout bend table + ABS/BOM $ cites
```

---

## Critical / process status (integrate)

| Item | Status |
|---|---|
| Critical **C-01** | **OPEN** |
| Critical **B-06** | **OPEN** (Lead) |
| Soft ICD numeric freeze | Pending CAD |
| Chafe sleeve PN | Wait ABS mock fit-check |
| Soft TB vs Mech OB-M5 | Separate bands |
| System ID PASS | **Not claimed** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |

---

## Draft recommendations (for Ola)

1. Accept packets 1–4 + this integrate as Soft physics-math paper stack deepen of ACCEPTED-A virtual physics / twin / C-01 / B-06 Soft lanes.  
2. Recalibrate all DESIGN ESTIMATE / HYPOTHESIS bands when TB-01…04 exist.  
3. Soft idle on live Blender soft-body until Lead asks (prior Ola soft-physics assessment).  
4. Prefer SoR land under `docs/engineering/` dated filenames (do not overwrite ACCEPTED-A sources).

---

## Open questions for Ola

1. Disposition ACCEPTED-A / revise on packets 1–4 + integrate?  
2. Any equation or ASSUMPTION kit row to strike before board cite?  
3. Confirm Soft idle posture after land until Lead asks for Blender hook or new physics question?

---

## Non-claims

- No PO · C-01 OPEN · B-06 OPEN  
- No invented measured lab P/strain/force/cycle life  
- DESIGN ESTIMATE ≠ System ID · DESIGN TARGET ≠ measured clearance  
- Soft TB ≠ Mech OB-M5 · no NEXT_PROMPT write

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT integrate for Lead review |
| Packets indexed | 1–4 dated 2026-09-21 |
| Prior ACCEPTED-A | Cited, not overwritten |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-21 ET · awaiting Ola disposition —
