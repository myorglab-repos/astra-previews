import bpy, math, sys
from mathutils import Vector
argv=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
out=argv[0] if argv else "/workspace/model-b/renders"
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
def mat(name,col,rough=0.5,metal=0.0,sub=0.0):
    m=bpy.data.materials.new(name);m.use_nodes=True
    b=m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(*col,1);b.inputs["Roughness"].default_value=rough;b.inputs["Metallic"].default_value=metal
    return m
M={k:mat(k,*v) for k,v in {
 "vinyl":((0.02,0.02,0.02),0.35),"accent":((0.6,0.03,0.03),0.4),"collar":((0.12,0.12,0.13),0.6),
 "ring":((0.35,0.36,0.38),0.3,0.8),"arm":((0.05,0.35,0.75),0.55),"armband":((0.95,0.45,0.05),0.5),
 "pack":((0.08,0.09,0.1),0.5),"battery":((0.8,0.1,0.05),0.4),"strap":((0.9,0.75,0.1),0.7),
 "chain":((0.6,0.6,0.62),0.25,1.0),"floor":((0.55,0.55,0.57),0.8),"wall":((0.85,0.85,0.83),0.9),"lens":((0.01,0.01,0.02),0.05)}.items()}
def put(o,m): o.data.materials.append(M[m]); return o
def cyl(r,d,loc,m,rot=(0,0,0),v=64):
    bpy.ops.mesh.primitive_cylinder_add(vertices=v,radius=r,depth=d,location=loc,rotation=rot); o=bpy.context.object; bpy.ops.object.shade_smooth(); return put(o,m)
def box(s,loc,m,rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(location=loc,rotation=rot); o=bpy.context.object; o.scale=(s[0]/2,s[1]/2,s[2]/2)
    bpy.ops.object.modifier_add(type='BEVEL'); o.modifiers[-1].width=0.01; o.modifiers[-1].segments=3; return put(o,m)
def torus(R,r,loc,m):
    bpy.ops.mesh.primitive_torus_add(major_radius=R,minor_radius=r,location=loc,major_segments=96,minor_segments=16); o=bpy.context.object; bpy.ops.object.shade_smooth(); return put(o,m)
def tube(pts,r,m):
    cu=bpy.data.curves.new("c","CURVE");cu.dimensions='3D';cu.bevel_depth=r;cu.bevel_resolution=6;cu.resolution_u=24
    sp=cu.splines.new('BEZIER');sp.bezier_points.add(len(pts)-1)
    for bp,p in zip(sp.bezier_points,pts): bp.co=p;bp.handle_left_type=bp.handle_right_type='AUTO'
    o=bpy.data.objects.new("t",cu);sc.collection.objects.link(o);cu.materials.append(M[m]);return o
# room
box((8,8,0.02),(0,0,-0.01),"floor"); box((8,0.05,3),(0,-2.2,1.5),"wall")
# bag 14in x 48in
R=0.178;top=1.9;L=1.22
cyl(R,L,(0,0,top-L/2),"vinyl")
for z in (top-0.04,top-L+0.04): cyl(R+0.004,0.05,(0,0,z),"accent")
# hanging hardware
cyl(0.03,0.08,(0,0,2.52),"chain"); torus(0.05,0.008,(0,0,2.44),"chain")
cyl(0.02,0.2,(0,0,2.68),"chain")
for i in range(4):
    a=i*math.pi/2+math.pi/4; p=Vector((R*0.8*math.cos(a),R*0.8*math.sin(a),top))
    tube([Vector((0,0,2.42)),(Vector((0,0,2.42))+p)/2,p],0.006,"chain")
# collar at top third
cz=top-0.36
cyl(R+0.02,0.13,(0,0,cz),"collar")
for i in range(8):
    a=i*math.pi/4; box((0.03,0.05,0.14),((R+0.035)*math.cos(a),(R+0.035)*math.sin(a),cz),"collar",(0,0,a))
torus(R+0.045,0.018,(0,0,cz+0.09),"ring")
# straps: 3 from ring/swivel down to collar
for i in range(3):
    a=math.pi/2+i*2*math.pi/3
    tube([Vector((0,0,2.43)),Vector(((R+0.03)*math.cos(a),(R+0.03)*math.sin(a),top+0.02)),Vector(((R+0.045)*math.cos(a),(R+0.045)*math.sin(a),cz+0.1))],0.009,"strap")
# pack on back (-Y)
py=-(R+0.12)
box((0.30,0.16,0.34),(0,py,cz-0.02),"pack")
box((0.26,0.02,0.24),(0,py-0.085,cz-0.02),"collar")
box((0.14,0.09,0.11),(0,py-0.12,cz-0.12),"battery")
for dz in (0.08,0.11,0.14): box((0.2,0.005,0.008),(0,py-0.098,cz+dz-0.02),"ring")
# camera pods facing +Y near arm roots
for s in (-1,1):
    cyl(0.025,0.04,(s*0.1,R+0.05,cz+0.13),"pack",(math.pi/2,0,0),32)
    cyl(0.014,0.01,(s*0.1,R+0.072,cz+0.13),"lens",(math.pi/2,0,0),32)
# soft arms from sides curving toward user (+Y)
for s in (-1,1):
    root=Vector((s*(R+0.06),0.02,cz+0.02))
    cyl(0.065,0.08,root,"collar",(0,math.pi/2,0))
    pts=[root+Vector((s*0.04,0,0)),root+Vector((s*0.22,0.12,-0.02)),root+Vector((s*0.26,0.38,-0.06)),root+Vector((s*0.12,0.62,-0.08))]
    tube(pts,0.055,"arm")
    # bellows bands
    cu=bpy.data.curves.new("p","CURVE");cu.dimensions='3D'
    sp=cu.splines.new('BEZIER');sp.bezier_points.add(3)
    for bp,p in zip(sp.bezier_points,pts): bp.co=p;bp.handle_left_type=bp.handle_right_type='AUTO'
    tmp=bpy.data.objects.new("path",cu);sc.collection.objects.link(tmp)
    for k in range(1,9):
        t=k/9.0
        # approximate position on polyline
        seg=min(int(t*3),2);lt=t*3-seg;p=pts[seg].lerp(pts[seg+1],lt)
        d=(pts[seg+1]-pts[seg]).normalized()
        bpy.ops.mesh.primitive_torus_add(major_radius=0.056,minor_radius=0.008,location=p)
        o=bpy.context.object;o.rotation_mode='QUATERNION';o.rotation_quaternion=Vector((0,0,1)).rotation_difference(d);bpy.ops.object.shade_smooth();put(o,"armband")
    bpy.data.objects.remove(tmp)
    # soft fist
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.075,location=pts[-1]+Vector((0,0.04,0)));o=bpy.context.object;o.scale=(1,1.2,0.9);bpy.ops.object.shade_smooth();put(o,"armband")
# lights / world
w=bpy.data.worlds.new("w");sc.world=w;w.use_nodes=True;w.node_tree.nodes["Background"].inputs[0].default_value=(0.9,0.92,0.95,1);w.node_tree.nodes["Background"].inputs[1].default_value=0.6
bpy.ops.object.light_add(type='AREA',location=(2,2.5,3.2));l=bpy.context.object;l.data.energy=900;l.data.size=3;l.rotation_euler=(math.radians(50),0,math.radians(140))
bpy.ops.object.light_add(type='AREA',location=(-2.5,-1,2.5));l=bpy.context.object;l.data.energy=400;l.data.size=3;l.rotation_euler=(math.radians(60),0,math.radians(-60))
sc.render.engine='CYCLES';sc.cycles.device='CPU';sc.cycles.samples=48;sc.cycles.use_denoising=True
sc.render.resolution_x=1400;sc.render.resolution_y=1050;sc.view_settings.view_transform='AgX'
bpy.ops.object.camera_add();cam=bpy.context.object;sc.camera=cam;cam.data.lens=40
def shot(name,loc,tgt):
    cam.location=loc;d=Vector(tgt)-Vector(loc);cam.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=f"{out}/{name}.png";bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath="/workspace/model-b/blender/model_b_concept_v0.blend")
shot("model_b_front_34",(1.9,2.6,1.9),(0,0,1.35))
shot("model_b_back_pack",(-1.4,-1.9,1.9),(0,-0.2,1.5))
shot("model_b_collar_closeup",(0.9,1.1,1.85),(0,0,1.55))
shot("model_b_side_full",(3.4,0,1.5),(0,0,1.4))
