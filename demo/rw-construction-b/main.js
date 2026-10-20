/* RW Construction concept — one motion system: Lenis + GSAP ScrollTrigger. */
(() => {
  const d = document, root = d.documentElement;
  const $ = (s, c = d) => c.querySelector(s), $$ = (s, c = d) => [...c.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const motion = !reduce && !!(window.gsap && window.ScrollTrigger);
  if (!motion) root.classList.remove('motion');

  /* smooth scroll: one clock drives Lenis and ScrollTrigger */
  let lenis = null;
  if (motion) {
    gsap.registerPlugin(ScrollTrigger);
    ScrollTrigger.config({ ignoreMobileResize: true });
    if (window.Lenis) {
      lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((t) => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }

  /* header state */
  const hdr = $('.hdr');
  const onScroll = () => hdr.classList.toggle('scrolled', scrollY > 30);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* mobile menu */
  const burger = $('.burger'), menu = $('#menu');
  const setMenu = (open) => {
    root.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open);
    menu.inert = !open;
    if (lenis) open ? lenis.stop() : lenis.start();
  };
  menu.inert = true;
  burger.addEventListener('click', () => setMenu(!root.classList.contains('menu-open')));
  addEventListener('keydown', (e) => { if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });
  $$('a', menu).forEach((a) => a.addEventListener('click', () => setMenu(false)));

  /* split headings into masked words (keeps <em>/<br>) */
  const splitWords = (el) => {
    const walk = d.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodes = [];
    while (walk.nextNode()) nodes.push(walk.currentNode);
    nodes.forEach((n) => {
      const frag = d.createDocumentFragment();
      n.textContent.split(/(\s+)/).forEach((part) => {
        if (!part) return;
        if (/^\s+$/.test(part)) return frag.append(' ');
        const o = d.createElement('span'), i = d.createElement('span');
        o.className = 'w'; i.textContent = part; o.append(i); frag.append(o);
      });
      n.replaceWith(frag);
    });
    return $$('.w > span', el);
  };
  $$('[data-split]').forEach((h) => {
    const words = splitWords(h);
    h.style.visibility = 'visible';
    if (!motion) return;
    const top = h.getBoundingClientRect().top < innerHeight;
    gsap.fromTo(words, { yPercent: 115 }, {
      yPercent: 0, duration: 1.1, ease: 'power4.out', stagger: 0.06, delay: top ? 0.45 : 0,
      scrollTrigger: top ? null : { trigger: h, start: 'top 88%' },
    });
  });

  if (motion) {
    /* entrances */
    $$('[data-reveal]').forEach((el) => gsap.fromTo(el, { y: 36, opacity: 0 }, {
      y: 0, opacity: 1, duration: 1, ease: 'power3.out', scrollTrigger: { trigger: el, start: 'top 92%' },
    }));
    /* image mask reveals */
    $$('[data-clip]').forEach((el) => {
      const im = $('img', el);
      const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 88%' } });
      tl.fromTo(el, { clipPath: 'inset(12% 8% 12% 8% round 6px)' }, { clipPath: 'inset(0% 0% 0% 0% round 6px)', duration: 1.3, ease: 'expo.out' });
      if (im) tl.fromTo(im, { scale: 1.18 }, { scale: 1, duration: 1.6, ease: 'expo.out' }, 0);
    });
    /* page heroes: slow drift */
    $$('.phero-img img').forEach((im) => gsap.fromTo(im, { yPercent: 0, scale: 1.08 }, {
      yPercent: 8, scale: 1.08, ease: 'none', scrollTrigger: { trigger: im.closest('.phero'), start: 'top top', end: 'bottom top', scrub: true },
    }));
  }

  /* counters */
  $$('[data-count]').forEach((el) => {
    const end = +el.dataset.count, fmt = (n) => Math.round(n).toLocaleString('en-US');
    if (!motion) return;
    const o = { v: 0 };
    el.textContent = '0';
    gsap.to(o, { v: end, duration: 2.2, ease: 'power3.out', onUpdate: () => (el.textContent = fmt(o.v)), scrollTrigger: { trigger: el, start: 'top 88%' } });
  });

  /* line drawings */
  $$('svg[data-draw]').forEach((svg) => {
    if (!motion) return;
    const lines = $$('.ln', svg);
    lines.forEach((p) => { const L = p.getTotalLength(); p.style.strokeDasharray = L; p.style.strokeDashoffset = L; });
    const onLoad = svg.dataset.draw === 'load';
    const tl = gsap.timeline(onLoad ? { delay: 0.5 } : { scrollTrigger: { trigger: svg, start: 'top 80%' } });
    tl.to(lines, { strokeDashoffset: 0, duration: 1.4, ease: 'power2.inOut', stagger: 0.07 });
    const txt = $$('.plan-txt text', svg);
    if (txt.length) tl.from(txt, { opacity: 0, duration: 0.5, stagger: 0.08 }, '-=0.6');
  });

  /* signature: plans -> frame -> finish */
  const story = $('.story');
  if (story && motion) {
    story.dataset.stage = 0;
    const lf = $('.l-frame', story), ln = $('.l-finish', story), eh = $('.edge-h', story), ev = $('.edge-v', story);
    const setStage = (p) => {
      story.dataset.stage = p < 0.3 ? 0 : p < 0.72 ? 1 : 2;
      story.style.setProperty('--p', Math.max(0.02, p).toFixed(3));
    };
    setStage(0);
    const build = (st) => {
      const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: { ...st, scrub: 0.6, onUpdate: (s) => setStage(s.progress) } });
      tl.to({}, { duration: 0.12 })
        .addLabel('f')
        .fromTo(lf, { clipPath: 'inset(100% 0% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.32 }, 'f')
        .fromTo($('img', lf), { scale: 1.14 }, { scale: 1, duration: 0.32 }, 'f')
        .fromTo(eh, { top: '100%', opacity: 1 }, { top: '0%', duration: 0.32, immediateRender: false }, 'f')
        .to(eh, { opacity: 0, duration: 0.03 })
        .to({}, { duration: 0.12 })
        .addLabel('n')
        .fromTo(ln, { clipPath: 'inset(0% 100% 0% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 0.32 }, 'n')
        .fromTo($('img', ln), { scale: 1.14 }, { scale: 1, duration: 0.32 }, 'n')
        .fromTo(ev, { left: '0%', opacity: 1 }, { left: '100%', duration: 0.32, immediateRender: false }, 'n')
        .to(ev, { opacity: 0, duration: 0.03 })
        .to({}, { duration: 0.1 });
      return tl;
    };
    const mm = gsap.matchMedia();
    mm.add('(min-width: 1101px)', () => { build({ trigger: story, start: 'top top', end: '+=180%', pin: true, anticipatePin: 1 }); });
    mm.add('(max-width: 1100px)', () => { build({ trigger: $('.plate', story), start: 'top 75%', end: 'bottom 20%' }); });
  }

  /* design-build rail */
  const fill = $('.tl-fill');
  if (fill && motion) gsap.fromTo(fill, { scaleY: 0 }, { scaleY: 1, ease: 'none', scrollTrigger: { trigger: '.tl', start: 'top 65%', end: 'bottom 65%', scrub: true } });

  /* before / after */
  $$('.ba').forEach((b) => {
    const r = $('input', b), set = () => b.style.setProperty('--pos', r.value + '%');
    r.addEventListener('input', set); set();
  });

  /* project filters (also honours #category in the URL) */
  const fbtn = $$('[data-filter]');
  if (fbtn.length) {
    const apply = (f, animate) => {
      fbtn.forEach((x) => x.setAttribute('aria-pressed', x.dataset.filter === f));
      const cards = $$('.pcard');
      cards.forEach((c) => (c.hidden = !(f === 'all' || c.dataset.cat === f)));
      if (motion && animate) {
        const shown = cards.filter((c) => !c.hidden);
        gsap.fromTo(shown, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out', stagger: 0.05, overwrite: true });
        ScrollTrigger.refresh();
      }
    };
    fbtn.forEach((b) => b.addEventListener('click', () => {
      apply(b.dataset.filter, true);
      history.replaceState(null, '', b.dataset.filter === 'all' ? location.pathname : '#' + b.dataset.filter);
    }));
    const fromHash = (animate) => { const h = location.hash.slice(1); if (fbtn.some((b) => b.dataset.filter === h)) apply(h, animate); };
    fromHash(false);
    addEventListener('hashchange', () => fromHash(true));
  }

  /* lightbox */
  const gal = $$('[data-lb]');
  if (gal.length) {
    const arrow = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
    const dlg = d.createElement('dialog');
    dlg.className = 'lb';
    dlg.setAttribute('aria-label', 'Photo viewer');
    dlg.innerHTML = `<figure><img alt=""><figcaption></figcaption></figure>
      <button class="lb-x" type="button" aria-label="Close"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
      <button class="lb-p" type="button" aria-label="Previous photo">${arrow}</button>
      <button class="lb-n" type="button" aria-label="Next photo">${arrow}</button>`;
    d.body.append(dlg);
    const im = $('img', dlg), cap = $('figcaption', dlg);
    let idx = 0;
    const show = (i) => {
      idx = (i + gal.length) % gal.length;
      const a = gal[idx], src = $('img', a);
      im.src = a.href; im.alt = src.alt; cap.textContent = `${idx + 1} / ${gal.length}`;
      if (motion) gsap.fromTo(im, { opacity: 0, scale: 0.97 }, { opacity: 1, scale: 1, duration: 0.45, ease: 'power3.out' });
    };
    gal.forEach((a, i) => a.addEventListener('click', (e) => { e.preventDefault(); show(i); dlg.showModal(); lenis && lenis.stop(); }));
    $('.lb-x', dlg).onclick = () => dlg.close();
    $('.lb-p', dlg).onclick = () => show(idx - 1);
    $('.lb-n', dlg).onclick = () => show(idx + 1);
    dlg.addEventListener('click', (e) => { if (e.target === dlg || e.target.tagName === 'FIGURE') dlg.close(); });
    dlg.addEventListener('keydown', (e) => { if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1); });
    dlg.addEventListener('close', () => { lenis && lenis.start(); gal[idx].focus(); });
  }

  /* contact tabs */
  const tabs = $$('[role="tab"]');
  if (tabs.length) {
    const select = (t) => tabs.forEach((x) => {
      const on = x === t;
      x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
      d.getElementById(x.getAttribute('aria-controls')).hidden = !on;
    });
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => select(t));
      t.addEventListener('keydown', (e) => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
        select(n); n.focus();
      });
    });
    if (location.hash === '#subcontractors') select(tabs[1]);
  }

  /* concept forms: no backend yet */
  $$('form[data-concept]').forEach((f) => f.addEventListener('submit', (e) => {
    e.preventDefault();
    const note = $('.form-note', f);
    note.hidden = false; note.focus();
  }));

  /* magnetic CTAs (fine pointers only) */
  if (motion && matchMedia('(pointer: fine)').matches) {
    $$('.mag').forEach((el) => {
      const x = gsap.quickTo(el, 'x', { duration: 0.5, ease: 'power3' }), y = gsap.quickTo(el, 'y', { duration: 0.5, ease: 'power3' });
      el.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        x((e.clientX - r.left - r.width / 2) * 0.22); y((e.clientY - r.top - r.height / 2) * 0.3);
      });
      el.addEventListener('pointerleave', () => { x(0); y(0); });
    });
  }

  /* page transition curtain */
  const curtain = $('.curtain');
  if (motion) {
    $$('a[href]').forEach((a) => {
      const u = new URL(a.href, location.href);
      if (u.origin !== location.origin || a.target || !/\.html$/.test(u.pathname)) return;
      if (u.pathname === location.pathname) return;
      a.addEventListener('click', (e) => {
        if (e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button) return;
        e.preventDefault();
        curtain.style.animation = 'none';
        gsap.fromTo(curtain, { yPercent: 100 }, { yPercent: 0, duration: 0.5, ease: 'power3.in', onComplete: () => (location.href = a.href) });
      });
    });
    addEventListener('pageshow', (e) => { if (e.persisted) { curtain.style.animation = 'none'; gsap.set(curtain, { yPercent: -100 }); } });
    addEventListener('load', () => ScrollTrigger.refresh());
  }
})();
