# Plate / pulse M

Pass: `p3-aperture-plates-pulse-m`

Viewer: http://127.0.0.1:8765/

Open from the repository root: `powershell -ExecutionPolicy Bypass -File scripts/open-latest-viewer.ps1`. The launcher selects the newest `index.html` under `assets/astra` and opens it in the default browser. All renderer modules and Draco decoders are local.

67 sharp, chamfered panels follow the traced LogoFull M outline. Each has a neutral titanium frame, recessed navy face, and a separate cyan light channel in an open joint. Planar panel faces follow the tangent of the curved underlying volume. The logo's curved outer shoulders remain; the surface has no rounded pebble or fish-scale pieces. Palette: #00B4FE, #19E3F2, #00123F and neutral metal.

The dominant motion is a smooth 3-second sine traveling across 16 groups of seam channels. `Seam_Pulse_3s` is embedded in both GLBs: 16 morph-weight tracks widen and narrow the light aperture without moving the plates. The local viewer also varies seam emission at the same period. Light beat or a tap produces a single 1.3-second expansion to 103.8% plus a light surge, then settles. Pointer follow is limited to approximately 3 degrees horizontally and 2 degrees vertically. No idle panel lifting.

Pause removes the canvas and stops the animation loop. Initial reduced motion loads only the WebP poster, without requesting the model or renderer. Live preference changes are supported. A failed 3D load also falls back to the poster.

| Deliverable | Purpose |
| --- | --- |
| `hero-plates-pulse-m.blend` | Editable Blender 3.6 scene, camera, lights, materials and NLA animation |
| `hero-plates-pulse-m.glb` | Uncompressed working model, 769,604 bytes |
| `hero-plates-pulse-m.web.glb` | Draco model with embedded pulse, 227,964 bytes |
| `poster.master.png` | Transparent Blender master, 1338 × 936 |
| `poster.webp` | ffmpeg-encoded transparent poster, 143,900 bytes |
| `seam-pulse.mp4`, `seam-pulse.webm` | 3-second seamless preview of browser lighting and intrinsic seam motion |
| `index.html`, `viewer.js`, `controls.js`, `review.css`, `vendor/` | Standalone local sample |
| `author.py`, `native-geometry.json` | Self-contained Blender authoring source and native outline data |
| `qa/verification.json`, `qa/verify.mjs` | Repeatable browser checks |
| `qa/viewer-*.png`, `qa/pulse-*.png` | Desktop, mobile, pause, light-beat and pulse captures |

Rebuild geometry with Blender 3.6:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 3.6/blender.exe' --background --python assets/astra/2026-09-19/blender/hero-plates-pulse-m/author.py
```

Run browser verification after serving this directory on port 8765:

```powershell
node assets/astra/2026-09-19/blender/hero-plates-pulse-m/qa/verify.mjs
```

The Blender poster uses studio area lights; browser reflections differ. The GLB carries light-aperture motion; emission modulation, pointer follow, and the interaction beat are viewer behavior. Matching the APERTURE reference remains a design review decision. The supplied YouTube pages were requested, but video frames were not available through the retrieval tool; this pass implements the explicit surface and motion directions in the brief. References: https://www.youtube.com/watch?v=RhGiG-yZP-c, https://www.youtube.com/shorts/zaBDyEfhrnk, https://www.youtube.com/shorts/UcWTeZepXJc.

Section stills were skipped to focus on the hero. The rejected `hero-scaled-m` folder is preserved. No site integration or React changes were made.

Review question for Lilian: Does plate hardness + pulse pacing match APERTURE enough to iterate, or another surface pass?
