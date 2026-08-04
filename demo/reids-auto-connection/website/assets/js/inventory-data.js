/* =========================================================================
   Reids Auto Connection — shared inventory store
   Seed data (12 real vehicles) + localStorage layer so the dashboard's
   "Add vehicle" posts live into the public inventory (client-side demo).
   ========================================================================= */
window.ReidsInventory = (function () {
  "use strict";
  var ADD_KEY = "reids_inv_added_v1";   // vehicles added via dashboard
  var HIDE_KEY = "reids_inv_hidden_v1"; // seed ids marked removed
  var SOLD_KEY = "reids_inv_sold_v1";   // ids marked sold

  // ---- Seed inventory (real makes/models w/ realistic specs) ----
  var SEED = [
    { id:"s1", year:2022, make:"Toyota", model:"Camry", trim:"SE", body:"Sedan", price:24988, mileage:31400, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Silver", int:"Black", mpg:"28/39", engine:"2.5L I4", vin:"4T1G11AK5NU******", tag:"$0 DOWN",
      features:["Apple CarPlay","Backup Camera","Lane Assist","Bluetooth","Alloy Wheels"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-1.webp" },
    { id:"s2", year:2021, make:"Honda", model:"Accord", trim:"Sport", body:"Sedan", price:23450, mileage:38900, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Modern Steel Gray", int:"Black", mpg:"29/35", engine:"1.5L Turbo I4", vin:"1HGCV1F3XMA******", tag:"$0 DOWN",
      features:["Apple CarPlay","Heated Seats","Backup Camera","Bluetooth","Keyless Start"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-2.webp" },
    { id:"s3", year:2022, make:"Ford", model:"F-150", trim:"XLT", body:"Truck", price:33450, mileage:42100, transmission:"Automatic", drivetrain:"4x4", fuel:"Gasoline", ext:"Velocity Blue", int:"Gray", mpg:"19/24", engine:"3.5L V6 EcoBoost", vin:"1FTFW1E85NF******", tag:"$0 DOWN",
      features:["Tow Package","Backup Camera","Apple CarPlay","Bed Liner","Running Boards"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-3.webp" },
    { id:"s4", year:2023, make:"Honda", model:"CR-V", trim:"EX", body:"SUV", price:28760, mileage:28700, transmission:"Automatic", drivetrain:"AWD", fuel:"Gasoline", ext:"Platinum White", int:"Black", mpg:"28/34", engine:"1.5L Turbo I4", vin:"5J6RW2H80PL******", tag:"Low miles",
      features:["Sunroof","Apple CarPlay","Heated Seats","Backup Camera","Blind Spot Monitor"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-4.webp" },
    { id:"s5", year:2021, make:"Nissan", model:"Altima", trim:"SV", body:"Sedan", price:19995, mileage:36715, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Super Black", int:"Charcoal", mpg:"28/39", engine:"2.5L I4", vin:"1N4BL4DV4MN******", tag:"$0 DOWN",
      features:["Backup Camera","Apple CarPlay","Blind Spot Monitor","Push Start","Alloy Wheels"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-5.webp" },
    { id:"s6", year:2022, make:"Chevrolet", model:"Silverado 1500", trim:"LT", body:"Truck", price:37900, mileage:33180, transmission:"Automatic", drivetrain:"4x4", fuel:"Gasoline", ext:"Black", int:"Jet Black", mpg:"16/20", engine:"5.3L V8", vin:"1GCUYDED9NZ******", tag:"$0 DOWN",
      features:["Tow Package","Backup Camera","Apple CarPlay","Bed Liner","Remote Start"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-6.webp" },
    { id:"s7", year:2023, make:"Toyota", model:"RAV4", trim:"XLE", body:"SUV", price:29450, mileage:21540, transmission:"Automatic", drivetrain:"AWD", fuel:"Gasoline", ext:"Ruby Flare Red", int:"Black", mpg:"27/35", engine:"2.5L I4", vin:"2T3P1RFV6PC******", tag:"Low miles",
      features:["Sunroof","Apple CarPlay","Heated Seats","Backup Camera","Lane Assist"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-7.webp" },
    { id:"s8", year:2021, make:"Jeep", model:"Grand Cherokee", trim:"Limited", body:"SUV", price:30988, mileage:44220, transmission:"Automatic", drivetrain:"4x4", fuel:"Gasoline", ext:"Bright White", int:"Black", mpg:"19/26", engine:"3.6L V6", vin:"1C4RJFBG5MC******", tag:"$0 DOWN",
      features:["Leather","Sunroof","Navigation","Backup Camera","Heated Seats"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-8.webp" },
    { id:"s9", year:2022, make:"Kia", model:"Sportage", trim:"LX", body:"SUV", price:23400, mileage:27900, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Steel Gray", int:"Black", mpg:"23/30", engine:"2.4L I4", vin:"KNDPMCAC9N7******", tag:"Low miles",
      features:["Apple CarPlay","Backup Camera","Bluetooth","Alloy Wheels","Keyless Entry"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-9.webp" },
    { id:"s10", year:2020, make:"Nissan", model:"Rogue", trim:"SV", body:"SUV", price:18995, mileage:51300, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Brilliant Silver", int:"Charcoal", mpg:"26/33", engine:"2.5L I4", vin:"JN8AT2MV0LW******", tag:"$0 DOWN",
      features:["Backup Camera","Apple CarPlay","Blind Spot Monitor","Heated Seats","Push Start"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-10.webp" },
    { id:"s11", year:2021, make:"Hyundai", model:"Elantra", trim:"SEL", body:"Sedan", price:17950, mileage:39000, transmission:"Automatic", drivetrain:"FWD", fuel:"Gasoline", ext:"Intense Blue", int:"Gray", mpg:"33/43", engine:"2.0L I4", vin:"5NPLM4AG7MH******", tag:"$0 DOWN",
      features:["Apple CarPlay","Backup Camera","Lane Assist","Bluetooth","Alloy Wheels"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-11.webp" },
    { id:"s12", year:2022, make:"Ford", model:"Explorer", trim:"XLT", body:"SUV", price:31200, mileage:35600, transmission:"Automatic", drivetrain:"4WD", fuel:"Gasoline", ext:"Agate Black", int:"Ebony", mpg:"21/28", engine:"2.3L Turbo I4", vin:"1FMSK8DH1NG******", tag:"$0 DOWN",
      features:["3rd Row Seating","Apple CarPlay","Backup Camera","Blind Spot Monitor","Remote Start"], img:"/demo/reids-auto-connection/website/assets/img/cars/car-12.webp" }
  ];

  function read(key) { try { return JSON.parse(localStorage.getItem(key)) || []; } catch (e) { return []; } }
  function write(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {} }

  function getAdded()  { return read(ADD_KEY); }
  function getHidden() { return read(HIDE_KEY); }
  function getSold()   { return read(SOLD_KEY); }

  /* Full visible inventory: added (newest first) + seed, minus hidden, w/ sold flag */
  function all() {
    var hidden = getHidden(), sold = getSold();
    var list = getAdded().concat(SEED).filter(function (v) { return hidden.indexOf(v.id) === -1; });
    list.forEach(function (v) { v.sold = sold.indexOf(v.id) !== -1; });
    return list;
  }
  function available() { return all().filter(function (v) { return !v.sold; }); }

  function add(v) {
    var added = getAdded();
    v.id = "u" + Date.now();
    v.custom = true;
    added.unshift(v);
    write(ADD_KEY, added);
    return v;
  }
  function remove(id) {
    var added = getAdded();
    var idx = added.findIndex(function (v) { return v.id === id; });
    if (idx > -1) { added.splice(idx, 1); write(ADD_KEY, added); return; }
    var hidden = getHidden(); if (hidden.indexOf(id) === -1) { hidden.push(id); write(HIDE_KEY, hidden); }
  }
  function toggleSold(id) {
    var sold = getSold(), i = sold.indexOf(id);
    if (i === -1) sold.push(id); else sold.splice(i, 1);
    write(SOLD_KEY, sold);
  }
  function resetDemo() { localStorage.removeItem(ADD_KEY); localStorage.removeItem(HIDE_KEY); localStorage.removeItem(SOLD_KEY); }

  /* helpers */
  function money(n) { return "$" + Number(n).toLocaleString("en-US"); }
  function miles(n) { return Number(n).toLocaleString("en-US") + " mi"; }
  function estPayment(price) { // rough demo estimate: 72mo @ 12.9% APR, $0 down
    var r = 0.129 / 12, n = 72, p = price;
    var m = (p * r) / (1 - Math.pow(1 + r, -n));
    return "$" + Math.round(m) + "/mo";
  }

  return { SEED:SEED, all:all, available:available, add:add, remove:remove, toggleSold:toggleSold, resetDemo:resetDemo, money:money, miles:miles, estPayment:estPayment };
})();
