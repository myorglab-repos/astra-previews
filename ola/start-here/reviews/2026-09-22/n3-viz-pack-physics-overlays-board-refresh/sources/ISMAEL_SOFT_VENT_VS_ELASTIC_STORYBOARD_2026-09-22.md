# ISMAEL — Soft Vent-vs-Elastic Return ASSUMPTION Storyboard (PAPER)

| Field | Value |
|---|---|
| **Author** | Ismael (Soft Robotics Desk) · MYORGLAB |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-22 ET |
| **Disposition** | PAPER — Track A film storyboard beats only |
| **Critical C-01** | **OPEN** |
| **Critical B-06** | **OPEN** |
| **PO** | **NONE** — $0 digital |
| **SoR target** | `docs/engineering/ISMAEL_SOFT_VENT_VS_ELASTIC_STORYBOARD_2026-09-22.md` |
| **Box path** | `/workspace/boxing-trainer/drafts/docs/engineering/ISMAEL_SOFT_VENT_VS_ELASTIC_STORYBOARD_2026-09-22.md` |

**Cites (do not overwrite):**  
`ISMAEL_SOFT_RETURN_VENT_TIME_ORDER_2026-09-21.md` (Soft DESIGN ESTIMATE);  
`ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md` §4.4 (**ACCEPTED-A**);  
`ISMAEL_VIRTUAL_SOFT_ARM_TWIN_DEEPEN_2026-09-21.md` (**ACCEPTED-A** paper);  
`ISMAEL_C01_COUPON_SIZING_MATH_2026-09-21.md` lumen volumes;  
`ISMAEL_SOFT_PHYSICS_MATH_INTEGRATE_2026-09-21.md` E10–E12.

**Standing:** Labeled **ASSUMPTION** timing bands — **not cycle life**; **not** measured TB-04; **no invented FPS claims as measured**. Soft idle on live `.blend`. Soft TB ≠ Mech OB-M5. Zero spend language.

---

## Summary

Still-frame / storyboard beats for Track A film teaching vent-dominated return vs elastic snapback, drawn only from ACCEPTED-A §4.4 + Soft vent time-order DESIGN ESTIMATE. Timing bands are **ASSUMPTION / DESIGN ESTIMATE** for animation pacing — **not** product duty cycle, **not** TB-04 ID. Prefer animate on \(\tau_{\mathrm{return,plan}}\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) — typically **seconds**, not pure elastic hundreds of ms.

---

## Findings

| ID | Severity | Finding |
|---|---|---|
| SB-01 | High | Elastic τ is lower-bound after pressure gone — vent lag often longer (VT-01). |
| SB-02 | Med | Storyboard must stamp every beat: DESIGN ESTIMATE / twin ≠ ID / not cycle life. |
| SB-03 | Med | Orifice / tube OD ASSUMPTIONs drive τ_vent — Soft DFM not frozen. |
| SB-04 | Info | No measured FPS / return time claimed — animation frame counts are teaching aids only. |
| SB-05 | Info | Soft idle on live blend; CloudAgent may use beats as caption inputs. |

---

## ASSUMPTION timing bands (plain sight)

**ASSUMPTION kit (from vent time-order / ACCEPTED-A):**

| Item | Value | Tag |
|---|---|---|
| Glove mass | **14 oz = 0.397 kg** | **ASSUMPTION** |
| \(L_{U+F}\) | **0.720 m** | **ASSUMPTION** mid GEOMETRY TARGET |
| \(R_{\mathrm{sec}}\) | **45 mm**; \(\eta\in[0.20,0.35]\) | **ASSUMPTION** |
| Ecoflex τ_el @ η=0.35 / 14 oz | **~610 ms** | **DESIGN ESTIMATE** |
| Ecoflex τ_el @ η=0.20 / 14 oz | **~810 ms** | **DESIGN ESTIMATE** |
| DS30 τ_el @ η=0.35 / 14 oz | **~210 ms** | **DESIGN ESTIMATE** |
| Orifice \(d_o\) | **1.0 / 1.5 mm**; \(C_d=0.60\) | **ASSUMPTION** |
| ΔP for Q | **40 kPa** (Ecoflex p_norm map) | **HYPOTHESIS** — not product P |
| TB-01 mid lumen | **0.565 L** | **ASSUMPTION** geometry |
| τ_vent @ 1.0 mm | **~4.7 s** (1V) | **DESIGN ESTIMATE** |
| τ_vent @ 1.5 mm | **~2.1 s** (1V) | **DESIGN ESTIMATE** |
| Longer tube friction band | **~2–10 s** | **HYPOTHESIS / DESIGN ESTIMATE** |
| Planning return | \(\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) | **DESIGN ESTIMATE** |

**Takeaway for film:** Ecoflex + 14 oz → **vent-dominated** (~2–5+ s vs ~0.6–0.8 s elastic). **NOT cycle life.**

**Animation pacing note (not measured FPS):** Prefer a **seconds-class** return morph for pedagogy. Do **not** caption “measured at N fps” or invent lab capture rates. Any frame-count in a CloudAgent timeline is an **ASSUMPTION teaching aid** only.

---

## Storyboard beats (Track A film)

Stamp on every still: `DESIGN ESTIMATE · twin ≠ ID · not cycle life · C-01 OPEN`

| Beat | Still / action | On-screen caption (ASSUMPTION) | Timing band |
|---|---|---|---|
| **B0** | Title card | Soft return: elastic vs vent — DESIGN ESTIMATE pedagogy | — |
| **B1** | Arm at rest; chambers labeled U1–U3 / F1–F3 / T1–T2 | 8-chamber lock; elastic return architecture (stored strain, not suction) | Rest |
| **B2** | Inflate differential (e.g. F-side) | \(p_{\mathrm{norm}}\) → ΔP map **HYPOTHESIS** (Eco 40 kPa @ 1) | Inflate morph |
| **B3** | Hold pressurized pose | Tip δ / θ = bend **DESIGN ESTIMATE** (see HUD brief) — ≠ System ID | Hold |
| **B4** | Vent command fires (`SO_VENT_STATE`) | Vent event — pressure leaving chamber | t = 0 vent |
| **B5** | Elastic-only ghost overlay (optional dashed) | If pressure already gone: τ_el Eco ~**0.6–0.8 s** DESIGN ESTIMATE | **ASSUMPTION** elastic band ~0.6–0.8 s |
| **B6** | Primary return morph (vent-limited) | τ_vent order **~2–5+ s** @ 1–1.5 mm orifice ASSUMPTION | **ASSUMPTION** vent band ~2–5+ s |
| **B7** | Split-screen: τ_el vs τ_vent bars | \(\tau_{\mathrm{return,plan}}\gtrsim\max(\tau_{\mathrm{el}},\tau_{\mathrm{vent}})\) — **vent often dominates** | Compare |
| **B8** | Rest + limp-bladder callout | Limp bladder **cannot pull** — return work = elastomer + textile + return bands | Rest |
| **B9** | End card | Recalibrate TB-04 · **not cycle life** · Critical C-01 OPEN · Soft idle on live blend | — |

### Optional stills (coupon host — Soft paper only)

| Still | Content | Tag |
|---|---|---|
| S-TB01 | Single mid bladder vent narrative | TB-01 mid \(V=0.565\,\mathrm{L}\) **ASSUMPTION** |
| S-ORIF | Orifice icons 1.0 vs 1.5 mm | **ASSUMPTION** planning diameters |
| S-DS | DS30 comparative shorter τ_el (~0.2–0.3 s) still vent-dominated | **DESIGN ESTIMATE** |

---

## Recommended twin hooks for beats (ASSUMPTION / Lead-confirm)

| Hook | Storyboard use |
|---|---|
| `SO_VENT_STATE` | Beat B4 trigger |
| `tau_return_s` | Prefer vent-dominated seconds-class for B6 (not elastic-only) |
| `SK_REST_RETURN` | Morph to rest on τ_plan |
| HUD Card E | Overlay τ_el vs τ_vent bars on B7 |

---

## Draft recommendations

1. Accept storyboard as Soft Track A teach companion to ACCEPTED-A §4.4 + vent time-order pack.  
2. Animate primary return on **vent-dominated** seconds band until TB-04 overwrites.  
3. Never caption cycle life / measured FPS / System ID from these beats.  
4. Soft idle on live `.blend`; CloudAgent may keyframe from beats + HUD brief.

---

## Test gaps

| Gap | Status |
|---|---|
| TB-04 tip return time history | OPEN — required overwrite |
| Measured orifice / valve conductance | NOT IN SOURCE |
| Multi-chamber simultaneous vent | OPEN |
| Return-band / textile dissipation quantitative | NOT IN SOURCE |
| Cycle life / fatigue | OUT OF SCOPE — never claimed |

---

## Open questions for Ola

1. Accept vent-dominated seconds-class primary morph for Track A film?  
2. Authorize optional elastic-ghost overlay (B5) as pedagogy contrast only?  
3. Confirm Soft idle on live blend; CloudAgent may adopt beats?  
4. Preferred SoR land OK?

---

## Non-claims

- **Not cycle life** · not System ID · not measured TB-04  
- No invented FPS as measured · no PO · C-01 OPEN · B-06 OPEN  
- Soft TB ≠ Mech OB-M5 · no NEXT_PROMPT · no spend chase

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT for Lead review |
| Label | **DESIGN ESTIMATE** — storyboard / not cycle life |
| Critical C-01 / B-06 | **OPEN** |
| PO | **None** |

— Ismael · Soft Robotics Desk · 2026-09-22 ET · awaiting Ola disposition —
