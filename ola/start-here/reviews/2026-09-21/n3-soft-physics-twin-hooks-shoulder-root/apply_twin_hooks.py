"""Track A twin pass: soft-physics hooks + left shoulder-root silhouette.

ASSUMPTION: collar color stays the existing material I1_bag_black.
ASSUMPTION: left-root slim is a teaching silhouette. Centerline is kept.
The wide face of the left sleeve at the root is pulled toward its own thin
face so the junction reads closer to the right-side thin collar. This is not
a measured section, not hardware, and not a cyan pad.

Soft-physics objects are DESIGN ESTIMATE / HYPOTHESIS hooks from
docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md section 6.
They do not claim measured pressure, strain, force, or cycle life.
Product bladders are not converted into soft-body FEA.
"""
import bpy, bmesh, json, math
from pathlib import Path
from mathutils import Vector
import numpy as np

ROOT = Path(r'C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag')
PKT = ROOT / 'reviews' / '2026-09-21' / 'n3-soft-physics-twin-hooks-shoulder-root'
YAW = ROOT / 'reviews' / '2026-09-21' / 'n3-head-yaw-live-usb-path' / 'Punching_Bag_N3_Head_Track_Yaw.blend'
BEFORE = PKT / 'before'
AFTER = PKT / 'after'
CUES = PKT / 'cues'
for p in (BEFORE, AFTER, CUES):
    p.mkdir(parents=True, exist_ok=True)

ASSUMPTION = (
    'ASSUMPTION / DESIGN ESTIMATE. Twin cue is not System ID. '
    'Not measured pressure, strain, force, or cycle life. Recalibrate at TB-01..04. '
    'B-06 and C-01 stay OPEN.'
)

scene = bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE']
bpy.context.window.scene = scene
scene.render.image_settings.file_format = 'PNG'
scene.render.film_transparent = False


def n1(o):
    return o.get('N1_source') or ''


def pad_for(side):
    name = 'PEDAGOGY_L' if side == 'L' else 'PEDAGOGY_R'
    return next(o for o in scene.objects if o.name.startswith(name) and 'CONCEPT_PADDED_ROOT' in o.name)


def render_still(path, frame):
    scene.frame_set(frame)
    scene.render.film_transparent = False
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)


def render_arm(path, frame, side):
    scene.frame_set(frame)
    state = [(o, o.hide_render) for o in scene.objects]
    prefix = f'M1_{side}_'
    for o, _ in state:
        o.hide_render = not n1(o).startswith(prefix)
    scene.render.film_transparent = True
    scene.render.filepath = str(path)
    bpy.ops.render.render(write_still=True)
    for o, h in state:
        o.hide_render = h
    scene.render.film_transparent = False


def top_chord(path, rows=28):
    img = bpy.data.images.load(str(path))
    w, h = img.size
    px = img.pixels[:]
    bpy.data.images.remove(img)
    hits = []
    for y in range(h):
        # Blender images are bottom-up.
        src = h - 1 - y
        xs = []
        for x in range(w):
            a = px[(src * w + x) * 4 + 3]
            if a > 0.08:
                xs.append(x)
        if xs:
            hits.append(max(xs) - min(xs) + 1)
    if not hits:
        return dict(median=0, max=0, n=0)
    top = hits[:rows]
    top_s = sorted(top)
    return dict(median=top_s[len(top_s) // 2], max=top_s[-1], n=len(hits))


def slim_left_root(pad):
    """Pull the left root's wide cross-section toward its thin axis.

    ASSUMPTION: visual only. Slice centroids stay put, so the centerline
    and the arm length do not move. Fade-out leaves the distal forearm alone.
    """
    mw_pad = pad.matrix_world.copy()
    inv_pad = mw_pad.inverted()
    edited = []
    for obj in list(scene.objects):
        if obj.type != 'MESH' or not n1(obj).startswith('M1_L_'):
            continue
        if obj.data.users > 1:
            obj.data = obj.data.copy()
        me = obj.data
        mw = obj.matrix_world.copy()
        inv_obj = mw.inverted()
        keys = list(me.shape_keys.key_blocks) if me.shape_keys else [None]
        moved = 0
        for kb in keys:
            n = len(me.vertices)
            pad_pts = []
            for i in range(n):
                co = Vector(kb.data[i].co) if kb else Vector(me.vertices[i].co)
                pad_pts.append(inv_pad @ (mw @ co))
            buckets = {}
            for i, p in enumerate(pad_pts):
                buckets.setdefault(round(p.y, 2), []).append(i)
            for ykey, idxs in buckets.items():
                if len(idxs) < 8:
                    continue
                # Root is near y=0. Distal upper/elbow is more negative.
                y = float(np.mean([pad_pts[i].y for i in idxs]))
                if y < -0.22 or y > 0.06:
                    continue
                pts = np.array([[pad_pts[i].x, pad_pts[i].z] for i in idxs], dtype=float)
                c = pts.mean(axis=0)
                X = pts - c
                cov = (X.T @ X) / max(len(idxs), 1)
                evals, evecs = np.linalg.eigh(cov)
                major = evecs[:, 1]
                spread = np.sqrt(np.maximum(evals, 0))
                if spread[1] < 1e-6:
                    continue
                raw = float(np.clip(spread[0] / spread[1], 0.45, 1.0))
                if y >= -0.05:
                    fade = 0.0
                else:
                    fade = (-0.05 - y) / 0.17
                    fade = max(0.0, min(1.0, fade))
                    fade = fade * fade * (3 - 2 * fade)
                factor = raw + (1.0 - raw) * fade
                if factor > 0.98:
                    continue
                for k, i in enumerate(idxs):
                    delta = X[k]
                    along = float(delta @ major)
                    across = delta - along * major
                    new_xz = c + across + major * (along * factor)
                    p = pad_pts[i]
                    world = mw_pad @ Vector((float(new_xz[0]), p.y, float(new_xz[1])))
                    local = inv_obj @ world
                    if kb:
                        kb.data[i].co = local
                    else:
                        me.vertices[i].co = local
                    moved += 1
        if me.shape_keys:
            basis = me.shape_keys.key_blocks[0]
            for i, v in enumerate(me.vertices):
                v.co = basis.data[i].co
        me.update()
        if moved:
            edited.append(dict(name=obj.name, n1=n1(obj), verts_written=moved, users=me.users))
    return edited


def make_material():
    name = 'SOFT_PHYS_CUE_AMBER'
    mat = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    mat.diffuse_color = (0.86, 0.42, 0.08, 1.0)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get('Principled BSDF')
    if bsdf:
        bsdf.inputs['Base Color'].default_value = (0.86, 0.42, 0.08, 1.0)
        bsdf.inputs['Roughness'].default_value = 0.6
    mat['assumption'] = 'Teaching amber. Not a product finish. Not the retired cyan pad.'
    return mat


def cylinder(name, radius, depth, mat):
    me = bpy.data.meshes.new(name + '_mesh')
    bm = bmesh.new()
    bmesh.ops.create_cone(bm, cap_ends=True, segments=24, radius1=radius, radius2=radius, depth=depth)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    me.materials.append(mat)
    return ob


def add_shape_keys(ob):
    basis = ob.shape_key_add(name='Basis', from_mix=False)
    swell = ob.shape_key_add(name='Swell_ASSUMPTION', from_mix=False)
    bend = ob.shape_key_add(name='Bend_ASSUMPTION', from_mix=False)
    twist = ob.shape_key_add(name='Twist_ASSUMPTION', from_mix=False)
    # Cylinder from create_cone is along local Z. Teaching axis is Z.
    for i, v in enumerate(ob.data.vertices):
        co = v.co
        swell.data[i].co = Vector((co.x * 1.7, co.y * 1.7, co.z))
        bow = (co.z / 0.09) * 0.045
        bend.data[i].co = Vector((co.x, co.y + bow, co.z))
        ang = (co.z / 0.09) * 0.9
        c, s = math.cos(ang), math.sin(ang)
        twist.data[i].co = Vector((c * co.x - s * co.y, s * co.x + c * co.y, co.z))
    bend.slider_min = -1.0
    twist.slider_min = -1.0
    swell.slider_min = 0.0
    swell.slider_max = 1.0
    return basis, swell, bend, twist


def prop(ob, key, value, desc):
    ob[key] = value
    try:
        ob.id_properties_ui(key).update(description=desc)
    except Exception:
        pass


def single_prop(drv, name, target, path):
    var = drv.variables.new()
    var.name = name
    var.type = 'SINGLE_PROP'
    var.targets[0].id_type = 'OBJECT'
    var.targets[0].id = target
    var.targets[0].data_path = path
    return var


def has_driver(keyblock):
    ad = keyblock.id_data.animation_data
    if not ad:
        return False
    token = f'key_blocks["{keyblock.name}"].value'
    return any(token in fc.data_path for fc in ad.drivers)


def add_max_driver(keyblock, empties):
    fcu = keyblock.driver_add('value')
    drv = fcu.driver
    drv.type = 'MAX'
    for i, empty in enumerate(empties):
        single_prop(drv, f'p{i}', empty, '["p_norm"]')
    return fcu


def add_diff_driver(keyblock, a, b):
    fcu = keyblock.driver_add('value')
    drv = fcu.driver
    drv.type = 'SCRIPTED'
    single_prop(drv, 'a', a, '["p_norm"]')
    single_prop(drv, 'b', b, '["p_norm"]')
    drv.expression = 'a-b'
    return fcu


def build_hooks(mat):
    cue_scene = bpy.data.scenes.get('SOFT_PHYS_CUE_SHEET')
    if cue_scene is None:
        cue_scene = bpy.data.scenes.new('SOFT_PHYS_CUE_SHEET')
    cue_scene.render.engine = 'BLENDER_WORKBENCH'
    cue_scene.render.resolution_x = 980
    cue_scene.render.resolution_y = 560
    cue_scene.render.image_settings.file_format = 'PNG'
    cue_scene.display.shading.light = 'FLAT'
    cue_scene.display.shading.color_type = 'MATERIAL'
    if cue_scene.world is None:
        cue_scene.world = bpy.data.worlds.new('SOFT_PHYS_WORLD')
    cue_scene.world.color = (0.08, 0.09, 0.11)

    coll = bpy.data.collections.get('SOFT_PHYSICS_TWIN_HOOKS')
    if coll is None:
        coll = bpy.data.collections.new('SOFT_PHYSICS_TWIN_HOOKS')
    if coll.name not in scene.collection.children:
        scene.collection.children.link(coll)

    card = bpy.data.objects.get('SOFT_PHYS_CARD') or bpy.data.objects.new('SOFT_PHYS_CARD', None)
    if card.name not in coll.objects:
        coll.objects.link(card)
    card.empty_display_type = 'CUBE'
    card.empty_display_size = 0.04
    prop(card, 'assumption', ASSUMPTION, ASSUMPTION)
    prop(card, 'source', 'docs/engineering/ISMAEL_VIRTUAL_SOFT_ARM_PHYSICS.md', 'Paper hook only.')
    prop(card, 'E_ecoflex_MPa_DESIGN_ESTIMATE', 0.118, 'DESIGN ESTIMATE from paper section 1.3. Not a coupon.')
    prop(card, 'E_ds30_MPa_DESIGN_ESTIMATE', 1.02, 'DESIGN ESTIMATE from paper section 1.3. Not a coupon.')
    prop(card, 'stiffness_ratio_DESIGN_ESTIMATE', 8.6, 'DESIGN ESTIMATE Ecoflex softer than DS30. Not measured.')
    prop(card, 'lambda_max_DESIGN_ASSUMPTION', 1.10, 'DESIGN ASSUMPTION textile clamp. Not measured strain.')
    prop(card, 'glove_oz_ASSUMPTION', 14, 'ASSUMPTION baseline glove mass. Not a product measurement.')
    prop(card, 'p_norm_1_kPa_HYPOTHESIS_ecoflex', 40, 'HYPOTHESIS editable constant from paper section 6. Not a setpoint.')
    prop(card, 'B06', 'OPEN', 'Critical B-06 stays open.')
    prop(card, 'C01', 'OPEN', 'Critical C-01 stays open.')
    prop(card, 'return_note', 'DESIGN ESTIMATE return order from paper section 4.4. Vent may dominate. Not a measured cycle.', 'Not cycle life.')

    chambers = {}
    for o in scene.objects:
        ch = o.get('M1_chamber')
        if ch:
            chambers[ch] = o

    hooks = {}
    order = ['U1', 'U2', 'U3', 'F1', 'F2', 'F3', 'T1', 'T2']
    for side in 'LR':
        for ch in order:
            key = f'{side}-{ch}'
            host = chambers[key]
            name = f'SOFT_PHYS_{side}_{ch}'
            empty = bpy.data.objects.get(name) or bpy.data.objects.new(name, None)
            if empty.name not in coll.objects:
                coll.objects.link(empty)
            empty.parent = host
            empty.location = (0.0, 0.0, 0.0)
            empty.empty_display_type = 'SPHERE'
            empty.empty_display_size = 0.012
            prop(empty, 'p_norm', 0.0, 'ASSUMPTION normalized teaching input in [0,1]. Not measured pressure.')
            try:
                empty.id_properties_ui('p_norm').update(min=0.0, max=1.0)
            except Exception:
                pass
            prop(empty, 'chamber', key, 'Frozen chamber id. Object count is not sealed-topology proof.')
            prop(empty, 'assumption', ASSUMPTION, ASSUMPTION)
            prop(empty, 'maps_to', host.name, 'Named product chamber this hook follows. The chamber mesh is not a soft-body solve.')
            hooks[key] = empty

    # Visible teaching cues live in their own scene so the yaw product camera stays clean.
    cue_coll = bpy.data.collections.get('SOFT_PHYS_CUE_BOARD')
    if cue_coll is None:
        cue_coll = bpy.data.collections.new('SOFT_PHYS_CUE_BOARD')
    if cue_coll.name not in cue_scene.collection.children:
        cue_scene.collection.children.link(cue_coll)

    cues = {}
    layout = {'U': 0.22, 'F': 0.0, 'T': -0.22}
    for side, y in (('L', 0.18), ('R', -0.18)):
        for sec, z in layout.items():
            name = f'SOFT_PHYS_CUE_{side}_{sec}'
            ob = bpy.data.objects.get(name)
            if ob is None:
                ob = cylinder(name, 0.016, 0.18, mat)
            if ob.name not in cue_coll.objects:
                cue_coll.objects.link(ob)
            ob.location = (0.0, y, z)
            ob.rotation_euler = (0.0, 0.0, 0.0)
            if ob.data.shape_keys is None:
                add_shape_keys(ob)
            prop(ob, 'assumption', 'Teaching swell-then-bend cue. Not a product close. Not measured strain.', ASSUMPTION)
            prop(ob, 'section', sec, 'U upper, F forearm, T soft wrist.')
            members = [hooks[f'{side}-{sec}{i}'] for i in (('1', '2') if sec == 'T' else ('1', '2', '3'))]
            swell = ob.data.shape_keys.key_blocks['Swell_ASSUMPTION']
            bend = ob.data.shape_keys.key_blocks['Bend_ASSUMPTION']
            twist = ob.data.shape_keys.key_blocks['Twist_ASSUMPTION']
            if not has_driver(swell):
                # U/F: swell is the max teaching input, bend is chamber 1 minus chamber 2.
                # T: swell is the max, twist is T1 minus T2. Bend stays at rest on T.
                add_max_driver(swell, members)
            if sec == 'T':
                if not has_driver(twist):
                    add_diff_driver(twist, hooks[f'{side}-T1'], hooks[f'{side}-T2'])
            else:
                if not has_driver(bend):
                    add_diff_driver(bend, hooks[f'{side}-{sec}1'], hooks[f'{side}-{sec}2'])
            cues[f'{side}_{sec}'] = ob

    cam_data = bpy.data.cameras.get('SOFT_PHYS_CUE_CAM') or bpy.data.cameras.new('SOFT_PHYS_CUE_CAM')
    cam_data.type = 'ORTHO'
    cam_data.ortho_scale = 1.15
    cam = bpy.data.objects.get('SOFT_PHYS_CUE_CAM') or bpy.data.objects.new('SOFT_PHYS_CUE_CAM', cam_data)
    if cam.name not in cue_coll.objects:
        cue_coll.objects.link(cam)
    cam.location = (1.35, 0.0, 0.0)
    cam.rotation_euler = (math.radians(90), 0.0, math.radians(90))
    cue_scene.camera = cam

    light_data = bpy.data.lights.get('SOFT_PHYS_CUE_LIGHT') or bpy.data.lights.new('SOFT_PHYS_CUE_LIGHT', 'SUN')
    light = bpy.data.objects.get('SOFT_PHYS_CUE_LIGHT') or bpy.data.objects.new('SOFT_PHYS_CUE_LIGHT', light_data)
    if light.name not in cue_coll.objects:
        cue_coll.objects.link(light)
    light.rotation_euler = (math.radians(50), 0.0, math.radians(20))
    return cue_scene, hooks, cues


def set_norms(hooks, values):
    for key, empty in hooks.items():
        empty['p_norm'] = float(values.get(key, 0.0))


def apply_cue_pose(cues, hooks):
    """Evaluate the same formulas the drivers encode, so the still does not depend on auto-run."""
    def p(side, ch):
        return float(hooks[f'{side}-{ch}']['p_norm'])
    for side in 'LR':
        for sec, names in (('U', ('U1', 'U2', 'U3')), ('F', ('F1', 'F2', 'F3')), ('T', ('T1', 'T2'))):
            ob = cues[f'{side}_{sec}']
            vals = [p(side, n) for n in names]
            ob.data.shape_keys.key_blocks['Swell_ASSUMPTION'].value = max(vals)
            diff = vals[0] - vals[1]
            if sec == 'T':
                ob.data.shape_keys.key_blocks['Twist_ASSUMPTION'].value = diff
                ob.data.shape_keys.key_blocks['Bend_ASSUMPTION'].value = 0.0
            else:
                ob.data.shape_keys.key_blocks['Bend_ASSUMPTION'].value = diff
                ob.data.shape_keys.key_blocks['Twist_ASSUMPTION'].value = 0.0


def render_cues(cue_scene, hooks, cues):
    panels = {
        'rest': {},
        'swell': {f'{s}-{c}': 1.0 for s in 'LR' for c in ('U1', 'U2', 'U3', 'F1', 'F2', 'F3')},
        'bend': {f'{s}-U1': 1.0 for s in 'LR'} | {f'{s}-U2': 0.0 for s in 'LR'} | {f'{s}-F1': 1.0 for s in 'LR'} | {f'{s}-F2': 0.15 for s in 'LR'},
        'twist': {f'{s}-T1': 1.0 for s in 'LR'} | {f'{s}-T2': 0.0 for s in 'LR'},
        'return_rest': {},
    }
    bpy.context.window.scene = cue_scene
    paths = {}
    for name, vals in panels.items():
        set_norms(hooks, vals)
        apply_cue_pose(cues, hooks)
        bpy.context.view_layer.update()
        path = CUES / f'{name}.png'
        cue_scene.render.filepath = str(path)
        bpy.ops.render.render(write_still=True)
        paths[name] = str(path.relative_to(ROOT)).replace('\\', '/')
    set_norms(hooks, {})
    apply_cue_pose(cues, hooks)
    bpy.context.window.scene = scene
    return paths


def bag_check():
    bag = bpy.data.materials['I1_bag_black']
    pads = []
    cyan = []
    for o in scene.objects:
        if 'CONCEPT_PADDED_ROOT' not in o.name or o.type != 'MESH':
            continue
        mat = o.data.materials[0] if o.data.materials else None
        pads.append(dict(name=o.name, mat=mat.name if mat else None, same=mat == bag,
                         dims=[round(v, 4) for v in o.dimensions]))
        if mat and 'SOFT_BOOT' in mat.name:
            cyan.append(o.name)
    return dict(
        diffuse=[round(c, 5) for c in bag.diffuse_color[:3]],
        pads=pads,
        soft_boot_users=cyan,
    )


def main():
    report = dict(assumption=ASSUMPTION, bag_before=bag_check())
    for frame in (30, 68):
        render_still(BEFORE / f'yaw_f{frame:03d}.png', frame)
        print('BEFORE', frame, flush=True)
    before_chords = {}
    for frame in (30, 68):
        for side in 'LR':
            path = BEFORE / f'sil_f{frame:03d}_{side}.png'
            render_arm(path, frame, side)
            before_chords[f'{frame}_{side}'] = top_chord(path)
            print('CHORD_BEFORE', frame, side, before_chords[f'{frame}_{side}'], flush=True)
    report['root_chord_before'] = before_chords

    pad = pad_for('L')
    report['slim'] = slim_left_root(pad)
    print('SLIMMED', len(report['slim']), flush=True)

    mat = make_material()
    cue_scene, hooks, cues = build_hooks(mat)
    report['hooks'] = sorted(hooks)
    report['cues'] = sorted(cues)
    report['cue_panels'] = render_cues(cue_scene, hooks, cues)

    bpy.context.window.scene = scene
    for frame in (30, 68):
        render_still(AFTER / f'yaw_f{frame:03d}.png', frame)
        print('AFTER', frame, flush=True)
    after_chords = {}
    for frame in (30, 68):
        for side in 'LR':
            path = AFTER / f'sil_f{frame:03d}_{side}.png'
            render_arm(path, frame, side)
            after_chords[f'{frame}_{side}'] = top_chord(path)
            print('CHORD_AFTER', frame, side, after_chords[f'{frame}_{side}'], flush=True)
    report['root_chord_after'] = after_chords
    report['bag_after'] = bag_check()

    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=str(YAW))
    report['blend'] = str(YAW)
    (PKT / 'hook_report.json').write_text(json.dumps(report, indent=2))
    print('APPLY_DONE', flush=True)


main()
