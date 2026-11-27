/* ============================================================
   TOP SHELF: SEE YOUR BUSINESS  ·  site widget
   Replaces the old gap quiz pop-up (assets/gap-quiz.js stays in the repo, unused).
   Pick an industry, see that sample business's website and CRM side by side,
   then Try the CRM. Self-contained: injects its own CSS, no other scripts, no form.
   Same open rules the gap quiz used: 45% scroll or exit intent, once per session,
   7 days quiet after a dismiss, a reopen tab bottom-left.
   The PAIRS block is written by scripts/build_site_update.py from
   renders-src/industry-crm/pairs.json; edit there, not here.
   ============================================================ */
(function(){
"use strict";

/*PAIRS:start*/
var PAIRS = [
 {"slug":"home-services","label":"Home Services","business":"Everline Home Services","site":"websites/everline-home-services/index.html","web":"assets/img/websites/everline-home-services-home-d.webp","crm":"assets/img/crm/industries/home-services/1-today-d.webp","crm_role":"Owner · Today","page":"industry-home-services.html"},
 {"slug":"car-lots","label":"Car Lots","business":"Bramlett Motor Co.","site":"websites/bramlett-motor-co/index.html","web":"assets/img/websites/bramlett-motor-co-home-d.webp","crm":"assets/img/crm/industries/car-lots/1-home-d.webp","crm_role":"Owner · Home","page":"industry-auto.html#car-lots"},
 {"slug":"auto-repair","label":"Auto Repair","business":"Apex Auto Werks","site":"websites/apex-auto-werks/index.html","web":"assets/img/websites/apex-auto-werks-home-d.webp","crm":"assets/img/crm/industries/auto-repair/1-owner-home-d.webp","crm_role":"Owner · Service today","page":"industry-auto.html#auto-repair"},
 {"slug":"auto-detailing","label":"Auto Detailing","business":"Kestrel Lane Detail Co.","site":"websites/kestrel-lane-detail/index.html","web":"assets/img/websites/kestrel-lane-detail-home-d.webp","crm":"assets/img/crm/industries/auto-detailing/1-owner-home-d.webp","crm_role":"Owner · Home","page":"industry-auto.html#auto-detailing"},
 {"slug":"real-estate","label":"Real Estate","business":"Elena Marsh Real Estate","site":"websites/elena-marsh-realty/index.html","web":"assets/img/websites/elena-marsh-realty-home-d.webp","crm":"assets/img/crm/industries/real-estate/1-today-d.webp","crm_role":"Agent · Today","page":"industry-real-estate.html"},
 {"slug":"fitness","label":"Gyms & Fitness","business":"Larkspur Strength Club","site":"websites/larkspur-strength-club/index.html","web":"assets/img/websites/larkspur-strength-club-home-d.webp","crm":"assets/img/crm/industries/fitness/1-dashboard-d.webp","crm_role":"Owner · Dashboard","page":"industry-salon-spa-fitness.html#fitness"},
 {"slug":"salon-spa","label":"Salon & Spa","business":"Lumen Wellness","site":"websites/lumen-wellness/index.html","web":"assets/img/websites/lumen-wellness-home-d.webp","crm":"assets/img/crm/industries/salon-spa/1-owner-today-d.webp","crm_role":"Owner · Today","page":"industry-salon-spa-fitness.html#salon-spa"},
 {"slug":"restaurants","label":"Restaurants & Bars","business":"Ember & Oak","site":"websites/ember-and-oak/index.html","web":"assets/img/websites/ember-and-oak-home-d.webp","crm":"assets/img/crm/industries/restaurants/1-tonight-d.webp","crm_role":"Owner · Tonight","page":"industry-restaurants.html"},
 {"slug":"medical-dental","label":"Medical & Dental","business":"Brightwater Dental","site":"websites/brightwater-dental/index.html","web":"assets/img/websites/brightwater-dental-home-d.webp","crm":"assets/img/crm/industries/medical-dental/1-today-d.webp","crm_role":"Dentist · Today","page":"industry-medical-dental.html"},
 {"slug":"legal","label":"Law Firms","business":"Halcourt & Vale","site":"websites/halcourt-vale/index.html","web":"assets/img/websites/halcourt-vale-home-d.webp","crm":"assets/img/crm/industries/legal/1-today-d.webp","crm_role":"Attorney · Today","page":"industry-legal.html"},
 {"slug":"retail","label":"Retail & Local Shops","business":"Field & Fawn","site":"websites/field-and-fawn/index.html","web":"assets/img/websites/field-and-fawn-home-d.webp","crm":"assets/img/crm/industries/retail/1-today-d.webp","crm_role":"Owner · Today","page":"industry-retail.html"},
 {"slug":"vet","label":"Vet Clinics","business":"Wellspring Animal Hospital","site":"websites/wellspring-animal-hospital/index.html","web":"assets/img/websites/wellspring-animal-hospital-home-d.webp","crm":"assets/img/crm/industries/vet/1-today-d.webp","crm_role":"Doctor · Today","page":"industry-custom.html"}
];
/*PAIRS:end*/

var TEXT = {
  kicker:"Top Shelf",
  title:"See your business",
  sub:"Pick your industry to see a sample business with its website and its CRM side by side. They share a name and a look, the way yours would.",
  picker:"Pick your industry",
  note:"Sample website · Sample CRM",
  web:"Sample website", crm:"Sample CRM",
  cta:"Try the CRM", ctaHref:"contact.html",
  more:"See this industry",
  how:"Fill out a short form. We call you, then send you a demo."
};
var BE = {scrollPercent:45, exitIntent:true, oncePerSession:true, dismissDays:7,
  reopenLabel:"See your business", suppressPaths:["contact.html","thank-you.html"]};
var C = {ground:"#0B0906",surface:"#100C08",card:"#15100B",gold:"#C9A86A",goldBright:"#E4C98A",ink:"#F4F0E8",ink2:"#CFC7B8",ink3:"#A39A89",line:"rgba(201,168,106,.22)"};
var FD="'DM Serif Display',Georgia,serif", FB="'DM Sans',system-ui,sans-serif";

var root, card, chips=[], cur=0, opened=false, lastFocus=null, tab;

function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];});}

function css(){
  var s=document.createElement('style');s.id='tssyb-css';s.textContent=
  '#tssyb,#tssyb *{box-sizing:border-box}'+
  '#tssyb{position:fixed;inset:0;z-index:99990;display:none;align-items:center;justify-content:center;background:rgba(6,5,3,.66);padding:20px;font-family:'+FB+'}'+
  '#tssyb.show{display:flex}'+
  '.syb-card{width:100%;max-width:880px;max-height:92vh;overflow:auto;background:'+C.ground+';border:1px solid '+C.line+';border-radius:18px;padding:26px;color:'+C.ink2+';position:relative;outline:none;animation:syb-in .32s cubic-bezier(.23,1,.32,1)}'+
  '@keyframes syb-in{from{opacity:0;transform:translateY(12px) scale(.98)}to{opacity:1;transform:none}}'+
  '.syb-top{display:flex;align-items:center;justify-content:space-between;gap:12px}'+
  '.syb-brand{display:flex;align-items:center;gap:10px;font-size:11px;font-weight:500;letter-spacing:2.4px;text-transform:uppercase;color:'+C.gold+'}'+
  '.syb-brand img{width:28px;height:28px;display:block}'+
  '.syb-x{width:40px;height:40px;display:grid;place-items:center;background:none;border:1px solid transparent;border-radius:10px;color:'+C.ink3+';cursor:pointer}'+
  '.syb-x:hover{color:'+C.ink+';border-color:'+C.line+'}'+
  '.syb-h{font-family:'+FD+';font-weight:400;color:'+C.ink+';font-size:clamp(26px,3.4vw,34px);line-height:1.1;margin:14px 0 8px}'+
  '.syb-sub{margin:0;font-size:15px;line-height:1.6;max-width:62ch}'+
  '.syb-pick{margin:18px 0 8px;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:'+C.ink3+'}'+
  '.syb-chips{display:flex;flex-wrap:wrap;gap:8px}'+
  '.syb-chip{font-family:'+FB+';font-size:14px;font-weight:500;color:'+C.ink2+';background:transparent;border:1px solid '+C.line+';border-radius:999px;padding:9px 15px;cursor:pointer;transition:border-color .2s,background-color .2s,color .2s}'+
  '.syb-chip:hover{border-color:rgba(201,168,106,.55);color:'+C.ink+'}'+
  '.syb-chip[aria-checked="true"]{background:'+C.gold+';border-color:'+C.gold+';color:'+C.ground+'}'+
  '.syb-chip:focus-visible,.syb-x:focus-visible,.syb-btn:focus-visible{outline:2px solid '+C.goldBright+';outline-offset:2px}'+
  '.syb-show{margin-top:22px;padding-top:20px;border-top:1px solid '+C.line+'}'+
  '.syb-biz{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:4px 16px}'+
  '.syb-biz h3{font-family:'+FD+';font-weight:400;color:'+C.ink+';font-size:24px;margin:0;line-height:1.2}'+
  '.syb-note{font-size:13px;color:'+C.ink3+'}'+
  '.syb-shots{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px}'+
  '.syb-shots figure{margin:0}'+
  '.syb-shots img{display:block;width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;border-radius:10px;border:1px solid '+C.line+';background:'+C.surface+';color:'+C.ink3+';font-size:12px}'+
  '.syb-shots figcaption{margin-top:7px;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:'+C.gold+'}'+
  '.syb-acts{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin-top:20px}'+
  '.syb-btn{display:inline-flex;align-items:center;justify-content:center;min-height:46px;padding:0 22px;border-radius:999px;font:500 15px/1 '+FB+';text-decoration:none;border:1px solid transparent;transition:background-color .2s,border-color .2s}'+
  '.syb-gold{background:'+C.gold+';color:'+C.ground+'}.syb-gold:hover{background:'+C.goldBright+'}'+
  '.syb-line{border-color:rgba(201,168,106,.45);color:'+C.goldBright+'}.syb-line:hover{background:rgba(201,168,106,.1)}'+
  '.syb-how{width:100%;margin:2px 0 0;font-size:13px;color:'+C.ink3+'}'+
  '#tssyb-tab{position:fixed;left:16px;bottom:16px;z-index:99989;background:linear-gradient(180deg,'+C.goldBright+','+C.gold+' 58%,#A98A4E);color:'+C.ground+';border:1px solid rgba(228,201,138,.6);border-radius:999px;padding:11px 18px;font-family:'+FB+';font-weight:600;font-size:13px;cursor:pointer;display:none;box-shadow:inset 0 1px 0 rgba(255,255,255,.4),0 12px 28px -10px rgba(201,168,106,.55),0 3px 8px -2px rgba(0,0,0,.45);transition:transform .34s cubic-bezier(.34,1.3,.5,1)}'+
  '#tssyb-tab:hover{transform:translateY(-3px)}'+
  '#tssyb-tab:focus-visible{outline:2px solid '+C.ink+';outline-offset:2px}'+
  '@media(max-width:560px){#tssyb{padding:0}.syb-card{max-width:100%;max-height:100vh;min-height:100vh;border-radius:0;padding:20px 16px 28px}.syb-shots{grid-template-columns:1fr}.syb-chip{font-size:13px;padding:8px 12px}.syb-btn{flex:1 1 100%}}'+
  '@media(prefers-reduced-motion:reduce){.syb-card{animation:none}#tssyb-tab,.syb-chip,.syb-btn{transition:none}#tssyb-tab:hover{transform:none}}';
  document.head.appendChild(s);
}

function build(){
  root=document.createElement('div');root.id='tssyb';
  var ch=PAIRS.map(function(p,i){
    return '<button type="button" class="syb-chip" role="radio" aria-checked="false" tabindex="-1" data-i="'+i+'">'+esc(p.label)+'</button>';
  }).join('');
  root.innerHTML='<div class="syb-card" role="dialog" aria-modal="true" aria-labelledby="syb-h" aria-describedby="syb-sub" tabindex="-1">'+
    '<div class="syb-top"><span class="syb-brand"><img src="assets/logo-mark.png" alt="">'+esc(TEXT.kicker)+'</span>'+
    '<button type="button" class="syb-x" aria-label="Close"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg></button></div>'+
    '<h2 class="syb-h" id="syb-h">'+esc(TEXT.title)+'</h2>'+
    '<p class="syb-sub" id="syb-sub">'+esc(TEXT.sub)+'</p>'+
    '<p class="syb-pick" id="syb-pick">'+esc(TEXT.picker)+'</p>'+
    '<div class="syb-chips" role="radiogroup" aria-labelledby="syb-pick">'+ch+'</div>'+
    '<div class="syb-show" aria-live="polite">'+
      '<div class="syb-biz"><h3 id="syb-biz"></h3><span class="syb-note">'+esc(TEXT.note)+'</span></div>'+
      '<div class="syb-shots">'+
        '<figure><img id="syb-web" width="1200" height="750" alt=""><figcaption>'+esc(TEXT.web)+'</figcaption></figure>'+
        '<figure><img id="syb-crm" width="1440" height="900" alt=""><figcaption>'+esc(TEXT.crm)+'</figcaption></figure>'+
      '</div>'+
      '<div class="syb-acts"><a class="syb-btn syb-gold" href="'+TEXT.ctaHref+'">'+esc(TEXT.cta)+'</a>'+
      '<a class="syb-btn syb-line" id="syb-more" href="#">'+esc(TEXT.more)+'</a>'+
      '<p class="syb-how">'+esc(TEXT.how)+'</p></div>'+
    '</div>'+
  '</div>';
  document.body.appendChild(root);
  card=root.querySelector('.syb-card');
  chips=[].slice.call(root.querySelectorAll('.syb-chip'));
  chips.forEach(function(b){
    b.addEventListener('click',function(){pick(+b.getAttribute('data-i'),true);});
  });
  root.querySelector('.syb-chips').addEventListener('keydown',function(e){
    var n=chips.length,k=e.key,i=cur;
    if(k==='ArrowRight'||k==='ArrowDown')i=(cur+1)%n;
    else if(k==='ArrowLeft'||k==='ArrowUp')i=(cur-1+n)%n;
    else if(k==='Home')i=0;
    else if(k==='End')i=n-1;
    else return;
    e.preventDefault();pick(i,true);
  });
  root.querySelector('.syb-x').addEventListener('click',close);
  root.addEventListener('click',function(e){if(e.target===root)close();});
  document.addEventListener('keydown',function(e){
    if(!opened)return;
    if(e.key==='Escape'){e.preventDefault();close();return;}
    if(e.key==='Tab')trap(e);
  });
  tab=document.createElement('button');tab.type='button';tab.id='tssyb-tab';tab.textContent=BE.reopenLabel;
  tab.addEventListener('click',open);document.body.appendChild(tab);
  pick(0,false);
}

function pick(i,focus){
  cur=i;var p=PAIRS[i];
  chips.forEach(function(b,j){var on=j===i;b.setAttribute('aria-checked',on?'true':'false');b.tabIndex=on?0:-1;});
  if(focus)chips[i].focus();
  root.querySelector('#syb-biz').textContent=p.business;
  var w=root.querySelector('#syb-web'),c=root.querySelector('#syb-crm');
  w.alt='Home page of the '+p.business+' sample website';
  c.alt=p.business+' sample CRM, '+p.crm_role+' screen';
  if(opened){w.src=p.web;c.src=p.crm;}
  root.querySelector('#syb-more').href=p.page;
}

function focusables(){
  return [].slice.call(card.querySelectorAll('a[href],button:not([disabled]),[tabindex]:not([tabindex="-1"])'))
    .filter(function(el){return el.offsetParent!==null;});
}
function trap(e){
  var f=focusables();if(!f.length)return;
  var first=f[0],last=f[f.length-1],a=document.activeElement;
  if(e.shiftKey&&(a===first||a===card)){e.preventDefault();last.focus();}
  else if(!e.shiftKey&&a===last){e.preventDefault();first.focus();}
  else if(!card.contains(a)){e.preventDefault();first.focus();}
}

function open(){
  if(opened)return;opened=true;lastFocus=document.activeElement;
  root.classList.add('show');document.documentElement.style.overflow='hidden';
  tab.style.display='none';
  pick(cur,false);
  chips[cur].focus();
}
function close(){
  if(!opened)return;opened=false;
  root.classList.remove('show');document.documentElement.style.overflow='';
  try{localStorage.setItem('tssyb_dismissed',Date.now());}catch(e){}
  tab.style.display='block';
  if(lastFocus&&lastFocus.focus&&lastFocus!==document.body)lastFocus.focus();else tab.focus();
}

function arm(){
  var fired=false;
  function go(){if(fired)return;fired=true;try{sessionStorage.setItem('tssyb_shown','1');}catch(e){}open();}
  try{var d=+localStorage.getItem('tssyb_dismissed');if(d&&(Date.now()-d)<BE.dismissDays*864e5){tab.style.display='block';return;}}catch(e){}
  if(BE.oncePerSession){try{if(sessionStorage.getItem('tssyb_shown')){tab.style.display='block';return;}}catch(e){}}
  if(BE.scrollPercent)window.addEventListener('scroll',function ons(){
    var max=document.body.scrollHeight-innerHeight;if(max<=0)return;
    if(scrollY/max*100>=BE.scrollPercent){window.removeEventListener('scroll',ons);go();}
  },{passive:true});
  if(BE.exitIntent)document.addEventListener('mouseout',function(e){if(!e.relatedTarget&&e.clientY<=0)go();});
}

function suppressed(){var p=location.pathname.split('/').pop();return BE.suppressPaths.indexOf(p)>-1;}
function init(){if(suppressed()||!PAIRS.length)return;css();build();arm();window.TSSee={open:open,close:close};}
if(document.readyState!=='loading')init();else document.addEventListener('DOMContentLoaded',init);
})();
