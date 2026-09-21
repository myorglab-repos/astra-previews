# Full LogoFull lockup in 3D

Pass: p8-logotrue-extrude-full
Local viewer: http://127.0.0.1:8778/

Original M plus all eight MYORGLAB glyphs, image-traced directly from the untouched source. Nine closed meshes parented as one animated asset. Letter holes, spacing and source lockup placement are preserved. No substituted font or invented mark.

Depth: 0.195 units (19.5 source pixels), bevel radius: 0.0025 units (0.25 pixels), 100 source pixels per unit. Original source-projected M colors preserve the blue/cyan crossing and dark folded gradients. Wordmark face is #00123F. Emission-based faces preserve brand appearance; the narrow extrusion edges use satin shaded materials. This is intentionally a faithful shallow logo extrusion.

## Files

- `hero-logotrue-extrude-full.blend`: 3,085,216 bytes
- `hero-logotrue-extrude-full.glb`: 823,240 bytes
- `hero-logotrue-extrude-full.web.glb`: 203,188 bytes
- `poster.webp`: 91,244 bytes
- `spin-preview.mp4`: 329,931 bytes
- `spin-preview.webm`: 333,376 bytes

Also included: standalone vanilla HTML/CSS/Three.js viewer, all local vendor dependencies, original source copies, trace.py, contours.json, author.py, source-color-texture.png, and QA reports/screenshots. The Blender file packs its texture. The GLBs embed geometry, texture and the intrinsic animation. No CDN, React or external app code is needed.

## Fidelity QA

The source PNG alpha is opaque over both artwork and its white background, except two white edge rows. Therefore literal alpha IoU would compare the white canvas. The measured artwork mask is explicitly extracted with min(R,G,B)<140. No resizing, registration, bounding-box normalization or best-fit alignment is used.

Blender front render: 99.9943% full IoU; M 100%; wordmark 99.9855%. All eight glyphs individually exceed 99.95%. Browser-rendered Draco GLB: 100% full / M / wordmark thresholded IoU. This is silhouette agreement, not a claim of identical RGB/antialias pixels.

Review qa/comparison.png, qa/source-vs-front-overlay.png, qa/front-on-white.png, qa/silhouette.json and qa/web-silhouette.json. Nine meshes are closed and have positive volume (qa/mesh-validation.json). Original source copies match originals by SHA-256. Desktop and 390x844 mobile browser checks pass with no normal-use page errors or failed requests. Reduced-motion loads only the static poster; model failure falls back to poster. Physical-phone review remains for after publication.

## Motion

6.2 seconds, one shot: two-turn cubic ease-out to 10 degrees shy at 3.40s, brief stop, quintic settle to exact front by 4.20s, hold thereafter. The full horizontal lockup turns as one asset. Both GLBs contain the animation; MP4 (H.264/yuv420p/faststart) and WebM (VP9) are 1280x540, 30fps. ffmpeg encoded both movies and the lossless WebP poster. No GIFs were copied.

Viewer controls: Front view, Show depth (25 degrees), Spin up, Pause/Play motion. The viewer starts with one spin, then holds. Reduced-motion shows the front poster.

## Rebuild

Run python trace.py; run Blender 3.6 in background with --python author.py. QA scripts are in qa/. Run a local HTTP server at this folder (port 8778), then run node qa/verify.mjs and node qa/capture.mjs. check_silhouette.py compares the generated poster. validate_blend.py runs inside Blender. package.py validates the films and generates the publish archive.

## Handoff

Pages is not published. pages-snapshot.zip contains the runtime under lilian/hero-logotrue-extrude-full/. See PUBLISH_FOR_IBRAHIM.md. Browser auto-open was attempted; automatic approval review rejected the launch with “blocked by policy”. The local viewer remains available at the URL above.

Lilian / Michael: Full lockup extrusion OK for the temporary logo page, or M-only + flat wordmark?
