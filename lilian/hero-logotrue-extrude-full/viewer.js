import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {DRACOLoader} from 'three/addons/loaders/DRACOLoader.js';
export async function createViewer(stage){
 const renderer=new THREE.WebGLRenderer({alpha:true,antialias:true,preserveDrawingBuffer:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.setClearColor(0xffffff,0);renderer.toneMapping=THREE.NoToneMapping;
 const scene=new THREE.Scene();scene.add(new THREE.HemisphereLight(0xffffff,0x507090,2));
 for(const [power,pos] of [[3,[-5,7,8]],[2,[7,1,4]]]){const l=new THREE.DirectionalLight(0xffffff,power);l.position.set(...pos);scene.add(l);}
 const camera=new THREE.OrthographicCamera(-10.665,10.665,4.48,-4.48,.1,100);camera.position.z=30;
 const draco=new DRACOLoader();draco.setDecoderPath('./vendor/draco/');const loader=new GLTFLoader();loader.setDRACOLoader(draco);let gltf;
 try{gltf=await loader.loadAsync('./hero-logotrue-extrude-full.web.glb');}catch{gltf=await loader.loadAsync('./hero-logotrue-extrude-full.glb');}finally{draco.dispose();}
 const rig=new THREE.Group();rig.add(gltf.scene);scene.add(rig);const root=gltf.scene.getObjectByName('Full_logo_spin');
 const mixer=new THREE.AnimationMixer(gltf.scene);const actions=gltf.animations.map(c=>{const a=mixer.clipAction(c);a.setLoop(THREE.LoopOnce,1);a.clampWhenFinished=true;a.play();return a;});
 let running=false,raf=0,last=0,elapsed=6.2;const status=document.querySelector('#status');
 function resize(){const w=stage.clientWidth,h=stage.clientHeight,a=w/h,v=Math.max(8.96,21.33/a);camera.left=-v*a/2;camera.right=v*a/2;camera.top=v/2;camera.bottom=-v/2;camera.updateProjectionMatrix();renderer.setSize(w,h,false);if(renderer.domElement.isConnected)renderer.render(scene,camera);}
 new ResizeObserver(resize).observe(stage);resize();
 function seek(t){elapsed=Math.max(0,Math.min(6.2,t));for(const a of actions){a.reset().play();}mixer.setTime(elapsed);}
 function draw(now){if(!running)return;const dt=document.hidden?0:Math.min(.05,(now-last)/1000);last=now;elapsed=Math.min(6.2,elapsed+dt);mixer.update(dt);renderer.render(scene,camera);status.textContent=elapsed<3.4?'Spinning · slowing down':elapsed<4.2?'Settling into place':'Front pose · full source lockup';raf=requestAnimationFrame(draw);}
 function pause(){running=false;cancelAnimationFrame(raf);renderer.domElement.remove();}
 function play(){pause();stage.append(renderer.domElement);rig.rotation.set(0,0,0);seek(0);resize();running=true;last=performance.now();raf=requestAnimationFrame(draw);}
 function pose(deg){pause();stage.append(renderer.domElement);seek(6.2);rig.rotation.y=deg*Math.PI/180;resize();renderer.render(scene,camera);status.textContent=deg?'25° view · shallow extrusion':'Front pose · full source lockup';}
 function beat(){play();}
 document.addEventListener('visibilitychange',()=>{last=performance.now();});
 window.heroReview={gltf,renderer,scene,camera,root,rig,mixer,seek,get elapsed(){return elapsed;}};
 return {play,pause,pose,beat};
}
