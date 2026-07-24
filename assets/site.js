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
