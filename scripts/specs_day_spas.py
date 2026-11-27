"""Per-page content specs for the SEO corpus, day spas batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, day-spa-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the massage, med-spa, nail, or hair-salon content reworded.

Salon, Spa & Fitness hub, shared with specs_massage_therapy.py, specs_nail_salons.py, and
specs_hair_salons.py. Four service angles live here in one file (the ai-receptionist dict
carries "demo": True). A day spa is a full-service relaxation and wellness destination that
sells massage, facials, body wraps and scrubs, and sauna or steam as bookable treatments, and
above all packages, memberships, and gift cards, so this file is written around a front desk
that cannot answer while it is with a guest or turning over a treatment room, the gift-card and
gifting-season revenue that is a huge share of a spa's year, rebooking guests on a relaxation
cadence, converting a gift-card visit into a regular, and selling and redeeming gift cards and
memberships. It stays relaxation and wellness, never medical, so it makes no medical or
health-outcome claims and never blurs into the med-spa (injectables and clinical) sibling, and
it is distinct from single-modality massage and from hair and nail salons. Each example body
ends with the literal "Illustrative example, not a client." per the honesty rule; if the
generator also appends that line, dedupe there.
"""

SPECS = [
# ============================= AI Receptionist for Day Spas =============================
{
    "slug": "ai-receptionist-for-day-spas", "demo": True,
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "AI Receptionist for Day Spas",
    "title": "AI Receptionist for Day Spas | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Day Spas",
    "meta_desc": "A day spa answering service answers every booking, package, and gift card call the moment it rings and books the room while your front desk is with a guest.",
    "service_schema_name": "AI Receptionist for Day Spas",
    "eyebrow": "For Day Spas",
    "h1_html": "AI Receptionist <em>for Day Spas</em>",
    "answer_block": "A day spa answering service answers every call and text the moment it lands, sorts a couples booking from a gift card question or a guest asking what a package includes, and books the room while your front desk is turning over a treatment room. The number stays yours, and so does every guest it books.",
    "sections": [
        {"h2_html": "The call you miss is the guest who <em>books the spa down the road</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The front desk at a day spa is one person doing several things at once, checking a guest in, walking someone back to the relaxation lounge, turning over a treatment room, ringing up a candle from the retail shelf, and the phone rings through all of it. A day spa\'s calls are also more involved than most: someone wants to know what the signature package includes, whether a couples room is free on Saturday, how to buy a gift card for a birthday, whether the facial comes with time in the steam room. Those callers do not leave a voicemail. They call the next spa, and the one after that, until someone picks up. And the caller you lose is not one visit, it is the whole spa day, the package, and the standing monthly guest they might have become.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up the moment the call lands, warm and unhurried the way a spa should sound, answers what a package includes or whether a couples suite is open, and books the room or captures the details so nothing is lost. The booking is captured and scheduled instead of handed to the spa down the road that simply had someone free to reach the phone.</p>'},
        {"h2_html": "Gift card and package questions are <em>real bookings, not interruptions</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A big share of a day spa\'s phone traffic is people trying to hand you money in a way that takes a minute to explain. Someone wants a gift card for a spa day but is not sure which package to put on it. A partner wants to book a couples massage for an anniversary and needs to know what is included and whether a room is open that evening. A guest wants to add a friend to their membership. These are not quick yes-or-no calls, and they are exactly the ones a front desk with a guest in front of them has to let ring out. The caller trying to buy a gift card is the easiest sale you will ever miss, because they will simply buy one wherever answers first.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answering service handles these the way an attentive coordinator would. It explains what a package includes, points a gift buyer to the right option, checks the book for an open couples room, and either takes the booking or captures the buyer\'s details so your team can finish the sale. A gift card inquiry becomes a sale, and a package question becomes a booked spa day, instead of both slipping to a spa that was easier to reach.</p>'},
        {"h2_html": "Built around how a day spa <em>actually books</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">No two calls to a day spa are the same, and an off-the-shelf call center reading a script cannot tell a sixty-minute facial from a half-day package, a single guest from a couples booking, or a gift card question from a rebooking regular. The answering service handles the conversation the way a calm front desk would on an unhurried afternoon.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers calls and texts around the clock, so the guest who books at midnight and the one who calls on a quiet Sunday both reach a real reply instead of a voicemail box.</li><li>Books the right service or package into the right room for the right length of time, and knows a couples suite, a body wrap, and a full spa day each need different space on the book.</li><li>Takes gift card and package questions and either captures the buyer or hands you the details, so a seasonal gift does not slip to a spa that was easier to reach.</li><li>Treats a member or a standing monthly guest differently from a first-time caller, so the people who already come to unwind with you never feel like they are explaining themselves to a stranger.</li></ul>'},
        {"h2_html": "You own the number, the calls, and <em>the guest list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on the number your spa already uses, or a new one put in your name, never a line we own. Every caller, every text, and every booking it takes stays exportable whenever you want it, because the guest list a day spa builds over the years is the most valuable thing it owns, and it should never be locked behind a contract or rented back to you a month at a time. And it does not work off on its own. It is one piece of the Top Shelf platform, so every booking it takes drops into the CRM that rebooks and follows up, which is how a first spa day becomes a standing monthly visit and a gift card guest becomes a regular. There is nothing for you to run and nothing to answer; it works quietly in the background while your front desk stays with the guest in front of them.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A gift card call at closing, captured while the front desk <em>walks a guest out</em>",
        "body_html": "It is ten minutes to close and someone calls wanting to buy a spa-day gift card for their mom's birthday that weekend, unsure whether to put the massage-and-facial package or the full day on it. Your one front desk person is walking the last guest of the evening out and cannot get to the phone. Instead of ringing through to voicemail, the answering service picks up, warmly walks the caller through what each package includes, and captures their details and what they want to buy so your team can finish the gift card sale first thing in the morning. The buyer feels looked after, you keep a sale that can pay for the whole month, and no one had to abandon a guest at the door. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current spa phone number?",
         "Yes. It can answer on your existing spa number, or set up a new one registered in your name. Either way the number and every call, text, and booking that comes through it belong to you and go with you if you ever leave."),
        ("Can it answer questions about packages, couples bookings, and gift cards?",
         "Yes, and those are some of the most valuable calls a day spa gets. It explains what a package includes, checks whether a couples room is open, and walks a gift buyer to the right option, then books the room or captures the details so your team can finish a gift card sale instead of losing the caller to a spa that picked up."),
        ("Can it answer texts, not just calls?",
         "Yes. A lot of guests reach out by text after hours or while they are deciding on a spa day, and the answering service replies to those in seconds, answers the first question, and books the room, so a late message does not sit until your front desk is free the next day."),
        ("Will it sound like a robot to someone booking a relaxing day?",
         "It answers warmly and calmly, the way a spa should sound, and it is upfront rather than pretending to be a person. Someone booking an escape mostly wants to feel that a real, welcoming spa has them scheduled, and a warm reply that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your packages, your rooms, your hours, and your booking rules for you, so it is answering in days, not weeks.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for day spas"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-day-spas.html", "The CRM that rebooks every guest you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending gift card and package calls to <em>voicemail</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# ================================= CRM for Day Spas =================================
{
    "slug": "crm-for-day-spas",
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "CRM for Day Spas",
    "title": "CRM for Day Spas | Top Shelf Business Solutions",
    "og_title": "CRM for Day Spas",
    "meta_desc": "A CRM for day spas keeps every guest, package, membership, and gift card in one place and rebooks them for you, so a monthly spa guest keeps coming back.",
    "service_schema_name": "CRM for Day Spas",
    "eyebrow": "For Day Spas",
    "h1_html": "CRM <em>for Day Spas</em>",
    "answer_block": "A CRM for day spas keeps every guest, package, membership, and gift card in one place and rebooks them for you, so the guest due for a monthly facial and the one who came in once on a gift card both return to unwind with you instead of drifting off. Your guest list quietly becomes revenue that repeats.",
    "sections": [
        {"h2_html": "The guest who does not rebook is the revenue you are <em>quietly losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most day spas the trouble is not filling the appointment book once, it is getting a guest back on the rhythm relaxation runs on. Someone who comes in for a monthly facial or a regular massage is not a single sale, they are a standing visit for as long as the habit holds, and a member is that plus a payment every month. When a guest leaves the relaxation lounge without the next visit booked, the way people do when they are floating out the door unwound and not thinking about calendars, that room time does not vanish, it sits empty or someone else takes it, and the repeat revenue that guest represented drifts off with them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM holds every guest and their history where you can see it and sends the rebooking nudge itself, by text or email, timed to the rhythm each guest keeps. The one who likes a facial every few weeks hears from you right around when they are due, books the next visit, and stays on a relaxation cadence instead of letting months slip past and eventually trying whatever spa is nearest when they think of it again. You never sit down to chase it, and the standing visit keeps standing.</p>'},
        {"h2_html": "Gift cards, packages, and memberships only pay off if they get <em>used</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa sells more prepaid, promised, and gifted value than almost any local business, and every bit of it quietly slips away when nobody is tracking it. A gift card sits in a drawer unredeemed. A package someone bought for the discount goes half-finished. A member stops coming in but keeps paying, until they notice and cancel. None of that is a guest problem, it is a follow-up problem, and it is exactly what a front desk with rooms to turn over never finds time to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Gift cards are tracked from sale to redemption, so an unused card gets a gentle reminder and the guest a gift brought in is invited back on their own instead of disappearing after one visit.</li><li>Prepaid packages are tracked against the right guest, so the spa days someone already paid for actually get booked and used before they are forgotten.</li><li>Memberships are watched too, so a member who has not been in this month hears from you before they start wondering what they are paying for and cancel.</li><li>Every guest, their treatments, preferences, preferred therapist or esthetician, and full history live in one record instead of scattered across a booking app, a card file, and memory.</li></ul>'},
        {"h2_html": "The gift card visit and the lapsed guest are both a <em>goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Two of the highest-return hours a day spa can spend cost almost nothing, because in both the trust is already there. The first is the guest a gift card brought in: they have already been inside, felt the space, and enjoyed a treatment, and a warm note a couple of weeks later, inviting them back on their own, turns a one-time gifted visit into a paying regular more often than you would guess. The second is the guest who used to come and quietly stopped, not because anything went wrong but because life got busy and no reminder ever came. A lapsed guest has nothing to relearn, their preferences and history are all on file, and a well-timed, gentle message brings a real share of them back to unwind.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The CRM surfaces both, the gift recipient who never rebooked and the regular who went quiet, and sends the message for you, so guests you had written off land back on the calendar without anyone combing through old records.</p>'},
        {"h2_html": "Fewer empty rooms, and a guest list <em>you own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A no-show or a late cancellation on a booked treatment room is some of the most expensive time a day spa has, because a room and a therapist\'s hour sit idle and neither can be sold tomorrow. Automatic confirmations and reminders go out ahead of every appointment, the most reliable way to hold no-shows down and give a guest an easy way to move their time instead of simply not arriving. And when a cancellation does open a room, the CRM can quietly offer it to guests who asked for something sooner, filling it before the hour is gone. Everything, every guest and every note, stays yours to export whenever you like, never trapped in software you only rent, and because the CRM runs on the same database as the answering service, a booking the phone takes shows up here and gets worked without anyone re-entering it. Nothing you have already earned is left to go cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The gift card guest who becomes a <em>monthly regular</em>",
        "body_html": "Someone comes in on a spa-day gift card their sister gave them, has a wonderful afternoon, and floats out without booking again, the way most people do on a gift they did not pay for. Ordinarily that is the last you would see of them. Instead, two weeks on, the CRM sends a warm note in your spa's voice, thanking them for coming in and offering an easy way to book their own visit, with the treatments they enjoyed already noted. They book a facial for the next month, and a few visits later they are on the membership. A guest who arrived on someone else's card became a regular of their own, and no one at the front desk had to remember them. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing guests and their history?",
         "Yes. Your current guests, their contact details, treatments, preferences, preferred therapist or esthetician, notes, and past visits come in and live in one place, and everything stays yours and exportable. The point is to make the guest list you already have actually work for you."),
        ("Will it really prompt guests to rebook on their own?",
         "Yes, on the cadence you set. A monthly facial or massage guest can hear from you right around when they are due, all sent for you, so the standing visits keep rebooking instead of depending on someone remembering at the front desk while a guest is checking out. You can message anyone directly any time too."),
        ("Can it track gift cards, packages, and memberships?",
         "Yes, and for a day spa that is where a lot of quiet revenue slips away. Gift cards are tracked from sale to redemption, prepaid packages against the right guest, and memberships too, so an unused card, a half-finished package, or a member who has drifted all get a nudge before the value goes to waste."),
        ("Can it win back a gift card visitor or a guest who stopped coming?",
         "Yes, and both are among the cheapest business a day spa can win. It can invite a guest a gift card brought in to come back on their own, and reach a lapsed regular with a warm, well-timed message, both sent for you, so a one-time visit or a name you had given up on turns back into a booking."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your guests, build your rebooking and win-back reminders, and connect it to your calls and calendar, so it is working in days.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for day spas"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-day-spas.html", "The answering service that feeds it every booking"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting guests and gift cards <em>go cold</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
# =============================== Marketing for Day Spas ===============================
# ============================= Websites for Day Spas =============================
{
    "slug": "websites-seo-for-day-spas",
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Websites for Day Spas",
    "title": "Websites for Day Spas | Top Shelf Business Solutions",
    "og_title": "Websites for Day Spas",
    "meta_desc": "A day spa website built for SEO ranks for spa near me and spa packages, feels as serene as the visit, and lets a guest book a room or buy a gift card in a tap.",
    "service_schema_name": "Websites for Day Spas",
    "eyebrow": "For Day Spas",
    "h1_html": "Websites <em>for Day Spas</em>",
    "answer_block": "A day spa website built for SEO ranks for what a guest types, spa near me, spa packages, couples massage, or a spa gift card, feels as serene as the visit, and lets someone book a room or buy a gift card in a tap, so the guest and sale stay yours.",
    "sections": [
        {"h2_html": "Your website has to feel like the <em>escape you sell</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa sells calm, and the first test of whether you can deliver it is your own website. A guest lands on it from a search or your profile, and in a few seconds they are deciding whether this looks like the serene, cared-for place they want to spend an afternoon, whether you offer the treatments and packages they have in mind, and whether booking is going to be simple. A slow, cluttered, dated site does the opposite of what a spa is for, it puts a person on edge, and they leave for the spa whose site felt like a deep breath. So the build starts from that feeling: calm, uncluttered pages, real photos of the rooms and the relaxation lounge, and a clear, unhurried path to booking, all of it fast on a phone, because that is where they are looking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A genuinely lovely spa with an afterthought of a website loses guests it never even hears about, and loses them to spas that are not necessarily better, only easier to picture and easier to say yes to.</p>'},
        {"h2_html": "Rank for what a guest types when they want to <em>get away</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone wants a spa, the search is specific and local: day spa near me, facial near me, couples massage, spa packages, a spa day, a spa gift card near me. The very top of that results page is often a booking marketplace or a directory, not the spas themselves, because those sites run thousands of pages on years of built-up authority, and a searching guest lands there first, where the booking gets passed around or skimmed for a cut. You will not knock a national directory off the single broadest term this year, and you do not have to. The winnable ground is your own spa name, the neighborhoods you draw from, and the specific things a guest types when they are ready, each treatment, each package, and the gift searches that climb around the holidays. Pages built around the treatments and packages you actually offer and the area you actually serve are what search engines, and a guest ready to book, reward with the click, because a national app has no reason to write a real page about your spa or your town. The local, specific searches can start moving within weeks while the broad head term compounds over months.</p>'},
        {"h2_html": "Booking a room and buying a gift card should both take <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa website has two jobs a single-service business does not, and it has to do both effortlessly. The first is booking: a guest deciding on a spa day, often at night, wants to see the menu and packages clearly, understand what each one includes, and reserve a room or a couples suite in a tap on your real availability, not fill out a form and wait for a callback while the mood passes. The second is the gift card, and this is the one most spa sites get wrong. A gift buyer is often ready to spend right now, late at night, days before an occasion, and if buying a gift card means calling during business hours or driving in, that sale goes to whatever spa lets them buy one online in the moment. A site that puts online gift card purchase right up front, next to easy booking, catches money that would otherwise walk out the door. Clear service and package names, plainly showing what is included, matter here more than in most trades, because a guest choosing a spa day wants to know exactly what they are booking or gifting before they commit.</p>'},
        {"h2_html": "The guest and the sale belong to <em>you</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A booking that comes through a marketplace or a pay-per-guest app always skims its cut, was never fully yours, and vanishes the day you stop paying the platform. A site you own goes on ranking, goes on showing your rooms and your menu, and goes on taking bookings and gift card sales for as long as it is up, and it sits under your name, not a platform that can rewrite its terms or drop you. It feeds straight into the same CRM that rebooks the guests it brings in and turns a gift card visit into a regular, and the answering service that fields the callers who would rather ask about a package than tap through a menu, so nothing it earns you slips through the cracks. What you are building is an asset that gains value over the years, not a rent you keep paying just to reach your own guests.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late-night gift card, bought before the <em>tab closes</em>",
        "body_html": "It is nearly midnight and someone has just remembered an anniversary is days away and they still have nothing. They search for a spa gift card near them, and instead of a marketplace that would line up ten spas and take a cut, they find your site ranking for that search. It looks calm and inviting, the packages are laid out plainly so they can see exactly what a spa day includes, and there is a clear button to buy a gift card right there. They buy a couples package as a gift before they close the tab, no phone call, no waiting until morning, no cut taken by a middleman. The sale is yours, and a few weeks later that gift card walks two new guests through your door. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and booking apps?",
         "Not for the broadest terms overnight. It can realistically rank for your spa name, your specific neighborhoods, and the treatment, package, and gift searches a national app has no reason to target well, facials, couples massage, spa packages, and a spa gift card near you, which is exactly where a local spa can win."),
        ("Can guests book a room and buy a gift card right from the site?",
         "Yes, and for a day spa both matter. The site puts easy booking on your real availability and online gift card purchase right up front, so a guest can reserve a spa day or buy a gift in a tap, at night, when the decision is made, instead of calling during business hours or letting the moment pass."),
        ("Can it clearly show my packages and what each one includes?",
         "Yes, and it should. A guest choosing a spa day or a gift wants to know exactly what is in each package before they commit, so we lay your menu and packages out plainly, which both earns the booking and answers the question a guest would otherwise call to ask."),
        ("Most of my guests come from word of mouth and gift cards. Does a website even help?",
         "Yes, because a referred guest and a gift card recipient both look you up before they book, and a gift buyer often wants to purchase online in the moment. A fast, serene, easy-to-book site with online gift card purchase is what turns all of that interest into a booking or a sale instead of losing it to a spa that made it easier."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for day spas"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search for <em>a day spa in your town</em>",
    "cta_sub": "Try the CRM and see how it answers calls, books jobs, and follows up on every lead. No credit card, never a call center.",
},
]
