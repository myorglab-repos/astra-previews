# I — Toolchain and reproducibility

Observed runtime: Blender 3.6.5, Python 3.11, OpenCV 4.8.1, Pillow 12.3.0; NumPy, Mistune and system FFmpeg/ffprobe. No claim of newest supported versions. The OpenCV bundled `haarcascade_frontalface_default.xml` model is used with default detection parameters (ASSUMPTION prior). Exact observed version strings and model hash are recorded in `runtime.json`.

From this packet folder, after dependencies are present:

```powershell
python make_fixture.py
python test_bridge.py
python run_blender.py build_bridge ../n3-b06-pitch-height-pedagogy/Punching_Bag_N3_Pitch_Height_Pedagogy.blend
python run_blender.py audit_bridge
python run_blender.py render_bridge
python compose_media.py
python build_packet.py
python verify_packet.py
```

`run_blender.py` uses the installed Blender 3.6 path; `build_bridge.py` uses the installed Python311 path for the OpenCV subprocess. Edit those tool paths when moving machines. The builder checks the accepted parent hash and compares five inherited scene signatures before saving a new successor; it never writes the parent. It can regenerate its own candidate output. The saved film is baked from the actual UDP receive log, then rendered offline; per-frame acknowledgements guarantee deterministic test transfer and are not a throughput benchmark.

`render_frames/` and `composed_frames/` are reproducible intermediates excluded from Git. Logs/caches/runtime latch state are local. `packet_manifest.json` includes deliverable hashes. Use Git LFS to fetch actual blends, images and video (`git lfs pull`) after cloning; pointer files are not usable media. Ancestor blend hashes live in `lineage.json`.

The supplied source still is attributed to NASA / Eileen Collins, via scikit-image's public-domain sample. [Source description](https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.astronaut), [source image](https://raw.githubusercontent.com/scikit-image/scikit-image/v0.25.2/skimage/data/astronaut.png), [OpenCV cascade API](https://docs.opencv.org/4.x/d1/de5/classcv_1_1CascadeClassifier.html). The fixture crops/translates that still to exercise the detector; it does not depict an actual boxing session or actual person movement. Source bytes and transformation details are in fixture_provenance.json.
