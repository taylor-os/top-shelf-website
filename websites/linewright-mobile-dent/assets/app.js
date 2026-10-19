/* Linewright: Lenis + GSAP, reflection-line board, hail, before/after, damage picker, photo quote. Reduced-motion and no-JS safe. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.remove("no-js"); root.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var hasGSAP = window.gsap && window.ScrollTrigger;
  var finePointer = window.matchMedia("(pointer: fine)").matches;
  if (!reduce && document.querySelector(".board")) root.classList.add("js-pin");

  /* ---- Lenis smooth scroll ---- */
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

  /* ---- Header state ---- */
  var header = document.querySelector(".header");
  function onScroll() { if (header) header.classList.toggle("scrolled", window.scrollY > 40); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* ---- Mobile drawer ---- */
  var drawer = document.querySelector(".drawer"), openBtn = document.querySelector(".nav-toggle"), closeBtn = document.querySelector(".drawer__close");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) open ? lenis.stop() : lenis.start();
    if (open && closeBtn) closeBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); if (openBtn) openBtn.focus(); });
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && drawer.classList.contains("open")) setDrawer(false); });

  /* ---- Anchor scroll ---- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var id = a.getAttribute("href"); if (id.length < 2) return;
      var el = document.querySelector(id); if (!el) return;
      e.preventDefault();
      if (lenis) lenis.scrollTo(el, { offset: -90 }); else el.scrollIntoView({ behavior: reduce ? "auto" : "smooth" });
    });
  });

  /* ---- Reveal ---- */
  var revealEls = document.querySelectorAll("[data-reveal],[data-reveal-stagger]");
  if (reduce || !("IntersectionObserver" in window)) revealEls.forEach(function (el) { el.classList.add("in"); });
  else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute("data-reveal-stagger")) Array.prototype.forEach.call(el.children, function (c, i) { c.style.transitionDelay = (i * 0.08) + "s"; });
        el.classList.add("in"); io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Count-up (values are seeded in the HTML) ---- */
  function animateCount(el) {
    var raw = el.getAttribute("data-count"), target = parseFloat(raw), dec = (raw.split(".")[1] || "").length;
    if (reduce) return;
    var start = null;
    function fmt(v) { return v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec }); }
    (function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / 1600, 1);
      el.textContent = fmt(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    })(performance.now());
  }
  var counters = document.querySelectorAll("[data-count]");
  if (counters.length && "IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { animateCount(en.target); cio.unobserve(en.target); } });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---- Hero rotating word ---- */
  var rot = document.querySelector("[data-rotate]");
  if (rot && !reduce) {
    var words = JSON.parse(rot.getAttribute("data-rotate")), wi = 0;
    setInterval(function () {
      wi = (wi + 1) % words.length;
      rot.style.transition = "opacity .3s, transform .3s"; rot.style.opacity = "0"; rot.style.transform = "translateY(-10px)";
      setTimeout(function () {
        rot.textContent = words[wi]; rot.style.transform = "translateY(10px)";
        requestAnimationFrame(function () { rot.style.opacity = "1"; rot.style.transform = "none"; });
      }, 300);
    }, 2600);
  }

  /* ---- Hero parallax ---- */
  if (hasGSAP && !reduce) {
    if (!lenis) gsap.registerPlugin(ScrollTrigger);
    var heroImg = document.querySelector(".hero__media img");
    if (heroImg) gsap.to(heroImg, { yPercent: -10, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    var heroCard = document.querySelector(".hero__card");
    if (heroCard) gsap.from(heroCard, { y: 40, opacity: 0, duration: 1, delay: .4, ease: "power3.out" });
    var hHead = document.querySelector(".hero h1");
    if (hHead) gsap.from(hHead, { y: 30, opacity: 0, duration: 1.1, ease: "power3.out" });
  }

  function onVisible(el, cb) {
    if (!("IntersectionObserver" in window)) { cb(true); return; }
    new IntersectionObserver(function (en) { cb(en[0].isIntersecting); }).observe(el);
  }
  function sizeCanvas(cv) {
    var dpr = Math.min(window.devicePixelRatio || 1, 2), r = cv.getBoundingClientRect();
    cv.width = Math.round(r.width * dpr); cv.height = Math.round(r.height * dpr);
    var ctx = cv.getContext("2d"); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    return { ctx: ctx, w: r.width, h: r.height };
  }

  /* ---- Reflection-line board: a dent bends the reflected lines; scroll straightens them ---- */
  var board = document.querySelector(".board");
  if (board) {
    var cv = board.querySelector("canvas"), steps = board.querySelectorAll(".board__steps li"), meter = board.querySelector(".board__meter");
    var S = sizeCanvas(cv), progress = 0, live = false, dirty = true;
    var cur = { x: -9, y: -9, a: 0, t: 0 };
    window.addEventListener("resize", function () { S = sizeCanvas(cv); dirty = true; });
    if (finePointer && !reduce) {
      cv.addEventListener("pointermove", function (e) { var r = cv.getBoundingClientRect(); cur.x = e.clientX - r.left; cur.y = e.clientY - r.top; cur.t = 1; dirty = true; });
      cv.addEventListener("pointerleave", function () { cur.t = 0; dirty = true; });
    }
    function dentAt() { var wide = S.w > 860; return { x: S.w * (wide ? 0.68 : 0.5), y: S.h * (wide ? 0.5 : 0.25), r: Math.min(S.w, S.h) * (wide ? 0.2 : 0.3) }; }
    function draw() {
      var ctx = S.ctx, w = S.w, h = S.h, d = dentAt();
      var e = Math.min(Math.max((progress - 0.08) / 0.74, 0), 1);
      var a = reduce ? 1.1 : 1.35 * Math.pow(1 - e, 1.6);
      ctx.clearRect(0, 0, w, h);
      var gap = Math.max(h / 22, 22), lw = gap * 0.36, first = (h % gap) / 2;
      var grad = ctx.createLinearGradient(0, 0, w, 0);
      grad.addColorStop(0, "rgba(233,237,242,0.06)"); grad.addColorStop(0.35, "rgba(233,237,242,0.55)");
      grad.addColorStop(0.7, "rgba(233,237,242,0.75)"); grad.addColorStop(1, "rgba(233,237,242,0.12)");
      var nearest = Math.round((d.y - first) / gap);
      ctx.lineCap = "round"; ctx.lineJoin = "round";
      for (var i = 0, y0 = first; y0 < h + gap; i++, y0 += gap) {
        ctx.beginPath();
        for (var x = -10; x <= w + 10; x += 5) {
          var dx = x - d.x, dy = y0 - d.y, wgt = Math.exp(-(dx * dx + dy * dy) / (d.r * d.r));
          var y = y0 + dy * a * wgt + Math.sin(dx / d.r * 2.4) * d.r * 0.08 * a * wgt;
          if (cur.a > 0.01) {
            var cx = x - cur.x, cy = y0 - cur.y, cr = d.r * 0.55, cw = Math.exp(-(cx * cx + cy * cy) / (cr * cr));
            y += cy * 1.2 * cur.a * cw;
          }
          x === -10 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
        }
        var isLime = i === nearest;
        ctx.strokeStyle = isLime ? "rgba(204,255,61," + (0.55 + 0.45 * e) + ")" : grad;
        ctx.lineWidth = isLime ? lw * 0.8 : lw;
        ctx.stroke();
      }
      steps.forEach(function (li, k) { li.classList.toggle("on", reduce || progress >= [0, 0.34, 0.72][k]); });
      if (meter) meter.style.setProperty("--p", reduce ? 1 : e.toFixed(3));
    }
    function readProgress() {
      if (reduce) return;
      var r = board.getBoundingClientRect(), total = r.height - window.innerHeight;
      var p = total > 0 ? Math.min(Math.max(-r.top / total, 0), 1) : 0;
      if (Math.abs(p - progress) > 0.0005) { progress = p; dirty = true; }
    }
    function loop() {
      if (!live) return;
      readProgress();
      var na = cur.a + (cur.t - cur.a) * 0.12;
      if (Math.abs(na - cur.a) > 0.001) { cur.a = na; dirty = true; }
      if (dirty) { draw(); dirty = false; }
      requestAnimationFrame(loop);
    }
    draw();
    if (!reduce) onVisible(board, function (v) { if (v && !live) { live = true; requestAnimationFrame(loop); } else if (!v) live = false; });
  }

  /* ---- Hail canvas ---- */
  var hc = document.querySelector(".hail-canvas");
  if (hc && !reduce) {
    var H = sizeCanvas(hc), stones = [], hlive = false;
    function seed() { stones = []; var n = Math.round(H.w / 16); for (var i = 0; i < n; i++) stones.push({ x: Math.random() * H.w, y: Math.random() * H.h, v: 3 + Math.random() * 5, r: 1 + Math.random() * 2.6 }); }
    seed();
    window.addEventListener("resize", function () { H = sizeCanvas(hc); seed(); });
    (function hloop() {
      if (hlive) {
        var c = H.ctx; c.clearRect(0, 0, H.w, H.h);
        stones.forEach(function (s) {
          s.y += s.v; s.x -= s.v * 0.28;
          if (s.y > H.h + 10) { s.y = -10; s.x = Math.random() * (H.w + 200); }
          c.strokeStyle = "rgba(233,237,242," + (0.1 + s.r * 0.05) + ")"; c.lineWidth = s.r * 0.7;
          c.beginPath(); c.moveTo(s.x + s.v * 2.2, s.y - s.v * 8); c.lineTo(s.x, s.y); c.stroke();
          c.fillStyle = "rgba(240,244,248," + (0.45 + s.r * 0.12) + ")";
          c.beginPath(); c.arc(s.x, s.y, s.r, 0, 6.283); c.fill();
        });
      }
      requestAnimationFrame(hloop);
    })();
    onVisible(hc, function (v) { hlive = v; });
  }

  /* ---- Before / after sliders ---- */
  document.querySelectorAll(".ba").forEach(function (ba) {
    var input = ba.querySelector("input[type=range]"), touched = false;
    function set(v) { ba.style.setProperty("--pos", v + "%"); }
    input.addEventListener("input", function () { touched = true; set(input.value); });
    if (!reduce && "IntersectionObserver" in window) {
      var bio = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return; bio.disconnect();
        var t0 = null;
        (function sweep(ts) {
          if (touched) return;
          if (!t0) t0 = ts;
          var p = Math.min((ts - t0) / 2200, 1), v = 50 + 32 * Math.sin(p * Math.PI * 2) * (1 - p);
          set(v); input.value = Math.round(v);
          if (p < 1) requestAnimationFrame(sweep); else { set(50); input.value = 50; }
        })(performance.now());
      }, { threshold: 0.5 });
      bio.observe(ba);
    }
  });

  /* ---- Tabs (before/after sets) ---- */
  document.querySelectorAll("[role=tablist]").forEach(function (list) {
    var tabs = list.querySelectorAll("[role=tab]");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) {
          var on = t === tab; t.setAttribute("aria-selected", on ? "true" : "false"); t.tabIndex = on ? 0 : -1;
          document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
        });
      });
      tab.addEventListener("keydown", function (e) {
        var i = Array.prototype.indexOf.call(tabs, tab), n = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : null;
        if (n === null) return; n = (n + tabs.length) % tabs.length; tabs[n].focus(); tabs[n].click();
      });
    });
  });

  /* ---- Damage picker ---- */
  var pickBtns = document.querySelectorAll("[data-pick]");
  if (pickBtns.length) {
    var choose = function (id) {
      pickBtns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-pick") === id ? "true" : "false"); });
      document.querySelectorAll(".pick").forEach(function (p) { p.classList.toggle("on", p.id === "pick-" + id); });
    };
    pickBtns.forEach(function (b) { b.addEventListener("click", function () { choose(b.getAttribute("data-pick")); }); });
    choose(pickBtns[0].getAttribute("data-pick"));
  }

  /* ---- Photo quote: previews + demo submit ---- */
  var drop = document.querySelector(".drop");
  if (drop) {
    var fileIn = drop.querySelector("input[type=file]"), thumbs = document.querySelector(".thumbs"), count = drop.querySelector("[data-count-label]");
    fileIn.addEventListener("change", function () {
      thumbs.innerHTML = "";
      Array.prototype.slice.call(fileIn.files, 0, 8).forEach(function (f) {
        if (!/^image\//.test(f.type)) return;
        var img = document.createElement("img"); img.alt = "Your photo: " + f.name; img.src = URL.createObjectURL(f); thumbs.appendChild(img);
      });
      if (count) count.textContent = fileIn.files.length ? fileIn.files.length + " photo" + (fileIn.files.length > 1 ? "s" : "") + " added" : "Tap to add photos";
    });
    ["dragenter", "dragover"].forEach(function (ev) { drop.addEventListener(ev, function () { drop.classList.add("over"); }); });
    ["dragleave", "drop"].forEach(function (ev) { drop.addEventListener(ev, function () { drop.classList.remove("over"); }); });
  }
  var form = document.querySelector("[data-demo-form]");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var ok = form.querySelector("[data-form-ok]");
    form.querySelectorAll("input,select,textarea,button").forEach(function (el) { el.disabled = true; });
    if (ok) { ok.hidden = false; ok.focus(); }
  });

  var y = document.querySelector("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
