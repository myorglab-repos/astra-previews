"""Build the bounded A-J review packet from measured digital test outputs."""
from pathlib import Path
import datetime,html,json
import mistune
R=Path(__file__).resolve().parent
read=lambda p:json.loads((R/p).read_text(encoding='utf-8-sig'))
a=read('model_verification.json');m=read('media_verification.json')
u=read('unit_verification.json');i=read('integration_verification.json')
usb=read('usb_path_verification.json');cam=read('camera_probe.json');gym=read('gym_spotcheck.json')
scope='**Track A does not prove strike impulse.** B-06 root hardware and C-01 pressure-to-motion-to-impact measurements remain Critical OPEN. No physical actuation, measured sensing accuracy, detector FPS, latency, durability or safety qualification is claimed. DIGITAL_TWIN_ONLY.'
freeze='Eight soft continuum chambers per arm: U1–U3, F1–F3, T1–T2; textile strain limiting, vent plus elastic return and no exposed distal metal. Bag/fill/mast stay fixed; only the shoulder carrier yaws. Protected-root cover remains an illustrative envelope.'
glossary='''## Plain-language glossary

| Term | Everyday meaning | Why it matters in this pass |
|---|---|---|
| live USB path | Code that can open a real webcam when one is plugged in. | This pass hardens `--camera N` so a missing device fails clearly instead of hanging. |
| SKIPPED_NO_CAMERA | Gym check not run because no camera — not a software failure. | CI / packet proof uses the clip fixture and still PASSes. |
| SKIPPED_NO_OPERATOR_APPROVAL | Camera opened, but no person attested a one-face gym prior. | Device-present is not gym L/R evidence; no invented stills/film. |
| ROI / bbox / centroid | Image region / rectangle around a detected face / its center. | Horizontal center supplies the yaw cue; no identity is inferred. |
| Head hypothesis | A tentative face detection. | One-face plus operator spot-check is a demo prior, not qualified sensing. |
| Carrier yaw | Shoulders turning around the mast. | The filled bag must remain stationary. |
| UDP / replay | Local message transport / playing saved inputs again. | Actual detector packets drive the receiver; the film is inherited ACCEPTED-A evidence. |
| Presence stub | An injected yes/no signal (`--sim-present` or timeline). | This pass has no ToF/PIR/mat hardware. |
| Inhibit latch / watchdog | A stop that stays set / a check for missing fresh data. | Chase stops on a fault; manual reset and arm are separate local actions. |
| ASSUMPTION / TBD—Lead | A working demo choice / a decision still owned by Ola. | Demo angles and timeouts are not hardware limits or performance targets. |
| HY-02 | Open item: real camera chase not yet product-closed. | Software path + optional gym qualitative only; not done product. |
| A-05 / A-03 | Wrist alignment / chamber-group teaching cues. | Alignment is audited; accepted U/F/T cues stay preserved. |
| G-03 / G-05 | Arm-to-bag proxy gap / carrier-to-cover axial gap. | Sampled digital geometry does not qualify loaded clearances. |
| B-06 / C-01 | Unqualified root hardware / missing propulsion and impact measurements. | Both remain Critical OPEN regardless of this USB path. |
| Track A / Track D | Digital visualization / perception-action engineering. | This packet proves clip CI + USB fail-fast, not real-world CV performance. |

What changed / what is still not proven: the same shoulder-follow demo can open a USB camera without hanging, and still proves itself from a file clip when no camera is present. Real-gym chase, physical stops, root structure and punch power remain unproven.
'''
assumptions='''## Assumptions and Lead decisions

| Item | Implementation proposal / demo value | Status |
|---|---|---|
| Detector | OpenCV bundled frontal-face Haar; default detector parameters; exactly one candidate | ASSUMPTION; face is a head prior, no confidence/accuracy bar |
| Qualitative validity | Candidate accepted only with explicit `--head-spotcheck-approved` | ASSUMPTION; fixture visually checked; live scene needs its own operator check |
| Normalization / units / sign | Frame fraction [0,1]; degrees; signed offset = 2x−1; positive yaw turns -Y home toward +X | ASSUMPTION; camera mirroring/mount calibration TBD—Lead |
| Gain / clamp | Production template null; opt-in demo 30 degrees per signed unit, ±30-degree clamp | ASSUMPTION demo only, not an approved motion range; normative mapping TBD—Lead |
| Idle | Immediate digital home-zero; no tween or hold-last | ASSUMPTION; physical return policy TBD—Lead |
| Watchdog / poll | Demo 2-second freshness window; 0.02-second requested UI poll | ASSUMPTION software settings, not achieved latency/FPS or safety bars; Lead TBD |
| Transport | Loopback-only UDP/JSON `head-yaw-v1`; sender monotonic time on same machine; ordered single stream | ASSUMPTION; no second schema; no network clock synchronization |
| Presence | Explicit `--sim-present` or timeline; default absent | ASSUMPTION stub; real thresholds, debounce and wiring TBD—Lead |
| Sync | Injected ok/stale/unknown; non-ok blocks effective chase | ASSUMPTION for digital replay; physical fusion tolerance TBD—Lead |
| Timing | Inherited film encoded at 12 frames/s; acknowledged offline UDP replay | Media construction choices, NOT processing rate or latency evidence |
| Source clip | Translated public-domain NASA still; no actual person movement | Synthetic fixture, not recorded gym/webcam validation |
| USB open | DirectShow on Windows + hard timeout (default 5 s); clear CAMERA_OPEN_FAILED | Fail-fast software behavior; not a camera quality bar |
'''
docs={}
docs['EXECUTIVE_REVIEW']=f'''# Live-USB-capable head → N3 carrier yaw

This pass extends the **ACCEPTED-A** digital Track A bridge (`n3-head-track-yaw-bridge`, 2026-09-21) with a **live-USB-capable** sender path. Protocol `head-yaw-v1` is unchanged. `bridge_core.py` and `blender_receiver.py` are reused without a second schema. The Blender successor and 12-second synthetic film are **inherited, not remade**. Normative interface language is Elias `ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md` as integrated by Ola (`OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md`): `SKIPPED_NO_CAMERA` is not a software FAIL; `presence_source = SIMULATED_BOOL_NOT_HARDWARE` until hardware; Haar + one-face + `--head-spotcheck-approved`; digital idle `home_zero` + clean-exit stop packet; HY-02 gym qualitative stays OPEN even if the software path PASSes.

`--camera N` now fails fast with `CAMERA_OPEN_FAILED` when the index cannot open (no hang). `--clip` remains the CI / packet path. `--head-spotcheck-approved` and `--sim-present` are documented operator flags. The receiver still **re-derives** enable/yaw and never trusts sender-computed fields.

**Verified this pass (cite JSON only):** unit {u['gate_combinations']}/{u['gate_combinations']} gate combinations, {u['failures']} failures (`unit_verification.json` {u['status']}); clip integration {i['packets_applied']} actual UDP packets, receiver_rederived={i['receiver_rederived']} (`integration_verification.json` {i['status']}); USB fail-fast {usb['test_methods']} methods, {usb['failures']} failures (`usb_path_verification.json` {usb['status']}); camera probe **{cam['status']}**; gym qualitative **{gym['status']}**. Inherited model audit: bag/camera matrix deviation 0.0; yaw replay max error ~{a['yaw_replay_max_error_deg']:.1e}°; 5 inherited scenes / 11 ancestor hashes.

**Disposition requested:** Accept the software USB path + clip CI as a delta on ACCEPTED-A. HY-02 remains OPEN (not product-closed). Do not freeze demo gain/clamp/sign. B-06 / C-01 / SAF-02 remain Critical OPEN.

{freeze}

{scope}

{assumptions}

{glossary}'''
docs['README']=r'''# Run the live-USB-capable head → carrier yaw path

This folder reuses the accepted `head-yaw-v1` bridge. **Digital twin only.** Python must provide `opencv-python`; Blender uses the standard-library core and its own `bpy`. Tested environment is recorded in TOOLCHAIN_REPRO.

## Operator flags

| Flag | Meaning |
|---|---|
| `--clip PATH` | CI / fixture path. Use when no USB camera is present. |
| `--camera N` | Live USB index. **Fails fast** (`CAMERA_OPEN_FAILED`) if the index cannot open; does not hang. |
| `--camera-open-timeout-s SEC` | USB open + first-grab timeout (default 5). |
| `--head-spotcheck-approved` | Operator attests a qualitative one-face prior. Without it, head is invalid and chase idles. |
| `--sim-present` | ASSUMPTION: simulated presence. **Not** a hardware sensor. Default is absent. |
| `--timeline FILE` | Simulated presence / fault / sync rows (clip chapters). |
| `--send` / `--wait-ack` | Loopback UDP; `--wait-ack` is clip integration only. |
| `--log FILE` | Opt-in JSONL. No webcam media is recorded. |
| `--preview` | Local overlay window; `q` exits. |
| `--max-frames N` | Stop after N frames (gym / probe helper). |

## Watch or inspect

Open [review index](INDEX.html) or the inherited [film](media/head_yaw_review.mp4). Open `Punching_Bag_N3_Head_Track_Yaw.blend` in Blender 3.6.5 and select `N3_HEAD_TRACK_YAW_BRIDGE`. The saved animation is the ACCEPTED-A replay; it does not run a detector on opening.

## Start the interactive receiver

In Blender's Python console, set `bridge_dir` to this folder's absolute path:

```python
import sys
from pathlib import Path
bridge_dir = Path(r"C:\Users\mfawe\OneDrive\Documents\GitHub\robotic-punching-bag\reviews\2026-09-21\n3-head-yaw-live-usb-path")
sys.path.insert(0, str(bridge_dir))
import blender_receiver as bridge
bridge.start(bridge_dir / "demo_config.json")
```

This explicitly selects **ASSUMPTION demo values**. `bridge.start()` without a path uses `config_template.json`, whose null mapping/watchdog values deny chase. The receiver recomputes enable/yaw; sender fields are not trusted.

## Send the supplied clip (CI / packet path)

```powershell
python capture_head.py --clip media/input_synthetic.avi --timeline presence_timeline.json --config demo_config.json --head-spotcheck-approved --send --preview
```

## USB camera (fail-fast)

```powershell
python capture_head.py --camera 0 --sim-present --head-spotcheck-approved --config demo_config.json --send --preview
```

If index 0 cannot open, the process exits with `CAMERA_OPEN_FAILED` and a timeout (default 5 s). That is **not** a clip-path failure. Packet gym branch becomes `SKIPPED_NO_CAMERA`.

`--sim-present` explicitly simulates the presence sensor. Without it or a timeline, presence defaults absent. Only use `--head-spotcheck-approved` after qualitatively checking the actual scene. No camera media is recorded.

## Reset, arm, rebind and stop

The **local operator**, not the sender/AI, controls reset. After clearing the simulated source fault and receiving a fresh packet with both stop inputs false:

```python
bridge.STATE.manual_reset()  # stays home; does not start chase
bridge.STATE.arm()           # stays home until the next fresh packet
```

Only loopback traffic is supported. Port 18766 is an ASSUMPTION local demo port.

## Signal behavior

`session_enable = user_present AND head_hypothesis_valid AND NOT inhibit_latched`.
`yaw_cmd_enable` additionally requires NOT `e_stop_asserted`.
`effective_enable` additionally requires configured mapping, good sync, fresh ordered input, receiver latch clear and manual arm. Presence-sensor fault forces absent. The receiver recomputes the map and gates; sender-provided yaw/enable fields are not trusted. Idle policy is **home_zero**.

See [reproduce](TOOLCHAIN_REPRO.html) and [assumptions](EXECUTIVE_REVIEW.html).
'''
docs['PUNCH_PATH_CHECKLIST']='''# A — Punch path and palm conventions

No new punch is commanded. This pass does not remake the ACCEPTED-A yaw scene. Inherited mid-height guard pose and palm conventions stand. U/F/T teaching intent remains qualitative.

| Item | Result | Evidence / defect |
|---|---|---|
| Saved inherited strike scenes | PASS, unchanged (inherited ACCEPTED-A) | model_verification.json; lineage.json |
| Clip L/R → yaw (software path re-run) | PASS on synthetic clip | udp_received.json frames 30 / 68 |
| Absent/invalid/fault/sync/inhibit/E-stop → idle | PASS digital samples / tests | unit_verification.json; integration idle chapters |
| USB fail-fast / clip CI | PASS | usb_path_verification.json; camera_probe.json |
| Gym qualitative L/R | See gym_spotcheck.json (SKIPPED is not FAIL) | gym_spotcheck.json |
| Wrist–glove alignment | PASS sampled inherited scene | A-05; ENVELOPE_GEOMETRY_AUDIT |
| Strike propulsion / impact | OPEN | C-01; Track A does not prove strike impulse |

RH-02 inherited policy remains. No head-tracking result upgrades those reach claims.
'''
docs['DEFECT_REGISTER']='''# B — Defect register

| ID | Severity | Observation / interpretation | Fix or disposition | Files |
|---|---|---|---|---|
| HY-01 | Integration | Camera-head cue had no running N3 carrier adapter | CLOSED-A on parent digital pass; protocol reused here | capture_head.py; blender_receiver.py |
| HY-02 | High residual | Real-gym chase not product-closed | **OPEN residual (Lead 2026-09-21).** Software path may PASS; gym qualitative stays OPEN. SKIPPED_NO_CAMERA / SKIPPED_NO_OPERATOR_APPROVAL are not FAIL. | camera_probe.json; gym_spotcheck.json; usb_path_verification.json |
| HY-03 | High residual | Gain, sign/calibration, clamp, idle and timeouts not frozen | OPEN Lead; null template plus explicitly labeled demo config | config_template.json; demo_config.json |
| HY-04 | Digital fault behavior | Missing/invalid/old packets or sticky inhibit could leave chase enabled | CLOSED-A (software) on parent; re-exercised by unit + clip integration | unit_verification.json; integration_verification.json |
| A-05 | High baseline | Wrist–glove junction drift | Inherited sampled alignment PASS | model_verification.json |
| A-03 | High baseline | Distinct U/F/T intent | Inherited airflow scenes unchanged | lineage.json |
| G-03 / G-05 | High baseline | Arm/bag and axial envelope proxies | Inherited sampled digital gaps positive; physical loaded gaps OPEN | model_verification.json |
| B-06 / C-01 | Critical | Root structure / pneumatic propulsion-contact evidence missing | **OPEN; not closed by this software pass** | EXECUTIVE_REVIEW.md |
| SAF-02 / P-05 | Critical residual | Physical stop and limp behavior unqualified | **OPEN; GUI home-zero is not a hardware stop or vent policy** | INTERFACE_VULNERABILITIES.md |
'''
docs['POSE_ATLAS']='# C — Head/yaw evidence atlas\n\nInherited ACCEPTED-A stills. Every image: **prescribed motion — not measured force**. Input is a synthetic translated NASA still unless gym_spotcheck.json says GYM_DONE. Presence/fault flags are simulated.\n\n'
for frame,name in m['stills'].items():
    docs['POSE_ATLAS']+=f'## {name.replace("_"," ").title()} — frame {frame}\n\n![{name}](media/{name}.png)\n\n'
docs['POSE_ATLAS']+=f'''## Gym qualitative branch

Status: **{gym['status']}**. Camera probe: **{cam['status']}**.

No invented L/R gym stills. If this branch is SKIPPED_NO_CAMERA or SKIPPED_NO_OPERATOR_APPROVAL, that is not a software FAIL.
'''
docs['CONTINUUM_PNEUMATIC_INTENT']=f'''# D — Continuum pneumatic intent

{freeze}

This USB-path pass does not change soft-arm shapes, protected-root pitch or glove orientation. It drives no fill/vent values.

{scope}
'''
docs['DOF_MECHANISM']='''# E — Degrees of freedom

Scene: `N3_HEAD_TRACK_YAW_BRIDGE` (inherited ACCEPTED-A successor). Exact isolated target: `HEAD_YAW_CARRIER`, carrying `head_yaw_target = true` and N1 source identity `M1__AZ-H2__bearing_supported_arm_carrier`.

Local +Z Euler rotation supplies yaw around the mast. Home points toward world -Y; positive yaw turns toward world +X (right in the fixed front review view). ASSUMPTION: non-mirrored image right maps to this world direction; real camera alignment/sign is TBD—Lead.

The live USB sender uses the same mapping. Idle policy remains **home_zero**. This pass does not remake carrier keys.
'''
docs['ENVELOPE_GEOMETRY_AUDIT']=f'''# F — Saved-model geometry audit

Inherited ACCEPTED-A audit. Independent audit opened the saved successor; this pass did not remake it.

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

See [raw model verification](model_verification.json). This pass does not claim a new physical verification.

{scope}
'''
docs['INTERFACE_VULNERABILITIES']='''# G — Interface vulnerabilities / DFMEA inputs

Design failure mode and effects analysis (DFMEA) inputs only; no invented risk-priority numbers.

| Interface | Failure mode / effect | Digital mitigation / remaining work |
|---|---|---|
| USB camera open | Missing/busy index hangs the sender or is mistaken for a packet FAIL | Hard timeout + `CAMERA_OPEN_FAILED`; gym `SKIPPED_NO_CAMERA` is not FAIL; clip CI remains the proof path |
| Haar head prior | False face, occlusion, multiple people, image flip → wrong cue | Qualitative spot-check opt-in; multiple/zero candidates invalid; real camera dataset and calibration OPEN (HY-02) |
| Presence input | `--sim-present` mistaken for proximity proof | Source labeled SIMULATED_BOOL_NOT_HARDWARE; default absent; actual fail-safe wiring OPEN |
| UDP → HEAD_YAW_CARRIER | Lost, delayed, duplicate, malformed or reordered input | Same-machine monotonic freshness, sequence/stream validation, local watchdog; loopback only; receiver re-derives enable/yaw |
| Local inhibit | Reconnect clears stop or reset starts motion | Sticky runtime file; local reset plus separate arm; physical stop independence OPEN |
| UI / Blender process | Hang prevents home update | No hardware outputs; Blender timer is not an independent E-stop; SAF-02 OPEN |
| Home-zero return | Sudden virtual pose jump mistaken for physical stop profile | Digital-only idle assumption; physical deceleration/limp policy P-05 remains OPEN |
| Carrier/root/bearing/anchor | Unqualified load path / pinch / unlock | B-06 F-01/F-05/F-08 remain OPEN; no physical movement |

F-01 `pitch_lock_engaged` is not required for this digital yaw demo. No signal here is wired to hardware.
'''
docs['CHANGELOG_OPEN_ITEMS']=f'''# H — Changes and open items

**This pass (n3-head-yaw-live-usb-path):** hardened `capture_head.py` USB open (DirectShow + timeout, `CAMERA_OPEN_FAILED`, no hang); documented `--head-spotcheck-approved` / `--sim-present`; clip re-integration over actual UDP with receiver re-derive; USB fail-fast unit tests; camera probe + gym branch JSON (`{cam['status']}` / `{gym['status']}`); A–J docs delta. Did **not** remake the ACCEPTED-A successor blend or synthetic pedagogy film. Did **not** fork `head-yaw-v1`.

Completed digital checks are in unit_verification.json, integration_verification.json, usb_path_verification.json, camera_probe.json and gym_spotcheck.json. Inherited model/media verification remains PASS from the parent packet. Independent Ola acceptance remains pending.

OPEN: HY-02 residual (real-gym chase not product-closed); HY-03 Lead mapping freeze; B-06/C-01 Critical physical evidence; SAF-02/P-05 controls qualification; loaded clearance, durability and textile retention. No Soft physics documents, POs, valves or external messages are part of this pass.
'''
docs['TOOLCHAIN_REPRO']='''# I — Toolchain and reproducibility

Observed runtime is recorded in `runtime.json` after this pass's commands. No claim of newest supported versions. The OpenCV bundled `haarcascade_frontalface_default.xml` model is used with default detection parameters (ASSUMPTION prior).

From this packet folder, after dependencies are present. **Do not remake the successor** unless the inherited blend hash is broken:

```powershell
python make_fixture.py
python test_bridge.py
python test_usb_path.py
python run_clip_integration.py
python probe_usb.py
python build_packet.py
python verify_packet.py
```

`run_blender.py build_bridge` remakes the ACCEPTED-A successor and is **out of scope** for this USB-path delta. Interactive receive still uses `blender_receiver.py` + `demo_config.json`.

`render_frames/` and `composed_frames/` are reproducible intermediates excluded from Git. `packet_manifest.json` includes deliverable hashes. Use Git LFS to fetch actual blends, images and video (`git lfs pull`) after cloning.

The supplied source still is attributed to NASA / Eileen Collins, via scikit-image's public-domain sample. Fixture bytes are in fixture_provenance.json.
'''
stamp=datetime.datetime.now().astimezone().strftime('%Y-%m-%d %H:%M ET')
ready=f'''## READY_FOR_OLA
status: awaiting_ola
timestamp: {stamp}
pass_id: n3-head-yaw-live-usb-path
track: A

### Summary
Delivered a live-USB-capable head→yaw path on the accepted `head-yaw-v1` bridge without a second schema. `--camera N` fails fast (`CAMERA_OPEN_FAILED`) instead of hanging; `--clip` remains the CI proof. Unit {u['gate_combinations']}/{u['gate_combinations']} gates ({u['failures']} failures); clip integration {i['packets_applied']} actual UDP packets with receiver re-derive; USB fail-fast {usb['status']} ({usb['test_methods']} methods). Camera probe **{cam['status']}**; gym qualitative **{gym['status']}**. SKIPPED_NO_CAMERA or SKIPPED_NO_OPERATOR_APPROVAL is not a software FAIL; no invented gym L/R media. Demo mapping/sign/gain/clamp/watchdog stay ASSUMPTION. HY-02 residual remains OPEN. B-06 / C-01 / SAF-02 remain Critical OPEN. Track A does not prove strike impulse. DIGITAL_TWIN_ONLY. $0 / no PO.

### Paths
- reviews/2026-09-21/n3-head-yaw-live-usb-path/INDEX.html
- reviews/2026-09-21/n3-head-yaw-live-usb-path/README.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/SOURCE_BRIEF.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/DEFECT_REGISTER.md
- reviews/2026-09-21/n3-head-yaw-live-usb-path/camera_probe.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/gym_spotcheck.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/usb_path_verification.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/integration_verification.json
- reviews/2026-09-21/n3-head-yaw-live-usb-path/packet_verification.json
- reviews/2026-09-21/n3-head-track-yaw-bridge/ENGINEERING_ASSESSMENT_N3_HEAD_TRACK_YAW_BRIDGE_2026-09-21.md
- docs/engineering/ELIAS_LIVE_USB_CAMERA_TWIN_ICD_INTERFACES.md
- docs/engineering/OLA_INTEGRATE_ELIAS_PRESENCE_LIVE_USB_2026-09-21.md

### Ask Ola
Disposition the USB fail-fast + clip CI delta on ACCEPTED-A. Confirm HY-02 stays OPEN (software path only). Do not freeze demo gain/clamp/sign from this pass. No physical or sensing-performance closure is requested.

### Acceptance criteria self-check
- [x] Architecture freeze intact (no distal metal / continuum 8-chamber)
- [x] No invented force/pressure/life numbers
- [x] Punch vocabulary / palm frames addressed if Track A (inherited scenes preserved; no new strike)
- [x] Demarcation stated: Track A does not prove strike impulse
- [x] `--camera N` fail-fast documented and tested; live USB path packaged
- [x] Clip path unit + integration PASS with real JSON counts
- [x] Gym branch recorded as {gym['status']} (SKIPPED_NO_CAMERA is not FAIL)
- [x] Assumptions labeled; packet, SOURCE_BRIEF, DEFECT_REGISTER, glossary supplied
- [ ] Independent Ola acceptance; HY-02 / HY-03 / B-06 / C-01 / SAF-02 remain OPEN

### Blockers
None to local digital review. Gym qualitative is {gym['status']}. Lead parameter freeze and Critical hardware remain OPEN. Git delivery result is recorded separately. This marker is a local handoff, not automatic delivery or a watcher.

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
evidence='<p>'+''.join(f'<a href="{p}">{label}</a> · ' for p,label in [('Punching_Bag_N3_Head_Track_Yaw.blend','Inherited Blender successor'),('episode.jsonl','Detector episode'),('udp_received.json','Received yaw'),('unit_verification.json','Gate tests'),('usb_path_verification.json','USB fail-fast'),('camera_probe.json','Camera probe'),('gym_spotcheck.json','Gym branch'),('model_verification.json','Model / receiver audit'),('lineage.json','Baseline lineage'),('SOURCE_BRIEF.md','Source brief'),('packet_verification.json','Packet checks'),('READY_FOR_OLA.html','Ola handoff')])+'</p>'
body='<h1>The USB path is live-capable.<br>The clip still proves it.</h1><p>Same head-yaw-v1 bridge. Hardened camera open. Clip CI when no webcam. Receiver re-derives enable and yaw.</p><p class="notice"><strong>Ready for Ola review — live USB path + clip fixture.</strong> Camera probe: <strong>'+cam['status']+'</strong>. Gym qualitative: <strong>'+gym['status']+'</strong>. SKIPPED_NO_CAMERA is not a software FAIL. Inherited synthetic film is ACCEPTED-A evidence, not a remake. Track A does not prove strike impulse. Demo mapping remains ASSUMPTION.</p><video id="film" controls preload="metadata" poster="media/head_left.png"><source src="media/head_yaw_review.mp4" type="video/mp4"></video>'+buttons+'<p><small>Inherited 12-second review film. Encoded frame rate is a media property, not a detector performance result. Demo mapping and idle settings remain ASSUMPTION / TBD—Lead.</small></p><h2>Eight inherited review moments</h2><div class="gallery">'+gallery+'</div><h2>Run and reproduce</h2><p><a href="README.html">Clip / USB instructions</a> · <a href="TOOLCHAIN_REPRO.html">Rebuild and verify</a> · <a href="demo_config.json">Explicit demo settings</a> · <a href="config_template.json">Unconfigured template</a></p><h2>Engineering packet A–J</h2>'+nav+'<h2>Evidence</h2>'+evidence
(R/'INDEX.html').write_text(page('N3 live-USB head tracking to carrier yaw',body),encoding='utf-8')
print('PACKET_DOCS_READY')
