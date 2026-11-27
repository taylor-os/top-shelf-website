/* Larkspur Strength Club: Lenis + GSAP motion, drawer, reveals, schedule filter, demo form. Reduced-motion and no-JS safe. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = window.gsap && window.ScrollTrigger;

  /* Lenis smooth scroll, synced to GSAP when present */
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

  /* Hero barbell drifts as you scroll past it */
  if (hasGSAP && !reduce && document.querySelector(".hero__bar")) {
    gsap.registerPlugin(ScrollTrigger);
    gsap.to(".hero__bar", { yPercent: -12, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
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
    if (lenis) open ? lenis.stop() : lenis.start();
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
      var status = document.querySelector("[data-filter-status]");
      if (status) status.textContent = type === "all" ? "Showing every class." : "Showing " + btn.textContent.trim() + " only.";
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
