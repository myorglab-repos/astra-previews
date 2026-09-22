"""Workbench teaching renders for B-06 keep-out and C-01 coupon boards.

Block sizes are drawing aids. They are not CAD millimeters and not measured clearance.
No blend of the product twin is opened or saved.
"""
import math
import sys
from pathlib import Path

import bmesh
import bpy

ROOT = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag")
PKT = ROOT / "reviews" / "2026-09-21" / "n3-viz-pack-soft-phys-envelope-c01-saf"
B06 = PKT / "raw" / "b06"
C01 = PKT / "raw" / "c01"
B06.mkdir(parents=True, exist_ok=True)
C01.mkdir(parents=True, exist_ok=True)

FONT_PATH = Path(r"C:\Windows\Fonts\segoeuib.ttf")


def new_scene(name):
    scene = bpy.data.scenes.new(name)
    bpy.context.window.scene = scene
    scene.render.engine = "BLENDER_WORKBENCH"
    scene.render.resolution_x = 1500
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.film_transparent = False
    scene.display.shading.light = "STUDIO"
    scene.display.shading.color_type = "MATERIAL"
    scene.display.render_aa = "8"
    if scene.world is None:
        scene.world = bpy.data.worlds.new(name + "_WORLD")
    scene.world.color = (0.07, 0.09, 0.12)
    return scene


def material(name, rgb):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = (*rgb, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)
        bsdf.inputs["Roughness"].default_value = 0.55
    return mat


def link(scene, ob):
    scene.collection.objects.link(ob)
    return ob


def cube(scene, name, loc, scale, mat):
    me = bpy.data.meshes.new(name + "_mesh")
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    ob.scale = scale
    me.materials.append(mat)
    return link(scene, ob)


def cylinder(scene, name, loc, radius, depth, mat, rot=(0.0, 0.0, 0.0)):
    me = bpy.data.meshes.new(name + "_mesh")
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=28, radius1=radius, radius2=radius, depth=depth)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    ob.rotation_euler = rot
    me.materials.append(mat)
    return link(scene, ob)


def text(scene, name, body, loc, size, mat, font):
    curve = bpy.data.curves.new(name, "FONT")
    curve.body = body
    curve.size = size
    curve.align_x = "LEFT"
    if font:
        curve.font = font
    ob = bpy.data.objects.new(name, curve)
    ob.location = loc
    ob.rotation_euler = (math.radians(90), 0.0, 0.0)
    if mat:
        curve.materials.append(mat)
    return link(scene, ob)


def camera_for(scene, loc, ortho):
    data = bpy.data.cameras.new(scene.name + "_CAM")
    data.type = "ORTHO"
    data.ortho_scale = ortho
    ob = bpy.data.objects.new(scene.name + "_CAM", data)
    ob.location = loc
    ob.rotation_euler = (math.radians(90), 0.0, 0.0)
    scene.collection.objects.link(ob)
    scene.camera = ob
    return ob


def paint(ob, rgb, hot):
    gain = 1.0 if hot else 0.22
    ob.data.materials[0].diffuse_color = (*(c * gain for c in rgb), 1.0)


def render_range(scene, folder, count):
    for frame in range(1, count + 1):
        scene.frame_set(frame)
        scene.render.filepath = str(folder / f"{frame:04d}.png")
        bpy.ops.render.render(write_still=True)
        if frame == 1 or frame % 16 == 0 or frame == count:
            print(scene.name, frame, flush=True)


def build_b06(font):
    scene = new_scene("B06_KEEP_OUT_ASSUMPTION")
    camera_for(scene, (0.15, -6.5, 0.15), 4.6)
    ink = material("B06_INK", (0.93, 0.95, 0.97))
    amber = material("B06_AMBER_INK", (0.96, 0.78, 0.42))
    text(
        scene,
        "B06_TITLE",
        "B-06 OPTION B KEEP-OUT  ·  ASSUMPTION ILLUSTRATION",
        (-2.15, -0.4, 1.85),
        0.09,
        amber,
        font,
    )
    text(
        scene,
        "B06_SUB",
        "Not measured clearance. No invented mm. Critical B-06 stays OPEN.",
        (-2.15, -0.4, 1.62),
        0.045,
        ink,
        font,
    )

    stack = [
        ("KO_MAST_HUB", (0.45, 0.48, 0.50), (0.0, 0.0, -1.35)),
        ("KO_YAW_CARTRIDGE", (0.35, 0.55, 0.62), (0.0, 0.0, -0.95)),
        ("KO_PITCH_PIN_PLATE", (0.25, 0.62, 0.38), (0.0, 0.0, -0.55)),
        ("KO_RECESSED_BOOT", (0.72, 0.58, 0.40), (0.0, 0.0, -0.15)),
        ("KO_TEXTILE_EYE_RECESS", (0.78, 0.48, 0.28), (0.0, 0.0, 0.22)),
        ("KO_CONTINUUM", (0.86, 0.45, 0.22), (0.0, 0.0, 0.62)),
        ("KO_SOFT_WRIST_GLOVE", (0.55, 0.36, 0.28), (0.0, 0.0, 1.05)),
    ]
    blocks = []
    for i, (name, rgb, loc) in enumerate(stack):
        mat = material("B06_" + name, rgb)
        ob = cube(scene, name, loc, (0.55, 0.18, 0.16), mat)
        blocks.append((ob, rgb))
        text(scene, "LBL_" + name, name, (0.42, -0.35, loc[2] - 0.04), 0.04, ink, font)

    loops = []
    for name, rgb, loc, scale in (
        ("KO_FLEX_LOOP_SHORT", (0.35, 0.75, 0.95), (-1.15, 0.0, -0.55), (0.16, 0.08, 0.16)),
        ("KO_FLEX_LOOP_MID", (0.30, 0.62, 0.90), (-1.15, 0.0, -0.05), (0.22, 0.08, 0.22)),
        ("KO_FLEX_LOOP_TALL", (0.25, 0.50, 0.85), (-1.15, 0.0, 0.50), (0.28, 0.08, 0.28)),
    ):
        mat = material("B06_" + name, rgb)
        ob = cube(scene, name, loc, scale, mat)
        loops.append((ob, rgb))
        text(scene, "LBL_" + name, name + "  class", (-2.15, -0.35, loc[2] - 0.02), 0.032, ink, font)

    pinch = []
    for name, loc in (
        ("KO_PINCH_PITCH_HINGE", (-1.15, 0.0, -0.95)),
        ("KO_PINCH_PIN_CHEEK", (0.95, 0.0, -0.55)),
        ("KO_PINCH_BOOT_GUARD", (0.95, 0.0, -0.15)),
    ):
        mat = material("B06_" + name, (0.85, 0.28, 0.26))
        ob = cube(scene, name, loc, (0.34, 0.02, 0.22), mat)
        pinch.append((ob, (0.85, 0.28, 0.26)))
        text(scene, "LBL_" + name, name, (loc[0] - 0.15, -0.35, loc[2] + 0.16), 0.026, ink, font)

    text(
        scene,
        "B06_CHAFE",
        "CHAFE SLEEVE UNFROZEN — wait ABS mock fit-check",
        (-2.15, -0.4, -1.7),
        0.038,
        amber,
        font,
    )
    text(
        scene,
        "B06_LOCK",
        "pitch_lock_engaged required before any strike story. Soft does not imply S3.",
        (-2.15, -0.4, -1.95),
        0.034,
        ink,
        font,
    )

    def hot_for(frame):
        # 96 frames. Drawing-aid chapters, not a measured motion.
        if frame <= 12:
            return "all"
        if frame <= 24:
            return "root"
        if frame <= 40:
            return "pitch"
        if frame <= 56:
            return "boot"
        if frame <= 72:
            return "loops"
        if frame <= 84:
            return "pinch"
        return "all"

    count = 96
    for frame in range(1, count + 1):
        chapter = hot_for(frame)
        for i, (ob, rgb) in enumerate(blocks):
            hot = chapter in ("all", "root") and i < 2 or chapter == "pitch" and i == 2 or chapter == "boot" and i in (3, 4) or chapter == "all"
            if chapter == "loops" or chapter == "pinch":
                hot = False
            if chapter == "all":
                hot = True
            paint(ob, rgb, hot)
        for ob, rgb in loops:
            paint(ob, rgb, chapter in ("loops", "all"))
        for ob, rgb in pinch:
            paint(ob, rgb, chapter in ("pinch", "all") and chapter != "all" or chapter == "pinch")
            if chapter == "all" and frame > 84:
                paint(ob, rgb, True)
        scene.frame_set(frame)
        scene.render.filepath = str(B06 / f"{frame:04d}.png")
        bpy.ops.render.render(write_still=True)
        if frame == 1 or frame % 16 == 0:
            print("B06", frame, chapter, flush=True)
    print("B06_RENDER_DONE", flush=True)


def build_c01(font):
    scene = new_scene("C01_COUPON_BOARD_ASSUMPTION")
    camera_for(scene, (0.2, -7.2, 0.05), 5.4)
    ink = material("C01_INK", (0.93, 0.95, 0.97))
    amber = material("C01_AMBER_INK", (0.96, 0.72, 0.28))
    text(
        scene,
        "C01_TITLE",
        "C-01 COUPON GEOMETRY  ·  TEACHING BOARD  ·  NO CAST",
        (-2.45, -0.55, 1.95),
        0.08,
        amber,
        font,
    )
    text(
        scene,
        "C01_SUB",
        "Paper sequence only. Critical C-01 stays OPEN. Not System ID. No PO.",
        (-2.45, -0.55, 1.72),
        0.04,
        ink,
        font,
    )

    bladder = material("C01_BLADDER", (0.86, 0.48, 0.16))
    sleeve = material("C01_SLEEVE", (0.25, 0.55, 0.72))
    boss = material("C01_BOSS", (0.75, 0.78, 0.35))
    later = material("C01_LATER", (0.35, 0.38, 0.42))
    band = material("C01_BAND", (0.55, 0.25, 0.28))

    stations = []

    def add_station(key, objs):
        stations.append((key, objs))

    # TB-01 single sleeved bladder + reserved port boss. Proportions are drawing aids.
    tb01 = []
    tb01.append(cylinder(scene, "TB01_BLADDER", (-1.85, 0.0, -0.15), 0.07, 0.85, bladder))
    tb01.append(cylinder(scene, "TB01_SLEEVE", (-1.85, 0.0, -0.15), 0.10, 0.72, sleeve))
    tb01.append(cylinder(scene, "TB01_NECK", (-1.85, 0.0, 0.40), 0.035, 0.16, bladder))
    tb01.append(cube(scene, "TB01A_PORT_BOSS", (-1.62, 0.0, 0.40), (0.08, 0.08, 0.08), boss))
    text(scene, "TB01_LBL", "TB-01  single bladder", (-2.35, -0.45, -0.85), 0.04, ink, font)
    text(scene, "TB01A_LBL", "TB-01a boss RESERVE", (-2.35, -0.45, -1.05), 0.03, amber, font)
    add_station("tb01", tb01)

    tb02u = []
    for i in range(3):
        ang = math.radians(-90 + i * 120)
        loc = (-0.55 + 0.16 * math.cos(ang), 0.0, -0.05 + 0.16 * math.sin(ang))
        tb02u.append(cylinder(scene, f"TB02U_{i}", loc, 0.045, 0.7, bladder))
    text(scene, "TB02U_LBL", "TB-02-U  FIRST", (-1.05, -0.45, -0.85), 0.04, ink, font)
    text(scene, "TB02U_LBL2", "U1-U3  120-class ASSUMPTION", (-1.15, -0.45, -1.05), 0.026, amber, font)
    add_station("tb02u", tb02u)

    tb02f = []
    for i in range(3):
        ang = math.radians(-90 + i * 120)
        loc = (0.85 + 0.16 * math.cos(ang), 0.0, -0.05 + 0.16 * math.sin(ang))
        tb02f.append(cylinder(scene, f"TB02F_{i}", loc, 0.045, 0.7, later))
    text(scene, "TB02F_LBL", "TB-02-F  AFTER U", (0.35, -0.45, -0.85), 0.04, ink, font)
    add_station("tb02f", tb02f)

    tb03 = []
    tb03.append(cylinder(scene, "TB03_T1", (1.85, 0.0, 0.05), 0.05, 0.38, bladder, (0.0, math.radians(28), 0.0)))
    tb03.append(cylinder(scene, "TB03_T2", (2.15, 0.0, -0.15), 0.05, 0.38, bladder, (0.0, math.radians(-28), 0.0)))
    text(scene, "TB03_LBL", "TB-03  later torsion", (1.55, -0.45, -0.85), 0.04, ink, font)
    add_station("tb03", tb03)

    tb04 = []
    tb04.append(cylinder(scene, "TB04_HOST", (-1.85, 0.15, -1.45), 0.06, 0.4, later))
    tb04.append(cylinder(scene, "TB04_BAND", (-1.45, 0.15, -1.45), 0.11, 0.08, band))
    text(scene, "TB04_LBL", "TB-04  reuses TB-01/02 host + return band", (-2.35, -0.45, -1.85), 0.032, ink, font)
    add_station("tb04", tb04)

    text(
        scene,
        "C01_FOOT",
        "Smooth-On cast is a candidate path on paper. This film is not a cast, a coupon, or a pressure test.",
        (-2.45, -0.55, -2.15),
        0.032,
        amber,
        font,
    )
    for ob in list(scene.objects):
        if ob.type == "MESH" and ob.data.materials and ob.data.materials[0]:
            ob.data.materials[0] = ob.data.materials[0].copy()

    order = ["tb01", "tb02u", "tb02f", "tb03", "tb04", "all"]
    count = 96
    for frame in range(1, count + 1):
        chapter = order[min(len(order) - 1, (frame - 1) // 16)]
        for key, objs in stations:
            hot = chapter == "all" or chapter == key
            for ob in objs:
                rgb = ob.data.materials[0].diffuse_color[:3]
                # Recover the authored color from the first frame by storing it once.
                if "base_rgb" not in ob:
                    ob["base_rgb"] = [float(c) for c in rgb]
                paint(ob, tuple(ob["base_rgb"]), hot)
        scene.frame_set(frame)
        scene.render.filepath = str(C01 / f"{frame:04d}.png")
        bpy.ops.render.render(write_still=True)
        if frame == 1 or frame % 16 == 0:
            print("C01", frame, chapter, flush=True)
    print("C01_RENDER_DONE", flush=True)


def main():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    font = bpy.data.fonts.load(str(FONT_PATH)) if FONT_PATH.exists() else None
    extra = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if "c01" in extra:
        build_c01(font)
    elif "b06" in extra:
        build_b06(font)
    else:
        build_b06(font)
        build_c01(font)
    print("SCHEMATIC_RENDER_DONE", flush=True)


main()
