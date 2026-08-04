/* =========================================================================
   Dealer Dashboard — auth gate, tabs, inventory manager (client-side demo)
   ========================================================================= */
(function () {
  "use strict";
  var INV = window.ReidsInventory;

  /* ---- Auth gate ---- */
  if (localStorage.getItem("reids_auth") !== "1") { location.replace("login.html"); return; }
  var email = localStorage.getItem("reids_user") || "owner@reidsautoconnection.com";
  document.getElementById("duser").textContent = email;
  document.getElementById("dava").textContent = (email[0] || "R").toUpperCase();

  var $ = function (id) { return document.getElementById(id); };
  function toast(msg) { var t = $("toast"); $("toastMsg").textContent = msg; t.classList.add("show"); clearTimeout(t._t); t._t = setTimeout(function () { t.classList.remove("show"); }, 2600); }

  /* ---- Tabs ---- */
  var TITLES = { overview:"Overview", leads:"Leads", followups:"Follow-Ups", sales:"New Sales", reviews:"Reviews", inventory:"Update Inventory" };
  var navlinks = document.querySelectorAll(".dnav a[data-page]");
  function go(page) {
    document.querySelectorAll(".dpage").forEach(function (p) { p.classList.remove("active"); });
    var el = $("page-" + page); if (el) el.classList.add("active");
    navlinks.forEach(function (a) { a.classList.toggle("active", a.dataset.page === page); });
    $("dtitle").textContent = TITLES[page] || "Dashboard";
    closeSide();
    window.scrollTo(0, 0);
    if (page === "inventory") renderInv();
  }
  navlinks.forEach(function (a) { a.addEventListener("click", function () { go(a.dataset.page); }); });
  document.querySelectorAll("[data-jump]").forEach(function (a) { a.addEventListener("click", function () { go(a.dataset.jump); }); });

  /* ---- Mobile sidebar ---- */
  var side = $("dside"), scrim = $("dscrim");
  function openSide() { side.classList.add("open"); scrim.classList.add("open"); }
  function closeSide() { side.classList.remove("open"); scrim.classList.remove("open"); }
  $("dburger").addEventListener("click", openSide);
  scrim.addEventListener("click", closeSide);

  /* ---- Logout ---- */
  $("logout").addEventListener("click", function () { localStorage.removeItem("reids_auth"); localStorage.removeItem("reids_user"); location.href = "login.html"; });

  /* ---- Follow-up checkboxes ---- */
  document.querySelectorAll(".task input[type=checkbox]").forEach(function (c) {
    c.addEventListener("change", function () { c.closest(".task").classList.toggle("done", c.checked); });
  });
  document.querySelectorAll(".drev__reply").forEach(function (b) { b.addEventListener("click", function () { toast("Reply drafted — send from Google Business (demo)"); }); });

  /* =======================================================================
     INVENTORY MANAGER
     ======================================================================= */
  var invman = $("invman");
  function renderInv() {
    var list = INV.all();
    $("inv-total").textContent = "· " + list.length + " vehicles";
    invman.innerHTML = list.map(function (v) {
      var img = v.img ? '<img class="invrow__img" src="' + v.img + '" alt="" onerror="this.style.visibility=\'hidden\'">' : '<div class="invrow__img"></div>';
      return '<div class="invrow" data-id="' + v.id + '">' + img +
        '<div class="invrow__t"><b>' + v.year + " " + v.make + " " + v.model + " " + (v.trim || "") + (v.sold ? ' <span class="tag-sold">SOLD</span>' : (v.custom ? ' <span class="tag-sold" style="color:var(--aurora-b);background:rgba(35,201,160,.12);border-color:rgba(35,201,160,.3);">NEW</span>' : "")) +
        "</b><small>" + INV.money(v.price) + " · " + INV.miles(v.mileage) + " · " + v.drivetrain + " · " + v.ext + "</small></div>" +
        '<div class="invrow__act">' +
          '<button class="icobtn" data-act="sold" title="Toggle sold">' + (v.sold ? "↺" : "✓") + "</button>" +
          '<button class="icobtn danger" data-act="del" title="Remove"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2m3 0v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6"/></svg></button>' +
        "</div></div>";
    }).join("");
    invman.querySelectorAll(".invrow").forEach(function (row) {
      var id = row.dataset.id;
      row.querySelector('[data-act="sold"]').addEventListener("click", function () { INV.toggleSold(id); renderInv(); toast("Availability updated"); });
      row.querySelector('[data-act="del"]').addEventListener("click", function () { INV.remove(id); renderInv(); toast("Vehicle removed from website"); });
    });
  }
  $("resetDemo").addEventListener("click", function () { INV.resetDemo(); renderInv(); toast("Demo inventory reset"); });

  /* ---- Add-vehicle modal ---- */
  var addveh = $("addveh"), photos = [];
  function openAdd() { addveh.classList.add("open"); document.body.style.overflow = "hidden"; }
  function closeAdd() { addveh.classList.remove("open"); document.body.style.overflow = ""; }
  $("addBtn").addEventListener("click", openAdd);
  $("addClose").addEventListener("click", closeAdd);
  $("addCancel").addEventListener("click", closeAdd);
  addveh.addEventListener("click", function (e) { if (e.target === addveh) closeAdd(); });

  var drop = $("drop"), photoInput = $("photo"), preview = $("preview");
  drop.addEventListener("click", function () { photoInput.click(); });
  photoInput.addEventListener("change", function () {
    var files = Array.prototype.slice.call(photoInput.files);
    files.forEach(function (f) {
      resizeImage(f, 1100, function (dataUrl) {
        photos.push(dataUrl);
        var im = document.createElement("img"); im.src = dataUrl; preview.appendChild(im);
      });
    });
  });
  function resizeImage(file, maxW, cb) {
    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        var scale = Math.min(1, maxW / img.width);
        var c = document.createElement("canvas");
        c.width = Math.round(img.width * scale); c.height = Math.round(img.height * scale);
        c.getContext("2d").drawImage(img, 0, 0, c.width, c.height);
        cb(c.toDataURL("image/jpeg", 0.82));
      };
      img.src = e.target.result;
    };
    reader.readAsDataURL(file);
  }

  $("addForm").addEventListener("submit", function (e) {
    e.preventDefault();
    var f = e.target;
    var mileage = +f.mileage.value;
    var v = {
      year: +f.year.value, make: f.make.value.trim(), model: f.model.value.trim(), trim: f.trim.value.trim(),
      body: f.body.value, price: +f.price.value, mileage: mileage, drivetrain: f.drivetrain.value,
      transmission: f.transmission.value, fuel: f.fuel.value, ext: f.ext.value.trim() || "—", int: "—",
      mpg: f.mpg.value.trim(), engine: f.engine.value.trim() || "—", vin: "—",
      features: f.features.value.split(",").map(function (s) { return s.trim(); }).filter(Boolean),
      img: photos[0] || "", tag: mileage && mileage < 30000 ? "Low miles" : "$0 DOWN"
    };
    INV.add(v);
    closeAdd(); f.reset(); photos = []; preview.innerHTML = "";
    renderInv();
    toast("✓ " + v.year + " " + v.make + " " + v.model + " posted to the website");
  });

  renderInv();
})();
