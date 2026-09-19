import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {DRACOLoader} from 'three/addons/loaders/DRACOLoader.js';
import {RoomEnvironment} from 'three/addons/environments/RoomEnvironment.js';
export async function createViewer(stage){
 const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0x00123f,0);renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.1;
 const scene=new THREE.Scene(),pmrem=new THREE.PMREMGenerator(renderer),room=new RoomEnvironment(),environment=pmrem.fromScene(room,.04);scene.environment=environment.texture;room.dispose();pmrem.dispose();
 scene.add(new THREE.HemisphereLight(0xffffff,0x00123f,1.3));
 for(const [color,intensity,pos] of [[0xffffff,2,[-3,4,6]],[0x9bedff,1,[4,1,4]],[0x73c8ff,2,[-3,3,-4]]]){const l=new THREE.DirectionalLight(color,intensity);l.position.set(...pos);scene.add(l);}
 const camera=new THREE.OrthographicCamera(-3,3,2,-2,.1,50);camera.position.set(0,0,12);
 const draco=new DRACOLoader();draco.setDecoderPath('./vendor/draco/');const loader=new GLTFLoader();loader.setDRACOLoader(draco);let gltf;
 try{gltf=await loader.loadAsync('./hero-smooth-spin-decel-m.web.glb');}catch{gltf=await loader.loadAsync('./hero-smooth-spin-decel-m.web.glb');}finally{draco.dispose();}
 const rig=new THREE.Group();scene.add(rig);rig.add(gltf.scene);const mixer=new THREE.AnimationMixer(gltf.scene);if(!gltf.animations.length)throw new Error('Missing intrinsic spin');
 const actions=gltf.animations.map(c=>{const a=mixer.clipAction(c);a.setLoop(THREE.LoopOnce,1);a.clampWhenFinished=true;a.play();return a;});
 let running=false,raf=0,last=0,elapsed=0,restartOffset=0;const pointer=new THREE.Vector2(),status=document.querySelector('#status');
 const root=gltf.scene.getObjectByName('M_spin_decel_settle');
 function resize(){const w=stage.clientWidth,h=stage.clientHeight,a=w/h,v=Math.max(4,5.65/a);camera.left=-v*a/2;camera.right=v*a/2;camera.top=v/2;camera.bottom=-v/2;camera.updateProjectionMatrix();renderer.setSize(w,h,false);}
 new ResizeObserver(resize).observe(stage);resize();
 stage.addEventListener('pointermove',e=>{if(!running||e.pointerType==='touch')return;const r=stage.getBoundingClientRect();pointer.set((e.clientX-r.left)/r.width*2-1,(e.clientY-r.top)/r.height*2-1);});stage.addEventListener('pointerleave',()=>pointer.set(0,0));
 function seek(t){elapsed=Math.max(0,Math.min(6.2,t));for(const a of actions){a.paused=false;a.enabled=true;}mixer.setTime(elapsed);}
 function restart(){
  // Preserve the visible angle on a tap during motion, easing its offset away.
  restartOffset=Math.atan2(2*root.quaternion.w*root.quaternion.y,1-2*root.quaternion.y**2)+rig.rotation.y;
  rig.rotation.y=restartOffset;
  elapsed=0;for(const a of actions)a.reset().play();mixer.setTime(0);
 }
 function draw(now){if(!running)return;const dt=document.hidden?0:Math.min(.05,(now-last)/1000);last=now;elapsed=Math.min(6.2,elapsed+dt);mixer.update(dt);
  const f=1-Math.exp(-dt*5),offset=restartOffset*Math.max(0,1-elapsed/3.4)**3;
  rig.rotation.y+=(pointer.x*.055+offset-rig.rotation.y)*f;rig.rotation.x+=(pointer.y*.035-rig.rotation.x)*f;
  if(!pointer.lengthSq()&&elapsed>=4.2)rig.rotation.set(0,0,0);
  const label=elapsed<3.4?'Spinning · slowing down':elapsed<4.2?'Soft landing':'Front pose · tap to spin again';if(status.textContent!==label)status.textContent=label;
  renderer.render(scene,camera);raf=requestAnimationFrame(draw);
 }
 function pause(){running=false;cancelAnimationFrame(raf);renderer.domElement.remove();pointer.set(0,0);rig.rotation.set(0,0,0);restartOffset=0;}
 function play(){if(running)return;running=true;stage.append(renderer.domElement);resize();restartOffset=0;elapsed=0;for(const a of actions)a.reset().play();mixer.setTime(0);last=performance.now();raf=requestAnimationFrame(draw);}
 document.addEventListener('visibilitychange',()=>{last=performance.now();});
 window.heroReview={gltf,mixer,rig,renderer,scene,camera,root,seek,get elapsed(){return elapsed;}};
 return {play,pause,beat(){if(running)restart();}};
}
