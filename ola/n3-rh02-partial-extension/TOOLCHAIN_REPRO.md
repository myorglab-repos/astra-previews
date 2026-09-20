# I. Reproduction

Blender 3.6.5 CLI with bpy/NumPy; Python 3.11 and Pillow. Native Blender and bpy were exercised; computer-use UI was not used. Saved successor SHA-256: `8eebb0669a7a5b3092abee51921b8e33a3b7b598db53eaf89abdfd4f062d0564`. Git LFS applies to blend and PNG files. Nine ancestor hashes in lineage.json include the audited N1; never overwrite source evidence. The builder refuses to overwrite its destination unless --replace-candidate is explicitly passed during an unsettled iteration. Rebuild settled evidence in a fresh output checkout/version.

```powershell
$packetPath = 'reviews/2026-09-19/n3-rh02-partial-extension'
$sourceBlend = 'reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/Punching_Bag_N3_Airflow_Bladder_Bend.blend'
python "$packetPath/run_blender.py" build_policy $sourceBlend
python "$packetPath/run_blender.py" audit_atlas
python "$packetPath/run_blender.py" audit_lineage
python "$packetPath/audit_policy.py"
python "$packetPath/run_blender.py" render_atlas
python "$packetPath/compose_atlas.py"
python "$packetPath/build_packet.py"
# Inspect atlas images and record visual_review.json before:
python "$packetPath/verify_packet.py"
```

Audit scripts read the saved model independently from the builder. Native exit codes are recorded in process receipts. Atlas vertex/target checks verify rendered wireframe endpoints against case boxes. Existing markdown rendering helpers are read from revision_n/review_packet/build_index.py. Image inspection is recorded separately from numeric passes. No film is needed to support this policy-only atlas handoff; no playback claim is made.

**Track A does not prove strike impulse.** No measured pneumatic propulsion, force, durability, loaded reach or real CV result is supplied.