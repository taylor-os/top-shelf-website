/* Scrubz Carpet Care — site behavior. Vanilla, no dependencies. */
(() => {
  window.scrubzReady = true; /* tells the inline failsafe in <head> that reveals will run */
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  /* film grain: one small random-noise tile, generated once */
  try {
    const g = document.createElement('canvas'); g.width = g.height = 128;
    const gx = g.getContext('2d'), px = gx.createImageData(128, 128);
    for (let i = 0; i < px.data.length; i += 4) {
      const v = Math.random() * 255; px.data[i] = px.data[i + 1] = px.data[i + 2] = v; px.data[i + 3] = 255;
    }
    gx.putImageData(px, 0, 0);
    document.body.style.setProperty('--grain', `url(${g.toDataURL()})`);
  } catch (e) { /* grain is decoration only */ }

  /* header: transparent over the hero, solid once you scroll */
  const hdr = $('.hdr');
  const onScroll = () => hdr && hdr.classList.toggle('solid', scrollY > 24);
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  /* mobile menu */
  const menuBtn = $('.menu-btn');
  if (menuBtn) {
    const setMenu = open => {
      document.body.classList.toggle('menu-open', open);
      menuBtn.setAttribute('aria-expanded', open);
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    menuBtn.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
    $$('.nav a').forEach(a => a.addEventListener('click', () => setMenu(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
    matchMedia('(min-width: 961px)').addEventListener('change', e => e.matches && setMenu(false));
  }

  /* scroll reveals + count-ups */
  const counters = $$('[data-count]');
  if (!reduce) counters.forEach(el => { el.textContent = el.dataset.from || '0'; });
  const countUp = el => {
    const to = +el.dataset.count, from = +(el.dataset.from || 0), dur = 1600, t0 = performance.now();
    const tick = t => {
      const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(2, -10 * p);
      el.textContent = Math.round(from + (to - from) * (p === 1 ? 1 : e));
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      if (en.target.dataset.count && !reduce) countUp(en.target);
      io.unobserve(en.target);
    }), { rootMargin: '0px 0px -8% 0px', threshold: .12 });
    $$('[data-reveal]').forEach(el => io.observe(el));
    counters.forEach(el => io.observe(el));
  } else {
    $$('[data-reveal]').forEach(el => el.classList.add('in'));
  }

  /* gentle parallax on hero photos (transform only) */
  const par = $$('.hero-media, .phero-media');
  if (par.length && !reduce) {
    let ticking = false;
    const move = () => {
      const y = scrollY;
      if (y < innerHeight * 1.3) par.forEach(el => { el.style.transform = `translate3d(0, ${y * .28}px, 0)`; });
      ticking = false;
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(move); } }, { passive: true });
  }

  /* ---------- floating soap bubbles (the signature) ---------- */
  const makeSprite = red => {
    const c = document.createElement('canvas'), S = 128, R = 60, x = c.getContext('2d');
    c.width = c.height = S;
    const g = x.createRadialGradient(S * .42, S * .38, R * .1, S / 2, S / 2, R);
    const rim = red ? '235,70,60' : '255,255,255';
    g.addColorStop(0, `rgba(${rim},0)`);
    g.addColorStop(.72, `rgba(${rim},.03)`);
    g.addColorStop(.94, `rgba(${rim},${red ? .32 : .2})`);
    g.addColorStop(1, `rgba(${rim},0)`);
    x.fillStyle = g; x.beginPath(); x.arc(S / 2, S / 2, R, 0, Math.PI * 2); x.fill();
    x.lineWidth = 1.4; x.strokeStyle = `rgba(${rim},${red ? .7 : .5})`;
    x.beginPath(); x.arc(S / 2, S / 2, R - 1, 0, Math.PI * 2); x.stroke();
    x.lineWidth = 3; x.strokeStyle = red ? 'rgba(255,120,90,.55)' : 'rgba(255,90,70,.4)';
    x.beginPath(); x.arc(S / 2, S / 2, R - 4, Math.PI * .1, Math.PI * .65); x.stroke();
    const h = x.createRadialGradient(S * .34, S * .3, 0, S * .34, S * .3, R * .32);
    h.addColorStop(0, 'rgba(255,255,255,.9)'); h.addColorStop(1, 'rgba(255,255,255,0)');
    x.fillStyle = h; x.beginPath(); x.arc(S * .34, S * .3, R * .32, 0, Math.PI * 2); x.fill();
    return c;
  };
  let sprites;
  const runBubbles = canvas => {
    sprites = sprites || [makeSprite(false), makeSprite(true)];
    const host = canvas.parentElement, ctx = canvas.getContext('2d');
    const density = +canvas.dataset.bubbles || 1;
    let W = 0, H = 0, list = [], pops = [], raf = 0, last = 0, on = false;
    const spawn = initial => {
      const r = 4 + Math.pow(Math.random(), 2.2) * 34;
      return {
        r, x: Math.random() * W, y: initial ? Math.random() * H : H + r + Math.random() * 60,
        vy: .25 + Math.random() * .55 + r * .006, amp: 6 + Math.random() * 18,
        ph: Math.random() * 6.28, ws: .008 + Math.random() * .014,
        t: Math.random() < .45 ? 1 : 0, a: .45 + Math.random() * .5
      };
    };
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      for (const b of list) {
        ctx.globalAlpha = b.a;
        ctx.drawImage(sprites[b.t], b.x + Math.sin(b.ph) * b.amp - b.r, b.y - b.r, b.r * 2, b.r * 2);
      }
      for (const p of pops) {
        const k = 1 - p.life, rr = p.r * (1 + k * .7);
        ctx.globalAlpha = p.life * .8;
        ctx.strokeStyle = p.t ? 'rgb(255,110,90)' : '#fff'; ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(p.x, p.y, rr, 0, Math.PI * 2); ctx.stroke();
        ctx.fillStyle = ctx.strokeStyle;
        for (let i = 0; i < 7; i++) {
          const ang = i / 7 * 6.28 + p.r, d = p.r * (1 + k * 1.5);
          ctx.beginPath(); ctx.arc(p.x + Math.cos(ang) * d, p.y + Math.sin(ang) * d, 1.6, 0, 6.28); ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
    };
    const step = t => {
      const dt = Math.min(50, t - (last || t)) / 16.67; last = t;
      for (let i = 0; i < list.length; i++) {
        const b = list[i];
        b.y -= b.vy * dt; b.ph += b.ws * dt;
        if (b.y < -b.r - 20) list[i] = spawn(false);
      }
      for (const p of pops) p.life -= .045 * dt;
      pops = pops.filter(p => p.life > 0);
      draw();
      raf = requestAnimationFrame(step);
    };
    const start = () => { if (!on && !reduce) { on = true; last = 0; raf = requestAnimationFrame(step); } };
    const stop = () => { on = false; cancelAnimationFrame(raf); };
    const resize = () => {
      const dpr = Math.min(devicePixelRatio || 1, 2), r = host.getBoundingClientRect();
      W = r.width; H = r.height;
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const n = Math.round(Math.min(56, (W * H) / 26000 * density));
      while (list.length < n) list.push(spawn(true));
      list.length = n;
      draw();
    };
    resize();
    new ResizeObserver(resize).observe(host);
    let inView = false;
    new IntersectionObserver(([en]) => { inView = en.isIntersecting; inView ? start() : stop(); }).observe(host);
    document.addEventListener('visibilitychange', () => document.hidden ? stop() : inView && start());
    if (reduce) return;
    /* pop bubbles with the pointer: customers love the bubbles */
    const popAt = (cx, cy, reach) => {
      const r = canvas.getBoundingClientRect(), px = cx - r.left, py = cy - r.top;
      list.forEach((b, i) => {
        const bx = b.x + Math.sin(b.ph) * b.amp;
        if (b.r > 7 && Math.hypot(bx - px, b.y - py) < b.r + reach) {
          pops.push({ x: bx, y: b.y, r: b.r, life: 1, t: b.t });
          list[i] = spawn(false);
        }
      });
    };
    host.addEventListener('pointermove', e => e.pointerType === 'mouse' && popAt(e.clientX, e.clientY, 4), { passive: true });
    host.addEventListener('pointerdown', e => popAt(e.clientX, e.clientY, 18), { passive: true });
  };
  $$('canvas.bubbles').forEach(runBubbles);

  /* review rails: prev / next buttons */
  $$('[data-rail]').forEach(btn => btn.addEventListener('click', () => {
    const rail = document.getElementById(btn.getAttribute('aria-controls'));
    rail.scrollBy({ left: (btn.dataset.rail === 'next' ? 1 : -1) * rail.clientWidth * .85, behavior: reduce ? 'auto' : 'smooth' });
  }));

  /* ---------- gallery: filters + lightbox ---------- */
  const grid = $('.g-grid');
  if (grid) {
    const items = $$('.g-item', grid);
    const btns = $$('.filters button');
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.setAttribute('aria-pressed', x === b));
      const f = b.dataset.filter;
      items.forEach(it => { it.hidden = f !== 'all' && it.dataset.cat !== f; });
    }));

    const lb = $('#lb');
    if (lb && lb.showModal) {
      const img = $('img', lb), cap = $('.lb-cap', lb), count = $('.lb-count', lb);
      let vis = [], idx = 0;
      const show = i => {
        idx = (i + vis.length) % vis.length;
        const a = vis[idx], src = $('img', a);
        img.src = a.getAttribute('href'); img.alt = src.alt;
        cap.textContent = src.alt;
        count.textContent = `${idx + 1} / ${vis.length}`;
        img.style.animation = 'none'; img.offsetWidth; img.style.animation = '';
      };
      items.forEach(it => $('a', it).addEventListener('click', e => {
        e.preventDefault();
        vis = items.filter(x => !x.hidden).map(x => $('a', x));
        show(vis.indexOf($('a', it)));
        lb.showModal();
      }));
      $('.lb-prev', lb).addEventListener('click', () => show(idx - 1));
      $('.lb-next', lb).addEventListener('click', () => show(idx + 1));
      $('.lb-close', lb).addEventListener('click', () => lb.close());
      lb.addEventListener('keydown', e => {
        if (e.key === 'ArrowLeft') show(idx - 1);
        if (e.key === 'ArrowRight') show(idx + 1);
      });
      let sx = null, swiped = false;
      lb.addEventListener('click', e => {
        if (swiped) { swiped = false; return; }
        if (e.target === lb || e.target.classList.contains('lb-stage')) lb.close();
      });
      lb.addEventListener('pointerdown', e => { sx = e.clientX; });
      lb.addEventListener('pointerup', e => {
        if (sx !== null && Math.abs(e.clientX - sx) > 50) { swiped = true; show(idx + (e.clientX < sx ? 1 : -1)); }
        sx = null;
      });
    }
  }

  /* ---------- quote form: opens the visitor's email app, no backend ---------- */
  const form = $('form#quote');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      if (!form.reportValidity()) return;
      const d = new FormData(form);
      const body = [
        `Name: ${d.get('name')}`,
        `Phone: ${d.get('phone')}`,
        `Email: ${d.get('email') || ''}`,
        `Service: ${d.get('service')}`,
        '',
        `${d.get('details') || ''}`
      ].join('\n');
      const subject = `Free estimate request: ${d.get('service')}`;
      location.href = `mailto:scrubzcarpetcare@outlook.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      $('.form-status', form).textContent = 'Your email app should open with the request filled in. Just hit send. If nothing opened, call us at 817-262-7777.';
    });
  }
})();
