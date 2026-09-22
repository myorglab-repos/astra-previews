"""Point the cue camera at the board and render the teaching stills."""
import bpy
from pathlib import Path
from mathutils import Vector

CUES = Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-21\n3-soft-physics-twin-hooks-shoulder-root\cues')
scene = bpy.data.scenes['SOFT_PHYS_CUE_SHEET']
bpy.context.window.scene = scene
cam = bpy.data.objects['SOFT_PHYS_CUE_CAM']
cam.location = (1.7, 0.0, 0.0)
cam.rotation_euler = Vector((0.0, 0.0, -1.0)).to_track_quat('-Z', 'Z').to_euler() if False else (0.0, 1.5708, 0.0)
cam.rotation_euler = Vector((-1.0, 0.0, 0.0)).to_track_quat('-Z', 'Z').to_euler()
fwd = cam.matrix_world.to_3x3() @ Vector((0, 0, -1))
print('FWD', tuple(round(c, 3) for c in fwd), flush=True)
cam.data.ortho_scale = 1.35
scene.camera = cam

hooks = {o['chamber']: o for o in bpy.data.objects if o.get('chamber') and o.name.startswith('SOFT_PHYS_')}


def pose(values):
    for empty in hooks.values():
        empty['p_norm'] = 0.0
    for key, val in values.items():
        hooks[key]['p_norm'] = val
    for side in 'LR':
        for sec, names in (('U', ('U1', 'U2', 'U3')), ('F', ('F1', 'F2', 'F3')), ('T', ('T1', 'T2'))):
            ob = bpy.data.objects[f'SOFT_PHYS_CUE_{side}_{sec}']
            vals = [float(hooks[f'{side}-{n}']['p_norm']) for n in names]
            sk = ob.data.shape_keys.key_blocks
            sk['Swell_ASSUMPTION'].value = max(vals)
            diff = vals[0] - vals[1]
            if sec == 'T':
                sk['Twist_ASSUMPTION'].value = diff
                sk['Bend_ASSUMPTION'].value = 0.0
            else:
                sk['Bend_ASSUMPTION'].value = diff
                sk['Twist_ASSUMPTION'].value = 0.0


panels = {
    'rest': {},
    'swell': {f'{s}-{c}': 1.0 for s in 'LR' for c in ('U1', 'U2', 'U3', 'F1', 'F2', 'F3')},
    'bend': {f'{s}-U1': 1.0 for s in 'LR'} | {f'{s}-F1': 1.0 for s in 'LR'},
    'twist': {f'{s}-T1': 1.0 for s in 'LR'},
    'return_rest': {},
}
for name, vals in panels.items():
    pose(vals)
    bpy.context.view_layer.update()
    scene.render.filepath = str(CUES / f'{name}.png')
    bpy.ops.render.render(write_still=True)
    print('CUE', name, flush=True)
pose({})
bpy.context.preferences.filepaths.save_version = 0
bpy.ops.wm.save_mainfile()
print('CUE_CAM_SAVED', flush=True)
