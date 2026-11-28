/* Bramlett Motor Co. sample site: Lenis + GSAP when available, safe without JS and under reduced motion. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = !!(window.gsap && window.ScrollTrigger);
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* Smooth scroll */
  var lenis = null;
  if (window.Lenis && !reduce) {
    lenis = new Lenis({ duration: 1.05, smoothWheel: true });
    if (hasGSAP) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on("scroll", ScrollTrigger.update);
      gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
      gsap.ticker.lagSmoothing(0);
    } else {
      requestAnimationFrame(function raf(t) { lenis.raf(t); requestAnimationFrame(raf); });
    }
  }

  /* Header background once the page moves */
  var header = $(".header");
  var sentinel = document.createElement("div");
  sentinel.style.cssText = "position:absolute;top:0;height:40px;width:1px;pointer-events:none";
  document.body.prepend(sentinel);
  if (header && "IntersectionObserver" in window) {
    new IntersectionObserver(function (e) { header.classList.toggle("scrolled", !e[0].isIntersecting); }).observe(sentinel);
  }

  /* Mobile drawer */
  var drawer = $("#drawer"), openBtn = $(".nav-toggle"), closeBtn = $(".drawer__close"), scrim = $(".scrim");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    if (scrim) scrim.classList.toggle("on", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) { if (open) lenis.stop(); else lenis.start(); }
    if (open && closeBtn) closeBtn.focus();
    else if (!open && openBtn && drawer.contains(document.activeElement)) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); });
  if (scrim) scrim.addEventListener("click", function () { setDrawer(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && drawer.classList.contains("open")) setDrawer(false); });

  /* Reveal on scroll */
  var reveals = $$("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* Photo parallax: hero and night-lot backgrounds drift slower than the page */
  if (hasGSAP && !reduce) {
    $$("[data-parallax]").forEach(function (el) {
      var host = el.parentElement, night = host.classList.contains("night");
      gsap.fromTo(el, { yPercent: night ? -5 : 0 }, { yPercent: night ? 5 : 14, ease: "none",
        scrollTrigger: { trigger: host, start: night ? "top bottom" : "top top", end: "bottom top", scrub: true } });
    });
  }

  /* "How are you paying?" segmented control */
  $$("[data-seg]").forEach(function (seg) {
    var tabs = $$("[role=tab]", seg);
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute("aria-selected", on ? "true" : "false");
        t.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(t.getAttribute("aria-controls"));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(t); });
      t.addEventListener("keydown", function (e) {
        var n = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (n) { e.preventDefault(); select(tabs[(i + n + tabs.length) % tabs.length], true); }
      });
    });
  });

  /* Inventory filter */
  var filters = $("[data-filters]");
  if (filters) {
    var cars = $$("[data-body]"), empty = $("[data-empty]"), count = $("[data-count]");
    filters.addEventListener("click", function (e) {
      var b = e.target.closest("button");
      if (!b) return;
      $$("button", filters).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      var f = b.getAttribute("data-filter"), shown = 0;
      cars.forEach(function (c) {
        var ok = f === "all" || (f === "under10" ? +c.getAttribute("data-price") < 10000 : c.getAttribute("data-body") === f);
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (empty) empty.classList.toggle("on", shown === 0);
      if (count) count.textContent = shown + (shown === 1 ? " sample car" : " sample cars");
    });
  }

  /* Test-drive form: preselect the car from ?car=, earliest day is today */
  var form = $("[data-drive-form]");
  if (form) {
    var car = new URLSearchParams(location.search).get("car");
    var sel = $("#td-car", form);
    if (car && sel && $('option[value="' + car.replace(/[^0-9-]/g, "") + '"]', sel)) sel.value = car.replace(/[^0-9-]/g, "");
    var day = $("#td-day", form);
    if (day) {
      var d = new Date(), pad = function (n) { return (n < 10 ? "0" : "") + n; };
      day.min = d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
      /* Closed Sunday: block it with the browser's own validation message */
      day.addEventListener("input", function () {
        var sun = day.value && new Date(day.value + "T12:00:00").getDay() === 0;
        day.setCustomValidity(sun ? "We're closed Sunday. Please pick Monday to Saturday." : "");
      });
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = $("[data-form-ok]");
      $$("input,select,textarea,button", form).forEach(function (el) { el.disabled = true; });
      if (ok) { ok.hidden = false; ok.focus(); }
    });
  }

  var y = $("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
