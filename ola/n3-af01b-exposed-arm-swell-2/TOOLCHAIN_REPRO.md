# I. Toolchain and reproduction

Blender 3.6.5 CLI with bpy/NumPy; Python 3.11, Pillow, Mistune and imageio-ffmpeg. Blender CLI access was exercised; native UI and uninterrupted manual playback are not claimed. Successor SHA-256: `b4626cce4a82a8a5996988168b80fd9c7bce271e36a888714b66631910c01263`. Source and eight baseline hashes are in lineage.json. Models and media are real binaries tracked by Git LFS.

Use a fresh sibling output directory for the build scripts. Never overwrite settled evidence. Prefix commands with `python reviews/2026-09-19/n3-af01b-exposed-arm-swell-2/`:

```text
run_blender.py build_bend reviews/2026-09-19/n3-af01b-exposed-arm-swell/Punching_Bag_N3_Airflow_Bladder_Bend.blend
run_blender.py audit_lineage <successor.blend>
run_blender.py audit_atlas <successor.blend>
run_blender.py audit_swell <successor.blend>
run_blender.py render_media <successor.blend> whole
run_blender.py render_media <successor.blend> exposed
run_blender.py render_media <successor.blend> exposed_reverse
run_blender.py render_cells <successor.blend>
audit_exposed_render.py
compose_media.py
qa_media.py
build_packet.py
# Inspect final decoded sheets and stills, record visual_review.json and READY_FOR_OLA.md.
verify_packet.py
```

Main film 2400x1400; blind film 1640x900. Each is 128 frames at 4 fps / 32 seconds. Intermediate frame folders are ignored. Inherited orphan shape-key load diagnostics remain documented in process logs; attached shape schedules are checked after reload. No clean-load claim is made. `visual_review.json` is an inspection record, not automatically generated viewer acceptance.

**Track A does not prove strike impulse.** Swelling, bend and timing are prescribed illustrations, not a pneumatic solution or measured pressure, flow, strain, propulsion, contact force, durability or real CV.