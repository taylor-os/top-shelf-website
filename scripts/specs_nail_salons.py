"""Per-page content specs for the SEO corpus, nail salons batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, nail-salon-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the hair-salon, massage, or gym content reworded.

Salon, Spa & Fitness hub, shared with specs_hair_salons.py, specs_massage_therapy.py, and
specs_gyms.py. Four service angles live here in one file (the ai-receptionist dict carries
"demo": True). Where a hair salon rebooks a color appointment on a six-week cadence built around
the stylist relationship, a massage practice sells a therapeutic maintenance cadence, and a gym
sells a recurring membership, a nail salon runs on high appointment and walk-in volume with a
much tighter two to three week rebooking cadence (fills, manicures, pedicures), on techs who are
mid-service with a client's hands under the lamp, and on intensely visual discovery through
nail-art photos, so this file is written around capturing every booking and same-day call,
rebooking regulars on that short cadence, filling last-minute openings, loyalty and packages,
and reactivating lapsed regulars, never the six-week color rebook, therapeutic bodywork, or the
membership funnel. Each example body ends with the literal "Illustrative example, not a client."
per the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Nail Salons =========================
{
    "slug": "ai-receptionist-for-nail-salons", "demo": True,
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "AI Receptionist for Nail Salons",
    "title": "AI Receptionist for Nail Salons | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Nail Salons",
    "meta_desc": "A nail salon answering service answers every booking call the moment it comes in, day or night, books the appointment, and never sends a client to voicemail.",
    "service_schema_name": "AI Receptionist for Nail Salons",
    "eyebrow": "For Nail Salons",
    "h1_html": "AI Receptionist <em>for Nail Salons</em>",
    "answer_block": "A nail salon answering service answers every call and text the moment it comes in, day or night, sorts a client booking a full set from someone asking for an opening this afternoon, and books it onto the right tech's calendar while your hands are under the lamp. You keep your own number, and every client is yours.",
    "sections": [
        {"h2_html": "The call you miss is a booked chair that goes to <em>the salon that answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A nail tech in the middle of a set has both hands on a client, or a client sitting with her fingers under the lamp waiting on the gel to cure, and neither can stop to grab a ringing phone. A nail salon runs on a steady stream of booking calls and quick questions about openings all day long, and the busier the salon is, the more of them ring out, because every tech at the tables is already working. The person calling to book will not leave a voicemail and wait for a callback. She taps the next salon on the list, and the one after that, until someone picks up, and the appointment, along with the standing visit every couple of weeks she would have kept all year, goes to whoever answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up on the first ring, day or night, sounds friendly instead of rushed, asks what she wants done and roughly when, and either books it outright or takes the details so nothing is lost. The booking is captured and scheduled instead of handed to the salon down the block that simply got to the phone first.</p>'},
        {"h2_html": "'Do you have an opening this afternoon' is a booking, <em>not a nuisance</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A big share of nail business is not planned a week out. Someone chips a nail the morning of an event, decides on a whim to get a pedicure before a trip, or wants a fresh set before the weekend and calls around to see who can fit her in today. That same-day demand is some of the easiest money a salon can book, and it is also the most fragile, because the caller will simply keep dialing until a salon says yes. If your team is heads-down at the tables and the call rings out, she is in another salon\'s chair within the hour.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answering service answers in seconds, checks your book against what she needs and how long it takes, and either slots her into a real opening or offers the next one, so a same-day caller becomes a booked appointment instead of a walk-in for the salon that happened to pick up. It can also hold the details for a full set or nail art that needs more chair time and hand it to you to place.</p>'},
        {"h2_html": "Built around how a nail salon <em>actually books</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">No two bookings take the same chair time, and an off-the-shelf call center reading a script does not know a gel fill from a full set of acrylics, or that nail art and a spa pedicure need far more time than a quick polish change. The answering service handles it the way a sharp front desk would on a busy Saturday.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers calls and texts around the clock, so the client who finds you at midnight and the one who calls on a Sunday both reach a real reply instead of a voicemail box.</li><li>Books the right service for the right amount of chair time with the right tech, and knows a full set of acrylics or a detailed nail-art design is not a fifteen-minute appointment.</li><li>Handles a group booking, a birthday or a bridal party wanting mani-pedis together, by taking the size and the date so you can set aside the tables instead of losing it.</li><li>Treats a standing regular differently from a first-time caller, so the clients who see you every few weeks never feel like they are talking to a stranger.</li></ul>'},
        {"h2_html": "You own the number, the calls, and <em>the client list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing salon number, or a new one registered in your name, not ours. Every caller, every message, and every booking is yours and exportable any time, so the client list you are building is an asset you keep instead of something you rent back month to month, with no long contract holding your clients hostage. The answering service is one piece of the Top Shelf platform, and it hands every booking it captures to the same CRM that rebooks and follows up, so a first-time client turns into a regular who is back in your chair every couple of weeks instead of a one-time visit you never see again.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A lunchtime call for a same-day fill, booked while every <em>tech is at a table</em>",
        "body_html": "A client realizes at noon that her gel is lifting at the corners and she has a weekend away starting Friday, so she calls to see if anyone can squeeze in a fill this afternoon. Every one of your techs is mid-service with a client's hands under the lamp, and the phone would normally ring straight through to voicemail. Instead the answering service picks up in seconds, checks the book, sees a spot opened by an earlier cancellation at three, and books her in with a text confirming the time. She shows up that afternoon instead of calling the salon two doors down, and you filled a slot that would have sat empty, all without anyone stepping away from a table. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current salon phone number?",
         "Yes. It can answer on your existing salon number, or set up a new one registered in your name. Either way the number and every call, text, and booking that comes through it belong to you and go with you if you ever leave."),
        ("Can it book same-day and walk-in requests, not just appointments booked ahead?",
         "Yes, and that is where a lot of nail business lives. When someone calls wanting a fill or a pedicure this afternoon, it checks your book against what she needs and the time it takes, and either slots her into a real opening or offers the next one, so a same-day caller does not just walk into whichever salon happened to pick up."),
        ("Will it book the right service on the right tech's calendar?",
         "Yes. It books the right service for the right amount of chair time based on your calendar and rules, and it knows a full set or nail art needs more time than a polish change, and you get the details right away. For anything that needs your judgment it takes the details and hands it to you to confirm."),
        ("Will it sound like a robot to someone calling to book?",
         "It answers naturally and warmly, and it is upfront rather than pretending to be a person. A caller mostly wants to know she can get in and that a real salon has her booked, and a friendly reply that captures the details beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your services, your techs, your hours, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you how many calls and messages your current setup is missing.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for nail salons"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-nail-salons.html", "The CRM that rebooks every client you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing booked chairs to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many booking calls, texts, and same-day requests your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Nail Salons ================================
{
    "slug": "crm-for-nail-salons",
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "CRM for Nail Salons",
    "title": "CRM for Nail Salons | Top Shelf Business Solutions",
    "og_title": "CRM for Nail Salons",
    "meta_desc": "A CRM for nail salons keeps every client, service, and visit in one place and rebooks them for you, so a gel client due every few weeks keeps coming back.",
    "service_schema_name": "CRM for Nail Salons",
    "eyebrow": "For Nail Salons",
    "h1_html": "CRM <em>for Nail Salons</em>",
    "answer_block": "A CRM for nail salons keeps every client, service note, and past visit in one place and rebooks them for you, so the gel client due in two to three weeks and the regular who drifted away both come back to your chair instead of trying the salon down the block. Your client list quietly becomes recurring revenue.",
    "sections": [
        {"h2_html": "The client who does not rebook is the chair you are <em>quietly losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most nail salons the trouble is not finding new clients, it is getting the ones they already have back on the tight schedule the work runs on. A gel manicure starts lifting and growing out in about two to three weeks, a fill comes due just as fast, and a client on that rhythm is a standing appointment every couple of weeks for as long as she keeps coming. When she leaves without the next visit booked, the way most people do when the salon is busy, that chair time does not disappear, it either sits empty or someone else fills it, and the steady run of visits she represented walks out with her. Because the cadence is so short, a client who drifts for even a few weeks has already missed a visit, and it is easy for her to settle into a new habit at whatever salon is convenient.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every client and her history in front of you and sends the rebooking nudge itself, by text or email, timed to when each service comes due. The gel client hears from you right as her nails are ready for a fill, books the next visit, and stays on the schedule instead of drifting off, and you never sit down to chase it.</p>'},
        {"h2_html": "Every client you have seen once is a client for <em>years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your past clients are the easiest chair to fill. They already know your work, the drive, and the price, and the next fill, pedicure, or full set is yours if you stay in touch. But no one can keep a few hundred clients straight in her head, when each is due back, which tech they like, the shape and color they always ask for, or who still has visits left on a package, so a lot of that repeat work slips to whoever they find when they finally get around to booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every client, her preferred tech, the colors and shapes she favors, any notes, and her full visit history live in one place instead of an appointment book and someone\'s memory.</li><li>Rebooking reminders go out on the short cadence nail work runs on, so fills, manicures, and pedicures come back around without anyone tracking dates.</li><li>Loyalty punch cards and prepaid packages are tracked against the right client, so the people who paid ahead or are one visit from a reward actually come in and use it.</li><li>You can see who is due, who is overdue, and reach the right client with the right reminder at the right time.</li></ul>'},
        {"h2_html": "The regulars who drifted away are a <em>goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A client you have not seen in a couple of months is usually not upset, she just got busy, traveled, or fell out of the habit, and on a two-week cadence it does not take long for a couple of missed visits to turn into months away. Reaching back out to the regulars who have gone quiet is some of the highest-return work a nail salon can do, because you are not paying to win a stranger\'s trust, you are reminding someone who already liked your work that you are still here. A lapsed client has nothing to relearn either, her preferred tech, her go-to color and shape, and her history are all still on file. A warm, well-timed message brings a real share of them back into the chair, and the CRM finds the clients who have lapsed and sends that message for you, so a name you had written off turns back into a standing appointment without anyone combing through the old book.</p>'},
        {"h2_html": "Filled cancellations, packages that get used, and a list <em>you own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Two things quietly drain a fully booked day: the no-show who forgets, and the last-minute cancellation that leaves a hole. For a nail salon that second one stings less than it does for most trades, because there is almost always someone who wanted a same-day spot, and the CRM can text the clients on a waitlist the moment a slot opens and fill it before the chair sits empty. Automatic confirmations and reminders go out ahead of every appointment, which is the most reliable way to hold no-shows down and give a client an easy way to move her time instead of just not showing. Every client and note is yours and exportable any time, never locked inside software you only rent, and because the CRM shares one database with the answering service, a booking the phone captures lands here and gets rebooked on its own. Nothing you have already earned is left to go cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A gel client who rebooks before her polish <em>grows out</em>",
        "body_html": "A client comes in for a gel manicure on a Saturday and leaves without booking her next visit, the way most people do when the salon is busy. Normally that is the last you think of it until she resurfaces weeks later, or tries somewhere new. Instead, about two weeks on, the CRM sends her a friendly reminder that she is coming due, written to sound like you, with a link to grab a time before the gel starts lifting. She books that afternoon and stays on a rhythm that keeps her in your chair all year, instead of drifting off and settling in at whatever salon is convenient when she finally notices her nails. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing clients and their history?",
         "Yes. Your current clients, their contact details, preferred tech, the colors and shapes they favor, notes, and past visits come in and live in one place, and everything stays yours and exportable. The point is to make the client list you already have actually work for you."),
        ("Will it really prompt clients to rebook on its own?",
         "Yes, on the cadence you set. Because nail work runs on a short two to three week rhythm, a gel or fill client can hear from you right as she is coming due, all sent for you, so the standing visits keep rebooking instead of depending on someone remembering at the desk. You can message anyone directly any time too."),
        ("Can it store each client's preferred tech, colors, and shapes?",
         "Yes. Each client's preferred tech, go-to colors and shapes, any allergies or sensitivities, and full history stay attached to her profile, so whoever seats her can pick up exactly where the last visit left off instead of starting from a guess."),
        ("Can it handle loyalty punch cards, packages, no-shows, and cancellations?",
         "Yes. Loyalty rewards and prepaid packages are tracked against the right client, automatic reminders cut no-shows, and when someone cancels at the last minute it can text a waitlist to fill the opening before that chair sits empty."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your clients, build your rebooking and win-back reminders, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where visits are slipping through today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for nail salons"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-nail-salons.html", "The answering service that feeds it every booking"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting regulars <em>fall off your cadence</em>",
    "cta_sub": "Get a free audit of how many of your clients are overdue to rebook or have quietly stopped coming in, whether you work with us or not. No credit card, never a call center.",
},
# ============================= Marketing for Nail Salons =============================
{
    "slug": "marketing-for-nail-salons",
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Marketing for Nail Salons",
    "title": "Marketing for Nail Salons | Top Shelf Business Solutions",
    "og_title": "Marketing for Nail Salons",
    "meta_desc": "Nail salon marketing keeps your Google profile and Instagram active and your name first in the map pack, so new clients nearby find and book you first.",
    "service_schema_name": "Marketing for Nail Salons",
    "eyebrow": "For Nail Salons",
    "h1_html": "Marketing <em>for Nail Salons</em>",
    "answer_block": "Marketing for nail salons keeps you visible where new clients actually look, your Google Business Profile, the map pack, and Instagram, so when someone nearby searches for a nail salon or scrolls past a set she loves, yours is the active, well-reviewed name she books instead of the salon that let its profile go stale.",
    "sections": [
        {"h2_html": "New clients pick a nail salon off a <em>photo</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a nail salon more than almost any business, the product is a picture. Before a new client ever calls, she has already looked you up, scrolled through photos of the sets and designs you have actually done, and decided whether your work looks like what she wants on her own hands. That judgment happens on a screen, in a minute or two, long before the phone rings, and it turns on whether your photos show clean, current work she would be proud to show off. So the whole game for a nail salon is being easy to find and obviously good in the exact places a new client looks, not clever ads aimed at people who are not thinking about their nails.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Show real, recent work and look active in that moment, and the booking is usually yours. Look neglected or show nothing, and she books the salon whose photos told her what she would be walking out with, no matter how skilled your techs actually are.</p>'},
        {"h2_html": "Your Google Business Profile is your <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone searches for a nail salon nearby, or for gel nails, dip powder, or a pedicure in your area, the map pack, those three local listings with the star ratings, is the first thing she sees, above the websites and the ads. A profile left untouched for months, with dim photos and hours that may or may not be right, looks closed next to one with recent sets, current details, and a steady stream of fresh reviews. It is also where the practical questions get settled at a glance, whether you take walk-ins, whether you do dip powder or a full set of acrylics or the nail art she has in mind, and whether the place looks clean and well kept, which matters more to a nail client than to almost anyone. Keeping that profile full, fresh, and honest is a quiet advertisement running in the one spot a new client actually decides from, and it is free space most salons let go to waste.</p>'},
        {"h2_html": "Instagram is where a design becomes a <em>booking</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a nail salon, social media is the sample book. A huge amount of new-client interest starts with someone scrolling, saving a set she loves, and tapping through to find out who did it, and plenty of clients walk in with a screenshot asking whether you can do exactly that. A feed full of real work, the seasonal designs people ask for around the holidays and summer, the range from a clean neutral to detailed art, does the selling for you while the salon is closed and gives a nervous first-timer the confidence that you can do the look she is picturing. A feed that has gone quiet for months tells her the opposite. Posting real work steadily, and making it easy to go from a saved photo to a booking, is what turns a scroll into a client in the chair, especially when the post links straight to a way to reach you.</p>'},
        {"h2_html": "Reviews and a steady local presence, <em>working together</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Recent, honest reviews are the other half of the trust a new client weighs, and they feed the same Google profile that decides whether you show up in the map pack at all. For a nail salon the reviews do particular work, because they tell the next reader how long the gel actually lasted, how careful and clean the salon is, and whether the tech nailed the design, the exact things she is nervous about. More reviews lift you in local search, which brings more clients, who leave more reviews, and it compounds. A steady presence, fresh photos of real sets, replies to the reviews that come in, posts tied to the seasons and the designs people are asking for, keeps you top of mind across the neighborhoods you serve. This is the public-facing side of the salon, aimed at people who are not clients yet; the private follow-up to the clients already in your book is the CRM. Either way the reputation stays yours, tied to your own profile, not a directory or an app that rents your own name back to you.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The design she screenshotted leads her <em>to you</em>",
        "body_html": "Someone saves a photo of a set she wants for a wedding she is in next month, then searches for a nail salon near her that can pull it off. Because your Google profile is active and full of recent work, with a wall of fresh five-star reviews, and your Instagram shows that exact style of art done well, yours is the name that feels safe for something she will be photographed with all day. She books with you and never finishes checking the others. The salon a mile away, with a profile last touched a year ago and no photos of real work, never entered the running. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile and Instagram for me?",
         "Yes. We keep both active with real photos of your work, updates, and local content on a regular schedule, and keep your hours, services, and whether you take walk-ins accurate, so you look current and busy whenever a new client looks you up."),
        ("How do I get more reviews?",
         "Reviews are part of the picture, asked for at the right moment and pointed at the Google profile that feeds your local ranking. We help you gather honest reviews from happy clients and reply to the ones that come in, since responding is itself a signal that lifts you in local search."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with clients already in your book, rebooking and win-back. Marketing is the public-facing side, your Google profile, reviews, and social, aimed at people who are not your clients yet but need to find you and trust your work before they will book."),
        ("Do I need to be on every social platform?",
         "No. For a nail salon the work is concentrated where people browse nails and pick a salon by the photos, your Google Business Profile and the visual feeds. We focus your effort there instead of spreading you thin across places that do not bring bookings."),
        ("How long before I see it working?",
         "A neglected Google profile can climb in the map pack within weeks once it is active and complete, and it compounds as reviews and photos build. Setup is included, and a free audit will show you what your online presence looks like to a new client searching near you today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for nail salons"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-nail-salons.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the nail salon they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are on Google and social in your area right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Websites & SEO for Nail Salons =========================
{
    "slug": "websites-seo-for-nail-salons",
    "trade_slug": "nail_salons", "trade_plural": "nail salons",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Websites & SEO for Nail Salons",
    "title": "Websites & SEO for Nail Salons | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Nail Salons",
    "meta_desc": "A nail salon website built for SEO doubles as a nail-art portfolio, ranks for gel manicure and pedicure near me, and lets clients book or walk in same day.",
    "service_schema_name": "Websites & SEO for Nail Salons",
    "eyebrow": "For Nail Salons",
    "h1_html": "Websites &amp; SEO <em>for Nail Salons</em>",
    "answer_block": "A nail salon website built for SEO works as a nail-art portfolio first, a fast, photo-forward gallery of your real sets that ranks for gel manicure, dip powder, and pedicure near me, surfaces your walk-in openings, and takes the booking directly, so the client and the booking are yours instead of a marketplace's cut.",
    "sections": [
        {"h2_html": "Your website is a <em>nail-art portfolio</em> first",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Ask most nail clients how they picked their salon and the honest answer is a photo. They scrolled through actual sets, ombre, French, dip powder, gel-X, chrome, seasonal art, found work that matched what they had in mind, and plenty of them screenshotted a design to bring in and ask for. So your website is not a brochure with a small gallery tucked inside, it is the gallery. Its first job is to put a deep, organized set of your real work in front of a stranger fast, so she can see whether you do the style she wants before she looks at anything else.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That means the build starts from the photos. Your sets are sorted the way a client shops, by service and by style, they load quickly on a phone instead of choking on a slow slideshow, and they are refreshed so the page shows what you are doing this season, not a set from two years ago. A salon that shows a wall of real work she can picture on her own hands wins the booking over one that offers a stock photo and a phone number.</p>'},
        {"h2_html": "Rank for gel manicure and pedicure <em>near me</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone wants her nails done, the search is specific and local: nail salon near me, gel manicure near me, dip powder nails, a pedicure, nail art near me, sometimes acrylics or a full set in a named neighborhood. The very top of that results page is often a national directory or a booking app, not the salons themselves, because those sites carry thousands of pages and years of authority. You are not going to knock a national directory off the single broadest term this year, and you do not have to. The winnable ground is your own salon name, the neighborhoods you actually draw from, and each specific service a client types when she is ready to book, terms a national app has no reason to cover well for your street. Pages built around the services you offer and the areas you serve are what earns those clicks, and the local, specific searches can start moving within weeks while the broad head term compounds over months.</p>'},
        {"h2_html": "Put walk-in and same-day openings <em>on the page</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting your nails done is far more of a spur-of-the-moment decision than a hair color appointment booked weeks out. A chipped nail before a night out, a free hour at lunch, a pedicure on the way to a trip, a lot of nail business is decided the same day, and that client is not going to fill out a contact form and wait for a callback. She wants to know one thing right now: can she come in today. A website that answers that on the spot, showing whether you take walk-ins, roughly what the wait looks like, and a tap-to-call or same-day book button that is impossible to miss, catches the client who is deciding in the moment. Bury that behind a form and she keeps scrolling to the next salon that made saying yes easy. Making today obvious, alongside the option to book ahead for a full set or a group, turns a spur-of-the-moment search into a client in your chair that afternoon.</p>'},
        {"h2_html": "Win the booking on trust, and <em>keep it yours</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">There is a specific worry a nail client carries that a hair client does not, and a smart site answers it before she has to ask. She is wondering whether the tools are clean, whether files and buffers are fresh or single-use, whether the foot baths are sanitized between clients, and whether the techs are properly licensed. Showing that plainly on the site, your license, how you handle sanitation, real photos of a clean and orderly space, quietly settles the one thing most likely to send a careful client somewhere else. It is a trust signal most trades never think about and nail salons almost always should.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And the booking that trust earns should land with you, not with a middleman. When a client books through a marketplace app, it takes a cut of a booking that could have come to you for nothing, keeps the relationship inside its own account, and stops sending anyone the day you stop paying. A site you own does the opposite: it keeps ranking, keeps showing your work, and sends the booking and the client straight into your own book, so what you build is an asset that compounds instead of rent you pay to reach your own clients.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A lunchtime 'pedicure near me' search, in your chair <em>by two</em>",
        "body_html": "On her lunch break someone decides she is finally getting the pedicure she has been putting off, and searches for one near her. She lands on your site, and instead of a slow page and a contact form, she sees a gallery of real work, a line that says walk-ins are welcome with openings this afternoon, and a button to call or book in one tap. She taps it, sees a two o'clock is open, and books it before she finishes her sandwich. She is in your chair that afternoon, a booking that would have gone to whichever salon answered the phone or turned up first, and it came straight to you with no app taking a cut. Illustrative example, not a client."},
    "faqs": [
        ("Is my website basically a photo gallery of my work?",
         "In large part, yes, and that is the point. For a nail salon the gallery is the site, so we build it photo-first: your real sets sorted by service and style, loading fast on a phone, and easy to refresh as your work changes with the seasons. A stranger deciding on a salon is buying a look, and the fastest way to earn her is to show it."),
        ("What nail searches can it rank for, and how fast?",
         "Realistically your salon name, your neighborhoods, and specific service searches like gel manicure, dip powder, pedicure, and nail art near you, not the single broadest term overnight, which a national directory tends to hold. Those local, specific terms can start moving within weeks, while the broad ones compound over months."),
        ("Can the site show walk-in availability and let someone book same-day?",
         "Yes, and for nails it should. We can surface whether you take walk-ins and show a tap-to-call or same-day book button up front, because a lot of nail visits are decided in the moment, and a client who wants to come in this afternoon will not fill out a form and wait."),
        ("Can it show that we are licensed and follow sanitation standards?",
         "Yes. We can display your license, how you handle clean and single-use tools, and real photos of the space, which answers the exact thing a careful nail client checks for before she books. It is a trust signal worth making plain, since it often decides between two salons."),
        ("How is this different from just listing on a booking app?",
         "A booking app takes a cut of a booking that could have come to you directly, keeps the client in its own system, and stops the day you stop paying. A website you own captures the booking and the client for nothing extra and keeps working long after it is built, so it becomes an asset instead of a fee on every visit.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for nail salons"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-nail-salons.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Make your work the reason she <em>books you</em>",
    "cta_sub": "Get a free audit of how your website, your photos, and your local search stack up against the salons and booking apps near you, whether you work with us or not. No credit card, never a call center.",
},
]
