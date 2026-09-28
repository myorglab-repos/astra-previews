import bpy, math, bmesh, sys
from mathutils import Vector, Matrix
out="/workspace/model-b/renders_v5"
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
def mat(name,col,rough=0.5,metal=0.0,sheen=0.0,alpha=1.0):
    m=bpy.data.materials.new(name);m.use_nodes=True;b=m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(*col,1);b.inputs["Roughness"].default_value=rough;b.inputs["Metallic"].default_value=metal
    if sheen: b.inputs["Sheen Weight"].default_value=sheen
    return m
M={k:mat(k,*v) for k,v in {
 "vinyl":((0.015,0.015,0.015),0.35),"accent":((0.55,0.02,0.02),0.4),
 "saddle":((0.02,0.02,0.022),0.8,0,0.6),"arm":((0.008,0.008,0.009),0.28),"glove":((0.22,0.004,0.004),0.3),"cuff":((0.01,0.01,0.011),0.45),
 "pack":((0.05,0.055,0.06),0.45),"battery":((0.75,0.08,0.05),0.4),"webbing":((0.02,0.02,0.02),0.9),
 "steel":((0.7,0.7,0.72),0.25,1.0),"alu":((0.5,0.52,0.55),0.35,1.0),"boot":((0.03,0.03,0.035),0.75,0,0.6),
 "floor":((0.45,0.45,0.47),0.8),"wall":((0.6,0.61,0.62),0.9),"rubber":((0.01,0.01,0.01),0.7),
 "ringmat":((0.012,0.012,0.014),0.7),"bladder":((0.8,0.78,0.72),0.35),"sleeve":((0.06,0.06,0.065),0.8,0,0.5),
 "tag":((0.7,0.03,0.02),0.5)}.items()}
# canvas: woven texture via two crossed wave bands -> bump + colour variation
cm=bpy.data.materials.new("canvas");cm.use_nodes=True;nt=cm.node_tree;b=nt.nodes["Principled BSDF"]
tc=nt.nodes.new("ShaderNodeTexCoord")
w1=nt.nodes.new("ShaderNodeTexWave");w1.bands_direction='X';w1.inputs["Scale"].default_value=900;w1.inputs["Distortion"].default_value=1.5
w2=nt.nodes.new("ShaderNodeTexWave");w2.bands_direction='Z';w2.inputs["Scale"].default_value=900;w2.inputs["Distortion"].default_value=1.5
for w in (w1,w2): nt.links.new(tc.outputs["Object"],w.inputs["Vector"])
mx=nt.nodes.new("ShaderNodeMath");mx.operation='MULTIPLY';nt.links.new(w1.outputs["Fac"],mx.inputs[0]);nt.links.new(w2.outputs["Fac"],mx.inputs[1])
bump=nt.nodes.new("ShaderNodeBump");bump.inputs["Strength"].default_value=0.6;bump.inputs["Distance"].default_value=0.0015;nt.links.new(mx.outputs[0],bump.inputs["Height"]);nt.links.new(bump.outputs["Normal"],b.inputs["Normal"])
ramp=nt.nodes.new("ShaderNodeValToRGB");ramp.color_ramp.elements[0].color=(0.07,0.068,0.055,1);ramp.color_ramp.elements[1].color=(0.16,0.155,0.125,1)
nt.links.new(mx.outputs[0],ramp.inputs["Fac"]);nt.links.new(ramp.outputs["Color"],b.inputs["Base Color"]);b.inputs["Roughness"].default_value=0.92
M["canvas"]=cm
def put(o,m): o.data.materials.append(M[m]); return o
def cyl(r,d,loc,m,rot=(0,0,0),v=96):
    bpy.ops.mesh.primitive_cylinder_add(vertices=v,radius=r,depth=d,location=loc,rotation=rot);o=bpy.context.object;bpy.ops.object.shade_smooth();return put(o,m)
def box(s,loc,m,rotz=0,bev=0.004,rot=None):
    bpy.ops.mesh.primitive_cube_add(location=loc,rotation=rot if rot else (0,0,rotz));o=bpy.context.object;o.scale=(s[0]/2,s[1]/2,s[2]/2)
    bpy.ops.object.modifier_add(type='BEVEL');o.modifiers[-1].width=bev;o.modifiers[-1].segments=3;return put(o,m)
def torus(R,r,loc,m,rot=(0,0,0),q=None,seg=48):
    bpy.ops.mesh.primitive_torus_add(major_radius=R,minor_radius=r,location=loc,rotation=rot,major_segments=seg,minor_segments=10);o=bpy.context.object
    if q is not None: o.rotation_mode='QUATERNION';o.rotation_quaternion=q
    bpy.ops.object.shade_smooth();return put(o,m)
def sphere(r,loc,m,scale=(1,1,1),q=None):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r,location=loc,segments=48,ring_count=24);o=bpy.context.object;o.scale=scale
    if q is not None: o.rotation_mode='QUATERNION';o.rotation_quaternion=q
    bpy.ops.object.shade_smooth();return put(o,m)
def polytube(pts,radii,m,res=6):
    cu=bpy.data.curves.new("c","CURVE");cu.dimensions='3D';cu.bevel_depth=1.0;cu.bevel_resolution=res;cu.use_fill_caps=True
    sp=cu.splines.new('POLY');sp.points.add(len(pts)-1)
    for p_,p,r in zip(sp.points,pts,radii): p_.co=(*p,1);p_.radius=r
    o=bpy.data.objects.new("t",cu);sc.collection.objects.link(o);cu.materials.append(M[m]);return o
def ribbon(pts,radials,w,t,m):
    me=bpy.data.meshes.new("rb");bm=bmesh.new();L=[];Rr=[]
    for i,p in enumerate(pts):
        tg=(pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]).normalized()
        wd=radials[i].cross(tg).normalized()
        L.append(bm.verts.new(p+wd*w/2));Rr.append(bm.verts.new(p-wd*w/2))
    for i in range(len(pts)-1): bm.faces.new((L[i],L[i+1],Rr[i+1],Rr[i]))
    bm.to_mesh(me);bm.free();o=bpy.data.objects.new("rb",me);sc.collection.objects.link(o)
    mo=o.modifiers.new("s",'SOLIDIFY');mo.thickness=t;mo.offset=0
    me.materials.append(M[m]);[setattr(pl,'use_smooth',True) for pl in me.polygons];return o
def arc_shell(R0,thick,h,zc,ca,wa,m,bev=0.01):
    bpy.ops.mesh.primitive_cylinder_add(vertices=256,radius=R0,depth=h,location=(0,0,zc),end_fill_type='NOTHING');o=bpy.context.object
    if wa<2*math.pi-0.01:
        bm=bmesh.new();bm.from_mesh(o.data)
        kill=[v for v in bm.verts if abs(((math.atan2(v.co.y,v.co.x)-ca+math.pi)%(2*math.pi))-math.pi)>wa/2]
        bmesh.ops.delete(bm,geom=kill,context='VERTS');bm.to_mesh(o.data);bm.free()
    bpy.ops.object.modifier_add(type='SOLIDIFY');o.modifiers[-1].thickness=thick;o.modifiers[-1].offset=1
    bpy.ops.object.modifier_add(type='BEVEL');o.modifiers[-1].width=bev;o.modifiers[-1].segments=5
    bpy.ops.object.shade_smooth();return put(o,m)
def P(r,a,z): return Vector((r*math.cos(a),r*math.sin(a),z))
def rad(a): return Vector((math.cos(a),math.sin(a),0))
FRONT=math.pi/2; BACK=-math.pi/2
box((8,8,0.02),(0,0,-0.01),"floor");box((8,0.05,3.2),(0,-2.4,1.6),"wall")
# customer bag 14 x 48 in
R=0.2415;top=1.95;L=1.22
cyl(R,L,(0,0,top-L/2),"vinyl")
for z in (top-0.04,top-L+0.04): cyl(R+0.003,0.05,(0,0,z),"accent")
cyl(0.02,0.25,(0,0,2.83),"steel");cyl(0.035,0.07,(0,0,2.66),"steel");torus(0.05,0.009,(0,0,2.57),"steel",(math.pi/2,0,0))
for i in range(4):
    a=i*math.pi/2+math.pi/4;p=P(R*0.8,a,top)
    polytube([Vector((0,0,2.53))+(p-Vector((0,0,2.53)))*k/6 for k in range(7)],[0.006]*7,"steel",3)
# ---- rear padded saddle (Model A shoulder band, rear portion only) ----
zc=1.50; hs=math.radians(85); sh=0.34; zr=zc+0.06; zs=zc-0.075
arc_shell(R+0.001,0.022,sh,zc,BACK,2*hs,"saddle",0.009)
# narrow curved pack + slide-in battery
arc_shell(R+0.023,0.05,0.24,zc,BACK,0.15/R,"pack",0.012)
arc_shell(R+0.03,0.035,0.075,zc-0.16,BACK,0.10/R,"battery",0.008)
# ---- v5b: two PARALLEL horizontal front straps, 38 mm polyester canvas, one crank ratchet each ----
ZU=zs+0.06; ZL=zs-0.06
RA=float(__import__('os').environ.get('RANG','31')); AA=float(__import__('os').environ.get('AANG','24'))
def hstrap(z,off,thA,thB):
    pts=[];rads=[]
    n=140
    for i in range(n+1):
        th=thA-(thA-thB)*i/n; d=math.degrees(th)
        r=R+0.004+off
        if d>=180 or d<=0: r=R+0.024+off
        elif d>174: r=R+0.004+off+0.02*(d-174)/6
        elif d<6: r=R+0.004+off+0.02*(6-d)/6
        pts.append(P(r,th,z));rads.append(rad(th))
    return pts,rads
straps=[]
for z,ta,tb in ((ZU,270-AA-2,-90+RA),(ZL,270-RA,-90+AA+2)):
    pts,rads=hstrap(z,0.0,math.radians(ta),math.radians(tb)); straps.append(ribbon(pts,rads,0.038,0.0028,"canvas"))
# anchors: upper strap anchored left, lower strap anchored right (ratchets alternate sides)
torus(0.016,0.004,P(R+0.05,math.radians(270-AA),ZU),"steel",(0,math.pi/2,math.radians(270-AA)))
torus(0.016,0.004,P(R+0.05,math.radians(-90+AA),ZL),"steel",(0,math.pi/2,math.radians(-90+AA)))
# crank ratchet (cargo-strap style): frame plates, slotted spool, two toothed wheels, lever with grip, release tab
def ratchet(th,z,open_deg=0,name="r"):
    parts=[]
    def add(o): parts.append(o)
    add(box((0.11,0.018,0.004),(0,0.012,0.024),"steel",bev=0.0015))
    add(box((0.11,0.018,0.004),(0,0.012,-0.024),"steel",bev=0.0015))
    add(box((0.11,0.004,0.052),(0,0.002,0),"steel",bev=0.0015))
    add(cyl(0.008,0.05,(0.025,0.02,0),"alu",(0,0,0),32))
    for zz in (0.028,-0.028):
        add(cyl(0.019,0.004,(0.025,0.02,zz),"steel",(0,0,0),48))
        for k in range(14):
            a=k*2*math.pi/14
            add(box((0.006,0.004,0.004),(0.025+0.021*math.cos(a),0.02+0.021*math.sin(a),zz),"steel",rotz=a,bev=0.0005))
    lever=[]
    lever.append(box((0.13,0.004,0.046),(-0.03,0.0,0.0),"steel",bev=0.0015))
    lever.append(box((0.06,0.016,0.054),(-0.075,0.006,0.0),"rubber",bev=0.006))
    lever.append(box((0.012,0.008,0.03),(0.005,0.006,0.0),"tag",bev=0.002))
    add(cyl(0.014,0.04,(0.025,0.02,0),"canvas",(0,0,0),32))
    a=math.radians(open_deg)
    for o in lever:
        v=o.location.copy();pivot=Vector((0.025,0,0))
        rel=v-pivot;rel=Matrix.Rotation(a,3,'Z')@rel
        o.location=pivot+rel+Vector((0,0.034,0));o.rotation_euler=(0,0,a);parts.append(o)
    bpy.ops.object.select_all(action='DESELECT')
    for o in parts: o.select_set(True)
    bpy.context.view_layer.objects.active=parts[0];bpy.ops.object.convert(target='MESH');bpy.ops.object.transform_apply(location=True,rotation=True,scale=True);bpy.ops.object.join();o=bpy.context.object;o.name=name
    # local x = tangent, y = radial, z = up
    tg=Vector((-math.sin(th),math.cos(th),0));rd=rad(th)
    Mx=Matrix((tg,rd,Vector((0,0,1)))).transposed().to_4x4()
    o.matrix_world=Matrix.Translation(P(R+(0.03 if (math.degrees(th)%360)>180 else 0.008),th,z))@Mx
    return o
rR=ratchet(math.radians(-90+RA),ZU,0,"ratchet_R")
rL=ratchet(math.radians(270-RA),ZL,35,"ratchet_L")
# ---- arm roots at rear-left / rear-right (Model A) ----
roots=[]
for s in (1,-1):
    a=BACK+s*math.radians(58);c=P(R+0.05,a,zr)
    roots.append((s,a,c))
# ---- Model A soft continuum arm: upper section (3 bladders) + flexible saddle + forearm (3 bladders) + soft torsion wrist + glove ----
def qbez(a,m,b,n):
    return [(1-t)**2*a+2*(1-t)*t*m+t*t*b for t in (i/n for i in range(n+1))]
def frames(pts):
    T=[(pts[min(i+1,len(pts)-1)]-pts[max(i-1,0)]).normalized() for i in range(len(pts))]
    N=[T[0].cross(Vector((0,0,1))).normalized()];
    for i in range(1,len(pts)):
        q=T[i-1].rotation_difference(T[i]);N.append((q@N[-1]).normalized())
    return T,N
ARMOBJ={}
def build_arm(key,c,E,W,s,bend_u,bend_f,cut=False):
    objs=[]
    p0=c+ (E-c).normalized()*0.03
    up=qbez(p0,(p0+E)/2+bend_u,E,28)
    fo=qbez(E,(E+W)/2+bend_f,W,28)[1:]
    tgw=(fo[-1]-fo[-2]).normalized()
    wr=[W+tgw*0.105*k/8 for k in range(1,9)]
    pts=up+fo+wr
    rr=[0.034-0.003*i/28 for i in range(29)]+[0.031-0.004*i/28 for i in range(1,29)]+[0.027]*8
    T,N=frames(pts)
    if not cut:
        objs.append(polytube(pts,rr,"arm"))
        # textile restraint bands
        pass  # Model A exposed arm: smooth glossy black cover, no external rib rings
    else:
        # cover removed: three pale bladders at 120 deg per section, knit sleeve bands, red bias stripe
        for sec,(i0,i1,off,rb) in enumerate(((0,29,0.024,0.018),(28,57,0.021,0.016))):
            for k in range(3):
                ang=k*2*math.pi/3
                bp=[pts[i]+(Matrix.Rotation(ang,3,T[i])@N[i])*off for i in range(i0,i1)]
                objs.append(polytube(bp,[rb]*len(bp),"bladder",4))
            for i in range(i0+3,i1,4):
                objs.append(torus(off+rb+0.002,0.003,pts[i],"sleeve",q=Vector((0,0,1)).rotation_difference(T[i])))
            # red programmed bias region on the inner side of the sleeve
            inner=[pts[i]+(Matrix.Rotation(math.pi/3,3,T[i])@N[i])*(off+rb+0.004) for i in range(i0,i1)]
            objs.append(polytube(inner,[0.005]*len(inner),"tag",3))
        # elastic return bands (two per section)
        for ang in (2.3,4.0):
            eb=[pts[i]+(Matrix.Rotation(ang,3,T[i])@N[i])*0.047 for i in range(0,57)]
            objs.append(polytube(eb,[0.004]*len(eb),"rubber",3))
        # wrist torsion cells (opposite helices)
        for hand in (1,-1):
            hp=[];n=24
            for j in range(n+1):
                i=57+min(7,int(j*8/n));f=j/n;ang=hand*f*2*math.pi*1.2
                hp.append(W+tgw*0.105*f+(Matrix.Rotation(ang,3,T[i])@N[i])*(0.024 if hand==1 else 0.03))
            objs.append(polytube(hp,[0.008]*len(hp),"bladder" if hand==1 else "sleeve",3))
    # flexible inter-section saddle (no elbow pin)
    pass  # flexible elbow is under the smooth cover (no visible collar), as on Model A
    # glove on distal wrist cuff
    q=Vector((0,1,0)).rotation_difference(tgw)
    # black wrist cuff (Model A), then deep-red glossy glove: rounded fist + thumb + short cuff
    objs.append(cyl(0.034,0.045,pts[-1]+tgw*0.005,"cuff",(0,0,0),48));objs[-1].rotation_mode='QUATERNION';objs[-1].rotation_quaternion=Vector((0,0,1)).rotation_difference(tgw)
    objs.append(cyl(0.045,0.05,pts[-1]+tgw*0.045,"glove",(0,0,0),48));objs[-1].rotation_mode='QUATERNION';objs[-1].rotation_quaternion=Vector((0,0,1)).rotation_difference(tgw)
    g=pts[-1]+tgw*0.115
    objs.append(sphere(0.062,g,"glove",(1.0,1.25,1.05),q))
    objs.append(sphere(0.024,g+q@Vector((-s*0.05,-0.025,0.035)),"glove",(1,1.5,1),q))
    ARMOBJ[key]=objs;return objs
def pose(s,name):
    x=s;z=zr
    if name=="guard":    return Vector((x*0.36,0.10,z-0.16)),Vector((x*0.22,0.31,z+0.06)),Vector((x*0.06,-0.02,-0.02)),Vector((x*0.07,0.0,-0.12))
    if name=="straight": return Vector((x*0.31,0.27,z+0.01)),Vector((x*0.12,0.68,z+0.06)),Vector((x*0.03,0,0)),Vector((x*0.015,0,0))
    if name=="hook":     return Vector((x*0.46,0.30,z+0.07)),Vector((x*0.06,0.53,z+0.09)),Vector((x*0.04,-0.03,0)),Vector((x*0.05,0.07,0.02))
    if name=="uppercut": return Vector((x*0.35,0.16,z-0.12)),Vector((x*0.12,0.42,z+0.25)),Vector((x*0.04,0,-0.02)),Vector((x*0.03,0.06,-0.06))
for s,a,c in roots:
    E,W,bu,bf=pose(s,"guard");build_arm(("guard",s),c,E,W,s,bu,bf)
sR,aR,cR=roots[0]
for nm in ("straight","hook","uppercut"):
    E,W,bu,bf=pose(sR,nm);build_arm((nm,sR),cR,E,W,sR,bu,bf)
E,W,bu,bf=pose(sR,"guard");build_arm(("cut",sR),cR,E,W,sR,bu,bf,cut=True)
def show(keys):
    for k,objs in ARMOBJ.items():
        for o in objs: o.hide_render=(k not in keys)
# ---- hanger straps: 25 mm polyester canvas, snap hook at bag ring, cam buckle, D-ring on saddle top edge ----
for a in (BACK,BACK+math.radians(70),BACK-math.radians(70)):
    topp=Vector((0,0,2.53))
    pts=[topp+P(0.035,a,-0.01)]
    edge=P(R+0.012,a,top+0.015);low=P(R+0.026,a,zc+sh/2-0.01)
    for k in range(1,13): pts.append(pts[0]+(edge-pts[0])*k/12)
    for k in range(1,13): pts.append(edge+(low-edge)*k/12)
    ribbon(pts,[rad(a)]*len(pts),0.025,0.0025,"canvas")
    torus(0.018,0.005,topp+P(0.035,a,-0.03),"steel",(0,math.pi/2,a))
    mid=edge+(low-edge)*0.35
    box((0.04,0.018,0.045),mid+P(0.006,a,0),"alu",a+math.pi/2)
    torus(0.014,0.004,low+Vector((0,0,0.005)),"steel",(math.pi/2,0,a+math.pi/2))
# ---- secondary retention tether: black 12 mm webbing, red tag (NOT a wire) ----
tpts=[P(R+0.05,BACK,zc+0.12)]
tend=Vector((0.02,-0.03,2.52))
mid1=P(R+0.03,BACK+0.12,top+0.03)
tpts=qbez(tpts[0],mid1,tend,24)
ribbon(tpts,[rad(BACK)]*len(tpts),0.012,0.002,"webbing")
box((0.02,0.004,0.035),P(R+0.052,BACK,zc+0.155),"tag",BACK+math.pi/2,0.002)
# lighting / render
w=bpy.data.worlds.new("w");sc.world=w;w.use_nodes=True;w.node_tree.nodes["Background"].inputs[0].default_value=(0.55,0.57,0.6,1);w.node_tree.nodes["Background"].inputs[1].default_value=0.5
for loc,e,rot in (((2.2,2.6,3.0),700,(50,0,140)),((-2.5,-1.2,2.6),450,(60,0,-60)),((0,3.5,1.2),250,(85,0,180))):
    bpy.ops.object.light_add(type='AREA',location=loc);l=bpy.context.object;l.data.energy=e;l.data.size=2.5;l.rotation_euler=[math.radians(x) for x in rot]
sc.render.engine='CYCLES';sc.cycles.device='CPU';sc.cycles.samples=40;sc.cycles.use_denoising=True
sc.view_settings.view_transform='AgX';sc.view_settings.look='AgX - Punchy'
bpy.ops.object.camera_add();cam=bpy.context.object;sc.camera=cam
def shot(name,loc,tgt,lens=40,res=(1400,1050)):
    sc.render.resolution_x,sc.render.resolution_y=res
    cam.data.lens=lens;cam.location=loc;cam.rotation_euler=(Vector(tgt)-Vector(loc)).to_track_quat('-Z','Y').to_euler()
    sc.render.filepath=f"{out}/{name}{os.environ.get('SUF','')}.png";bpy.ops.render.render(write_still=True)

# ==== v5: COPY Model A (N1) exterior arm objects verbatim; no re-modelling ====
SRC="/workspace/modelA_src/N1.blend"
import os
SHIFT=float(os.environ.get("RSHIFT","0.03")); DZ=float(os.environ.get("DZ","0.19"))
with bpy.data.libraries.load(SRC,link=False) as (fr,to):
    to.objects=[n for n in fr.objects if n.startswith("N1_WHOLE__M1_L") or n.startswith("N1_WHOLE__M1_R") or n.startswith("N1_WHOLE__M1_ROOT_")]
SIDE={}
for side,s_ in (("L",1),("R",-1)):
    a=BACK+s_*math.radians(56); d=Vector((math.cos(a),math.sin(a),0))
    e=bpy.data.objects.new("B_ARM_"+side,None); sc.collection.objects.link(e)
    AS=float(os.environ.get("ASCALE","1.0")); rc=Vector((-0.35 if side=="L" else 0.35,0.234,1.369))
    e.matrix_world=Matrix.Translation(-d*SHIFT+Vector((0,0,DZ)))@Matrix.Rotation(math.pi,4,'Z')@Matrix.Translation(rc)@Matrix.Scale(AS,4)@Matrix.Translation(-rc); SIDE[side]=e
AOBJ=[]
for o in to.objects:
    if o is None: continue
    sc.collection.objects.link(o); AOBJ.append(o)
for o in AOBJ:
    side="L" if ("_L_" in o.name or "_L__" in o.name or "ROOT_L" in o.name) else "R"
    if o.parent is None or o.parent.name.startswith("N1_WHOLE__M1__AZ-H2"):
        o.parent=SIDE[side]; o.matrix_parent_inverse=Matrix.Identity(4)
FR=int(os.environ.get("AFRAME","1")); sc.frame_set(FR)
def show(keys):
    for k,objs in ARMOBJ.items():
        for o in objs: o.hide_render=True
print("IMPORTED",len(AOBJ))
only=sys.argv[sys.argv.index("--")+1:] if "--" in sys.argv else []
G=[("guard",1),("guard",-1)]
def want(n): return not only or n in only
if want("front"): show(G);shot("v5_front_34",(2.1,2.9,2.1),(0,0,1.55))
if want("front_straight"): show(G);shot("v5_front",(0.0,3.2,1.75),(0,0,1.5),50)
if want("back"): show(G);shot("v5_back_34",(-1.7,-2.3,2.0),(0,-0.1,1.6))
if want("back_straight"): show(G);shot("v5_back",(0.0,-2.15,1.6),(0,0,1.45),32)
if want("top"): show(G);shot("v5_top",(0.0,0.9,3.4),(0,0.08,1.5),35)
rp=P(R,math.radians(270-RA),ZL)
if want("ratchet"): show(G);shot("v5_ratchet_detail",tuple(rp+Vector((-0.30,-0.50,0.18))),tuple(rp),40)
if want("top_back"): show(G);shot("v5_top_back",(0.0,-1.0,3.3),(0,-0.08,1.5),35)
if want("strapx"): show(G);shot("v5_strap_cross_detail",(0.30,0.80,zs+0.05),(0,0.17,zs),50)
if want("tether"): show(G);shot("v5_tether_detail",(-0.5,-0.9,2.05),(0,-0.15,1.85),45)
if want("cut"): show([("guard",-1),("cut",1)]);shot("v5_arm_cutaway",(1.2,0.9,1.85),(0.25,0.15,1.5),45)
if want("poses"):
    for nm in ("guard","straight","hook","uppercut"):
        show([("guard",-1),(nm,1)]);shot(f"v5_pose_{nm}",(1.3,1.9,2.4),(0.15,0.25,1.5),42,(800,800))

if want("apose"):
    for pf in [int(x) for x in os.environ.get("PFRAMES","81,321,561,801,1041,1281,1521,1761").split(",")]:
        sc.frame_set(pf); show(G)
        shot(f"v5_apose_f{pf:04d}",(2.1,2.9,2.1),(0,0,1.55),40,(900,675))
        shot(f"v5_apose_top_f{pf:04d}",(0.0,0.9,3.4),(0,0.08,1.5),35,(900,675))
    sc.frame_set(FR)

if want('clear'):
    import json
    import numpy as np
    
    top=1.95;L=1.22;zb=top-L
    sc=bpy.context.scene;res={}
    arms=[o for o in bpy.data.objects if o.name.startswith("N1_WHOLE__M1_") and o.type=='MESH' and "ROOT_" not in o.name]
    frames=list(range(1,1921,8))
    for f in frames:
        sc.frame_set(f);dg=bpy.context.evaluated_depsgraph_get()
        for side in "LR":
            best=(9,None)
            for o in arms:
                if f"_{side}_" not in o.name and f"_{side}__" not in o.name: continue
                if "ROOT" in o.name or "root" in o.name.lower(): continue
                e=o.evaluated_get(dg);m=e.to_mesh();mw=e.matrix_world
                n=len(m.vertices)
                if n:
                    a=np.empty(n*3,dtype=np.float32);m.vertices.foreach_get("co",a);a=a.reshape(-1,3)
                    M=np.array(mw);P=a@M[:3,:3].T+M[:3,3]
                    k=(P[:,2]>zb)&(P[:,2]<top)
                    if k.any():
                        d=float((np.hypot(P[k,0],P[k,1])-R).min())
                        if d<best[0]: best=(d,o.name)
                e.to_mesh_clear()
            res.setdefault(side,[]).append((f,round(best[0]*1000,1),best[1]))
    for s in "LR":
        arr=res[s];mn=min(arr,key=lambda t:t[1])
        print("MIN",s,mn)
        print("PEN",s,[t[:2] for t in arr if t[1]<0][:40])
    json.dump(res,open("/workspace/model-b/clearance_v5.json","w"))
bpy.ops.wm.save_as_mainfile(filepath='/workspace/model-b/blender/model_b_concept_v5.blend')
