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
 try{gltf=await loader.loadAsync('./hero-smooth-spin-m.web.glb');}catch{gltf=await loader.loadAsync('./hero-smooth-spin-m.web.glb');}finally{draco.dispose();}
 const rig=new THREE.Group();scene.add(rig);rig.add(gltf.scene);const mixer=new THREE.AnimationMixer(gltf.scene);if(!gltf.animations.length)throw new Error('Missing intrinsic spin');gltf.animations.forEach(c=>mixer.clipAction(c).play());
 const basePitch=.06,baseYaw=0;rig.rotation.x=basePitch;
 let running=false,raf=0,last=0,beatAge=10;const pointer=new THREE.Vector2();
 function resize(){const w=stage.clientWidth,h=stage.clientHeight,a=w/h,v=Math.max(4,5.65/a);camera.left=-v*a/2;camera.right=v*a/2;camera.top=v/2;camera.bottom=-v/2;camera.updateProjectionMatrix();renderer.setSize(w,h,false);}
 new ResizeObserver(resize).observe(stage);resize();
 stage.addEventListener('pointermove',e=>{if(!running||e.pointerType==='touch')return;const r=stage.getBoundingClientRect();pointer.set((e.clientX-r.left)/r.width*2-1,(e.clientY-r.top)/r.height*2-1);});stage.addEventListener('pointerleave',()=>pointer.set(0,0));
 function draw(now){if(!running)return;const dt=document.hidden?0:(now-last)/1000;last=now;beatAge+=dt;const envelope=beatAge<1.6?Math.sin(Math.PI*beatAge/1.6)**2:0;mixer.timeScale=1+2*envelope;mixer.update(dt);const f=1-Math.exp(-dt*3);rig.rotation.y+=(pointer.x*.055-rig.rotation.y)*f;rig.rotation.x+=(basePitch+pointer.y*.035-rig.rotation.x)*f;renderer.render(scene,camera);raf=requestAnimationFrame(draw);}
 function pause(){running=false;cancelAnimationFrame(raf);renderer.domElement.remove();pointer.set(0,0);rig.rotation.set(basePitch,0,0);beatAge=10;mixer.timeScale=1;}
 function play(){if(running)return;running=true;stage.append(renderer.domElement);resize();last=performance.now();raf=requestAnimationFrame(draw);}
 document.addEventListener('visibilitychange',()=>{last=performance.now();});
 window.heroReview={gltf,mixer,rig,renderer,scene,camera,basePitch,baseYaw};return {play,pause,beat(){if(running&&beatAge>=1.6)beatAge=0;}};
}

