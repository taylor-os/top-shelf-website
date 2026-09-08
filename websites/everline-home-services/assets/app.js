/* Everline Home Services — motion + interactions
   Lenis smooth scroll + GSAP ScrollTrigger, all reduced-motion & no-JS safe. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = window.gsap && window.ScrollTrigger;

  /* ---- Lenis smooth scroll (synced to GSAP) ---- */
  var lenis = null;
  if (window.Lenis && !reduce) {
    lenis = new Lenis({ duration: 1.1, easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); }, smoothWheel: true });
    if (hasGSAP) {
      gsap.registerPlugin(ScrollTrigger);
      lenis.on("scroll", ScrollTrigger.update);
      gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
      gsap.ticker.lagSmoothing(0);
    } else {
      requestAnimationFrame(function raf(t) { lenis.raf(t); requestAnimationFrame(raf); });
    }
  }

  /* ---- Header scrolled state ---- */
  var header = document.querySelector(".header");
  function onScroll(y) { if (header) header.classList.toggle("scrolled", y > 40); }
  if (lenis) lenis.on("scroll", function (e) { onScroll(e.scroll); });
  else window.addEventListener("scroll", function () { onScroll(window.scrollY); }, { passive: true });
  onScroll(window.scrollY);

  /* ---- Mobile drawer ---- */
  var drawer = document.querySelector(".drawer");
  var openBtn = document.querySelector(".nav-toggle");
  var closeBtn = document.querySelector(".drawer__close");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) open ? lenis.stop() : lenis.start();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); });
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setDrawer(false); });

  /* ---- Anchor smooth-scroll via Lenis ---- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var el = document.querySelector(id);
      if (!el) return;
      e.preventDefault();
      if (lenis) lenis.scrollTo(el, { offset: -90 });
      else el.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
    });
  });

  /* ---- Reveal on scroll (IntersectionObserver — always safe) ---- */
  var revealEls = document.querySelectorAll("[data-reveal],[data-reveal-stagger]");
  if (reduce || !("IntersectionObserver" in window)) {
    revealEls.forEach(function (el) { el.classList.add("in"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute("data-reveal-stagger")) {
          Array.prototype.forEach.call(el.children, function (child, i) {
            child.style.transitionDelay = (i * 0.08) + "s";
          });
        }
        el.classList.add("in");
        io.unobserve(el);
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Count-up stats ---- */
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var dec = (el.getAttribute("data-count").split(".")[1] || "").length;
    var suffix = el.getAttribute("data-suffix") || "";
    var prefix = el.getAttribute("data-prefix") || "";
    if (reduce) { el.textContent = prefix + target.toLocaleString(undefined, { minimumFractionDigits: dec }) + suffix; return; }
    var start = null, dur = 1600;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      var val = target * eased;
      el.textContent = prefix + val.toLocaleString(undefined, { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length) {
    if (!("IntersectionObserver" in window)) counters.forEach(animateCount);
    else {
      var cio = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); } });
      }, { threshold: 0.6 });
      counters.forEach(function (el) { cio.observe(el); });
    }
  }

  /* ---- Hero rotating word ---- */
  var rot = document.querySelector("[data-rotate]");
  if (rot) {
    var words = JSON.parse(rot.getAttribute("data-rotate"));
    var i = 0;
    rot.textContent = words[0];
    if (!reduce) setInterval(function () {
      i = (i + 1) % words.length;
      rot.style.transition = "opacity .32s, transform .32s"; rot.style.opacity = "0"; rot.style.transform = "translateY(-8px)";
      setTimeout(function () {
        rot.textContent = words[i];
        rot.style.transform = "translateY(8px)";
        requestAnimationFrame(function () { rot.style.opacity = "1"; rot.style.transform = "translateY(0)"; });
      }, 320);
    }, 2400);
  }

  /* ---- Hero parallax ---- */
  if (hasGSAP && !reduce) {
    var heroImg = document.querySelector(".hero__media img");
    if (heroImg) gsap.to(heroImg, {
      yPercent: 14, ease: "none",
      scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
    });
    /* subtle depth on hero card */
    var heroCard = document.querySelector(".hero__card");
    if (heroCard) gsap.from(heroCard, { y: 40, opacity: 0, duration: 1, delay: .3, ease: "power3.out" });
  }

  /* ---- Hero headline load-in ---- */
  var hHead = document.querySelector(".hero h1");
  if (hHead && !reduce) {
    hHead.style.opacity = "0"; hHead.style.transform = "translateY(20px)";
    requestAnimationFrame(function () {
      hHead.style.transition = "opacity .9s var(--ease-out), transform .9s var(--ease-out)";
      hHead.style.opacity = "1"; hHead.style.transform = "none";
    });
  }

  /* ---- Contact form (demo, no backend) ---- */
  var form = document.querySelector("[data-demo-form]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = form.querySelector("[data-form-ok]");
    form.querySelectorAll("input,select,textarea,button").forEach(function (el) { el.disabled = true; });
    if (ok) { ok.hidden = false; ok.scrollIntoView ? ok.scrollIntoView({ behavior: "smooth", block: "center" }) : null; }
  });

  /* year */
  var y = document.querySelector("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
