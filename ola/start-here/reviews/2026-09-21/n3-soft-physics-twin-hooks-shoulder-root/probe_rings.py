"""Find the foam sleeve ring layout."""
import bpy, json, math
from pathlib import Path
from mathutils import Vector
import numpy as np

scene = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
obj = next(o for o in scene.objects if (o.get('N1_source') or '') == 'M1_L_U__foam_and_contact_sleeve')
cos = np.array([v.co[:] for v in obj.data.vertices])
n = len(cos)
rows = []
for ring, count in ((28, n // 28), (56, n // 56), (24, n // 24), (32, n // 32)):
    if n % ring:
        continue
    # station-major: ring verts contiguous
    radii = []
    cents = []
    for s in range(count):
        pts = cos[s * ring:(s + 1) * ring]
        c = pts.mean(0)
        cents.append(c)
        radii.append(float(np.linalg.norm(pts - c, axis=1).mean()))
    cents = np.array(cents)
    step = np.linalg.norm(np.diff(cents, axis=0), axis=1)
    rows.append(dict(layout='station-major', ring=ring, stations=count,
                     r_mean=round(float(np.mean(radii)), 4), r_std=round(float(np.std(radii)), 4),
                     step_mean=round(float(step.mean()), 4), step_std=round(float(step.std()), 4)))
    radii = []
    cents = []
    for s in range(count):
        pts = cos[s::count]
        if len(pts) != ring:
            # stride by stations
            pass
        pts = cos[s::count] if False else cos.reshape(count, ring, 3)[s] if False else None
    # ring-major stored as (ring index slow): verts[i] belongs to station i % count? 
    pts_all = cos.reshape(ring, count, 3)  # if ring is the slow? try both
    # already did station-major as contiguous blocks of `ring`
    # alternate: contiguous blocks of `count` would be the other
print('N', n)
# also edge-length based: for each vert, nearest neighbor distance
d = []
for i in range(0, n, 50):
    delta = cos - cos[i]
    dist = np.linalg.norm(delta, axis=1)
    dist[i] = 1e9
    d.append(float(dist.min()))
Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-21\n3-soft-physics-twin-hooks-shoulder-root\probe_rings.json').write_text(json.dumps(dict(n=n, rows=rows, nn=d[:8]), indent=2))
print(json.dumps(rows, indent=2), flush=True)
