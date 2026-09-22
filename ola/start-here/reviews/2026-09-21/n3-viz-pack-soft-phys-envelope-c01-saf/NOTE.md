# Note

Workbench teaching renders on Blender 3.6.5. HUD and the SAF-02 schematic were composed in Python (Pillow) and encoded with ffmpeg, libx264, yuv420p, authored 12 fps.

`render_soft_phys_cues.py` and `render_yaw_slim.py` open `Punching_Bag_N3_Head_Track_Yaw.blend` and do not save it. Cue shape values are applied in memory for the film. Yaw frames are a re-render of the slimmed scene `N3_HEAD_TRACK_YAW_BRIDGE`.

`render_schematics.py` builds a fresh illustration file in memory for the B-06 keep-out stack and the C-01 coupon board. Block and coupon sizes are drawing aids.

`compose_films.py saf` draws the presence / inhibit / limp schematic. It does not command a valve or a drive.

The previous black-collar yaw mp4 was left in place. Atlas, exposed-blind, and airflow mp4s were missing from origin/main (they lived only on local commit 9032c69). Those embed files were restored so the existing START_HERE players resolve. They were not re-rendered.
