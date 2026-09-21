import bpy,json,hashlib,numpy as np
def anim(owner):
 a=getattr(owner,'animation_data',None)
 if not a:return None
 return [(fc.data_path,fc.array_index,[(tuple(k.co),k.interpolation,tuple(k.handle_left),tuple(k.handle_right)) for k in fc.keyframe_points]) for fc in a.action.fcurves] if a.action else []
def signature():
 out={}
 for s in bpy.data.scenes:
  if s.name=='N3_HEAD_TRACK_YAW_BRIDGE':continue
  bpy.context.window.scene=s;s.frame_set(s.frame_start);bpy.context.view_layer.update()
  scene_objects={}
  for o in sorted(s.objects,key=lambda x:x.name):
   h=hashlib.sha256()
   transform=[o.name,o.parent.name if o.parent else None,list(o.matrix_parent_inverse),list(o.location),list(o.rotation_euler),list(o.rotation_quaternion),list(o.scale),o.hide_render,anim(o)]
   # Animation channels are compared exactly below; their transient RNA values
   # can be stale for an inactive scene. Do not hash a cached evaluation state.
   paths={fc[0] for fc in (anim(o) or [])}
   for prop,index in [('location',3),('rotation_euler',4),('rotation_quaternion',5),('scale',6),('hide_render',7)]:
    if prop in paths:transform[index]='ANIMATED_EXACT_CURVES_COMPARED'
   if o.type=='MESH':
    a=np.empty(len(o.data.vertices)*3,dtype=np.float32);o.data.vertices.foreach_get('co',a);h.update(a.tobytes())
    h.update(json.dumps([list(p.vertices) for p in o.data.polygons]).encode())
    if o.data.shape_keys:
     for k in o.data.shape_keys.key_blocks:
      a=np.empty(len(k.data)*3,dtype=np.float32);k.data.foreach_get('co',a);h.update(a.tobytes())
     h.update(json.dumps(anim(o.data.shape_keys)).encode())
   if o.type=='FONT':h.update(o.data.body.encode())
   if o.type=='CURVE':h.update(json.dumps([[list(p.co) for p in sp.points] for sp in o.data.splines]).encode())
   materials=[(m.name,'ANIMATED_EXACT_CURVES_COMPARED' if any(fc[0]=='diffuse_color' for fc in (anim(m) or [])) else list(m.diffuse_color),anim(m)) for m in o.data.materials if m] if o.data and hasattr(o.data,'materials') else []
   scene_objects[o.name]=dict(transform=json.loads(json.dumps(transform,default=list)),geometry=h.hexdigest(),materials=materials)
  out[s.name]=scene_objects
 return out
