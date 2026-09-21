"""Synthetic translated NASA still -> video; not recorded human movement."""
import hashlib, json, subprocess
from pathlib import Path
import cv2
import numpy as np
R=Path(__file__).resolve().parent
(R/'media').mkdir(exist_ok=True)
image=cv2.imread(str(R/'assets/astronaut.png'))
assert image is not None
# Crop includes head and shoulders. Geometric composition is a detector test fixture.
crop=cv2.resize(image[20:300,120:340],(176,224))
writer=cv2.VideoWriter(str(R/'media/input_synthetic.avi'),cv2.VideoWriter_fourcc(*'MJPG'),12,(640,360))
assert writer.isOpened()
rows=[]
for i in range(144):
    cx = 320 if i<12 else int(320-160*min(1,(i-12)/12)) if i<36 else int(160+320*min(1,(i-36)/24))
    case='center' if i<12 else 'left' if i<36 else 'right' if i<72 else 'absent_with_face' if i<84 else 'invalid_head_present' if i<96 else 'presence_fault' if i<108 else 'stale_sync' if i<120 else 'inhibit' if i<132 else 'e_stop'
    frame=np.full((360,640,3),(32,26,20),dtype=np.uint8)
    if case!='invalid_head_present':frame[68:292,cx-88:cx+88]=crop
    writer.write(frame)
    rows.append(dict(frame=i+1,case=case,user_present=case!='absent_with_face',presence_sensor_fault=case=='presence_fault',sync_quality='stale' if case=='stale_sync' else 'ok',inhibit_latched=case=='inhibit',e_stop_asserted=case=='e_stop'))
writer.release()
(R/'presence_timeline.json').write_text(json.dumps(rows,indent=2))
(R/'fixture_provenance.json').write_text(json.dumps(dict(source_url='https://raw.githubusercontent.com/scikit-image/scikit-image/v0.25.2/skimage/data/astronaut.png',source_documentation='https://scikit-image.org/docs/stable/api/skimage.data.html#skimage.data.astronaut',credit='NASA / Eileen Collins; public-domain sample distributed by scikit-image',sha256=hashlib.sha256((R/'assets/astronaut.png').read_bytes()).hexdigest(),transformation='Crop, resize and translate still on blank field; no actual human movement. Haar detector runs on decoded video, not prescribed boxes.',frames=144,encoded_fps=12,scope='Synthetic digital integration test, NOT sensing accuracy/FPS/latency evidence. Presence/fault/sync are injected.'),indent=2))
print('FIXTURE_READY')
