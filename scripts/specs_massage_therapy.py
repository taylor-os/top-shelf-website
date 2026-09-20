"""Per-page content specs for the SEO corpus, massage therapists batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, massage-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the hair-salon or gym content reworded.

Salon, Spa & Fitness hub, shared with specs_hair_salons.py and specs_gyms.py. Four service
angles live here in one file (the ai-receptionist dict carries "demo": True). Where a hair
salon rebooks a per-visit color appointment and a gym sells a recurring membership, a massage
practice sells a standing maintenance cadence, prepaid packages, and gift certificates, and it
runs solo far more often, so this file is written around a therapist who cannot answer
mid-session, monthly rebooking, filling canceled table time, reactivating lapsed clients, and
the seasonal gifting waves, never per-visit color rebooking or the membership funnel. This is
legitimate therapeutic massage; the copy stays professional and makes no medical-cure or
wellness-outcome claims. Each example body ends with the literal "Illustrative example, not a
client." per the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ====================== AI Receptionist for Massage Therapists ======================
{
    "slug": "ai-receptionist-for-massage-therapists", "demo": True,
    "trade_slug": "massage_therapists", "trade_plural": "massage therapists",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "AI Receptionist for Massage Therapists",
    "title": "AI Receptionist for Massage Therapists | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Massage Therapists",
    "meta_desc": "A massage therapy answering service picks up every call and text the second it lands, books the session while you are on the table, and never uses voicemail.",
    "service_schema_name": "AI Receptionist for Massage Therapists",
    "eyebrow": "For Massage Therapists",
    "h1_html": "AI Receptionist <em>for Massage Therapists</em>",
    "answer_block": "A massage therapy answering service picks up every call and text the second it lands, sorts a new client booking their first session from someone with a quick question, and puts the appointment on the right therapist's calendar while you are working in a quiet room. The number stays yours, and so does every client it books.",
    "sections": [
        {"h2_html": "The call you miss is the client who <em>books the practice that answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When you are in a session your hands are on a client, the room is quiet and dim, and a full massage runs sixty or ninety minutes with no natural break to step out and grab a ringing phone. Plenty of massage therapists work solo, with no front desk and no one else to pick up, so a call that comes in while you are on the table simply is not answered by anyone. A new client trying to book their first massage will not leave a message and sit waiting for a callback the way they might for a doctor. They hang up and try the next practice, and the one after that, until a person or an online booking replies. The work on the table is the very reason the phone rings out, and that new client, along with every monthly visit they might have booked all year, goes to whoever answered first.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up the moment the call comes in, sounds calm and professional instead of rushed, asks what kind of session the caller is after and roughly when they want it, and either books it outright or captures the details so the lead survives. That new client ends up scheduled with you rather than passed to the practice down the street that simply happened to be free when the phone rang, and you never had to break the session you were already being paid to give.</p>'},
        {"h2_html": "Most new clients reach out at night, or while you are <em>on the table</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A large share of massage bookings never start during your working hours at all. Someone finishes a long week with a stiff neck and decides at ten at night that they want a deep tissue session, a partner goes looking for a gift certificate once the house is quiet, or a first-timer finally works up the nerve to book and sends a text on a Sunday afternoon. Interest like that has a short shelf life. If the message sits unanswered until you finish your last client tomorrow, the moment has cooled and they have already booked somewhere that replied while they were still deciding.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answering service replies in seconds to a text or a message, not only a phone call, and turns that late-night intention into a booked session while the person is still ready to act on it. The one who reached out at ten at night wakes up already on your schedule, with the session length and the details sitting in their texts, instead of still scrolling for someone who picks up. For a practice that runs on one set of hands, that reply going out the moment the interest is hot is the whole difference between a booked hour and a client who never comes back.</p>'},
        {"h2_html": "Built around how a massage practice <em>actually books</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">No two bookings are quite the same, and an off-the-shelf call center working from a script cannot tell a sixty-minute session from a ninety, deep tissue from prenatal, or that a first-time client needs an intake and a bit more time than a standing regular. The answering service handles the conversation the way an attentive front desk would on a calm afternoon.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Picks up calls and texts at any hour, so a midnight inquiry and a quiet-Sunday caller both get a real answer rather than a voicemail beep and a callback that comes too late.</li><li>Books the right session with the right therapist for the right length of time, and answers the questions that decide it: what a session runs, how long it takes, and which modalities you offer.</li><li>Takes gift certificate and package questions and either passes you the details or captures the buyer, so a seasonal gift does not slip to a practice that was easier to reach.</li><li>Treats a standing monthly client differently from a first-time caller, so the people who already trust you with their care never feel like they are explaining themselves to a stranger.</li></ul>'},
        {"h2_html": "You own the number, the calls, and <em>the client list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It answers on the number you already use, or a fresh one put in your name, never a line we own. Every caller, every text, and every booking it takes stays exportable whenever you want it, because the client list a massage practice slowly builds is the most valuable thing it owns, and it should never be locked behind a contract or rented back to you a month at a time. And it does not work off on its own. It is one piece of the Top Shelf platform, so each booking it takes drops into the CRM that rebooks and follows up, which is how a first visit becomes a standing monthly appointment rather than a name you never see twice. There is nothing for you to run and nothing to answer; it works quietly in the background while you stay focused on the client on the table in front of you.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A 10pm deep tissue booking, captured while your <em>hands are full</em>",
        "body_html": "A new client three neighborhoods over has had a knot in their shoulder all week and, at ten at night, finds your profile and sends a message asking whether you have anything that weekend. You left the studio hours ago, or you are still finishing a late session with the phone silenced, but the answering service answers within seconds, learns what they are after, checks the calendar, and books a ninety-minute deep tissue session for Saturday morning with the details confirmed in their texts. They wake up on your schedule instead of scrolling to the next practice because nobody replied, and you gained a client and their standing monthly visits while your hands were full. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current practice phone number?",
         "Yes. It can answer on your existing number, or set up a new one registered in your name. Either way the number and every call, text, and booking that comes through it belong to you and go with you if you ever leave."),
        ("Can it answer texts, not just calls?",
         "Yes, and that matters for a solo practice. A lot of clients reach out by text after hours, while you are mid-session, or after seeing your work at night, and the answering service replies to those instantly, answers the first question, and books the session, so a late message does not sit until you finish for the day."),
        ("Will it book the right kind of session on the right therapist's calendar?",
         "Yes. It books the right session length with the right therapist based on your calendar and rules, whether that is a sixty-minute Swedish or a ninety-minute deep tissue, and you get the details right away. For anything that needs your judgment, a complex intake or a special request, it takes the details and hands it to you to confirm."),
        ("Will it sound like a robot to someone booking something this personal?",
         "It answers naturally and calmly, and it is upfront rather than pretending to be a person. Someone booking bodywork mostly wants to know they can get in and that a real practice has them scheduled, and a warm reply that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your session lengths, your hours, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you how many calls and messages your current setup is missing.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for massage therapists"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-massage-therapists.html", "The CRM that rebooks every client you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending new clients to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls, texts, and after-hours messages your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ============================ CRM for Massage Therapists ============================
{
    "slug": "crm-for-massage-therapists",
    "trade_slug": "massage_therapists", "trade_plural": "massage therapists",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "CRM for Massage Therapists",
    "title": "CRM for Massage Therapists | Top Shelf Business Solutions",
    "og_title": "CRM for Massage Therapists",
    "meta_desc": "A CRM for massage therapists keeps every client, note, and package in one place and rebooks them for you, so a monthly massage client keeps coming back.",
    "service_schema_name": "CRM for Massage Therapists",
    "eyebrow": "For Massage Therapists",
    "h1_html": "CRM <em>for Massage Therapists</em>",
    "answer_block": "A CRM for massage therapists keeps every client, session note, and prepaid package together and does the rebooking for you, so the one due for a monthly massage and the regular who slipped away months ago both return to your table instead of trying the practice down the street. Your book of regulars quietly turns into revenue that repeats.",
    "sections": [
        {"h2_html": "The client who does not rebook is the revenue you are <em>quietly losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most massage practices the trouble is not finding new clients, it is getting the ones they already have back onto the table. A client who comes in for regular maintenance is not a one-time sale, they are a standing appointment every month or so for as long as they keep coming, and the same is true of the client working through a run of sessions. When they leave without the next visit booked, the way most people do when the week ahead feels full, that hour on your table does not vanish, it either sits empty or gets filled by someone else, and the recurring revenue that client represented quietly walks out with them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM holds every client and their history where you can see it and sends the rebooking nudge itself, by text or email, timed to the rhythm each client tends to keep. The regular who likes a monthly session hears from you right around the time they are due, books the next one, and stays on your table instead of drifting off and, months later, booking wherever they happen to land. You never sit down to chase it, and the standing appointment keeps standing. A massage practice lives on that monthly rhythm more than on any single booking, because one client who stays on a standing cadence is worth many who each come once and vanish, and the rhythm only holds if someone reaches out before the habit fades.</p>'},
        {"h2_html": "Every client you have seen once is a client for <em>years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your past clients are the easiest hour on your table to fill. They already trust you with something as personal as bodywork, they know the space and the price, and the next session is yours if you stay in touch. But no one can keep a few hundred clients straight in their head, when each is due back, who likes firm pressure and who likes light, which areas one wants worked and another wants left alone, or who still has sessions left on a package, so much of that repeat work drifts to whoever they happen to find once they finally get around to booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every client, their intake, pressure and focus preferences, preferred therapist, and complete visit history sit in one record instead of scattered across a paper file, a notes app, and your memory.</li><li>Rebooking nudges fire on whatever cadence each client keeps, so the monthly regulars come back around without you tracking a single date.</li><li>Prepaid packages, memberships, and gift certificates stay tracked against the right client, so the sessions people already paid for actually get used before they are forgotten.</li><li>At a glance you can tell who is coming due, who is already past it, and send each of them the right reminder at the right moment.</li></ul>'},
        {"h2_html": "The clients who drifted away are a <em>goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A client you have not seen in six months is usually not unhappy, they just got busy, lost the habit, or never got a reason to book again. Circling back to the clients who went quiet is about the highest-return hour a massage practice can spend, because there is no stranger\'s trust to buy here, only a gentle reminder to someone who already knew your hands and your room that the door is still open. A warm, well-timed message brings a real share of them back onto the table, and a lapsed client has nothing to relearn, their intake, their preferences, and their comfort with you are all still on file. The CRM surfaces the clients who have lapsed and sends that note on its own, so someone you had quietly given up on lands back on the schedule, and you never had to comb through old files to find them. The timing matters too, and the software can pace a nudge to the season or to how long it has been since their last visit, so the message lands as a welcome reminder rather than a cold pitch.</p>'},
        {"h2_html": "Fewer empty slots, filled cancellations, and a list <em>you own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Even a booked-solid week loses time two ways: the client who forgets and never shows, and the late cancellation that leaves an hour of table time with no one to fill it. That empty hour is gone for good, unlike a retail sale you can still make tomorrow, which makes it some of the most expensive time in the practice. Automatic confirmations and reminders go out ahead of every session, which is the most reliable way to hold down no-shows and give a client a simple way to move their time rather than just vanishing from the calendar. And when a late cancellation does open a hole, it can quietly offer that hour to the clients who asked for something sooner, filling it before the time is gone. Everything, every client and every note, stays yours to export whenever you like, never trapped in software you only rent, and because the CRM runs on the same database as the answering service, a booking the phone takes shows up here and gets worked without anyone re-entering it. Nothing you have already earned is left to go cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A monthly client who rebooks before they <em>drift</em>",
        "body_html": "A client comes in for a session on a Saturday and leaves without booking the next one, the way most people do when the week ahead feels full. Ordinarily you would forget it entirely, until they turned up again half a year on, or never did. Instead, a few weeks on, the CRM sends a friendly reminder that they are about due for their monthly session, worded in your own voice, with a one-tap link to pick a time. They book that afternoon and stay on a rhythm that keeps them on your table all year, instead of falling out of the habit and starting over somewhere else. You never lifted a finger to bring them back. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing clients and their history?",
         "Yes. Your current clients, their contact details, intake, preferences, notes, and past visits come in and live in one place, and everything stays yours and exportable. The point is to make the client list you already have actually work for you."),
        ("Will it really prompt clients to rebook on its own?",
         "Yes, on the cadence you set. A monthly regular can hear from you around the time they are due, another client on their own rhythm, all sent for you, so the standing appointments keep rebooking instead of depending on someone remembering at the end of a session. You can message anyone directly any time too."),
        ("Can it store client preferences and intake notes?",
         "Yes. Each client's pressure preference, the areas they want worked or left alone, their preferred therapist, any notes they share, and their history stay attached to their profile, so whoever is on the table can pick up exactly where the last session left off instead of starting from a guess."),
        ("Can it track packages, memberships, and gift certificates?",
         "Yes. Prepaid packages, memberships, and gift certificates are tracked against the right client, so you can see who has sessions left to use and gently remind them, and the money people paid ahead actually turns into booked time instead of being forgotten."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your clients, build your rebooking and win-back reminders, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where visits are slipping through today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for massage therapists"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-massage-therapists.html", "The answering service that feeds it every booking"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting regulars <em>drift away</em>",
    "cta_sub": "Get a free audit of how many of your clients are overdue to rebook or have quietly stopped coming in, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Marketing for Massage Therapists =========================
{
    "slug": "marketing-for-massage-therapists",
    "trade_slug": "massage_therapists", "trade_plural": "massage therapists",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Marketing for Massage Therapists",
    "title": "Marketing for Massage Therapists | Top Shelf Business Solutions",
    "og_title": "Marketing for Massage Therapists",
    "meta_desc": "Massage therapy marketing keeps your Google Business Profile active and your name first in the map pack, so clients nearby find and book you first.",
    "service_schema_name": "Marketing for Massage Therapists",
    "eyebrow": "For Massage Therapists",
    "h1_html": "Marketing <em>for Massage Therapists</em>",
    "answer_block": "Marketing for massage therapists puts you in front of new clients where they actually search, on your Google Business Profile and in the map pack, so when someone nearby wants a massage or a gift certificate, yours is the current, well-reviewed name they book rather than the practice whose profile has gone stale.",
    "sections": [
        {"h2_html": "People choose a massage therapist on <em>trust</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Bodywork is about as personal as a service gets. A new client is going to lie on a table and let a stranger\'s hands work on them for an hour, so before they ever book, they look you up, study your space, read a handful of reviews, and decide whether they feel comfortable with you. All of that plays out on a screen, inside a minute or two, well before anyone dials your number. So for a massage practice the entire task is to be easy to find, obviously current, and plainly professional right where a new client is already looking, rather than buying clever ads aimed at people who have no massage on their mind. Many first-time clients are a little nervous about the whole thing, and what they are really scanning for online is a signal that you are a licensed, careful professional and that the visit will be comfortable and private.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get found, look active, and show a calm, professional space in that moment, and the booking is usually yours. Look neglected or invisible, and they book the practice that showed up looking legitimate and cared-for, no matter how skilled you actually are on the table.</p>'},
        {"h2_html": "Your Google Business Profile is your <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a massage nearby, or for deep tissue, prenatal work, or a sports massage in your town, and the map pack, that trio of local listings carrying the star ratings, sits at the very top, ahead of the websites and even the ads. A listing left alone for months, with a dim photo and hours that may or may not still be right, reads as a practice that might not even be open. One with a calm, real photo of the room, current hours, the modalities you offer, and a steady stream of fresh reviews reads as a professional a person can trust with something this personal. A profile kept full, fresh, and honest is a small advertisement that runs day and night in the one place a new client actually decides from, and it costs nothing, which is exactly why it is a shame so many practices leave it to gather dust. It is also where the practical questions get settled at a glance, whether you are licensed, what a session costs, which modalities you actually offer, and whether the space looks like somewhere a person would feel at ease, so the practice that answers those on the spot wins the client who would have quietly moved on from one that made them dig or call to find out.</p>'},
        {"h2_html": "Gift certificates and gifting seasons are <em>real revenue</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A massage is one of the most given gifts there is, and that makes the calendar matter in a way it does not for most trades. The run-up to the holidays, Valentine\'s Day, Mother\'s Day, and Father\'s Day each send a wave of people looking to buy a gift certificate or book a couples session, and many of them are not your clients yet and have no particular practice in mind. The one that is easy to find, clearly sells gift certificates, and looks trustworthy at a glance catches that buyer, and a gift certificate often turns into a first visit, and a first visit into a regular. Being visible and ready right before each of those waves, rather than scrambling once they arrive, is some of the cheapest new-client work a practice can do. It is a distinct kind of demand from the client booking their own maintenance session, and it is easy to leave on the table if nobody is minding it.</p>'},
        {"h2_html": "Reviews and a steady local presence, <em>working together</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Fresh, honest reviews carry the rest of the trust a new client is weighing, and they pour back into the same Google profile that decides whether you appear in the map pack in the first place. Each new review nudges you up in local search, that visibility brings more clients, those clients leave more reviews, and the loop keeps feeding itself. A steady presence, fresh photos of the space, replies to the reviews that come in, posts tied to the seasons and the sessions people are asking about, keeps you front of mind across the neighborhoods you actually cover. All of this is the outward-facing half of the practice, meant for people who have not booked with you yet; the quiet, one-to-one follow-up with the clients already on your table belongs to the CRM, and the two are built to work as a pair. Either way the reputation stays yours, tied to your own profile, not a booking directory that quietly rents your own name back to you. Kept up consistently, that presence does the quiet reassuring for you around the clock, so a stranger who has never met you can feel like they already know the space before they ever walk in.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Mother's Day gift search finds <em>you</em>",
        "body_html": "A week before Mother's Day, someone remembers they still need a gift and searches for a massage gift certificate near them on their phone. Because your Google profile is active, with a calm photo of the room, the modalities you offer, and a wall of recent reviews, and because it clearly shows you sell gift certificates, yours is the name that feels like a safe choice. They buy the certificate that night, and a few weeks later it turns into a first session, and that first session into someone who books a standing monthly appointment. The practice a mile over, with a profile last touched a year ago, never entered the running, and it spent that gifting season wondering where the walk-ins went. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         "Yes. We keep it active with real photos of your space, updates, and local content on a regular schedule, and keep your hours, services, and modalities accurate, so you look current and professional whenever a new client looks you up."),
        ("How do I get more reviews?",
         "Reviews are part of the picture, asked for at the right moment and pointed at the Google profile that feeds your local ranking. We help you gather honest reviews from happy clients and reply to the ones that come in, since responding is itself a signal that lifts you in local search."),
        ("Can you help me get ahead of the gifting seasons?",
         "Yes. We time your visibility to the waves that matter, the holidays, Valentine's Day, Mother's Day, and Father's Day, so you are in front of gift buyers and couples before the rush instead of scrambling to get noticed the same week as everyone else."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with clients already on your table, rebooking and win-back. Marketing is the public-facing side, your Google profile, reviews, and local presence, aimed at people who are not your clients yet but need to find you and trust you before they will book something this personal."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds as reviews and photos build. Setup is included, and a free audit will show you what your online presence looks like to a new client searching near you today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for massage therapists"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-massage-therapists.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the practice they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are on Google in your area right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Websites & SEO for Massage Therapists =======================
{
    "slug": "websites-seo-for-massage-therapists",
    "trade_slug": "massage_therapists", "trade_plural": "massage therapists",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Websites & SEO for Massage Therapists",
    "title": "Websites & SEO for Massage Therapists | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Massage Therapists",
    "meta_desc": "A massage therapy website built for SEO ranks for deep tissue and massage-near-me searches, shows your modalities, and lets a client book in one tap.",
    "service_schema_name": "Websites & SEO for Massage Therapists",
    "eyebrow": "For Massage Therapists",
    "h1_html": "Websites &amp; SEO <em>for Massage Therapists</em>",
    "answer_block": "A massage therapy website built for SEO shows up for what a client actually types, massage near me, deep tissue, prenatal or sports massage in your area, leads with your modalities and calm space, and takes the booking in a single tap, so the client is yours rather than a booking app's cut of your own sessions.",
    "sections": [
        {"h2_html": "A new client trusts your website before they trust <em>your hands</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Massage is personal and takes a real measure of trust, so a new client does their homework before they book, and your website is where that trust gets won or lost. They land on it from a search or a link in your profile, and within seconds they are judging whether your space looks calm and professional, whether you offer the kind of session they want, and whether booking is going to be easy. A site that loads slowly, hides the modalities, or forces them to call during working hours, when you are on the table and cannot pick up, is a site they quietly leave for the next practice, no matter how good you are at the work itself.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It has to open fast on a phone, show your real space and the sessions you offer, put your reviews where they can see them, and make booking effortless. A genuinely skilled therapist whose website is an afterthought loses clients they never even hear about, and loses them to practices that are not necessarily better, only easier to say yes to.</p>'},
        {"h2_html": "Rank for what someone types when they <em>need a massage</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The results at the top for massage near me in your town are often a booking marketplace or a directory, not the local practices themselves. They run thousands of pages on top of years of built-up authority, so a searching client lands on them first, and from there the booking either gets passed around among practices or skims a cut off a client who could have come straight to you at no cost. Beating a national directory on the single broadest term is not happening this year, and it does not have to. You can win the searches those big directories have no reason to cover well: your own name, the neighborhoods you serve, and the specific things people look for, deep tissue massage in your city, prenatal massage, sports massage, couples massage, a massage gift certificate near me. Pages built around the modalities and the areas you actually serve are what search engines, and clients ready to book, reward with the click, because a national app has no reason to write a real page about your neighborhood or the specific work you do. The same holds for the searches tied to gifting, a massage gift certificate or a couples massage near me, which climb around the holidays and are exactly the kind of specific, local, high-intent term a local practice can own.</p>'},
        {"h2_html": "A visitor on their phone should book in <em>one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A new client is almost always on their phone, often at night just after deciding they need a session, and they have no patience for long paragraphs or for hunting down a phone number, especially when calling only reaches a voicemail because you are with a client. The site has to load fast, describe your modalities in plain language so someone can tell whether they want deep tissue, prenatal, sports, or a simple relaxation session, put your reviews where they cannot be missed, and give a book button that works in one tap and respects your real availability, day or night. Clear session names and lengths matter more here than in most trades, because a client picking bodywork wants to know exactly what they are booking before they lie down. A calm, simple site that makes booking easy is what turns a nervous first-timer into a scheduled session; a pretty site that buries the booking is a wasted opportunity, and a visitor should never leave without an easy way onto your table. Letting a client fill out the intake online before they arrive is one more piece of that ease, because it turns a first visit into a calm, prepared session instead of a clipboard and a rushed conversation at the door.</p>'},
        {"h2_html": "The bookings are <em>yours</em>, permanently",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A booking that comes through a marketplace or a pay-per-client app always skims its cut, was never fully yours in the first place, and vanishes the moment you stop paying the platform. A site you own goes on ranking, goes on showing your room and your work, and goes on taking bookings for as long as it is up, and it sits under your name, not under a platform that can rewrite its terms or cut you loose. It feeds straight into the same CRM that rebooks the clients it brings in and the answering service that fields the ones who would sooner text than tap a button, so none of what it earns you ever slips through the cracks. What you are building is an asset that gains value over time, not a rent you keep paying forever just to reach your own clients.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late-night 'deep tissue near me' search finds <em>you</em>, not an app",
        "body_html": "Someone has been putting off doing something about a tight shoulder, and at nine at night they finally search for deep tissue massage near them on their phone. Instead of a marketplace that would skim a cut and line up ten practices side by side, they find your site ranking for that search, with a calm photo of the room, a plain description of the deep tissue work you do, real reviews underneath, and one clear button to book. They see exactly the session they want, pick a time for the weekend, and book before they close the tab. The booking is yours, nobody skimmed a cut, and no app ever sat between you and your new client, and the session is on your calendar before you finish the one you are in. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and booking apps?",
         "Not for the broadest terms overnight. It can realistically rank for your practice name, your specific neighborhoods, and the modality searches a national app has no reason to target well, deep tissue, prenatal, sports, and couples massage in your area, which is exactly where a local practice can win."),
        ("How is this different from paying a booking marketplace?",
         "A marketplace shows a new client ten practices at once and takes a cut of a booking that could have been yours directly, and it stops the day you stop paying. A website you own captures bookings that are yours alone, with no cut taken, and keeps working long after it is built."),
        ("Do I need a page for every modality and neighborhood?",
         "You start with the ones that matter most: your top sessions and your core areas. We build those pages first, around what people actually search and what you most want to book, then expand, rather than spreading thin across everything at once."),
        ("Most of my clients come from word of mouth. Does a website even help?",
         "Yes, because even a referred client looks you up before they book. Word of mouth gets your name in front of them, but they check your site, your modalities, and your reviews before they trust you with something this personal, and that is where a fast, calm, easy-to-book page turns a referral into a scheduled session."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for massage therapists"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-massage-therapists.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search for <em>massage in your town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and booking apps taking your clients, whether you work with us or not. No credit card, never a call center.",
},
]
