"""Independent reopened-model geometric/lineage audit plus live receiver smoke."""
import bpy,json,math,hashlib,sys,socket,time
import numpy as np
from pathlib import Path
R=Path(__file__).resolve().parent;ROOT=R.parents[2];sys.path.insert(0,str(R))
from scene_signature import signature
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
lineage=json.loads((R/'lineage.json').read_text())
assert sha(Path(bpy.data.filepath))==lineage['successor_sha256']
inherited=signature()
s=bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE'];bpy.context.window.scene=s
src={o.get('N1_source'):o for o in s.objects if o.get('N1_source')}
carrier=s.objects['HEAD_YAW_CARRIER']
fixed=[o for k,o in src.items() if any(q in k for q in ['sewn_outer_cover.004__LOWER','sewn_outer_cover.004__UPPER','G1-SP-201','refillable_textile_volume.004__LOWER','refillable_textile_volume.004__UPPER'])]
assert len(fixed)==5
rows=json.loads((R/'udp_received.json').read_text())
episode=[json.loads(x) for x in (R/'episode.jsonl').read_text().splitlines()]
baseline={};max_fixed=0.;max_cam=0.;A05=0.;G03=float('inf');G05=float('inf');max_yaw_error=0.;arm_relative={};relative_error=0.
def verts(o,dg):
    e=o.evaluated_get(dg);a=np.empty(len(e.data.vertices)*3);e.data.vertices.foreach_get('co',a);m=np.array(e.matrix_world);return a.reshape(-1,3)@m[:3,:3].T+m[:3,3]
def find(q):return next(o for k,o in src.items() if q in k)
for f in range(1,145):
    s.frame_set(f);bpy.context.view_layer.update();dg=bpy.context.evaluated_depsgraph_get()
    for o in fixed:
        m=np.array(o.evaluated_get(dg).matrix_world)
        baseline.setdefault(o.name,m);max_fixed=max(max_fixed,float(abs(m-baseline[o.name]).max()))
    cam=np.array(s.camera.matrix_world);baseline.setdefault('camera',cam);max_cam=max(max_cam,float(abs(cam-baseline['camera']).max()))
    yaw=math.degrees(carrier.rotation_euler.z);r=rows[f-1];p=episode[f-1]
    max_yaw_error=max(max_yaw_error,abs(yaw-r['output']['yaw_cmd']))
    if not r['output']['effective_enable']:assert yaw==0
    if f in (30,68):assert yaw<0 if f==30 else yaw>0
    assert r['head_centroid_x']==p['head_centroid_x']
    # All exposed arm geometry stays fixed in carrier coordinates: only yaw changes.
    inv=np.linalg.inv(np.array(carrier.matrix_world))
    for side in 'LR':
        glove=src[f'M1_{side}__foam_textile_glove'];w=np.array(glove.evaluated_get(dg).matrix_world.translation)
        for suffix,index,count in [('soft_wrist_shear_core',18,12),('distal_soft_wrist_cuff',4,32),('soft_wrist_cover',18,28)]:
            a=verts(src[f'M1_{side}__{suffix}'],dg);A05=max(A05,float(np.linalg.norm(a[index*count:(index+1)*count].mean(0)-w)*1000))
        for sec in 'UF':
            obj=src[f'M1_{side}_{sec}__foam_and_contact_sleeve'];a=verts(obj,dg);cl=a[:37*28].reshape(37,28,3).mean(1)
            G03=min(G03,float((np.linalg.norm(cl[:,:2],axis=1)-.346).min()*1000))
            local=a@inv[:3,:3].T+inv[:3,3];arm_relative.setdefault(obj.name,local)
            relative_error=max(relative_error,float(abs(local-arm_relative[obj.name]).max()))
    lo=verts(find('sewn_outer_cover.004__LOWER'),dg)[:,2].max();up=verts(find('sewn_outer_cover.004__UPPER'),dg)[:,2].min();band=verts(find('sewn_outer_cover.004__ROTATING_SHOULDER_BAND'),dg)[:,2]
    G05=min(G05,float(min(band.min()-lo,up-band.max())*1000))
assert max_fixed==0 and max_cam==0 and max_yaw_error<1e-4 and relative_error<1e-6
assert A05<.01 and G03>0 and G05>0
assert len([o for o in s.objects if o.get('M1_chamber')])==16
assert not [o for o in s.objects if o.get('N1_source','').startswith('M1_ROOT_') and not o.hide_render]
audit=dict(status='PASS',frames=144,fixed_bag_fill_mast_max_matrix_deviation=max_fixed,fixed_camera_max_matrix_deviation=max_cam,yaw_replay_max_error_deg=max_yaw_error,arm_local_geometry_max_deviation_m=relative_error,A05_max_mm=A05,G03_sampled_proxy_min_mm=G03,G05_axial_min_mm=G05,chambers=16,scope='Digital geometric samples only; no loaded clearance, mechanics, sensing performance or impulse qualification.')
# Exercise the real interactive receiver against actual UDP, without saving these test edits.
import blender_receiver as receiver
receiver.start(R/'demo_config.json');tx=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
base=dict(episode[60]);base.update(stream_id='interactive-receiver-audit',seq=0,sent_monotonic_s=time.monotonic())
tx.sendto(json.dumps(base).encode(),('127.0.0.1',18766));receiver.poll()
assert carrier.rotation_euler.z>0
base.update(seq=1,e_stop_asserted=True,sent_monotonic_s=time.monotonic());tx.sendto(json.dumps(base).encode(),('127.0.0.1',18766));receiver.poll();assert carrier.rotation_euler.z==0 and receiver.STATE.latched
receiver.stop();receiver.start(R/'demo_config.json');assert receiver.STATE.latched
receiver.stop();receiver.STATE=None;receiver.start(R/'demo_config.json');assert receiver.STATE.latched
base.update(seq=2,e_stop_asserted=False,sent_monotonic_s=time.monotonic());tx.sendto(json.dumps(base).encode(),('127.0.0.1',18766));receiver.poll();assert carrier.rotation_euler.z==0
receiver.STATE.manual_reset();receiver.STATE.arm()
base.update(seq=3,sent_monotonic_s=time.monotonic());tx.sendto(json.dumps(base).encode(),('127.0.0.1',18766));receiver.poll();assert carrier.rotation_euler.z>0
receiver.STATE.last_rx-=3;receiver.poll();assert carrier.rotation_euler.z==0
receiver.stop();tx.close();audit['interactive_receiver_udp_latch_restart_reset_watchdog']='PASS'
bpy.ops.wm.open_mainfile(filepath=str(ROOT/lineage['source']))
parent=signature();assert parent==inherited
assert all(sha(ROOT/p)==v for p,v in lineage['baselines'].items())
audit['inherited_scenes_unchanged']=len(inherited);audit['baselines_preserved']=len(lineage['baselines'])
audit['inherited_scene_signatures']={k:hashlib.sha256(json.dumps(v,sort_keys=True).encode()).hexdigest() for k,v in inherited.items()}
(R/'model_verification.json').write_text(json.dumps(audit,indent=2))
print('MODEL_AND_LIVE_RECEIVER_PASS',audit,flush=True)
