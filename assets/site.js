/* ============================================================
   TOP SHELF — shared site behavior (all pages)
   1) Reveal + count-up motion (GSAP)  2) Gold-dust background
   Requires GSAP + ScrollTrigger loaded before this file.
   Reveal elements are VISIBLE by default (CSS); JS animates FROM hidden.
   ============================================================ */
(function () {
  var nav = document.getElementById('nav');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasGSAP = window.gsap && window.ScrollTrigger;

  function setNav() {
    if (!nav) return;
    if ((window.scrollY || 0) > 24) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }

  /* Count-up: final values are the DOM default; failsafe guarantees them. */
  function forceCounts() {
    document.querySelectorAll('[data-count]').forEach(function (el) {
      var pre = el.getAttribute('data-prefix') || '';
      var suf = el.getAttribute('data-suffix') || '';
      el.textContent = pre + el.getAttribute('data-count') + suf;
    });
  }
  var countFailsafe = setTimeout(forceCounts, 2400);

  var ROW_SEL = '.rowitem, .index-item, .feature-row';

  if (reduce || !hasGSAP) {
    clearTimeout(countFailsafe);
    setNav();
    window.addEventListener('scroll', setNav, { passive: true });
    // Motion allowed but no GSAP: still enable the hover-slide on rows.
    if (!reduce) document.querySelectorAll(ROW_SEL).forEach(function (el) { el.classList.add('is-ready'); });
    return;
  }

  document.documentElement.classList.add('js-motion');
  gsap.registerPlugin(ScrollTrigger);
  ScrollTrigger.create({ start: 0, end: 99999, onUpdate: setNav });

  var EASE = 'power3.out';

  /* On-load reveal for whichever hero this page has */
  var heroSel = document.querySelector('.hero') ? '.hero .reveal' : '.page-hero .reveal';
  var heroReveals = gsap.utils.toArray(heroSel);
  if (heroReveals.length) {
    gsap.to(heroReveals, { opacity: 1, y: 0, duration: 1.15, ease: EASE, stagger: 0.11, delay: 0.15 });
  }

  /* Count-up (rolls 0 -> final). Hero stats fire on load; any other
     [data-count] fires when scrolled into view. */
  function countUp(el) {
    if (el._counted) return; el._counted = true;
    var target = parseFloat(el.getAttribute('data-count'));
    var pre = el.getAttribute('data-prefix') || '';
    var suf = el.getAttribute('data-suffix') || '';
    var obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 1.6, ease: 'power2.out',
      onUpdate: function () { el.textContent = pre + Math.round(obj.v) + suf; },
      onComplete: function () { el.textContent = pre + target + suf; }
    });
  }
  var heroCounts = gsap.utils.toArray('.hero [data-count], .page-hero [data-count]');
  if (heroCounts.length) {
    gsap.delayedCall(0.7, function () { heroCounts.forEach(countUp); });
  }
  gsap.utils.toArray('[data-count]').forEach(function (el) {
    if (el.closest('.hero') || el.closest('.page-hero')) return;
    ScrollTrigger.create({ trigger: el, start: 'top 90%', once: true, onEnter: function () { countUp(el); } });
  });

  /* Scroll-in reveals for everything outside the hero */
  gsap.utils.toArray('.reveal').forEach(function (el) {
    if (el.closest('.hero') || el.closest('.page-hero')) return;
    var isRow = el.matches(ROW_SEL);
    gsap.to(el, {
      opacity: 1, y: 0, duration: 0.95, ease: EASE,
      scrollTrigger: { trigger: el, start: 'top 88%', once: true },
      onComplete: function () { if (isRow) el.classList.add('is-ready'); }
    });
  });

  /* Safety: force any still-hidden reveal visible after load */
  window.addEventListener('load', function () {
    setTimeout(function () {
      gsap.utils.toArray('.reveal').forEach(function (el) {
        if (getComputedStyle(el).opacity === '0') gsap.set(el, { opacity: 1, y: 0 });
      });
      document.querySelectorAll(ROW_SEL).forEach(function (el) { el.classList.add('is-ready'); });
      ScrollTrigger.refresh();
    }, 1400);
  });
})();

/* ==================== GOLD DUST BACKGROUND ==================== */
(function () {
  var canvas = document.getElementById('gold-dust-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var DPR = Math.min(window.devicePixelRatio || 1, 1.5);
  var W = 0, H = 0, particles = [], rafId = null, running = false, scrollY = 0;
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var GOLDS = [{ r: 201, g: 168, b: 106 }, { r: 228, g: 201, b: 138 }];

  function particleCount() {
    var area = window.innerWidth * window.innerHeight;
    var n = Math.round(area / (2560 * 1440) * 100);
    return Math.max(40, Math.min(80, n));
  }
  function makeParticle(randomY) {
    var depth = Math.pow(Math.random(), 1.6);
    var isGlow = depth > 0.82 && Math.random() < 0.5;
    var col = GOLDS[Math.random() < 0.65 ? 0 : 1];
    return {
      x: Math.random() * W, y: randomY ? Math.random() * H : H + 10 * DPR,
      depth: depth, layer: depth > 0.5 ? 1 : 0,
      r: (isGlow ? (1.6 + Math.random() * 0.9) : (0.5 + depth * 1.3)) * DPR, glow: isGlow, col: col,
      vy: -(0.04 + depth * 0.10) * DPR, vx: (0.008 + depth * 0.028) * DPR * (Math.random() < 0.75 ? 1 : -1),
      wanderPhase: Math.random() * Math.PI * 2, wanderSpeed: 0.0018 + Math.random() * 0.0022, wanderAmp: (0.015 + Math.random() * 0.03) * DPR,
      baseA: 0.10 + Math.random() * 0.13, ampA: 0.05 + Math.random() * 0.09, twPhase: Math.random() * Math.PI * 2, twSpeed: 0.0035 + Math.random() * 0.0055
    };
  }
  function resize() {
    W = Math.round(window.innerWidth * DPR); H = Math.round(window.innerHeight * DPR);
    canvas.width = W; canvas.height = H; seed(); if (reduceMotion) drawFrame(0);
  }
  function seed() { particles = []; var n = particleCount(); for (var i = 0; i < n; i++) particles.push(makeParticle(true)); }
  function drawFrame(t) {
    ctx.clearRect(0, 0, W, H);
    var par0 = -(scrollY * 0.012) * DPR, par1 = -(scrollY * 0.028) * DPR;
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      var a = p.baseA + p.ampA * Math.sin(t * p.twSpeed + p.twPhase);
      if (a < 0.03) continue; a = Math.min(a, 0.35);
      var py = p.y + (p.layer === 1 ? par1 : par0); py = ((py % H) + H) % H;
      var c = p.col;
      if (p.glow) {
        var g = ctx.createRadialGradient(p.x, py, 0, p.x, py, p.r * 3.2);
        g.addColorStop(0, 'rgba(' + c.r + ',' + c.g + ',' + c.b + ',' + a.toFixed(3) + ')');
        g.addColorStop(0.45, 'rgba(' + c.r + ',' + c.g + ',' + c.b + ',' + (a * 0.35).toFixed(3) + ')');
        g.addColorStop(1, 'rgba(' + c.r + ',' + c.g + ',' + c.b + ',0)');
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, py, p.r * 3.2, 0, Math.PI * 2); ctx.fill();
      } else {
        ctx.fillStyle = 'rgba(' + c.r + ',' + c.g + ',' + c.b + ',' + a.toFixed(3) + ')';
        ctx.beginPath(); ctx.arc(p.x, py, p.r, 0, Math.PI * 2); ctx.fill();
      }
    }
  }
  function step(t) {
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.y += p.vy; p.x += p.vx + Math.sin(t * p.wanderSpeed + p.wanderPhase) * p.wanderAmp;
      if (p.y < -12 * DPR) { particles[i] = makeParticle(false); particles[i].x = Math.random() * W; }
      else { if (p.x < -12 * DPR) p.x = W + 10 * DPR; else if (p.x > W + 12 * DPR) p.x = -10 * DPR; }
    }
    drawFrame(t); if (running) rafId = requestAnimationFrame(step);
  }
  function start() { if (running || reduceMotion) return; running = true; rafId = requestAnimationFrame(step); }
  function stop() { running = false; if (rafId) { cancelAnimationFrame(rafId); rafId = null; } }
  window.addEventListener('resize', resize, { passive: true });
  window.addEventListener('scroll', function () { scrollY = window.scrollY || 0; }, { passive: true });
  document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else start(); });
  resize(); if (reduceMotion) drawFrame(0); else start();
})();

/* ==================== MOBILE MENU ==================== */
(function () {
  var nav = document.getElementById('nav');
  if (!nav) return;
  var btn = nav.querySelector('.nav-menu-btn');
  var links = nav.querySelector('.nav-links');
  if (!btn || !links) return;

  // Build the panel from the existing nav so it stays in sync with every page.
  var panel = document.createElement('div');
  panel.className = 'mobile-menu';
  panel.setAttribute('aria-hidden', 'true');
  links.querySelectorAll(':scope > .nav-item, :scope > .nav-link').forEach(function (node) {
    if (node.classList.contains('nav-item')) {
      var head = node.querySelector('.nav-link');
      var title = document.createElement('p');
      title.className = 'mm-group-title';
      title.textContent = (head ? head.textContent : '').replace(/[▾▼]/g, '').trim();
      panel.appendChild(title);
      node.querySelectorAll('.nav-dropdown a').forEach(function (a) {
        var c = a.cloneNode(true); c.className = 'mm-sub'; panel.appendChild(c);
      });
    } else {
      var c = node.cloneNode(true); c.className = 'mm-lead'; panel.appendChild(c);
    }
  });
  var cta = nav.querySelector('.nav-cta .btn');
  if (cta) { var cc = cta.cloneNode(true); cc.className = 'btn btn-gold'; panel.appendChild(cc); }
  document.body.appendChild(panel);

  function setOpen(open) {
    panel.classList.toggle('open', open);
    document.body.classList.toggle('mm-open', open);
    panel.setAttribute('aria-hidden', open ? 'false' : 'true');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    btn.textContent = open ? 'Close' : 'Menu';
  }
  btn.addEventListener('click', function (e) { e.preventDefault(); setOpen(!panel.classList.contains('open')); });
  panel.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
  window.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  // Close automatically if resized up to desktop
  window.matchMedia('(min-width: 861px)').addEventListener('change', function (e) { if (e.matches) setOpen(false); });
})();

/* ===== Website assistant (concierge) — shell (markup + open/close) ===== */
(function () {
  if (document.getElementById('tsChatFab')) return;
  var fab = document.createElement('button');
  fab.className = 'tsc-fab'; fab.id = 'tsChatFab'; fab.setAttribute('aria-label', 'Chat with Top Shelf');
  fab.innerHTML = '<svg viewBox="0 0 24 24" width="26" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-8.5 8.5 8.5 8.5 0 0 1-3.8-.9L3 21l1.9-5.7A8.5 8.5 0 1 1 21 11.5z"/></svg>';
  var panel = document.createElement('section');
  panel.className = 'tsc-panel'; panel.id = 'tsChatPanel'; panel.setAttribute('aria-label', 'Top Shelf assistant');
  panel.innerHTML =
    '<div class="tsc-head"><div class="tsc-av"><svg viewBox="0 0 24 24" width="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2 3 7l9 5 9-5-9-5zM3 12l9 5 9-5M3 17l9 5 9-5"/></svg></div>'
    + '<div><b>Top Shelf Concierge</b><span>Typically replies instantly</span></div>'
    + '<button type="button" aria-label="Close">×</button></div>'
    + '<div class="tsc-body"></div>'
    + '<div class="tsc-quick"></div>'
    + '<form class="tsc-foot"><input type="text" placeholder="Ask about our services…" aria-label="Message" autocomplete="off"><button type="submit">Send</button></form>';
  document.body.appendChild(fab); document.body.appendChild(panel);

  var greeted = false;
  var api = {
    open: function () {
      panel.classList.add('open'); fab.style.display = 'none';
      if (!greeted && window.__tsChatGreet) { greeted = true; window.__tsChatGreet(); }
      setTimeout(function () { var i = panel.querySelector('.tsc-foot input'); if (i) i.focus(); }, 250);
    },
    close: function () { panel.classList.remove('open'); fab.style.display = 'grid'; }
  };
  fab.addEventListener('click', api.open);
  panel.querySelector('.tsc-head button').addEventListener('click', api.close);
  document.querySelectorAll('[data-open-chat]').forEach(function (el) {
    el.addEventListener('click', function (e) { e.preventDefault(); api.open(); });
  });
  window.__tsChat = api;
})();

/* ===== Website assistant — retrieval engine ===== */
(function () {
  var panel = document.getElementById('tsChatPanel');
  if (!panel) return;
  var body = panel.querySelector('.tsc-body');
  var quick = panel.querySelector('.tsc-quick');
  var form = panel.querySelector('.tsc-foot');
  var input = form.querySelector('input');

  var VAULT = { services: [], sections: [] };
  fetch('assets/services-vault.json').then(function (r) { return r.json(); })
    .then(function (d) { VAULT = d; }).catch(function () {});

  var STOP = ' the a an and or for of to your you with we our is are on in do does can ';
  function score(text, keywords) {
    var t = ' ' + text.toLowerCase() + ' ', s = 0;
    keywords.forEach(function (k) { if (t.indexOf(k) !== -1) s += k.length; });
    return s;
  }

  // Site-level intents (checked before the vault)
  var INTENTS = [
    { k: ['hello','hi','hey','help','start'], a: function () { return "Hi! I'm the Top Shelf concierge. I can walk you through what we do — websites, marketing, CRM, AI phone answering, payments and a lot more — and help you get a free audit. What kind of business do you run?"; } },
    { k: ['price','pricing','cost','how much','quote','rate','fee','afford','budget'], a: function () { return "Every business is different, so we don't do one-size-fits-all pricing — we run a quick <strong>free audit</strong> of your business and build you a custom plan that fits. Want me to set that up? I'll just grab your details."; } },
    { k: ['who are you','what is top shelf','about','why you','why top shelf','trust'], a: function () { return "Top Shelf Business Solutions is your all-in-one growth partner — we handle the tech and marketing that get you more customers, so you can run your business. We tailor everything to your trade and you keep what we build for you."; } },
    { k: ['how does it work','how it works','process','get started','start','next step'], a: function () { return "Simple: we do a free audit of where you're losing customers, show you exactly what we'd fix, and build a custom plan — no guesswork. Want me to get you on the list for an audit?"; } },
    { k: ['contact','talk','human','call','phone','reach','speak','email'], a: function () { return "Happy to connect you with a real person. Drop your info and we'll reach out fast — what's your name?"; } },
    { k: ['services','what do you offer','what do you do','offerings','list','everything'], a: function () { return "We cover a lot — grouped into: " + (VAULT.sections.join(', ') || 'web presence, marketing, CRM, phone & communications, payments, and more') + ". Which area is on your mind? Or tell me your biggest headache and I'll point you to the fix."; } },
  ];

  function findAnswer(text) {
    var best = null, bs = 0;
    INTENTS.forEach(function (it) { var s = score(text, it.k); if (s > bs) { bs = s; best = { a: it.a(), cta: /audit|reach out|on the list|your name|your details/i.test(it.a()) }; } });
    VAULT.services.forEach(function (sv) {
      var s = score(text, sv.keywords) + score(text, [sv.name.toLowerCase()]) * 1.5;
      if (s > bs) { bs = s; best = { a: '<strong>' + sv.name + '.</strong> ' + sv.blurb + (sv.great_for ? ' <em>Great for ' + sv.great_for + '.</em>' : '') + ' Want a free audit to see what this looks like for your business?', cta: true }; }
    });
    if (!best) return { a: "Great question — the fastest way to a solid answer is a quick free audit tailored to your business. Want me to grab your info so a Top Shelf specialist can follow up?", cta: true };
    return best;
  }

  function el(html, cls) { var d = document.createElement('div'); d.className = cls; d.innerHTML = html; body.appendChild(d); body.scrollTop = body.scrollHeight; return d; }
  function botTyping() { return el('<div class="tsc-typing"><span></span><span></span><span></span></div>', 'tsc-msg tsc-msg--bot'); }
  function botReply(html, delay) { var t = botTyping(); setTimeout(function () { t.innerHTML = html; body.scrollTop = body.scrollHeight; }, delay || 650); }
  function userMsg(text) { el(escapeHtml(text), 'tsc-msg tsc-msg--user'); }
  function escapeHtml(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  window.__tsChatBotReply = botReply; window.__tsChatUserMsg = userMsg; window.__tsChatEscape = escapeHtml;

  window.__tsChatGreet = function () {
    botReply("Hi! I'm the <strong>Top Shelf concierge</strong>. Ask me anything about how we help businesses grow — or tell me your trade and I'll point you to the right fix. 👋", 400);
    setQuick(['What do you offer?', 'Help me get more customers', 'Book a free audit']);
  };

  function setQuick(items) {
    quick.innerHTML = '';
    items.forEach(function (label) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = label;
      b.addEventListener('click', function () { handle(label); });
      quick.appendChild(b);
    });
  }
  window.__tsChatSetQuick = setQuick;

  // Base responder — Task 5 wraps this to add lead capture.
  window.__tsChatRespond = function (text) {
    var res = findAnswer(text);
    botReply(res.a, 700);
    return res; // { a, cta }
  };

  function handle(text) {
    if (!text || !text.trim()) return;
    userMsg(text);
    (window.__tsChatHandle || window.__tsChatRespond)(text);
  }
  window.__tsChatHandleInput = handle;

  form.addEventListener('submit', function (e) { e.preventDefault(); var v = input.value; input.value = ''; handle(v); });
})();

/* ===== Website assistant — lead capture + submit ===== */
(function () {
  if (!window.__tsChatRespond) return;
  var LEAD_ENDPOINT = 'https://top-shelf-production.up.railway.app/api/website-lead';
  var FORMSPREE = 'https://formspree.io/f/FORMSPREE_ID'; // fallback (same id as the contact form)
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  var PHONE_RE = /(\d[\s\-().]*){10,}/;

  var lead = { active: false, step: 0, name: '', business: '', contact: '', need: '' };

  function ask(q, delay) { window.__tsChatBotReply(q, delay || 450); }

  function start(need) {
    lead = { active: true, step: 1, name: '', business: '', contact: '', need: need || '' };
    window.__tsChatSetQuick([]);
    ask("Love it — let's get you a free audit. First, what's your name?");
  }
  window.__tsChatStartCapture = start;

  function submit() {
    var payload = { name: lead.name, business: lead.business, need: lead.need, page: location.href };
    if (EMAIL_RE.test(lead.contact)) payload.email = lead.contact; else payload.phone = lead.contact;
    var done = function () {
      ask("You're all set, " + window.__tsChatEscape(lead.name.split(' ')[0]) + "! ✅ A Top Shelf specialist will reach out shortly about your free audit. Prefer email? <a href='mailto:contact@topshelfsolutions.io'>contact@topshelfsolutions.io</a>.", 500);
      lead.active = false;
    };
    fetch(LEAD_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { if (!r.ok) throw new Error('bad'); return r.json(); })
      .then(done)
      .catch(function () {
        // Fallback so a lead is never lost.
        fetch(FORMSPREE, { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
          .then(done).catch(done);
      });
  }

  function step(text) {
    if (lead.step === 1) { lead.name = text.trim(); lead.step = 2; ask("Thanks, " + window.__tsChatEscape(lead.name.split(' ')[0]) + "! What's your business or trade?"); return; }
    if (lead.step === 2) { lead.business = text.trim(); lead.step = 3; ask("Got it. What's the best email or phone to reach you?"); return; }
    if (lead.step === 3) {
      if (!EMAIL_RE.test(text) && !PHONE_RE.test(text)) { ask("Hmm, that doesn't look like an email or a full phone number — mind sending one so we can reach you?"); return; }
      lead.contact = text.trim(); lead.step = 4;
      ask("Perfect. Anything specific you're hoping to fix or grow? (Optional — you can say 'not sure'.)"); return;
    }
    if (lead.step === 4) { if (!lead.need) lead.need = text.trim(); lead.step = 0; submit(); return; }
  }

  var wantsCapture = /(call me|reach out|contact me|leave|my (name|number|info)|get (an )?audit|book|sign me up|yes|get started|interested)/i;

  window.__tsChatHandle = function (text) {
    if (lead.active) { step(text); return; }
    var res = window.__tsChatRespond(text); // renders the answer
    if (res && (res.cta || wantsCapture.test(text))) { setTimeout(function () { if (!lead.active) start(text); }, 1500); }
  };
})();
