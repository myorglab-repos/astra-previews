> **Ola integrate 2026-09-21: ACCEPTED-A (paper scout).** Lead locks without further Michael approvals: (1) **TB-01/TB-02 first path = in-house cast** (Smooth-On Ecoflex / Dragon Skin class) for System ID speed; custom molded bladder RFQ (Dynamic/ARC/Eutsler) only after cast coupons teach geometry. (2) **Manifold:** coupon bench = discrete / paired catalog manifolds (NITRA/SMC); production = custom or Twintec-class **8-branch** after tube OD freeze — not serial U→F. (3) Coupon tube OD provisional **NITRA 6 mm or 1/4″** until Soft DFM freezes; production prefer **Festo PUN-H**. Critical B-06 stays Lead. No PO.

# Soft-module BOM class list + supplier scout (PAPER ONLY)

**Author:** Ismael (Soft Robotics Desk) · MYORGLAB AI boxing trainer  
**Date:** 2026-09-21 ET  
**Doc class:** Paper-only BOM / supplier scout — **NO purchase orders**  
**Canonical SoR target (parent CopyFromBox):**  
`C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\docs\engineering\ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md`  
**Box staging:**  
- `/workspace/boxing-trainer/drafts/ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md`  
- `/workspace/_pc_sync/docs/engineering/ISMAEL_SOFT_BOM_SUPPLIER_SCOUT.md`

**Companion papers:** `ISMAEL_SOFT_ROBOTICS_OPEN_ITEMS_BRIEF` (ACCEPTED-A), `ISMAEL_SOFT_ACTUATOR_INVENTORY.md`, `ISMAEL_SOFT_ACTUATOR_FEASIBILITY_RISK_DRAFT.md`, `TRACK_B_SYSTEM_ID_PLAN.md`, `B06_ROOT_PITCH_HARDWARE_SKETCH.md`

---

## Freeze / locks (do not re-open in this paper)

| Lock | Binding statement |
|---|---|
| Continuum | Soft continuum **8 chambers/arm** (U1–U3, F1–F3, T1–T2); textile strain limit; elastic return; soft wrist; **no distal exposed metal** |
| Stand-off | **Option A** — no arm lengthening in Soft DFM / BOM geometry |
| Soft-termination ICD | Textile-eye geometry class + strain relief + hose loop/chafe keep-out (**no load ratings**) |
| Pitch MVP | **Option B pinned pitch** — keep-out notes align to **pinned preset**, not continuous pitch servo |
| Critical B-06 | Structural root/pitch/hub stays **Lead (Ola)** — Ismael = interface notes only |
| Coupon band (first spend) | When Stephen opens spend: **TB-01 + TB-02** first (bladder + section kits). Prefer **TB-*** IDs over legacy B-0x |
| Track A | Pedagogy / prescribed motion only — **≠ System ID** |

---

## Explicit non-claims

- **No PO authority.** This document does not authorize purchase, RFQ issuance as commitment, or inventory receipt.
- **No Critical close** (B-06, C-01 remain Lead/Track lanes).
- **Do not write / overwrite `chats/NEXT_PROMPT.md`.**
- **Stephen-gated spend** — coupon kits and any material buy wait CFO/Stephen open.
- **Track A ≠ System ID** — films/prescribed motion do not close Track B coupons.
- **No invented prices, SKUs, MOQs, load ratings, working pressures, or cycle lives.** Unknowns marked **NOT PUBLICLY LISTED** or **NOT IN SOURCE**.
- Prices below are **budgetary snapshot bands from public catalog pages as of research date**; they are not quotes and may change without notice.

---

## Coupon call-outs (TB-01 / TB-02)

| Coupon ID | Legacy map | Kit intent (paper) | BOM classes that feed pricing class |
|---|---|---|---|
| **TB-01** | B-01 (+ neck peel H-05) | Single sleeved-bladder coupon: P → axial strain; leak/peel; vent return | Class 1 (bladder/elastomer), Class 2 (registered textile), Class 4 (fittings/pigtails), Class 3 (return band optional for return path) |
| **TB-02** | B-04 (+ polarity) | Differential 3-chamber section (U or F): tip angle/curvature vs ΔP; registration | Class 1–4 + Class 5 (partial manifold / branch identity) + Class 2 registration yarn/textile |

**First Stephen coupon band when spend opens:** TB-01 + TB-02 only (unless Ola enlarges band).  
**ask_stephen:** Confirm budget envelope and whether TB-01/TB-02 are **in-house cast** (Smooth-On class) vs **supplier-molded bladder RFQ** before any buy.  
**ask_ola:** Confirm coupon kit path preference (in-house vs custom rubber house) for Soft DFM narrative.

---

## 1) Soft-module build-intent BOM class list

| Class ID | Class name | Role in Soft module | TB link |
|---|---|---|---|
| **SM-C1** | Sleeved bladders / elastomer candidates | Pressure vessels / chamber bodies (cast silicone or custom molded bladder/sleeve) | **TB-01** primary; **TB-02** multi |
| **SM-C2** | Registered textile / yarn | Strain-limiting sleeve, chamber ID registration, continuous textile load path | TB-01 sleeve; **TB-02** registration |
| **SM-C3** | Return bands | Elastic return / snapback wear parts (not suction) | Supports TB-04 later; optional on TB-01 vent-return |
| **SM-C4** | Fittings / pigtails | Push-in fittings, short tube pigtails to chamber necks | TB-01/TB-02 air path |
| **SM-C5** | Manifold ports (8-branch concept) | Isolated parallel branch envelope (not serial U→F) | TB-02 section; full-arm later |
| **SM-C6** | Textile-eye termination hardware class | Soft root harness eye geometry into recessed boot (interface to B-06) | Soft-termination coupons; Critical stays Lead |
| **SM-C7** *(optional)* | Soft wrist cuff / glove retention class | Distal soft retention; no exposed metal | Later TB-03; sources thin |

---

## 2) Supplier candidates by class

**Method:** WebSearch + WebFetch of public US/EU industrial and catalog pages (2026-09-21 ET).  
**Rule:** Budgetary price only if publicly listed on fetched/catalog page; else **NOT PUBLICLY LISTED**. No invented SKUs as committed line items — catalog family / example PN cited only when the page shows it.

### SM-C1 — Sleeved bladders / elastomer candidates

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **Smooth-On, Inc.** (via distributors) | Product: Ecoflex™ 00-30 — https://www.smooth-on.com/products/ecoflex-00-30/ · Dragon Skin™ 30 — https://www.smooth-on.com/products/dragon-skin-30/ · Soft Robotics Toolkit cites Dragon Skin 30 for PneuNets-class builds: https://softroboticstoolkit.com/book/pneunets-bill-materials | **Publicly listed (distributor):** Ecoflex 00-30 trial set **$33.00** (Douglas and Sturgess, https://douglasandsturgess.com/products/eco-flex-00-30-trial-kit). Dragon Skin 30 trial set **$38.05** (https://douglasandsturgess.com/products/dragon-skin-30-2-pint-set). Smooth-On OEM page lists unit sizes (trial / gallon / 5-gal) but **OEM unit price NOT PUBLICLY LISTED** on product pages fetched. | **Strong for TB-01/TB-02 in-house cast coupons.** Soft, high-elongation silicones for sleeved-bladder coupons. Not a finished sleeved bladder — molds/tooling separate (**mold cost NOT IN SOURCE**). |
| 2 | **Dynamic Rubber, Inc.** | https://www.dynamicrubber.com/ — custom inflatable seals, fabric-reinforced seals, inflatable bladders & tooling (EPDM, silicone, FKM, neoprene, nitrile, fabric rein.) | **NOT PUBLICLY LISTED** (RFQ / application engineering) | **Production-class custom bladder/sleeve RFQ** when Stephen opens spend for molded parts beyond cast coupons. Good analog for sleeved pneumatic chambers; not Soft-Robotics-specific SKU. |
| 3 | **American Rubber Corp (ARC)** | https://www.americanrubbercorp.com/inflatable-seals-native/ — non-reinforced & fabric-reinforced inflatable seals; clamping bladders; custom valve/inlet tube | **NOT PUBLICLY LISTED** (custom quote) | Candidate for fabric-reinforced inflate/deflate chambers; Made-in-USA custom. Suitability for TB-01 geometry TBD after drawing handoff — **geometry NOT IN SOURCE** until Soft DFM freeze. |
| 4 *(alt)* | **Eutsler Technical Products** | https://www.eutsler-rubber.com/sleeves/ — custom molded elastomer sleeves, tubes, bladders | **NOT PUBLICLY LISTED** (request quote) | Custom ID/OD sleeves & bladders; useful if coupon evolves to reinforced sleeve over cast bladder. |

**ask_stephen / ask_ola:** Choose **cast-coupon path (Smooth-On)** vs **custom molded RFQ (Dynamic / ARC / Eutsler)** for first TB-01 kit — cost, lead time, and repeatability trade; no PO from this paper.

---

### SM-C2 — Registered textile / yarn (power-net / stretch mesh class)

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **Mood Fabrics** | White High Compression PowerNet Mesh — https://www.moodfabrics.com/products/white-high-compression-powernet-mesh-311389 — 84% nylon / 16% spandex, 170 gsm, 60″ | **Publicly listed:** **$13.96 / yard** (page fetched 2026-09-21 ET; listing showed sold-out / lead-time note — treat as catalog band, verify stock before any buy) | **TB-01/TB-02 coupon textile** — small-yard sampling possible. Registration / strain-limit candidate; not load-rated for Critical B-06. |
| 2 | **Sportek International Inc.** | SP-1013 Nylon-Spandex PowerNet — https://sportek.com/products/sp-1013-nylon-spandex-powernet-mesh — 84/16, 170 GSM, 58–60″; stock MOQ stated as one roll ~100 yds | Page shows “Regular price $5.00” with **unit unavailable / ambiguous** → treat as **NOT PUBLICLY LISTED** (confirm unit with sales) | Wholesale roll path for registered textile if coupon → module. Dye-to-match available per page. |
| 3 | **Pine Crest Fabrics** | Compression Mesh — https://pinecrestfabrics.com/products/compression-mesh/ — 74% nylon / 26% spandex, 120 GSM, 60/62″; min 15 yd stock; $500 first-purchase minimum stated | **NOT PUBLICLY LISTED** (FAQ: contact for price) | Wholesale stretch mesh; better for module yardage than single coupon unless Stephen accepts min. |

**Note:** “Registered textile / yarn” fiber ID (chamber polarity marking) — **specific industrial yarn SKU NOT IN SOURCE**; use contrasting thread / tape class until Soft DFM specifies.

---

### SM-C3 — Return bands (elastic shock cord / elastic recovery class)

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **McMaster-Carr** | Elastic / mil-spec shock cords family — https://www.mcmaster.com/products/elastic-shock-cords/ · MIL-C-5651 Type 3 — https://www.mcmaster.com/products/bungee-cords/military-specification~mil-c-5651-type-3/ | Catalog shows diameters & lengths; **dollar prices NOT PUBLICLY LISTED** in fetched search extract (masked / session-dependent) → **NOT PUBLICLY LISTED** | Fast sample path for TB-01 optional return and later **TB-04**. McMaster warns: never use for lifting — aligns with Soft “return, not structural hang.” |
| 2 | **Lexco Cable** | https://www.lexcocable.com/products/bungee-cords/ — bulk shock cord, cut-to-length, assemblies, MIL-spec on request | **NOT PUBLICLY LISTED** (request quote) | OEM bulk / custom ends for wear-part return bands. |
| 3 | **Consolidated Cordage Corp.** | MIL-C-5651 cotton-covered shock cord — https://consolidatedcordage.com/viewitems/bungee-shock-cord/shock-cord-cotton-bungee- | Tensile tables appear on some catalog lines; **unit sell price NOT PUBLICLY LISTED** on fetched page | Spec-class elastic for repeatable coupon bands. |

**No Soft load rating claimed.** Return bands are wear parts per open-items brief; failed-band behavior is TB-04 scope, not this scout.

---

### SM-C4 — Fittings / pigtails (push-in + PU tubing class)

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **AutomationDirect (NITRA™)** | Polyurethane tubing spec/price sheet: https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf · Push-to-connect overview: https://www.automationdirect.com/adc/overview/catalog/pneumatic_components/fittings/push-to-connect | **Publicly listed (catalog PDF):** e.g. PU 1/8″ × 100 ft **$23.50**; PU 5/32″ (4 mm) × 100 ft **$21.50**; PU 6 mm × 100 ft **$32.50–$34.00**; PU 1/4″ × 100 ft **$32.00** (colors vary). Tubing cutter TC-12 **$5.75**. | **TB-01/TB-02 pigtail tubing class** with published bend-radius specs (cite in keep-out §3). Fitting dollar bands: see NITRA fittings PDFs — verify live cart before spend (**fitting unit prices vary by PN; not exhaustively re-fetched** → many fitting PNs **NOT PUBLICLY LISTED** in this paper unless cited). |
| 2 | **SMC** | KM One-touch Fittings Manifold Series — https://www.smcusa.com/products/km-one-touch-fittings-manifold-series~21864 · KM11 family (6/10 outlets common; verify exact branch count at order) | **NOT PUBLICLY LISTED** on SMC USA page (configurator / login / quote) | Industrial one-touch fittings + manifold family for branch pigtails. Prefer metric OD matched to chamber neck once Soft DFM freezes tube OD (**tube OD freeze NOT IN SOURCE**). |
| 3 | **Festo** | Plastic tubing PUN / PUN-H family datasheet — https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF · Note: Festo advises PUN not for new designs → prefer **PUN-H** per datasheet strategy note | Part numbers listed; **unit prices NOT PUBLICLY LISTED** in datasheet | Gold-standard PU tubing geometry + **published min / flow-relevant bend radii** (keep-out citations). Pair with Festo QS push-in fittings family (catalog; prices typically distributor-quote). |
| 4 *(alt)* | **Parker / Legris** | Push-to-connect fittings master catalogs (LF3000 class for air + PU) — e.g. distributor literature pointing to Parker Legris pneumatic PTC families | **NOT PUBLICLY LISTED** in this scout (login / distributor quote) | Equivalent fittings class if SMC/Festo lead times issue. |

**TB-01/TB-02 note:** Soft Robotics Toolkit historical BOM references ~1/8″ OD pneumatic tubing examples; treat as **pedagogy analog**, not frozen Soft OD.

---

### SM-C5 — Manifold ports (8-branch concept)

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **Twintec Inc.** | Push-to-Connect multi-tube manifolds — https://twintecinc.com/push_to_connect_series — body styles up to 12–24 ports; **8-tube assemblies listed** (e.g. chart rows for 8 tubes @ various OD) | **NOT PUBLICLY LISTED** (call / quote) | Closest **public catalog family** showing 8-branch multi-tube disconnect concept for isolated chamber lines. Good exploratory ICD for shoulder services. |
| 2 | **SMC KM series** | https://www.smcusa.com/products/km-one-touch-fittings-manifold-series~21864 — one-touch manifolds; common configs 6 or 10 outlets (exact 8 may require paired manifolds or custom) | **NOT PUBLICLY LISTED** | Envelope for branch identity; may need **2× manifolds** or custom block for true 8 — architecture OPEN. |
| 3 | **AutomationDirect NITRA aluminum manifolds** | https://cdn.automationdirect.com/static/specs/nitramanifolds.pdf | **Publicly listed example:** MLA-5 **$42.00** (1/2″ NPT in, five 1/4″ NPT out) — **not 8-port**; round 2/3-out variants also in family | Useful for **coupon bench distribution**, not final 8-chamber Soft manifold. Shows public price band for aluminum distribution class. |
| 4 *(ref)* | **Festo Didactic / lab manifold** | Public PDF describes 8 self-sealing push-in manifold (common P → 8) — Festo Didactic part literature (e.g. manifold doc referencing QS-1/8 fittings) | Educational / didactic pricing **NOT PUBLICLY LISTED** in this scout | Conceptual proof that 8-branch common-supply manifolds exist; **not** assumed Soft production PN. |

**Architecture reminder (SoR intent):** Manifold is **envelope** until circuit defined; air must **not** flow serially U→F; isolated parallel branches. Rotary union deferred (see §3).

---

### SM-C6 — Textile-eye termination hardware class

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **Sailmaker’s Supply** | 1″ welded D-ring (webbing accessories) — https://www.sailmakerssupply.com/product/1-inch-welded-d-ring/webbing-accessories · related D-rings / pad eyes on same site | **Publicly listed:** **$0.78 each** (1″ welded D-ring) | **Geometry-class analog** for textile-eye / webbing cinch into recessed boot. **No Soft load rating.** Metal stays at boot — distal Soft remains metal-free. |
| 2 | **Bainbridge International USA** | https://bainbridgeintusa.com/ · Sail & cover hardware catalog (webbing & fittings family; PDF BA2 Sailmakers Hardware) | Trade catalog; **item unit prices NOT PUBLICLY LISTED** on corporate landing page | Sailmaker webbing / eye-strap / grommet ecosystem for textile-eye class ICD. |
| 3 | **Suncor Stainless** | Tie-downs & fittings / webbing hardware — https://suncorstainless.com/tie-downs-fittings/ · brochure: stainless webbing hardware, D-rings, custom webbing sewing | **NOT PUBLICLY LISTED** (quote / distributor) | Industrial stainless webbing hardware; custom webbing assemblies. Interface class only — Critical B-06 structural still Lead. |
| 4 *(alt)* | **Wichard** (EU marine) | Webbing eye straps (e.g. marine.wichard.com webbing eye strap family) | **NOT PUBLICLY LISTED** in this scout | Recessed-boot eye geometry analog; import path if US sailmaker stock insufficient. |

**Critical B-06:** Soft papers textile-eye → recessed boot **interface class only**. No peel/pull load numbers. Structural stays / pitch / hub remain Lead.

---

### SM-C7 — Soft wrist cuff / glove retention class *(optional; sources thin)*

| # | Company | URL / catalog family | Budgetary price | Suitability notes |
|---|---|---|---|---|
| 1 | **Mood / Sportek / Pine Crest** (same SM-C2 stretch textiles) | Power-net / compression mesh as cuff / glove retention sleeve | See SM-C2 | Soft cuff from registered stretch textile — preserves **no distal exposed metal**. |
| 2 | **Industrial knit-wrist glove suppliers** (e.g. PIP G-Tek family catalogs via distributors) | Catalogs describe elastic knit wrists on industrial gloves — retention **geometry analog** only | Finished glove SKUs are PPE, not Soft modules; **module cuff price NOT IN SOURCE** | Do **not** buy finished gloves as Soft wrist — use as retention geometry reference for TB-03 later. |
| 3 | Soft-robotics research glove literature | Academic textile actuator gloves (elastic bands + Velcro retention) — not a vendor | N/A | **NOT a supplier** — indicates cuff/Velcro-class retention is common; commercial Soft wrist SKU **NOT IN SOURCE**. |

---

## 3) Soft-termination keep-out ICD notes (paper)

**Scope:** Qualitative geometry keep-outs for Soft root services → Lead B-06 boot. **No invented load ratings. No invented Soft mm unless cited from a public hose/tubing catalog.**

### 3.1 Flex-loop under finite yaw (P-06 MVP)

- Pitch/yaw Soft services use a **hose flex-loop / service loop** at the root so finite carrier yaw does not kink chamber pigtails.
- **Rotary union:** deferred — **later only if continuous spin** is required. MVP assumes **finite yaw**, not continuous rotation.
- Loop must remain inside chafe keep-out (boot / guard) and outside pinch planes of Option B pitch hardware (Lead).

### 3.2 Bend-radius / chafe keep-out classes *(cite public tubing catalogs)*

Qualitative rule: **do not route Soft pigtails below the manufacturer’s published minimum bend radius** for the selected tube family; keep chafe away from sharp edges, pitch hinges, and textile-eye hard points.

| Catalog family (public) | Example published bend figures | Use in ICD |
|---|---|---|
| **Festo PUN** datasheet (2025 EN) | **Min. bending radius** examples: 4×0.75 → **8 mm**; 6×1 → **16 mm**; 8×1.25 → **24 mm**. **Flow-relevant** radii larger (e.g. 4 mm OD → 17 mm; 6 mm → 26.5 mm). Source: https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF | Prefer **flow-relevant** radius as Soft keep-out floor when motion + flow both matter. Switch to **PUN-H** for new designs per Festo note. |
| **AutomationDirect NITRA PU** | Catalog lists bend radius per OD, e.g. 1/8″ → **0.200 in**; 5/32″ → **0.250 in**; 6 mm → **12.0 mm**; 1/4″ → **0.476 in**. Source: https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf | Coupon bench may use NITRA figures until Soft freezes on Festo/SMC OD. |

**Chafe keep-out (qualitative):** Abrasion sleeve / textile wrap at any Soft tube contact with metal boot lip, webbing eye, or pitch pin; no Soft tube clamped under textile-eye stitch line.

### 3.3 Option B pinned pitch alignment

- Hose loop / pigtail bundle must **survive preset pitch changes and service** (pin remove/re-pin), **not** continuous pitch actuation.
- Keep-out volume sized for **discrete preset envelopes**, not continuous servo sweep.
- Soft termination ICD must not assume a pitch rotary union or continuous flexure machine.

### 3.4 Textile-eye → recessed boot interface class

- Soft load path ends in **textile eye / webbing harness** entering a **recessed boot** (last metal at boot — aligns with no distal exposed metal).
- Strain relief: gradual textile → eye → boot; hose loop exits boot without bearing Soft structural load.
- **No peel / pull / N ratings** in this paper — peel/pull coupons are Stephen-gated Soft-termination tests supporting Lead B-06, not Soft-only Critical close.

### 3.5 Option A stand-off

- Soft DFM / BOM geometries assume **Option A stand-off** — **no arm lengthening** to buy hose length. Flex-loop volume comes from root packaging, not longer continuum.

---

## 4) Price found vs NOT PUBLICLY LISTED (summary)

| Class | Public price examples found | NOT PUBLICLY LISTED / NOT IN SOURCE |
|---|---|---|
| SM-C1 Elastomer | Ecoflex trial **$33.00**; Dragon Skin 30 trial **$38.05** (distributor pages) | Dynamic Rubber, ARC, Eutsler custom bladders; Smooth-On OEM bulk list |
| SM-C2 Textile | Mood PowerNet **$13.96/yd** | Pine Crest wholesale; Sportek unit ambiguous |
| SM-C3 Return bands | — | McMaster dollars (session), Lexco, Consolidated sell price |
| SM-C4 Fittings/tubing | NITRA PU tubing bands **~$21.50–$34+ / 100 ft** (size-dependent); cutter **$5.75** | SMC/Festo/Parker fitting unit prices; Soft frozen tube OD |
| SM-C5 Manifold | NITRA MLA-5 **$42.00** (5-out, not 8) | Twintec 8-branch; SMC KM; true Soft 8-port PN |
| SM-C6 Textile-eye | Sailmaker’s 1″ D-ring **$0.78** | Bainbridge/Suncor/Wichard Soft-specific assemblies |
| SM-C7 Wrist cuff | — | Dedicated Soft wrist SKU **NOT IN SOURCE** |

---

## 5) ask_ola / ask_stephen flags (choice points only)

| Flag | Choice needed | Why |
|---|---|---|
| **ask_ola** | In-house cast (Smooth-On) vs custom molded bladder RFQ (Dynamic/ARC/Eutsler) for TB-01 narrative | Affects Soft DFM story, lead time, and whether coupon = System ID on cast geometry |
| **ask_ola** | Confirm Soft-termination textile-eye ICD ownership remains Ismael while Critical B-06 stays Lead | Prevents Soft Critical claim |
| **ask_stephen** | Open spend for **TB-01 + TB-02** coupon materials only (first band) | Stephen-gated; no PO from this paper |
| **ask_stephen** | If cast path: accept distributor trial kits vs wait for custom rubber house samples | Budget / schedule |
| **ask_ola + ask_stephen** | Tube OD family freeze (NITRA coupon vs Festo PUN-H / SMC production) before manifold RFQ | Avoid orphaned fittings inventory |

---

## 6) Research sources (verified URLs)

1. https://www.smooth-on.com/products/ecoflex-00-30/  
2. https://www.smooth-on.com/products/dragon-skin-30/  
3. https://douglasandsturgess.com/products/eco-flex-00-30-trial-kit  
4. https://douglasandsturgess.com/products/dragon-skin-30-2-pint-set  
5. https://softroboticstoolkit.com/book/pneunets-bill-materials  
6. https://www.dynamicrubber.com/  
7. https://www.americanrubbercorp.com/inflatable-seals-native/  
8. https://www.eutsler-rubber.com/sleeves/  
9. https://www.moodfabrics.com/products/white-high-compression-powernet-mesh-311389  
10. https://sportek.com/products/sp-1013-nylon-spandex-powernet-mesh  
11. https://pinecrestfabrics.com/products/compression-mesh/  
12. https://www.mcmaster.com/products/elastic-shock-cords/  
13. https://www.lexcocable.com/products/bungee-cords/  
14. https://cdn.automationdirect.com/static/specs/nitratubingpoly.pdf  
15. https://cdn.automationdirect.com/static/specs/nitramanifolds.pdf  
16. https://www.smcusa.com/products/km-one-touch-fittings-manifold-series~21864  
17. https://ftp.festo.com/Public/PNEUMATIC/SOFTWARE_SERVICE/Documentation/2025/EN/PUN_PUN_DUO_EN.PDF  
18. https://twintecinc.com/push_to_connect_series  
19. https://www.sailmakerssupply.com/product/1-inch-welded-d-ring/webbing-accessories  
20. https://bainbridgeintusa.com/  
21. https://suncorstainless.com/tie-downs-fittings/  

---

## Document control

| Field | Value |
|---|---|
| Status | PAPER DRAFT — supplier scout |
| PO | **None** |
| Critical close | **None** |
| NEXT_PROMPT | **Not touched** |
| Prefer IDs | **TB-*** over legacy B-0x for coupon spend talk |
| Research date | 2026-09-21 ET |

— Ismael · Soft Robotics Desk · MYORGLAB
