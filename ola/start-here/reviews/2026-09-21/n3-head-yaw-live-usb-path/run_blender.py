import subprocess,sys,json,time
from pathlib import Path
R=Path(__file__).resolve().parent
name=sys.argv[1]
blend=Path(sys.argv[2]) if len(sys.argv)>2 else R/'Punching_Bag_N3_Head_Track_Yaw.blend'
cmd=['C:/Program Files/Blender Foundation/Blender 3.6/blender.exe','-b',str(blend),'-t','4','--python-exit-code','1','--python',str(R/(name+'.py'))]
start=time.time()
with (R/(name+'.log')).open('w',encoding='utf-8') as log:p=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT)
(R/(name+'_process.json')).write_text(json.dumps(dict(command=cmd,exit_code=p.returncode,elapsed_s=time.time()-start),indent=2))
print(name,p.returncode,flush=True);sys.exit(p.returncode)
