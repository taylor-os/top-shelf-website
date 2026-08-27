/* =========================================================================
   Reids Auto Connection — Daybreak interactions (restrained by design)
   1. Header condense on scroll   2. Mobile nav   3. Fade-up reveal
   No animation library, no auto-playing motion, reduced-motion respected.
   ========================================================================= */
(function () {
  "use strict";
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- header condense ---- */
  var hdr = document.getElementById('hdr');
  if (hdr) {
    var onScroll = function () { hdr.classList.toggle('scrolled', window.scrollY > 12); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- mobile nav ---- */
  var nav = document.querySelector('.nav');
  var burger = document.querySelector('.hamburger');
  if (nav && burger) {
    var navLinks = nav.querySelector('.nav-links');
    if (navLinks && !navLinks.querySelector('.nav-call')) {
      var call = document.createElement('a');
      call.className = 'nav-call';
      call.href = 'tel:+19724361600';
      call.innerHTML = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.9.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg> Call (972) 436-1600';
      navLinks.insertBefore(call, navLinks.firstChild);
    }
    burger.setAttribute('aria-expanded', 'false');
    var setMenu = function (open) {
      nav.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };
    burger.addEventListener('click', function () { setMenu(!nav.classList.contains('menu-open')); });
    nav.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { setMenu(false); });
    });
  }

  /* ---- fade-up reveal ---- */
  var items = document.querySelectorAll('.reveal:not(.in)');
  if (reduced || !('IntersectionObserver' in window)) {
    items.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    items.forEach(function (el) { io.observe(el); });
  }
})();
