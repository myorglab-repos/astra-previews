# ISMAEL — Soft Return / Vent Time-Order DESIGN ESTIMATE (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Disposition** | PAPER — vent vs elastic return **time-order DESIGN ESTIMATE** only |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** (Lead) |
| **PO** | **NONE** |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_RETURN_VENT_TIME_ORDER_2026-09-21.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_RETURN_VENT_TIME_ORDER_2026-09-21.md` |

**Cites:** `ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` §4.4 (ACCEPTED-A); twin deepen τ props; C-01 sizing lumen volumes; Soft BOM scout tube OD / bend cites.

**Standing rule:** Labeled **DESIGN ESTIMATE** — **not** cycle life; **not** System ID; **not** measured TB-04.

---

## Summary

Orders two return mechanisms after a vent command: (1) **elastic** stored-strain snapback time-scale \(\tau_{\mathrm{el}}\sim\sqrt{m/k_{\mathrm{eff}}}\) from ACCEPTED-A physics; (2) **vent-conductance** discharge time-scale \(\tau_{\mathrm{vent}}\) from chamber lumen volume through **ASSUMPTION** orifice / tube OD. Planning takeaway: for Ecoflex-class sections with glove tip mass, **vent often dominates** elastic \(\tau_{\mathrm{el}}\) under small orifice ASSUMPTIONs — TB-04 must measure tip return history. **Not cycle life.**

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| VT-01 | High | Elastic τ is a **lower-bound hypothesis** after pressure is gone — vent lag often longer. |
| VT-02 | Med | Orifice / tube OD ASSUMPTIONs drive \(\tau_{\mathrm{vent}}\) order — Soft DFM not frozen. |
| VT-03 | Med | Limp bladder **cannot pull** — return work = elastomer + textile + return bands. |
| VT-04 | Info | Twin `tau_return_s` should use max(τ_el, τ_vent) or longer orifice lag — stamp twin ≠ ID. |
| VT-05 | Info | This pack does **not** claim cycle life, fatigue, or product duty cycle. |

---

## Equations

### Elastic return (**DESIGN ESTIMATE** — ACCEPTED-A §4.4)

\[
k_{\mathrm{eff}} \approx \frac{3\,EI_{\mathrm{eff}}}{L^{3}},\qquad EI_{\mathrm{eff}}=\eta E I,\qquad \tau_{\mathrm{el}} \sim \sqrt{\frac{m}{k_{\mathrm{eff}}}}
\]

**ASSUMPTION:** \(L=L_{U+F}=0.720\,\mathrm{m}\); \(R_{\mathrm{sec}}=45\,\mathrm{mm}\); glove mass baseline **14 oz = 0.397 kg**.

### Vent-dominated discharge (**DESIGN ESTIMATE** pedagogy)

Chamber lumen:

\[
V = \pi r^{2} L
\]

Orifice Bernoulli-order volume flow (**ASSUMPTION** idealization — isothermal/choked refinements omitted):

\[
Q \approx C_d A_o \sqrt{\frac{2\,\Delta P}{\rho_{\mathrm{air}}}},\qquad A_o=\pi (d_o/2)^{2}
\]

One-volume exchange time order:

\[
\tau_{\mathrm{vent,1V}} \sim \frac{V}{Q}
\]

Tube friction lengthens \(\tau_{\mathrm{vent}}\) vs bare orifice — treat table as **order-of-magnitude**, recalibrate TB-04.

**Combined planning return time:**

\[
\tau_{\mathrm{return,plan}} \gtrsim \max(\tau_{\mathrm{el}},\, \tau_{\mathrm{vent}})
\]

(plus any return-band / textile dissipation — **NOT IN SOURCE** quantitatively).

---

## ASSUMPTION orifice / tube OD (plain sight)

| Item | Value | Tag |
|---|---|---|
| Coupon / provisional tube OD | **NITRA 6 mm or 1/4″** | **ASSUMPTION** (OD freeze open) |
| Prod lean tube | **Festo PUN-H** class | **ASSUMPTION** context |
| Effective ID for flow order | **~4 mm** (6 mm OD PU class) | **ASSUMPTION** |
| Tube run length class | **0.5–1.5 m** root→coupon | **ASSUMPTION** |
| Orifice / valve effective diameter | **1.0 mm** and **1.5 mm** cases | **ASSUMPTION** planning |
| Discharge coefficient \(C_d\) | **0.60** | **ASSUMPTION** |
| Air density \(\rho_{\mathrm{air}}\) | **1.2 kg/m³** | **ASSUMPTION** (STP order) |
| ΔP for Q estimate | **40 kPa** (Ecoflex p_norm map) | **HYPOTHESIS** map — not product P |
| Chamber mid geometry | \(r=30\,\mathrm{mm}\), \(L=200\,\mathrm{mm}\) (TB-01 mid) | **ASSUMPTION** (sizing math) |
| Section continuum L | \(0.720\,\mathrm{m}\) for elastic τ | **ASSUMPTION** mid GEOMETRY TARGET |

---

## Elastic \(\tau_{\mathrm{el}}\) card (**DESIGN ESTIMATE** — from ACCEPTED-A)

| Material | \(\eta\) | \(m\) | \(\tau_{\mathrm{el}}\) | Tag |
|---|---|---|---|---|
| Ecoflex 00-30 | 0.20 | 14 oz | **~810 ms** | **DESIGN ESTIMATE** |
| Ecoflex 00-30 | 0.35 | 14 oz | **~610 ms** | **DESIGN ESTIMATE** |
| Ecoflex 00-30 | 0.35 | 12 / 16 oz | ~560 / ~650 ms order | **DESIGN ESTIMATE** |
| Dragon Skin 30 | 0.20 | 14 oz | **~275 ms** | **DESIGN ESTIMATE** |
| Dragon Skin 30 | 0.35 | 14 oz | **~210 ms** | **DESIGN ESTIMATE** |
| DS10 / DS20 | — | 14 oz | Between Eco and DS30 (rank by \(E\)) | **DESIGN ESTIMATE** interpolate |

**Critical caveat:** elastic \(\tau_{\mathrm{el}}\) assumes pressure already gone — **vent not included**.

---

## Vent \(\tau_{\mathrm{vent}}\) card (**DESIGN ESTIMATE**)

**Lumen:** TB-01 mid \(V=0.565\,\mathrm{L}\); TB-02 one-ch mid \(V=0.707\,\mathrm{L}\) (sizing math).

| Case | \(d_o\) | \(Q\) order @ 40 kPa | \(\tau_{\mathrm{vent,1V}}\) @ TB-01 mid | Tag |
|---|---|---|---|---|
| Small orifice | **1.0 mm** | ~1.2×10⁻⁴ m³/s | **~4.7 s** | **DESIGN ESTIMATE** |
| Mid orifice | **1.5 mm** | ~2.7×10⁻⁴ m³/s | **~2.1 s** | **DESIGN ESTIMATE** |
| Longer tube friction | same orifices + 0.5–1.5 m run | lower effective Q | **~2–10 s** planning band | **HYPOTHESIS / DESIGN ESTIMATE** |
| Multi-chamber TB-02 (3× mid lumen order) | — | 3× volume class | **longer** than single | **DESIGN ESTIMATE** order |

---

## Vent-dominated vs elastic — time-order takeaway

| Material class | \(\tau_{\mathrm{el}}\) order | \(\tau_{\mathrm{vent}}\) order (1–1.5 mm orifice ASSUMPTION) | Which dominates? | Tag |
|---|---|---|---|---|
| Ecoflex + 14 oz | **~0.6–0.8 s** | **~2–5+ s** | **Vent-dominated** | **DESIGN ESTIMATE** |
| DS30 + 14 oz | **~0.2–0.3 s** | **~2–5+ s** | **Vent-dominated** | **DESIGN ESTIMATE** |
| Large vent path / short pigtail | same \(\tau_{\mathrm{el}}\) | may approach ~1 s | Contested — measure TB-04 | **HYPOTHESIS** |

**Planning rule for twin / fault-vent narrative:** animate return on \(\tau_{\mathrm{return,plan}}\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) — typically **seconds**, not pure elastic hundreds of ms — until TB-04 overwrites.

**NOT cycle life:** no fatigue N, no duty-cycle Hz, no product endurance claim.

---

## ASSUMPTION tables

| # | ASSUMPTION |
|---|---|
| A1 | Glove mass 14 oz = 0.397 kg baseline |
| A2 | Neo-Hookean E / η / R_sec from ACCEPTED-A physics |
| A3 | Orifice d_o ∈ {1.0, 1.5} mm; C_d=0.60; ρ_air=1.2 |
| A4 | Tube OD provisional NITRA 6 mm / 1/4″; ID~4 mm class |
| A5 | ΔP=40 kPa for Q arithmetic = Ecoflex p_norm map **HYPOTHESIS** |
| A6 | Bernoulli orifice idealization — no choked/isothermal refinement |
| A7 | Return-band / textile dissipation time **NOT IN SOURCE** quantitatively |
| A8 | DESIGN ESTIMATE ≠ TB-04 measured return ≠ cycle life |

---

## Draft recommendations

1. Accept vent-vs-elastic time-order as Soft DESIGN ESTIMATE companion to ACCEPTED-A §4.4.  
2. Twin / fault-vent pedagogy: prefer **vent-dominated** seconds-class return until TB-04.  
3. Soft DFM should document vent orifice / valve effective area when Stephen opens Soft TB band.  
4. Do **not** publish cycle life from this pack.

---

## Test gaps

| Gap | Status |
|---|---|
| TB-04 tip return time history | OPEN — required overwrite |
| Measured orifice / valve conductance | NOT IN SOURCE |
| Multi-chamber simultaneous vent | OPEN |
| Return-band preload effects | NOT IN SOURCE |
| Cycle life / fatigue | OUT OF SCOPE — never claimed here |

---

## Open questions for Ola

1. Accept vent-dominated planning return (seconds class) as Soft DESIGN ESTIMATE?  
2. Confirm twin `tau_return_s` may be set longer than elastic τ to model orifice lag?  
3. Preferred Soft DFM note: document vent effective diameter before multi-chamber TB-04?  
4. Any freeze delta to elastic-return architecture (stored strain, not suction)?

---

## Non-claims

- **Not cycle life** · not System ID · not measured TB-04  
- No PO · C-01 OPEN · B-06 OPEN  
- No invented lab return times as product ID  
- No NEXT_PROMPT write

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Label | **DESIGN ESTIMATE** — not cycle life |
| Critical C-01 / B-06 | **OPEN** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |

— Ismael · Soft Robotics Desk · 2026-09-21 ET · awaiting Ola disposition —
