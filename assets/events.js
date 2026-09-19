/* Top Shelf conversion tracking (plan §12). Fires GA4 events for the money actions so
   performance is measured in LEADS, not pageviews. In GA4, mark generate_lead /
   click_to_call / book_call as Key Events so they count as conversions. Loaded on every
   page. window.tsTrack lets the gap-quiz and chat widgets fire generate_lead on a
   confirmed submit; both run on trade pages, so the trade tag rides along automatically. */
(function () {
  var KEY = 'ts_trade';
  // Remember the trade of the last trade page viewed, so a lead that lands on the shared
  // (trade-less) thank-you.html is still attributable to the trade page it came from.
  function trade() {
    var t = (document.body && document.body.dataset.trade) || '';
    try {
      if (t) sessionStorage.setItem(KEY, t);
      else t = sessionStorage.getItem(KEY) || '';
    } catch (e) {}
    return t;
  }
  function ev(name) {
    try {
      if (window.gtag) gtag('event', name, { page_path: location.pathname, trade: trade() });
    } catch (e) {}
  }
  window.tsTrack = ev; // gap-quiz.js + site.js chat call this on a confirmed lead
  function hook(selector, name) {
    document.querySelectorAll(selector).forEach(function (a) {
      a.addEventListener('click', function () { ev(name); });
    });
  }
  trade(); // persist this page's trade on load, before any navigation away
  hook('a[href^="tel:"]', 'click_to_call');
  // Only the real scheduler (booking.html / /booking) counts as booking a call, NOT
  // solution-booking.html or the online-booking-for-* money pages that the nav and footer
  // link on every page.
  hook('a[href^="booking"], a[href^="/booking"]', 'book_call');
  hook('a[href*="contact"]', 'cta_click');
  // generate_lead = a CONFIRMED audit request. The contact form redirects here on success;
  // the gap-quiz and chat widgets call window.tsTrack('generate_lead') on their own success.
  if (/thank-you/i.test(location.pathname)) ev('generate_lead');
})();
