"""Did the left sleeve basis actually move?"""
import bpy, json
from pathlib import Path
scene = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
rows = []
for o in scene.objects:
    src = o.get('N1_source') or ''
    if not src.startswith('M1_L_') or o.type != 'MESH':
        continue
    me = o.data
    bb = [round(v, 4) for v in o.dimensions]
    sk = me.shape_keys.key_blocks.keys() if me.shape_keys else []
    rows.append(dict(name=o.name, n1=src, dims=bb, verts=len(me.vertices), sk=len(sk), users=me.users))
hooks = [o.name for o in bpy.data.objects if o.name.startswith('SOFT_PHYS')]
Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-21\n3-soft-physics-twin-hooks-shoulder-root\check_slim.json').write_text(json.dumps(dict(rows=rows, hooks=hooks, scenes=[s.name for s in bpy.data.scenes]), indent=2))
print('CHECK', len(rows), len(hooks), flush=True)
