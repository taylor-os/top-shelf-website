#!/usr/bin/env python3
"""Generate the one-time service pages and their hub.

Owner decision 2026-10-01: "you buy the build, the plan is upkeep". A website or a big fix
is a single-payment job the customer owns; a monthly plan keeps it working. These pages are
where the free audit's recommendation lands.

Prices, what each job includes and the terms mirror `topshelf/offer.py` in the
topshelf-seo-audit skill (ONE_TIME, ONE_TIME_TERMS). Change a price there first, then here.
Nothing on these pages may promise a ranking, mention a monthly price, say how to host, or
offer photography (owner, 2026-10-01: "we are not photographers"). A website job is always a
full replacement built by us, and a logo can be included in it.

The shell (head, nav, footer, the "+" pins and the side drawer) is lifted from
industry-retail.html so the pages track the live design.

Usage:  python scripts/generate_one_time.py   (from the repo root), then build_sitemap.py
"""
import html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.topshelfsolutions.io"
SHELL = "industry-retail.html"
HUB = "one-time-services.html"
TERMS = "Half up front, half when the job is done."
# Owner, 2026-10-02 (offer.py FIVE_PAGES, FIVE_PAGES_NOTE, LOGO_NOTE, PACKAGE_LINES, PACKAGES).
FIVE_PAGES = ("Home", "Services or Products", "About", "Reviews", "Contact")
FIVE_LINE = ("The usual five pages are %s and %s. You decide what each page is."
             % (", ".join(FIVE_PAGES[:-1]), FIVE_PAGES[-1]))
LOGO_NOTE = "No logo yet? Tell us and we design one as part of this job."
L_LISTING = "Your Google listing corrected: category, hours, what you sell, description"
L_REVIEWS = "A reply to every unanswered review, each one approved by you first"
L_CARD = "A review card for the counter that takes a customer straight to your review form"
NO_RANK = "We do not promise a ranking, because nobody controls Google's results."
OWN_BOTH = "You do. The website, the domain and the Google listing are in your name, and you keep every login."

ICONS = {
    "search": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="16" y1="16" x2="21" y2="21"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 21s-6.5-5.6-6.5-10.5a6.5 6.5 0 0 1 13 0C18.5 15.4 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.3"/></svg>',
    "page": '<svg viewBox="0 0 24 24"><rect x="5" y="3.5" width="14" height="17" rx="1.5"/><line x1="8.5" y1="8.5" x2="15.5" y2="8.5"/><line x1="8.5" y1="12" x2="15.5" y2="12"/><line x1="8.5" y1="15.5" x2="13" y2="15.5"/></svg>',
    "star": '<svg viewBox="0 0 24 24"><path d="M12 3.6l2.6 5.4 5.9.8-4.3 4.1 1 5.9L12 17l-5.2 2.8 1-5.9-4.3-4.1 5.9-.8z"/></svg>',
    "key": '<svg viewBox="0 0 24 24"><circle cx="8" cy="15" r="4"/><line x1="11" y1="12" x2="20" y2="3.5"/><line x1="16.5" y1="7" x2="19.5" y2="10"/></svg>',
    "camera": '<svg viewBox="0 0 24 24"><rect x="3.5" y="7" width="17" height="12.5" rx="1.8"/><circle cx="12" cy="13.2" r="3.4"/><path d="M8.5 7l1.4-2.5h4.2L15.5 7"/></svg>',
    "chart": '<svg viewBox="0 0 24 24"><line x1="4" y1="20" x2="20" y2="20"/><rect x="6" y="12" width="3" height="6"/><rect x="11" y="8" width="3" height="10"/><rect x="16" y="5" width="3" height="13"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><rect x="7.5" y="2.8" width="9" height="18.4" rx="2"/><line x1="11" y1="18.2" x2="13" y2="18.2"/></svg>',
}

# The same four terms close every job page.
P_TERMS = ("chart", "One price, paid in two halves", TERMS + " There is no plan and nothing to cancel.",
           ["Half up front", "Half when the job is done", "No contract"])
P_OWN = ("key", "Yours, in your name", "Everything we build or correct stays in your name, and you keep every login. "
         "There is no plan to cancel and nothing to hand back.", ["Your Google Business Profile", "Your website and domain", "Every login in your hands"])

SERVICES = [
    {
        "slug": "google-business-profile-fix", "name": "Google listing fix", "price": "$345",
        "hero": "marketing-hero", "eyebrow": "One-Time Job &middot; $345",
        "h1": "Your Google Listing, <em>Corrected</em>.",
        "title": "Google Business Profile Fix, $345 One Time",
        "meta": "A one-time Google Business Profile fix for $345: categories, hours, services, description and attributes corrected. Half up front. No monthly plan.",
        "sub": "Most local searches end on a Google listing, not a website. If yours has the wrong category, missing hours or a blank description, people looking for what you sell are shown someone else. This job corrects the listing, once, for one price.",
        "for": ["Your listing shows the wrong category, or only one of them", "Hours, holiday hours or services are missing or out of date",
                "The description is blank, or reads like someone else wrote it", "The listing was set up once and never touched again"],
        "gets": ["Your Google listing corrected wherever our audit found a gap", "Categories, hours, services, description and attributes brought up to date"],
        "pins": [("search", "Categories and services", "Google decides which searches to show you for largely from your category and the services you list. A wrong or missing one hides you from people looking for exactly what you do.",
                  ["Primary and secondary categories checked", "Every service you sell listed", "Attributes that apply to you turned on"]),
                 ("pin", "Hours and details", "Wrong hours send a customer to a locked door. We bring the hours, holiday hours, links and description in line with how you actually run.",
                  ["Regular and holiday hours", "Booking or appointment link, if you have one", "A description written for your customers"]),
                 ("key", "Claimed, and yours", "An unclaimed listing can be edited by anyone who suggests a change. We make sure it is claimed in your name, with us added only as a manager.",
                  ["Claimed in your name", "We work as a manager, not the owner", "Remove us whenever you like"]),
                 P_TERMS],
        "demo": None,
        "faqs": [("Do I need a monthly plan to buy this?", "No. It is a one-time job for $345. There is no plan, no contract and nothing to cancel."),
                 ("How do I pay?", TERMS),
                 ("Will this put me at the top of the map?", "We do not promise a ranking, because nobody controls Google's results. This job corrects what is wrong on the listing."),
                 ("My reviews need answering too. Is there one price for both?", "Yes. Get Found: Listing + Reviews is the listing fix, a reply to every unanswered review and a review card for $500."),
                 ("Who controls the listing afterward?", "You do. The listing stays in your name and you keep every login. We work as a manager on the profile and you can remove us whenever you like.")],
        "related": ["map-pack-push", "review-reply-catch-up", "get-found-listing-reviews"],
        "reads": [("not-showing-on-google-maps.html", "Why you are not showing on Google Maps"), ("why-am-i-not-on-google.html", "Why am I not on Google?")],
        "solution": ("solution-marketing.html", "Marketing &amp; Reviews"),
    },
    {
        "slug": "get-found-package", "name": "Get Found", "price": "$795",
        "who": "For a business with no website.",
        "parts": ["google-business-profile-fix", "one-page-website", "review-card"],
        "in": ["Your Google listing corrected", "A one-page website of your own, built by us", "A review card for the counter"],
        "hero": "websites-seo-hero", "eyebrow": "One-Time Package &middot; $795",
        "h1": "No Website? Start With <em>Get Found</em>.",
        "title": "Get Found: Google Listing, One-Page Website and Review Card, $795",
        "meta": "For a business with no website: your Google listing corrected, a one-page website of your own and a review card, $795 one time. Half up front. No monthly plan.",
        "sub": "If the only thing a customer can find is a Facebook page or a half-filled Google listing, this is the job to start with. One price covers the listing, a website of your own and a way to ask for reviews at the counter.",
        "for": ["You have no website, or only a Facebook page", "Your Google listing was set up once and never touched",
                "Customers tell you they could not find your hours or your address", "You want one job and one price, not a monthly plan"],
        "gets": ["Your Google listing corrected wherever our audit found a gap", "A one-page website of your own, built by us", "A logo designed for you, if you need one",
                 "A review card that takes a customer straight to your Google review form"],
        "pins": [("pin", "Your Google listing", "The listing is corrected first, because it is what most people see: categories, hours, services, description and attributes.",
                  ["Categories and services", "Hours and details", "Claimed in your name"]),
                 ("page", "A website of your own", "One page with what a customer needs to choose you: what you do, where you are, when you are open, and how to reach you. It is yours, in your name.",
                  ["Built for a phone first", "A logo designed for you, if you need one", "Yours to keep"]),
                 ("star", "A review card", "A card for the counter or the invoice that takes a customer straight to your Google review form, so asking takes one sentence.",
                  ["Opens your review form directly", "Works from any phone camera", "No software to learn"]),
                 P_TERMS],
        "demo": ("field", "field-and-fawn", "a demo site we built for a home and lifestyle shop"),
        "faqs": [("Do I need a monthly plan to buy this?", "No. Get Found is a one-time job for $795. There is no plan and no contract."),
                 ("How do I pay?", TERMS),
                 ("What if I already have a website?", "Then this is not the right package. If the website is fine, Get Found: Listing + Reviews covers the listing and your reviews for $500. If the website is holding you back, Get Found Plus replaces it with a new custom 5-page website and covers the listing and reviews too, for $1,995."),
                 ("Who owns the website and the listing?", OWN_BOTH)],
        "reads": [("not-showing-up-on-google.html", "Not showing up on Google"), ("why-am-i-not-on-google.html", "Why am I not on Google?")],
        "solution": ("solution-websites-seo.html", "Websites &amp; SEO"),
    },
    {
        "slug": "get-found-plus", "name": "Get Found Plus", "price": "$1,995",
        "who": "For a business with a poor website and a weak Google listing.",
        "parts": ["custom-5-page-website", "google-business-profile-fix", "review-reply-catch-up", "review-card"],
        "in": ["A new custom 5-page website, built by us", "Your Google listing corrected", L_REVIEWS, "A review card for the counter"],
        "hero": "websites-seo-hero", "eyebrow": "One-Time Package &middot; $1,995",
        "h1": "A New Website and Your Google Listing, <em>One Job</em>.",
        "title": "Get Found Plus: New 5-Page Website and Google Listing Fix, $1,995",
        "meta": "Get Found Plus: a new custom 5-page website, your Google listing corrected, a reply to every unanswered review and a review card. $1,995 one time. No monthly plan.",
        "sub": "One job that fixes all of it. We build you a new website and put your Google listing right, so you put your best foot forward and Google has every reason to show you to the customers searching near you.",
        "for": ["Your website is slow, dated or hard to use on a phone", "Your Google listing has the wrong category, missing hours or a blank description",
                "Reviews sit on your listing with no reply", "You want one job that covers all of it, not a list of fixes"],
        "gets": ["A custom 5-page website, built new by us, in your name", "Built for phones, with a number customers tap to call",
                 L_LISTING, L_REVIEWS, L_CARD, FIVE_LINE],
        "pins": [("page", "A new 5-page website", "We build you a new website from the ground up, in your name. It is built for phones, with a number customers tap to call. " + FIVE_LINE,
                  [", ".join(FIVE_PAGES), "You decide what each page is", LOGO_NOTE]),
                 ("pin", "Your Google listing", "The listing is what most people see first. We correct the category, the hours, what you sell and the description.",
                  ["Category and what you sell", "Hours and description", "The listing stays in your name"]),
                 ("star", "Reviews answered, and a review card", "Every unanswered review gets a written reply, and nothing is posted until you approve it. The review card sits on the counter and takes a customer straight to your review form.",
                  ["A reply to every unanswered review", "Each one approved by you first", "A review card for the counter"]),
                 P_TERMS],
        "demo": ("brightwater", "brightwater-dental", "a demo site we built for a dental practice"),
        "faqs": [("Do I need a monthly plan to buy this?", "No. Get Found Plus is a one-time job for $1,995. There is no plan and no contract."),
                 ("How do I pay?", TERMS),
                 ("Which five pages do I get?", FIVE_LINE),
                 ("What if my website is fine?", "Then you do not need this one. Get Found: Listing + Reviews covers the listing, the review replies and the review card for $500, and your website stays exactly as it is."),
                 ("Will this put me at the top of Google?", NO_RANK + " This job builds the website and corrects the listing."),
                 ("Who owns the website and the listing?", OWN_BOTH)],
        "reads": [("losing-jobs-to-better-websites.html", "Losing jobs to better websites"), ("not-showing-up-on-google.html", "Not showing up on Google"),
                  ("industry-retail.html", "Retail &amp; Local shops")],
        "solution": ("solution-websites-seo.html", "Websites &amp; SEO"),
    },
    {
        "slug": "get-found-listing-reviews", "name": "Get Found: Listing + Reviews", "price": "$500",
        "who": "For a business whose website is fine.",
        "parts": ["google-business-profile-fix", "review-reply-catch-up", "review-card"],
        "in": ["Your Google listing corrected", L_REVIEWS, "A review card for the counter", "Your website stays exactly as it is"],
        "hero": "reviews-hero", "eyebrow": "One-Time Package &middot; $500",
        "h1": "Website Fine? Fix the <em>Listing and the Reviews</em>.",
        "title": "Get Found: Listing + Reviews, $500 One Time",
        "meta": "Get Found: Listing + Reviews. Your Google listing corrected, a reply to every unanswered review and a review card, $500 one time. Your website stays exactly as it is.",
        "sub": "One job that fixes all of it, so your listing puts its best foot forward and Google has every reason to show you to the customers searching near you. Your website stays exactly as it is.",
        "for": ["Your website does its job and you want to keep it", "Your Google listing has the wrong category, missing hours or a blank description",
                "Reviews sit on your listing with no reply", "You want one job that covers the listing and the reviews"],
        "gets": [L_LISTING, L_REVIEWS, L_CARD, "Your website stays exactly as it is"],
        "pins": [("pin", "Your Google listing", "The listing is what most people see first. We correct the category, the hours, what you sell and the description.",
                  ["Category and what you sell", "Hours and description", "The listing stays in your name"]),
                 ("key", "Every review answered", "Good ones and bad ones. Each gets a written reply, and nothing is posted until you have read it and approved it.",
                  ["A reply to every unanswered review", "Each one approved by you first", "Posted under your business name"]),
                 ("star", "A review card", "A card for the counter that takes a customer straight to your Google review form, so asking takes one sentence.",
                  ["Opens your review form directly", "Works from any phone camera", "No software to learn"]),
                 P_TERMS],
        "demo": None,
        "faqs": [("Do I need a monthly plan to buy this?", "No. Get Found: Listing + Reviews is a one-time job for $500. There is no plan and no contract."),
                 ("How do I pay?", TERMS),
                 ("Will you change my website?", "No. Your website stays exactly as it is. If the website is what holds you back, Get Found Plus replaces it with a new custom 5-page website and covers the listing and reviews too, for $1,995."),
                 ("Will this put me at the top of the map?", NO_RANK + " This job corrects what is wrong on the listing and answers your reviews."),
                 ("Who controls the listing afterward?", "You do. The listing stays in your name and you keep every login. We work as a manager on the profile and you can remove us whenever you like.")],
        "reads": [("not-showing-on-google-maps.html", "Why you are not showing on Google Maps"), ("how-do-i-get-more-reviews.html", "How do I get more reviews?"),
                  ("industry-retail.html", "Retail &amp; Local shops")],
        "solution": ("solution-reviews.html", "Reviews &amp; Reputation"),
    },
    {
        "slug": "map-pack-push", "name": "Map-pack push", "price": "$1,250",
        "hero": "marketing-hero", "eyebrow": "One-Time Job &middot; $1,250",
        "h1": "Good Reviews, Still Not in the <em>Top Three</em>?",
        "title": "Map-Pack Push: A One-Time Google Maps Work List, $1,250",
        "meta": "A fixed list of work on your Google listing, other directories and your site, with rank checks before, at 30 and at 60 days. $1,250 one time. A list of work, not a ranking promise.",
        "sub": "Google shows three businesses on the map before anyone has to tap for more. If you have the reviews and still sit below that line, this is a fixed list of work aimed at the things that hold a listing down, with your position checked before we start, at 30 days and at 60 days.",
        "for": ["Your reviews are strong and you still sit outside the top three", "You show up in your own town and vanish in the next one over",
                "Your details differ from one directory to the next", "You want to see the before and the after for yourself"],
        "gets": ["Your Google listing corrected wherever our audit found a gap", "Corrections submitted to your listings on the other directories",
                 "Common questions answered on the listing, and a location page if we built your site", "Where you rank, checked before we start, at 30 days and at 60 days",
                 "A list of work, not a ranking promise"],
        "pins": [("pin", "The listing itself", "Everything in the Google listing fix is part of this job: categories, hours, services, description and attributes.",
                  ["Categories and services", "Hours and details", "Claimed in your name"]),
                 ("search", "Other directories", "Your name, address and phone should match everywhere they appear. We find where they do not and submit the corrections.",
                  ["Mismatched details found", "Corrections submitted for you", "A list of what was sent, and where"]),
                 ("page", "Questions and a location page", "The common questions people ask about a business like yours, answered on your listing. If we built your site, it also gets a page for the area you want to be found in.",
                  ["Common questions answered on the listing", "A location page, on a site we built", "Written for your customers"]),
                 ("chart", "Checked three times", "We record where you rank before we start, then again at 30 days and at 60 days, so you can see what moved.",
                  ["Before we start", "At 30 days", "At 60 days"])],
        "demo": None,
        "faqs": [("Do you promise a top-three ranking?", "No. Nobody controls Google's results, and the result on a phone also depends on where the person searching is standing. This is a fixed list of work, with your position checked before we start, at 30 days and at 60 days."),
                 ("How is this different from the Google listing fix?", "The listing fix corrects the listing. The map-pack push includes that and adds the other directories, answers to common questions on the listing, a location page if we built your site, and the three rank checks. You buy one or the other, not both."),
                 ("How do I pay?", TERMS),
                 ("Do I need a monthly plan?", "No. It is a one-time job for $1,250, with no plan and no contract.")],
        "related": ["google-business-profile-fix", "custom-5-page-website", "review-reply-catch-up"],
        "reads": [("not-showing-on-google-maps.html", "Why you are not showing on Google Maps"), ("losing-jobs-to-better-websites.html", "Losing jobs to better websites")],
        "solution": ("solution-marketing.html", "Marketing &amp; Reviews"),
    },
    {
        "slug": "custom-5-page-website", "name": "Custom 5-page website", "price": "$1,500",
        "hero": "websites-seo-hero", "eyebrow": "One-Time Job &middot; $1,500",
        "h1": "A Website You <em>Own</em>, Built Once.",
        "title": "Custom 5-Page Website, $1,500 One Time",
        "meta": "A custom 5-page website for $1,500 one time, built new by us and published, with basic on-page SEO and a logo if you need one. Yours to keep. No monthly plan required.",
        "sub": "Before anyone calls, they look you up. We build you a new 5-page website from the ground up, publish it, and it is yours to keep. We replace a site rather than patch it, so every page is built to be found. You pay once, and you do not need a monthly plan to buy it.",
        "for": ["Your current site is slow, dated or hard to use on a phone", "One page is trying to cover everything you offer",
                "A past vendor built your site and you are not sure you own it", "You would rather buy a website than rent one"],
        "gets": ["A custom 5-page website, built new by us and published", FIVE_LINE, "Basic on-page SEO built in, so it can be found", "A logo designed for you, if you need one", "Yours to keep, in your name"],
        "pins": [("page", "Five pages, built for you", "Five pages written and designed around your business, not poured into a template. " + FIVE_LINE,
                  [", ".join(FIVE_PAGES), "You decide what each page is", "A logo designed for you, if you need one"]),
                 ("phone", "Made for a phone", "Most people will see it on a phone first. The number can be tapped, the pages load quickly, and the next step is always on screen.",
                  ["Tap-to-call phone number", "Readable without pinching", "The next step on every screen"]),
                 ("search", "Basic SEO built in", "Page titles, descriptions, headings and the business details Google reads are set up as the site is built, so it can be found.",
                  ["Titles and descriptions on every page", "One clear headline per page", "Business details Google can read"]),
                 P_OWN],
        "demo": ("brightwater", "brightwater-dental", "a demo site we built for a dental practice"),
        "faqs": [("Do I need a monthly plan to get a website?", "No. The website is a one-time build for $1,500 and it is yours. A monthly plan is optional, and what a plan does is keep the site and your listing working after it is built."),
                 ("How do I pay?", TERMS),
                 ("Which five pages do I get?", FIVE_LINE),
                 ("My Google listing needs work too. Is there one price for both?", "Yes. Get Found Plus is the custom 5-page website, the Google listing fix, a reply to every unanswered review and a review card for $1,995."),
                 ("Who owns it?", "You do. The website and the domain are in your name and you keep every login."),
                 ("Why replace my site instead of fixing it?", "A site we build is one we can keep optimized. Patching a site inside someone else's builder means working around its limits, and you pay for the workaround. If your current site is doing its job, the free audit will say so and we will not sell you a new one.")],
        "related": ["get-found-plus", "one-page-website", "take-back-your-website"],
        "reads": [("losing-jobs-to-better-websites.html", "Losing jobs to better websites"), ("cost-to-modernize-local-business-online.html", "What it costs to modernize a local business online")],
        "solution": ("solution-websites-seo.html", "Websites &amp; SEO"),
    },
    {
        "slug": "one-page-website", "name": "One-page website", "price": "$495",
        "hero": "websites-seo-hero", "eyebrow": "One-Time Job &middot; $495",
        "h1": "One Page. <em>Yours</em>. Done.",
        "title": "One-Page Website, $495 One Time",
        "meta": "A one-page website of your own for $495 one time: what you do, where you are, when you are open and how to reach you. Yours to keep. No monthly plan required.",
        "sub": "Not every business needs five pages. If a customer mainly wants to know what you do, where you are, when you are open and how to reach you, one good page covers it, and it is yours.",
        "for": ["Your only web presence is a Facebook page or a brokerage profile", "You are a one-person business and want a site in your own name",
                "Customers ask for your hours and address because they could not find them", "You want something small and finished, not a project"],
        "gets": ["A one-page website of your own, built by us", "What you do, where you are, when you are open and how to reach you", "A logo designed for you, if you need one", "Yours to keep, in your name"],
        "pins": [("page", "One clear page", "Everything a customer needs to choose you, in the order they look for it, without a menu to dig through.",
                  ["What you do", "Where you are and when you are open", "How to reach you"]),
                 ("phone", "Made for a phone", "The page is built for a phone first, with a number that can be tapped and directions one tap away.",
                  ["Tap-to-call phone number", "Directions one tap away", "Loads quickly"]),
                 ("search", "Readable by Google", "Your name, address, phone and hours are set up so Google can read them and match them to your listing.",
                  ["Matches your Google listing", "A proper page title and description", "Business details Google can read"]),
                 P_OWN],
        "demo": ("field", "field-and-fawn", "a demo site we built for a home and lifestyle shop"),
        "faqs": [("Do I need a monthly plan to buy this?", "No. It is a one-time job for $495, with no plan and no contract."),
                 ("How do I pay?", TERMS),
                 ("Can it grow later?", "Yes. On a site we built, an extra page for a city or a service is $325. If you know you need several pages from the start, the custom 5-page website is the better buy."),
                 ("Who owns it?", "You do. The website and the domain are in your name and you keep every login.")],
        "related": ["get-found-package", "custom-5-page-website", "google-business-profile-fix"],
        "reads": [("not-showing-up-on-google.html", "Not showing up on Google"), ("losing-jobs-to-better-websites.html", "Losing jobs to better websites")],
        "solution": ("solution-websites-seo.html", "Websites &amp; SEO"),
    },
    {
        "slug": "take-back-your-website", "name": "Take back what's yours", "price": "$495",
        "hero": "crm-hero", "eyebrow": "One-Time Job &middot; $495",
        "h1": "Your Website. Your Domain. <em>Your Name</em>.",
        "title": "Take Back Your Website, Domain and Google Listing, $495 One Time",
        "meta": "Your domain and Google listing moved out of a past or current vendor's hands and into your own name, and your website too where it can be moved, for $495 one time. No monthly plan.",
        "sub": "A lot of owners are not sure who actually holds their domain or their Google listing. If the answer is a marketing company, past or current, you cannot leave without losing them. This job moves your domain and your listing into your own name, and your website too where the vendor's system lets it leave.",
        "for": ["A marketing company registered your domain and you never got the login", "Your Google listing is managed by someone you no longer work with",
                "You want to switch vendors and are afraid of losing your website", "You are not sure who holds what, and want to know"],
        "gets": ["Your domain and Google listing moved into your own name", "Your website moved too, where the vendor's system lets it leave", "Every login in your hands"],
        "pins": [("key", "Your domain", "The domain is the address your customers type and the one printed on your trucks and cards. It should be registered to you.",
                  ["Registered in your name", "The login in your hands", "Nothing held by a vendor"]),
                 ("page", "Your website", "Where the vendor's system lets the site leave, it moves with you. Some builders will not release a site, and we tell you that before you pay.",
                  ["Moved with you where it can be", "You are told first if it cannot", "Every login handed over"]),
                 ("pin", "Your Google listing", "The listing carries your reviews. Ownership of it should sit with you, with anyone else added only as a manager.",
                  ["You as the owner", "Your reviews stay with you", "Old managers removed"]),
                 P_OWN],
        "demo": None,
        "faqs": [("How do I know if I need this?", "If you cannot log in to your own domain, your own website and your own Google listing today, someone else holds them. The free audit checks what we can see from the outside."),
                 ("How do I pay?", TERMS),
                 ("Do I have to become your customer afterward?", "No. It is a one-time job for $495. When it is done, everything is in your name and you can work with anyone you like."),
                 ("Does this cancel my contract with my current vendor?", "No. A contract you signed is between you and them. This job moves what belongs to you into your name.")],
        "related": ["custom-5-page-website", "google-business-profile-fix", "map-pack-push"],
        "reads": [("switching-from-hibu-thryv.html", "Switching from Hibu or Thryv"), ("thryv-alternative.html", "A Thryv alternative")],
        "solution": ("solution-websites-seo.html", "Websites &amp; SEO"),
    },
    {
        "slug": "review-reply-catch-up", "name": "Review reply catch-up", "price": "$150",
        "hero": "reviews-hero", "eyebrow": "One-Time Job &middot; $150",
        "h1": "Every Review, <em>Answered</em>.",
        "title": "Review Reply Catch-Up, $150 One Time",
        "meta": "A written reply to every unanswered Google review, each one approved by you before it is posted, for $150 one time. No monthly plan.",
        "sub": "A row of reviews with no reply tells the next customer nobody is listening. This job writes a reply to every unanswered review, and nothing is posted until you have read it and approved it.",
        "for": ["You have reviews going back months or years with no reply", "You mean to answer them and never get to it",
                "You are not sure how to answer the bad ones", "You want it caught up once, then to keep up yourself"],
        "gets": ["A written reply to every unanswered review", "Each reply approved by you before it is posted"],
        "pins": [("star", "Every unanswered review", "Good ones and bad ones. Each gets a reply written for that review, not a line pasted under all of them.",
                  ["Written for each review", "The difficult ones included", "In your voice"]),
                 ("key", "You approve each one", "Nothing is posted until you have read it. You can change a word or strike a reply altogether.",
                  ["You read every reply first", "Change or strike any of them", "Posted only after your yes"]),
                 ("pin", "Posted on your listing", "Once approved, the replies are posted on your Google listing under your business name.",
                  ["Posted for you", "Under your business name", "Your listing stays yours"]),
                 P_TERMS],
        "demo": None,
        "faqs": [("Will you post anything without asking me?", "No. Every reply is approved by you before it is posted."),
                 ("How do I pay?", TERMS),
                 ("Do I need a monthly plan?", "No. It is a one-time job for $150, with no plan and no contract."),
                 ("Does this get me more reviews?", "No, it answers the ones you have. A review card that takes a customer straight to your Google review form is $95.")],
        "related": ["google-business-profile-fix", "get-found-listing-reviews", "map-pack-push"],
        "reads": [("how-do-i-get-more-reviews.html", "How do I get more reviews?"), ("solution-reviews.html", "Reviews &amp; Reputation")],
        "solution": ("solution-reviews.html", "Reviews &amp; Reputation"),
    },
]
BY_SLUG = {s["slug"]: s for s in SERVICES}
# Small jobs with no page of their own; listed on the hub.
SMALL = [("Extra page", "$325 per page", "One new page for a city or a service, on a site we built."),
         ("Review card", "$95", "A card or counter stand that takes a customer straight to your Google review form.")]

# The Get Found family (owner, 2026-10-02): a package is several jobs sold as one job for one
# price. A package is any service with "parts"; the rest are single jobs.
PACKAGES = [s for s in SERVICES if "parts" in s]
JOBS = [s for s in SERVICES if "parts" not in s]


def money(n):
    return "$" + format(n, ",")


def dollars(price):
    return int(price.lstrip("$").replace(",", ""))


def part(slug):
    """(name, price, href) of one part of a package. The review card has no page of its own."""
    if slug == "review-card":
        return "Review card", "$95", HUB + "#jobs"
    return BY_SLUG[slug]["name"], BY_SLUG[slug]["price"], slug + ".html"


def mid(name):
    """A job name as it reads in the middle of a sentence."""
    return name if name.startswith("Google") else name[0].lower() + name[1:]


def parts_total(s):
    return sum(dollars(part(p)[1]) for p in s["parts"])


for _p in PACKAGES:
    assert parts_total(_p) > dollars(_p["price"]), (_p["slug"], "a package must cost less than its parts")
    _names = ", ".join("%s %s" % (mid(n), pr) for n, pr, _h in map(part, _p["parts"]))
    _p["related"] = [x for x in _p["parts"] if x in BY_SLUG]
    _p["faqs"] = _p["faqs"][:2] + [("Can I buy just part of it?", "Yes. Every part is sold on its own: %s. Bought one at a time they come to %s. Together they are %s."
                                    % (_names, money(parts_total(_p)), _p["price"]))] + _p["faqs"][2:]

PAGE_CSS = """<style>
.ot-terms{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem;margin-top:2.2rem}
.ot-term{border:1px solid var(--hair);border-radius:6px;padding:1.2rem 1.3rem;background:rgba(255,255,255,.015)}
.ot-term b{display:block;font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.7rem;line-height:1.1;color:var(--ink)}
.ot-term span{display:block;margin-top:.35rem;font-size:.82rem;color:var(--ink-3)}
.ot-two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2.4rem;margin-top:2.4rem}
.ot-list{list-style:none;margin:1.2rem 0 0;padding:0;display:grid;gap:.8rem}
.ot-list li{position:relative;padding-left:1.5rem;color:var(--ink-2);line-height:1.6}
.ot-list li::before{content:"";position:absolute;left:0;top:.72em;width:.6rem;height:1px;background:var(--gold)}
.ot-pins{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin-top:2.4rem}
.ot-pins .annot-pin,.ot-cards .annot-pin{position:static;width:100%;justify-content:space-between;text-align:left}
.ot-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1.1rem;margin-top:2.4rem}
.ot-card{border:1px solid var(--hair);border-radius:6px;padding:1.5rem;display:flex;flex-direction:column;gap:.7rem;background:rgba(255,255,255,.015)}
.ot-card h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.55rem;line-height:1.15;margin:0}
.ot-card h3 a{color:var(--ink);text-decoration:none}.ot-card h3 a:hover{color:var(--gold)}
.ot-card .ot-price{color:var(--gold);font-size:.95rem;letter-spacing:.04em}
.ot-card p{margin:0;font-size:.92rem;line-height:1.6;color:var(--ink-2)}
.ot-links{display:flex;flex-wrap:wrap;gap:.7rem 1.6rem;margin-top:1.4rem}
.ot-links a{color:var(--gold);text-decoration:none;border-bottom:1px solid var(--hair)}
.ot-links a:hover{border-color:var(--gold)}
.ot-card .ot-list{margin:0;font-size:.9rem;gap:.5rem}
.ot-parts{margin-top:2rem;color:var(--ink-2);line-height:1.7;max-width:72ch}
.ot-parts a{color:var(--gold);text-decoration:none;border-bottom:1px solid var(--hair)}
@media (max-width:900px){.ot-terms{grid-template-columns:repeat(2,minmax(0,1fr))}.ot-two,.ot-pins{grid-template-columns:1fr}.ot-cards{grid-template-columns:1fr}}
</style>"""

DRAWER_JS = """<script>
(function(){
  var bits=document.querySelectorAll('.annot-pin'); if(!bits.length) return;
  var IC=%(icons)s;
  var A=%(data)s;
  var scrim=document.getElementById('siteScrim'), drawer=document.getElementById('siteDrawer');
  var eI=document.getElementById('siteIcon'), eT=document.getElementById('siteTitle'), eD=document.getElementById('siteDesc'), eP=document.getElementById('sitePoints');
  function open(k){ var d=A[k]; if(!d) return; eI.innerHTML=IC[d.i]||''; eT.textContent=d.t; eD.textContent=d.d; eP.innerHTML=''; d.pts.forEach(function(p){ var li=document.createElement('li'); li.textContent=p; eP.appendChild(li); }); drawer.scrollTop=0; document.body.classList.add('drawer-open'); scrim.classList.add('open'); drawer.classList.add('open'); drawer.setAttribute('aria-hidden','false'); scrim.setAttribute('aria-hidden','false'); }
  function close(){ document.body.classList.remove('drawer-open'); scrim.classList.remove('open'); drawer.classList.remove('open'); drawer.setAttribute('aria-hidden','true'); scrim.setAttribute('aria-hidden','true'); }
  bits.forEach(function(b){ b.addEventListener('click', function(){ open(b.dataset.aspect); }); });
  scrim.addEventListener('click', close);
  document.getElementById('siteX').addEventListener('click', close);
  document.addEventListener('keydown', function(e){ if(e.key==='Escape') close(); });
})();
</script>"""

PLUS = ('<span class="annot-plus" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2.6" stroke-linecap="round"><line x1="12" y1="6" x2="12" y2="18"/><line x1="6" y1="12" x2="18" y2="12"/></svg></span>')


def e(t):
    return html.escape(t, quote=True)


def shell():
    s = open(os.path.join(ROOT, SHELL), encoding="utf-8").read()
    head_end = s.index("</head>")
    nav = s[s.index("<body"):s.index('<section class="page-hero')]
    foot = s[s.index('<footer class="footer">'):]
    x = re.search(r'<button class="sdrawer-x"[^>]*>(.*?)</button>', s, re.S).group(1)
    # head assets only: stylesheet, fonts, icon, analytics. Title, meta and schema are per page.
    keep = re.findall(r'<link rel="(?:icon|preconnect|stylesheet)"[^>]*>|<link href="https://fonts[^>]*>', s[:head_end])
    gtag = re.search(r"<!-- Google tag.*?</script>\s*<script>.*?</script>", s[:head_end], re.S).group(0)
    return "\n".join(keep) + "\n" + gtag, nav, foot, x


def head(title, desc, slug, schema, assets):
    url = "%s/%s.html" % (SITE, slug)
    full = "%s | Top Shelf Business Solutions" % title
    return ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>%(t)s</title>\n<meta name="description" content="%(d)s">\n<link rel="canonical" href="%(u)s">\n'
            '<meta name="robots" content="index,follow">\n<meta property="og:type" content="website">\n'
            '<meta property="og:site_name" content="Top Shelf Business Solutions">\n<meta property="og:title" content="%(t)s">\n'
            '<meta property="og:description" content="%(d)s">\n<meta property="og:url" content="%(u)s">\n'
            '<meta property="og:image" content="%(s)s/assets/logo-full.png">\n<meta name="twitter:card" content="summary_large_image">\n'
            '<meta name="twitter:title" content="%(t)s">\n<meta name="twitter:description" content="%(d)s">\n'
            '<meta name="twitter:image" content="%(s)s/assets/logo-full.png">\n%(a)s\n'
            '<script type="application/ld+json">%(j)s</script>\n%(c)s\n</head>\n'
            % {"t": e(full), "d": e(desc), "u": url, "s": SITE, "a": assets, "j": json.dumps(schema, ensure_ascii=False), "c": PAGE_CSS})


def crumbs(name, slug):
    items = [("Home", SITE + "/"), ("One-Time Services", "%s/%s" % (SITE, HUB))]
    if slug:
        items.append((name, "%s/%s.html" % (SITE, slug)))
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i, "name": n, "item": u} for i, (n, u) in enumerate(items, 1)]}


def hero(eyebrow, h1, sub, img, primary, secondary):
    return ('<section class="page-hero ih">\n  <div class="ih-bg" aria-hidden="true" style="background-image:url(\'assets/img/solution/%s.jpg\')"></div>\n'
            '  <div class="ih-scrim" aria-hidden="true"></div>\n  <div class="container page-hero-inner">\n'
            '    <span class="eyebrow reveal">%s</span>\n    <h1 class="display display-lg reveal">%s</h1>\n'
            '    <p class="page-hero-sub reveal">%s</p>\n    <div class="page-hero-actions reveal">\n'
            '      <a href="%s" class="btn btn-gold">%s <span class="arr">&rarr;</span></a>\n      <a href="%s" class="btn btn-line">%s</a>\n'
            '    </div>\n  </div>\n</section>\n' % (img, eyebrow, h1, e(sub), primary[0], primary[1], secondary[0], secondary[1]))


def drawer(x_icon, pins, cta):
    data = {"p%d" % i: {"i": icon, "t": t, "d": d, "pts": pts} for i, (icon, t, d, pts) in enumerate(pins)}
    return ('<div class="sdrawer-scrim" id="siteScrim" aria-hidden="true"></div>\n'
            '<aside class="sdrawer" id="siteDrawer" role="dialog" aria-modal="true" aria-label="What this covers" aria-hidden="true">\n'
            '  <div class="sdrawer-in">\n    <div class="sdrawer-top"><span class="sdrawer-eyebrow">What this covers</span>'
            '<button class="sdrawer-x" id="siteX" type="button" aria-label="Close">%s</button></div>\n'
            '    <div class="sdrawer-icon" id="siteIcon" aria-hidden="true"></div>\n    <h3 class="sdrawer-title" id="siteTitle"></h3>\n'
            '    <p class="sdrawer-desc" id="siteDesc"></p>\n    <ul class="sdrawer-points" id="sitePoints"></ul>\n'
            '    <a class="sdrawer-cta" href="%s">%s <span aria-hidden="true">&rarr;</span></a>\n  </div>\n</aside>\n%s\n'
            % (x_icon, cta[0], cta[1], DRAWER_JS % {"icons": json.dumps(ICONS), "data": json.dumps(data, ensure_ascii=False)}))


def pins_html(pins):
    return "".join('<button type="button" class="annot-pin" data-aspect="p%d"><span>%s</span>%s</button>\n' % (i, e(t), PLUS)
                   for i, (_, t, _d, _p) in enumerate(pins))


def faq_html(faqs):
    rows = "".join('      <div class="qa-row reveal">\n        <span class="qa-num">%02d</span>\n        <div>\n'
                   '          <p class="qa-q">%s</p>\n          <p class="qa-a">%s</p>\n        </div>\n      </div>\n' % (i, e(q), e(a))
                   for i, (q, a) in enumerate(faqs, 1))
    return rows


def cta_block():
    return ('<section class="cta rule-top">\n  <div class="container">\n    <img src="assets/logo-mark.png?v=20260804b" alt="" class="cta-mark reveal">\n'
            '    <span class="eyebrow reveal">Free. No Obligation. No Pressure.</span>\n    <h2 class="cta-title reveal">Start With the<br><em>Free Audit</em></h2>\n'
            '    <p class="cta-sub reveal">The audit shows you what is wrong with your Google listing and your website, with your own numbers. If one job would close the gap, it names it. It costs nothing, and it is yours whether you work with us or not.</p>\n'
            '    <div class="cta-actions reveal">\n      <a href="contact.html" class="btn btn-gold">Get My Free Audit <span class="arr">&rarr;</span></a>\n'
            '      <a href="%s" class="btn btn-line">See Every One-Time Job</a>\n    </div>\n'
            '    <p class="cta-fine reveal">Call or text (469) 833-3033.</p>\n  </div>\n</section>\n\n' % HUB)


def package_card(s, link_text="See what it covers"):
    """A package on the hub and in the family row: who it is for, what is in it, the price."""
    return ('      <div class="ot-card reveal"><span class="ot-price">%s one time</span><h3><a href="%s.html">%s</a></h3><p>%s</p>'
            '<ul class="ot-list">%s</ul><a href="%s.html" style="color:var(--gold);text-decoration:none;font-size:.9rem;margin-top:auto">%s &rarr;</a></div>\n'
            % (s["price"], s["slug"], e(s["name"]), e(s["who"]), "".join("<li>%s</li>" % e(x) for x in s["in"]), s["slug"], link_text))


def service_page(s, assets, nav, foot, x_icon):
    slug, url = s["slug"], "%s/%s.html" % (SITE, s["slug"])
    pack = "parts" in s
    schema = [
        {"@context": "https://schema.org", "@type": "Service", "name": s["name"], "serviceType": s["title"],
         "provider": {"@type": "Organization", "name": "Top Shelf Business Solutions", "url": SITE + "/"},
         "areaServed": {"@type": "AdministrativeArea", "name": "Dallas-Fort Worth Metroplex"}, "url": url, "description": s["meta"],
         "offers": {"@type": "Offer", "price": s["price"].lstrip("$").replace(",", ""), "priceCurrency": "USD", "url": url}},
        crumbs(s["name"], slug),
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in s["faqs"]]},
    ]
    out = head(s["title"], s["meta"], slug, schema, assets) + nav
    out += hero(s["eyebrow"], s["h1"], s["sub"], s["hero"], ("contact.html", "Get Your Free Audit"), ("#covers", "See What It Covers"))
    terms = [(s["price"], "one time"), ("Half up front", "half when the job is done"), ("No contract", "nothing monthly"), ("Yours to keep", "in your name")]
    parts = ""
    if pack:        # what the parts cost on their own, each linked to its own page
        parts = ('    <p class="ot-parts reveal">Bought one at a time, the parts come to %s: %s. As one package they are %s.</p>\n'
                 % (money(parts_total(s)), ", ".join('<a href="%s">%s</a> %s' % (h, e(mid(n)), pr) for n, pr, h in map(part, s["parts"])), s["price"]))
    out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">One job, one price</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">%s, <em>%s</em> one time</h2>\n'
            '    </div>\n    <div class="ot-terms reveal">%s</div>\n    <div class="ot-two">\n'
            '      <div class="reveal"><span class="eyebrow">This is for you if</span><ul class="ot-list">%s</ul></div>\n'
            '      <div class="reveal"><span class="eyebrow">What you get</span><ul class="ot-list">%s</ul></div>\n    </div>\n%s  </div>\n</section>\n\n'
            % (e(s["name"]), s["price"], "".join('<div class="ot-term"><b>%s</b><span>%s</span></div>' % (e(a), e(b)) for a, b in terms),
               "".join("<li>%s</li>" % e(x) for x in s["for"]), "".join("<li>%s</li>" % e(x) for x in s["gets"]), parts))
    demo = ""
    if s["demo"]:
        img, site, what = s["demo"]
        demo = ('    <div class="demoshow reveal" style="margin-top:2.6rem">\n'
                '      <figure class="demoshow-browser"><span class="demoshow-bar"><i></i><i></i><i></i></span><img src="assets/img/demo/%s-desktop.jpg?v=4" alt="A demo website built by Top Shelf, on a computer" loading="lazy" width="1280" height="800"></figure>\n'
                '      <figure class="demoshow-phone"><img src="assets/img/demo/%s-mobile.jpg?v=4" alt="The same demo website on a phone" loading="lazy" width="390" height="844"></figure>\n'
                '    </div>\n    <p class="reveal" style="text-align:center;margin-top:1.4rem;color:var(--ink-3);font-size:.9rem">This is %s. Yours is built around your business. '
                '<a href="websites/%s/index.html" target="_blank" rel="noopener" style="color:var(--gold)">View the live demo &rarr;</a></p>\n' % (img, img, e(what), site))
    out += ('<section id="covers" class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">What it covers</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Tap a <em>+</em> for the detail</h2>\n'
            '    </div>\n    <div class="ot-pins reveal">\n%s    </div>\n%s  </div>\n</section>\n\n' % (pins_html(s["pins"]), demo))
    out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">How it works</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Three steps, <em>no plan</em></h2>\n    </div>\n'
            '    <div class="ot-cards">\n'
            '      <div class="ot-card reveal"><span class="ot-price">01</span><h3>The free audit</h3><p>We look at your Google listing and your website and show you what is wrong, with your own numbers. You see what the job covers before you pay anything.</p></div>\n'
            '      <div class="ot-card reveal"><span class="ot-price">02</span><h3>The job</h3><p>%s We work on it until it is done.</p></div>\n'
            '      <div class="ot-card reveal"><span class="ot-price">03</span><h3>Yours to keep</h3><p>Everything we build or correct stays in your name, and you keep every login. What you do next is up to you.</p></div>\n'
            '    </div>\n  </div>\n</section>\n\n' % e(TERMS))
    out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">Questions</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">What Owners Ask <em>First</em></h2>\n    </div>\n'
            '    <div class="qa-list">\n%s    </div>\n  </div>\n</section>\n\n' % faq_html(s["faqs"]))
    if pack:        # the three Get Found packages point at each other
        out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
                '      <span class="eyebrow reveal">The Get Found packages</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Not Quite <em>Your Case</em>?</h2>\n'
                '      <p class="reveal">There are three Get Found packages. Which one fits depends on your website.</p>\n    </div>\n'
                '    <div class="ot-cards">\n%s    </div>\n  </div>\n</section>\n\n' % "".join(package_card(p) for p in PACKAGES if p is not s))
    rel = "".join('      <div class="ot-card reveal"><span class="ot-price">%s one time</span><h3><a href="%s.html">%s</a></h3><p>%s</p></div>\n'
                  % (BY_SLUG[r]["price"], r, e(BY_SLUG[r]["name"]), e(BY_SLUG[r]["gets"][0])) for r in s["related"])
    reads = "".join('<a href="%s">%s</a>' % (h, t) for h, t in s["reads"] + [s["solution"], (HUB, "Every one-time job"), ("pricing.html", "Monthly plans")])
    rel_head = ("What is in it", "The Parts, <em>On Their Own</em>") if pack else ("Related jobs", "Often Bought <em>Alongside</em>")
    out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">%s</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">%s</h2>\n    </div>\n'
            '    <div class="ot-cards">\n%s    </div>\n    <div class="ot-links reveal">%s</div>\n  </div>\n</section>\n\n' % (rel_head + (rel, reads)))
    out += cta_block() + drawer(x_icon, s["pins"], ("contact.html", "Get the free audit")) + foot
    return out


def hub_page(assets, nav, foot, x_icon):
    desc = ("One-time jobs and packages with one price each: the three Get Found packages, a Google listing fix, a new website you own and more. "
            "Half up front, half when the job is done. No monthly plan required.")
    faqs = [("Do I need a monthly plan to buy one of these?", "No. Each one is a single job with a single price. There is no plan, no contract and nothing to cancel."),
            ("How do I pay?", TERMS),
            ("What is a package?", "Several jobs sold as one job, for less than the jobs cost one at a time. "
             + " ".join("%s is %s. %s" % (p["name"], p["price"], p["who"]) for p in PACKAGES)),
            ("Which job should I start with?", "The free audit answers that. It shows what is wrong with your Google listing and your website. If one job would close the gap, it names it, and if nothing needs fixing it says so."),
            ("What is the difference between a one-time job and a monthly plan?", "You buy the build once and you own it. A monthly plan is optional, and what it does is keep your website and your listing working after the job is done.")]
    schema = [
        {"@context": "https://schema.org", "@type": "ItemList", "name": "One-time services", "itemListElement": [
            {"@type": "ListItem", "position": i, "name": s["name"], "url": "%s/%s.html" % (SITE, s["slug"])} for i, s in enumerate(PACKAGES + JOBS, 1)]},
        crumbs("One-Time Services", None),
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
    ]
    pins = [("key", "You buy it once", "A website or a fix is a single job with a single price. You pay for it once and you own what was built.",
             ["One price per job", "No plan and no contract", "Yours to keep"]),
            ("chart", "Half up front", TERMS + " There is no plan and nothing to cancel.",
             ["Half up front", "Half when the job is done", "No contract"]),
            ("pin", "Start with the audit", "The free audit shows what is wrong and, where one job would close the gap, names it, so you are not choosing from a menu blind.",
             ["Free, and yours to keep", "Your own numbers", "One job named, not a menu"]),
            ("page", "A plan is optional", "A monthly plan keeps the website and the listing working after the job is done. Plenty of owners buy the job and stop there.",
             ["Upkeep, not the build", "Month to month", "Only if you want it"])]
    out = head("One-Time Services, One Price Each", desc, HUB[:-5], schema, assets) + nav
    out += hero("One-Time Services", "Buy the Job <em>Once</em>. Own It.", "Not everything needs a monthly plan. These are single jobs with a single price: you see what is wrong, you buy the fix, and it is yours.",
                "websites-seo-hero", ("contact.html", "Get Your Free Audit"), ("#packages", "See Packages and Jobs"))
    out += ('<section id="packages" class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">Packages</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Get Found, <em>Three Ways</em></h2>\n'
            '      <p class="reveal">A package is several jobs sold as one, for less than the jobs cost one at a time. Which one fits depends on your website.</p>\n    </div>\n'
            '    <div class="ot-cards">\n%s    </div>\n  </div>\n</section>\n\n' % "".join(package_card(p) for p in PACKAGES))
    cards = "".join('      <div class="ot-card reveal"><span class="ot-price">%s one time</span><h3><a href="%s.html">%s</a></h3><p>%s</p>'
                    '<a href="%s.html" style="color:var(--gold);text-decoration:none;font-size:.9rem;margin-top:auto">See what it covers &rarr;</a></div>\n'
                    % (s["price"], s["slug"], e(s["name"]), e(s["sub"].split(". ")[0] + "."), s["slug"]) for s in JOBS)
    cards += "".join('      <div class="ot-card reveal"><span class="ot-price">%s</span><h3>%s</h3><p>%s</p></div>\n' % (p, e(n), e(d)) for n, p, d in SMALL)
    out += ('<section id="jobs" class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">The jobs</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">One Job, <em>One Price</em></h2>\n'
            '      <p class="reveal">Every job is paid half up front and half when it is done.</p>\n    </div>\n'
            '    <div class="ot-cards">\n%s    </div>\n  </div>\n</section>\n\n' % cards)
    out += ('<section id="covers" class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">How it works</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">Tap a <em>+</em> for the detail</h2>\n    </div>\n'
            '    <div class="ot-pins reveal">\n%s    </div>\n  </div>\n</section>\n\n' % pins_html(pins))
    out += ('<section class="section rule-top">\n  <div class="container">\n    <div class="section-head">\n'
            '      <span class="eyebrow reveal">Questions</span>\n      <h2 class="display display-lg reveal" style="margin-top:1.6rem">What Owners Ask <em>First</em></h2>\n    </div>\n'
            '    <div class="qa-list">\n%s    </div>\n    <div class="ot-links reveal"><a href="pricing.html">Monthly plans</a><a href="solution-websites-seo.html">Websites &amp; SEO</a>'
            '<a href="solution-reviews.html">Reviews &amp; Reputation</a><a href="switching-from-hibu-thryv.html">Switching from Hibu or Thryv</a></div>\n  </div>\n</section>\n\n' % faq_html(faqs))
    out += cta_block() + drawer(x_icon, pins, ("contact.html", "Get the free audit")) + foot
    return out


def main():
    assets, nav, foot, x_icon = shell()
    pages = {HUB: hub_page(assets, nav, foot, x_icon)}
    for s in SERVICES:
        pages[s["slug"] + ".html"] = service_page(s, assets, nav, foot, x_icon)
    for name, key in [(s["slug"] + ".html", k) for s in SERVICES for k in ("title", "meta", "h1")]:
        assert sum(1 for s in SERVICES if s[key] == BY_SLUG[name[:-5]][key]) == 1, (name, key, "not unique")
    for name, body in pages.items():
        text = re.sub(r"<script.*?</script>|<nav.*?</nav>|<footer.*?</footer>", "", body, flags=re.S)
        for bad in ("hosting", "hosted", "guarantee", "—", "–", "Blend"):
            assert bad not in text, (name, bad)
        low = text.lower()
        for bad in ("refund", "money back", "money-back", "leak", "tune-up", "tune up", "photograph", "photos", "free website", "free logo",
                    "elevate", "seamless", "unlock", "$275", "$295", "$395"):
            assert bad not in low, (name, bad)
        # Only the map-pack push has dated checks; no other one-time job carries a timeframe or a report.
        if not name.startswith("map-pack"):
            assert not re.search(r"\b\d+ (?:days?|weeks?)\b|before-and-after|report", low), (name, "a timeframe or a report")
        assert not re.search(r"\$[\d,]+\s*(?:/|a |per )mo", text), (name, "a monthly price")
        assert body.count("<h1") == 1 and body.count('rel="canonical"') == 1, (name, "h1 or canonical")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', body, re.S):
            json.loads(block)
        for href in set(re.findall(r'href="([^"#:]+\.html)', body)):     # every internal link lands on a real page
            assert href in pages or os.path.exists(os.path.join(ROOT, href)), (name, "dead link", href)
        if name != HUB:
            s = BY_SLUG[name[:-5]]
            assert s["price"] in text and TERMS in text, (name, "price or terms missing")
            if "parts" in s:
                assert money(parts_total(s)) in text and all(p["slug"] + ".html" in text for p in PACKAGES if p is not s), (name, "package")
        with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(body)
    print("wrote %d pages: %s" % (len(pages), ", ".join(sorted(pages))))


if __name__ == "__main__":
    main()
