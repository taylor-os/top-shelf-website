/* Scrubz Carpet Care v2: site behavior. Vanilla, no dependencies.
   Every effect here is an enhancement: with JS off the page is complete (see the .js gates in styles.css). */
(() => {
  window.scrubzReady = true; /* tells the inline failsafe in <head> that reveals will run */
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];

  /* header: hairline + shadow once the page moves */
  const hdr = $('.hdr');
  const onScroll = () => hdr && hdr.classList.toggle('scrolled', scrollY > 8);
  onScroll();
  addEventListener('scroll', onScroll, { passive: true });

  /* mobile menu: panel opens below the header (and below the ribbon at scroll 0) */
  const menuBtn = $('.menu-btn'), nav = $('#nav');
  if (menuBtn && nav && hdr) {
    const setMenu = open => {
      if (open) nav.style.setProperty('--menu-top', Math.max(0, hdr.getBoundingClientRect().bottom) + 'px');
      document.body.classList.toggle('menu-open', open);
      root.classList.toggle('menu-lock', open);
      menuBtn.setAttribute('aria-expanded', open);
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    menuBtn.addEventListener('click', () => setMenu(!document.body.classList.contains('menu-open')));
    $$('a', nav).forEach(a => a.addEventListener('click', () => setMenu(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape') setMenu(false); });
    matchMedia('(min-width: 961px)').addEventListener('change', e => e.matches && setMenu(false));
  }

  /* reveals: headings get a clean-pass sweep, photos clear like steam, blocks rise.
     Targets are never clipped or zero-sized, so the observer always sees them. */
  const targets = $$('[data-reveal], [data-sweep], [data-steam]');
  if (reduce || !('IntersectionObserver' in window)) {
    targets.forEach(el => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver(entries => entries.forEach(en => {
      if (!en.isIntersecting) return;
      en.target.classList.add('in');
      io.unobserve(en.target);
    }), { rootMargin: '0px 0px -8% 0px', threshold: 0 });
    targets.forEach(el => io.observe(el));
  }

  /* pinned photo strip: vertical scroll slides the row sideways.
     Without JS (or with reduced motion) it stays a native swipeable rail. */
  const strip = $('.strip');
  if (strip && !reduce) {
    const sticky = $('.strip-sticky', strip), track = $('.strip-track', strip), bar = $('.strip-progress i', strip);
    let dist = 0, lastW = 0, raf = 0;
    const move = () => {
      raf = 0;
      if (!dist) return;
      const top = strip.getBoundingClientRect().top;
      const p = Math.min(1, Math.max(0, -top / dist));
      track.style.transform = `translate3d(${(-p * dist).toFixed(1)}px,0,0)`;
      if (bar) bar.style.transform = `scaleX(${p.toFixed(3)})`;
    };
    const measure = force => {
      if (!force && innerWidth === lastW) return; /* ignore phone URL-bar height changes */
      lastW = innerWidth;
      /* phones: a full-screen pin leaves dead space around a short row, so keep the native swipe rail */
      if (innerWidth < 761) { strip.classList.remove('pinned'); strip.style.height = ''; track.style.transform = ''; dist = 0; return; }
      strip.classList.add('pinned');
      track.style.transform = '';
      dist = Math.max(0, track.scrollWidth - track.clientWidth);
      if (dist < 40) { strip.classList.remove('pinned'); strip.style.height = ''; dist = 0; return; }
      strip.style.height = (sticky.offsetHeight + dist) + 'px';
      move();
    };
    addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(move); }, { passive: true });
    addEventListener('resize', () => measure(false));
    addEventListener('load', () => measure(true));
    measure(true);
    /* strip photos sit off to the side until they slide in, so start them loading before the section arrives */
    const pre = new IntersectionObserver(([en]) => {
      if (!en.isIntersecting) return;
      $$('img', track).forEach(img => { img.loading = 'eager'; });
      pre.disconnect();
    }, { rootMargin: '800px 0px' });
    pre.observe(strip);
  }

  /* ---------- gallery: filters + lightbox ---------- */
  const grid = $('.g-grid');
  if (grid) {
    const items = $$('.g-item', grid);
    const btns = $$('.filters button');
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.setAttribute('aria-pressed', x === b));
      const f = b.dataset.filter;
      items.forEach(it => { it.hidden = f !== 'all' && it.dataset.cat !== f; it.classList.add('in'); });
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

  /* ---------- estimate form: opens the visitor's email app, no backend ---------- */
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
