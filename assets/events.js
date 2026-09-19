/* Top Shelf conversion tracking (plan §12). Fires GA4 events for the three money actions so
   performance is measured in LEADS, not pageviews. In GA4, mark generate_lead / click_to_call /
   book_call as Key Events so they count as conversions. Loaded on every page. */
(function () {
  function ev(name) {
    try {
      if (window.gtag) gtag('event', name, {
        page_path: location.pathname,
        trade: (document.body && document.body.dataset.trade) || ''
      });
    } catch (e) {}
  }
  function hook(selector, name) {
    document.querySelectorAll(selector).forEach(function (a) {
      a.addEventListener('click', function () { ev(name); });
    });
  }
  hook('a[href^="tel:"]', 'click_to_call');
  hook('a[href*="booking"]', 'book_call');
  hook('a[href*="contact"]', 'cta_click');
  // generate_lead = a CONFIRMED audit request. The contact form submits by fetch and redirects
  // to thank-you.html on success, so thank-you loading means a lead actually landed.
  if (/thank-you/i.test(location.pathname)) ev('generate_lead');
})();
