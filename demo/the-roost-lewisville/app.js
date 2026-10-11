/* The Roost Lewisville. Small progressive enhancements; every page works without this file. */
(function () {
  var d = document;
  var $$ = function (s) { return Array.prototype.slice.call(d.querySelectorAll(s)); };

  // Mobile nav toggle
  var toggle = d.querySelector('.nav-toggle');
  var nav = d.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      toggle.setAttribute('aria-expanded', String(nav.classList.toggle('open')));
    });
  }

  // Section reveals, staggered per batch
  var reveals = $$('[data-reveal]');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      var n = 0;
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.style.transitionDelay = (n++ * 80) + 'ms';
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Menu page: highlight the category you are reading
  var catLinks = $$('.catnav a');
  if (catLinks.length && 'IntersectionObserver' in window) {
    var row = d.querySelector('.catnav-row');
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        catLinks.forEach(function (a) {
          if (a.getAttribute('href') === '#' + e.target.id) {
            a.setAttribute('aria-current', 'true');
            row.scrollLeft = a.offsetLeft - 16;
          } else {
            a.removeAttribute('aria-current');
          }
        });
      });
    }, { rootMargin: '-35% 0px -60% 0px' });
    $$('.menu-section').forEach(function (s) { spy.observe(s); });
  }

  // Flavor picker: the menu allows up to 2 flavors per order
  var flavs = $$('.flav');
  var out = d.querySelector('.pick');
  if (flavs.length && out) {
    var picks = [];
    out.textContent = 'Tap up to 2 flavors.';
    flavs.forEach(function (b) {
      b.addEventListener('click', function () {
        var i = picks.indexOf(b);
        if (i > -1) picks.splice(i, 1);
        else { picks.push(b); if (picks.length > 2) picks.shift(); }
        flavs.forEach(function (x) { x.setAttribute('aria-pressed', String(picks.indexOf(x) > -1)); });
        var names = picks.map(function (x) { return x.getAttribute('data-name'); });
        out.textContent = !names.length ? 'Tap up to 2 flavors.'
          : names.length === 1 ? 'Your pick: ' + names[0] + '. Room for one more.'
          : 'Your pick: ' + names.join(' + ') + '. Tell us at the bar.';
      });
    });
  }

  // Hours: mark today and show open/closed. Open 11 AM to 2 AM every day, Lewisville (Central) time.
  var badge = d.querySelector('.open-now');
  if (badge || d.querySelector('.hours')) {
    try {
      var now = new Date();
      var fmt = function (o) { o.timeZone = 'America/Chicago'; return new Intl.DateTimeFormat('en-US', o).format(now); };
      var hour = parseInt(fmt({ hour: 'numeric', hour12: false }), 10) % 24;
      var day = fmt({ weekday: 'long' });
      $$('.hours li').forEach(function (li) { if (li.getAttribute('data-day') === day) li.classList.add('is-today'); });
      if (badge) {
        var open = hour >= 11 || hour < 2;
        badge.textContent = open ? 'Open now until 2 AM' : 'Closed right now. Back at 11 AM.';
        if (!open) badge.classList.add('is-closed');
      }
    } catch (e) { /* no Intl time zones: leave the plain hours list */ }
  }
})();
