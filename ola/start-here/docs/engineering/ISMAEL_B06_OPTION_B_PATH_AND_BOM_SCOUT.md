# B-06 Option B — path freeze sketch + mechanical BOM / supplier scout

| Field | Value |
|---|---|
| **Title** | Option B root/pitch hardware path freeze sketch + no-PO BOM/supplier scout (mechanical) |
| **Author** | Ismael (Soft Robotics desk draft for Ola disposition) |
| **Lead** | Ola (Lead Robotics) |
| **Date** | 2026-09-21 ET |
| **Status** | **DRAFT — ready for Lead review** |
| **Critical B-06** | **OPEN** (do not close) |
| **PO** | **NONE** — $0; quotes/scout language only |
| **Normative lock bit** | `pitch_lock_engaged` (Lead ask 2026-09-21) |
| **Soft Blender soft-body remakes** | **Out of scope** / not a gate |
| **Canonical SoR target (parent CopyFromBox)** | `C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\docs\engineering\ISMAEL_B06_OPTION_B_PATH_AND_BOM_SCOUT.md` · machineId `c9e3c1b7-3db3-4333-a063-5b46c67938f9` |
| **Box staging** | `/workspace/boxing-trainer/drafts/` · `/workspace/boxing-trainer/docs/engineering/` · `/workspace/boxing-trainer/sor_sync/` |

**Companion Lead papers (read / continue):** `B06_OPTION_B_INTERFACE_FREEZE.md`, `B06_OPTION_B_FEA_SCOPE.md`, `B06_ROOT_PITCH_HARDWARE_SKETCH.md`, `BUILD_INTENT_BOM.md`.  
**Peer scouts:** Soft `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` (Accepted-A tube/eye keep-outs); Elias `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` §5 pitch lock switches (**cite, do not re-primary**).

---

## Structured findings (Soft desk style)

### Summary
Paper freezes the **Option B pinned short/mid/tall** mechanical path sketch (mast → yaw → pitch pin plate → recessed soft boot → textile eye → continuum; flex-loop services under finite yaw) and scouts **catalog-candidate** mechanical parts for quoting. Critical **B-06 stays OPEN**. Soft-termination geometry/keep-outs are in Ismael lane; structural sizing, CAD lock, bearing ratings, and FEA disposition stay Lead. Soft Blender soft-body remakes are not a gate. No PO.

### Findings (severity)

| Severity | Finding |
|---|---|
| **High (process)** | Critical B-06 remains OPEN — no fab release, no invented N·m / MPa / force / cycle / FEA PASS. |
| **High (ICD)** | Normative bit spelling is **`pitch_lock_engaged`** before S3 pressurized strike; switch mounting geometry **ASSUMPTION** until Mech CAD. |
| **Med** | McMaster-Carr unit dollars are **masked** in public fetch this session → many pin/bumper families cited by **family URL only** (**NOT IN SOURCE** for $). Alternate US catalogs used where dollars verified. |
| **Med** | Pivot shaft / bushing / bearing **sizing OPEN** (Lead); scout lists SAE 841 sleeve class as candidate only — not a rating. |
| **Low** | Soft Blender soft-body remakes explicitly out of scope / not a gate for this paper. |
| **Info** | Pitch lock switch pricing stays with Elias §5 (Omron D4N / Honeywell BZ); this paper **pointers only**. |

### Draft recommendations (for Ola — not Closed)
1. Accept Option B path freeze sketch as quoting language (pinned presets; Option A bolt circle reserved; flex-loop MVP).
2. Keep Soft-termination ICD (textile-eye / strain relief / hose chafe keep-out) under Ismael; structural plate/pin/FEA under Lead.
3. When Stephen opens spend: Mech fixture kit first (pins + plate blank + bushings + bumpers + fasteners + flex-loop tube) — **no PO from this doc**.
4. Align Controls twin to `pitch_lock_engaged` only; retire informal aliases in ICD text at Lead disposition.

### Test gaps
See §8. Track B / Stephen-gated: pin engagement sense fixture, textile-eye pull coupon, hose flex at pitch presets, pinch-gap review — none close B-06 alone.

### Open questions for Ola
See §9.

---

## 1. Summary (plain language)

For the first hardware path we freeze **manual pinned height presets** (short / mid / tall) at the protected root. Metal stays behind padding; soft arm still punches. Services through pitch use an **MVP flex hose loop** under finite yaw (rotary union later if continuous spin). Soft root ends in a **textile eye** into a **recessed boot** — no distal exposed metal. Reach uses **Option A stand-off** (no continuum lengthening). Camera-in-hand is **not** a gate for this mechanical freeze. Soft Blender soft-body remakes are **out of scope**.

This paper: (1) restates the path freeze sketch continuing Lead B-06 papers; (2) scouts mechanical catalog candidates + public lead-time language only. **No purchase orders. Critical B-06 OPEN.**

---

## 2. Locks / freeze bits

| Item | Freeze | Source |
|---|---|---|
| Pitch architecture | **Option B — pinned presets** (detent / pin + flag). Option A actuated = later upgrade; same boot bolt circle reserved | Lead `B06_OPTION_B_INTERFACE_FREEZE` |
| Height set | Discrete **short / mid / tall** (Track A teaching angles are drawing aids, not hardware ratings) | Lead freeze + pedagogy ACCEPTED-A |
| Stack order (outboard) | Mast hub → yaw cartridge → **pitch pin plate** → recessed soft boot → textile eye → continuum | Lead freeze |
| Services through pitch | MVP **flex hose loop** (finite yaw); rotary union only if continuous spin later | Lead freeze; Soft keep-outs Accepted |
| Soft termination | Textile eye / harness into **recessed boot**; last exposed distal metal **forbidden** | Lead + Soft BOM scout |
| Stand-off | **Option A** reach policy — **no continuum lengthening** | Lead freeze |
| Branches | **8 independent** pneumatic branches; never serial U→F | Soft / Stage 0 freeze |
| Controls lock bit | Pin/flag engaged → **`pitch_lock_engaged`** required before **S3** pressurized strike | Lead ask 2026-09-21; Elias twin table |
| Camera-in-hand | **NOT a gate** for Option B mechanical freeze | This draft (Soft desk) |
| Soft Blender soft-body remakes | **Out of scope** / not a gate | This draft |
| Critical B-06 | **OPEN** until designed + analyzed + prototype | Lead |

**ASSUMPTION (ICD align-to-Lead):** Older informal Control/Mech prose may have used aliases such as “pitch locked,” “lock engaged,” or generic “pin seated” language. Normative twin/ICD spelling is **`pitch_lock_engaged`** only. Any residual alias in peer drafts is **ASSUMPTION → align-to-Lead** at disposition (do not invent alternate bit names in new twin code).

---

## 3. Path freeze sketch (stack)

```
  [mast / fixed hub]
           |
  [yaw cartridge / rotor]  ← finite yaw; encoder/limit ICD TBD (Elias)
           |
  [pitch pin plate (Option B)]  ← short / mid / tall pin holes + hard stops
           |     pin + visual flag ──► limit/flag switch ──► pitch_lock_engaged
           |
  [recessed soft boot]  ← last metal; padding keep-out; service access
           |
  [textile eye / webbing harness]  ← Soft ICD (geometry class; no ratings)
           |
  [soft continuum 8 chambers]  ← no distal exposed metal
           |
  [soft wrist / glove]

  SERVICES (MVP): 8× flex-loop hose bundle at root
    - loop volume inside chafe keep-out / outside pitch pinch planes
    - survives discrete preset change (pin remove/re-pin), not continuous pitch servo
    - Option A stand-off: do NOT lengthen continuum to buy hose length
```

**Quoting classes (this scout):** OB-M1…OB-M7 mechanical + OB-S1 pointer to Elias. Soft modules priced in Soft BOM scout; presence/E-stop/yaw encoder in Elias scout.

---

## 4. Soft-termination ICD notes (geometry class only — Ismael lane)

**In scope for Ismael:** textile-eye geometry class, strain relief narrative, hose loop / chafe keep-out vs pin plate. **Out of scope for Ismael (Lead):** structural sizing, CAD lock, bearing/pin ratings, FEA PASS/FAIL.

| Topic | Note | Ratings |
|---|---|---|
| Textile eye | Soft load path ends in webbing / eye harness entering recessed boot; geometry-class analogs include sailmaker D-ring / eye-strap families (Soft SM-C6) | **No peel/pull N** |
| Strain relief | Gradual textile → eye → boot; hose loop exits boot **without** bearing Soft structural load | **No ratings** |
| Hose loop / chafe | Flex-loop inside boot/guard; abrasion sleeve at metal lip / eye / pin plate contact; do not route below selected tube family’s **published** min bend radius (cite Soft §3 / Festo PUN / NITRA catalogs) | Catalog bend radii only — not Soft load ratings |
| Preset motion | Bundle must survive **discrete** pitch changes + service; keep-out sized for preset envelopes, **not** continuous servo sweep | — |
| Option A stand-off | Flex-loop volume from root packaging, **not** longer continuum | — |

**ASSUMPTION:** Exact eye ID/OD, stitch pattern, and boot bolt circle dimensions wait Mech CAD + Soft DFM freeze — **not invented here**.

---

## 5. Controls ICD hook — `pitch_lock_engaged`

| Rule | Statement |
|---|---|
| Normative bit | **`pitch_lock_engaged`** (Lead 2026-09-21) |
| Gate | Required before **S3 pressurized strike**; **not** required for S0/S1 twin / yaw pedagogy |
| Detection intent | Option B pin seated / flag home → limit or plunger switch (B-06 F-01) + visual pin flag |
| Twin / ICD cites | `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md`; `CONTROLS_INHIBIT_ESTOP_LIMP_ICD.md`; Elias BOM scout **§5** |
| Switch class (primary) | **Pointer to Elias §5** — Omron **D4N** (ex. D4N-1120) / Honeywell **BZ** (ex. BZ-2RQ1-A2). Do **not** re-price as primary here |
| **ASSUMPTION** | Switch mounting cam/flag geometry and actuation travel are **TBD after Mech CAD** of pin plate; Controls wires fail-safe (false/unknown → inhibit S3) |

---

## 6. BOM / supplier scout table (no PO)

**Method:** WebSearch + WebFetch of public US catalog pages 2026-09-21 ET.  
**Rule:** Price / lead-time language **only** if seen on a public page this session; else **NOT IN SOURCE** / **NOT PUBLICLY LISTED**. Candidates only — not frozen selections. No invented N·m, MPa, force, cycle life, or FEA PASS.

| Class ID | Part class | Example catalog family / SKU (candidate only) | Role | Public price band OR NOT IN SOURCE | Public lead-time language OR NOT IN SOURCE | Source URL | Notes / ASSUMPTIONS |
|---|---|---|---|---|---|---|---|
| **OB-M1** | Clevis / quick-release / detent pin class for presets | Fastenal-class cotterless detent / hitch pin — ex. reseller listing **0157078** (5/16″ × 4-5/8″ eff. zinc detent). McMaster locking quick-release / clevis pin **families** also candidates | Discrete short/mid/tall pin engagement + removable service | Freer Tool public list **$4.03** ea (0157078). McMaster unit $: **NOT IN SOURCE** (masked 000000 in fetch) | Freer: “contact Sales for all lead times”; stock note “In-Stock: 294” on that page. McMaster: **NOT PUBLICLY LISTED** beyond catalog availability language | https://www.freertool.com/products/fts-0157078 · https://www.mcmaster.com/products/locking-quick-release-pins/ · https://www.mcmaster.com/products/pins/pin-type~clevis/ | **ASSUMPTION:** diameter/usable length TBD after plate thickness + cheek stack. Gym sweat → prefer stainless / coated candidates at Lead pick. Not a shear rating. |
| **OB-M2** | Pitch plate / cheek plate hardware | Laser-cut aluminum plate blank class — **SendCutSend** sheet-cutting (5052 / 6061 families). Stock plate blank path: OnlineMetals / Similar mill plate (page verify blocked this session) | Pitch pin plate + cheek plates; three preset holes + bolt circle to boot | SendCutSend **pricing examples** on public page from **$19.51/ea** (illustrative small laser-cut parts; geometry-dependent). Exact Option B plate $: **NOT IN SOURCE** until CAD upload. OnlineMetals live unit: **NOT IN SOURCE** (Cloudflare block this session) | SendCutSend: free US shipping language on orders ≥$39; lead time **NOT PUBLICLY LISTED** as fixed days on pricing page (instant quote after file). OnlineMetals: **NOT IN SOURCE** | https://sendcutsend.com/pricing/ · https://sendcutsend.com/materials/6061-aluminum/ · https://www.onlinemetals.com/ | **ASSUMPTION:** plate alloy/thickness/hole pattern Lead CAD. Language = stock or laser-cut **candidate** — **no fab drawing claim**. No FEA PASS. |
| **OB-M3** | Pivot shaft / bushing or bearing class | SAE 841 oil-impregnated bronze sleeve — ex. Bunting **EP101210** (5/8″ ID × 3/4″ OD × 5/8″ L) on MROSupply. McMaster sleeve / ball bearing families as alt. MISUMI precision pivot pin family (ex. CDGH) cited in search — live unit **not re-verified** this session | Pitch hinge support between yaw flange and pin plate | MROSupply public **$1.72** ea (EP101210). MISUMI CDGH live $ this session: **NOT IN SOURCE** (fetch timeout / Cloudflare). McMaster $: **NOT IN SOURCE** (masked) | MROSupply: “Typically Ships in: 1 day”. MISUMI/McMaster ship language: **NOT IN SOURCE** this capture | https://www.mrosupply.com/products/579599/as-markdown/ · https://www.grainger.com/product/BUNTING-BEARINGS-Sleeve-Bearing-Bronze-12R737 · https://us.misumi-ec.com/ | **Sizing OPEN** (Lead). Catalog PV / temp on supplier pages are **not** adopted as Soft or root ratings. Ball bearing vs bushing = Lead disposition after load cases (`B06_OPTION_B_FEA_SCOPE`). |
| **OB-M4** | Hard stops / bumper class | Rubber / polyurethane threaded or screw-in bumper class — Grainger-model door/equipment bumper ex. **10192-017U** (1-1/2″ black rubber, 10 pk) via Raptor. McMaster threaded-stud PU bumper family (ex. 9223K*) | Energy absorption at pitch hard stops (F-06 intent) | Raptor public **$9.39 / pkg of 10** (ex. VAT listing; 2026-09-21 fetch). McMaster bumper $: **NOT IN SOURCE** (masked) | Raptor: “Ships within 2 days via …” + “10 In Stock” on page. McMaster: **NOT IN SOURCE** | https://www.raptorsupplies.com/pd/grainger/10192-017u · https://www.mcmaster.com/products/bumpers/ | **ASSUMPTION:** bumper size/durometer after mass props (Lead). No energy / cycle rating claimed. Door-bumper SKUs are **geometry class analogs**, not qualified machine stops until fixture test. |
| **OB-M5** | Recessed boot shell class | Polymer / sheet candidates: ABS sheet (ePlastics / TAP Plastics cut-to-size families); vacuum-form or CNC from sheet; optional industrial ABS enclosure scrap for mockup | Recessed soft boot shell hiding root metal; padding keep-out | Verified unit $ this session: **NOT IN SOURCE** (ePlastics / TAP fetches blocked or timed out). Family exists publicly | Lead time: **NOT PUBLICLY LISTED** without quote / cut size | https://www.eplastics.com/ · https://www.tapplastics.com/product/plastics/cut_to_size_plastic/abs_sheets/524 · https://www.mcmaster.com/products/abs-pvc-sheet-stock/ | **ASSUMPTION:** boot envelope after Soft textile-eye + hose loop volume. Structural strength of boot = Lead (with Soft interface notes). No distal metal beyond boot. |
| **OB-M6** | Fasteners / retainers class | Socket / button head cap screw class — AutomationDirect FATH fasteners PDF ex. **161100** M8-1.25 × 16 mm SHCS **$5.50 / 10 pk**; related 1/4-20 / M6 packs $1.00–$8.00 / 10. Cotter / retaining rings companion to clevis pins (McMaster family; $ masked) | Stack retention yaw↔pitch↔boot; pin retainers | ADC FATH catalog PDF publicly lists **$5.50/10** (161100) and neighboring SHCS packs **~$1.00–$8.25/10**. McMaster retainer $: **NOT IN SOURCE** | ADC free 2-day small-package policy language (site-wide; confirm at checkout). Exact pin-retainer ship: **NOT IN SOURCE** | https://cdn.automationdirect.com/static/specs/fathfasteners.pdf · https://www.mcmaster.com/products/retaining-pins/ | **ASSUMPTION:** final thread/length after CAD. FATH SKUs are T-slot rail oriented — treat as **fastener class price band**, not frozen root BOM PNs. |
| **OB-M7** | Flex-loop hose + fittings class | Align Soft tube freeze: **coupon** NITRA PU **6 mm** or **1/4″**; **prod prefer Festo PUN-H**. Fittings: NITRA push-to-connect union straight **US6M** / **US14** class | 8 independent branches through root flex-loop; chafe keep-out per Soft §3 | NITRA catalog PDF: PU6MBLK100 **$34.00**/100 ft; PU14BLK100 **$32.00**/100 ft; US6M **$10.00**/5 pk; US14 **$10.00**/5 pk; TC-12 cutter **$5.75**. Festo PUN-H unit $: **NOT PUBLICLY LISTED** (datasheet) | ADC: free 2-day small-package language when stocked; example backorder language seen on other NITRA reels (ex. PU6MCLR500 “Backordered… earliest 11/30/2026” on ADC product page search snapshot) — **confirm live SKU**. Festo lead: **NOT PUBLICLY LISTED** | Soft scout: `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` SM-C4 · https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf · https://cdn.automationdirect.com/static/specs/nitraunionstraight.pdf · https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF | Cite Soft for bend-radius keep-outs. **ASSUMPTION:** tube OD freeze still Lead/Soft joint (NITRA coupon vs Festo PUN-H prod). 8 branches never serial U→F. |
| **OB-S1** | Pitch lock sense switch | **Pointer to Elias §5** — Omron **D4N** (ex. D4N-1120) / Honeywell **BZ** (ex. BZ-2RQ1-A2) | Assert `pitch_lock_engaged` when pin/flag seated | **Do not re-price as primary.** Elias scout snapshot bands ~**$35–$45** (D4N aggregators) / ~**$22.79** (BZ Digi-Key-cited) — re-verify on Elias paper before any requisition | See Elias §5 / §9 open list (fork-lever D4N exact SKU band NOT IN SOURCE there) | `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` §5 · Omron D4N family https://automation.omron.com/en/ca/products/family/D4N | **ASSUMPTION:** Mech CAD defines cam/flag before Controls freezes actuator style (roller vs plunger). |

### Price found vs NOT IN SOURCE (row count)

| Rows in table | With public $ band this session | NOT IN SOURCE / pointer-only for $ |
|---|---|---|
| **8** (OB-M1…M7 + OB-S1) | **6** with at least one verified public $ example (M1 Freer; M2 SendCutSend example; M3 MROSupply; M4 Raptor; M6 ADC FATH; M7 NITRA) — note M2 example is **illustrative geometry**, not Option B plate | **OB-M5** shell unit $ NOT IN SOURCE; **OB-S1** pointer to Elias (not re-priced as primary); McMaster $ generally NOT IN SOURCE |

*(If counting strictly “Option B plate-specific $”: OB-M2 exact = NOT IN SOURCE; SendCutSend $19.51 is example-part language only.)*

---

## 7. Open dimensions / TBD table (no invented numbers)

| Item | Owner | Status |
|---|---|---|
| Pin diameter / usable length / material | Mech / Lead | TBD — after cheek stack |
| Preset angles (hardware) vs Track A teaching angles | Lead | Teaching angles ≠ ratings |
| Pitch travel / hard-stop range | Lead | TBD anthropometry + boot keep-out |
| Bearing / bushing ID-OD-L and capacity | Lead | OPEN — FEA scope assumed loads only |
| Boot bolt circle / keep-out envelope | Lead + Soft ICD | TBD CAD |
| Hose loop volume / min bend at hinge | Soft cite catalogs + Mech | Catalog R_min only; fixture TBD |
| Switch cam/flag travel | Mech → Controls | ASSUMPTION until CAD |
| Glove + arm mass properties | Lead / Track C | NOT IN SOURCE — no fake kg |
| Pinch gap qualification | Safety / Lead | OPEN before user-adjacent demo |

---

## 8. Test gaps / Track B & Stephen-gated fixtures

| Gap | Why it matters | Gate |
|---|---|---|
| Pin engage / disengage + `pitch_lock_engaged` sense | F-01 unlock under gravity / punch reaction | Controls + Mech fixture (Stephen when spend opens) |
| Textile-eye pull / peel coupon into recessed boot mock | Soft termination retention (F-03) — **no rating invented here** | Soft coupon + Lead B-06 |
| Hose flex at short/mid/tall presets + chafe inspection | F-04 hose pinch/fatigue | Soft + Mech; RH-03 bend table later |
| Hard-stop bumper hit (fixture mass) | F-06 shock | Mech after mass props |
| Pinch / guard review | F-08 user proximity | Safety before pilot |
| Static load / FEA on pin plate | G2 in root sketch — **scope only today** (`B06_OPTION_B_FEA_SCOPE`) | Stephen analyst path if Lead routes |
| Soft Blender soft-body remake | **Not required / not a gate** | Explicitly out of scope |

Track A pedagogy films ≠ System ID and do **not** close G2–G5.

---

## 9. Open questions for Ola (Lead)

1. Confirm **Option B path freeze sketch** (§3) as quoting language for first fixture (pinned short/mid/tall; Option A bolt circle reserved)?
2. Confirm Soft-termination ICD ownership remains **Ismael** (geometry/keep-outs) while structural plate/pin/FEA stays **Lead**?
3. Prefer **detent/ball-lock pin** vs **clevis + cotter** for operator changeover + visual flag coupling to D4N/BZ?
4. Bushing (SAE 841) vs commercial ball bearing for MVP pitch hinge — wait FEA scope load cases first?
5. Boot shell path: cut ABS sheet mock → vacuum form, or jump to molded/printed after envelope CAD?
6. When Stephen opens spend: authorize **Mech fixture kit band** (OB-M1…M7 samples) separate from Soft TB-01/TB-02?
7. ICD sweep: retire any residual lock-bit aliases to **`pitch_lock_engaged`** only across twin + inhibit docs?
8. Confirm camera-in-hand and Soft Blender soft-body remakes remain **non-gates** for B-06 mechanical path?

---

## 10. Non-claims

- **No purchase orders** from this document; **$0**.
- Critical **B-06 remains OPEN** — not fab release; not consumer-ready.
- **No invented** quotes, prices, lead times, N·m, MPa, force ratings, cycle life, or FEA PASS/FAIL.
- Prices are **public catalog snapshots** 2026-09-21 ET; re-verify before any requisition.
- Soft Blender soft-body remakes are **out of scope** / not a gate.
- This paper does **not** touch `chats/NEXT_PROMPT.md` or any NEXT_PROMPT.
- Spend, if Lead routes, goes through **Stephen / CFO**.
- Catalog candidates ≠ frozen supplier selection.

---

## Research sources (session)

1. Lead: `/workspace/_b06_gather/B06_OPTION_B_INTERFACE_FREEZE.md`  
2. Lead: `/workspace/_b06_gather/B06_OPTION_B_FEA_SCOPE.md`  
3. Lead: `/workspace/boxing-trainer/sor_sync/B06_ROOT_PITCH_HARDWARE_SKETCH.md`  
4. Lead: `/workspace/_b06_gather/BUILD_INTENT_BOM.md`  
5. Elias: `ELIAS_CONTROLS_SENSING_BOM_SUPPLIER_SCOUT.md` §5  
6. Soft: `ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md` (SM-C4/C6 + §3 keep-outs)  
7. https://www.freertool.com/products/fts-0157078  
8. https://www.mcmaster.com/products/locking-quick-release-pins/  
9. https://www.mcmaster.com/products/pins/pin-type~clevis/  
10. https://sendcutsend.com/pricing/  
11. https://www.mrosupply.com/products/579599/as-markdown/  
12. https://www.raptorsupplies.com/pd/grainger/10192-017u  
13. https://cdn.automationdirect.com/static/specs/fathfasteners.pdf  
14. https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf  
15. https://cdn.automationdirect.com/static/specs/nitraunionstraight.pdf  
16. https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF  
17. https://www.sailmakerssupply.com/product/1-inch-welded-d-ring/webbing-accessories (Soft eye analog cross-ref)  
18. Elias twin: `ELIAS_TWIN_ADAPTER_SIGNAL_TABLE.md` (`pitch_lock_engaged`)

---

## Document control

| Field | Value |
|---|---|
| Status | DRAFT — ready for Lead review |
| Critical B-06 | **OPEN** |
| PO | **None** |
| NEXT_PROMPT | **Not touched** |
| Research date | 2026-09-21 ET |

— Ismael · Soft Robotics Desk · MYORGLAB · draft for Ola disposition
