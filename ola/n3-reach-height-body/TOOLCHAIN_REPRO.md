# I. Reproduction and provenance

Blender 3.6.5 CLI with bpy/NumPy; Python 3.11 with Pillow and imageio-ffmpeg. No native UI operation is required or claimed. Mesh topology and static coordinates are compared independently; current audits and every render metadata file identify the saved successor SHA-256 `c956779e3874b6f9e54a943315174b805fdf4543935bd6571d06eaf35c6b6ea0`. All three baseline hashes appear in lineage.json and are independently recomputed in atlas_audit.json.

Build in an isolated checkout/output with no successor file. The explicit `--replace-candidate` switch is only for an unsettled candidate and was used during this pass; do not overwrite a settled review binary. The builder reads the prior N3 routing functions through AST without executing its builder. No baseline is saved or mutated. Intermediate PNG frames are ignored; saved blends, PNG stills and MP4 films use Git LFS. Verify real binary contents after cloning.

```powershell
$packetPath = 'reviews/2026-09-19/n3-reach-height-body'
$sourceBlend = 'reviews/2026-09-19/n3-geometry-delta/Punching_Bag_N3_Geometry_Delta.blend'
$atlasBlend = "$packetPath/Punching_Bag_N3_Reach_Height_Body.blend"
python "$packetPath/run_blender.py" build_atlas $sourceBlend
python "$packetPath/run_blender.py" audit_atlas
python "$packetPath/run_blender.py" audit_lineage
python "$packetPath/run_blender.py" render_media $atlasBlend stills
python "$packetPath/run_blender.py" render_media $atlasBlend atlas
python "$packetPath/run_blender.py" render_media $atlasBlend whole
python "$packetPath/run_blender.py" render_media $atlasBlend exposed
python "$packetPath/compose_media.py"
python "$packetPath/build_packet.py"
# Inspect final stills and film samples; record visual_review.json, then:
python "$packetPath/verify_packet.py"
```

The atlas renders source frames 1,3,...,1215 at 4 fps, preserving 152 seconds of prescribed 8 fps timeline. Each of four airflow chapters renders all 32 source poses at 4 fps (two-times slow presentation), totaling 32 seconds. Native process receipts record return codes; media verification fully decodes both films and checks dimensions/duration/frame count. Preview timing is not measured actuator timing. Visual QA is direct image inspection; browser playback is separately stated if tested.

**Track A does not prove strike impulse.** Motion, color emphasis and timing are prescribed illustrations. No measured propulsion, pressure response, contact force, durability or real CV is claimed.
