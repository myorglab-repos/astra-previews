import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

export async function createViewer(stage) {
  const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setClearColor(0x00123f, 0);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = .9;
  const scene = new THREE.Scene();
  const pmrem = new THREE.PMREMGenerator(renderer);
  const room = new RoomEnvironment();
  const environment = pmrem.fromScene(room, .04);
  scene.environment = environment.texture;
  room.dispose(); pmrem.dispose();
  scene.environmentIntensity = .6;
  scene.add(new THREE.HemisphereLight(0xffffff, 0x00123f, 1));
  const key = new THREE.DirectionalLight(0xffffff, 2); key.position.set(-3, 4, 6); scene.add(key);
  const fill = new THREE.DirectionalLight(0x19e3f2, 1); fill.position.set(4, 1, 4); scene.add(fill);
  const camera = new THREE.OrthographicCamera(-3, 3, 2, -2, .1, 50); camera.position.set(0, 0, 12);
  const draco = new DRACOLoader(); draco.setDecoderPath('./vendor/draco/');
  const loader = new GLTFLoader(); loader.setDRACOLoader(draco);
  let gltf;
  try { gltf = await loader.loadAsync('./hero-plates-pulse-m.web.glb'); }
  catch { gltf = await loader.loadAsync('./hero-plates-pulse-m.glb'); }
  finally { draco.dispose(); }
  const rig = new THREE.Group(); scene.add(rig); rig.add(gltf.scene);
  const mixer = new THREE.AnimationMixer(gltf.scene);
  if (!gltf.animations.length) throw new Error('The asset contains no intrinsic animation.');
  gltf.animations.forEach(clip => mixer.clipAction(clip).play());
  const seamMaterials = [];
  gltf.scene.traverse(o => { if (o.isMesh && o.material?.name.startsWith('seam_')) { o.material.toneMapped=false; o.material.side=THREE.DoubleSide; seamMaterials.push({material:o.material,phase:Number(o.material.name.slice(-2))/16}); } });
  let running = false, raf = 0, last = 0, beatAge = 10;
  const pointer = new THREE.Vector2();
  function resize() {
    const width = stage.clientWidth, height = stage.clientHeight, aspect = width / height;
    const h = Math.max(3.95, 5.65 / aspect);
    camera.left = -h * aspect / 2; camera.right = h * aspect / 2;
    camera.top = h / 2; camera.bottom = -h / 2; camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }
  new ResizeObserver(resize).observe(stage); resize();
  stage.addEventListener('pointermove', e => {
    if (!running || e.pointerType === 'touch') return;
    const r = stage.getBoundingClientRect();
    pointer.set((e.clientX-r.left)/r.width*2-1, (e.clientY-r.top)/r.height*2-1);
  });
  stage.addEventListener('pointerleave', () => pointer.set(0, 0));
  function draw(now) {
    if (!running) return;
    const dt = Math.min((now-last)/1000, .05); last = now;
    mixer.update(dt); beatAge += dt;
    const follow = 1-Math.exp(-dt*3);
    rig.rotation.y += (pointer.x*.055-rig.rotation.y)*follow;
    rig.rotation.x += (pointer.y*.035-rig.rotation.x)*follow;
    const envelope = beatAge < 1.3 ? Math.sin(Math.PI*beatAge/1.3)**2 : 0;
    rig.scale.setScalar(1 + .038*envelope);
    for (const s of seamMaterials) s.material.emissiveIntensity = .25 + 3.1*(.5+.5*Math.sin(2*Math.PI*(mixer.time/3-s.phase))) + 3*envelope;
    renderer.render(scene, camera); raf = requestAnimationFrame(draw);
  }
  function pause() {
    running = false; cancelAnimationFrame(raf); renderer.domElement.remove();
    pointer.set(0, 0); rig.rotation.set(0, 0, 0); rig.scale.setScalar(1); beatAge = 10;
  }
  function play() {
    if (running) return; running = true; stage.append(renderer.domElement);
    resize(); last = performance.now(); raf = requestAnimationFrame(draw);
  }
  document.addEventListener('visibilitychange', () => { last = performance.now(); });
  // Read-only inspection hook for repeatable local QA. Idle transforms belong to GLB clips.
  window.heroReview = { gltf, mixer, rig, renderer, scene, camera, seamMaterials };
  return { play, pause, beat() { if (running && beatAge >= 1.3) beatAge = 0; } };
}
