"""Slim conceptual shoulder spheres to a thin black collar.

ASSUMPTION: pad color is the twin's existing I1_bag_black (workbench diffuse
0.014, 0.016, 0.018; principled base 0.006, 0.007, 0.008). That is the darkest
bag/mast body this file already displays. No new finish is invented.

Collar size is measured from the foam sleeve at the protected root, then a
thin band (sleeve radius + 14 mm, 90 mm long, 10 mm edge round) replaces the
oversized sphere. HUD curves are left alone. Inherited 2026-09-19 scenes are
not edited.
"""
import bpy, bmesh, json, math, sys
from pathlib import Path
from mathutils import Vector

ROOT = Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag')
OUT = ROOT / 'reviews' / '2026-09-21' / 'n3-shoulder-visual-align-dark'
YAW = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'Punching_Bag_N3_Head_Track_Yaw.blend'
PED = ROOT / 'reviews' / '2026-09-21' / 'n3-b06-pitch-height-pedagogy' / 'Punching_Bag_N3_Pitch_Height_Pedagogy.blend'
SAVE = '--save' in sys.argv
RENDER = '--render-test' in sys.argv or '--render-all' in sys.argv
RENDER_ALL = '--render-all' in sys.argv

BAG = bpy.data.materials['I1_bag_black']
# Workbench uses diffuse_color. Do not mutate the shared bag material.
NOTE = {
    'assumption': 'Pad mesh uses existing I1_bag_black, unmodified.',
    'workbench_diffuse_rgb': [round(c, 5) for c in BAG.diffuse_color[:3]],
    'principled_base_rgb': [round(c, 5) for c in BAG.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value[:3]],
    'cover': 'Thin collar: measured foam-sleeve radius + 0.014 m, 0.090 m long, 0.010 m edge round. Replaces the 0.25 x 0.36 x 0.30 m teaching sphere.',
}


def collar_mesh(mesh, radius, length, fillet, shift_y):
    """Open rounded band along local +Y. Cylinder with softened rims, not a sphere."""
    segs = 48
    half = length * 0.5
    steps = 8
    profile = []
    for i in range(steps + 1):
        theta = math.pi * 0.5 * (steps - i) / steps
        profile.append((-half - fillet * math.sin(theta), radius - fillet * (1 - math.cos(theta))))
    for i in range(1, steps + 1):
        theta = math.pi * 0.5 * i / steps
        profile.append((half + fillet * math.sin(theta), radius - fillet * (1 - math.cos(theta))))
    bm = bmesh.new()
    rings = []
    for y, rad in profile:
        ring = []
        for j in range(segs):
            ang = 2 * math.pi * j / segs
            ring.append(bm.verts.new((rad * math.cos(ang), y + shift_y, rad * math.sin(ang))))
        rings.append(ring)
    for a, b in zip(rings, rings[1:]):
        for j in range(segs):
            j2 = (j + 1) % segs
            bm.faces.new((a[j], a[j2], b[j2], b[j]))
    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.to_mesh(mesh)
    mesh.update()
    bm.free()


def sleeve_radius(pad, scene):
    side = 'L' if pad.name.startswith('PEDAGOGY_L') else 'R'
    inv = pad.matrix_world.inverted()
    dg = bpy.context.evaluated_depsgraph_get()
    radii = []
    ys = []
    for o in scene.objects:
        if o.type != 'MESH' or 'foam_and_contact_sleeve' not in o.name:
            continue
        if f'M1_{side}_' not in o.name:
            continue
        ev = o.evaluated_get(dg)
        me = ev.to_mesh()
        try:
            mw = ev.matrix_world
            for v in me.vertices:
                p = inv @ (mw @ v.co)
                if -0.02 <= p.y <= 0.20 and abs(p.x) < 0.2 and abs(p.z) < 0.2:
                    radii.append(math.hypot(p.x, p.z))
                    ys.append(p.y)
        finally:
            ev.to_mesh_clear()
    if len(radii) < 30:
        return None
    radii.sort()
    # Outer textile surface, ignoring a few stray verts.
    r = radii[int(len(radii) * 0.92)]
    ys.sort()
    return dict(radius=r, y_med=ys[len(ys)//2], samples=len(radii), side=side)


def slim(scene_name, frame):
    scene = bpy.data.scenes[scene_name]
    bpy.context.window.scene = scene
    scene.frame_set(frame)
    bpy.context.view_layer.update()
    report = []
    pads = [o for o in scene.objects if 'CONCEPT_PADDED_ROOT' in o.name and o.type == 'MESH']
    assert len(pads) == 2, pads
    for pad in pads:
        before = dict(scale=list(pad.scale), dims=list(pad.dimensions), mat=pad.data.materials[0].name if pad.data.materials else None)
        measured = sleeve_radius(pad, scene)
        if measured is None:
            radius, shift = 0.062, 0.04
            measured = dict(radius=radius, y_med=shift, samples=0, side=pad.name, fallback=True)
        else:
            radius = measured['radius']
            shift = max(0.02, min(0.08, measured['y_med']))
        outer = radius + 0.014
        pad.scale = (1, 1, 1)
        collar_mesh(pad.data, outer, 0.090, 0.010, shift - 0.045)
        if not pad.data.materials:
            pad.data.materials.append(BAG)
        else:
            pad.data.materials[0] = BAG
        pad['assumption_material'] = 'I1_bag_black'
        pad['assumption_cover'] = 'thin collar, not the prior teaching sphere'
        bpy.context.view_layer.update()
        report.append(dict(name=pad.name, before=before, measured=measured, outer_m=round(outer, 4),
                            shift_y=round(shift - 0.045, 4), after_dims=[round(v, 4) for v in pad.dimensions]))
    return report


reports = {}
reports['pitch'] = slim('N3_PITCH_HEIGHT_PEDAGOGY', 145)
reports['yaw'] = slim('N3_HEAD_TRACK_YAW_BRIDGE', 68)
reports['color'] = NOTE
(OUT / 'pad_edit.json').write_text(json.dumps(reports, indent=2))
print('SLIMMED', json.dumps(reports), flush=True)

if RENDER:
    test = OUT / 'media'
    test.mkdir(parents=True, exist_ok=True)
    jobs = [('N3_PITCH_HEIGHT_PEDAGOGY', 145, test / 'test_pitch_145.png')]
    if RENDER_ALL:
        raw = ROOT / 'reviews' / '2026-09-21' / 'n3-b06-pitch-height-pedagogy' / 'media' / 'raw'
        raw.mkdir(parents=True, exist_ok=True)
        yaw_frames = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'render_frames'
        yaw_frames.mkdir(parents=True, exist_ok=True)
        jobs = []
    for scene_name, frame, path in [('N3_PITCH_HEIGHT_PEDAGOGY', 145, test / 'test_pitch_145.png'),
                                     ('N3_HEAD_TRACK_YAW_BRIDGE', 68, test / 'test_yaw_068.png')]:
        if RENDER_ALL:
            break
        s = bpy.data.scenes[scene_name]
        bpy.context.window.scene = s
        s.frame_set(frame)
        s.render.image_settings.file_format = 'PNG'
        s.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        print('TEST_RENDER', path, flush=True)
    if RENDER_ALL:
        s = bpy.data.scenes['N3_PITCH_HEIGHT_PEDAGOGY']
        bpy.context.window.scene = s
        s.render.image_settings.file_format = 'PNG'
        raw = ROOT / 'reviews' / '2026-09-21' / 'n3-b06-pitch-height-pedagogy' / 'media' / 'raw'
        for f in range(s.frame_start, s.frame_end + 1):
            s.frame_set(f)
            s.render.filepath = str(raw / f'{f:04d}.png')
            bpy.ops.render.render(write_still=True)
            if f % 25 == 0:
                print('PITCH', f, flush=True)
        y = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
        bpy.context.window.scene = y
        y.render.image_settings.file_format = 'PNG'
        ydir = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'render_frames'
        for f in range(y.frame_start, y.frame_end + 1):
            y.frame_set(f)
            y.render.filepath = str(ydir / f'{f:04d}.png')
            bpy.ops.render.render(write_still=True)
            if f % 24 == 0:
                print('YAW', f, flush=True)
        print('RENDER_ALL_DONE', flush=True)

if SAVE:
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=str(YAW))
    bpy.ops.wm.save_as_mainfile(filepath=str(PED))
    print('SAVED', YAW, PED, flush=True)
