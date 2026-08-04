/* =========================================================================
   Public inventory page — filtering, sorting, rendering, detail modal
   ========================================================================= */
(function () {
  "use strict";
  var INV = window.ReidsInventory;
  if (!INV) return;

  var $ = function (id) { return document.getElementById(id); };
  var grid = $("inv-grid"), count = $("inv-count");
  var els = {
    search: $("f-search"), make: $("f-make"), body: $("f-body"), price: $("f-price"),
    year: $("f-year"), miles: $("f-miles"), drive: $("f-drive"), sort: $("f-sort")
  };

  /* Populate Make dropdown from data */
  (function fillMakes() {
    var makes = {};
    INV.available().forEach(function (v) { makes[v.make] = true; });
    Object.keys(makes).sort().forEach(function (m) {
      var o = document.createElement("option"); o.value = m; o.textContent = m; els.make.appendChild(o);
    });
  })();

  function priceBracket(p) {
    switch (p) {
      case "u20": return function (v) { return v.price < 20000; };
      case "20-30": return function (v) { return v.price >= 20000 && v.price < 30000; };
      case "30-40": return function (v) { return v.price >= 30000 && v.price < 40000; };
      case "40p": return function (v) { return v.price >= 40000; };
      default: return function () { return true; };
    }
  }

  function apply() {
    var list = INV.available();
    var q = (els.search.value || "").trim().toLowerCase();
    if (q) list = list.filter(function (v) {
      return (v.year + " " + v.make + " " + v.model + " " + v.trim + " " + v.body + " " + v.ext).toLowerCase().indexOf(q) !== -1;
    });
    if (els.make.value) list = list.filter(function (v) { return v.make === els.make.value; });
    if (els.body.value) list = list.filter(function (v) { return v.body === els.body.value; });
    list = list.filter(priceBracket(els.price.value));
    if (els.year.value) list = list.filter(function (v) { return v.year >= +els.year.value; });
    if (els.miles.value) list = list.filter(function (v) { return v.mileage <= +els.miles.value; });
    if (els.drive.value) {
      list = list.filter(function (v) {
        return els.drive.value === "4" ? (v.drivetrain === "4x4" || v.drivetrain === "4WD") : v.drivetrain === els.drive.value;
      });
    }
    switch (els.sort.value) {
      case "plow": list.sort(function (a, b) { return a.price - b.price; }); break;
      case "phigh": list.sort(function (a, b) { return b.price - a.price; }); break;
      case "mlow": list.sort(function (a, b) { return a.mileage - b.mileage; }); break;
      case "ynew": list.sort(function (a, b) { return b.year - a.year; }); break;
    }
    render(list);
  }

  function card(v) {
    var hwy = (v.mpg || "").split("/")[1] || "";
    var img = v.img
      ? '<img src="' + v.img + '" alt="' + v.year + " " + v.make + " " + v.model + " " + v.trim + ' in ' + v.ext + '" loading="lazy" onerror="this.style.display=\'none\'">'
      : '<svg class="silh" width="150" height="70" viewBox="0 0 150 70" fill="currentColor"><path d="M15 50c0-6 5-9 9-14l8-11c3-4 8-6 13-6h26c6 0 11 3 14 8l7 12c4 1 20 5 27 9 4 2 6 5 6 9v3H15z"/><circle cx="42" cy="55" r="9" fill="#0a0e1c"/><circle cx="42" cy="55" r="5" fill="currentColor"/><circle cx="112" cy="55" r="9" fill="#0a0e1c"/><circle cx="112" cy="55" r="5" fill="currentColor"/></svg>';
    return '<article class="car reveal in" data-id="' + v.id + '" tabindex="0" role="button" aria-label="View ' + v.year + " " + v.make + " " + v.model + '">' +
      '<div class="car-photo"><span class="car-tag">' + (v.tag || "$0 DOWN") + "</span>" + img + "</div>" +
      '<div class="car-body"><span class="yr">' + v.year + " · " + INV.miles(v.mileage) + "</span>" +
      "<h3>" + v.make + " " + v.model + " " + v.trim + "</h3>" +
      '<div class="car-specs"><span>◈ ' + v.drivetrain + "</span><span>⛽ " + (hwy ? hwy + " MPG hwy" : v.fuel) + "</span><span>✦ " + v.ext + "</span></div>" +
      '<div class="car-price"><span class="amt">' + INV.money(v.price) + '</span><span class="est">Est. ' + INV.estPayment(v.price) + "<b>$0 down</b></span></div></div></article>";
  }

  function render(list) {
    count.textContent = list.length + (list.length === 1 ? " vehicle" : " vehicles");
    if (!list.length) { grid.innerHTML = '<p style="grid-column:1/-1;color:var(--text-soft);padding:40px 0;text-align:center;">No vehicles match those filters. <button class="btn btn-ghost" id="inv-clear2" style="margin-left:10px;">Clear filters</button></p>'; var c = $("inv-clear2"); if (c) c.onclick = reset; return; }
    grid.innerHTML = list.map(card).join("");
    grid.querySelectorAll(".car").forEach(function (el) {
      var v = list.find(function (x) { return x.id === el.dataset.id; });
      el.addEventListener("click", function () { openModal(v); });
      el.addEventListener("keydown", function (e) { if (e.key === "Enter") openModal(v); });
    });
  }

  function reset() {
    Object.keys(els).forEach(function (k) { els[k].value = ""; });
    els.sort.value = ""; apply();
  }

  /* ---- Detail modal ---- */
  var modal = $("veh-modal");
  function openModal(v) {
    var hwy = (v.mpg || "");
    modal.querySelector(".vm-body").innerHTML =
      '<div class="vm-photo">' + (v.img ? '<img src="' + v.img + '" alt="' + v.year + " " + v.make + " " + v.model + '" onerror="this.style.display=\'none\'">' : "") + '<span class="car-tag">' + (v.tag || "$0 DOWN") + '</span></div>' +
      '<div class="vm-info">' +
        '<span class="yr" style="color:var(--gold-soft);font-weight:600;font-size:13px;">' + v.year + " · " + INV.miles(v.mileage) + " · VIN " + (v.vin || "—") + "</span>" +
        "<h3 style=\"font-size:28px;margin:6px 0 4px;\">" + v.make + " " + v.model + " " + v.trim + "</h3>" +
        '<div class="vm-price">' + INV.money(v.price) + ' <span>· Est. ' + INV.estPayment(v.price) + " · $0 down</span></div>" +
        '<div class="vm-specs">' +
          spec("Body", v.body) + spec("Drivetrain", v.drivetrain) + spec("Transmission", v.transmission) +
          spec("Engine", v.engine) + spec("Fuel economy", hwy + " mpg") + spec("Exterior", v.ext) +
          spec("Interior", v.int) + spec("Fuel", v.fuel) +
        "</div>" +
        (v.features && v.features.length ? '<div class="vm-feat"><h4>Features</h4><ul>' + v.features.map(function (f) { return "<li>" + f + "</li>"; }).join("") + "</ul></div>" : "") +
        '<div class="vm-actions"><a class="btn btn-gold btn-lg" href="../get-approved.html">Get approved for this car</a><a class="btn btn-ghost btn-lg" href="tel:+19724361600">Call (972) 436-1600</a></div>' +
      "</div>";
    modal.classList.add("open"); document.body.style.overflow = "hidden";
  }
  function spec(k, val) { return '<div class="vm-spec"><span>' + k + "</span><b>" + (val || "—") + "</b></div>"; }
  function closeModal() { modal.classList.remove("open"); document.body.style.overflow = ""; }
  if (modal) {
    modal.querySelector(".vm-close").addEventListener("click", closeModal);
    modal.addEventListener("click", function (e) { if (e.target === modal) closeModal(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeModal(); });
  }

  /* Wire filters */
  Object.keys(els).forEach(function (k) { els[k].addEventListener(els[k].tagName === "INPUT" ? "input" : "change", apply); });
  var rb = $("f-reset"); if (rb) rb.addEventListener("click", reset);

  apply();
})();
