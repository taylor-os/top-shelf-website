/* Larkspur Strength Club: Lenis + GSAP motion, header state, drawer, reveals,
   schedule filter, demo form. Reduced-motion and no-JS safe. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = !!(window.gsap && window.ScrollTrigger);

  /* Hero headline and photo settle in once the page is ready */
  var heroes = document.querySelectorAll(".hero, .phero");
  function ready() { heroes.forEach(function (h) { h.classList.add("is-ready"); }); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { requestAnimationFrame(ready); });
  else requestAnimationFrame(ready);
  setTimeout(ready, 1200);

  /* Lenis smooth scroll, synced to GSAP */
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

  /* Photos drift a little slower than the page (the wrapper is oversized, so no edge shows) */
  if (hasGSAP && !reduce && window.matchMedia("(min-width: 900px)").matches) {
    gsap.registerPlugin(ScrollTrigger);
    document.querySelectorAll(".parallax").forEach(function (el) {
      var host = el.closest(".hero, .phero, .band, .plans-band") || el.parentNode;
      var top = host.classList.contains("hero") || host.classList.contains("phero");
      gsap.fromTo(el, { yPercent: top ? 0 : -6 }, {
        yPercent: 6, ease: "none",
        scrollTrigger: { trigger: host, start: top ? "top top" : "top bottom", end: "bottom top", scrub: true }
      });
    });
  }

  /* Header turns solid once you leave the top of the page */
  var header = document.querySelector(".header");
  if (header && "IntersectionObserver" in window) {
    var mark = document.createElement("div");
    mark.setAttribute("aria-hidden", "true");
    mark.style.cssText = "position:absolute;top:0;left:0;width:1px;height:48px;pointer-events:none";
    document.body.prepend(mark);
    new IntersectionObserver(function (en) { header.classList.toggle("is-solid", !en[0].isIntersecting); }).observe(mark);
  }

  /* Mobile drawer */
  var drawer = document.querySelector(".drawer");
  var openBtn = document.querySelector(".nav-toggle");
  var closeBtn = document.querySelector(".drawer__close");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) { if (open) lenis.stop(); else lenis.start(); }
    if (open && closeBtn) requestAnimationFrame(function () { closeBtn.focus(); });
    else if (!open && openBtn && drawer.contains(document.activeElement)) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); });
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && drawer.classList.contains("open")) setDrawer(false); });

  /* Reveal on scroll */
  var els = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    els.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    els.forEach(function (el) { io.observe(el); });
  }

  /* Schedule filter by class type */
  var filters = document.querySelectorAll("[data-filter]");
  filters.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var type = btn.getAttribute("data-filter");
      filters.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      document.querySelectorAll(".slot").forEach(function (s) {
        s.classList.toggle("is-hidden", type !== "all" && s.getAttribute("data-type") !== type);
      });
      document.querySelectorAll(".day").forEach(function (d) {
        d.toggleAttribute("data-empty", !d.querySelector(".slot:not(.is-hidden)"));
      });
      var status = document.querySelector("[data-filter-status]");
      if (status) status.textContent = type === "all" ? "Showing every class." : "Showing " + btn.textContent.trim() + " only.";
      if (hasGSAP) ScrollTrigger.refresh();
    });
  });

  /* Intro class request form (sample: nothing is sent) */
  var form = document.querySelector("[data-demo-form]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = form.querySelector("[data-form-ok]");
    form.querySelectorAll("input,select,textarea,button").forEach(function (el) { el.disabled = true; });
    if (ok) { ok.hidden = false; ok.focus(); }
  });

  var y = document.querySelector("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
