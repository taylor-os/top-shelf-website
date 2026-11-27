/* Kestrel Lane Detail Co. | sample site. Lenis + GSAP (optional), hero light streak, size pricing, before/after, booking form.
   Reduced-motion and no-JS safe: every price is in the HTML; JS only switches and totals. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.remove("no-js"); root.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var finePointer = window.matchMedia("(pointer: fine)").matches;
  var hasGSAP = !!(window.gsap && window.ScrollTrigger);

  /* The shop's price list (the CRM's sample menu). Cents, minutes. */
  var MENU = {
    full: { name: "Full detail", car: 18000, suv: 22000, truck: 25000, min: 180 },
    interior: { name: "Interior shampoo", car: 12000, suv: 12000, truck: 12000, min: 120 },
    exterior: { name: "Exterior wash and wax", car: 9000, suv: 9000, truck: 9000, min: 90 },
    ceramic: { name: "Ceramic coating, 3-year", car: 90000, suv: 90000, truck: 90000, min: 480 }
  };
  var ADDONS = {
    pet: { name: "Pet hair removal", cents: 4000, min: 30 },
    headlight: { name: "Headlight restore", cents: 6000, min: 60 },
    engine: { name: "Engine bay", cents: 5000, min: 60 }
  };
  var SIZES = { car: "Car", suv: "SUV", truck: "Truck or van" };
  var DEPOSIT = 0.25, CLOSE = 17 * 60;

  function money(c, whole) { var d = c / 100; return "$" + (whole && c % 100 === 0 ? d.toLocaleString("en-US") : d.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })); }
  function deposit(c) { return Math.round(c * DEPOSIT); }
  function dur(m) { var h = Math.floor(m / 60), r = m % 60; return (h ? h + " h" : "") + (h && r ? " " : "") + (r ? r + " min" : ""); }
  function clock(m) { var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? "PM" : "AM", h12 = h % 12 || 12; return h12 + ":" + (mm < 10 ? "0" : "") + mm + " " + ap; }

  /* ---- Lenis ---- */
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

  /* ---- Drawer ---- */
  var drawer = document.querySelector(".drawer"), openBtn = document.querySelector(".nav-toggle"), closeBtn = document.querySelector(".drawer__close");
  function setDrawer(open) {
    if (!drawer) return;
    drawer.classList.toggle("open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    document.body.style.overflow = open ? "hidden" : "";
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (lenis) { if (open) lenis.stop(); else lenis.start(); }
    if (open && closeBtn) setTimeout(function () { closeBtn.focus(); }, 60); // after visibility flips
  }
  if (openBtn) openBtn.addEventListener("click", function () { setDrawer(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setDrawer(false); if (openBtn) openBtn.focus(); });
  if (drawer) drawer.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setDrawer(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer && drawer.classList.contains("open")) { setDrawer(false); if (openBtn) openBtn.focus(); } });

  /* ---- Reveal ---- */
  var revealEls = document.querySelectorAll("[data-reveal],[data-reveal-stagger]");
  if (reduce || !("IntersectionObserver" in window)) revealEls.forEach(function (el) { el.classList.add("in"); });
  else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute("data-reveal-stagger")) Array.prototype.forEach.call(el.children, function (c, i) { c.style.transitionDelay = (i * 0.07) + "s"; });
        el.classList.add("in"); io.unobserve(el);
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---- Hero: light streak follows the pointer; GSAP entrance ---- */
  var hero = document.querySelector(".hero");
  if (hero && !reduce) {
    var streak = hero.querySelector(".streak"), art = hero.querySelector(".panel-art");
    if (streak && art && finePointer) {
      hero.addEventListener("pointermove", function (e) {
        var r = art.getBoundingClientRect(), p = (e.clientX - r.left) / r.width;
        hero.classList.add("tracking");
        streak.style.transform = "translateX(" + Math.round(-200 + p * 1500) + "px)";
      });
      hero.addEventListener("pointerleave", function () { hero.classList.remove("tracking"); streak.style.transform = ""; });
    }
    if (hasGSAP) {
      gsap.from(".hero h1", { y: 34, opacity: 0, duration: 1.1, ease: "power3.out" });
      gsap.from(".hero .lede, .hero__actions, .hero__facts", { y: 20, opacity: 0, duration: .9, delay: .2, stagger: .08, ease: "power3.out" });
      gsap.from(".booked", { y: 40, opacity: 0, duration: 1, delay: .45, ease: "power3.out" });
      gsap.from(".bead-layer use", { scale: 0, opacity: 0, duration: .7, delay: .3, stagger: { each: .025, from: "random" }, ease: "back.out(2)" });
      gsap.to(".panel-art", { yPercent: 8, ease: "none", scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true } });
    }
  }

  /* ---- Size switch (home readout + packages table) ---- */
  document.querySelectorAll("[data-sizer]").forEach(function (box) {
    var btns = box.querySelectorAll("[data-size]");
    function pick(size) {
      btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-size") === size ? "true" : "false"); });
      var full = MENU.full;
      box.querySelectorAll("[data-out]").forEach(function (el) {
        var k = el.getAttribute("data-out");
        if (k === "price") el.textContent = money(full[size], true);
        if (k === "deposit") el.textContent = money(deposit(full[size]));
        if (k === "size") el.textContent = SIZES[size];
        if (k === "rest") el.textContent = money(full[size] - deposit(full[size]));
      });
      box.querySelectorAll("[data-col]").forEach(function (c) { c.classList.toggle("on", c.getAttribute("data-col") === size); });
      box.querySelectorAll("[data-book-link]").forEach(function (a) { a.setAttribute("href", "book.html?package=full&size=" + size); });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { pick(b.getAttribute("data-size")); }); });
  });

  /* ---- Before / after ---- */
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
          var p = Math.min((ts - t0) / 2200, 1), v = 50 + 30 * Math.sin(p * Math.PI * 2) * (1 - p);
          set(v); input.value = Math.round(v);
          if (p < 1) requestAnimationFrame(sweep); else { set(50); input.value = 50; }
        })(performance.now());
      }, { threshold: 0.5 });
      bio.observe(ba);
    }
  });

  /* ---- Booking form ---- */
  var form = document.querySelector("[data-book]");
  if (form) {
    var out = function (k) { return form.querySelector("[data-sum=" + k + "]"); };
    var q = new URLSearchParams(location.search);
    if (SIZES[q.get("size")]) { var s = form.querySelector("input[name=size][value=" + q.get("size") + "]"); if (s) s.checked = true; }
    if (MENU[q.get("package")]) { var pk = form.querySelector("input[name=package][value=" + q.get("package") + "]"); if (pk) pk.checked = true; }
    var day = form.querySelector("input[name=day]");
    if (day) { var t = new Date(); t.setDate(t.getDate() + 1); day.min = t.getFullYear() + "-" + ("0" + (t.getMonth() + 1)).slice(-2) + "-" + ("0" + t.getDate()).slice(-2); }

    var update = function () {
      var size = (form.querySelector("input[name=size]:checked") || {}).value || "suv";
      form.querySelectorAll("[data-pkg-price]").forEach(function (el) { el.textContent = money(MENU[el.getAttribute("data-pkg-price")][size], true); });
      var pkgIn = form.querySelector("input[name=package]:checked"), pkg = pkgIn ? MENU[pkgIn.value] : null;
      var adds = Array.prototype.map.call(form.querySelectorAll("input[name=addon]:checked"), function (i) { return ADDONS[i.value]; });
      var total = pkg ? pkg[size] : 0, mins = pkg ? pkg.min : 0;
      adds.forEach(function (a) { total += a.cents; mins += a.min; });

      // A time only works if the job ends by close.
      var timeNote = form.querySelector("[data-time-note]"), dropped = false, fits = 0;
      form.querySelectorAll("input[name=time]").forEach(function (r) {
        var start = parseInt(r.getAttribute("data-min"), 10), tooLate = !!pkg && start + mins > CLOSE;
        r.disabled = tooLate;
        if (!tooLate) fits++;
        if (tooLate && r.checked) { r.checked = false; dropped = true; }
      });
      if (timeNote) timeNote.textContent = pkg && !fits ? "This combination takes about " + dur(mins) + ", longer than we can fit in one day. Call 123-456-7890 and we'll set it up." : pkg ? "Takes about " + dur(mins) + ". Times that would run past 5:00 PM are greyed out." + (dropped ? " Your earlier time no longer fits, so pick another." : "") : "Pick a package first and we'll show how long it takes.";

      var timeIn = form.querySelector("input[name=time]:checked");
      var when = "Pick a day and time";
      if (day && day.value) {
        var d = new Date(day.value + "T12:00:00");
        when = d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric" }) + (timeIn ? " · " + clock(parseInt(timeIn.getAttribute("data-min"), 10)) : " · pick a time");
      } else if (timeIn) when = "Pick a day · " + clock(parseInt(timeIn.getAttribute("data-min"), 10));

      var lines = out("lines");
      lines.innerHTML = "";
      function line(label, val) { var div = document.createElement("div"), sp = document.createElement("span"), b = document.createElement("b"); sp.textContent = label; b.textContent = val; div.appendChild(sp); div.appendChild(b); lines.appendChild(div); }
      line("Vehicle", SIZES[size]);
      if (pkg) line(pkg.name, money(pkg[size]));
      else line("Package", "Not picked yet");
      adds.forEach(function (a) { line(a.name, "+" + money(a.cents)); });
      out("when").textContent = when;
      out("total").textContent = money(total);
      out("deposit").textContent = money(deposit(total));
      out("fine").textContent = pkg ? "Your " + money(deposit(total)) + " deposit holds this time and comes off your bill. The rest, " + money(total - deposit(total)) + ", is due at pickup." : "The deposit is 25% of your booking. It holds your time and comes off your bill.";
    };
    form.addEventListener("change", update);
    form.addEventListener("input", update);
    update();

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      // Every time can be greyed out, and native validation skips a fully disabled group.
      if (!form.querySelector("input[name=time]:checked:enabled")) {
        var note = form.querySelector("[data-time-note]");
        if (note) { note.setAttribute("tabindex", "-1"); note.scrollIntoView({ block: "center" }); note.focus({ preventScroll: true }); }
        return;
      }
      var ok = form.querySelector("[data-form-ok]");
      form.querySelectorAll("input,textarea,button").forEach(function (el) { el.disabled = true; });
      if (ok) { ok.hidden = false; ok.focus(); }
    });
  }

  var y = document.querySelector("[data-year]"); if (y) y.textContent = new Date().getFullYear();
})();
