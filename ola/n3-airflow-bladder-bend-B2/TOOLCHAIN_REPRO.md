# I. Toolchain and reproduction

Blender 3.6.5 CLI with bpy/NumPy; Python 3.11, Pillow, Mistune and imageio-ffmpeg. Blender access was exercised; native UI and browser playback are not claimed. Source hashes are in [lineage.json](lineage.json); successor SHA-256 is `b8ebfdb134b5a4337ec7f10f7d83f8a4941f0d535c413fe9265b9506a8bcbeeb`. Git LFS stores .blend/.png/.mp4 files. Source binaries are real files, not pointers.

Run builds in a new output directory or isolated checkout. Never overwrite settled baselines. `--replace-candidate` applies only to an unsettled output. Scripts resolve the packet directory from their location. Use this prefix for the following commands: `python reviews/2026-09-19/n3-airflow-bladder-bend-B2/`.

```text
run_blender.py build_bend reviews/2026-09-19/n3-airflow-bladder-bend/Punching_Bag_N3_Airflow_Bladder_Bend.blend
run_blender.py audit_lineage <successor.blend>
run_blender.py audit_atlas <successor.blend>
run_blender.py audit_swell <successor.blend>
run_blender.py render_media <successor.blend> whole
run_blender.py render_media <successor.blend> exposed
run_blender.py render_cells <successor.blend>
compose_media.py
qa_media.py
build_packet.py
# Inspect the decoded phase sheets and full-resolution stills; record visual_review.json.
verify_packet.py
```

Film has four chapters, 128 frames at 4 fps, 2400×1400 pixels. Transitions between chapters are cuts; timing is explanatory. Intermediate frame folders are ignored. Native Blender process receipts and source-bound render records are retained. Blender reports eight invalid orphan shape-key pointers and action-user diagnostics on load, also present in the parent packet; the loader discards those blocks. All attached atlas shape schedules and selected B2 morph weights pass the saved-model checks after loading. The file is not claimed to load without diagnostics. Complete film decode and selected decoded-frame visual QA do not imply continuous manual playback.

**Track A does not prove strike impulse.** These are prescribed geometry and illustrative pneumatic cues. Measured propulsion, contact force, durability and real CV remain unverified.