"""Clone accepted scene; run actual OpenCV sender -> UDP -> bpy; bake received yaw."""
import bpy,json,hashlib,math,socket,subprocess,sys,time
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parent;ROOT=R.parents[2]
sys.path.insert(0,str(R))
from bridge_core import ReceiverState
from scene_signature import signature
SOURCE=R.parent/'n3-b06-pitch-height-pedagogy/Punching_Bag_N3_Pitch_Height_Pedagogy.blend'
DEST=R/'Punching_Bag_N3_Head_Track_Yaw.blend'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert Path(bpy.data.filepath).resolve()==SOURCE.resolve()
assert sha(SOURCE)=='3e7a93ed92dc41ff5871f6b49c8ce720f3189177cfc54e319abb4b348b5f64ab'
before=signature()
source=bpy.data.scenes['N3_PITCH_HEIGHT_PEDAGOGY'];bpy.context.window.scene=source;source.frame_set(145)
bpy.context.view_layer.update()
bpy.ops.scene.new(type='FULL_COPY');s=bpy.context.scene;s.name='N3_HEAD_TRACK_YAW_BRIDGE'
for o in s.objects:
    o.animation_data_clear()
    if o.data and hasattr(o.data,'animation_data_clear'):o.data.animation_data_clear()
    if o.type=='MESH' and o.data.shape_keys:o.data.shape_keys.animation_data_clear()
    if o.data and hasattr(o.data,'materials'):
        for i,m in enumerate(o.data.materials):
            if m:
                m=m.copy();m.animation_data_clear();o.data.materials[i]=m
                if m.node_tree:m.node_tree.animation_data_clear()
    # Remove pitch-only explanation in yaw scene; preserve fixed floor/bag datums.
    if o.name.startswith('PEDAGOGY_') and any(x in o.name for x in ('PITCH_AXIS','FIXED_HORIZONTAL','ANGLE_ARC')):o.hide_render=True
carrier=next(o for o in s.objects if o.get('N1_source')=='M1__AZ-H2__bearing_supported_arm_carrier')
carrier.name='HEAD_YAW_CARRIER';carrier['head_yaw_target']=True
camera=s.camera;camera.location=(0,-5,3.4);camera.rotation_euler=(Vector((0,-.05,1.1))-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.ortho_scale=3.5
s.frame_start=1;s.frame_end=144;s.render.fps=12
s.render.resolution_x=790;s.render.resolution_y=650;s.render.resolution_percentage=100
s.render.engine='BLENDER_WORKBENCH';s.render.use_sequencer=False;s.display.render_aa='8'
s['scope']='DIGITAL TWIN ONLY: detected centroids from synthetic translated-still clip; simulated presence. Track A does not prove strike impulse or real-gym sensing.'
s['mapping_assumptions']=(R/'demo_config.json').read_text()
cfg=json.loads((R/'demo_config.json').read_text());state=ReceiverState(cfg)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM);sock.bind((cfg['host'],cfg['port']));sock.settimeout(30)
python=str(Path.home()/'AppData/Local/Programs/Python/Python311/python.exe')
cmd=[python,str(R/'capture_head.py'),'--clip',str(R/'media/input_synthetic.avi'),'--timeline',str(R/'presence_timeline.json'),'--config',str(R/'demo_config.json'),'--head-spotcheck-approved','--send','--wait-ack','--log',str(R/'episode.jsonl')]
log=(R/'capture_process.log').open('w');process=subprocess.Popen(cmd,stdout=log,stderr=subprocess.STDOUT)
received=[]
try:
    for frame in range(1,145):
        raw,addr=sock.recvfrom(65535);p,out=state.ingest(raw)
        if p is None:raise RuntimeError('Rejected detector packet: '+str(out))
        assert p['seq']==frame-1
        carrier.rotation_euler.z=math.radians(out['yaw_cmd']);carrier.keyframe_insert('rotation_euler',index=2,frame=frame)
        bpy.context.view_layer.update()
        received.append(dict(frame=frame,seq=p['seq'],stimulus=p['stimulus'],head_centroid_x=p['head_centroid_x'],output=out,carrier_yaw_deg=math.degrees(carrier.rotation_euler.z)))
        sock.sendto(json.dumps(dict(seq=p['seq'],accepted=True)).encode(),addr)
    raw,addr=sock.recvfrom(65535);p,out=state.ingest(raw);assert p and not out['effective_enable'] and out['yaw_cmd']==0
    assert process.wait(timeout=30)==0
finally:
    sock.close();log.close()
    if process.poll() is None:process.kill();process.wait()
for fc in carrier.animation_data.action.fcurves:
    for key in fc.keyframe_points:key.interpolation='CONSTANT'
s['receiver_target']=carrier.name;s['episode']='episode.jsonl'
s.frame_set(1);bpy.context.view_layer.update()
assert signature()==before,'Source scenes modified'
bpy.context.window.scene=s;s.frame_set(1)
bpy.context.preferences.filepaths.save_version=0
bpy.ops.wm.save_as_mainfile(filepath=str(DEST))
prior=json.loads((SOURCE.parent/'lineage.json').read_text());baselines=prior['baselines'];baselines[SOURCE.relative_to(ROOT).as_posix()]=sha(SOURCE)
(R/'lineage.json').write_text(json.dumps(dict(source=SOURCE.relative_to(ROOT).as_posix(),source_sha256=sha(SOURCE),successor_sha256=sha(DEST),blender=bpy.app.version_string,baselines=baselines,method='FULL_COPY of accepted pitch/yaw pedagogy at frame 145; freeze pose, isolated camera and detected UDP yaw keys. Five inherited scenes unchanged.'),indent=2))
(R/'udp_received.json').write_text(json.dumps(received,indent=2))
(R/'integration_verification.json').write_text(json.dumps(dict(status='PASS',transport='actual loopback UDP/JSON',detector='OpenCV Haar',packets_applied=len(received),EOF_idle=True,sender_command=cmd,performance_claim='NONE; per-frame acknowledgements pace offline integration, not a real-time benchmark'),indent=2))
print('BRIDGE_BUILT',DEST,flush=True)
