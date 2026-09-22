"""Re-render N3_HEAD_TRACK_YAW_BRIDGE from the already-slimmed blend.

Does not edit mesh, does not save the blend, does not remake 2026-09-19 scenes.
Collar material is expected to remain I1_bag_black. Cyan pad material stays unused.
"""
import json
from pathlib import Path

import bpy

ROOT = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag")
PKT = ROOT / "reviews" / "2026-09-21" / "n3-viz-pack-soft-phys-envelope-c01-saf"
RAW = PKT / "raw" / "yaw"
RAW.mkdir(parents=True, exist_ok=True)

scene = bpy.data.scenes["N3_HEAD_TRACK_YAW_BRIDGE"]
bpy.context.window.scene = scene
scene.render.engine = "BLENDER_WORKBENCH"
scene.render.use_sequencer = False
scene.render.use_compositing = False
scene.render.image_settings.file_format = "PNG"
scene.render.film_transparent = False
scene.render.resolution_percentage = 100

bag = bpy.data.materials["I1_bag_black"]
pads = []
cyan_names = []
for ob in scene.objects:
    if ob.type != "MESH":
        continue
    mats = [m.name for m in ob.data.materials if m] if ob.data.materials else []
    if any("SOFT_BOOT" in name or name == "PEDAGOGY_CONCEPT_SOFT_BOOT" for name in mats):
        cyan_names.append(ob.name)
    if "CONCEPT_PADDED_ROOT" in ob.name:
        pads.append(
            {
                "name": ob.name,
                "materials": mats,
                "uses_I1_bag_black": "I1_bag_black" in mats,
                "dimensions_m_ASSUMPTION_visual": [round(float(v), 4) for v in ob.dimensions],
            }
        )

audit = {
    "scene": scene.name,
    "engine": scene.render.engine,
    "resolution": [scene.render.resolution_x, scene.render.resolution_y],
    "frame_start": scene.frame_start,
    "frame_end": scene.frame_end,
    "I1_bag_black_diffuse_rgb": [round(float(c), 5) for c in bag.diffuse_color[:3]],
    "pads": pads,
    "soft_boot_mesh_names": cyan_names,
    "note": "Dimensions are the twin silhouette. Not a measured section. Not hardware.",
}
(PKT / "raw" / "yaw_scene_audit.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")
print("YAW_AUDIT", json.dumps(audit), flush=True)
if cyan_names:
    raise RuntimeError("cyan pad material still assigned: " + ", ".join(cyan_names))
if not pads or not all(p["uses_I1_bag_black"] for p in pads):
    raise RuntimeError("padded roots are not all on I1_bag_black: " + json.dumps(pads))

start = int(scene.frame_start)
end = int(scene.frame_end)
for frame in range(start, end + 1):
    scene.frame_set(frame)
    scene.render.filepath = str(RAW / f"{frame:04d}.png")
    bpy.ops.render.render(write_still=True)
    if frame == start or frame % 12 == 0 or frame == end:
        print("YAW_FRAME", frame, flush=True)
print("YAW_RENDER_DONE", end, flush=True)
