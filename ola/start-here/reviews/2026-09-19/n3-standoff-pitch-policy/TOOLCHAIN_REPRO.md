# I. Reproduction and provenance

Blender 3.6.5 CLI / bpy / NumPy; Python 3.11, Pillow and imageio-ffmpeg. Final saved SHA-256: `a653d2dd1c6e7e7531ed2379b8e81aa8924d8ff734a8176742664fa9105a782f`. See lineage.json for all four preserved baseline hashes. Blender access was exercised directly through the CLI; native app UI is not claimed.

Build only in a new version/output or isolated checkout with no settled destination binary. `--replace-candidate` is for unsettled candidates only. Intermediate film frames are ignored; Blender, stills and MP4 outputs use Git LFS. Verify real binary payloads after clone. Source scripts have no source-model save operation.

```powershell
$packetPath = 'reviews/2026-09-19/n3-standoff-pitch-policy'
$sourceBlend = 'reviews/2026-09-19/n3-reach-height-body/Punching_Bag_N3_Reach_Height_Body.blend'
$policyBlend = "$packetPath/Punching_Bag_N3_Standoff_Pitch_Policy.blend"
python "$packetPath/run_blender.py" build_policy $sourceBlend
python "$packetPath/run_blender.py" audit_atlas $policyBlend
python "$packetPath/run_blender.py" audit_lineage $policyBlend
python "$packetPath/run_blender.py" render_media $policyBlend stills
python "$packetPath/run_blender.py" render_media $policyBlend atlas
python "$packetPath/compose_media.py"
python "$packetPath/build_packet.py"
# Inspect stills/film contact sheets and record visual_review.json, then:
python "$packetPath/verify_packet.py"
```

The atlas samples every other source frame at 4 fps, retaining the 152-second prescribed duration. All 38 cases appear in 608 film frames; chapter changes are cuts. The inherited airflow film is copied, hash-checked and fully decoded; it remains 128 frames / 32 seconds. Native process receipts record exit status. Render receipts bind stills/atlas to the final saved hash; inherited airflow is separately attributed. Media decode and direct image QA do not establish physical motion validity. Browser playback has not been claimed.

**Track A does not prove strike impulse.** These are prescribed geometry, motion and qualitative air cues. Measured pneumatic propulsion, contact force, durability and real CV remain unverified.
