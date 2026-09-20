"""Per-page content specs for the SEO corpus, barbershops batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, barbershop-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the hair-salon, nail-salon, or massage content reworded.

Salon, Spa & Fitness hub, shared with specs_hair_salons.py, specs_nail_salons.py, and
specs_massage_therapy.py. Four service angles live here in one file (the ai-receptionist dict
carries "demo": True). Where a hair salon rebooks a six-week color appointment built around a
stylist, a nail salon runs on same-day walk-in volume and a nail-art portfolio, and a massage
practice sells a monthly maintenance cadence and gift certificates, a barbershop runs on a much
tighter two-to-four-week cut cadence (a fade grows out fast), on live walk-in questions ("you
guys open, how long's the wait"), on booth-rent barbers who each keep their own book and their
own following so a client asks for one chair by name, and on years-long loyalty to a single
barber. So this file is written around catching the walk-in call while every barber is mid-fade,
booking a specific barber by name, rebooking regulars on the short fade cadence, holding the
standing every-other-week slot, winning back a lapsed regular, and being found by men who pick a
shop on proximity and vibe, never the six-week color rebook, the nail-art gallery, or the
gifting funnel. Each example body ends with the literal "Illustrative example, not a client."
per the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Barbershops =========================
{
    "slug": "ai-receptionist-for-barbershops", "demo": True,
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "AI Receptionist for Barbershops",
    "title": "AI Receptionist for Barbershops | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Barbershops",
    "meta_desc": "A barbershop answering service answers every call the moment it rings, tells a walk-in the wait, and books the chair with the right barber, day or night.",
    "service_schema_name": "AI Receptionist for Barbershops",
    "eyebrow": "For Barbershops",
    "h1_html": "AI Receptionist <em>for Barbershops</em>",
    "answer_block": "A barbershop answering service answers every call and text the second it comes in, tells a walk-in how long the wait is right now, and books the chair with the barber a regular asks for by name, all while your barbers are mid-fade and cannot stop to grab the phone. You keep your own number, and every client is yours.",
    "sections": [
        {"h2_html": "The call you miss is the walk-in who <em>drives to the shop that answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barber halfway through a fade has clippers in one hand and a client in the chair, and he is not going to stop a lineup to pick up a ringing phone. A barbershop lives on a steady run of calls all day, most of them one of two things: is the shop open, and how long is the wait right now. The man asking is usually already in his truck deciding where to go, and he will not leave a voicemail and sit waiting for a callback. He calls the next shop on the map, gets a live answer, and drives there instead. The busier your chairs are, the more of those calls ring out, because every barber is already cutting, and the walk-in you never heard about is sitting in someone else\'s chair twenty minutes later.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up on the first ring, tells him honestly whether you are open and roughly how long the wait is, and either points him to come in now or books him a chair so he stops shopping around. The walk-in is captured instead of handed to the shop down the street that simply got to the phone first, and no barber had to put down the clippers to make it happen.</p>'},
        {"h2_html": "'You guys open, how long's the wait, can I get in with Mike' is a <em>chair you fill or lose</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Almost every call to a barbershop is one of three questions, and all three are money. Are you open right now. How long is the wait if I come in. Can I book with a specific barber, because a lot of men will only sit in one chair. Miss those and you are not missing a nuisance, you are missing a booked chair, and often a regular who would have come back every couple of weeks for years. A generic call center reading a script cannot answer any of them, because it does not know your hours, your wait, or that half your barbers keep their own books. The answering service handles all three the way a sharp front desk would on a busy Saturday.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers calls and texts around the clock, so the man checking at nine at night whether you open tomorrow and the one calling on a Sunday both get a real answer instead of a voicemail.</li><li>Gives an honest read on the walk-in wait and tells him whether to come in now or grab a chair for later, so a ready-to-go customer does not drive past you to a shop that picked up.</li><li>Books him with the barber he asks for by name, because a man loyal to one barber will wait weeks or walk out over exactly that, and it treats a standing regular differently from a first-timer.</li><li>Takes the details for a bigger job, a cut and beard, a straight-razor shave, a group before a wedding, and hands it to you to place.</li></ul>'},
        {"h2_html": "Built around how a barbershop <em>actually runs its chairs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barbershop is rarely one shared calendar. It is often a room of chairs rented by barbers who each keep their own following, their own book, and their own hours, sitting alongside walk-in chairs anyone can take. A call that books the wrong barber, or a walk-in waved toward a chair that is booked solid, means a frustrated customer and a barber stepping away mid-cut to untangle it. The answering service is set up around how your shop is really laid out, so every call reaches the right chair without anyone at the tables breaking stride.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It knows which barbers take walk-ins and which run appointment only, how long a skin fade or a cut and beard actually takes so it never stacks a chair too tight, and who is off today. A regular who books with his barber gets his barber; a first-timer who just wants the next open chair gets pointed to the shortest wait. It runs the front of the shop the way you would if you were not already cutting.</p>'},
        {"h2_html": "You own the number, the calls, and <em>the client list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This answers on the number already painted on your window, or a new one put in your name, never a line we own. Every caller, every text, and every booking it takes stays yours and exportable any time, because the list of regulars a shop builds over years is the most valuable thing it has, and it should never be rented back to you a month at a time or held hostage in a contract. The answering service is one piece of the Top Shelf platform, so every chair it books drops into the same CRM that rebooks and follows up, which is how a first-time walk-in turns into a regular who is back every two or three weeks instead of a face you cut once and never see again.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Saturday rush, booked while every <em>barber is heads-down</em>",
        "body_html": "It is eleven on a Saturday, every chair is full, and the phone is going off the hook with men trying to work out whether it is worth coming in. Normally those calls ring straight to voicemail because nobody can stop a fade to answer, and half of them drive to whatever shop picks up. Instead the answering service catches each one, tells them the wait is about forty minutes, and books two of them into chairs that open up early afternoon, one with the barber he asked for by name. They show up instead of scrolling to the next shop, your chairs stay full all day, and not one barber put down the clippers to make it happen. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current shop phone number?",
         "Yes. It can answer on your existing shop number, or set up a new one registered in your name. Either way the number and every call, text, and booking that comes through it belong to you and go with you if you ever leave."),
        ("Can it tell someone the walk-in wait and whether we're open?",
         "Yes, and those are the two calls a barbershop gets most. It gives an honest read on the current wait, tells a walk-in whether to come in now or grab a chair for later, and answers whether you are open, so a ready customer does not drive past you to a shop that happened to pick up."),
        ("Can it book a specific barber by name?",
         "Yes, and for a barbershop that matters more than almost anything, because a man loyal to one barber will wait or leave over it. It books him with the barber he asks for, knows which barbers take walk-ins and which are appointment only, and hands anything that needs your call to you to confirm."),
        ("Will it sound like a robot to someone calling to book?",
         "It answers naturally and plainly, and it is upfront rather than pretending to be a person. A caller mostly wants to know he can get in, what the wait is, and that a real shop has him down, and a straight answer beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your barbers, your walk-in and appointment rules, your hours, and your services for you, so it is answering in days, not weeks. Start with a free audit and we will show you how many calls your current setup is missing.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for barbershops"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-barbershops.html", "The CRM that rebooks every client you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing walk-ins to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls, walk-in questions, and after-hours texts your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Barbershops ================================
{
    "slug": "crm-for-barbershops",
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "CRM for Barbershops",
    "title": "CRM for Barbershops | Top Shelf Business Solutions",
    "og_title": "CRM for Barbershops",
    "meta_desc": "A CRM for barbershops keeps every client and their barber in one place and rebooks them on the two to four week cut cadence, so a regular keeps his chair.",
    "service_schema_name": "CRM for Barbershops",
    "eyebrow": "For Barbershops",
    "h1_html": "CRM <em>for Barbershops</em>",
    "answer_block": "A CRM for barbershops keeps every client, their barber, and every past cut in one place and rebooks them on the tight two to four week cadence a fade runs on, so the regular growing out and the one who drifted away both come back to the same chair. Your book of regulars quietly becomes standing revenue.",
    "sections": [
        {"h2_html": "The regular who does not rebook is the standing chair you are <em>quietly losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most barbershops the problem is not filling a chair once, it is keeping a man on the tight rhythm his cut actually needs. A fade or a tapered cut starts looking grown-out in about two to three weeks, a lineup even faster, and a man who cares how he looks is a standing appointment every couple of weeks for as long as he keeps coming. When he leaves without the next cut booked, the way most men do when they are out the door and back to their day, that chair time does not disappear, it either sits empty or another walk-in fills it, and the steady every-two-weeks revenue he represented walks out with him.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Because the cadence is so short, a regular who drifts for even a few weeks has already missed a cut, and it is easy for him to end up in whatever chair is convenient when his hair finally bothers him. A CRM keeps every client and his history in front of you and sends the rebooking nudge itself, by text, timed to when his cut is growing out, so he books the next one and stays on the rotation instead of drifting off. You never sit down to chase it.</p>'},
        {"h2_html": "One barber, one chair, a client for <em>years</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A man does not shop around for a barber every few weeks the way he might for other things. Once he finds someone who cuts his hair exactly the way he likes it, he sits in that chair for years, and often will not let anyone else touch his head. That loyalty is the whole business, and it is also fragile, because the relationship lives in one barber\'s memory, his guard numbers, how he likes his neckline, the part he asks for, and if that barber has a full book or a rough week, the details are easy to lose.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every client, his barber, his usual cut and guard numbers, his beard preference, and his full history live in one place instead of one barber\'s memory and a stack of appointment cards.</li><li>Rebooking reminders go out on the short two to three week cadence a fade runs on, so regulars come back around without anyone tracking dates.</li><li>Standing appointments, the every-other-Friday-at-ten kind, are held and confirmed automatically, so a man who wants the same slot forever actually keeps it.</li><li>Loyalty punch cards and prepaid packages are tracked against the right client, so the man one cut from a free one actually comes in to claim it.</li></ul>'},
        {"h2_html": "The regular who drifted away is a <em>goldmine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A man you have not cut in a couple of months is usually not upset, he just got busy, traveled, or let it slide, and on a two-week rhythm it does not take long for a couple of missed cuts to turn into months gone. Reaching back out to the regulars who have gone quiet is some of the highest-return work a barbershop can do, because you are not paying to earn a stranger\'s trust, you are reminding a man who already liked how you cut his hair that his chair is still here. A lapsed regular has nothing to relearn either, his barber, his usual cut, and his history are all still on file, so he can pick up exactly where he left off.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The CRM finds the clients who have lapsed and sends that message for you, in your shop\'s voice, so a name you had written off turns back into a standing appointment without anyone digging through old cards. On a barber\'s slow week, that quiet win-back is the difference between an empty chair and a full one.</p>'},
        {"h2_html": "Filled cancellations, standing slots, and a list <em>you own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Two things quietly drain a booked day: the no-show who forgot, and the last-minute cancellation that leaves a hole. For a barbershop the second one stings less than it does for most trades, because there is almost always a walk-in who wanted a sooner chair, and the CRM can text a waitlist the moment a slot opens and fill it before the chair sits cold. Automatic confirmations and reminders go out ahead of every appointment, the most reliable way to hold no-shows down and give a man an easy way to move his time instead of just not showing. Every client and note is yours and exportable any time, never locked inside software you only rent, and because the CRM shares one database with the answering service, a chair the phone books lands here and gets rebooked on its own. Nothing you have already earned is left to go cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A fade client who rebooks before it <em>grows out</em>",
        "body_html": "A regular comes in for a skin fade on a Friday and heads out without booking the next one, the way most men do when they are already late getting back to work. Normally that is the last you think of it until he turns up three weeks later, or ends up in a chair across town when his fade gets shaggy. Instead, about two weeks on, the CRM texts him a friendly reminder that he is about due, written to sound like the shop, with a link to grab his usual slot with his barber. He books that afternoon and stays on the every-two-weeks rotation that keeps him in your chair all year. You never sat down to chase it. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing clients and their cut history?",
         "Yes. Your current clients, their contact details, their barber, usual cut and guard numbers, beard preferences, notes, and past visits come in and live in one place, and everything stays yours and exportable. The point is to make the book of regulars you already have actually work for you."),
        ("Will it really prompt regulars to rebook on its own?",
         "Yes, on the cadence you set. Because a fade runs on a short two to three week rhythm, a regular can hear from you right as his cut is growing out, all sent for you, so the standing appointments keep rebooking instead of depending on someone remembering at the desk. You can message anyone directly any time too."),
        ("Does it work for a shop full of booth-rent barbers?",
         "Yes. Each barber keeps his own book and his own clients inside the shared system, so rebooking reminders, notes, and history follow the right barber, and a regular loyal to one chair stays tied to that barber instead of getting mixed into the whole shop."),
        ("Can it handle standing appointments, punch cards, no-shows, and cancellations?",
         "Yes. Standing slots are held and confirmed automatically, loyalty punch cards and packages are tracked against the right client, reminders cut no-shows, and when someone cancels it can text a waitlist to fill the chair before it sits empty."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your clients, build your rebooking and win-back reminders around each barber's book, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where regulars are slipping through today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for barbershops"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-barbershops.html", "The answering service that feeds it every booking"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting regulars <em>fall off your rotation</em>",
    "cta_sub": "Get a free audit of how many of your regulars are overdue for a cut or have quietly stopped coming in, whether you work with us or not. No credit card, never a call center.",
},
# ============================= Marketing for Barbershops =============================
{
    "slug": "marketing-for-barbershops",
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Marketing for Barbershops",
    "title": "Marketing for Barbershops | Top Shelf Business Solutions",
    "og_title": "Marketing for Barbershops",
    "meta_desc": "Barbershop marketing keeps your Google profile and Instagram active and your name first in the map pack, so nearby men find and pick you first.",
    "service_schema_name": "Marketing for Barbershops",
    "eyebrow": "For Barbershops",
    "h1_html": "Marketing <em>for Barbershops</em>",
    "answer_block": "Marketing for barbershops keeps you visible where men actually pick a barber, your Google Business Profile, the map pack, and Instagram, so when someone nearby searches for a barbershop or a fade near them, yours is the close, well-reviewed shop with fresh-cut photos he walks into instead of the shop that let its profile go stale.",
    "sections": [
        {"h2_html": "Men pick a barber by who is <em>close and looks right</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A man choosing a barbershop does not agonize over it the way some people shop for a service. He searches, glances at the map, and picks a shop that is close, open, and looks like his kind of place with cuts that match what he wants. That whole decision happens on a phone in under a minute, usually the day he needs a cut, and it turns on two things: are you near him, and do you look like you cut hair the way he wears it. So the entire game for a barbershop is being easy to find and obviously good in the exact spot a man looks, not clever ads aimed at people who are not thinking about their hair.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Show up close, look busy and current, and put real cuts in front of him in that moment, and the walk-in is usually yours. Show a dead profile with no photos, and he picks the shop that looked alive, no matter how sharp your barbers actually are.</p>'},
        {"h2_html": "Your Google Business Profile is your <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a man searches for a barbershop near him, or for a fade, a beard trim, or a hot towel shave in your area, the map pack, those three local listings with the star ratings, is the first thing he sees, above the websites and the ads. A profile left untouched for months, with a dim photo and hours that may or may not be right, looks like a shop that might not even be open, next to one with recent cuts, current hours, whether you take walk-ins, and a steady stream of fresh reviews. It is where the man in his truck settles the practical questions at a glance, are you open now, do you take walk-ins, do you cut the style he wants, is it his kind of shop. Keeping that profile full, fresh, and honest is a quiet advertisement running in the one spot a man actually decides from, and it is free space most shops let go to waste.</p>'},
        {"h2_html": "Instagram is where a fresh cut becomes a <em>walk-in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a barbershop, social media is the portfolio and the vibe check in one. A man deciding between shops will scroll your feed to see the cuts you actually turn out, the fades, the lineups, the beard work, and to get a feel for whether this is his kind of place. A feed full of real fresh-cut photos and a bit of the shop\'s culture does the selling for you while the chairs sit empty at night, and it lets each barber show off the work that builds his own following. A feed that has gone quiet for months tells him the opposite. Posting real cuts steadily, and making it easy to go from a photo straight to booking or the door, is what turns a scroll into a man in the chair, especially when the post points right to a way to reach you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It also gives each barber a way to build his own name. A lot of men follow a barber, not just a shop, and a feed that tags and features each chair lets a new client find the barber whose work he likes and ask for him next time, while a short clip of a fade coming together travels further than any still photo and pulls in men from just outside your usual blocks.</p>'},
        {"h2_html": "Reviews and a steady local presence, <em>working together</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Recent, honest reviews are the other half of the trust a man weighs before he lets a stranger near his head, and they feed the same Google profile that decides whether you show up in the map pack at all. For a barbershop the reviews do specific work, they tell the next man whether the fade was clean, whether the barber listened, and whether the wait matched what the shop said. More reviews lift you in local search, which brings more men in, who leave more reviews, and it compounds. A steady presence, fresh cut photos, replies to the reviews that land, posts tied to the busy stretches before holidays and school, keeps you top of mind across the neighborhoods you actually draw from. This is the public-facing side of the shop, aimed at men who are not your regulars yet; the private follow-up to the clients already in your book is the CRM. Either way the reputation stays yours, tied to your own profile, not a directory or an app that rents your own name back to you.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "New in town, and yours is the shop he <em>can already see</em>",
        "body_html": "A man just moved to the area and needs a new barber, which for a lot of guys is a genuinely annoying search because a bad cut sticks around for weeks. He looks up a barbershop near him and, the same minute, taps through to see the work. Because your Google profile is active and full of recent fades, shows you take walk-ins, and carries a wall of fresh five-star reviews, and your feed shows the exact style he wears, yours is the shop that feels safe to try. He walks in that week and, if the cut is right, sits in that chair for the next three years. The shop a mile away, with a profile last touched a year ago, never entered the running. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile and Instagram for me?",
         "Yes. We keep both active with real cut photos, updates, and local content on a regular schedule, and keep your hours, services, and whether you take walk-ins accurate, so you look current and busy whenever a man looks you up."),
        ("How do I get more reviews?",
         "Reviews are part of the picture, asked for at the right moment and pointed at the Google profile that feeds your local ranking. We help you gather honest reviews from happy clients and reply to the ones that come in, since responding is itself a signal that lifts you in local search."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with the regulars already in your book, rebooking and win-back. Marketing is the public-facing side, your Google profile, reviews, and social, aimed at men who are not your clients yet but need to find you and like your work before they walk in."),
        ("Do I need to be on every social platform?",
         "No. For a barbershop the work is concentrated where men look and decide, your Google Business Profile and the visual feeds where they judge a cut. We focus your effort there instead of spreading you thin across places that do not bring walk-ins."),
        ("How long before I see it working?",
         "A neglected Google profile can climb in the map pack within weeks once it is active and complete, and it compounds as reviews and photos build. Setup is included, and a free audit will show you what your online presence looks like to a man searching near you today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for barbershops"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-barbershops.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the barbershop they <em>can already see</em>",
    "cta_sub": "Get a free audit of how visible you actually are on Google and social in your area right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Websites & SEO for Barbershops =========================
{
    "slug": "websites-seo-for-barbershops",
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Websites & SEO for Barbershops",
    "title": "Websites & SEO for Barbershops | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Barbershops",
    "meta_desc": "A barbershop website built for SEO ranks for barber and fade near me, shows the walk-in wait and each barber's booking link, and books the chair in one tap.",
    "service_schema_name": "Websites & SEO for Barbershops",
    "eyebrow": "For Barbershops",
    "h1_html": "Websites &amp; SEO <em>for Barbershops</em>",
    "answer_block": "A barbershop website built for SEO ranks for what a man types when he needs a cut, barbershop near me, fade near me, beard trim, shows whether you are open and the walk-in wait, and lets him book a specific barber in one tap, so the client is yours instead of a booking app's cut.",
    "sections": [
        {"h2_html": "A man decides fast, on his <em>phone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A man who needs a cut is on his phone, usually the same day, and he is not going to read paragraphs or hunt for a phone number. He wants three things answered in the first few seconds: are you open, how long is the wait, and can he get in with his barber. A site that loads slow, hides the hours, or makes him call to find out the wait, when every barber is mid-cut and cannot pick up, is a site he backs out of and replaces with the next shop on the map. The cut itself can be the best in town and it will not matter if the site made him work to find that out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site has to open fast on a phone, put your hours, your walk-in status, and a book button right in front of him, and make coming in feel easy. A sharp shop with an afterthought of a website loses men it never even hears about, and loses them to shops that are not better, only easier to say yes to.</p>'},
        {"h2_html": "Rank for barber and fade <em>near me</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a man wants a cut, the search is short and local: barbershop near me, barber near me, fade near me, beard trim, kids haircut, hot towel shave in a named neighborhood. The very top of that results page is often a national directory or a booking app, not the shops themselves, because those sites carry thousands of pages and years of authority. You are not going to knock a national directory off the single broadest term this year, and you do not need to. The winnable ground is your own shop name, the neighborhoods you actually draw from, and each specific thing a man types when he is ready to sit down, a fade, a beard line-up, a kids cut, a straight-razor shave. Pages built around the cuts you offer and the areas you serve are what earn those clicks, and the local, specific searches can start moving within weeks while the broad head term compounds over months.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It helps that the bar is low. A lot of barbershops never build a real site at all, leaning on a Google listing or an Instagram account, so the ground for your own name and your own neighborhoods is often wide open to whoever bothers to claim it. Simple pages for the things men actually search, a kids first haircut, a wedding-morning group, walk-ins welcome, senior and student rates, give Google something concrete to rank and a searching man a clear reason to pick you.</p>'},
        {"h2_html": "Each barber's chair, bookable <em>by name</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barbershop website has a job most sites do not: it has to work for a room of barbers who each keep their own following. A man coming to your site is often not looking for the shop in general, he is looking for his barber, and the site should let him book that specific chair in one tap, or pick the next open one if he is new and just wants a cut today. Give each barber a booking link and a few photos of his work, and the site does double duty, it lands the new walk-in and it lets a loyal regular lock in his usual slot without a phone call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Just as important is the question a man always has before he leaves the house, how long is the wait. A site that shows whether you are open, whether you are taking walk-ins, and roughly what the wait looks like answers the one thing that decides whether he comes now or later, and it catches the man deciding in the moment instead of sending him to call a phone nobody can answer mid-fade.</p>'},
        {"h2_html": "The booking is <em>yours</em>, not an app's cut",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A booking that comes through a marketplace app skims its cut, keeps the client inside its own account, and stops sending anyone the day you stop paying, and the man who booked there thinks of the app, not your shop. A site you own does the opposite: it keeps ranking, keeps showing your barbers\' work, and sends the booking and the client straight into your own book at no cut taken. It feeds the same CRM that rebooks every regular it brings in and the answering service that catches the men who would rather call than tap, so nothing it earns you slips away. What you build is an asset that compounds and sits under your own name, not rent you pay forever to reach your own clients.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A lunchtime 'fade near me' search, in the chair <em>by one</em>",
        "body_html": "On his lunch break a man decides he needs his fade cleaned up before the weekend and searches for a barber near him. He lands on your site, and instead of a slow page and a contact form, he sees that you are open, taking walk-ins with about a twenty-minute wait, and a button to book his barber in one tap. He taps it, sees his usual barber has a one o'clock, and books it before he finishes his lunch. He is in the chair that afternoon, a booking that would have gone to whichever shop turned up first or answered the phone, and it came straight to you with no app taking a cut. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and booking apps?",
         "Not for the broadest terms overnight. It can realistically rank for your shop name, your specific neighborhoods, and the service searches a national app has no reason to target well, a fade, a beard trim, a kids cut, a straight-razor shave near you, which is exactly where a local shop can win."),
        ("Can the site show whether we're open and the walk-in wait?",
         "Yes, and for a barbershop it should. We can surface your hours, whether you are taking walk-ins, and a read on the current wait up front, because that is the first thing a man checks before he decides whether to come now, and a site that answers it catches the walk-in a phone nobody can answer would lose."),
        ("Can each barber have his own booking link?",
         "Yes, and for a shop of booth-rent barbers that matters. Each barber can have his own booking link and a few photos of his work, so a regular books his specific chair in one tap while a new man grabs the next open one, and every booking still lands in your own system."),
        ("How is this different from just listing on a booking app?",
         "A booking app takes a cut of a chair that could have come to you directly, keeps the client in its own system, and stops the day you stop paying. A website you own captures the booking and the client for nothing extra and keeps working long after it is built, so it becomes an asset instead of a fee on every cut."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for barbershops"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-barbershops.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search for <em>a barber in your town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and booking apps taking your chairs, whether you work with us or not. No credit card, never a call center.",
},
]
