(() => {
  const d = document, root = d.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const motion = !reduce && 'IntersectionObserver' in window;
  if (motion) root.classList.add('motion');

  // Header: solid after scrolling; mobile menu
  const hdr = d.querySelector('.hdr');
  const burger = d.querySelector('.burger');
  const solid = () => hdr.classList.toggle('is-solid', scrollY > 24);
  solid();
  addEventListener('scroll', solid, { passive: true });
  const setMenu = open => {
    hdr.classList.toggle('is-open', open);
    d.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', open);
    burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  };
  burger.addEventListener('click', () => setMenu(!hdr.classList.contains('is-open')));
  d.addEventListener('keydown', e => { if (e.key === 'Escape' && hdr.classList.contains('is-open')) { setMenu(false); burger.focus(); } });
  matchMedia('(min-width: 1001px)').addEventListener('change', e => { if (e.matches) setMenu(false); });

  // Scroll reveals
  if (motion) {
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    }), { rootMargin: '0px 0px -8% 0px' });
    d.querySelectorAll('.rv, .dim').forEach(el => io.observe(el));
  }

  // Count-up (markup holds the final value, so no-JS and reduced motion show it as-is)
  if (motion) d.querySelectorAll('[data-count]').forEach(el => {
    const end = +el.dataset.count;
    el.textContent = '0';
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting) return;
      io.disconnect();
      const t0 = performance.now(), dur = 1800;
      const step = t => {
        const p = Math.min(1, (t - t0) / dur);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 4))).toLocaleString('en-US');
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }, { threshold: .6 });
    io.observe(el);
  });

  // Subtle parallax on oversized background images
  const px = [...d.querySelectorAll('[data-parallax]')];
  if (motion && px.length) {
    let ticking = false;
    const run = () => {
      ticking = false;
      const vh = innerHeight;
      px.forEach(el => {
        const r = el.parentElement.getBoundingClientRect();
        if (r.bottom < 0 || r.top > vh) return;
        const y = (r.top + r.height / 2 - vh / 2) * -(+el.dataset.parallax || .1);
        el.style.transform = `translate3d(0, ${y.toFixed(1)}px, 0)`;
      });
    };
    addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(run); } }, { passive: true });
    run();
  }

  // Before / after sliders (native range input drives a CSS variable)
  d.querySelectorAll('.ba input').forEach(inp => {
    const stage = inp.closest('.ba__stage');
    const set = () => stage.style.setProperty('--pos', inp.value + '%');
    inp.addEventListener('input', set);
    set();
  });

  // Home services list: swap the preview photo on hover / focus
  const frame = d.querySelector('.svc__peek');
  if (frame) d.querySelectorAll('.svc__row').forEach(a => {
    const show = () => {
      d.querySelectorAll('.svc__row.is-active').forEach(x => x.classList.remove('is-active'));
      a.classList.add('is-active');
      if (frame.getAttribute('src') === a.dataset.img) return;
      frame.classList.add('swap');
      setTimeout(() => { frame.src = a.dataset.img; frame.alt = a.dataset.alt; }, 180);
    };
    a.addEventListener('pointerenter', show);
    a.addEventListener('focus', show);
  });
  if (frame) frame.addEventListener('load', () => frame.classList.remove('swap'));

  // Portfolio filter
  const filters = d.querySelectorAll('[data-filter]');
  filters.forEach(b => b.addEventListener('click', () => {
    const c = b.dataset.filter;
    filters.forEach(x => x.setAttribute('aria-pressed', x === b));
    d.querySelectorAll('.pcard[data-cat]').forEach(card => { card.hidden = c !== 'all' && card.dataset.cat !== c; });
  }));

  // Lightbox
  const lb = d.querySelector('dialog.lb');
  if (lb) {
    const im = lb.querySelector('img'), cap = lb.querySelector('figcaption'), count = lb.querySelector('.lb__count');
    let set = [], i = 0;
    const show = k => {
      i = (k + set.length) % set.length;
      const a = set[i];
      im.src = a.getAttribute('href');
      im.alt = a.querySelector('img').alt;
      cap.textContent = a.dataset.caption || im.alt;
      count.textContent = `${i + 1} / ${set.length}`;
      lb.querySelector('.lb__prev').hidden = lb.querySelector('.lb__next').hidden = set.length < 2;
    };
    im.addEventListener('load', () => im.style.setProperty('--nw', Math.round(im.naturalWidth * 1.2) + 'px'));
    d.addEventListener('click', e => {
      const a = e.target.closest('a[data-lb]');
      if (!a) return;
      e.preventDefault();
      set = [...d.querySelectorAll(`a[data-lb="${a.dataset.lb}"]`)];
      show(set.indexOf(a));
      lb.showModal();
    });
    lb.querySelector('.lb__prev').addEventListener('click', () => show(i - 1));
    lb.querySelector('.lb__next').addEventListener('click', () => show(i + 1));
    lb.querySelector('.lb__close').addEventListener('click', () => lb.close());
    lb.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
    lb.addEventListener('click', e => { if (e.target === lb || e.target.classList.contains('lb__fig')) lb.close(); });
  }

  // Forms are a concept preview: no backend yet
  d.querySelectorAll('form[data-concept]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const n = f.querySelector('.form__note');
    n.hidden = false;
    n.focus();
  }));
})();
