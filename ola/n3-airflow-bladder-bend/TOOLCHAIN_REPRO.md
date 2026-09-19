# I. Toolchain and reproduction

Blender 3.6.5 CLI with bpy/NumPy; Python 3.11, Pillow, Mistune and imageio-ffmpeg. Blender access was exercised; native UI and browser playback are not claimed. Source hashes are in [lineage.json](lineage.json); successor SHA-256 is `2eff852b5f0ecd3d8f498125d213bb7601164d4801d46e5d57cfc24cd45a44a3`. Git LFS stores .blend/.png/.mp4 files. Source binaries are real files, not pointers.

Run builds in a new output directory or isolated checkout. Never overwrite settled baselines. `--replace-candidate` applies only to an unsettled output. Scripts resolve the packet directory from their location. Use this prefix for the following commands: `python reviews/2026-09-19/n3-airflow-bladder-bend/`.

```text
run_blender.py build_bend reviews/2026-09-19/n3-standoff-pitch-policy/Punching_Bag_N3_Standoff_Pitch_Policy.blend
run_blender.py audit_lineage <successor.blend>
run_blender.py audit_atlas <successor.blend>
run_blender.py audit_swell <successor.blend>
run_blender.py render_media <successor.blend> whole
run_blender.py render_media <successor.blend> exposed
compose_media.py
qa_media.py
build_packet.py
# Inspect the decoded phase sheets and full-resolution stills; record visual_review.json.
verify_packet.py
```

Film has four chapters, 128 frames at 4 fps, 1800×1000 pixels. Transitions between chapters are cuts; timing is explanatory. Intermediate frame folders are ignored. Native Blender process receipts and source-bound render records are retained. Complete film decode and selected decoded-frame visual QA do not imply continuous manual playback.

**Track A does not prove strike impulse.** These are prescribed geometry and illustrative pneumatic cues. Measured propulsion, contact force, durability and real CV remain unverified.