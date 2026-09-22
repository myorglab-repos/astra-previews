# ISMAEL — C-01 Coupon Sizing Math (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Disposition** | PAPER — coupon volume / fill-mass / predicted observables only |
| **Critical C-01** | **OPEN** (no measured System ID) |
| **Critical B-06** | **OPEN** — Lead; not closed here |
| **PO** | **NONE** — $0; Stephen before any cast kit |
| **SoR target** | `docs/engineering/ISMAEL_C01_COUPON_SIZING_MATH_2026-09-21.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_C01_COUPON_SIZING_MATH_2026-09-21.md` |

**Cites:** `ISMAEL_C01_SOFT_COUPON_SPECIMEN_GEOMETRY.md`; `ISMAEL_C01_SOFT_COUPON_GEOMETRY_DEEPEN_2026-09-21.md`; `ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` (ACCEPTED-A); `ISMAEL_DIGITAL_TRACK_B_PREP.md`; Neo-Hookean pack `ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md`.

**Ola locks honored:** TB-01+TB-02 first; **TB-02-U before F**; Smooth-On cast first; TB-01a port boss reserve; C-01 stays Critical OPEN; Soft does not invent sensing ICD.

---

## Summary

Sizing math for Soft TB coupons: elastomer wall **volumes** and **fill masses** from **ASSUMPTION** geometry × TDS density; expected wall strain at **ASSUMPTION** pressures as **DESIGN ESTIMATE**; instrumented TB-01…04 matrix with **predicted observables** (what to measure when cast) — **not claimed results**. Critical **C-01 remains OPEN**.

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| C01M-01 | Critical OPEN | No physical P→motion evidence — C-01 OPEN. |
| C01M-02 | High | First band TB-01 + TB-02; TB-02-U before F; Smooth-On cast first. |
| C01M-03 | Med | Fill masses = ASSUMPTION geometry × TDS ρ — mold dims Soft DFM TBD. |
| C01M-04 | Med | Predicted observables ≠ measured System ID. |
| C01M-05 | Info | TB-01a port boss reserved before first cast (geometry class only). |

---

## Equations

### Fill mass (**ASSUMPTION** geometry × TDS density)

\[
V_{\mathrm{wall}} = \pi L \left[(r+t)^{2} - r^{2}\right] = \pi L (2 r t + t^{2})
\]

\[
m_{\mathrm{elastomer}} = V_{\mathrm{wall}} \times \rho,\qquad \rho_{\mathrm{Eco}}=\mathbf{1.07}\,\mathrm{g/cc},\ \rho_{\mathrm{DS20/30}}=\mathbf{1.08}\,\mathrm{g/cc}\ \text{(TDS)}
\]

Lumen volume (air volume for vent math — companion pack):

\[
V_{\mathrm{lumen}} = \pi r^{2} L
\]

---

## ASSUMPTION geometry kit (planning — Soft OD **NOT IN SOURCE** as freeze)

| Specimen | Active free length \(L\) | Bladder \((r,t)\) class | Tag |
|---|---|---|---|
| TB-01 slim | **200 mm** (within 150–250) | (20, 3) mm | **ASSUMPTION** |
| TB-01 mid (baseline) | **200 mm** | **(30, 4) mm** | **ASSUMPTION** |
| TB-01 fat | **200 mm** | (40, 5) mm | **ASSUMPTION** |
| TB-02 one chamber mid | **250 mm** (shortened OK) | (30, 4) mm | **ASSUMPTION** |
| TB-02 section (×3 chambers) | **250 mm** | 3× mid walls | **ASSUMPTION** packing |
| TB-03 cuff span | **80–120 mm** | torsion elements TBD Soft DFM | **ASSUMPTION** |

**ASSUMPTION:** Coupon lengths are bench planning envelopes — **not** product U/F Soft free lengths (GEOMETRY TARGET paths remain film lengths).

---

## Volumes and fill masses (**DESIGN ESTIMATE** arithmetic)

| Case | \(V_{\mathrm{wall}}\) | Ecoflex 00-30 \(m\) | DS10 \(m\) (ρ=1.07) | DS20 / DS30 \(m\) (ρ=1.08) | Tag |
|---|---:|---:|---:|---:|---|
| TB-01 slim (20/3)×200 | **81.1 cm³** | **86.7 g** | **86.7 g** | **87.5 g** | **DESIGN ESTIMATE** |
| TB-01 mid (30/4)×200 | **160.8 cm³** | **172.1 g** | **172.1 g** | **173.7 g** | **DESIGN ESTIMATE** |
| TB-01 fat (40/5)×200 | **267.0 cm³** | **285.7 g** | **285.7 g** | **288.4 g** | **DESIGN ESTIMATE** |
| TB-02 one ch mid (30/4)×250 | **201.1 cm³** | **215.1 g** | **215.1 g** | **217.1 g** | **DESIGN ESTIMATE** |
| TB-02 ×3 mid | **603.2 cm³** | **645.4 g** | **645.4 g** | **651.4 g** | **DESIGN ESTIMATE** |

**NOT IN SOURCE:** textile sleeve mass, registration yarn, return-band mass, fittings — add only when areal densities known.

**Lumen volumes (for vent companion):** TB-01 mid \(V_{\mathrm{lumen}}=\mathbf{565.5\,\mathrm{cm}^{3}}\) (0.565 L); TB-02 one-ch mid **706.9 cm³** (0.707 L) — **ASSUMPTION** geometry.

---

## Expected wall strain at ASSUMPTION pressures (**DESIGN ESTIMATE**)

Using Neo-Hookean pack E / thin-wall hoop; textile clamp \(\lambda_{\max}=1.10\) **DESIGN ASSUMPTION**.

| Material | ΔP **ASSUMPTION** | Mid (30/4) \(\sigma=Pr/t\) | Bare \(\varepsilon\sim\sigma/E\) | Textile-limited | Tag |
|---|---|---|---|---|---|
| Ecoflex | 5 kPa | 37.5 kPa | ~0.32 | **clamp ~0.10** | **DESIGN ESTIMATE** |
| Ecoflex | 15 kPa | 112.5 kPa | ~0.95 | **clamp ~0.10** | **DESIGN ESTIMATE** |
| Ecoflex | 40 kPa (p_norm map) | 300 kPa | ≫1 (model break) | **clamp ~0.10** | **DESIGN ESTIMATE** |
| DS20 | 40 kPa | 300 kPa | ~0.52 | **clamp ~0.10** | **DESIGN ESTIMATE** |
| DS30 | 50 kPa | 375 kPa | ~0.37 | **clamp ~0.10** | **DESIGN ESTIMATE** |

**Takeaway:** With textile, **axial** useful strain is fiber-limited (~5–15% **DESIGN ASSUMPTION** band); tip bend on TB-02 comes from **differential** chamber pressure, not bulk free stretch. Overwrite with TB-01 measured P→ε.

**Sleeved ΔP HYPOTHESIS** (planning — not product P): Ecoflex ~10–80 kPa; DS30 ~30–150 kPa (ACCEPTED-A).

---

## Instrumented TB-01…04 matrix — **predicted observables** (not claimed results)

| Coupon | Build order | Channels Soft asks (via Ola→Elias) | **Predicted observables** when cast (what to record) | Does **not** claim |
|---|---|---|---|---|
| **TB-01** | **First** with TB-02 | 1× branch P; ΔL axial; optional temp; time sync | \(P(t)\), \(\Delta L(t)\), leak/hold qualitative, neck peel class, vent return on one chamber | Working product P; System ID PASS |
| **TB-01a** | Reserve boss **before** first cast | Same + cleaner P tap geometry | Same as TB-01 with port-boss mount notes | Elias SKU / bar range |
| **TB-01b** | Optional | Same + return-band wear | Early return narrative toward TB-04 | Cycle life |
| **TB-02-U** | **Before F** | 3× branch P; tip angle / κ proxy; time sync | \(\Delta P\) triad, tip \(\theta(t)\) / \(\kappa\), coupling qualitative, registration under load | Full-arm ID |
| **TB-02-F** | After U learning | Same | Forearm-section bend ID observables | Product Soft OD |
| **TB-03** | Later band | 2× P; signed twist; glove-like tip load class | Twist vs ΔP; unwanted ΔL / bend noted | Metal-shaft torsion; B-06 peel N |
| **TB-04** | On TB-01/02 hosts | Vent event + tip return history | Tip return \(x(t)\) on vent; sag vs snapback; fault-vent **inputs** | Product cycle life; elastic-only τ as truth |

**Predicted observable classes (paper checklist — measure when hardware exists):**

1. **Leak / hold:** gauge hold qualitative before motion runs — **no invented leak-rate setpoint**.  
2. **P→ε (TB-01):** axial stretch vs regulated P at discrete steps — overwrite DESIGN ESTIMATE bands.  
3. **κ(ΔP) (TB-02):** tip angle / curvature vs differential chamber pressures.  
4. **Coupling:** unintended motion of unpowered chambers.  
5. **Return (TB-04):** time to rest band after vent command; compare to vent-time DESIGN ESTIMATE pack.  
6. **Mass check:** weigh cast bladder dry → compare to fill-mass table (geometry validation).

---

## Cast / sequence locks (reconfirm)

```
[0] Reserve TB-01a port-boss geometry class
[1] Smooth-On Ecoflex 00-30 primary (+ optional DS comparative)
[2] Cast TB-01 → sleeve → qualitative leak → P→ε when Elias ready
[3] Cast/assemble TB-02-U → differential bend
[4] TB-02-F after U learning
[5] TB-03 / TB-04 later unless Lead reorders
```

**ASSUMPTION (tube):** provisional NITRA **6 mm or 1/4″**; prod lean Festo PUN-H — OD freeze open.  
**ASSUMPTION (textile):** power-net class first sleeves.

---

## ASSUMPTION tables

| # | ASSUMPTION |
|---|---|
| A1 | Ecoflex 00-30 primary; DS10/20/30 comparative ranking |
| A2 | Coupon \((L,r,t)\) classes above — Soft DFM may revise before cast |
| A3 | Densities from Smooth-On TDS (access 2026-09-21 ET) |
| A4 | Textile \(\lambda_{\max}\) planning 1.10 |
| A5 | Shortened coupons OK (Ola ACCEPTED-A) |
| A6 | TB-04 reuses TB-01/02 hosts |
| A7 | Sensing SKUs / ranges = Elias after Ola routes |
| A8 | Predicted observables ≠ measured results |

---

## Draft recommendations

1. Accept sizing math as Soft paper companion — **C-01 stays OPEN**.  
2. Use TB-01 mid (30/4)×200 as baseline fill-mass planning row.  
3. Weigh first cast lot vs table to validate geometry ASSUMPTIONs.  
4. Keep TB-01a reserved; Soft does not invent sensing ICD.

---

## Test gaps

| Gap | Status |
|---|---|
| Physical TB evidence packages | OPEN — Stephen Soft TB band |
| Frozen mold / Soft OD mm | Soft DFM TBD — **NOT IN SOURCE** |
| Elias instrumentation ICD | Parallel via Ola |
| Textile / fittings mass adders | NOT IN SOURCE |

---

## Open questions for Ola

1. Accept coupon sizing math as Soft DESIGN ESTIMATE companion (C-01 OPEN)?  
2. Confirm TB-01 mid (30/4)×200 as baseline planning geometry (or pick slim/fat)?  
3. Any change to TB-02-U-before-F or shortened-coupon acceptance?  
4. Confirm Soft still must not invent sensing ICD?

---

## Non-claims

- No PO · **C-01 OPEN** · **B-06 OPEN**  
- No claimed measured strain / force / life  
- No sensing SKU invention · no NEXT_PROMPT write

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Critical C-01 | **OPEN** |
| PO | **None ($0)** |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-21 ET · awaiting Ola disposition —
