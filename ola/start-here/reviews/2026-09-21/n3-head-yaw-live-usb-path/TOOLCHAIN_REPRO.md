# I — Toolchain and reproducibility

Observed runtime is recorded in `runtime.json` after this pass's commands. No claim of newest supported versions. The OpenCV bundled `haarcascade_frontalface_default.xml` model is used with default detection parameters (ASSUMPTION prior).

From this packet folder, after dependencies are present. **Do not remake the successor** unless the inherited blend hash is broken:

```powershell
python make_fixture.py
python test_bridge.py
python test_usb_path.py
python run_clip_integration.py
python probe_usb.py
python build_packet.py
python verify_packet.py
```

`run_blender.py build_bridge` remakes the ACCEPTED-A successor and is **out of scope** for this USB-path delta. Interactive receive still uses `blender_receiver.py` + `demo_config.json`.

`render_frames/` and `composed_frames/` are reproducible intermediates excluded from Git. `packet_manifest.json` includes deliverable hashes. Use Git LFS to fetch actual blends, images and video (`git lfs pull`) after cloning.

The supplied source still is attributed to NASA / Eileen Collins, via scikit-image's public-domain sample. Fixture bytes are in fixture_provenance.json.
