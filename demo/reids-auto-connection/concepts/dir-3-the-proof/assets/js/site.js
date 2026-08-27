/* Reids Auto Connection — shared interactions for interior pages.
   Mirrors the locked homepage's behavior: mobile nav, scroll reveals,
   count-up stats, and the sticky mobile CTA. All lookups are guarded so
   a page missing an element degrades quietly. Respects reduced-motion. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* mobile nav */
  var ham = document.getElementById('ham'), hdr = document.getElementById('hdr');
  if (ham && hdr) {
    ham.addEventListener('click', function () {
      var open = hdr.classList.toggle('open');
      ham.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () {
        hdr.classList.remove('open');
        ham.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* count-up */
  function countUp(el) {
    if (el.dataset.counted) return; el.dataset.counted = '1';
    var raw = el.getAttribute('data-count');
    var target = parseFloat(raw);
    var dec = (raw.split('.')[1] || '').length;
    var dur = 1100, start = null;
    function step(t) {
      if (start === null) start = t;
      var p = Math.min((t - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = (target * eased).toFixed(dec);
      if (p < 1) requestAnimationFrame(step); else el.textContent = target.toFixed(dec);
    }
    requestAnimationFrame(step);
  }

  if (reduce) {
    document.querySelectorAll('.reveal').forEach(function (e) { e.classList.add('in'); });
    document.querySelectorAll('[data-count]').forEach(function (e) {
      e.textContent = parseFloat(e.getAttribute('data-count')).toFixed((e.getAttribute('data-count').split('.')[1] || '').length);
    });
  } else if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          en.target.classList.add('in');
          en.target.querySelectorAll && en.target.querySelectorAll('[data-count]').forEach(countUp);
          if (en.target.matches('[data-count]')) countUp(en.target);
          io.unobserve(en.target);
        }
      });
    }, { threshold: .16, rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal, [data-count]').forEach(function (e) { io.observe(e); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (e) { e.classList.add('in'); });
  }

  /* sticky mobile CTA after the masthead/hero, hidden when a form is on screen */
  var mbar = document.getElementById('mbar');
  var top = document.querySelector('.masthead, .hero');
  if (mbar && top) {
    var onScroll = function () {
      var past = window.scrollY > (top.offsetHeight - 70);
      var nearForm = false;
      var f = document.getElementById('get-approved') || document.querySelector('form');
      if (f) { var r = f.getBoundingClientRect(); nearForm = r.top < window.innerHeight && r.bottom > 0; }
      mbar.classList.toggle('show', past && !nearForm);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
})();
