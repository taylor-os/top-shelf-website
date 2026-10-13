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

/* Phone numbers are always entered one way: (972) 555-1212. Formats as you type on
   every phone box, and tidies email boxes when you leave them. */
(function () {
  "use strict";
  function formatPhone(v) {
    var d = String(v || '').replace(/\D/g, '');
    if (d.length === 11 && d.charAt(0) === '1') d = d.slice(1);
    d = d.slice(0, 10);
    if (d.length === 0) return '';
    if (d.length < 4) return '(' + d;
    if (d.length < 7) return '(' + d.slice(0, 3) + ') ' + d.slice(3);
    return '(' + d.slice(0, 3) + ') ' + d.slice(3, 6) + '-' + d.slice(6);
  }
  window.reidsFormatPhone = formatPhone;
  document.querySelectorAll('input[type="tel"]').forEach(function (el) {
    el.setAttribute('inputmode', 'tel');
    el.setAttribute('maxlength', '16');
    if (el.value) el.value = formatPhone(el.value);
    el.addEventListener('input', function () {
      var atEnd = el.selectionStart === el.value.length;
      var next = formatPhone(el.value);
      if (next !== el.value) { el.value = next; if (!atEnd) { try { el.setSelectionRange(next.length, next.length); } catch (e) {} } }
      var n = next.replace(/\D/g, '').length;
      el.setCustomValidity(n === 0 || n === 10 ? '' : 'Please enter all 10 digits of the phone number.');
    });
  });
  document.querySelectorAll('input[type="email"]').forEach(function (el) {
    el.addEventListener('blur', function () { el.value = el.value.replace(/\s+/g, '').toLowerCase(); });
  });
})();
