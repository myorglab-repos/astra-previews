# Run the head → carrier yaw bridge

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
