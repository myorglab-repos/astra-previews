# Model B: Preliminary BOM & DFM Notes v0
Date: 2026-09-27 · Owner: Ola · **No prices.** Costing comes later and goes through Stephen. Quantities are per kit. Part choices are ASSUMPTIONS.

## BOM (functional level)
| # | Item | Qty | Make/buy | Notes |
|---|---|---|---|---|
| 1 | Collar band, segmented, ratchet, two sizes (13-15 / 16-19 in) | 1 | Make (molded + strap) | Tension indicator |
| 2 | High-grip liner | 1 | Buy | Must not mark covers (T-09) |
| 3 | Rotating shoulder ring with bearing | 1 | Make + buy bearing | Powered or passive TBD (CB-07) |
| 4 | Soft arm assembly (Model A family) | 2 | Make | Quick-release root (SI-B1) |
| 5 | Pack housing, padded, vented | 1 | Make (molded) | Isolation mounts inside |
| 6 | Compressor, compact 18/20 V class | 1 | Buy | Duty cycle is a key unknown |
| 7 | Air tank, small | 1 | Buy | Size from runtime study |
| 8 | Valve block + pressure sensors | 1 | Buy/assemble | Next to arm roots |
| 9 | Mechanical relief valve | 1 | Buy | Set below SI-B3 |
| 10 | Main board + IMU + radio | 1 | Make (PCB) | Shared firmware with Model A |
| 11 | Camera module(s) | 1-2 | Buy | Count TBD (Controls Q1) |
| 12 | Battery dock, dual, latched | 1 | Make | One tool platform (TBD) |
| 13 | Battery pack 18/20 V | 1 | Buy (or customer's own) | Certified only |
| 14 | Charger | 1 | Buy | |
| 15 | Load straps with length adjusters | 3-4 | Buy | WLL 125 lb or more each |
| 16 | Rated clips + secondary retention lanyard | 4 | Buy | |
| 17 | Handheld (shared with Model A) | 1 | Shared | |

## DFM / DFA notes
- Tool-free install. Target under 15 min for one person with the bag hanging (ASSUMPTION).
- A common core for both collar sizes: only the band segments differ, while the ring, pack and arms are the same part.
- The pack is one sealed service module that swaps as a unit.
- Arms and liner are consumables, so design them for quick replacement.
- Battery platform choice is a business decision (which tool brand, or a universal adapter). Flag it for Michael.
- Supplier risks: the compact compressor (few makers, duty-cycle limits) and the tool-battery licensing or adapter approach.
