# F. Envelope and regression audit

Reopened final saved Blender file; evaluated all 2,431 integer/half-frame times, both arms. G-03 uses each U/F sleeve's 37 ring centers and a 71 mm radius proxy against the infinite 275 mm bag cylinder. The reported gap is radial center distance minus 346 mm. G-05 uses evaluated axial extrema of the lower/upper covers and rotating band. A-05 compares wrist core/cuff/cover ring centers with the glove datum.

| Check | Saved-model result | Interpretation |
|---|---|---|
| G-03 U, both arms | +23.672451 mm minimum | Sampled positive proxy. |
| G-03 F, both arms | +1.792008 mm minimum | Tall 70% peaks, frames 1073 / 1137; reduced from parent +4.321681 mm. |
| G-05 lower / upper | +4.999995 / +4.999995 mm | Retained nominal axial gap. |
| A-05 worst | 0.000350 mm | Registration retained; below 0.001 mm. |
| Bag/mast fixed matrix deviation | 0 | Fill/mast remain stationary. |
| Chambers | 16 total | Eight per arm. |
| All policy peaks / palm checks | 38 / 38 PASS | Sampled inclusion and normal hemispheres only. |
| Added routing bow / changed mesh coordinates | 0 / none | RH-03 inherited 68 mm bow remains, physically unverified. |

No continuum chord lengthening occurred. Rotation preserves chord and arc geometry; inherited 50% shape extrapolation is not a constant-length or pressure-equilibrium model. Chord comparisons with the parent are checked numerically and complete mesh/shape signatures match. The 60-degree candidate left +0.060172 mm; final 57-degree cap improves that but does not restore the parent's full clearance margin.

Half-frame sampling cannot certify continuous extrema, triangle collision, seam/fabric compression, tolerances, deflection, hoses against hardware, loaded motion or collision during chapter changes. The nonnegative proxy criterion passes; the reduced margin remains a review issue. All 50% peak target coverage remains fragile (0.571485 mm sampled margin).

**Track A does not prove strike impulse.** These are prescribed geometry, motion and qualitative air cues. Measured pneumatic propulsion, contact force, durability and real CV remain unverified.


Spatial-policy check: all six 50% boxes intersect the infinite bag proxy by 125 mm radially. This is a target-assumption failure, distinct from the positive arm-to-bag G-03 result. It remains RH-02 OPEN; surface inclusion is not a usable opponent stand-off. See policy_spatial_audit.json.
