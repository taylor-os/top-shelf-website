// Concept A: mobile menu + the industry switcher (an ARIA tablist with arrow-key support).
(function () {
  var menu = document.querySelector('.menu');
  var nav = document.getElementById('nav');
  if (menu && nav) {
    menu.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      menu.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        menu.setAttribute('aria-expanded', 'false');
        menu.focus();
      }
    });
  }

  document.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute('aria-controls'));
        if (!panel) return;
        panel.hidden = !on;
        panel.classList.toggle('in', on);
      });
      if (focus) tab.focus();
      tab.scrollIntoView({ block: 'nearest', inline: 'nearest' });
    }
    tabs.forEach(function (tab, i) {
      tab.addEventListener('click', function () { select(tab, false); });
      tab.addEventListener('keydown', function (ev) {
        var n = null;
        if (ev.key === 'ArrowRight' || ev.key === 'ArrowDown') n = tabs[(i + 1) % tabs.length];
        if (ev.key === 'ArrowLeft' || ev.key === 'ArrowUp') n = tabs[(i - 1 + tabs.length) % tabs.length];
        if (ev.key === 'Home') n = tabs[0];
        if (ev.key === 'End') n = tabs[tabs.length - 1];
        if (n) { ev.preventDefault(); select(n, true); }
      });
    });
  });
})();
