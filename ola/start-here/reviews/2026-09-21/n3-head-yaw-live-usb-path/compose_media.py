"""Compose diagnostic panels from actual detector logs and Blender renders."""
import json,subprocess
from pathlib import Path
import cv2
from PIL import Image,ImageDraw,ImageFont
R=Path(__file__).resolve().parent
rows=json.loads((R/'udp_received.json').read_text());episode=[json.loads(x) for x in (R/'episode.jsonl').read_text().splitlines()]
cap=cv2.VideoCapture(str(R/'media/input_synthetic.avi'))
frames=R/'composed_frames';frames.mkdir(exist_ok=True)
FONT='C:/Windows/Fonts/segoeui.ttf';BOLD='C:/Windows/Fonts/segoeuib.ttf'
def font(n,b=False):return ImageFont.truetype(BOLD if b else FONT,n)
titles={'center':'CENTER / head prior enabled','left':'HEAD MOVES LEFT / carrier follows','right':'HEAD MOVES RIGHT / carrier follows','absent_with_face':'PRESENCE ABSENT / idle despite face','invalid_head_present':'HEAD INVALID / idle despite presence','presence_fault':'PRESENCE FAULT / forced absent + idle','stale_sync':'STALE SYNC / chase blocked','inhibit':'INHIBIT LATCH / idle until manual reset','e_stop':'SIMULATED E-STOP / chase blocked'}
stills={30:'head_left',68:'head_right',78:'absent',90:'invalid_head',102:'presence_fault',114:'stale_sync',126:'inhibit',138:'e_stop'}
for r,p in zip(rows,episode):
    ok,frame=cap.read();assert ok
    out=r['output'];im=Image.new('RGB',(1500,900),'#101c2a');d=ImageDraw.Draw(im)
    d.text((35,20),'HEAD → CARRIER YAW',font=font(36,True),fill='#e9f2fa')
    d.text((36,70),'Synthetic translated-still clip • detected centroids • actual UDP → Blender',font=font(22),fill='#9ab3c9')
    d.text((36,112),titles[r['stimulus']],font=font(28,True),fill='#78e9cc' if out['effective_enable'] else '#ffc775')
    pic=Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB));pd=ImageDraw.Draw(pic)
    box=p['head_hypothesis']['bbox']
    if box:
        x,y,w,h=box;pd.rectangle((x,y,x+w,y+h),outline='#75ffd7',width=3);pd.line((x+w/2,0,x+w/2,359),fill='#75ffd7',width=2)
    im.paste(pic,(35,175));d.rounded_rectangle((35,175,675,535),radius=3,outline='#38566c',width=2)
    twin=Image.open(R/'render_frames'/f"{r['frame']:04d}.png").convert('RGB');im.paste(twin,(700,165))
    d=ImageDraw.Draw(im)
    d.text((36,550),'INPUT: decoded synthetic clip + OpenCV Haar',font=font(22,True),fill='white')
    cx='invalid' if p['head_centroid_x'] is None else f"{p['head_centroid_x']:.3f}"
    d.text((36,590),f"Head centroid x: {cx}  |  image left 0 → right 1",font=font(21),fill='#bfd0df')
    d.text((36,625),f"Simulated presence: {'YES' if out['user_present'] else 'NO'}    Head valid: {'YES' if p['head_hypothesis_valid'] else 'NO'}",font=font(21),fill='#bfd0df')
    d.text((36,660),f"Effective yaw: {out['yaw_cmd']:+.2f}°   |   {'FOLLOW' if out['effective_enable'] else 'HOME / IDLE'}",font=font(25,True),fill='#78e9cc' if out['effective_enable'] else '#ffc775')
    flags=', '.join(out['quality_flags']) or 'qualitative head prior + simulated presence'
    # Keep detailed flags out of the title but visible in the engineering evidence.
    if len(flags)>60:flags=flags[:60]+'…'
    d.text((36,700),flags,font=font(18),fill='#a8bdcf')
    d.text((730,775),'OUTPUT: shoulders turn; bag + mast stay fixed',font=font(21,True),fill='#e8eef5')
    d.text((36,825),'ASSUMPTION: demo mapping only; gain / clamp / idle / timing remain TBD — Lead.',font=font(21),fill='#f4c982')
    d.text((36,860),'Prescribed twin motion — not measured force. No real-gym sensing, hardware stop or strike-impulse proof.',font=font(20),fill='#bacbda')
    im.save(frames/f"{r['frame']:04d}.png")
    if r['frame'] in stills:im.save(R/'media'/(stills[r['frame']]+'.png'))
cap.release()
cmd=['ffmpeg','-y','-framerate','12','-i',str(frames/'%04d.png'),'-c:v','libx264','-crf','20','-pix_fmt','yuv420p','-movflags','+faststart',str(R/'media/head_yaw_review.mp4')]
subprocess.run(cmd,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(R/'media/head_yaw_review.mp4')]))
stream=probe['streams'][0];assert int(stream['nb_read_frames'])==144
subprocess.run(['ffmpeg','-v','error','-i',str(R/'media/head_yaw_review.mp4'),'-f','null','-'],check=True)
review=Image.new('RGB',(1500,1800),'#101c2a')
for index,name in enumerate(['head_left','head_right','absent','invalid_head','presence_fault','stale_sync','inhibit','e_stop']):
    im=Image.open(R/'media'/(name+'.png'));im.thumbnail((750,450));review.paste(im,((index%2)*750,(index//2)*450))
review.save(R/'media/qa_contact_sheet.png')
(R/'media_verification.json').write_text(json.dumps(dict(status='PASS',decoded_frames=int(stream['nb_read_frames']),encoded_fps=stream['r_frame_rate'],duration_s=stream['duration'],resolution=[stream['width'],stream['height']],stills=stills,disclaimer='Encoded media properties only, NOT detector throughput or latency. Synthetic clip, not live camera performance.'),indent=2))
print('MEDIA_READY')
