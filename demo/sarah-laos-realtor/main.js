const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

// header + mobile call bar + parallax band
const hdr = $('.hdr'), bar = $('.mobile-bar'), bands = $$('.band > img');
const onScroll = () => {
  const y = scrollY;
  hdr.classList.toggle('solid', y > 40);
  if (bar) bar.classList.toggle('show', y > 500);
  if (!reduce) bands.forEach(img => {
    const r = img.parentElement.getBoundingClientRect();
    if (r.bottom > 0 && r.top < innerHeight) img.style.transform = `translateY(${(r.top + r.height / 2 - innerHeight / 2) * -0.12}px)`;
  });
};
addEventListener('scroll', onScroll, { passive: true }); onScroll();

// menu
$('.burger')?.addEventListener('click', e => {
  const open = document.body.classList.toggle('menu');
  e.currentTarget.setAttribute('aria-expanded', open);
});
$$('.nav a').forEach(a => a.addEventListener('click', () => document.body.classList.remove('menu')));

// reveal
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { rootMargin: '0px 0px -8% 0px' });
// anything already on screen shows immediately; the rest waits for scroll
$$('[data-reveal]').forEach(el => el.getBoundingClientRect().top < innerHeight ? el.classList.add('in') : io.observe(el));

// listing filters
$$('.filters button').forEach(b => b.addEventListener('click', () => {
  $$('.filters button').forEach(x => x.setAttribute('aria-pressed', x === b));
  $$('.cards .card').forEach(c => c.hidden = b.dataset.f !== 'all' && c.dataset.status !== b.dataset.f);
}));

// lightbox
const shots = $$('[data-shot]');
if (shots.length) {
  const lb = document.createElement('div');
  lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-label', 'Photo gallery');
  lb.innerHTML = '<img alt=""><button class="x" aria-label="Close">&times;</button><button class="prev" aria-label="Previous">&#8249;</button><button class="next" aria-label="Next">&#8250;</button><div class="count"></div>';
  document.body.append(lb);
  const img = $('img', lb); let i = 0;
  const show = n => { i = (n + shots.length) % shots.length; img.src = shots[i].dataset.shot; img.alt = shots[i].querySelector('img')?.alt || ''; $('.count', lb).textContent = `${i + 1} / ${shots.length}`; };
  const close = () => { lb.classList.remove('open'); document.body.style.overflow = ''; };
  shots.forEach((s, n) => s.addEventListener('click', () => { show(n); lb.classList.add('open'); document.body.style.overflow = 'hidden'; $('.x', lb).focus(); }));
  $('.x', lb).onclick = close; $('.prev', lb).onclick = () => show(i - 1); $('.next', lb).onclick = () => show(i + 1);
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  addEventListener('keydown', e => {
    if (!lb.classList.contains('open')) return;
    if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1);
  });
}

// mortgage calculator (principal + interest only)
const calc = $('#c-price')?.closest('.calc');
if (calc) {
  const run = () => {
    const price = +$('#c-price').value || 0, down = (+$('#c-down').value || 0) / 100, rate = (+$('#c-rate').value || 0) / 1200, n = 360;
    const P = price * (1 - down);
    const m = rate ? P * rate / (1 - Math.pow(1 + rate, -n)) : P / n;
    $('#c-out').textContent = '$' + Math.round(m).toLocaleString();
  };
  $$('input', calc).forEach(x => x.addEventListener('input', run)); run();
}

// demo forms: no backend on the preview, so confirm on the page
$$('form[data-demo]').forEach(f => f.addEventListener('submit', e => {
  e.preventDefault();
  if (!f.reportValidity()) return;
  f.classList.add('sent');
}));

// prefill contact message from ?about=
const about = new URLSearchParams(location.search).get('about'), msg = $('#msg');
if (about && msg) msg.value = `I'd like more information about ${about}.`;

$$('.yr').forEach(y => y.textContent = new Date().getFullYear());
