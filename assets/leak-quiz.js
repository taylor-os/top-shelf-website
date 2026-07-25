/* ============================================================
   TOP SHELF — LEAK FINDER (Quiz A)  ·  site widget
   Self-injecting pop-up lead tool. Loaded site-wide via
   <script src="assets/leak-quiz.js"></script> before </body>.
   Rebrandable: edit the CONFIG object below. Source template:
   Drive → Projects/Top Shelf/Templates/Lead-Capture Widgets/
   ============================================================ */
(function(){
"use strict";

var CONFIG = {
  brand: {
    name:"Top Shelf", logoText:"TOP SHELF", logoUrl:"", kicker:"Business Leak Finder",
    colors:{ground:"#0B0906",surface:"#100C08",gold:"#C9A86A",goldBright:"#E4C98A",ink:"#F4F0E8",ink2:"#CFC7B8",ink3:"#98907F",ink4:"#6E675A",hairline:"rgba(201,168,106,.20)"},
    fontImport:"https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,500;1,600&family=Jost:wght@300;400;500&display=swap",
    fontDisplay:"'Cormorant Garamond',Georgia,serif", fontBody:"'Jost',system-ui,sans-serif"
  },
  behavior: {
    triggerSeconds: 7, scrollPercent: 45, exitIntent: true,
    oncePerSession: true, dismissDays: 7, showDollars: true, currency: "$",
    leadEndpoint: "https://top-shelf-production.up.railway.app/api/website-lead",
    leadFallback: "https://formspree.io/f/FORMSPREE_ID",  /* set the real Formspree id if the CRM is down */
    reopen: true, reopenLabel: "Find your leaks",
    suppressPaths: ["contact.html","thank-you.html"]      /* don't pop on these pages */
  },
  intro: {
    eyebrow:"60-second business check",
    headline:"Where is your business <em>leaking money?</em>",
    sub:"No forms, no typing — just tap what sounds familiar. We'll show you where you're likely losing customers and what it's costing.",
    cta:"Find my leaks"
  },
  areas: [
    { eyebrow:"Getting found", icon:"map-pin", solution:"Websites & Local SEO", solutionUrl:"solution-websites-seo.html",
      question:"When someone needs what you do, how easily do they find you?", transition:"",
      symptoms:[{label:"Not on page 1 of Google for &lsquo;near me&rsquo;",monthly:1400},{label:"My website is dated, slow, or missing",monthly:900},{label:"Not showing in the Google Map Pack",monthly:1200}]},
    { eyebrow:"Your reputation", icon:"star", solution:"Reviews & Reputation", solutionUrl:"solution-reviews.html",
      question:"How does your reputation look when they compare you?", transition:"",
      transitionIf:{area:0,symptom:1,text:"With no website steering people to review you, this usually suffers too."},
      symptoms:[{label:"Fewer reviews than my competitors",monthly:1100},{label:"My reviews are old and stale",monthly:600},{label:"No system asking customers for reviews",monthly:900}]},
    { eyebrow:"The phone", icon:"phone", solution:"AI Phone & Receptionist", solutionUrl:"solution-ai-phone.html",
      question:"When they call and you&rsquo;re busy or closed, what happens?", transition:"They found you and trust the reviews — they still have to reach you.",
      symptoms:[{label:"Calls go to voicemail when we&rsquo;re busy",monthly:1800},{label:"Nobody answers after hours",monthly:1500},{label:"Not sure how many calls I miss",monthly:800}]},
    { eyebrow:"Follow-up", icon:"route", solution:"Lead Capture & CRM", solutionUrl:"solution-crm.html",
      question:"Who chases the leads and quotes that don&rsquo;t close on the spot?", transition:"And the ones who don&rsquo;t get through, or ask for a quote?",
      symptoms:[{label:"Quotes go cold — no follow-up",monthly:1700},{label:"Leads slip through the cracks",monthly:1400},{label:"No CRM — it&rsquo;s all in my head",monthly:900}]},
    { eyebrow:"Repeat &amp; time", icon:"refresh", solution:"Memberships & Automation", solutionUrl:"solution-memberships.html",
      question:"Once you win a customer, does anything bring them back?", transition:"Last one — winning them the first time is the expensive part.",
      symptoms:[{label:"Customers buy once and vanish",monthly:1200},{label:"No memberships or loyalty",monthly:800},{label:"I&rsquo;m buried in admin all day",monthly:1000}]}
  ],
  industries:["Home services","Restaurant / bar","Medical / dental","Law firm","Retail / local","Auto","Salon / spa / fitness","Other"],
  thankYou:{
    title:"Thank you — this is exactly what we needed.",
    body:"We&rsquo;ve got your answers. A Top Shelf specialist will personally reach out within one business day to walk you through what each leak is costing you — and exactly how we&rsquo;d plug it. No pressure, just your numbers.",
    note:"We&rsquo;ll reach out using the contact info you shared."
  }
};

var ICONS={
 "map-pin":'<path d="M12 21.5s7-6.6 7-12A7 7 0 0 0 5 9.5c0 5.4 7 12 7 12Z"/><circle cx="12" cy="9.3" r="2.4"/>',
 "star":'<path d="M12 3.3l2.6 5.4 5.9.8-4.3 4.2 1 5.9-5.2-2.8-5.2 2.8 1-5.9-4.3-4.2 5.9-.8Z"/>',
 "phone":'<path d="M6.5 3.5 9 6c.3.6.2 1.3-.3 1.8L7.3 9.2a13 13 0 0 0 7.5 7.5l1.4-1.4c.5-.5 1.2-.6 1.8-.3l2.5 2.5c.6.6.6 1.6-.1 2.1-1.2 1-2.8 1.5-4.4 1.1-5.4-1.4-9.6-5.6-11-11-.4-1.6.1-3.2 1.1-4.4.5-.7 1.5-.7 2.1-.1Z"/>',
 "route":'<circle cx="6" cy="19" r="2.4"/><circle cx="18" cy="5" r="2.4"/><path d="M8.4 19h6.1a3 3 0 0 0 0-6h-5a3 3 0 0 1 0-6H15.6"/>',
 "refresh":'<path d="M4 12a8 8 0 0 1 13.7-5.6L20 8.5"/><polyline points="20,3.5 20,8.5 15,8.5"/><path d="M20 12a8 8 0 0 1-13.7 5.6L4 15.5"/><polyline points="4,20.5 4,15.5 9,15.5"/>',
 "check":'<polyline points="4,12.5 9,17.5 20,6.5"/>',"x":'<line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/>',
 "report":'<rect x="4" y="3" width="16" height="18" rx="2"/><line x1="8" y1="8" x2="16" y2="8"/><line x1="8" y1="12" x2="16" y2="12"/><line x1="8" y1="16" x2="13" y2="16"/>'
};
function svg(n,s){return '<svg viewBox="0 0 24 24" width="'+(s||20)+'" height="'+(s||20)+'" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">'+(ICONS[n]||ICONS.star)+'</svg>';}

var B=CONFIG.brand,C=B.colors,BE=CONFIG.behavior;
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var cur=0,sel={},shown=0,MAX=0;CONFIG.areas.forEach(function(a){a.symptoms.forEach(function(s){MAX+=s.monthly;});});
var root,stage,moneyEl,yrEl,barEl,dotsEl,navEl,opened=false;

function css(){
  if(!document.getElementById('tsleak-fonts')){var l=document.createElement('link');l.id='tsleak-fonts';l.rel='stylesheet';l.href=B.fontImport;document.head.appendChild(l);}
  var s=document.createElement('style');s.textContent=
  '#tsleak,#tsleak *{box-sizing:border-box}'+
  '#tsleak{position:fixed;inset:0;z-index:99990;display:none;align-items:center;justify-content:center;background:rgba(6,5,3,.62);padding:20px;font-family:'+B.fontBody+'}'+
  '#tsleak.show{display:flex}'+
  '.tsl-card{width:100%;max-width:540px;max-height:92vh;overflow:auto;background:'+C.ground+';border:1px solid '+C.hairline+';border-radius:18px;padding:26px;color:'+C.ink2+';position:relative}'+
  '.tsl-eb{font-weight:500;font-size:11px;letter-spacing:2.4px;color:'+C.gold+';text-transform:uppercase}'+
  '.tsl-h{font-family:'+B.fontDisplay+';font-weight:500;color:'+C.ink+';margin:6px 0 0;line-height:1.15}'+
  '.tsl-tile{display:flex;align-items:center;gap:13px;width:100%;text-align:left;background:transparent;border:1px solid '+C.hairline+';border-radius:13px;padding:14px 15px;color:'+C.ink2+';font-size:14.5px;cursor:pointer;transition:border-color .22s,background .22s;font-family:'+B.fontBody+'}'+
  '.tsl-tile:hover{border-color:rgba(201,168,106,.5)}.tsl-tile.on{border-color:'+C.gold+';background:rgba(201,168,106,.07);color:'+C.ink+'}'+
  '.tsl-k{width:22px;height:22px;border-radius:6px;border:1px solid rgba(201,168,106,.4);display:flex;align-items:center;justify-content:center;flex:0 0 auto;color:'+C.ground+'}'+
  '.tsl-tile.on .tsl-k{background:'+C.gold+';border-color:'+C.gold+'}'+
  '.tsl-btn{font-family:'+B.fontBody+';font-weight:500;font-size:14px;border-radius:11px;padding:12px 20px;cursor:pointer;border:1px solid transparent}'+
  '.tsl-gold{background:'+C.gold+';color:'+C.ground+'}.tsl-gold:hover{background:'+C.goldBright+'}'+
  '.tsl-line{background:transparent;border:1px solid rgba(201,168,106,.35);color:'+C.gold+'}.tsl-line:hover{background:rgba(201,168,106,.08)}'+
  '.tsl-in{width:100%;background:'+C.surface+';border:1px solid rgba(201,168,106,.25);border-radius:10px;padding:11px 12px;color:'+C.ink+';font-family:'+B.fontBody+';font-size:14px;margin-top:8px}'+
  '.tsl-dot{width:7px;height:7px;border-radius:50%;background:rgba(201,168,106,.25)}.tsl-dot.on{background:'+C.gold+'}'+
  '.tsl-icn{color:'+C.gold+';flex:0 0 auto}'+
  '#tsleak-tab{position:fixed;left:16px;bottom:16px;z-index:99989;background:'+C.gold+';color:'+C.ground+';border:0;border-radius:30px;padding:11px 16px;font-family:'+B.fontBody+';font-weight:500;font-size:13px;cursor:pointer;display:none;box-shadow:0 10px 30px -12px rgba(0,0,0,.7)}'+
  '@media(max-width:560px){.tsl-card{max-width:100%;max-height:100vh;min-height:100vh;border-radius:0}#tsleak{padding:0}}';
  document.head.appendChild(s);
}
function build(){
  root=document.createElement('div');root.id='tsleak';root.setAttribute('role','dialog');root.setAttribute('aria-modal','true');root.setAttribute('aria-label','Business leak finder');
  var logo=B.logoUrl?'<img src="'+B.logoUrl+'" alt="'+B.name+'" style="height:22px">':'<span style="font-weight:500;letter-spacing:1.5px;color:'+C.ink+';font-size:14px">'+B.logoText+'</span>';
  root.innerHTML='<div class="tsl-card">'+
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px"><div style="display:flex;align-items:center;gap:9px"><span class="tsl-icn">'+svg("star",18)+'</span>'+logo+'<span style="color:'+C.ink4+';font-size:12px">· '+B.kicker+'</span></div><button id="tsl-close" aria-label="Close" style="background:none;border:0;color:'+C.ink4+';cursor:pointer">'+svg("x",18)+'</button></div>'+
    (BE.showDollars?'<div id="tsl-meter" style="background:'+C.surface+';border:1px solid rgba(201,168,106,.18);border-radius:13px;padding:14px 16px;margin-bottom:18px;display:none"><div style="display:flex;align-items:baseline;justify-content:space-between"><span class="tsl-eb">Money leaking / month</span><span id="tsl-yr" style="color:'+C.ink4+';font-size:12px">~'+BE.currency+'0 / yr</span></div><div id="tsl-money" style="font-family:'+B.fontDisplay+';font-weight:600;font-size:40px;color:'+C.goldBright+';line-height:1.1">'+BE.currency+'0</div><div style="height:5px;background:rgba(201,168,106,.14);border-radius:4px;margin-top:8px;overflow:hidden"><div id="tsl-bar" style="height:100%;width:0;background:'+C.gold+';transition:width .5s"></div></div><div style="color:'+C.ink4+';font-size:10.5px;margin-top:6px">Rough industry estimate — not a guarantee.</div></div>':'')+
    '<div id="tsl-stage"></div>'+
    '<div style="display:flex;align-items:center;justify-content:space-between;margin-top:20px"><div id="tsl-dots" style="display:flex;gap:6px"></div><div id="tsl-nav" style="display:flex;gap:10px"></div></div>'+
  '</div>';
  document.body.appendChild(root);
  stage=root.querySelector('#tsl-stage');moneyEl=root.querySelector('#tsl-money');yrEl=root.querySelector('#tsl-yr');barEl=root.querySelector('#tsl-bar');dotsEl=root.querySelector('#tsl-dots');navEl=root.querySelector('#tsl-nav');
  root.querySelector('#tsl-close').onclick=close;
  root.addEventListener('click',function(e){if(e.target===root)close();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&opened)close();});
  if(BE.reopen){var tab=document.createElement('button');tab.id='tsleak-tab';tab.textContent=BE.reopenLabel;tab.onclick=open;document.body.appendChild(tab);}
}
function fmt(n){return BE.currency+Math.round(n).toLocaleString();}
function total(){var t=0;for(var k in sel)sel[k].forEach(function(i){t+=CONFIG.areas[k].symptoms[i].monthly;});return t;}
function tween(to){if(reduce){shown=to;moneyEl.textContent=fmt(to);return;}var f=shown,st=performance.now();function fr(now){var p=Math.min(1,(now-st)/450);var v=f+(to-f)*(p<.5?2*p*p:1-Math.pow(-2*p+2,2)/2);moneyEl.textContent=fmt(v);if(p<1)requestAnimationFrame(fr);else{shown=to;moneyEl.textContent=fmt(to);}}requestAnimationFrame(fr);}
function meter(){if(!BE.showDollars)return;var t=total();tween(t);yrEl.textContent='~'+fmt(t*12)+' / yr';barEl.style.width=Math.min(100,t/MAX*140)+'%';}
function setMeter(v){var m=root.querySelector('#tsl-meter');if(m)m.style.display=v?'block':'none';}
function dots(a,c){dotsEl.innerHTML='';for(var i=0;i<c;i++){var d=document.createElement('div');d.className='tsl-dot'+(i<=a?' on':'');dotsEl.appendChild(d);}}
function intro(){setMeter(false);dotsEl.innerHTML='';
  stage.innerHTML='<div class="tsl-eb">'+CONFIG.intro.eyebrow+'</div><h3 class="tsl-h" style="font-size:27px">'+CONFIG.intro.headline+'</h3><p style="color:'+C.ink2+';font-size:14.5px;line-height:1.6;margin:12px 0 0;font-family:'+B.fontBody+'">'+CONFIG.intro.sub+'</p>';
  navEl.innerHTML='<button class="tsl-btn tsl-gold" id="tsl-start">'+CONFIG.intro.cta+' →</button>';
  root.querySelector('#tsl-start').onclick=function(){cur=0;setMeter(true);step();};
}
function tr(i){var a=CONFIG.areas[i];if(a.transitionIf){var t=a.transitionIf;if(sel[t.area]&&sel[t.area].indexOf(t.symptom)>-1)return t.text;}return a.transition;}
function step(){var a=CONFIG.areas[cur];dots(cur,CONFIG.areas.length);var t=tr(cur);
  var h='<div class="tsl-eb"><span style="vertical-align:-2px">'+svg(a.icon,14)+'</span> '+a.eyebrow+' · step '+(cur+1)+' of '+CONFIG.areas.length+'</div><h3 class="tsl-h" style="font-size:23px">'+a.question+'</h3>';
  if(t)h+='<p style="color:'+C.gold+';font-size:13.5px;font-style:italic;margin:9px 0 0">&ldquo;'+t+'&rdquo;</p>';
  h+='<div style="display:flex;flex-direction:column;gap:9px;margin-top:16px">';
  a.symptoms.forEach(function(s,i){var on=sel[cur]&&sel[cur].indexOf(i)>-1;h+='<button class="tsl-tile'+(on?' on':'')+'" data-i="'+i+'"><span class="tsl-k">'+(on?svg("check",14):'')+'</span><span class="tsl-icn">'+svg(a.icon,20)+'</span><span style="flex:1">'+s.label+'</span></button>';});
  h+='</div><p style="color:'+C.ink4+';font-size:11.5px;margin:12px 0 0">Tap any that sound familiar — leave blank if it&rsquo;s handled.</p>';
  stage.innerHTML=h;
  stage.querySelectorAll('.tsl-tile').forEach(function(b){b.onclick=function(){var i=+b.getAttribute('data-i');sel[cur]=sel[cur]||[];var p=sel[cur].indexOf(i);if(p>-1)sel[cur].splice(p,1);else sel[cur].push(i);step();meter();};});
  navEl.innerHTML='<button class="tsl-btn tsl-line" id="tsl-bk">Back</button><button class="tsl-btn tsl-gold" id="tsl-nx">'+(cur<CONFIG.areas.length-1?'Continue':'See my leak report')+' →</button>';
  root.querySelector('#tsl-nx').onclick=function(){if(cur<CONFIG.areas.length-1){cur++;step();}else report();};
  root.querySelector('#tsl-bk').onclick=function(){if(cur>0){cur--;step();}else intro();};
}
function report(){dots(CONFIG.areas.length,CONFIG.areas.length+1);var t=total();var areas=[];
  for(var k in sel){if(sel[k].length){var sub=0;sel[k].forEach(function(i){sub+=CONFIG.areas[k].symptoms[i].monthly;});areas.push([CONFIG.areas[k].eyebrow.replace('&amp;','&'),sub,CONFIG.areas[k].solution]);}}
  areas.sort(function(a,b){return b[1]-a[1];});
  var h='<div class="tsl-eb"><span style="vertical-align:-2px">'+svg("report",14)+'</span> Your leak report</div><h3 class="tsl-h" style="font-size:24px">You&rsquo;re likely leaking <span style="color:'+C.goldBright+'">'+fmt(t)+'/mo</span></h3><p style="color:'+C.ink3+';font-size:13px;margin:6px 0 14px">≈ '+fmt(t*12)+' a year — a rough estimate from your answers.</p>';
  if(areas.length){h+='<div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px">';areas.forEach(function(a){h+='<div style="display:flex;justify-content:space-between;align-items:center;border:1px solid rgba(201,168,106,.15);border-radius:10px;padding:10px 13px"><span style="color:'+C.ink+';font-size:13.5px">'+a[0]+' <span style="color:'+C.ink4+'">→ '+a[2]+'</span></span><span style="color:'+C.goldBright+';font-family:'+B.fontDisplay+';font-size:18px">'+fmt(a[1])+'</span></div>';});h+='</div>';}
  else h+='<p style="color:'+C.ink3+'">Nothing selected yet — most owners have at least a couple. Tap Back and take a look.</p>';
  h+='<div style="border-top:1px solid rgba(201,168,106,.15);padding-top:15px"><p style="color:'+C.ink+';font-size:14px;margin:0 0 2px;font-weight:500">Get your free, no-obligation leak audit</p><p style="color:'+C.ink3+';font-size:12.5px;margin:0 0 6px">We&rsquo;ll turn this into your real numbers — whether you work with us or not.</p><input class="tsl-in" id="tsl-name" placeholder="Your name"><input class="tsl-in" id="tsl-biz" placeholder="Business name"><select class="tsl-in" id="tsl-ind"><option value="">Your industry…</option>'+CONFIG.industries.map(function(x){return '<option>'+x+'</option>';}).join('')+'</select><input class="tsl-in" id="tsl-contact" placeholder="Phone or email"></div>';
  stage.innerHTML=h;
  navEl.innerHTML='<button class="tsl-btn tsl-line" id="tsl-bk">Back</button><button class="tsl-btn tsl-gold" id="tsl-submit">Send my leak report →</button>';
  root.querySelector('#tsl-bk').onclick=function(){cur=CONFIG.areas.length-1;step();};
  root.querySelector('#tsl-submit').onclick=submit;
}
function val(id){var e=root.querySelector('#'+id);return e?e.value:'';}
function submit(){
  var lead={name:val('tsl-name'),business:val('tsl-biz'),industry:val('tsl-ind'),contact:val('tsl-contact'),
    total_monthly:total(),total_annual:total()*12,currency:BE.currency,leaks:[],source:location.href,ts:new Date().toISOString(),quiz:"leak-finder-A"};
  for(var k in sel){if(sel[k].length){lead.leaks.push({area:CONFIG.areas[k].eyebrow.replace('&amp;','&'),solution:CONFIG.areas[k].solution,symptoms:sel[k].map(function(i){return CONFIG.areas[k].symptoms[i].label.replace(/&[a-z]+;/g,"'");}),monthly:sel[k].reduce(function(a,i){return a+CONFIG.areas[k].symptoms[i].monthly;},0)});}}
  var btn=root.querySelector('#tsl-submit');if(btn){btn.textContent='Sending…';btn.disabled=true;}
  var done=false;function finish(){if(done)return;done=true;thanks();}
  try{
    fetch(BE.leadEndpoint,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(lead)})
      .then(function(r){if(!r.ok)throw 0;finish();})
      .catch(function(){ if(BE.leadFallback&&BE.leadFallback.indexOf('FORMSPREE_ID')<0){fetch(BE.leadFallback,{method:"POST",headers:{"Accept":"application/json","Content-Type":"application/json"},body:JSON.stringify(lead)}).then(finish).catch(finish);} else finish(); });
  }catch(e){finish();}
  setTimeout(finish,4000);
}
function thanks(){dotsEl.innerHTML='';navEl.innerHTML='';setMeter(false);
  stage.innerHTML='<div style="text-align:center;padding:14px 6px 6px"><div style="width:54px;height:54px;border-radius:50%;border:1px solid '+C.gold+';display:flex;align-items:center;justify-content:center;margin:0 auto 16px;color:'+C.gold+'">'+svg("check",26)+'</div><h3 class="tsl-h" style="font-size:25px">'+CONFIG.thankYou.title+'</h3><p style="color:'+C.ink2+';font-size:14px;line-height:1.65;margin:12px auto 0;max-width:400px;font-family:'+B.fontBody+'">'+CONFIG.thankYou.body+'</p><p style="color:'+C.ink4+';font-size:12px;margin-top:14px">'+CONFIG.thankYou.note+'</p><button class="tsl-btn tsl-gold" style="margin-top:18px" id="tsl-done">Close</button></div>';
  root.querySelector('#tsl-done').onclick=close;
}
function open(){opened=true;root.classList.add('show');document.documentElement.style.overflow='hidden';var t=document.getElementById('tsleak-tab');if(t)t.style.display='none';if(!stage.innerHTML)intro();}
function close(){opened=false;root.classList.remove('show');document.documentElement.style.overflow='';try{localStorage.setItem('tsleak_dismissed',Date.now());}catch(e){}if(BE.reopen){var t=document.getElementById('tsleak-tab');if(t)t.style.display='block';}}
function arm(){var fired=false;function go(){if(fired)return;fired=true;try{sessionStorage.setItem('tsleak_shown','1');}catch(e){}open();}
  try{var d=+localStorage.getItem('tsleak_dismissed');if(d&&(Date.now()-d)<BE.dismissDays*864e5){if(BE.reopen){var t=document.getElementById('tsleak-tab');if(t)t.style.display='block';}return;}}catch(e){}
  if(BE.oncePerSession){try{if(sessionStorage.getItem('tsleak_shown')){if(BE.reopen){var tb=document.getElementById('tsleak-tab');if(tb)tb.style.display='block';}return;}}catch(e){}}
  if(BE.triggerSeconds!=null)setTimeout(go,BE.triggerSeconds*1000);
  if(BE.scrollPercent)window.addEventListener('scroll',function ons(){var sp=scrollY/(document.body.scrollHeight-innerHeight)*100;if(sp>=BE.scrollPercent){go();window.removeEventListener('scroll',ons);}},{passive:true});
  if(BE.exitIntent)document.addEventListener('mouseout',function(e){if(e.clientY<=0)go();});
}
function suppressed(){var p=location.pathname.split('/').pop();return (BE.suppressPaths||[]).indexOf(p)>-1;}
function init(){if(suppressed())return;css();build();arm();window.TSLeak={open:open,close:close};}
if(document.readyState!=='loading')init();else document.addEventListener('DOMContentLoaded',init);
})();
