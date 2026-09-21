"""Run from Blender Python console via exec(...); call start(config_path).
Local operator controls: STATE.manual_reset(), STATE.arm(), STATE.rebind().
No network command can clear the simulated inhibit latch.
"""
import bpy, json, math, socket, sys
from pathlib import Path
R=Path(__file__).resolve().parent
if str(R) not in sys.path:sys.path.insert(0,str(R))
from bridge_core import ReceiverState
STATE=None
SOCKET=None
SCENE='N3_HEAD_TRACK_YAW_BRIDGE'
LATCH_FILE=R/'receiver_latch_state.tmp'  # local runtime state, deliberately not committed


def persist_latch():
    if STATE:
        value=json.dumps({'latched':STATE.latched,'armed':STATE.armed})
        if not LATCH_FILE.exists() or LATCH_FILE.read_text()!=value:
            pending=LATCH_FILE.with_name('receiver_latch_pending.tmp')
            pending.write_text(value);pending.replace(LATCH_FILE)


def target():
    s=bpy.data.scenes.get(SCENE)
    if s is None:raise RuntimeError('Open the versioned Head Track Yaw successor first')
    candidates=[o for o in s.objects if o.get('head_yaw_target')]
    if len(candidates)!=1:raise RuntimeError('Expected exactly one carrier yaw target')
    return s,candidates[0]


def apply(output):
    s,o=target()
    o.rotation_euler.z=math.radians(output['yaw_cmd'])
    s['head_yaw_state_json']=json.dumps(output)
    bpy.context.view_layer.update()


def poll():
    if SOCKET is None:return None
    # Bounded drain prevents a local flood from monopolizing Blender's UI.
    for _ in range(64):
        try:raw,addr=SOCKET.recvfrom(65535)
        except BlockingIOError:break
        p,out=STATE.ingest(raw)
        apply(out)
    apply(STATE.tick())
    persist_latch()
    return .02  # ASSUMPTION: UI polling interval only, not achieved FPS/latency


def stop():
    global SOCKET
    if bpy.app.timers.is_registered(poll):bpy.app.timers.unregister(poll)
    if SOCKET:SOCKET.close();SOCKET=None
    if STATE:apply(STATE.idle('operator_stop'))
    persist_latch()


def start(config_path=None):
    global STATE,SOCKET
    stop()
    s,o=target()
    bpy.context.window.scene=s
    s.frame_set(1)
    # Live receiver must own yaw; remove replay keys only on the isolated demo target.
    o.animation_data_clear()
    config=json.loads(Path(config_path or R/'config_template.json').read_text(encoding='utf-8-sig'))
    if STATE and STATE.config!=config:raise RuntimeError('Restart Blender to change receiver configuration')
    if STATE is None:
        STATE=ReceiverState(config)
        if LATCH_FILE.exists():
            try:
                saved=json.loads(LATCH_FILE.read_text())
                if type(saved['latched']) is not bool or type(saved['armed']) is not bool:raise ValueError('Invalid latch file')
                STATE.latched=saved['latched'];STATE.armed=saved['armed']
            except (ValueError,KeyError,TypeError):STATE.latched=True;STATE.armed=False
    else:STATE.rebind()  # preserves latch and manual-arm state
    SOCKET=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    SOCKET.bind((config['host'],config['port']));SOCKET.setblocking(False)
    apply(STATE.idle('receiver_started'))
    bpy.app.timers.register(poll)
    print('DIGITAL ONLY receiver',SOCKET.getsockname(),'latch',STATE.latched)
    return STATE
