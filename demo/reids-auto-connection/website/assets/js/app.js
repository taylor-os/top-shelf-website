/* =========================================================================
   Reids Auto Connection — Aurora v2 interactions
   1. Header condensation  2. Reveal  3. Mobile nav  4. Chatbot "Dawn"
   ========================================================================= */
(function () {
  "use strict";
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Header condensation ---------- */
  var hdr = document.getElementById('hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('scrolled', window.scrollY > 12); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------- Mobile nav ---------- */
  var nav = document.querySelector('.nav');
  var burger = document.querySelector('.hamburger');
  if (nav && burger) {
    burger.addEventListener('click', function () { nav.classList.toggle('menu-open'); });
    nav.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { nav.classList.remove('menu-open'); });
    });
  }

  /* ---------- Reveal on scroll ---------- */
  var items = document.querySelectorAll('.reveal:not(.in)');
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });
    items.forEach(function (el) { io.observe(el); });
  }

  /* =======================================================================
     CHATBOT — "Dawn", the Reids Auto assistant (client-side retrieval + lead capture)
     ======================================================================= */
  var PHONE = "(972) 436-1600", PHONE_TEL = "9724361600";
  var KB = [
    { k: ["bankrupt","chapter 7","chapter 13","ch 7","ch 13","bk"], a: "Yes — helping people in Chapter 7 and Chapter 13 bankruptcy is our specialty. Our Fresh Start Vehicle Program is built for it, and we can often get you approved even during an active bankruptcy. Want me to have someone reach out to check your options?" },
    { k: ["bad credit","no credit","poor credit","low credit","credit score","repo","repossession","first time","first-time"], a: "Absolutely. We work with bad credit, no credit, first-time buyers, and past repossessions every day — it's who we're here for. There's no judgment, and approvals are often within an hour. Should I get someone to call you about approval?" },
    { k: ["down","down payment","money down","0 down","$0"], a: "Most of our loans are $0 down (that excludes tax, title & license). We'll always try to get you into a vehicle with the lowest out-of-pocket possible." },
    { k: ["approve","approval","qualify","pre-approv","prequal","get approved","financing","finance","loan"], a: "Getting pre-approved is quick and won't obligate you to anything. Most folks hear back within about an hour. I can start it for you right now — want to leave your name and number?" },
    { k: ["inventory","cars","vehicles","what do you have","in stock","selection","suv","truck"], a: "We carry late-model, low-mileage 2020–2025 cars, trucks, SUVs and vans across all makes. Our cars move fast, so the best way to see what fits your budget is a quick call — want someone to reach out with current options?" },
    { k: ["hours","open","close","when are you","today"], a: "We're open Mon–Sat 10am–7pm, and closed Sundays. We work by appointment so you get our full attention — I can help you set one up." },
    { k: ["where","location","address","directions","map","service area"], a: "Everything happens by phone and online, and we approve buyers nationwide. Out of the area? Ask me about our fly-in program." },
    { k: ["fly","flight","out of state","out of area","airport","southwest"], a: "Yes! For out-of-area buyers we can arrange a flight with courtesy pickup. We approve buyers nationwide." },
    { k: ["trade","trade-in","trade in","my car","current vehicle"], a: "We take trade-ins — even if you're in Chapter 7 or 13, you can often trade your current vehicle toward another. Tell me the year, make and model and I'll pass it along for a value." },
    { k: ["bring","documents","need","paperwork","requirements","what do i need"], a: "Usually just a valid ID, proof of income, and proof of residence — we'll walk you through anything else. Want me to text you the full checklist?" },
    { k: ["veteran","military","va","service"], a: "We're proudly veteran-owned and love working with military and veteran buyers. Thank you for your service — let's get you approved." },
    { k: ["price","cost","payment","monthly","how much","afford"], a: "Payments depend on the vehicle and your situation, but we specialize in fitting the payment to your budget. The fastest way to a real number is a quick pre-approval — want to start one?" },
    { k: ["review","reviews","rating","reputation","legit","scam","trust"], a: "We're rated 4.7★ across 200+ Google reviews and BBB A+ accredited since 2009. Customers most often mention fast approvals, fair pricing, and being treated with respect." },
    { k: ["hello","hi","hey","help","start"], a: "Hi there! I'm Dawn, the Reids Auto assistant. I can help with financing after bankruptcy, bad credit, $0 down, our cars, hours, or getting pre-approved. What brings you in today?" },
    { k: ["thank","thanks"], a: "You're very welcome! Anything else I can help you with, or would you like someone to reach out?" }
  ];
  var FALLBACK = "Good question — the quickest way to a solid answer is to talk to our team. Want to leave your name and number, or you can call us at " + PHONE + "?";

  function findAnswer(text) {
    var t = " " + text.toLowerCase() + " ", best = null, bestScore = 0;
    KB.forEach(function (e) { var s = 0; e.k.forEach(function (kw) { if (t.indexOf(kw) !== -1) s += kw.length; }); if (s > bestScore) { bestScore = s; best = e; } });
    return best ? best.a : FALLBACK;
  }

  var fab = document.getElementById('chatFab');
  var panel = document.getElementById('chatPanel');
  if (!fab || !panel) return;
  var body = panel.querySelector('.chat-body');
  var quick = panel.querySelector('.chat-quick');
  var form = panel.querySelector('.chat-foot');
  var input = form.querySelector('input');
  var lead = { name: null, phone: null, capturing: false, step: 0, greeted: false };

  function scrollDown() { body.scrollTop = body.scrollHeight; }
  function addMsg(text, who) { var d = document.createElement('div'); d.className = 'msg msg--' + who; d.innerHTML = text; body.appendChild(d); scrollDown(); return d; }
  function botTyping() { var d = document.createElement('div'); d.className = 'msg msg--bot'; d.innerHTML = '<div class="typing"><span></span><span></span><span></span></div>'; body.appendChild(d); scrollDown(); return d; }
  function botReply(text, delay) { var t = botTyping(); setTimeout(function () { t.innerHTML = text; scrollDown(); }, delay || 650); }
  function escapeHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

  function openChat() {
    panel.classList.add('open'); fab.style.display = 'none';
    if (!lead.greeted) { lead.greeted = true; botReply("Hi! I'm <strong>Dawn</strong>, the Reids Auto assistant 🌅 I help folks get approved — even after bankruptcy or with bad credit. How can I help?", 400); }
    setTimeout(function () { input.focus(); }, 300);
  }
  function closeChat() { panel.classList.remove('open'); fab.style.display = 'grid'; }
  fab.addEventListener('click', openChat);
  panel.querySelector('.chat-head button').addEventListener('click', closeChat);

  var PHONE_RE = /(\d[\s\-().]*){10,}/;
  function handleLeadStep(text) {
    if (lead.step === 1) { lead.name = text.trim(); lead.step = 2; botReply("Thanks, " + escapeHtml(lead.name.split(' ')[0]) + "! What's the best phone number to reach you?", 500); return true; }
    if (lead.step === 2) {
      if (!PHONE_RE.test(text)) { botReply("Hmm, that doesn't look like a full phone number — mind sending 10 digits so we can reach you?", 400); return true; }
      lead.phone = text.trim(); lead.step = 0; lead.capturing = false;
      botReply("You're all set, " + escapeHtml(lead.name.split(' ')[0]) + "! ✅ Someone from our team will reach out shortly to get you approved. In a hurry? Call <a href='tel:" + PHONE_TEL + "'>" + PHONE + "</a>.", 600);
      console.log("[LEAD CAPTURED]", { name: lead.name, phone: lead.phone }); return true;
    }
    return false;
  }
  function startCapture() { lead.capturing = true; lead.step = 1; botReply("Happy to help with that! First — what's your name?", 450); }
  function respond(text) {
    if (lead.capturing) { if (handleLeadStep(text)) return; }
    var wantsContact = /(call me|reach out|contact me|leave|my (name|number)|get approved|sign me up|yes)/i.test(text) && !lead.capturing;
    var ans = findAnswer(text);
    botReply(ans, 700);
    if (/want me to|want to leave|reach out|start one|set (one|it) up|pass it along|text you/i.test(ans) || wantsContact) { setTimeout(startCapture, 1500); }
  }
  function send(text) { if (!text.trim()) return; addMsg(escapeHtml(text), 'user'); respond(text); }
  form.addEventListener('submit', function (e) { e.preventDefault(); var v = input.value; input.value = ''; send(v); });
  if (quick) { quick.querySelectorAll('button').forEach(function (b) { b.addEventListener('click', function () { send(b.textContent); }); }); }
  document.querySelectorAll('[data-open-chat]').forEach(function (el) { el.addEventListener('click', function (e) { e.preventDefault(); openChat(); }); });
})();
