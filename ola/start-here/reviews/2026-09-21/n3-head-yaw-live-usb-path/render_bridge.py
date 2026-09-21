import bpy
from pathlib import Path
R=Path(__file__).resolve().parent
s=bpy.data.scenes['N3_HEAD_TRACK_YAW_BRIDGE'];bpy.context.window.scene=s
out=R/'render_frames';out.mkdir(exist_ok=True)
s.render.image_settings.file_format='PNG'
for f in range(1,145):
    s.frame_set(f);s.render.filepath=str(out/f'{f:04d}.png');bpy.ops.render.render(write_still=True)
print('RENDER_COMPLETE',flush=True)
