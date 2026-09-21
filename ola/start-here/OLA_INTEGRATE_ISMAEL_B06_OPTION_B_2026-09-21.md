# Ola integrate — Ismael B-06 Option B path + BOM scout (2026-09-21)

| Field | Value |
|---|---|
| **Disposition** | **ACCEPTED-A (paper)** — quoting / freeze language |
| **Author** | Ola (Lead Robotics) |
| **Input** | `ISMAEL_B06_OPTION_B_PATH_AND_BOM_SCOUT.md` |
| **Authority** | Michael — keep building outside virtual media; no-PO scout; report path = Ola only |
| **Critical B-06** | **OPEN** (unchanged) |
| **PO** | **NONE** |

## Summary

Ismael’s Option B path freeze sketch + mechanical BOM scout is **ACCEPTED-A as quoting language**. It continues Lead `B06_OPTION_B_INTERFACE_FREEZE.md` and does **not** close Critical B-06, authorize fab, or invent N·m / MPa / FEA PASS. Soft-termination geometry stays Ismael; structural sizing / CAD / FEA stays Lead.

## Findings (Lead)

| Severity | Finding | Disposition |
|---|---|---|
| Critical OPEN | B-06 still needs design + analysis + prototype | **Keep OPEN** |
| High (ICD) | Normative bit `pitch_lock_engaged` | **Confirm** — alias sweep authorized |
| Med | Many McMaster $ masked; family URLs OK | Accept with NOT IN SOURCE rule |
| Med | Pivot sizing OPEN | Lead owns after FEA load cases |
| Info | Soft Blender soft-body remakes out of scope | **Confirm non-gate** |

## Lead answers — §9 open questions

1. **Option B path freeze (§3) as quoting language** — **YES.** Pinned short/mid/tall; Option A bolt circle reserved; flex-loop MVP; stack as drawn.
2. **Soft-termination ICD ownership** — **YES.** Ismael = textile-eye / strain relief / chafe keep-outs (geometry class). Lead = plate / pin / bearing / FEA.
3. **Detent vs clevis** — Prefer **detent / ball-lock / quick-release pin + visual flag** for operator changeover and D4N/BZ coupling (matches Option B freeze). Clevis + cotter = alternate only if flag coupling is impractical after Mech CAD (**ASSUMPTION** until CAD).
4. **Bushing vs ball bearing** — **Wait FEA scope load cases first.** SAE 841 sleeve class OK as **MVP fixture candidate only** — not a capacity freeze.
5. **Boot shell path** — **Cut ABS / sheet mock first** after envelope sketch; vacuum-form or molded/printed only after envelope CAD. Do not jump to molded day-one.
6. **Stephen spend band** — When Stephen opens spend: Lead recommends **Mech fixture kit (OB-M1…M7 samples)** as a **separate** band from Soft TB-01/TB-02. **No PO from this integrate.** Route through Stephen.
7. **ICD alias sweep** — **YES.** Twin + inhibit + Soft/Mech prose: normative spelling **`pitch_lock_engaged` only**. Retire “pitch locked” / informal aliases in new text; flag residual aliases ASSUMPTION → align.
8. **Non-gates** — **Confirm:** camera-in-hand and Soft Blender soft-body remakes are **not** gates for B-06 mechanical path.

## Engineering recommendations

- Treat Ismael table as the mechanical quoting companion to Elias sensing scout + Soft tube/eye scout.
- Next Lead mech work (no PO): envelope sketch dimensions list for pin plate + boot keep-out (still no invented loads).
- CloudAgent live-USB path continues in parallel; does not close B-06.

## Test / validation gaps (unchanged)

Pin sense F-01, textile-eye coupon, hose flex at presets, bumper fixture, pinch review, FEA G2 — all Stephen-gated when spend opens. Pedagogy films ≠ System ID.

## Manufacturing notes

Catalog candidates ≠ frozen PNs. Re-verify public $ before any requisition. OB-S1 switches stay Elias §5 primary.

## Open for Michael (non-blocking)

- When spend opens: Mech fixture kit first vs Soft TB coupons first vs both under one Stephen band?

## Plain-language glossary

| Term | Everyday meaning |
|---|---|
| Option B | Manual pinned height stops (short/mid/tall), not a motorized pitch joint |
| Quoting language | Parts classes we can price from catalogs — not a buy order |
| `pitch_lock_engaged` | Controls bit that means “pin is in” before real pressurized punches |
| NOT IN SOURCE | Price or lead time was not on a public page this session — do not invent it |
| ACCEPTED-A (paper) | Lead accepts the write-up as the working path — not fab release |

---

*Ola Lead Robotics — integrate 2026-09-21. B-06 Critical OPEN. No PO. Report path: Ola → Michael only.*
