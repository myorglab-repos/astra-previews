# I. Reproduction and provenance

Blender 3.6.5 CLI/bpy; Python 3.11, NumPy in Blender, Pillow and imageio-ffmpeg. No Blender GUI use claimed. Direct saved-image inspection and local HTML link checks are recorded; interactive browser playback is not tested.

N1 baseline SHA-256: `7a2da9e58991c822c981ecd677c902538389701ec1fe662ab878c2fd2f417e1b`.
N2 source SHA-256: `4331bae6efa3573e67425d10591fc5d09f34323ae588879ddb47c0f311c8e1af`.
N3 successor SHA-256: `8038388e7d666e749af499bab65202c1a9fbed05647fc321e42c0aaffae161c6`.

Build in an isolated copy with no successor output. The builder refuses to overwrite a settled N3. Existing N1/N2 builders are never executed. Source meshes are copied, translated consistently across all existing shape keys, and unused copies purged before save. All topology, shape schedules, object transforms and constraints are inherited; the lineage audit confirms its stated comparison scope.

```powershell
$blenderExe = 'C:/Program Files/Blender Foundation/Blender 3.6/blender.exe'
$packetPath = 'reviews/2026-09-19/n3-geometry-delta'
& $blenderExe -b 'reviews/2026-09-19/n2-track-a/Punching_Bag_N2_Track_A.blend' --python-exit-code 1 --python "$packetPath/build_delta.py"
python "$packetPath/run_processes.py" audits
python "$packetPath/run_processes.py" stills
python "$packetPath/run_processes.py" films
python "$packetPath/encode_films.py"
python "$packetPath/make_sample_sheets.py"
python "$packetPath/plot_clearance.py"
python "$packetPath/build_packet.py"
# Inspect saved stills and movie sheets; record visual_review.json, then:
python "$packetPath/verify_packet.py"
```

Process receipts capture native exit codes and markers; scripts fail on mismatches. Film previews sample source frames 1,7,...,1915 at 4 fps for 80 seconds, 960x720; geometry audit extends to frame 1920. Full decoding checks file integrity, not feasibility. PNG movie intermediates and the rejected candidate are ignored, not included in the review manifest. Blends/media use Git LFS; verify binaries after clone/pull.

**Track A does not prove strike impulse.** Prescribed motion only; no measured pneumatic propulsion, contact force, pressure response, durability or real CV is claimed.
