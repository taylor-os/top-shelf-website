/* Reids Auto Connection — shared site behavior.
   Header stick-on-scroll, mobile menu, and reveal-on-scroll.
   All guarded so the file is safe to include on every page. */
(function () {
  "use strict";

  // sticky masthead shadow
  var mh = document.getElementById('masthead');
  if (mh) {
    var onScroll = function () { mh.classList.toggle('is-stuck', window.scrollY > 24); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // mobile menu
  var hamb = document.getElementById('hamb'), mmenu = document.getElementById('mmenu');
  if (hamb && mmenu) {
    hamb.addEventListener('click', function () {
      var open = mmenu.classList.toggle('open');
      hamb.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mmenu.addEventListener('click', function (e) {
      if (e.target.closest('a')) { mmenu.classList.remove('open'); hamb.setAttribute('aria-expanded', 'false'); }
    });
  }

  // reveal on scroll (respects reduced motion)
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  }
})();
