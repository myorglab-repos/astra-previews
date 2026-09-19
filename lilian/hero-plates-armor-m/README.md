# Armor volume M — p4

Pass: `p4-plates-armor-volume` · Design review pending Lilian.

Viewer: http://127.0.0.1:8765/

Folder: `C:\Users\mfawe\OneDrive\Documents\GitHub\myorglab-marketing\assets\astra\2026-09-19\blender\hero-plates-armor-m`

From the repository root, run `powershell -ExecutionPolicy Bypass -File scripts/open-latest-viewer.ps1`. This selects the newest asset viewer and opens the default browser. The viewer and Draco decoder are local; no CDN is required.

P4 replaces the inflated distance-field crown with a broad, gently bent front and a deep chamfered body. It has 57 rigid front plates and 216 plates around the chamfers and flanks. The narrow satin titanium frames surround planar recessed navy faces. Flat shading, small sharp chamfers, open joints and recessed edge laps replace the large raised frames of p3. Actual depth is 1.114 units across a 4.468-unit width, about 25%. The supplied three-quarter still exposes the wrap and inner returns.

The native LogoFull contour is simplified with 1.4px tolerance and the shoulder crown trimmed by 4px. Straight feet and the central valley remain. This is an intentionally faceted armor interpretation; it does not claim exact pixel identity with the logo or approval against APERTURE.

The embedded `Seam_Pulse_3s` clip has 16 morph-weight tracks. It opens cyan light apertures in a smoothly eased left-to-right wave every 3 seconds; no plates move during the idle loop. A narrower cosine-to-the-fourth peak strengthens the traveling current. The browser synchronizes emission to the same band centers. A tap or Light beat creates the retained 1.3-second expand-and-settle interaction. Pointer follow stays subtle around a fixed three-quarter review angle. Pause removes the canvas and freezes the mixer. Initial reduced motion requests only the poster and controls, and a failed model load also falls back to the poster.

| File | Purpose |
| --- | --- |
| `hero-plates-armor-m.blend` | Editable Blender 3.6 scene, materials, camera, lights and NLA animation |
| `hero-plates-armor-m.glb` | Uncompressed working asset, 999,624 bytes |
| `hero-plates-armor-m.web.glb` | Draco asset, 371,048 bytes; below the 600 KB ceiling |
| `poster.webp` | Transparent ffmpeg WebP poster, 100,890 bytes |
| `poster.master.png` | Transparent 1338 × 936 Blender master |
| `seam-pulse.mp4`, `seam-pulse.webm` | 90 frames at 30fps, one complete 3-second browser loop |
| `index.html`, `viewer.js`, `controls.js`, `review.css`, `vendor/` | Standalone viewer, no React |
| `author.py`, `panel-layout.json`, `native-geometry.json` | Rebuild source and robust clipped panel polygons |
| `layout.py`, `build-tools/` | Optional layout regeneration script and local Python dependencies; not loaded by the viewer |
| `qa/verification.json` | Desktop/mobile behavior and directional pulse checks |
| `qa/package-verification.json` | GLB structure, animation, size, depth and archive hash checks |
| `qa/front-orthographic.png`, `qa/depth-three-quarter.png` | Blender surface, silhouette and volume review |
| `qa/viewer-desktop.png`, `qa/viewer-mobile-motion.png` | Browser review screenshots |
| `qa/compression-raw.png`, `qa/compression-draco.png` | Same-time visual comparison of both models |

Rebuild:

```powershell
& 'C:/Program Files/Blender Foundation/Blender 3.6/blender.exe' --background --python assets/astra/2026-09-19/blender/hero-plates-armor-m/author.py
```

`author.py` consumes the saved layout and needs no Shapely installation inside Blender. Regenerate the optional layout with `python assets/astra/2026-09-19/blender/hero-plates-armor-m/layout.py` before rebuilding if changing the panel arrangement.

With the viewer served on port 8765:

```powershell
node assets/astra/2026-09-19/blender/hero-plates-armor-m/qa/verify.mjs
python assets/astra/2026-09-19/blender/hero-plates-armor-m/qa/package-check.py
node assets/astra/2026-09-19/blender/hero-plates-armor-m/qa/capture-loop.mjs
python assets/astra/2026-09-19/blender/hero-plates-armor-m/qa/encode-previews.py
```

QA passed: 3-second loop with zero endpoint error; 16 aperture peaks in increasing left-to-right order; pointer follow; beat settling; pause/resume; live reduced motion; initial mobile poster-only loading; tap interaction; no mobile overflow; failed-model poster fallback; no normal-use page errors or failed requests. Both GLBs have valid container/buffer bounds and the expected animation channels. This is structural and browser verification, not a Khronos validator certification.

Visual review: planar navy faces, thin sharp frames and deep armored returns are visible in the front and three-quarter stills. The browser uses environment lighting, so its reflections differ from the Cycles poster. Lilian retains the visual approval decision. All 174 files in the p2/p3 archive folders match their pre-pass SHA-256 hashes. No GIF copies or production-site edits were made.

Ask Lilian: Is plate hardness + volume close enough to wire, or one more pass?
