# F. Saved-model regression and geometry limits

Source: [atlas_audit.json](atlas_audit.json). Blender 3.6.5; successor SHA-256 `c956779e3874b6f9e54a943315174b805fdf4543935bd6571d06eaf35c6b6ea0`. All 2431 integer/half-frame times from 1 through 1216 were evaluated. Two arms produce 4,862 arm/time observations. G-03 measures ring-center distance to an infinite radius-275 mm nominal bag cylinder, less the same 71 mm arm-radius proxy. G-05 measures evaluated Z separation between outer covers. A-05 compares actual glove origin with core/cover distal and cuff-middle ring centroids using a 0.01 mm numerical criterion.

| Metric | Minimum / maximum mm | Disposition |
|---|---|---|
| G05_lower, frame 1 | minimum 4.999995 | PASS sampled nominal geometry |
| G05_upper, frame 1 | minimum 4.999995 | PASS sampled nominal geometry |
| G03_L_U, frame 913 | minimum 23.672451 | PASS sampled nominal geometry |
| vertex_L_U, frame 913 | minimum 32.749047 | PASS sampled nominal geometry |
| G03_L_F, frame 785 | minimum 4.321681 | PASS sampled nominal geometry |
| vertex_L_F, frame 785 | minimum 11.293300 | PASS sampled nominal geometry |
| G03_R_U, frame 945 | minimum 23.672451 | PASS sampled nominal geometry |
| vertex_R_U, frame 945 | minimum 32.749047 | PASS sampled nominal geometry |
| G03_R_F, frame 817 | minimum 4.321681 | PASS sampled nominal geometry |
| vertex_R_F, frame 817 | minimum 11.293300 | PASS sampled nominal geometry |
| A05_core, frame 762 | maximum 0.000384 | PASS registration |
| A05_cuff, frame 762 | maximum 0.000369 | PASS registration |
| A05_cover, frame 762 | maximum 0.000375 | PASS registration |
| within_chapter_halfstep, frame 1169 | maximum 29.693632 | Motion sample only, no speed rating |

The 60 mm added routing bow is zero at the shoulder and forearm distal endpoint and shared across the U/F junction; existing N3 bow and 5 mm band insets are retained. Dynamic U/F layers and feed paths receive the same parameterized shift. The resulting arc lengths differ from N3 and vary with interpolation. See per-pose U/F arcs in JSON; neither constant material length nor permissible strain is asserted. Short 50% poses extrapolate from the original guard/peak shapes. No mesh self-intersection, triangle distance, hose bend radius or loaded padding/tolerance test is closed by the cylinder proxy.

Ola's N3 CLOSED-A remains tied to its frozen source. The successor receives a new sampled regression result, not a retroactive rewrite of that baseline. B-03 retention and physical gaps remain open. The rejected candidate audit records the old failing geometry and is not evidence for the final model. Transitions across chapter cuts, full continuous extrema, all hardware collisions and loaded contact remain outside this check.

**Track A does not prove strike impulse.** Motion, color emphasis and timing are prescribed illustrations. No measured propulsion, pressure response, contact force, durability or real CV is claimed.