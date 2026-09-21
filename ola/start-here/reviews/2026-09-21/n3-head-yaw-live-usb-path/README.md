# Run the live-USB-capable head → carrier yaw path

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
