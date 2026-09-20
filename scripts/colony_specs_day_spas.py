"""Colony page specs for DAY SPAS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a day spa owner would search, answered directly up top (the 40-60 word
AEO answer), then two body sections, then a "the fix" bridge that funnels the page's authority
into the ONE money page the question implies. Lighter than a money page.

A DAY SPA is a full-service RELAXATION DESTINATION, not a single-modality massage practice and not
a medical med spa. It bundles massage, facials, body treatments, and time in the sauna or steam room
under one roof, and its revenue base is PACKAGES, MEMBERSHIPS, and GIFT CARDS, with the gifting
seasons (Mother's Day, the holidays, Valentine's Day) doing an outsized share of the year. One busy
front desk juggles in-spa guests while the phone rings with "what does the package include, can I
book a couples massage, how do I buy a gift card", and guests are rebooked on a relaxation cadence
rather than around any clinical due date. Every dict here owns UNIQUE, hand-written, day-spa-specific
substance (the generator owns shell, schema, events, keyword placement), and stays deliberately
DISTINCT from the med_spas and (single-modality) massage colonies: guests unwinding, not patients;
gift cards and packages, not Botox and filler; a serene destination, not a clinic or one massage room.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real Top Shelf prices ($299/$899 plans, $1,500 one-time site) ever appear, and
the spa's OWN package, membership, and gift card pricing stays generic with no numbers; no em/en
dashes anywhere; never "leak" as a metaphor. ETHICS: the AI receptionist does scheduling, booking,
and intake ONLY, and nothing here promises a health, medical, or wellness outcome; the day spa sells
relaxation, not treatment.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 day-spa-website-cost              (cost)     -> websites-seo-for-day-spas
  2 day-spa-answering-service-cost    (cost)     -> ai-receptionist-for-day-spas
  3 is-a-crm-worth-it-for-a-day-spa   (cost)     -> crm-for-day-spas
  4 why-day-spas-miss-calls           (problem)  -> ai-receptionist-for-day-spas
  5 why-spa-guests-dont-rebook        (problem)  -> crm-for-day-spas
  6 how-do-day-spas-get-more-clients  (how-to)   -> marketing-for-day-spas
"""

TOPICS = [
# ==================== How Much Does a Day Spa Website Cost? (cost -> websites-seo) ====================
{
    "slug": "day-spa-website-cost",
    "h1": "How Much Does a Day Spa Website Cost?",
    "title": "How Much Does a Day Spa Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A day spa website should book a spa day and sell gift cards online. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A day spa website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more is whether it books a spa day, sells a gift card online, and shows your packages and memberships clearly. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a day spa website actually <em>has to do</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa website is not a brochure, it is the front door to an escape, and it has two jobs a generic site never considers: it has to let a guest book a spa day and buy a gift card online, on their own, the moment the urge to unwind arrives. The site should feel like the calm you sell, unhurried and warm, so a visitor senses the relaxation before they ever walk in, and it should make the whole menu easy to take in: the massages, the facials, the body treatments, the time in the sauna or steam room, and the packages that bundle them into a half day or a full one. It is a relaxation destination, not a single massage room and not a medical clinic, so the site has to show a full experience rather than one service or a wall of credentials. It also has to be found. When someone searches for a day spa near them, for spa packages, or for a couples massage, or goes looking for a spa gift card around Mother's Day, the holidays, or Valentine's Day, your site has to turn up and let them act right there. A beautiful page that hides the booking button and cannot take a gift card sale is the most expensive kind, because you paid for it and it quietly turns visitors away.</p>'''},
        {"h2_html": "What a day spa should actually <em>pay for</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you know the site has to book, sell gift cards, and rank, the price makes more sense. A do-it-yourself builder is cheap each month, but you do the work and it rarely ranks or captures a booking on its own. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is handling the ongoing SEO that gets it found for the searches people make when they are planning an escape or shopping for a gift. An agency that bundles the build with ongoing SEO, the online booking, and the gift card storefront is where most of the long-term value lives, and also where the monthly cost lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'''}],
    "bridge_h2": "Get a site that books and sells for you",
    "bridge_text": "A day spa website is only worth the bookings and gift cards it brings in. Ours is built to feel like the calm you sell, rank for the searches guests make, and let them book a spa day or buy a gift card without ever picking up the phone.",
    "bridge_slug": "websites-seo-for-day-spas",
    "bridge_label": "Websites & SEO for day spas",
    "faqs": [
        ("Is a cheap template site good enough for a day spa to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks for a day spa near me or lets a guest book a spa day and buy a gift card on their own, and you do the upkeep. A serene site that cannot take a booking or a gift card sale is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ What Does a Day Spa Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "day-spa-answering-service-cost",
    "h1": "What Does a Day Spa Answering Service Cost?",
    "title": "What Does a Day Spa Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Day spa answering services often bill per call or minute. Top Shelf includes an AI receptionist that answers and books 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for day spas usually bill per call, per minute, or a monthly retainer, so a busy gifting season gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and text and books the room comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a busy stretch turns into a big bill. A day spa gets its heaviest phone traffic at the times a live front desk can least step away: evenings and weekends when people plan a spa day, and the gifting rushes around Mother's Day, the holidays, and Valentine's Day, when the phone barely stops with gift card questions. Those are exactly the minutes an after-hours or overflow service tends to charge the most for. It helps to know the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy gifting week or a wave of browsers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a caller working out which package to gift, or weighing a couples massage against a full spa day, costs more than a quick one, and those are your best calls.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'''},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a guest planning a spa day, or someone trying to buy a gift card before a birthday, does not leave a voicemail, they book with the spa that picked up. The real cost of no coverage is not a monthly fee, it is the whole spa day, the package, and the standing monthly guest that caller might have become, all handed to whoever answered. But a generic call center reading a script cannot explain what a signature package includes, check whether a couples suite is open on Saturday, or walk a gift buyer to the right option, so you can pay for coverage and still lose the booking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring by phone and text, day or night, warm and unhurried the way a spa should sound. It explains a package, checks the book for a couples room, and either books the visit or captures the details so your team can finish a gift card sale. It handles scheduling and booking only, and it comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter. One gift card or spa day it saves on a busy weekend can be worth well more than the plan, and everything after that is on top.</p>'''}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers by phone and text 24/7, explains a package, checks a couples room, and books it or captures a gift card sale, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-day-spas",
    "bridge_label": "AI receptionist for day spas",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly through your busiest gifting seasons, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the spa day or gift card it books after hours instead of losing to voicemail."),
        ("Does it cost extra for evenings, weekends, or the holiday rush?",
         "No. It answers 24/7 as part of the plan, including the weekend planners and the Mother's Day and holiday gift card calls that are some of your best of the year, with no after-hours surcharge or overage.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============== Is a CRM Worth It for a Day Spa? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-day-spa",
    "h1": "Is a CRM Worth It for a Day Spa?",
    "title": "Is a CRM Worth It for a Day Spa? | Top Shelf Business Solutions",
    "meta_desc": "For most day spas a CRM pays for itself by rebooking one guest and reviving one unused gift card. It comes in Top Shelf's Signature plan at $899 a month.",
    "answer": "For most day spas, yes. A CRM pays for itself the first time it rebooks a monthly facial guest before the habit fades, or brings back a gift card visitor who came in once. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it for a day spa, and when it is <em>not</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a day spa when you have more guests, packages, memberships, and gift cards than anyone at the front desk can keep track of, which is most established spas. It is not worth it if you are brand new with a handful of guests and genuinely reaching every one of them on time, though that rarely stays true as you grow. A day spa carries an extra layer most businesses do not: prepaid packages, memberships billing every month, and a pile of gift cards from the last gifting season, all of it money already collected that only turns into revenue when the guest actually comes in to use it. The honest test is simple. How many guests who like a monthly massage or facial are overdue to rebook right now, how many gift cards from Mother's Day or the holidays are sitting unredeemed, how many prepaid package visits have gone unused, and how many members have quietly stopped coming in? Those are the visits, and the value, a CRM is built to recover before they drift away.</p>'''},
        {"h2_html": "What it actually <em>earns a day spa</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a day spa is not the software, it is the repeat business that stops slipping away. Relaxation is a habit, and a habit only holds if something keeps it going: a guest who loves a monthly facial, a couples visit that could become a standing date, a package with visits still on it, a membership renewing every month. Each one is revenue you have already half-earned and are one well-timed, warm reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It nudges each guest on the rhythm they keep, so a monthly massage or facial rebooks without anyone at the desk tracking dates.</li><li>It watches gift cards, packages, and memberships, so an unredeemed card, a half-used package, or a member who has drifted all get a gentle reminder before the value goes to waste.</li><li>It keeps every guest, their treatments, their preferred therapist or esthetician, and their notes in one record instead of scattered across a booking app, a card file, and memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. Recover one lapsed guest or redeem one forgotten gift card and it has paid for itself, and the repeat visits after that are margin.</p>'''}],
    "bridge_h2": "Turn your guest list into repeat visits",
    "bridge_text": "The guests you already have are the cheapest bookings a day spa can get. A CRM reminds each one when they are due, chases down unused gift cards and packages, and revives the ones who drifted, so they come back to unwind with you instead of drifting off.",
    "bridge_slug": "crm-for-day-spas",
    "bridge_label": "CRM for day spas",
    "faqs": [
        ("Is a CRM overkill for a small day spa?",
         "Not usually. Even a small spa carries more guests, packages, memberships, and gift cards than anyone can track by memory. The point is not size, it is whether rebooking and follow-up are falling through. If guests drift past due and gift cards go unredeemed, a CRM earns its keep."),
        ("How is a CRM different from the booking tool I already use?",
         "A booking calendar records appointments. It does not nudge a guest who is due to rebook, flag a gift card or package going unused, or revive someone you have not seen in a year. A CRM does all of that on a schedule, so the repeat visits show up instead of depending on memory.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Do Day Spas Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-day-spas-miss-calls",
    "h1": "Why Do Day Spas Miss So Many Calls?",
    "title": "Why Do Day Spas Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Day spas miss calls because one front desk is with a guest while the phone rings with package and gift card questions. The caller who hits voicemail books elsewhere.",
    "answer": "Day spas miss calls because they come when the one person at the front desk is checking a guest in, walking someone to the lounge, or turning over a treatment room. The caller with a package, couples, or gift card question does not leave a voicemail, they book with the next spa that answers. A lot of that interest also lands after hours.",
    "sections": [
        {"h2_html": "The call comes while your front desk is <em>with a guest</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A day spa front desk is one person doing several things at once. When the phone rings they are checking a guest in, walking someone back to the relaxation lounge, turning over a treatment room between appointments, or ringing up a candle from the retail shelf, and the call rings through all of it. The busier the day, the more calls roll past, which means your fullest afternoons are also the ones where the most new bookings slip away. It is not a discipline problem. One person simply cannot tend the guest in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for someone planning a relaxing day it is not one. A caller deciding between a couples massage and a full spa day, or trying to buy a gift card before a birthday, will not leave a message and wait. They move down the list until a warm voice picks up, and by the time anyone checks the voicemail box, that spa day is already booked somewhere else. The call you could not get to was not a quick question, it was a booking walking out the door.</p>'''},
        {"h2_html": "The calls you miss are your <em>most valuable ones</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The ones a day spa lets ring are often the most involved, and the most valuable: a caller asking what the signature package includes, whether a couples suite is free on Saturday, or how to buy a spa-day gift card for a birthday. Those take a minute to talk through, which is exactly why a front desk with a guest in front of them has to let them go, and exactly why they are worth the most. A gift card caller is the easiest sale you will ever lose, because they will simply buy one wherever answers first. A good share of it also arrives when no one is there at all: someone planning a weekend escape on a Thursday night, or shopping for a present during the Mother's Day or holiday rush.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can actually handle a spa conversation. What works is something that answers on the first ring by phone and text, warm and unhurried, explains what a package includes, checks the book for a couples room, and books the visit or captures a gift card sale, handling scheduling and booking only, so the guest is caught instead of lost to a voicemail box.</p>'''}],
    "bridge_h2": "Stop sending bookings to voicemail",
    "bridge_text": "An AI receptionist answers every call and text on the first ring, day or night, warm the way a spa should sound, explains a package, checks a couples room, and books it or captures a gift card sale, so the booking never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-day-spas",
    "bridge_label": "AI receptionist for day spas",
    "faqs": [
        ("Would a guest rather reach a real person?",
         "What someone planning an escape wants most is to feel a real, welcoming spa has them scheduled, and a warm reply that captures the details beats a voicemail box every time. The AI receptionist is upfront that it is an assistant, answers package and gift card questions, and books the room."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail while you are with a guest, turning over a room, or closed for the night, which is when many of your best calls come in. Something that always answers and books is what catches them.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Don't My Spa Guests Rebook? (problem -> crm) ============
{
    "slug": "why-spa-guests-dont-rebook",
    "h1": "Why Don't My Spa Guests Rebook?",
    "title": "Why Don't My Spa Guests Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most spa guests do not rebook because no reminder came, not because they were unhappy. They float out unwound, life gets busy, and the next visit never gets booked.",
    "answer": "Most spa guests do not rebook because no reminder ever came, not because they were unhappy. A guest floats out of the relaxation lounge blissed out and not thinking about the calendar, life gets busy, and months slip past. The visit was always going to repeat, it just needed a warm, well-timed nudge.",
    "sections": [
        {"h2_html": "A quiet guest is usually forgotten, not <em>unhappy</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a guest who did not come back as one who was unhappy, so you move on. But most of the time they left thrilled and fully meant to return. The trouble is the moment they leave: a guest floats out of the relaxation lounge unwound, calm, and not thinking about calendars at all, which is the whole point of the visit and also exactly why the next appointment does not get booked at the desk. Then life gets busy, no reminder ever comes, and the spa day they meant to plan slides down a list of a hundred other things. Relaxation runs on a rhythm, a massage or facial every few weeks, a regular escape from a hard schedule, but nothing forces the guest to notice they are due the way a hard deadline would.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">They do not feel it as a decision to leave you. They just quietly come due, forget, and eventually try whatever spa is nearest when the thought finally returns. The spa they rebook with is usually not the one with the best treatment. It is the one that reached them at the right moment with a warm note that they are due to unwind again.</p>'''},
        {"h2_html": "Why the rebooking never happens on a <em>busy day</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Day spas do not skip the follow-up because they are careless. They skip it because the day fills up. The front desk is checking guests in, turning over rooms, walking people to the lounge, and answering the phone, and no one can also hold the visit rhythm of a few thousand guests in their head. Booking the next visit while a guest is drifting out the door unwound feels pushy, so it does not happen, and doing it later by memory only happens when things are slow, which is exactly when you have the fewest guests coming due.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system watching who is overdue on their cadence, so the reminder never goes out.</li><li>Gift card visitors who came in once, and package guests with visits left, quietly get forgotten.</li><li>Members stop coming, keep paying for a while, then cancel, and nobody noticed in time to bring them back.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and then it just runs. When every guest hears from you on the rhythm they keep, in your spa's own warm voice, the ones coming due keep rebooking and the repeat visits you already earned stop drifting to the spa down the road.</p>'''}],
    "bridge_h2": "Bring every guest back on their rhythm",
    "bridge_text": "A CRM holds every guest and their history and sends the rebooking nudge for you, timed to the rhythm each one keeps, so the monthly regular, the gift card visitor, and the member who drifted all come back to unwind with you instead of slipping away.",
    "bridge_slug": "crm-for-day-spas",
    "bridge_label": "CRM for day spas",
    "faqs": [
        ("How soon should I remind a spa guest to rebook?",
         "On the rhythm they actually keep: a monthly massage or facial guest as they come due, a package guest before too long a gap, a member before they start wondering what they are paying for. The key is that the reminder happens at all and on time, which is what a CRM handles for you."),
        ("Does an automated rebooking reminder feel impersonal?",
         "Not when it is written to sound like your spa and sent at a sensible moment. A short, warm note that they are due to unwind again reads as attentive, not pushy, and most guests welcome it because they meant to rebook and forgot. You can always step in and message anyone yourself.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ How Do Day Spas Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-day-spas-get-more-clients",
    "h1": "How Do Day Spas Get More Clients?",
    "title": "How Do Day Spas Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Day spas get more clients by showing up for a day spa near me in the map pack and reviews, making it one tap to book or gift a spa day, and rebooking current guests.",
    "answer": "Day spas get more clients by showing up where people planning a spa day or shopping for a gift actually look, the Google map pack and recent reviews, then making it effortless to book a visit or buy a gift card online. New guests matter, but the fastest growth pairs that with rebooking the guests you already have.",
    "sections": [
        {"h2_html": "Show up where people planning a spa day are <em>looking</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more day spa guests is less about one clever tactic and more about being visible and trusted in the few places people actually decide. When someone searches for a day spa near them, for spa packages, or for a couples massage, Google shows the map pack first, three local listings with star ratings, and most people choose from those three without scrolling. A day spa also has a rhythm most businesses do not: around Mother's Day, the holidays, and Valentine's Day, a wave of people go looking for a spa gift card or a spa day to give, and you want to be the spa they find and can buy from on the spot.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile verified, complete, and active, because the map pack is where most local spa searches begin.</li><li>Build a steady flow of genuine, recent reviews, since someone choosing where to unwind trusts other guests before they trust an ad.</li><li>Keep your listing and social presence warm and calm, showing the space and the packages, so the person planning an escape can picture it.</li><li>Make booking a visit or buying a gift card effortless from every one of those places, because interest cools fast if they have to hunt for how to reach you.</li></ul>'''},
        {"h2_html": "Then grow the guests you <em>already have</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New guests are only half of it, and usually the more expensive half. The cheapest growth a day spa has is the guest list it already earned. Spa visits repeat on a relaxation rhythm and sell well as packages, memberships, and gift cards, so a spa that consistently rebooks its regulars, invites its gift card visitors back, and revives the ones who drifted grows faster than one pouring everything into new faces that come once and disappear.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">In practice that means pairing the visibility above with the follow-up behind it. Answer every call and text the moment it comes in so a booking is not lost to voicemail, remind each guest when they are due to unwind again, nudge package guests to use the visits they paid for, and give members and gift card recipients a warm reason to come back. Do the visible part to fill the top and the follow-up part to keep guests cycling, and the two compound. What no honest company can promise is a specific number of new guests, but showing up where people look and following up on the guests you already have are the levers that reliably move bookings.</p>'''}],
    "bridge_h2": "Get found, then keep them coming back",
    "bridge_text": "Most day spa growth starts in the map pack and your reviews, and around the gifting seasons when people search for a spa day to give, then compounds when you rebook the guests you already have. Marketing that does both keeps the calendar full.",
    "bridge_slug": "marketing-for-day-spas",
    "bridge_label": "Marketing for day spas",
    "faqs": [
        ("What is the fastest way for a day spa to get more clients?",
         "Usually to get visible where people already look, a complete Google Business Profile in the map pack and recent reviews, and to make booking a visit or buying a gift card one tap. Pair that with rebooking the guests you already have and the calendar fills from both directions."),
        ("Do I need paid ads to grow a day spa?",
         "Not to start. A verified, well-reviewed Google profile, a warm social presence, and consistent rebooking of your current guests move bookings without an ad budget. Paid ads can add reach on top, but they work far better once the profile, reviews, and follow-up are already in place.")],
    "trade_slug": "day_spas", "trade_plural": "day spas",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
]
