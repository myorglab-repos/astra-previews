"""Build the bounded A-J review packet from measured digital test outputs."""
from pathlib import Path
import datetime,html,json,sys
import mistune
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
a=read('model_verification.json');m=read('media_verification.json')
scope='**Track A does not prove strike impulse.** B-06 root hardware and C-01 pressure-to-motion-to-impact measurements remain Critical OPEN. No physical actuation, measured sensing accuracy, detector FPS, latency, durability or safety qualification is claimed.'
freeze='Eight soft continuum chambers per arm: U1–U3, F1–F3, T1–T2; textile strain limiting, vent plus elastic return and no exposed distal metal. Bag/fill/mast stay fixed; only the shoulder carrier yaws. Protected-root cover remains an illustrative envelope.'
glossary='''## Plain-language glossary

| Term | Everyday meaning | Why it matters in this pass |
|---|---|---|
| ROI / bbox / centroid | Image region / rectangle around a detected face / its center. | Horizontal center supplies the yaw cue; no identity is inferred. |
| Head hypothesis | A tentative face detection. | One-face plus operator spot-check is a demo prior, not qualified sensing. |
| Carrier yaw | Shoulders turning around the mast. | The filled bag must remain stationary. |
| UDP / replay | Local message transport / playing saved inputs again. | Actual detector packets drive Blender; film playback is baked from those packets. |
| Presence stub | An injected yes/no signal. | This pass has no ToF/PIR/mat hardware. |
| Inhibit latch / watchdog | A stop that stays set / a check for missing fresh data. | Chase stops on a fault; manual reset and arm are separate local actions. |
| ASSUMPTION / TBD—Lead | A working demo choice / a decision still owned by Ola. | Demo angles and timeouts are not hardware limits or performance targets. |
| A-05 / A-03 | Wrist alignment / chamber-group teaching cues. | Alignment is audited; accepted U/F/T cues stay preserved. |
| G-03 / G-05 | Arm-to-bag proxy gap / carrier-to-cover axial gap. | Sampled digital geometry does not qualify loaded clearances. |
| B-06 / C-01 | Unqualified root hardware / missing propulsion and impact measurements. | Both remain Critical OPEN regardless of this film. |
| Track A / Track D | Digital visualization / perception-action engineering. | This bridge proves software integration on a synthetic clip, not real-world CV performance. |

What changed / what is still not proven: detected image position now turns the virtual shoulders with simulated gates; real camera performance, physical stops, root structure and punch power remain unproven.
'''
assumptions='''## Assumptions and Lead decisions

| Item | Implementation proposal / demo value | Status |
|---|---|---|
| Detector | OpenCV bundled frontal-face Haar; default detector parameters; exactly one candidate | ASSUMPTION; face is a head prior, no confidence/accuracy bar |
| Qualitative validity | Candidate accepted only with explicit `--head-spotcheck-approved` | ASSUMPTION; fixture visually checked; future live scene needs its own check |
| Normalization / units / sign | Frame fraction [0,1]; degrees; signed offset = 2x−1; positive yaw turns -Y home toward +X | ASSUMPTION; camera mirroring/mount calibration TBD—Lead |
| Gain / clamp | Production template null; opt-in demo 30 degrees per signed unit, ±30-degree clamp | ASSUMPTION demo only, not an approved motion range; normative mapping TBD—Lead |
| Idle | Immediate digital home-zero; no tween or hold-last | ASSUMPTION; physical return policy TBD—Lead |
| Watchdog / poll | Demo 2-second freshness window; 0.02-second requested UI poll | ASSUMPTION software settings, not achieved latency/FPS or safety bars; Lead TBD |
| Transport | Loopback-only UDP/JSON; sender monotonic time on same machine; ordered single stream | ASSUMPTION; no network clock synchronization or remote deployment |
| Presence | Explicit simulated boolean/timeline, default absent | ASSUMPTION stub; real thresholds, debounce and wiring TBD—Lead |
| Sync | Injected ok/stale/unknown; non-ok blocks effective chase | ASSUMPTION for digital replay; physical fusion tolerance TBD—Lead |
| Timing | Film encoded at 12 frames/s; acknowledged offline UDP replay | Media construction choices, NOT processing rate or latency evidence |
| Source clip | Translated public-domain NASA still; no actual person movement | Synthetic fixture, not recorded gym/webcam validation |
'''
docs={}
docs['EXECUTIVE_REVIEW']=f'''# Head tracking → N3 carrier yaw

Implemented a local OpenCV face-prior pipeline, gated UDP/JSON adapter and Blender receiver. A **synthetic translated-still clip** goes through actual decoded-image detection and actual loopback UDP into `bpy`. The 12-second film and eight stills pair the detected head rectangle with the virtual carrier. This is a digital integration demonstration; no webcam capture was performed.

{freeze}

**Verified:** 144 detector packets applied; all 32 presence/head/inhibit/E-stop/presence-fault combinations; malformed, reordered and stale input; timeout-to-home; sticky inhibit across sender rebind and receiver reconstruction; manual reset followed by separate arm. Five inherited scenes match the accepted parent by object geometry/transform/animation/material signatures; eleven ancestor hashes, including N1, match. Bag/fill/mast and camera matrix deviations are zero in the 144 saved frames.

**Disposition requested:** Ola qualitative review of direction and idle behavior, plus mapping/idle/normalization proposal. Current status is ready for review, not independent acceptance. Lead values remain null in the default config. See [README](README.html), [model audit](model_verification.json), [integration](integration_verification.json), [unit checks](unit_verification.json) and [source snapshots](source_documents.json).

{scope}

{assumptions}

{glossary}'''
docs['README']=r'''# Run the head → carrier yaw bridge

This folder is self-contained for live receiver/clip use with its saved successor. Run commands below from this folder. **Digital twin only.** Python must provide `opencv-python`; Blender uses the standard-library core and its own `bpy`. Tested environment is recorded in TOOLCHAIN_REPRO, not a promised future compatibility range.

## Watch or inspect

Open [review index](INDEX.html) or [film](media/head_yaw_review.mp4). Open `Punching_Bag_N3_Head_Track_Yaw.blend` in Blender 3.6.5 and select `N3_HEAD_TRACK_YAW_BRIDGE`. The saved animation replays received yaw; it does not run a detector on opening. Automatic Python execution is unnecessary.

## Start the interactive receiver

In Blender's Python console, set `bridge_dir` to this folder's absolute path:

```python
import sys
from pathlib import Path
bridge_dir = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-21\n3-head-track-yaw-bridge")
sys.path.insert(0, str(bridge_dir))
import blender_receiver as bridge
bridge.start(bridge_dir / "demo_config.json")
```

This explicitly selects **ASSUMPTION demo values**. `bridge.start()` without a path uses `config_template.json`, whose null mapping/watchdog values deny chase. Startup clears only the isolated carrier's baked yaw animation in memory so live values can own it. Reopen the saved file to restore replay. Keep timeline playback stopped during live use. No file is saved by the receiver.

## Send the supplied clip

From PowerShell in this folder:

```powershell
python capture_head.py --clip media/input_synthetic.avi --timeline presence_timeline.json --config demo_config.json --head-spotcheck-approved --send --preview
```

Timeline presence, sync and fault signals are simulated. The last two chapters latch inhibit/E-stop. Normal EOF sends absent/invalid home; crashes/lost packets fall back to the receiver watchdog. These are digital behaviors only.

## USB camera option (implemented; not exercised in this pass)

```powershell
python capture_head.py --camera 0 --sim-present --head-spotcheck-approved --config demo_config.json --send --preview
```

`--sim-present` explicitly simulates the presence sensor. Without it or a timeline, presence defaults absent. Only use `--head-spotcheck-approved` after qualitatively checking the actual scene. This simple fallback invalidates zero or multiple detections, but is not robust identity tracking. No camera media is recorded. Optional `--log episode.jsonl` writes local detections/gates, not video. Press q in preview or Ctrl+C in the sender to exit.

## Reset, arm, rebind and stop

The **local operator**, not the sender/AI, controls reset. After clearing the simulated source fault and receiving a fresh packet with both stop inputs false:

```python
bridge.STATE.manual_reset()  # stays home; does not start chase
bridge.STATE.arm()           # stays home until the next fresh packet
```

`bridge.STATE.rebind()` allows a new sender stream but preserves the latch. Rebinding is needed when restarting the sender; old stream/sequence packets are rejected. `bridge.stop()` closes the socket and homes the twin. `bridge.start(...)` preserves an existing latch. Local `receiver_latch_state.tmp` persists the digital latch and arm state across receiver reconstruction/restart; malformed state is treated as latched. It is excluded from Git and is **not safety-rated storage**. Deleting it is not the reset procedure. Restarting the computer, receiver or sender does not provide physical E-stop guarantees.

Only loopback traffic is supported. There is no valve, motor, serial, fieldbus, network-device or physical actuator output. Port 18766 is an ASSUMPTION local demo port; stop another receiver before running offline integration. Do not run interactive receive and `build_bridge.py` simultaneously.

## Signal behavior

`session_enable = user_present AND head_hypothesis_valid AND NOT inhibit_latched`.
`yaw_cmd_enable` additionally requires NOT `e_stop_asserted`.
`effective_enable` additionally requires configured mapping, good sync, fresh ordered input, receiver latch clear and manual arm. Presence-sensor fault forces absent. The receiver recomputes the map and gates; sender-provided yaw/enable fields are not trusted. All rejected/expired inputs select home-zero. A stop/inhibit stays latched until the local manual reset sequence.

The one-face rule and default Haar parameters are assumptions, not a detector validity standard. No temporal head tracker, identity association, camera calibration, proximity measurement or real-gym validation is included.

See [reproduce](TOOLCHAIN_REPRO.html) for the tested build commands and [assumptions](EXECUTIVE_REVIEW.html).
'''
docs['PUNCH_PATH_CHECKLIST']='''# A — Punch path and palm conventions

No new punch is commanded. The added scene freezes the accepted mid-height guard soft-arm pose and turns only the carrier. Cross palm-down, hook palm-inward, and uppercut palm-up remain the accepted inherited atlas conventions. U/F/T chamber-group teaching intent remains qualitative.

| Item | Result | Evidence / defect |
|---|---|---|
| Saved inherited strike scenes | PASS, unchanged geometry and animation signatures | model_verification.json; parent accepted atlas |
| New head-left → left yaw; head-right → right yaw | PASS on synthetic clip, review pending | frames 30 / 68; udp_received.json |
| Absent/invalid/fault/sync/inhibit/E-stop → idle | PASS digital samples / tests | film, unit_verification.json |
| Wrist–glove alignment | PASS sampled new scene | A-05; ENVELOPE_GEOMETRY_AUDIT |
| Strike propulsion / impact | OPEN | C-01; Track A does not prove strike impulse |

RH-02 inherited policy remains: 50% NON-HEAD; 70% limited head surface inclusion, including previously documented tall centroid shortfall. No head-tracking result upgrades those reach claims.
'''
docs['DEFECT_REGISTER']='''# B — Defect register

| ID | Severity | Observation / interpretation | Fix or disposition | Files |
|---|---|---|---|---|
| HY-01 | Integration | Camera-head cue had no running N3 carrier adapter | Local detector/UDP/receiver implemented; synthetic digital PASS; Ola review pending | capture_head.py; blender_receiver.py |
| HY-02 | High residual | Only synthetic translated still exercised; no real-gym sensing evidence | OPEN; protected camera plus real presence bench and qualitative scene checks needed | fixture_provenance.json |
| HY-03 | High residual | Gain, sign/calibration, clamp, idle and timeouts not frozen | OPEN Lead; null template plus explicitly labeled demo config | config_template.json; demo_config.json |
| HY-04 | Digital fault behavior | Missing/invalid/old packets or sticky inhibit could leave chase enabled | Tested home-zero, ordered freshness, latch, manual reset/arm; software scope only | unit_verification.json; model_verification.json |
| A-05 | High baseline | Wrist–glove junction drift | New scene sampled alignment PASS; inherited scenes unchanged | model_verification.json |
| A-03 | High baseline | Distinct U/F/T intent | Accepted airflow scenes unchanged; no new pressure claims | lineage.json |
| G-03 / G-05 | High baseline | Arm/bag and axial envelope proxies | Sampled digital gaps positive; physical loaded gaps OPEN | model_verification.json |
| B-06 / C-01 | Critical | Root structure / pneumatic propulsion-contact evidence missing | OPEN; no physical closure | EXECUTIVE_REVIEW.md |
| SAF-02 / P-05 | Critical residual | Physical stop and limp behavior unqualified | OPEN; GUI home-zero is not a hardware stop or vent policy | INTERFACE_VULNERABILITIES.md |
'''
docs['POSE_ATLAS']='# C — Head/yaw evidence atlas\n\nEvery image: **prescribed motion — not measured force**. Input is a synthetic translated NASA still; the face rectangle is detected from decoded pixels. Presence/fault flags are simulated.\n\n'
for frame,name in m['stills'].items():
    docs['POSE_ATLAS']+=f'## {name.replace("_"," ").title()} — frame {frame}\n\n![{name}](media/{name}.png)\n\n'
docs['CONTINUUM_PNEUMATIC_INTENT']=f'''# D — Continuum pneumatic intent

{freeze}

The added scene holds all soft-arm shapes, protected-root pitch and glove orientation relative to the carrier. It drives no fill/vent values. U1–U3 upper bending, F1–F3 forearm shaping and T1–T2 soft wrist torsion retain the accepted isolated-branch, uncalibrated visual intent in the inherited AF scenes. Elastic textile return after vent is architectural intent, not a tested recoil result.

{scope}
'''
docs['DOF_MECHANISM']='''# E — Degrees of freedom

Scene: `N3_HEAD_TRACK_YAW_BRIDGE`. Exact isolated target: `HEAD_YAW_CARRIER`, carrying `head_yaw_target = true` and N1 source identity `M1__AZ-H2__bearing_supported_arm_carrier`.

Local +Z Euler rotation supplies yaw around the mast. Home points toward world -Y; positive yaw turns toward world +X (right in the fixed front review view). ASSUMPTION: non-mirrored image right maps to this world direction; real camera alignment/sign is TBD—Lead. The live receiver owns only this target, not the bag/fill/mast or inherited scenes.

The arm geometry remains fixed in carrier coordinates. Camera is fixed. The white bag/floor datum stays still and the purple arrow turns with the carrier. Root pitch and pneumatic shape are held. The new animation uses constant key interpolation of received packets; it does not imply smooth or dynamically achievable physical motion. Reopened-model frame audit confirms the fixed and moving channels.
'''
docs['ENVELOPE_GEOMETRY_AUDIT']=f'''# F — Saved-model geometry audit

Independent audit opens the saved successor; it does not import the builder or save edits. All 144 received-packet frames are checked. Constant yaw keys hold between samples; no intervening interpolated stroke is claimed.

| Digital quantity | Result |
|---|---|
| Bag/fill/mast matrix maximum deviation | {a['fixed_bag_fill_mast_max_matrix_deviation']} |
| Camera matrix maximum deviation | {a['fixed_camera_max_matrix_deviation']} |
| Replay yaw maximum numerical error | {a['yaw_replay_max_error_deg']:.9f} degrees |
| Arm geometry maximum drift in carrier coordinates | {a['arm_local_geometry_max_deviation_m']:.10f} m |
| A-05 wrist/glove maximum drift | {a['A05_max_mm']:.6f} mm |
| G-03 sampled 71-mm radial arm-envelope proxy minimum | {a['G03_sampled_proxy_min_mm']:.6f} mm |
| G-05 cover/carrier axial gap minimum | {a['G05_axial_min_mm']:.6f} mm |
| Chamber object count | 16, eight per arm |
| Inherited scene signatures / ancestor hashes | 5 unchanged / 11 preserved |

See [raw model verification](model_verification.json). G-03 uses the inherited centerline/radial proxy against the axisymmetric bag, not mesh collision or loaded deflection. New conceptual root covers, hoses, pinch, cover compliance and real clearances remain unqualified. Previous accepted atlas geometry/animation is preserved by exact signatures; this pass does not claim a new physical verification or rerun its entire physical test plan.

{scope}
'''
docs['INTERFACE_VULNERABILITIES']='''# G — Interface vulnerabilities / DFMEA inputs

Design failure mode and effects analysis (DFMEA) inputs only; no invented risk-priority numbers.

| Interface | Failure mode / effect | Digital mitigation / remaining work |
|---|---|---|
| Haar head prior | False face, occlusion, multiple people, image flip → wrong cue | Qualitative spot-check opt-in; multiple/zero candidates invalid; real camera dataset and calibration OPEN |
| Presence input | Sim flag mistaken for proximity proof | Source labeled SIMULATED_BOOL_NOT_HARDWARE; default absent; actual fail-safe wiring OPEN |
| UDP → HEAD_YAW_CARRIER | Lost, delayed, duplicate, malformed or reordered input | Same-machine monotonic freshness, sequence/stream validation, local watchdog; loopback only; no authenticated hardware protocol |
| Local inhibit | Reconnect clears stop or reset starts motion | Sticky runtime file; corrupt state latches; local reset plus separate arm; physical stop independence OPEN |
| UI / Blender process | Hang prevents home update | No hardware outputs; Blender timer is not an independent E-stop; SAF-02 OPEN |
| Home-zero return | Sudden virtual pose jump mistaken for physical stop profile | Digital-only idle assumption; physical deceleration/limp policy P-05 remains OPEN |
| Carrier/root/bearing/anchor | Unqualified load path / pinch / unlock | B-06 F-01/F-05/F-08 remain OPEN; no physical movement |
| Distal textile / hose routing | Fatigue, leakage, retention or abrasion | B-03/RH-03 and Track B coupons remain OPEN |

F-01 pitch lock is not required for this digital yaw demo; F-01/F-05 and full S3 readiness remain required before pressurized strike. No signal here is wired to hardware.
'''
docs['CHANGELOG_OPEN_ITEMS']='''# H — Changes and open items

Added a versioned successor with an isolated yaw scene; OpenCV clip/USB entry point; strict local UDP receiver; null production template and illustrative config; synthetic fixture/provenance; episode logs; latch/reset/watchdog tests; A–J review documents; side-by-side film and eight stills. Source engineering documents are copied with hashes for provenance, not rewritten. Accepted pitch/atlas/AF scenes and eleven baseline files are preserved.

Completed digital checks are in unit_verification.json, integration_verification.json, model_verification.json and media_verification.json. Independent Ola acceptance remains pending.

OPEN: actual USB camera and real-person motion validation; protected optics/FOV/mirror calibration; authoritative proximity hardware; detector robustness/latency; gain/clamp/idle/sync freeze; B-06/C-01 Critical physical evidence; SAF-02/P-05 controls qualification; loaded clearance, durability and textile retention. No Soft physics documents, POs, valves or external messages are part of this pass.
'''
docs['TOOLCHAIN_REPRO']='''# I — Toolchain and reproducibility

Observed runtime: Blender 3.6.5, Python 3.11, OpenCV 4.8.1, Pillow 12.3.0; NumPy, Mistune and system FFmpeg/ffprobe. No claim of newest supported versions. The OpenCV bundled `haarcascade_frontalface_default.xml` model is used with default detection parameters (ASSUMPTION prior). Exact observed version strings and model hash are recorded in `runtime.json`.

From this packet folder, after dependencies are present:

```powershell
python make_fixture.py
python test_bridge.py
python run_blender.py build_bridge ../n3-b06-pitch-height-pedagogy/Punching_Bag_N3_Pitch_Height_Pedagogy.blend
python run_blender.py audit_bridge
python run_blender.py render_bridge
python compose_media.py
python build_packet.py
python verify_packet.py
```

`run_blender.py` uses the installed Blender 3.6 path; `build_bridge.py` uses the installed Python311 path for the OpenCV subprocess. Edit those tool paths when moving machines. The builder checks the accepted parent hash and compares five inherited scene signatures before saving a new successor; it never writes the parent. It can regenerate its own candidate output. The saved film is baked from the actual UDP receive log, then rendered offline; per-frame acknowledgements guarantee deterministic test transfer and are not a throughput benchmark.

`render_frames/` and `composed_frames/` are reproducible intermediates excluded from Git. Logs/caches/runtime latch state are local. `packet_manifest.json` includes deliverable hashes. Use Git LFS to fetch actual blends, images and video (`git lfs pull`) after cloning; pointer files are not usable media. Ancestor blend hashes live in `lineage.json`.

The supplied source still is attributed to NASA / Eileen Collins, via scikit-image's public-domain sample. [Source description](https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.astronaut), [source image](https://raw.githubusercontent.com/scikit-image/scikit-image/v0.25.2/skimage/data/astronaut.png), [OpenCV cascade API](https://docs.opencv.org/4.x/d1/de5/classcv_1_1CascadeClassifier.html). The fixture crops/translates that still to exercise the detector; it does not depict an actual boxing session or actual person movement. Source bytes and transformation details are in fixture_provenance.json.
'''
stamp=datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M ET')
ready=f'''## READY_FOR_OLA
status: awaiting_ola
timestamp: {stamp}
pass_id: n3-head-track-yaw-bridge
track: A

### Summary
Delivered an OpenCV head-prior → local UDP/JSON → N3 carrier-yaw bridge, a versioned Blender successor, a 12-second synthetic replay film, eight stills and A–J review documents. All 144 decoded synthetic frames were processed and applied through actual UDP; gate truth cases, malformed/old packets, idle on absent/invalid/fault/sync, sticky inhibit, manual reset/arm and watchdog checks passed. The bag/fill/mast and camera remain fixed; five inherited scenes and eleven ancestor hashes, including N1, are preserved. Default mapping values remain null and explicit demo settings are labeled ASSUMPTION; real camera/proximity performance and Lead mapping/idle freeze remain OPEN. B-06/C-01 remain Critical OPEN, and Track A does not prove strike impulse.

### Paths
- reviews/2026-09-21/n3-head-track-yaw-bridge/INDEX.html
- reviews/2026-09-21/n3-head-track-yaw-bridge/README.md
- reviews/2026-09-21/n3-head-track-yaw-bridge/Punching_Bag_N3_Head_Track_Yaw.blend
- reviews/2026-09-21/n3-head-track-yaw-bridge/media/head_yaw_review.mp4
- reviews/2026-09-21/n3-head-track-yaw-bridge/model_verification.json
- reviews/2026-09-21/n3-head-track-yaw-bridge/packet_verification.json

### Ask Ola
Review directional follow and home-idle behavior in the explicitly synthetic clip; disposition the isolated yaw target and proposed normalization/sign/idle conventions. Confirm the next real-camera plus authoritative presence test scope and freeze mapping/watchdog values before a normative configuration. No physical or sensing-performance closure is requested.

### Acceptance criteria self-check
- [x] Architecture freeze intact (no distal metal / continuum 8-chamber)
- [x] No invented force/pressure/life numbers
- [x] Punch vocabulary / palm frames addressed if Track A (inherited scenes preserved; no new strike)
- [x] Demarcation stated: Track A does not prove strike impulse
- [x] Detected synthetic head movement left/right drives visible carrier yaw
- [x] Absent/invalid and simulated fault cases select digital idle
- [x] Assumptions labeled; packet, film/stills, source lineage and glossary supplied
- [ ] Independent Ola acceptance and real-camera/proximity bench evidence

### Blockers
None to local digital review. Synthetic clip evidence is not webcam/gym validation; Lead parameter freeze and physical evidence remain OPEN. Git delivery result is recorded separately. This marker is a local handoff, not automatic delivery or a watcher.

{glossary}'''
docs['READY_FOR_OLA']=ready
for name,body in docs.items():(R/(name+'.md')).write_text(body,encoding='utf-8')
css='''body{margin:0;background:#101c2a;color:#d9e7f2;font:18px/1.6 system-ui}main{max-width:1200px;margin:auto;padding:36px}a{color:#82e6d0}h1{font-size:42px;line-height:1.15}h2{color:#a9d4ef;margin-top:2em}table{border-collapse:collapse;width:100%;font-size:16px}td,th{padding:12px;border:1px solid #3e5365;text-align:left;vertical-align:top}th{background:#243649}pre{overflow:auto;padding:20px;background:#07111c}code{background:#203144;padding:2px 4px}img,video{max-width:100%;border-radius:8px}nav{font-size:15px;display:flex;gap:24px}.notice{padding:18px;border-left:4px solid #f2c277;background:#243143}.gallery{display:grid;grid-template-columns:1fr 1fr;gap:24px}button{padding:10px;margin:5px;background:#274753;color:white;border:1px solid #628a93;border-radius:5px;cursor:pointer}small{color:#9ab3c9}@media(max-width:700px){main{padding:18px}.gallery{display:block}h1{font-size:32px}}'''
md=mistune.create_markdown(plugins=['table'])
def page(title,body):return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><style>'+css+'</style></head><body><main><nav><a href="INDEX.html">Review index</a><a href="README.html">Run the bridge</a><a href="EXECUTIVE_REVIEW.html">Engineering review</a></nav>'+body+'</main></body></html>'
for name,body in docs.items():(R/(name+'.html')).write_text(page(name.replace('_',' '),md(body)),encoding='utf-8')
buttons=''.join(f'<button onclick="let v=document.getElementById(\'film\');v.currentTime={t};v.play()">{label}</button>' for t,label in [(1,'Left'),(3,'Right'),(6,'Absent'),(7,'Invalid head'),(8,'Presence fault'),(9,'Stale sync'),(10,'Inhibit'),(11,'E-stop')])
gallery=''.join(f'<a href="media/{name}.png"><img loading="lazy" src="media/{name}.png" alt="{name.replace("_"," ")}"></a>' for name in m['stills'].values())
nav='<ul>'+''.join(f'<li><a href="{name}.html">{name.replace("_"," ").title()}</a></li>' for name in docs if name not in ['README','READY_FOR_OLA'])+'</ul>'
evidence='<p>'+''.join(f'<a href="{p}">{label}</a> · ' for p,label in [('Punching_Bag_N3_Head_Track_Yaw.blend','Blender successor'),('episode.jsonl','Detector episode'),('udp_received.json','Received yaw'),('unit_verification.json','Gate tests'),('model_verification.json','Model / receiver audit'),('lineage.json','Baseline lineage'),('fixture_provenance.json','Source credit'),('packet_verification.json','Packet checks'),('packet_manifest.json','Manifest'),('READY_FOR_OLA.html','Ola handoff')])+'</p>'
body='<h1>The head moves.<br>The shoulders follow.</h1><p>OpenCV face detection drives the N3 carrier through local UDP. A fixed camera shows the filled bag staying still while the shoulder carrier turns.</p><p class="notice"><strong>Ready for Ola review — synthetic input, simulated presence.</strong> The clip translates a public-domain NASA still. This proves bounded digital integration; real camera performance and physical actuation remain unproven. Track A does not prove strike impulse.</p><video id="film" controls preload="metadata" poster="media/head_left.png"><source src="media/head_yaw_review.mp4" type="video/mp4"></video>'+buttons+'<p><small>12-second review film. Encoded frame rate is a media property, not a detector performance result. Demo mapping and idle settings remain ASSUMPTION / TBD—Lead.</small></p><h2>Eight review moments</h2><div class="gallery">'+gallery+'</div><h2>Run and reproduce</h2><p><a href="README.html">Clip / USB instructions</a> · <a href="TOOLCHAIN_REPRO.html">Rebuild and verify</a> · <a href="demo_config.json">Explicit demo settings</a> · <a href="config_template.json">Unconfigured template</a></p><h2>Engineering packet A–J</h2>'+nav+'<h2>Evidence</h2>'+evidence
(R/'INDEX.html').write_text(page('N3 head tracking to carrier yaw',body),encoding='utf-8')
print('PACKET_DOCS_READY')
