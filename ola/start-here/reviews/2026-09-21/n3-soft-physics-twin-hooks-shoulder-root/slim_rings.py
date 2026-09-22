"""Thin the left root tube and aim the cue camera at the side of the cues.

ASSUMPTION: ring centroids stay put. Only the cross-section shrinks, and only
near the shoulder. Not a measured diameter. I1_bag_black collar is not edited.
"""
import bpy, json, math
from pathlib import Path
from mathutils import Vector

ROOT = Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag')
PKT = ROOT / 'reviews' / '2026-09-21' / 'n3-soft-physics-twin-hooks-shoulder-root'
YAW = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'Punching_Bag_N3_Head_Track_Yaw.blend'
AFTER = PKT / 'after'
CUES = PKT / 'cues'

scene = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
bpy.context.window.scene = scene


def n1(o):
    return o.get('N1_source') or ''


pad = next(o for o in scene.objects if o.name.startswith('PEDAGOGY_L') and 'CONCEPT_PADDED_ROOT' in o.name)
foam = next(o for o in scene.objects if n1(o) == 'M1_L_U__foam_and_contact_sleeve')
RING = 28


def basis_cos(obj):
    me = obj.data
    if me.shape_keys:
        block = me.shape_keys.key_blocks[0]
        return [Vector(block.data[i].co) for i in range(len(me.vertices))]
    return [Vector(v.co) for v in me.vertices]


def foam_rings():
    cos = basis_cos(foam)
    mw = foam.matrix_world
    world = [mw @ c for c in cos]
    origin = pad.matrix_world.translation
    groups = []
    count = len(cos) // RING
    for s in range(count):
        pts = world[s * RING:(s + 1) * RING]
        c = sum(pts, Vector()) / RING
        r = sum((p - c).length for p in pts) / RING
        groups.append(dict(c=c, r=r, d=(c - origin).length))
    d0 = min(g['d'] for g in groups)
    for i, g in enumerate(groups):
        dist = g['d'] - d0
        if dist <= 0.09:
            g['factor'] = 0.52
        elif dist >= 0.24:
            g['factor'] = 1.0
        else:
            t = (dist - 0.09) / 0.15
            t = t * t * (3 - 2 * t)
            g['factor'] = 0.52 + 0.48 * t
        if i == 0:
            g['tan'] = (groups[1]['c'] - g['c']) if False else None
    for i, g in enumerate(groups):
        if i == 0:
            tan = groups[1]['c'] - g['c']
        elif i == len(groups) - 1:
            tan = g['c'] - groups[i - 1]['c']
        else:
            tan = groups[i + 1]['c'] - groups[i - 1]['c']
        g['tan'] = tan.normalized()
    return groups


groups = foam_rings()
# Fix the forward-reference: recompute tangents now that all centroids exist.
for i, g in enumerate(groups):
    if i == 0:
        tan = groups[1]['c'] - g['c']
    elif i == len(groups) - 1:
        tan = g['c'] - groups[i - 1]['c']
    else:
        tan = groups[i + 1]['c'] - groups[i - 1]['c']
    g['tan'] = tan.normalized()

active = [g for g in groups if g['factor'] < 0.999]
print('RINGS', len(groups), 'active', len(active), 'r0', round(groups[0]['r'], 4), flush=True)


def nearest(world):
    best = None
    best_d = 1e9
    for g in active:
        d = (world - g['c']).length
        if d < best_d:
            best_d = d
            best = g
    return best, best_d


moved_objs = []
for obj in scene.objects:
    if obj.type != 'MESH' or not n1(obj).startswith('M1_L_'):
        continue
    if obj.data.users > 1:
        obj.data = obj.data.copy()
    me = obj.data
    mw = obj.matrix_world.copy()
    inv = mw.inverted()
    keys = list(me.shape_keys.key_blocks) if me.shape_keys else [None]
    count = 0
    for kb in keys:
        n = len(me.vertices)
        for i in range(n):
            co = Vector(kb.data[i].co) if kb else Vector(me.vertices[i].co)
            world = mw @ co
            g, dist = nearest(world)
            limit = max(0.09, g['r'] * 2.4)
            if dist > limit or g['factor'] >= 0.999:
                continue
            delta = world - g['c']
            along = delta.dot(g['tan']) * g['tan']
            perp = delta - along
            new_w = g['c'] + along + perp * g['factor']
            new_l = inv @ new_w
            if kb:
                kb.data[i].co = new_l
            else:
                me.vertices[i].co = new_l
            count += 1
    if me.shape_keys:
        basis = me.shape_keys.key_blocks[0]
        for i, v in enumerate(me.vertices):
            v.co = basis.data[i].co
    me.update()
    if count:
        moved_objs.append(dict(name=obj.name, n1=n1(obj), writes=count))

# Aim the cue camera at the board from the side, looking along -X.
cue_scene = bpy.data.scenes['SOFT_PHYS_CUE_SHEET']
cam = bpy.data.objects['SOFT_PHYS_CUE_CAM']
cam.location = (1.6, 0.0, 0.0)
direction = Vector((0.0, 0.0, 0.0)) - cam.location
cam.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
cam.data.ortho_scale = 0.85

# Pose cues again and render.
hooks = {o['chamber']: o for o in bpy.data.objects if o.name.startswith('SOFT_PHYS_') and 'CUE' not in o.name and 'CARD' not in o.name and o.get('chamber')}
cues = {f'{side}_{sec}': bpy.data.objects[f'SOFT_PHYS_CUE_{side}_{sec}'] for side in 'LR' for sec in 'UFT'}


def pose(values):
    for key, empty in hooks.items():
        empty['p_norm'] = float(values.get(key, 0.0))
    for side in 'LR':
        for sec, names in (('U', ('U1', 'U2', 'U3')), ('F', ('F1', 'F2', 'F3')), ('T', ('T1', 'T2'))):
            ob = cues[f'{side}_{sec}']
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
scene.render.film_transparent = False
for frame in (30, 68):
    scene.frame_set(frame)
    scene.render.filepath = str(AFTER / f'yaw_f{frame:03d}.png')
    bpy.ops.render.render(write_still=True)
    print('STILL', frame, flush=True)

def render_arm(path, frame, side):
    scene.frame_set(frame)
    state = [(o, o.hide_render) for o in scene.objects]
    for o, _ in state:
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
        print('SIL', frame, side, flush=True)

bpy.context.preferences.filepaths.save_version = 0
bpy.ops.wm.save_as_mainfile(filepath=str(YAW))
(PKT / 'ring_slim.json').write_text(json.dumps(dict(
    assumption='Left root tube cross-section scaled toward the thin collar. Centerline kept. ASSUMPTION, not a measured diameter.',
    active_rings=len(active),
    factor_root=0.52,
    objects=moved_objs,
), indent=2))
print('RING_SLIM_DONE', len(moved_objs), flush=True)
