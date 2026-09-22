# ISMAEL — C-01 TB Coupon Sizing Animation Inputs (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-22 ET |
| **Disposition** | PAPER — twin / Lilian-adjacent stills keyframe + caption inputs only |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** |
| **PO** | **NONE** — $0 digital; Soft paper only |
| **SoR target** | `docs/engineering/ISMAEL_C01_TB_COUPON_ANIMATION_INPUTS_2026-09-22.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_C01_TB_COUPON_ANIMATION_INPUTS_2026-09-22.md` |

**Cites (do not overwrite):**  
`ISMAEL_C01_COUPON_SIZING_MATH_2026-09-21.md`;  
`ISMAEL_C01_SOFT_COUPON_GEOMETRY_DEEPEN_2026-09-21.md` (**ACCEPTED-A** paper);  
`ISMAEL_C01_SOFT_COUPON_SPECIMEN_GEOMETRY.md`;  
`ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md`;  
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` (**ACCEPTED-A**);  
Ola `OLA_INTEGRATE_ISMAEL_C01_SOFT_COUPON_2026-09-21.md` / soft EXECUTE deepen.

**Standing:** Volumes / fill masses / predicted observables = **ASSUMPTION / DESIGN ESTIMATE** — **not** measured results. Soft TB ≠ Mech OB-M5. Zero spend language (no kit $ chase). Soft idle on live blend.

---

## Summary

Keyframe / caption inputs for twin or Lilian-adjacent stills explaining C-01 Soft TB coupon sizing: wall volumes, fill masses, lumen air volumes, expected textile-limited strain, and **predicted observables** checklist — all from ACCEPTED-A / Soft sizing-math sources. Critical **C-01 remains OPEN**. Soft paper only.

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| AN-01 | Critical OPEN | No physical P→motion — C-01 OPEN; animation ≠ ID. |
| AN-02 | High | First band TB-01 + TB-02; **TB-02-U before F**; Smooth-On cast first (locks). |
| AN-03 | Med | Fill masses = ASSUMPTION geometry × TDS ρ — mold dims Soft DFM TBD. |
| AN-04 | Med | Predicted observables ≠ claimed measured results. |
| AN-05 | Info | Soft does not invent sensing ICD; channel asks via Ola→Elias only. |

---

## Volumes / fill mass ASSUMPTION (animation table)

**Equations (cite sizing math E8/E9):**  
\(V_{\mathrm{wall}}=\pi L(2rt+t^{2})\); \(m=V\rho\); \(V_{\mathrm{lumen}}=\pi r^{2}L\).

**TDS densities:** Eco/DS10 **1.07 g/cc**; DS20/DS30 **1.08 g/cc** (**TDS**).

| Case | \(V_{\mathrm{wall}}\) | Ecoflex \(m\) | DS20/30 \(m\) | \(V_{\mathrm{lumen}}\) | Tag |
|---|---:|---:|---:|---:|---|
| TB-01 slim (20/3)×200 | **81.1 cm³** | **86.7 g** | **87.5 g** | — | **DESIGN ESTIMATE** |
| **TB-01 mid (30/4)×200** baseline | **160.8 cm³** | **172.1 g** | **173.7 g** | **565.5 cm³ (0.565 L)** | **DESIGN ESTIMATE** |
| TB-01 fat (40/5)×200 | **267.0 cm³** | **285.7 g** | **288.4 g** | — | **DESIGN ESTIMATE** |
| TB-02 one-ch mid (30/4)×250 | **201.1 cm³** | **215.1 g** | **217.1 g** | **706.9 cm³ (0.707 L)** | **DESIGN ESTIMATE** |
| TB-02 ×3 mid | **603.2 cm³** | **645.4 g** | **651.4 g** | 3× lumen class | **DESIGN ESTIMATE** |

**NOT IN SOURCE on stills:** textile sleeve mass, registration yarn, return-band mass, fittings.

**ASSUMPTION geometry kit:** TB-01 mid baseline \(L=200\,\mathrm{mm}\), \((r,t)=(30,4)\,\mathrm{mm}\); coupon lengths = bench envelopes ≠ product Soft free lengths.

---

## Predicted observables (caption checklist — not claimed results)

| Coupon | Build order | Caption: what to record when cast | Does **not** claim |
|---|---|---|---|
| **TB-01** | First with TB-02 | \(P(t)\), \(\Delta L(t)\), leak/hold qualitative, neck peel class, vent return | Working product P; System ID PASS |
| **TB-01a** | Reserve boss **before** first cast | Same + port-boss mount notes | Elias SKU / bar range |
| **TB-02-U** | **Before F** | ΔP triad, tip θ/κ proxy, coupling qualitative | Full-arm ID |
| **TB-02-F** | After U learning | Forearm-section bend observables | Product Soft OD |
| **TB-03** | Later | Twist vs ΔP; unwanted ΔL/bend | Metal-shaft torsion |
| **TB-04** | On TB-01/02 hosts | Tip return \(x(t)\) on vent; sag vs snapback | Product cycle life |

**Wall-strain DESIGN ESTIMATE caption (mid 30/4, textile λ_max=1.10):** bare Ecoflex @ 5 kPa → ε~0.32 outside clamp; with textile → **clamp ~0.10**; tip bend on TB-02 from **differential** P — overwrite TB-01.

---

## Animation keyframe / caption inputs

Stamp every still: `DESIGN ESTIMATE · C-01 OPEN · predicted observables ≠ measured · Soft paper only`

| KF | Visual | Caption inputs (copy-ready) |
|---|---|---|
| **K0** | Title | C-01 Soft TB coupon sizing — DESIGN ESTIMATE pedagogy |
| **K1** | Geometry callouts mid (30/4)×200 | ASSUMPTION: L=200 mm, r=30 mm, t=4 mm — Soft DFM may revise |
| **K2** | Wall volume highlight | \(V_{\mathrm{wall}}=160.8\,\mathrm{cm}^{3}\) DESIGN ESTIMATE |
| **K3** | Fill-mass bar Eco vs DS30 | Eco **172.1 g** / DS30 **173.7 g** — TDS ρ × V; weigh cast to validate |
| **K4** | Lumen air volume | \(V_{\mathrm{lumen}}=0.565\,\mathrm{L}\) ASSUMPTION — feeds vent τ storyboard |
| **K5** | Textile clamp diagram | λ_max=1.10 DESIGN ASSUMPTION; axial useful fiber-limited |
| **K6** | Sequence lock strip | [0] TB-01a boss → [1] Ecoflex primary → [2] TB-01 → [3] TB-02-U → [4] TB-02-F → [5] TB-03/04 later |
| **K7** | Observables checklist (TB-01/02) | Predicted: P→ε, κ(ΔP), coupling, leak/hold, mass check — **not claimed results** |
| **K8** | End card | Critical C-01 OPEN · Soft TB ≠ Mech OB-M5 · Soft idle on live blend · $0 digital |

### Twin / Lilian-adjacent still notes (Soft paper only)

- Prefer **TB-01 mid** as baseline hero still; slim/fat as sensitivity insets.  
- Do **not** animate product Soft OD as frozen mm.  
- Optional companion still: link lumen V → vent storyboard Beat B6 (seconds-class τ_vent).  
- Soft does **not** draw Elias SKU callouts — channel asks only.

---

## Draft recommendations

1. Accept animation inputs as Soft digital companion to C-01 sizing math — **C-01 stays OPEN**.  
2. Use TB-01 mid row as default keyframe geometry.  
3. Keep TB-02-U-before-F and TB-01a reserve in sequence stills.  
4. Zero spend language — park hardware until Lead/Stephen path opens elsewhere; Soft paper only here.

---

## Test gaps

| Gap | Status |
|---|---|
| Physical TB evidence packages | OPEN |
| Frozen mold / Soft OD mm | Soft DFM TBD — NOT IN SOURCE |
| Elias instrumentation ICD | Parallel via Ola |
| Textile / fittings mass adders | NOT IN SOURCE |

---

## Open questions for Ola

1. Accept TB coupon animation inputs as Soft DESIGN ESTIMATE stills pack (C-01 OPEN)?  
2. Confirm TB-01 mid (30/4)×200 as hero geometry for Track A / Lilian-adjacent stills?  
3. Soft idle on live blend after land — still correct?  
4. Preferred SoR land OK?

---

## Non-claims

- No PO · **C-01 OPEN** · **B-06 OPEN**  
- No claimed measured strain / force / life / FPS  
- No sensing SKU invention · Soft TB ≠ Mech OB-M5 · no NEXT_PROMPT · no spend chase

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Critical C-01 | **OPEN** |
| PO | **None ($0)** |

— Ismael · Soft Robotics Desk · 2026-09-22 ET · awaiting Ola disposition —
