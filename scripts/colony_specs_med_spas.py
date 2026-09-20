"""Colony page specs for MED SPAS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a med spa owner would search, answered directly up top (the 40-60 word
AEO answer), then two body sections, then a "the fix" bridge that funnels the page's authority
into the ONE money page the question implies. Lighter than a money page.

A MED SPA is MEDICAL AESTHETICS (Botox, filler, laser, medical facials), not a relaxation day
spa and not a general medical clinic. Every dict here owns UNIQUE, hand-written, med-spa-specific
substance (the generator owns shell, schema, events, keyword placement): aesthetic consultations,
memberships + treatment packages + gift cards as the revenue base, the rebooking cadence
(neurotoxin every few months, filler over the year, packages of sessions) as the retention engine,
deposits against no-shows, image and Instagram-driven discovery, and nervous price-shopping consult
callers.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real Top Shelf prices ($299/$899 plans, $1,500 one-time site) ever appear,
and the spa's OWN treatment, package, and membership pricing stays generic with no numbers; no
em/en dashes anywhere; never "leak" as a metaphor. ETHICS: the AI receptionist does scheduling and
intake ONLY, never medical or cosmetic advice, and nothing here promises a cosmetic result,
anti-aging outcome, or any medical result.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 med-spa-website-cost              (cost)     -> websites-seo-for-med-spas
  2 med-spa-answering-service-cost    (cost)     -> ai-receptionist-for-med-spas
  3 is-a-crm-worth-it-for-a-med-spa   (cost)     -> crm-for-med-spas
  4 why-med-spas-miss-calls           (problem)  -> ai-receptionist-for-med-spas
  5 why-med-spa-clients-dont-rebook   (problem)  -> crm-for-med-spas
  6 how-do-med-spas-get-more-clients  (how-to)   -> marketing-for-med-spas
"""

TOPICS = [
# ==================== How Much Does a Med Spa Website Cost? (cost -> websites-seo) ====================
{
    "slug": "med-spa-website-cost",
    "h1": "How Much Does a Med Spa Website Cost?",
    "title": "How Much Does a Med Spa Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A med spa website ranges from a cheap template to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A med spa website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more is whether it earns a nervous first-timer's trust and books the consult. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for a med spa website swings widely because you are not all buying the same thing. A cheap template you fill in yourself and a custom site built to earn trust and book consults are different products with the same name. Aesthetics is a look-first, trust-first business: a client is deciding whether to let you put a needle near her face, and she judges you on the photos, the polish, and how easy it is to book before she ever calls. This is medical aesthetics, not a relaxation day spa, so the site has to signal real clinical credibility, injectors, a medical director, genuine care, not just calm music and stock candles. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it rarely looks the part or ranks for the people searching for a med spa near them.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is handling the ongoing SEO that gets it found.</li><li>An agency retainer bundles the build with ongoing SEO, updates, and often the booking and follow-up, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site and the photos, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What a med spa should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A med spa website earns its money one way: it turns a nervous, comparison-shopping visitor into a booked consultation. That means it has to load fast, look as premium as the work you do, rank for the treatments and towns you serve, show your menu and credentials clearly, and put a book-now button in front of her before she scrolls away to the next spa. A beautiful site that never ranks and hides its booking link is the most expensive kind, because you paid for it and it brings you nothing. It should also do the quiet trust work aesthetics runs on: real photos, clear treatment descriptions, and the qualifications of your providers, without promising any particular result.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books consults",
    "bridge_text": "A med spa website is only worth the consults it books. Ours is built to look as premium as your work, rank for the treatments you offer, and turn a comparison-shopping visitor into a booked consultation.",
    "bridge_slug": "websites-seo-for-med-spas",
    "bridge_label": "Websites & SEO for med spas",
    "faqs": [
        ("Is a cheap template site good enough for a med spa to start with?",
         "It can get you online, but a template you fill in yourself rarely looks premium enough for aesthetics or ranks for the people searching for a med spa near them, and you do the upkeep. In a look-first, trust-first business, a site that does not earn confidence or turn visitors into consults is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it, and to your photos, if you leave, before you sign anything.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ What Does a Med Spa Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "med-spa-answering-service-cost",
    "h1": "What Does a Med Spa Answering Service Cost?",
    "title": "What Does a Med Spa Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Med spa answering services often bill per call or minute. Top Shelf includes an AI receptionist that answers and books consults 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for med spas usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and text and books the consult comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A med spa also gets much of its interest at the worst times for a live front desk: evenings and weekends, right after someone sees a before-and-after on Instagram, when after-hours minutes tend to cost the most. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty consult caller or a slow operator costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: an aesthetic client who has finally worked up the nerve to ask about Botox or filler does not leave a voicemail, she books with the spa that picked up. The real cost of no coverage is not a monthly fee, it is the first-time consult, and every treatment she would have booked for years after, that went to whoever answered. But a generic call center reading a script cannot tell a tox touch-up from a first-time filler consult, and it should never be answering clinical questions anyway, so you can pay for coverage and still get poor intake.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring by phone and text, day or night, greets a nervous first-timer warmly, captures what she is interested in, and books the consultation or holds the slot with a deposit. It is upfront that it is an assistant, it handles scheduling and intake only, and it leaves every medical and cosmetic question for your licensed provider at the consult. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One first-time consult you would have lost after hours can be worth well more than the plan across the visits that follow.</p>'}],
    "bridge_h2": "Answer every consult without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers by phone and text 24/7, books the consult or holds it with a deposit, and hands clinical questions to your provider, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-med-spas",
    "bridge_label": "AI receptionist for med spas",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours consult it books instead of losing to voicemail."),
        ("Does the AI give treatment or medical advice to callers?",
         "No, and it should not. It handles scheduling and intake only: what she is interested in, your consult types, your availability, and booking. Every medical and cosmetic question is left for your licensed provider at the consultation, where it belongs.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for a Med Spa? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-med-spa",
    "h1": "Is a CRM Worth It for a Med Spa?",
    "title": "Is a CRM Worth It for a Med Spa? | Top Shelf Business Solutions",
    "meta_desc": "For most med spas a CRM pays for itself by rebooking one tox client and reviving a lapsed one. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most med spas, yes. A CRM pays for itself the first time it rebooks a Botox client before her result fades, or brings back a member who quietly drifted off. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a med spa when you have more clients, packages, and memberships than anyone at the desk can keep track of, which is most established spas. It is not worth it if you are brand new with a handful of clients and genuinely reaching every one of them on time, though that rarely stays true as you grow. Gift cards and prepaid packages add another layer, money already collected that only becomes revenue when the client actually comes in to use it. The honest test is simple: how many tox and filler clients are past due for a touch-up right now, how many package clients still have paid sessions they have not used, and how many members have quietly stopped coming in? Those are the visits a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a med spa is not the software, it is the recurring revenue that stops slipping away. Aesthetic treatments are the most predictable repeat business there is: a tox client due every few months, a filler client due for a refresh, a package with sessions left on it, a membership about to renew. Each one is revenue you have already half-earned and are one well-timed reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It reminds each client on the cycle her treatment runs on, so a tox touch-up or the next session in a package rebooks without anyone at the desk tracking dates.</li><li>It watches memberships and packages, so you can see who still has sessions to use and who is due to renew, and reach them before the value goes unused and a member cancels.</li><li>It keeps every client, treatment history, and note in one place instead of scattered across paper charts, a booking app, and memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one lapsed client or one overdue rebooking and it has paid for itself, and the recurring visits after that are margin.</p>'}],
    "bridge_h2": "Turn your client list into recurring revenue",
    "bridge_text": "The clients you already have are the cheapest bookings a med spa can get. A CRM reminds each one when she is due and revives the ones who drifted, so they rebook with you instead of the spa that ran this week's promo.",
    "bridge_slug": "crm-for-med-spas",
    "bridge_label": "CRM for med spas",
    "faqs": [
        ("Is a CRM overkill for a small med spa?",
         "Not usually. Even a single-room spa serves more clients on repeating treatment cycles than anyone can track by memory. The point is not size, it is whether rebooking is falling through. If tox clients drift past due and package sessions go unused, a CRM earns its keep."),
        ("How is a CRM different from the booking tool I already use?",
         "A booking calendar records appointments. It does not watch treatment cycles, nudge a client who is coming due, flag a package going unused, or revive someone you have not seen in a year. A CRM does all of that on a schedule, so the repeat revenue shows up instead of depending on memory.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Med Spas Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-med-spas-miss-calls",
    "h1": "Why Do Med Spas Miss So Many Calls?",
    "title": "Why Do Med Spas Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Med spas miss calls because the front desk is with clients and the injector is mid-treatment. A first-timer who reaches voicemail books with the spa that answered.",
    "answer": "Med spas miss calls because they come when the front desk is walking a client back and the injector is mid-treatment with both hands busy. A nervous first-timer who reaches voicemail does not leave one, she books with the next spa that answers. A lot of interest also arrives after hours, from Instagram, when no one is there.",
    "sections": [
        {"h2_html": "The call comes when your team <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A med spa is a hands-full, client-facing business. When the phone rings your front desk is checking someone in, walking a client back to a room, or handling a checkout, and your injector is mid-treatment with gloves on and both hands busy. None of those are moments anyone can stop and take a call. The busier the day, the more calls roll past, which means your best weeks are also the ones where the most new interest slips away. It is not a discipline problem. A small team simply cannot treat the clients in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a first-time aesthetic caller it is not one. A client who finally worked up the nerve to ask about Botox or filler is nervous and comparison-shopping, and she will not leave a message and wait. She moves down the list until a real voice picks up, and by the time anyone checks the voicemail box, she is already booked somewhere else.</p>'},
        {"h2_html": "Your most valuable inquiries arrive <em>after hours</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A lot of the interest a med spa gets never arrives as a tidy call during business hours. Someone sees a before-and-after on Instagram at eleven at night and wants to book while the nerve holds. Someone fills out the form on your site over the weekend. Someone calls on a lunch break and cannot talk in an open office. Those after-hours inquiries are often your highest-intent ones, and they are exactly the ones that hit a dark front desk and a voicemail box.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can handle intake without pretending to be a clinician. A voicemail box cannot answer a nervous first-timer, and a generic call center does not know a lip flip from a filler dissolve or which consult needs your nurse. What actually works is something that answers on the first ring by phone and text, day or night, warmly captures what she is interested in, books the consultation or holds it with a deposit, and leaves every medical and cosmetic question for your provider, so the inquiry is caught instead of lost.</p>'}],
    "bridge_h2": "Stop losing consults to voicemail",
    "bridge_text": "An AI receptionist answers every call and text on the first ring, day or night, greets a nervous first-timer, books the consult or holds it with a deposit, and hands clinical questions to your provider, so the inquiry never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-med-spas",
    "bridge_label": "AI receptionist for med spas",
    "faqs": [
        ("Would a client rather reach a real person?",
         "What a nervous first-timer needs most is to feel a real, professional spa has her, and a warm reply that answers her scheduling questions beats a voicemail box every time. The AI receptionist is upfront that it is an assistant, captures her details, books the consult, and leaves clinical questions to your provider."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are mid-treatment, checking a client in, or closed for the night, which is when many of your best inquiries come in. Something that always answers and books is what catches the calls a forward would still miss.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Don't My Med Spa Clients Rebook? (problem -> crm) ============
{
    "slug": "why-med-spa-clients-dont-rebook",
    "h1": "Why Don't My Med Spa Clients Rebook?",
    "title": "Why Don't My Med Spa Clients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most med spa clients do not rebook because no reminder came, not because they were unhappy. Botox fades and packages sit unused, so they drift to the next promo.",
    "answer": "Most med spa clients do not rebook because no reminder ever came, not because they were unhappy. A client walks out thrilled, life gets busy, her Botox quietly fades, and she resurfaces months later at whatever spa ran a promo that week. The treatment was always going to repeat, it just needed a well-timed nudge.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>unhappy</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a client who did not come back as one who was unhappy, so you move on. But most of the time she was thrilled walking out and fully meant to return. Then life got busy, no reminder ever came, and the visit she meant to book slid down a list of a hundred other things. Aesthetic results fade on a schedule: neurotoxin softens in a few months, filler relaxes over the year, a laser or body package needs its next session on time to do its job. She does not feel any of that as a decision to leave you, she just quietly comes due and forgets.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The spa she rebooks with is usually not the one with the best work. It is the one that reached her at the right moment, a friendly note that she is coming due, a reminder that her package still has sessions on it. That well-timed touch is what turns a fading result into a booked visit, and it is exactly the thing a full front desk never gets around to between clients.</p>'},
        {"h2_html": "Why the rebooking <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Med spas do not skip the follow-up because they are careless. They skip it because the day fills up. The team is treating clients, checking people in, and answering the phone, and no one can also hold the treatment cycles of a few thousand clients in their head. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest clients coming due.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system watching who is past due for a tox touch-up or a filler refresh, so the reminder never goes out.</li><li>Package clients forget they have paid sessions left, and no one flags the ones going unused before they lapse.</li><li>Members quietly stop coming in, keep paying for a while, and then cancel, and nobody noticed in time to win them back.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and it just runs. When every client is reminded on the cycle her treatment actually runs on, written to sound like your spa, the ones coming due keep hearing from you at the right moment, and the recurring revenue you already earned stops drifting to the spa that ran the latest ad.</p>'}],
    "bridge_h2": "Bring every client back on cycle",
    "bridge_text": "A CRM watches every client's treatment cycle and sends the reminder for you, so a tox client coming due, a package with sessions left, and a lapsed member all rebook with you instead of drifting to the next promo.",
    "bridge_slug": "crm-for-med-spas",
    "bridge_label": "CRM for med spas",
    "faqs": [
        ("How soon should I remind a client to rebook?",
         "On the cycle her treatment actually runs on: a tox touch-up as she comes due, a package session before too long a gap, a member before her benefits reset. The key is that the reminder happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your spa and sent at a sensible moment. A short, warm note that she is coming due reads as attentive, not spammy, and most clients appreciate the nudge because they meant to rebook and forgot. You can always step in and message anyone yourself.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ How Do Med Spas Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-med-spas-get-more-clients",
    "h1": "How Do Med Spas Get More Clients?",
    "title": "How Do Med Spas Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Med spas get more clients by showing up in the map pack, in Google reviews, and on Instagram, then making it one tap to book a consult, and rebooking current clients.",
    "answer": "Med spas get more clients by showing up where aesthetic clients actually look, the Google map pack, recent reviews, and Instagram, and then making it effortless to book a consultation. New clients matter, but the fastest growth usually pairs that with rebooking the clients and packages you already have.",
    "sections": [
        {"h2_html": "Show up where aesthetic clients are <em>looking</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more med spa clients is less about one clever tactic and more about being visible and trustworthy in the few places people actually decide. When someone searches for a med spa near them, Google shows the map pack first, three local listings with star ratings, and most people choose from those three without scrolling. Aesthetics is also uniquely visual and social: a large share of discovery happens on Instagram, where before-and-afters and real client photos do the kind of convincing a text ad never could.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile verified, complete, and active, because the map pack is where most local searches for a med spa begin.</li><li>Build a steady flow of genuine, recent reviews, since a nervous first-timer trusts other clients before she trusts your ad.</li><li>Stay visible on Instagram, where aesthetic discovery really happens, so the late-night scroller finds you and can book in a tap.</li><li>Make booking a consultation effortless from every one of those places, because interest cools fast if she has to hunt for how to reach you.</li></ul>'},
        {"h2_html": "Then grow the clients you <em>already have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">New clients are only half of it, and usually the more expensive half. The cheapest growth a med spa has is the client list it already earned. Aesthetic treatments repeat on a schedule and sell well as packages, memberships, and gift cards, so a spa that consistently rebooks its existing clients and revives the lapsed ones grows faster than one pouring everything into new faces that book once and disappear.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">In practice that means pairing the visibility above with the follow-up behind it. Answer every inquiry the moment it comes in so interest is not lost to voicemail, remind each client when she is coming due, nudge package clients to use the sessions they paid for, and give members and gift-card buyers a reason to come back. Do the visible part to fill the top and the follow-up part to keep clients cycling, and the two compound. What no honest company can promise is a specific number of new clients or any particular result from a treatment, but showing up where clients look and following up on the ones you have are the levers that reliably move bookings.</p>'}],
    "bridge_h2": "Get found, then keep them coming back",
    "bridge_text": "Most med spa growth starts in the map pack, in your reviews, and on Instagram, then compounds when you rebook the clients you already have. Marketing that does both is how a med spa fills the calendar and keeps it full.",
    "bridge_slug": "marketing-for-med-spas",
    "bridge_label": "Marketing for med spas",
    "faqs": [
        ("What is the fastest way for a med spa to get more clients?",
         "Usually to get visible where people already look, a complete Google Business Profile in the map pack, recent reviews, and an active Instagram, and to make booking a consult one tap. Pair that with rebooking your existing clients and the calendar fills from both directions."),
        ("Do I need paid ads to grow a med spa?",
         "Not to start. A verified, well-reviewed Google profile, a steady social presence, and consistent rebooking of your current clients move bookings without an ad budget. Paid ads can add reach on top, but they work far better once the profile, reviews, and follow-up are already in place.")],
    "trade_slug": "med_spas", "trade_plural": "med spas",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
