# ISMAEL — Soft Twin Neo-Hookean HUD Overlay Brief (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-22 ET |
| **Disposition** | PAPER — teach / overlay only; Soft idle on live `.blend` |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** (Lead) |
| **PO** | **NONE** — $0 digital |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_TWIN_NEOHOOK_HUD_OVERLAY_BRIEF_2026-09-22.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_TWIN_NEOHOOK_HUD_OVERLAY_BRIEF_2026-09-22.md` |

**Cites (do not overwrite ACCEPTED-A sources):**  
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` + Ola `ENGINEERING_ASSESSMENT_ISMAEL_VIRTUAL_SOFT_PHYSICS_2026-09-21.md` (**ACCEPTED-A**);  
`ISMAEL_VIRTUAL_SOFT_ARM_TWIN_DEEPEN_2026-09-21.md` (**ACCEPTED-A** paper per Ola soft EXECUTE deepen);  
`ISMAEL_SOFT_ARM_NEOHOOK_PRESSURE_STRAIN_BEND_2026-09-21.md`;  
`ISMAEL_SOFT_PHYSICS_MATH_INTEGRATE_2026-09-21.md`;  
`ISMAEL_SOFT_RETURN_VENT_TIME_ORDER_2026-09-21.md`.

**Standing:** Every numeric on HUD = **ASSUMPTION** / **DESIGN ESTIMATE** / **HYPOTHESIS** in plain sight. Equations already ACCEPTED-A (virtual physics) or Soft DESIGN ESTIMATE deepen — **teach/overlay only**. Soft idle on live `.blend` unless Lead asks. Soft TB ≠ Mech OB-M5. No spend language.

---

## Summary

Track A **ASSUMPTION HUD** card text + recommended Blender driver / custom-property / shape-key map so Ola/CloudAgent can overlay Neo-Hookean pedagogy (`p_norm`, μ labels, bend DESIGN ESTIMATE) without claiming System ID. All equations cite ACCEPTED-A / Soft deepen packs; this brief does **not** invent new constitutive math. **C-01 and B-06 remain OPEN.** Soft stays idle on live blend.

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| HUD-01 | High (process) | Overlay shows **DESIGN ESTIMATE** only — never System ID / measured P→ε. |
| HUD-02 | Med | Named Blender props = Soft proposals (**ASSUMPTION / Lead-confirm**) from ACCEPTED-A twin deepen — not a live schema freeze. |
| HUD-03 | Med | Bend tip δ / θ rows are beam-analog **DESIGN ESTIMATE**; large θ strains the linear idealization. |
| HUD-04 | Info | Soft idle on live `.blend` (Ola ACCEPTED-A soft EXECUTE deepen) — this paper teaches CloudAgent overlays only. |
| HUD-05 | Info | Soft TB ≠ Mech OB-M5; twin morph ≠ ID. |

---

## ASSUMPTION HUD card text (what overlays show)

**Stamp every frame / metadata:** `DESIGN ESTIMATE / twin ≠ ID` · Critical **C-01 OPEN** · **B-06 OPEN**.

### Card A — Material μ (TDS → Neo-Hookean bridge)

| HUD line | Source value | Tag |
|---|---|---|
| Ecoflex 00-30 μ | **39.399 kPa** | **DESIGN ESTIMATE** from TDS 10 psi @ 100% (ACCEPTED-A / Neo-Hookean pack E2) |
| DS10 MEDIUM μ | **86.677 kPa** | **DESIGN ESTIMATE** (comparative) |
| DS20 μ | **193.053 kPa** | **DESIGN ESTIMATE** (comparative) |
| DS30 μ | **338.8 kPa** | **DESIGN ESTIMATE** (ACCEPTED-A) |
| Bridge note | TDS 100% modulus → μ via E2 | **ASSUMPTION** — not sleeved actuator fit |

**HUD copy (example):**  
`μ Ecoflex 39.4 kPa · DS30 339 kPa — DESIGN ESTIMATE from Smooth-On TDS (not System ID)`

### Card B — `p_norm` map

| HUD line | Value | Tag |
|---|---|---|
| `p_norm` | ∈ [0, 1] | **ASSUMPTION** editable scalar |
| Ecoflex-class `dp_map_kPa` @ `p_norm=1` | **40** | **HYPOTHESIS / DESIGN ESTIMATE** — not product working P |
| DS30-class `dp_map_kPa` | **100** | **HYPOTHESIS / DESIGN ESTIMATE** |
| Optional DS10/20 maps | **60 / 80** | **HYPOTHESIS** Soft proposal (rank interpolate) |
| Map equation | \(\Delta P = p_{\mathrm{norm}}\cdot\Delta P_{\mathrm{map}}\) | ACCEPTED-A E6 pedagogy |

**HUD copy:**  
`ΔP = p_norm × dp_map · Eco map 40 kPa / DS30 map 100 kPa — HYPOTHESIS editable; not working P`

### Card C — Bend DESIGN ESTIMATE (baseline ACCEPTED-A analog)

**ASSUMPTION geometry:** \(R_{\mathrm{sec}}=45\,\mathrm{mm}\), \(\eta=0.35\), forearm \(L=310\,\mathrm{mm}\).

| Material | ΔP | Forearm θ, δ | Tag |
|---|---|---|---|
| Ecoflex 00-30 | 5 kPa | **~22°, ~58 mm** | **DESIGN ESTIMATE** |
| Ecoflex 00-30 | 15 kPa | **~65°, ~158 mm** | **DESIGN ESTIMATE** |
| DS30 | 50 kPa | **~25°, ~67 mm** | **DESIGN ESTIMATE** |
| DS30 | 100 kPa | **~50°, ~128 mm** | **DESIGN ESTIMATE** |

**HUD copy:**  
`Bend θ/δ = DESIGN ESTIMATE beam analog (η=0.35, R=45 mm) — recalibrate TB-02; ≠ System ID`

### Card D — Textile clamp

| HUD line | Value | Tag |
|---|---|---|
| \(\lambda_{\max}\) baseline | **1.10** | **DESIGN ASSUMPTION** |
| Sensitivity | 1.05 / 1.15 | **DESIGN ASSUMPTION** |
| Axial useful | fiber-limited ~5–15% band | **DESIGN ASSUMPTION** |

**HUD copy:**  
`Textile λ_max = 1.10 DESIGN ASSUMPTION — axial clamp; bend from differential P`

### Card E — Return τ (pointer only; storyboard owns beats)

| HUD line | Value | Tag |
|---|---|---|
| Ecoflex τ_el @ 14 oz, η=0.35 | **~610 ms** | **DESIGN ESTIMATE** |
| Planning return | \(\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) — often **seconds** | **DESIGN ESTIMATE** — not cycle life |

**HUD copy:**  
`Return τ_plan ≳ max(τ_el, τ_vent) — vent often dominates; not cycle life; not TB-04`

### Explicit HUD non-claims (footer on every card)

- Not measured P→ε · not product working P · not System ID PASS  
- Not Track C force/impulse · not FEA PASS · not cycle life  
- Soft idle on live `.blend` · Soft TB ≠ Mech OB-M5

---

## Recommended Blender driver / custom-property / shape-key map

**ASSUMPTION / Lead-confirm:** Names below = Soft proposals from ACCEPTED-A twin deepen. Soft does **not** edit live `.blend`. Ola/CloudAgent may adopt for Track A teach overlay.

### Custom properties (overlay-bound)

| Prop | Overlay use | Default planning | Tag |
|---|---|---|---|
| `p_norm_U1`…`p_norm_T2` | Drive chamber morph + HUD bar | 0 = rest | **ASSUMPTION** |
| `mat_class` | Switch μ / `dp_map` HUD row | `0` Ecoflex / `1` DS30 | **ASSUMPTION** |
| `dp_map_kPa` | Card B ΔP map | 40 / 100 | **HYPOTHESIS / DESIGN ESTIMATE** |
| `lambda_max` | Clamp axial SK + Card D | **1.10** | **DESIGN ASSUMPTION** |
| `m_glove_kg` | Tip inertia label | **0.397** (14 oz) | **ASSUMPTION** |
| `tau_return_s` | Vent morph duration + Card E | Eco ~0.61 s elastic order; prefer longer if orifice lag | **DESIGN ESTIMATE** |
| `eta_knockdown` | Bend band selector | **0.20–0.35** | **ASSUMPTION** |
| `hud_stamp` (string) | Always visible | `DESIGN ESTIMATE / twin ≠ ID` | Lock |

### Shape keys → HUD linkage

| Shape key | Driven by | HUD annotation |
|---|---|---|
| `SK_BEND_UPPER` | Diff U1–U3 `p_norm` | Card C upper (qualitative) |
| `SK_BEND_FOREARM` | Diff F1–F3 `p_norm` | Card C forearm δ/θ DESIGN ESTIMATE |
| `SK_TWIST_WRIST` | Opposite T1/T2 | Soft wrist / no distal metal story |
| `SK_AXIAL_COMMON` | Common-mode; clamp ≤ f(`lambda_max`) | Card D |
| `SK_REST_RETURN` | `SO_VENT_STATE` / `tau_return_s` | Card E — not cycle life |

### Driver recommendations (qualitative — ASSUMPTION)

1. Map `p_norm_*` → local bulge / bend contribution (geometry-driven, not ID).  
2. When `mat_class` flips, swap HUD μ + `dp_map_kPa` rows only — do not claim measured stiffness.  
3. Clamp axial SK by `lambda_max`.  
4. On vent: animate rest over `tau_return_s` (or longer vent-dominated band — label metadata).  
5. Optional soft-body goal ranking Eco softer than DS30 (~**8.6×** E ratio **DESIGN ESTIMATE**) — Blender soft-body ≠ continuum FEA.

### Collections / Empties (unchanged proposals — cite twin deepen)

`COL_SOFT_ARM_L/R`, `COL_CHAMBERS_U/F/T`, `COL_SOFT_GLOVE_TIP`, `COL_SOFT_TWIN_DRIVERS`; Empties `SO_ARM_ROOT`, `SO_SEC_UPPER`, `SO_SEC_FOREARM`, `SO_WRIST_SOFT`, `SO_CH_U1`…`T2`, `SO_TIP_GLOVE_MASS`, `SO_VENT_STATE` — all **ASSUMPTION / Lead-confirm**.

---

## Equations already ACCEPTED-A / Soft deepen (teach only — no new math)

| ID | Role on HUD | Source |
|---|---|---|
| E2 | μ / C1 bridge | Neo-Hookean pack / integrate |
| E4 | M→κ→θ→δ bend analog | ACCEPTED-A deepen |
| E5 | Textile λ clamp | ACCEPTED-A |
| E6 | `p_norm` map | ACCEPTED-A twin / Neo-Hookean |
| E10–E12 | Return τ order (Card E pointer) | Vent time-order pack |

---

## Draft recommendations

1. Accept this HUD overlay brief as Soft **teach/overlay** companion to ACCEPTED-A twin deepen + Neo-Hookean pack — **not** a live `.blend` edit.  
2. Stamp every overlay: `DESIGN ESTIMATE / twin ≠ ID`; Criticals OPEN.  
3. Keep Soft idle on live blend until Lead asks; CloudAgent/Ola may use named props as ASSUMPTION proposals.  
4. Prefer zero-spend / paper-only language in Track A film captions.  
5. Do not surface tip-force OOM on primary HUD (optional off-by-default footnote if Lead asks — still **HYPOTHESIS**, not System ID).

---

## Test gaps

| Gap | Status |
|---|---|
| Live `.blend` schema freeze | OPEN — Lead-confirm names |
| TB-01…04 overwrite of DESIGN ESTIMATE bands | OPEN — C-01 |
| Soft-body as FEA | Forbidden claim |
| Measured HUD calibration | OUT OF SCOPE until TB |

---

## Open questions for Ola

1. Accept ASSUMPTION HUD card text (Cards A–E) as Track A teach overlay copy?  
2. Confirm Soft proposals for props/SKs remain **ASSUMPTION / Lead-confirm** for CloudAgent (Soft idle on live blend)?  
3. Prefer Ecoflex-primary HUD default (`mat_class=0`) with DS30 as comparative toggle only?  
4. Any freeze delta to 8-chamber / Option A / elastic return / distal-metal?  
5. Preferred SoR land path OK?

---

## Non-claims

- No PO · **C-01 OPEN** · **B-06 OPEN**  
- No live `.blend` edit from Soft desk · twin ≠ ID  
- No invented measured P / strain / force / FPS / cycle life  
- Soft TB ≠ Mech OB-M5 · no NEXT_PROMPT write · no spend chase

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Label | **DESIGN ESTIMATE** — teach/overlay only |
| Critical C-01 / B-06 | **OPEN** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-22 ET · awaiting Ola disposition —
