"""Pull the left root centerline toward the thin collar axis.

ASSUMPTION: visual alignment only. The collar axis is the pedagogy collar's
local Y. Distal forearm and glove are outside the fade, so reach is kept.
I1_bag_black is not edited. Right arm is not edited.
"""
import bpy, json
from pathlib import Path
from mathutils import Vector

ROOT = Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag')
PKT = ROOT / 'reviews' / '2026-09-21' / 'n3-soft-physics-twin-hooks-shoulder-root'
YAW = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'Punching_Bag_N3_Head_Track_Yaw.blend'
AFTER = PKT / 'after'
CUES = PKT / 'cues'

scene = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
bpy.context.window.scene = scene
scene.frame_set(68)
bpy.context.view_layer.update()


def n1(o):
    return o.get('N1_source') or ''


pad = next(o for o in scene.objects if o.name.startswith('PEDAGOGY_L') and 'CONCEPT_PADDED_ROOT' in o.name)
inv_pad = pad.matrix_world.inverted()
mw_pad = pad.matrix_world.copy()


def pull_of(y):
    # y=0 is the collar. Negative y runs down the arm.
    if y >= -0.05:
        return 0.82
    if y <= -0.30:
        return 0.0
    t = (-0.05 - y) / 0.25
    t = max(0.0, min(1.0, t))
    t = t * t * (3 - 2 * t)
    return 0.82 * (1.0 - t)


glove_before = None
for o in scene.objects:
    if n1(o) == 'M1_L__foam_textile_glove':
        glove_before = [round(v, 4) for v in o.matrix_world.translation]
        break

moved = []
for obj in scene.objects:
    if obj.type != 'MESH' or not n1(obj).startswith('M1_L_'):
        continue
    if obj.data.users > 1:
        obj.data = obj.data.copy()
    me = obj.data
    mw = obj.matrix_world.copy()
    inv = mw.inverted()
    keys = list(me.shape_keys.key_blocks) if me.shape_keys else [None]
    writes = 0
    for kb in keys:
        for i in range(len(me.vertices)):
            co = Vector(kb.data[i].co) if kb else Vector(me.vertices[i].co)
            p = inv_pad @ (mw @ co)
            k = pull_of(p.y)
            if k <= 0.001:
                continue
            p.x *= (1.0 - k)
            p.z *= (1.0 - k)
            new_l = inv @ (mw_pad @ p)
            if kb:
                kb.data[i].co = new_l
            else:
                me.vertices[i].co = new_l
            writes += 1
    if me.shape_keys:
        basis = me.shape_keys.key_blocks[0]
        for i, v in enumerate(me.vertices):
            v.co = basis.data[i].co
    me.update()
    if writes:
        moved.append(dict(name=obj.name, writes=writes))

bpy.context.view_layer.update()
glove_after = None
for o in scene.objects:
    if n1(o) == 'M1_L__foam_textile_glove':
        glove_after = [round(v, 4) for v in o.matrix_world.translation]

# Cue camera: look from +X toward the board, forward along -X.
cue_scene = bpy.data.scenes['SOFT_PHYS_CUE_SHEET']
cam = bpy.data.objects['SOFT_PHYS_CUE_CAM']
cam.location = (1.55, 0.0, 0.0)
cam.rotation_euler = (0.0, -1.5708, 0.0)
cam.data.type = 'ORTHO'
cam.data.ortho_scale = 0.95
cue_scene.camera = cam

hooks = {o['chamber']: o for o in bpy.data.objects if o.get('chamber') and str(o.name).startswith('SOFT_PHYS_') and 'CUE' not in o.name}


def pose(values):
    for empty in hooks.values():
        empty['p_norm'] = 0.0
    for key, val in values.items():
        hooks[key]['p_norm'] = float(val)
    for side in 'LR':
        for sec, names in (('U', ('U1', 'U2', 'U3')), ('F', ('F1', 'F2', 'F3')), ('T', ('T1', 'T2'))):
            ob = bpy.data.objects[f'SOFT_PHYS_CUE_{side}_{sec}']
            vals = [float(hooks[f'{side}-{n}']['p_norm']) for n in names]
            ob.data.shape_keys.key_blocks['Swell_ASSUMPTION'].value = max(vals)
            diff = vals[0] - vals[1]
            if sec == 'T':
                ob.data.shape_keys.key_blocks['Twist_ASSUMPTION'].value = diff
                ob.data.shape_keys.key_blocks['Bend_ASSUMPTION'].value = 0.0
            else:
                ob.data.shape_keys.key_blocks['Bend_ASSUMPTION'].value = diff
                ob.data.shape_keys.key_blocks['Twist_ASSUMPTION'].value = 0.0


panels = {
    'rest': {},
    'swell': {f'{s}-{c}': 1.0 for s in 'LR' for c in ('U1', 'U2', 'U3', 'F1', 'F2', 'F3')},
    'bend': {f'{s}-U1': 1.0 for s in 'LR'} | {f'{s}-F1': 1.0 for s in 'LR'},
    'twist': {f'{s}-T1': 1.0 for s in 'LR'},
    'return_rest': {},
}
bpy.context.window.scene = cue_scene
for name, vals in panels.items():
    pose(vals)
    bpy.context.view_layer.update()
    cue_scene.render.filepath = str(CUES / f'{name}.png')
    bpy.ops.render.render(write_still=True)
    print('CUE', name, flush=True)
pose({})

bpy.context.window.scene = scene
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False
for frame in (30, 68):
    scene.frame_set(frame)
    scene.render.filepath = str(AFTER / f'yaw_f{frame:03d}.png')
    bpy.ops.render.render(write_still=True)
    print('STILL', frame, flush=True)

def render_arm(path, frame, side):
    scene.frame_set(frame)
    state = [(o, o.hide_render) for o in scene.objects]
    for o, _h in state:
        o.hide_render = not n1(o).startswith(f'M1_{side}_')
    scene.render.film_transparent = True
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    for o, h in state:
        o.hide_render = h
    scene.render.film_transparent = False

for frame in (30, 68):
    for side in 'LR':
        render_arm(AFTER / f'sil_f{frame:03d}_{side}.png', frame, side)

bpy.context.preferences.filepaths.save_version = 0
bpy.ops.wm.save_as_mainfile(filepath=str(YAW))
(PKT / 'align_root.json').write_text(json.dumps(dict(
    assumption='Left root centerline pulled toward the collar axis. ASSUMPTION visual. Not a measured path.',
    pull_at_collar=0.82,
    glove_before=glove_before,
    glove_after=glove_after,
    objects=len(moved),
), indent=2))
print('ALIGN_DONE', glove_before, glove_after, len(moved), flush=True)
