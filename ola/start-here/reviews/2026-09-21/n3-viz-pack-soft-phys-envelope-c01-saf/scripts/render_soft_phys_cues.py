"""Render SOFT_PHYS_CUE_SHEET: rest -> swell -> bend -> twist -> return.

Does not save the blend. Shape values are teaching inputs.
Every numeric hook stays a DESIGN ESTIMATE, DESIGN ASSUMPTION, or HYPOTHESIS.
The twin is not System ID.
"""
import json
import math
from pathlib import Path

import bpy
from mathutils import Vector

ROOT = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag")
PKT = ROOT / "reviews" / "2026-09-21" / "n3-viz-pack-soft-phys-envelope-c01-saf"
RAW = PKT / "raw" / "cue"
RAW.mkdir(parents=True, exist_ok=True)

SWELL = {f"{s}-{c}": 1.0 for s in "LR" for c in ("U1", "U2", "U3", "F1", "F2", "F3")}
BEND = {f"{s}-U1": 1.0 for s in "LR"} | {f"{s}-F1": 1.0 for s in "LR"}
TWIST = {f"{s}-T1": 1.0 for s in "LR"}

# Inclusive frame ranges. Holds and ramps. 12 fps authored review rate, not a measured camera rate.
PHASES = [
    (1, 10, "rest", {}, {}),
    (11, 28, "swell", {}, SWELL),
    (29, 40, "swell", SWELL, SWELL),
    (41, 58, "bend", SWELL, BEND),
    (59, 70, "bend", BEND, BEND),
    (71, 88, "twist", BEND, TWIST),
    (89, 100, "twist", TWIST, TWIST),
    (101, 116, "return", TWIST, {}),
    (117, 126, "rest", {}, {}),
]


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def mix(a, b, t):
    keys = set(a) | set(b)
    return {k: (1.0 - t) * float(a.get(k, 0.0)) + t * float(b.get(k, 0.0)) for k in keys}


def pose_at(frame):
    for start, end, name, a, b in PHASES:
        if start <= frame <= end:
            span = max(1, end - start)
            t = 0.0 if a == b else smooth((frame - start) / span)
            return name, mix(a, b, t)
    return "rest", {}


def main():
    scene = bpy.data.scenes["SOFT_PHYS_CUE_SHEET"]
    bpy.context.window.scene = scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.use_sequencer = False
    scene.render.use_compositing = False
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "MATERIAL"
    scene.render.resolution_x = 980
    scene.render.resolution_y = 560
    scene.render.resolution_percentage = 100

    cam = bpy.data.objects["SOFT_PHYS_CUE_CAM"]
    cam.location = (1.7, 0.0, 0.0)
    cam.rotation_euler = Vector((-1.0, 0.0, 0.0)).to_track_quat("-Z", "Z").to_euler()
    cam.data.type = "ORTHO"
    cam.data.ortho_scale = 1.35
    scene.camera = cam

    hooks = {}
    for ob in bpy.data.objects:
        chamber = ob.get("chamber")
        if chamber and ob.name.startswith("SOFT_PHYS_") and not ob.name.startswith("SOFT_PHYS_CUE"):
            hooks[chamber] = ob
    if len(hooks) < 16:
        raise RuntimeError(f"expected 16 chamber hooks, found {sorted(hooks)}")

    cues = []
    for side in "LR":
        for sec in "UFT":
            ob = bpy.data.objects[f"SOFT_PHYS_CUE_{side}_{sec}"]
            keys = ob.data.shape_keys
            if keys and keys.animation_data:
                for fcu in keys.animation_data.drivers:
                    fcu.mute = True
            cues.append(ob)

    font_path = Path(r"C:\Windows\Fonts\segoeuib.ttf")
    font = bpy.data.fonts.load(str(font_path)) if font_path.exists() else None
    board = bpy.data.collections.get("SOFT_PHYS_CUE_BOARD")
    if font and board:
        mat = bpy.data.materials.get("SOFT_PHYS_CUE_AMBER")
        for side, y in (("L", 0.34), ("R", -0.34)):
            for sec, z in (("U", 0.22), ("F", 0.0), ("T", -0.22)):
                name = f"CUE_LBL_{side}_{sec}"
                if bpy.data.objects.get(name):
                    continue
                curve = bpy.data.curves.new(name, "FONT")
                curve.body = f"{side}-{sec}"
                curve.size = 0.028
                curve.align_x = "CENTER"
                curve.font = font
                label = bpy.data.objects.new(name, curve)
                label.location = (0.0, y, z)
                label.rotation_euler = (0.0, math.radians(-90), 0.0)
                if mat:
                    curve.materials.append(mat)
                board.objects.link(label)

    def apply_pose(values):
        for empty in hooks.values():
            empty["p_norm"] = 0.0
        for key, val in values.items():
            hooks[key]["p_norm"] = float(val)
        for side in "LR":
            for sec, names in (("U", ("U1", "U2", "U3")), ("F", ("F1", "F2", "F3")), ("T", ("T1", "T2"))):
                ob = bpy.data.objects[f"SOFT_PHYS_CUE_{side}_{sec}"]
                vals = [float(hooks[f"{side}-{n}"]["p_norm"]) for n in names]
                blocks = ob.data.shape_keys.key_blocks
                blocks["Swell_ASSUMPTION"].value = max(vals)
                diff = vals[0] - vals[1]
                if sec == "T":
                    blocks["Twist_ASSUMPTION"].value = diff
                    blocks["Bend_ASSUMPTION"].value = 0.0
                else:
                    blocks["Bend_ASSUMPTION"].value = diff
                    blocks["Twist_ASSUMPTION"].value = 0.0

    labels = {}
    last = PHASES[-1][1]
    for frame in range(1, last + 1):
        name, values = pose_at(frame)
        apply_pose(values)
        bpy.context.view_layer.update()
        apply_pose(values)
        scene.frame_set(frame)
        scene.render.filepath = str(RAW / f"{frame:04d}.png")
        bpy.ops.render.render(write_still=True)
        labels[str(frame)] = name
        if frame == 1 or frame % 15 == 0 or frame == last:
            print("CUE_FRAME", frame, name, flush=True)

    meta = {
        "frames": last,
        "fps_authored_review_rate": 12,
        "fps_note": "Authored review rate for the teaching film. Not a measured camera or detector rate.",
        "phase_by_frame": labels,
        "stills": {"rest": 6, "swell": 34, "bend": 64, "twist": 94, "return": 122},
        "assumption": (
            "ASSUMPTION / DESIGN ESTIMATE / HYPOTHESIS. "
            "p_norm is a teaching input in [0, 1], not measured pressure. "
            "Twin is not System ID. B-06 and C-01 stay OPEN."
        ),
    }
    (PKT / "raw" / "cue_phases.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("CUE_RENDER_DONE", last, flush=True)


main()
