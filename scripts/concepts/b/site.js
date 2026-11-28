/* Concept B motion. Everything is readable without this file; it only adds motion
   when GSAP loaded and the visitor has not asked for reduced motion. */
(function () {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (!window.gsap || !window.ScrollTrigger) return;
  var gsap = window.gsap, ST = window.ScrollTrigger;
  gsap.registerPlugin(ST);
  document.documentElement.classList.add("motion");

  // Smooth scroll, driven by GSAP's ticker so pins stay in sync.
  if (window.Lenis) {
    var lenis = new window.Lenis({ lerp: 0.1 });
    lenis.on("scroll", ST.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (ev) {
        var id = a.getAttribute("href");
        var el = id.length > 1 && document.getElementById(id.slice(1));
        if (!el) return;
        ev.preventDefault();
        lenis.scrollTo(el, { offset: -150 });
        el.setAttribute("tabindex", "-1");
        el.focus({ preventScroll: true });
        history.replaceState(null, "", id);
      });
    });
  }

  // Headline: words rise out of their own line box.
  gsap.from(".h-split .w", { yPercent: 105, duration: 1.1, ease: "expo.out", stagger: 0.045, delay: 0.05 });
  gsap.from(".hero-in > :not(h1)", { opacity: 0, y: 18, duration: 0.9, ease: "power3.out", stagger: 0.06, delay: 0.35 });

  // Generic reveals.
  gsap.set(".reveal", { opacity: 0, y: 26 });
  ST.batch(".reveal", {
    start: "top 90%", once: true,
    onEnter: function (b) { gsap.to(b, { opacity: 1, y: 0, duration: 0.9, ease: "power3.out", stagger: 0.07, overwrite: true }); }
  });

  // Hero: the screen lifts from a tilt to flat as you scroll, the phone drifts.
  var hd = document.querySelector(".hero-desk");
  if (hd) {
    gsap.fromTo(hd, { rotateX: 24, scale: 0.92, y: 30 }, {
      rotateX: 0, scale: 1, y: 0, ease: "none",
      scrollTrigger: { trigger: ".hero-stage", start: "top 95%", end: "top 25%", scrub: 0.6 }
    });
    gsap.fromTo(".hero-phone", { y: 0 }, {
      y: -100, ease: "none",
      scrollTrigger: { trigger: ".hero-stage", start: "top 90%", end: "bottom top", scrub: 0.6 }
    });
  }

  var mm = gsap.matchMedia();

  // The pinned device stage: one job, five beats.
  mm.add("(min-width: 960px) and (min-height: 620px)", function () {
    var sec = document.querySelector(".stage");
    if (!sec) return;
    var beats = gsap.utils.toArray(".beat", sec);
    var rail = gsap.utils.toArray(".rail li", sec);
    sec.classList.add("is-live");
    gsap.set(beats.slice(1), { opacity: 0 });
    var tl = gsap.timeline({
      defaults: { ease: "power2.inOut", duration: 1 },
      scrollTrigger: {
        trigger: sec.querySelector(".stage-pin"), start: "top top",
        end: "+=" + beats.length * 90 + "%", pin: true, scrub: 0.7
      },
      onUpdate: function () {
        var i = Math.min(beats.length - 1, Math.round(tl.time()));
        rail.forEach(function (r, k) { r.classList.toggle("is-on", k === i); });
      }
    });
    rail[0] && rail[0].classList.add("is-on");
    beats.forEach(function (b, i) {
      if (!i) return;
      var prev = beats[i - 1];
      // Out over [i-0.6, i-0.3], in over [i-0.3, i], then hold: copy never overlaps.
      tl.to(prev.querySelector(".beat-copy"), { y: -50, opacity: 0, duration: 0.3 }, i - 0.6)
        .to(prev.querySelector(".beat-shot"), { scale: 0.9, opacity: 0, filter: "blur(6px)", duration: 0.3 }, i - 0.6)
        .set(prev, { opacity: 0 }, i - 0.3)
        .set(b, { opacity: 1 }, i - 0.3)
        .fromTo(b.querySelector(".beat-copy"), { y: 60, opacity: 0 }, { y: 0, opacity: 1, duration: 0.3 }, i - 0.3)
        .fromTo(b.querySelector(".beat-shot"), { scale: 1.08, opacity: 0, filter: "blur(8px)" }, { scale: 1, opacity: 1, filter: "blur(0px)", duration: 0.3 }, i - 0.3);
    });
    tl.to({}, { duration: 0.4 });
    return function () { sec.classList.remove("is-live"); };
  });

  // Website + CRM meet in the middle as each pair scrolls into view.
  mm.add("(min-width: 760px)", function () {
    gsap.utils.toArray(".pair-vis, .ind-vis").forEach(function (v) {
      var a = v.children[0], b = v.children[1];
      var st = { trigger: v, start: "top 95%", end: "top 45%", scrub: 0.6 };
      if (v.classList.contains("ind-vis")) {
        gsap.fromTo(a, { x: -60, rotateY: 8 }, { x: 0, rotateY: 0, ease: "none", scrollTrigger: st });
        gsap.fromTo(b, { x: 60, rotateY: -8 }, { x: 0, rotateY: 0, ease: "none", scrollTrigger: st });
      } else {
        gsap.fromTo(b, { x: 30, y: 30 }, { x: 0, y: 0, ease: "none", scrollTrigger: st });
      }
    });
    gsap.utils.toArray(".fan").forEach(function (f) {
      gsap.from(f.children, { y: 80, opacity: 0, stagger: 0.12, ease: "none", scrollTrigger: { trigger: f, start: "top 90%", end: "top 45%", scrub: 0.6 } });
    });
  });

  // The price: arrives big and sharpens, the glow swells behind it.
  gsap.utils.toArray(".price").forEach(function (p) {
    var n = p.querySelector(".mega-n");
    if (n) gsap.fromTo(n, { scale: 0.7, opacity: 0.15, filter: "blur(14px)" }, {
      scale: 1, opacity: 1, filter: "blur(0px)", ease: "none",
      scrollTrigger: { trigger: p, start: "top 85%", end: "top 20%", scrub: 0.6 }
    });
    var g = p.querySelector(".price-glow");
    if (g) gsap.fromTo(g, { scale: 0.5, opacity: 0.2 }, { scale: 1.1, opacity: 1, ease: "none", scrollTrigger: { trigger: p, start: "top bottom", end: "bottom top", scrub: true } });
  });

  // Layout can shift as lazy images load; let pins re-measure.
  window.addEventListener("load", function () { ST.refresh(); });
})();
