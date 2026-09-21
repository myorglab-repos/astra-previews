# F — Saved-model geometry audit

Independent audit opens the saved successor; it does not import the builder or save edits. All 144 received-packet frames are checked. Constant yaw keys hold between samples; no intervening interpolated stroke is claimed.

| Digital quantity | Result |
|---|---|
| Bag/fill/mast matrix maximum deviation | 0.0 |
| Camera matrix maximum deviation | 0.0 |
| Replay yaw maximum numerical error | 0.000000777 degrees |
| Arm geometry maximum drift in carrier coordinates | 0.0000000350 m |
| A-05 wrist/glove maximum drift | 0.000081 mm |
| G-03 sampled 71-mm radial arm-envelope proxy minimum | 48.069149 mm |
| G-05 cover/carrier axial gap minimum | 4.999995 mm |
| Chamber object count | 16, eight per arm |
| Inherited scene signatures / ancestor hashes | 5 unchanged / 11 preserved |

See [raw model verification](model_verification.json). G-03 uses the inherited centerline/radial proxy against the axisymmetric bag, not mesh collision or loaded deflection. New conceptual root covers, hoses, pinch, cover compliance and real clearances remain unqualified. Previous accepted atlas geometry/animation is preserved by exact signatures; this pass does not claim a new physical verification or rerun its entire physical test plan.

**Track A does not prove strike impulse.** B-06 root hardware and C-01 pressure-to-motion-to-impact measurements remain Critical OPEN. No physical actuation, measured sensing accuracy, detector FPS, latency, durability or safety qualification is claimed.
