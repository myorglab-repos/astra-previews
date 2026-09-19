const stage=document.querySelector('#stage'),poster=document.querySelector('#poster'),motion=document.querySelector('#motion'),beat=document.querySelector('#beat'),status=document.querySelector('#status');
const reduced=matchMedia('(prefers-reduced-motion: reduce)');
let paused=false,viewer,pending;
function showPoster(message){viewer?.pause();poster.hidden=false;beat.disabled=true;status.textContent=message;motion.setAttribute('aria-pressed','true');}
async function sync(){
 if(reduced.matches){motion.disabled=true;motion.textContent='Reduced motion';showPoster('Reduced motion · static poster');return;}
 motion.disabled=false;motion.textContent=paused?'Play motion':'Pause motion';
 if(paused){showPoster('Motion paused · static poster');return;}
 status.textContent='Preparing motion…';
 try{
  pending??=import('./viewer.js').then(m=>m.createViewer(stage));viewer=await pending;
  if(paused||reduced.matches){viewer.pause();return;}
  viewer.play();poster.hidden=true;beat.disabled=false;motion.setAttribute('aria-pressed','false');
 }catch(error){console.error(error);paused=true;motion.textContent='Poster mode';motion.disabled=true;showPoster('Static poster · 3D unavailable');}
}
motion.addEventListener('click',()=>{paused=!paused;sync();});beat.addEventListener('click',()=>viewer?.beat());stage.addEventListener('click',()=>{if(!paused&&!reduced.matches)viewer?.beat();});reduced.addEventListener('change',sync);sync();
