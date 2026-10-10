#!/usr/bin/env python3
"""Wire the one-time service pages into the rest of the site. Re-runnable.

The page generators do not know about these links, so run this after any of them
(generate_colony / generate_pillars / generate_corpus / generate_one_time):

  - a footer link to the hub on every page
  - a short "one job, one price" block above the closing call to action on the pages whose
    topic one of the jobs answers (website cost, not showing on Google, reviews, switching
    vendors, and the three related solution pages)
  - the pricing page's website line linked to the 5-page site, and the packages and jobs
    copied from the hub onto the pricing page, above the monthly plans
  - the three Get Found packages on the industry pages, and in the blocks above where one fits

Usage:  python scripts/wire_one_time.py   (from the repo root)
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARK = "<!-- one-time-links -->"
PRICING_OPEN = "<!-- one-time-on-pricing: filled from one-time-services.html by scripts/wire_one_time.py -->"
PRICING_CLOSE = "<!-- /one-time-on-pricing -->"
HUB = '<a href="one-time-services.html">See every one-time job</a>'


def a(slug, text):
    return '<a href="%s.html">%s</a>' % (slug, text)


# The Get Found packages (owner, 2026-10-02). Names and prices mirror generate_one_time.py.
PLUS = a("get-found-plus", "Get Found Plus")
LISTING_REVIEWS = a("get-found-listing-reviews", "Get Found: Listing + Reviews")
GET_FOUND = a("get-found-package", "Get Found")

SITE_JOBS = ("Buying the site on its own? The %s is $1,500 one time and the %s is $495, each built new by us with a logo if you need one. "
             "Google listing needs work too? %s is the 5-page website, the listing corrected, your reviews answered and a review card for $1,995. "
             "If a past vendor holds your site or domain, %s moves them into your name for $495. %s."
             % (a("custom-5-page-website", "custom 5-page website"), a("one-page-website", "one-page website"), PLUS,
                a("take-back-your-website", "take back what's yours"), HUB))
MAP_JOBS = ("Want it fixed once, for one price? The %s is $345 and the %s is $1,250, both one time. "
            "Reviews need answering too? %s is the listing fix, a reply to every unanswered review and a review card for $500. "
            "No website at all? %s covers the listing and a one-page site for $795. %s."
            % (a("google-business-profile-fix", "Google listing fix"), a("map-pack-push", "map-pack push"), LISTING_REVIEWS, GET_FOUND, HUB))
REVIEW_JOBS = ("Behind on replies? The %s answers every unanswered review for $150 one time, each reply approved by you first. The %s corrects the listing itself for $345. "
               "%s is both of those and a review card for $500. %s."
               % (a("review-reply-catch-up", "review reply catch-up"), a("google-business-profile-fix", "Google listing fix"), LISTING_REVIEWS, HUB))
# On the industry pages, which otherwise only sell the monthly plans.
PACKAGES = ("Not ready for a monthly plan? Start with one job at one price, paid once. With no website, %s is $795. "
            "With a poor website and a weak Google listing, %s is $1,995 and includes a new 5-page website. "
            "If your website is fine, %s is $500. %s."
            % (GET_FOUND, PLUS, LISTING_REVIEWS, HUB))
TAKE_BACK = ("Not sure who holds your domain or your Google listing? %s moves your website, domain and listing into your own name for $495 one time. %s."
             % (a("take-back-your-website", "Take back what's yours"), HUB))

BLOCKS = {}
for f in glob.glob(os.path.join(ROOT, "*-website-cost.html")) + [os.path.join(ROOT, x) for x in (
        "how-much-hvac-website-costs.html", "cost-to-modernize-local-business-online.html",
        "losing-jobs-to-better-websites.html", "solution-websites-seo.html")]:
    BLOCKS[os.path.basename(f)] = SITE_JOBS
for f in ("not-showing-on-google-maps.html", "why-am-i-not-on-google.html", "not-showing-up-on-google.html", "solution-marketing.html"):
    BLOCKS[f] = MAP_JOBS
for f in ["how-do-i-get-more-reviews.html", "solution-reviews.html"] + [os.path.basename(x) for pat in (
        "get-more-*-reviews.html", "review-software-for-*.html", "how-to-get-*-reviews.html") for x in glob.glob(os.path.join(ROOT, pat))]:
    BLOCKS[f] = REVIEW_JOBS
for f in ("switching-from-hibu-thryv.html", "thryv-alternative.html"):
    BLOCKS[f] = TAKE_BACK
for f in glob.glob(os.path.join(ROOT, "industry-*.html")):
    BLOCKS[os.path.basename(f)] = PACKAGES

FOOT_OLD = '<a href="pricing.html">Pricing</a>\n          <a href="why-us.html">Why Top Shelf</a>'
FOOT_NEW = ('<a href="pricing.html">Pricing</a>\n          <a href="one-time-services.html">One-Time Services</a>\n'
            '          <a href="why-us.html">Why Top Shelf</a>')


def block(text):
    return ('%s\n<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">One job, one price</span>\n'
            '      <p class="reveal" style="margin-top:1.4rem;max-width:68ch">%s</p>\n    </div>\n  </div>\n</section>\n\n' % (MARK, text))


def main():
    footers = blocks = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        name = os.path.basename(path)
        s = open(path, encoding="utf-8", newline="").read()
        o = s
        nl = "\r\n" if "\r\n" in s else "\n"
        old, new = FOOT_OLD.replace("\n", nl), FOOT_NEW.replace("\n", nl)
        if "one-time-services.html\">One-Time Services" not in s and old in s:
            s = s.replace(old, new)
            footers += 1
        if name in BLOCKS:
            s = re.sub(re.escape(MARK) + r".*?</section>\s*", "", s, count=1, flags=re.S)     # refresh an old block
            i = s.find('<section class="cta')
            if i == -1:
                i = s.find('<footer class="footer">')
            if i == -1:
                continue                      # no safe place to put it; leave the page alone
            s = s[:i] + block(BLOCKS[name]).replace("\n", nl) + s[i:]
            blocks += 1
        if name == "pricing.html" and "custom-5-page-website.html" not in s:
            s = s.replace("A custom 5-page site is <strong", 'A <a href="custom-5-page-website.html" style="color:var(--gold)">custom 5-page site</a> is <strong', 1)
            s = s.replace("You do not need a plan to buy one.</p>",
                          'You do not need a plan to buy one. <a href="one-time-services.html" style="color:var(--gold)">See every one-time job</a>.</p>', 1)
        if name == "pricing.html" and PRICING_OPEN in s:
            # The packages and jobs sit above the monthly plans, copied from the hub so the
            # prices have one source (generate_one_time.py).
            hub = open(os.path.join(ROOT, "one-time-services.html"), encoding="utf-8", newline="").read()
            parts = [re.search(r"<style>.*?</style>", hub, re.S).group(0),
                     re.search(r'<section id="packages".*?</section>', hub, re.S).group(0),
                     re.search(r'<section id="jobs".*?</section>', hub, re.S).group(0)
                     + '\n<p class="container ot-parts" style="margin-top:-3rem;margin-bottom:4rem;max-width:var(--maxw)">'
                       '<a href="one-time-services.html">See what every one-time job covers</a></p>']
            body = "\n".join(parts).replace("\r\n", "\n").replace("\n", nl)
            s = re.sub(re.escape(PRICING_OPEN) + r".*?" + re.escape(PRICING_CLOSE),
                       lambda m: PRICING_OPEN + nl + body + nl + PRICING_CLOSE, s, count=1, flags=re.S)
        if s != o:
            open(path, "w", encoding="utf-8", newline="").write(s)
    print("footer link added on %d pages; link block on %d pages" % (footers, blocks))


if __name__ == "__main__":
    main()
