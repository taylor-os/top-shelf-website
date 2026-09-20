"""Per-page content specs for the SEO corpus, yoga studios batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, yoga-studio-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the gym or massage content reworded.

Salon, Spa & Fitness hub, shared with specs_gyms.py and specs_massage_therapy.py. Four service
angles live here in one file (the ai-receptionist dict carries "demo": True). A yoga studio is
its own animal: it is class-based, running a schedule of group classes rather than a gym's
equipment and 24/7 access, and it is not a massage therapist's 1:1 room. It runs on an intro
offer (a free first class, an intro week or month) that has to convert a nervous newcomer into
a member before it expires, then on class packs, memberships, waitlists, and the win-back of
students who drifted, with teacher-training and workshops as the higher-ticket upsell sold to
the community it already built. So this file is written around teachers who cannot answer
mid-class, the intro-offer-to-membership funnel, filling capped classes, and a beginner who
decides on trust, schedule clarity, and a welcoming reputation, never a gym membership funnel
or per-visit massage rebooking. The copy stays professional and makes no health or wellness
outcome claims. Each example body ends with the literal "Illustrative example, not a client."
per the honesty rule; if the generator also appends that line, dedupe there.
"""

SPECS = [
# ============================ AI Receptionist for Yoga Studios ============================
{
    "slug": "ai-receptionist-for-yoga-studios", "demo": True,
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "AI Receptionist for Yoga Studios",
    "title": "AI Receptionist for Yoga Studios | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Yoga Studios",
    "meta_desc": "A yoga studio answering service picks up every call and DM the second it lands, answers the beginner questions, and books the intro offer while class is on.",
    "service_schema_name": "AI Receptionist for Yoga Studios",
    "eyebrow": "For Yoga Studios",
    "h1_html": "AI Receptionist <em>for Yoga Studios</em>",
    "answer_block": "A yoga studio answering service picks up every call and DM the moment it lands, day or night, tells a nervous first-timer apart from a current member with a quick question, and books the intro offer or a first class while your teachers are on the mat. You keep your own number, and every student it books is yours.",
    "sections": [
        {"h2_html": "The call you miss is the beginner who <em>joins the studio that answered</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When your teachers are on the mat leading a class, the phone is silenced and nobody is at the desk to pick it up, because a yoga class runs sixty, seventy-five, or ninety minutes with no break to step out for a ringing phone. Plenty of studios run lean, with a teacher who is also the front desk, so a call that comes in during a class simply goes unanswered by anyone. A newcomer trying to figure out how to start will not leave a voicemail and wait for a callback. They hang up and try the next studio on the map, and the one after that, until a person answers or an online booking replies. And because a studio runs on turning that first visit into a membership, a missed first-timer is not one lost drop-in, it is a membership that never got the chance to begin.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An answering service picks up the moment the call comes in, sounds warm and welcoming instead of rushed, asks what the caller is looking for and whether they have practiced before, and either books the intro offer and a first class outright or captures the details so the lead survives. That newcomer ends up on your schedule rather than passed to the studio down the street that simply happened to be free when the phone rang, and you never had to break the class you were already teaching.</p>'},
        {"h2_html": "Most new students reach out at night or <em>from a DM</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A lot of the interest in trying yoga never lands during your open, staffed hours at all. Someone decides on a Sunday night that this is finally the week they start, a class clip catches them mid-scroll and they message to ask whether it is right for a beginner, or a friend talks them into going and they reach out once the studio is dark. Interest like that has a short shelf life. If the message sits unanswered until a teacher finishes the last class tomorrow, the resolve has cooled and they have already booked somewhere that replied while they were still deciding.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The answering service replies in seconds to a text or a social message, not only a phone call, and turns that late-night decision into a booked first class while the person is still ready to act on it. The one who messaged at eleven at night wakes up already on your schedule, with the intro offer explained and the details sitting in their texts, instead of scrolling on to the next studio because no one replied. For a studio that lives on filling classes, that reply going out before the moment cools is the whole difference between a booked mat and a lead that never comes back.</p>'},
        {"h2_html": "Built around how a yoga studio <em>actually fills classes</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Signing a new student is rarely one quick question, and a generic call center reading a script does not know your class schedule from your workshop calendar, or that a nervous beginner usually needs to know which class is safe to start with before they will commit to anything. The answering service handles the conversation the way an attentive front desk would on a calm afternoon.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers calls, texts, and social messages around the clock, so the person who finds you at midnight and the one who messages on a holiday both reach a real reply instead of a voicemail box.</li><li>Answers the questions that actually decide it: which class suits a first-timer, the schedule, how the intro offer works, whether you rent mats, and what to bring the first time.</li><li>Books the next real step, the intro offer, a first class, or a workshop seat, straight onto your schedule, because a newcomer ready to come in should never be told to call back later.</li><li>Handles a current member with a billing or class-booking question differently from a first-timer, so the students already paying you never feel like they are explaining themselves to a stranger.</li></ul>'},
        {"h2_html": "You own the number, the leads, and <em>the student list</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number this answers on is yours, your existing studio line or a new one put in your name, never ours. Every caller, every DM, and every lead it captures stays exportable whenever you want it, because the student list a studio slowly builds is the most valuable asset it owns, and it should never be rented back to you or locked behind a long contract. And the answering service does not work off on its own. It is one piece of the Top Shelf platform, so every lead it takes drops straight into the CRM that turns an intro offer into a paying membership and keeps following up, which means the person who messaged at nine at night becomes a member instead of a note the morning shift never finds. There is nothing for you to run and nothing to answer while you are teaching.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A 9pm beginner DM, booked while the <em>room is full</em>",
        "body_html": "It is nine on a weeknight and someone who has been meaning to try yoga for months finally sees a clip of one of your classes and sends a message asking whether you have anything gentle enough for a complete beginner. Your teachers are leading a full room and nobody is free at the desk, but the answering service replies within seconds, explains how the intro offer works, points them to a beginner-friendly class on the schedule, mentions that mats are there to borrow, and books them into Saturday morning. They wake up with the first class confirmed and the details in their texts, instead of scrolling on to the next studio because no one answered. You gained a new student while every teacher you have was busy leading a class. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current studio phone number?",
         "Yes. It can answer on your existing studio number, or set up a new one registered in your name. Either way the number and every call, text, and lead that comes through it belong to you and go with you if you ever leave."),
        ("Can it answer Instagram and text messages, not just calls?",
         "Yes, and that matters for a studio. A lot of new students reach out by DM or text after seeing a class clip at night, and the answering service replies to those instantly, answers the first questions about classes and the intro offer, and books the visit, so a late-night message does not sit until someone finishes teaching."),
        ("Can it actually book the intro offer or a first class?",
         "Yes. It books the next real step, the intro offer, a first class, or a workshop seat, straight onto your schedule based on your rules, and you get the details right away. For anything that needs a person, a membership freeze or a billing question, it takes the details and hands it to your team."),
        ("Will it sound like a robot to a nervous beginner?",
         "It sounds natural and welcoming, and it never pretends to be a human when it is not. Someone working up the nerve for their first class mostly wants to know they can get in, which class to start with, and that a real studio has them booked, and a friendly reply beats a voicemail box every time. You can hear it handle a live call before you decide."),
        ("How fast can it be running?",
         "Setup is included with no separate onboarding fee. We configure your class schedule, your intro offer, your hours, and your booking rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you how many inquiries your current phone setup is quietly letting slip.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for yoga studios"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-yoga-studios.html", "The CRM that turns a first class into a member"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing new students while you <em>teach</em>",
    "cta_sub": "Get a free audit of how many calls, texts, and DMs your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Yoga Studios ================================
{
    "slug": "crm-for-yoga-studios",
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "CRM for Yoga Studios",
    "title": "CRM for Yoga Studios | Top Shelf Business Solutions",
    "og_title": "CRM for Yoga Studios",
    "meta_desc": "A CRM for yoga studios keeps every student, intro offer, and class pack in one place and follows up for you, so a first class becomes a member who stays.",
    "service_schema_name": "CRM for Yoga Studios",
    "eyebrow": "For Yoga Studios",
    "h1_html": "CRM <em>for Yoga Studios</em>",
    "answer_block": "A CRM for yoga studios keeps every student, intro offer, and class pack in one place and does the follow-up for you, so the first-timer who tried a class but never came back and the member who quietly drifted off both return to the mat instead of the studio down the street. Your roster quietly becomes revenue that repeats.",
    "sections": [
        {"h2_html": "The intro offer that never converts is the membership you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most studios do not have a foot-traffic problem so much as a conversion problem. The intro offer, a free first class, an intro week, or an intro month, exists to do one thing: turn a curious newcomer into a member before it runs out. Someone claims it, comes to a class or two, fully means to sign up, and then the intro period quietly ends with nobody reaching out. That was never a dead lead. A person who walked in, rolled out a mat, and liked it enough to come back is far warmer than any cold click, and letting that go unworked is the costliest miss a studio makes. It just needed a friendly nudge before the intro window closed, and a nudge is exactly what slips when your teachers are leading classes all day.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every intro-offer student in front of you and follows up on a schedule you set, timed to the window before the offer expires, with texts and emails that go out whether or not anyone at the desk remembers. The newcomer still deciding whether to commit hears from you again while the offer is live and the habit is fresh, and the intro turns into a paying membership instead of a maybe that fades, all without a single reminder written by hand.</p>'},
        {"h2_html": "Retention and class packs are the <em>whole business</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A studio lives on memberships and class packs renewing, so the real fight is not signing a student once, it is keeping them past the first month and making sure the classes people prepaid for actually get used before they lapse. A student who quietly stops coming is a cancellation that has not been filed yet, and catching that drift early protects more revenue than almost any new-student push ever will.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every student, their join date, membership or class-pack balance, preferred classes, and notes live in one place instead of a booking app, a spreadsheet, and someone\'s memory.</li><li>New students move through a welcome sequence over their first weeks, a nudge to book that second class, a check-in after the first, so the habit sets before the early motivation fades.</li><li>A class pack running low or close to expiring triggers a reminder, so a ten-class pack gets finished and repurchased instead of quietly written off.</li><li>You can see who has not been on the mat lately and reach out with a real reason to come back before a quiet student becomes a cancelled one.</li></ul>'},
        {"h2_html": "Workshops and teacher training are <em>revenue you already earned</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The students already in your room are the natural audience for the offerings that pay more than a single drop-in: a weekend workshop, a multi-week series, a teacher training. These are almost never sold to strangers, they are sold to the regulars who already trust you and want more than a weekly class. But no one can keep track of which student mentioned being curious about a training, or which regulars would fill a workshop if only they heard about it, so those higher-value seats sit empty while the interest was there all along. The CRM lets you reach the right students, the regulars, the ones who have been coming a while, the ones who asked, with the workshop or training that fits them, so the offerings with the biggest tickets fill from the community you already built instead of from an ad budget. It is a kind of upsell a class-by-class studio leaves on the table simply because nobody is tracking who to ask.</p>'},
        {"h2_html": "Win-back, filled classes, and a student list <em>you own</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A student who stopped coming six months ago is usually not upset, they simply fell out of the routine, got busy, or told themselves they would start again eventually. Reaching back out to the people who have lapsed is some of the highest-return work a studio can do, because there is no stranger to win over, only a reminder to someone who already knew your room that the door is still open. A lapsed student has nothing to relearn, their account, their history, and their familiarity with the space are all still there, and a warm, well-timed message, especially right at the New Year when half the town is thinking about it again, brings a real share of them back onto the schedule. The CRM finds the students who have gone quiet and sends that note for you. It also sends class confirmations and reminders that cut the no-shows and late cancels that leave a capped class with empty mats, and it can offer a freed-up spot to the waitlist the moment someone drops, so a full class stays full. Every student and every note is yours and exportable at any time, never locked inside software you only rent, and because the CRM shares one database with the answering service, a lead the phone captures lands here and gets worked on its own. Nothing you have already earned is left to go cold.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "An intro offer that <em>signs itself</em>",
        "body_html": "Someone claims your intro offer, comes to a first class on a Tuesday, has a good time, and leaves saying they will think the membership over, the way most people honestly do. Normally the intro period just runs out and you never hear from them again. Instead, the next morning the CRM sends a friendly note saying it was great to have them on the mat, with a simple link to start a membership, and a gentle reminder a few days before the intro offer expires. The other studios they tried never reached back out, so when they are finally ready that weekend, yours is the only name still sitting in front of them, and they join without shopping around any further. No one at the desk had to remember to chase it down. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing students and their history?",
         "Yes. Your current members, leads, class packs, and visit history come in and live in one place, and everything stays yours and exportable. The point is to make the roster you already have actually work for you instead of sitting in a booking app."),
        ("Will it really follow up on intro offers on its own?",
         "Yes, on the schedule you set and timed to the window before the offer expires. A first-timer who has not signed hears from you a day or two after their class and again before the intro runs out, all sent for you, so a newcomer on the fence keeps hearing from you while the other studios go quiet. You can jump in and message anyone directly any time."),
        ("Can it help me keep members from cancelling?",
         "That is the biggest thing it does. It onboards new members over their first weeks, flags the ones who have not been in lately so you can reach them before they cancel, and reactivates students who already lapsed, all of which protects the memberships and class packs a studio runs on."),
        ("Can it track class packs and remind students to use them?",
         "Yes. A class pack running low or close to expiring triggers a reminder, so the classes a student prepaid for actually get used and the pack gets repurchased instead of quietly written off. Memberships and gift cards are tracked against the right student the same way."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your students, build your intro-conversion, onboarding, and win-back sequences, and connect it to your calls and schedule, so it is working in days. Start with a free audit and we will show you where students are slipping through today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for yoga studios"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-yoga-studios.html", "The answering service that feeds it every lead"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Turn intro offers into <em>memberships that stay</em>",
    "cta_sub": "Get a free audit of how many of your intro offers never converted and how many members have quietly stopped showing up, whether you work with us or not. No credit card, never a call center.",
},
# ============================== Marketing for Yoga Studios ==============================
{
    "slug": "marketing-for-yoga-studios",
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Marketing for Yoga Studios",
    "title": "Marketing for Yoga Studios | Top Shelf Business Solutions",
    "og_title": "Marketing for Yoga Studios",
    "meta_desc": "Yoga studio marketing keeps your Google Business Profile active and your name first in the map pack, so nearby beginners find, trust, and book you first.",
    "service_schema_name": "Marketing for Yoga Studios",
    "eyebrow": "For Yoga Studios",
    "h1_html": "Marketing <em>for Yoga Studios</em>",
    "answer_block": "Yoga studio marketing keeps you visible where new students actually look, your Google Business Profile, the map pack, and social, so when someone nearby searches for a yoga class or a beginner-friendly studio, yours is the current, welcoming, well-reviewed name they book instead of the studio that let its profile go stale.",
    "sections": [
        {"h2_html": "A new student picks a studio on <em>trust and welcome</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Trying yoga for the first time takes a little nerve. A lot of newcomers quietly worry that they will not be able to keep up, or that everyone else in the room will be far more advanced, so before they ever walk in they look you up, study the schedule, and read a handful of reviews to decide whether this feels like a place a beginner belongs. All of that plays out on a screen, inside a minute or two, well before anyone picks up the phone. So for a studio the whole task is to be easy to find, obviously current, and plainly welcoming right where a new student is already looking, rather than buying clever ads aimed at people who have no interest in yoga yet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get found, look active, and read as welcoming in that moment, and the booking is usually yours. Look neglected or invisible, and they book the studio that showed up looking current and glad to have a beginner, no matter how good your teachers actually are.</p>'},
        {"h2_html": "Your Google Business Profile is your <em>storefront</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for a yoga studio nearby, or for a beginner class or a specific style in your town, and the map pack, that trio of local listings carrying the star ratings, sits at the very top, ahead of the websites and even the ads. A listing left untouched for months, with a dim photo and hours that may or may not still be right, reads as a studio that might not even be open. One with a real photo of a class in progress, current hours, the styles you teach, and a steady stream of fresh reviews reads as an active studio with a real community. A profile kept full, fresh, and honest is a small advertisement running day and night in the exact place a new student decides from, and it costs nothing, which is why it is a shame so many studios leave it to gather dust. It is also where the practical questions get settled at a glance: what the schedule looks like, whether there is an intro offer, which classes are friendly to a beginner, whether you rent mats, and whether there is parking, so the studio that answers those on the spot wins the newcomer who would have quietly moved on from one that made them dig or call to find out.</p>'},
        {"h2_html": "Community and beginner-welcoming proof do <em>the selling</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">People do not choose a studio for the room, they choose it for whether they will feel like they belong once they are in it. Nothing settles that like seeing real people, including obvious beginners, in your actual classes, and reading reviews that mention how welcoming the teachers are to someone brand new. Honest photos and short clips of a real class, a teacher who plainly knows names, a beginner series that hands someone an easy way in, all of it quietly answers the worry every newcomer carries before they ever call, that they will be the only one who does not know what they are doing. Social is usually where they first notice you, a class clip or a schedule post catching their eye, and keeping it real and specific to your studio rather than staged stock photos is what turns a nervous scroll into a first class. It is the reason a newcomer picks you over the anonymous studio a mile down the road.</p>'},
        {"h2_html": "Reviews and a steady local presence, <em>working together</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Reviews are the other half of local trust, and they pull double duty. A newcomer reads them to judge whether your students are people like them and whether the studio delivers the welcome it promises, while Google reads them to decide whether to show you in the map pack at all. More honest reviews lift you in local search, which puts you in front of more new students, who leave more reviews of their own, and the whole thing feeds itself. What keeps it turning is a steady presence: fresh photos of real classes, a reply to every review whether it is glowing or hard to read, posts tied to the schedule, the workshops, and the intro offer your students actually care about. All of that is the public-facing side of the studio, aimed at people who are not students yet. The private, one-to-one follow-up with the people already on your roster is the CRM, and the two are meant to run as a pair. Either way the reputation stays yours, tied to your own profile, not a class-booking app that quietly rents your own name back to you.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A 'beginner yoga near me' search finds <em>the welcoming studio</em>",
        "body_html": "Someone who has been meaning to try yoga for months finally searches one evening for a beginner-friendly studio near them. Two studios sit the same short drive away. One profile has not been touched in a year, a single dim photo and hours that may be wrong. Yours is active: recent photos of a real class with people who clearly started as beginners, the schedule and the intro offer easy to see, and a wall of reviews that mention how welcoming the teachers are to someone new. They book the intro offer at your studio that night, because it is the one that looked like it wanted them there. The other studio never entered the running, and it spent the season wondering where the new students went. Illustrative example, not a client."},
    "faqs": [
        ("Do you post to my Google Business Profile and social for me?",
         "Yes. We keep them active with real photos of your classes, schedule updates, and local content on a regular schedule, and keep your hours, styles, and intro offer accurate, so you look current and welcoming whenever a new student looks you up."),
        ("How do I get more reviews?",
         "Reviews are a core piece of it, requested at the right moment and pointed at the same Google profile that drives your local ranking. We help you gather honest reviews from happy students and reply to the ones that come in, since responding is itself a signal that lifts you in local search."),
        ("Can you help beginners feel comfortable choosing my studio?",
         "Yes, and that is the heart of it for a studio. We keep your profile and social full of honest photos of real classes and reviews that speak to how welcoming you are to someone new, so a nervous first-timer can see before they ever call that your studio is a place a beginner belongs."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with people already on your roster or in your leads: onboarding, retention, and win-back. Marketing is the public-facing side, your Google profile, reviews, and social, aimed at people who are not students yet but need to find you and trust you before they will try a class."),
        ("How long before I see it working?",
         "A neglected profile can climb in the map pack within weeks once it is active and complete, and it compounds as reviews and fresh photos build. Setup is included, and a free audit will show you what your online presence looks like to a new student searching near you today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for yoga studios"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-yoga-studios.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the studio a beginner <em>picks first</em>",
    "cta_sub": "Get a free audit of how visible you actually are on Google and social in your area right now, whether you work with us or not. No credit card, never a call center.",
},
# ============================ Websites & SEO for Yoga Studios ============================
{
    "slug": "websites-seo-for-yoga-studios",
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
    "breadcrumb_leaf": "Websites & SEO for Yoga Studios",
    "title": "Websites & SEO for Yoga Studios | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Yoga Studios",
    "meta_desc": "A yoga studio website built for SEO ranks for beginner yoga and yoga-near-me, shows the class schedule and intro offer, and books a first class in one tap.",
    "service_schema_name": "Websites & SEO for Yoga Studios",
    "eyebrow": "For Yoga Studios",
    "h1_html": "Websites &amp; SEO <em>for Yoga Studios</em>",
    "answer_block": "A yoga studio website built for SEO shows up for what a new student actually types, yoga near me, beginner yoga, hot or prenatal yoga in your area, puts the class schedule and intro offer front and center, and books a first class in one tap, so the student is yours, not a class-booking app's cut.",
    "sections": [
        {"h2_html": "A new student decides if your studio is <em>their place</em> before they walk in",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Trying yoga is a small leap of nerve, so a newcomer does their homework before they show up. They land on your site from a search or a link in your profile, and within seconds they are deciding whether this looks like a place for someone like them, whether there is a class that fits both their schedule and their level, and whether starting will feel easy or awkward. A site that loads slowly, hides the schedule, buries the intro offer, or forces them to call during the day, when your teachers are teaching and cannot pick up, is a site they quietly leave for the studio that felt more welcoming.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site has to load fast on a phone, show the real room and real people, make the schedule and the way in obvious, and read like an invitation rather than a wall to climb. A genuinely great studio with a neglected website loses newcomers it never even hears about, and it loses them to places that are not necessarily better, only easier to say yes to.</p>'},
        {"h2_html": "Rank for what someone types when they are <em>ready to try a class</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The results at the very top for yoga near me in your town are often a class-booking marketplace or a directory, not the local studios themselves. Those sites publish thousands of pages on top of years of built-up authority, so a searching newcomer lands there first, and the sign-up either gets passed around or costs you a cut of a student who could have come straight to you at no cost. Beating a national marketplace on the single broadest term is not happening this year, and it does not have to. You can win the searches those big platforms have no reason to cover well: your own name, the neighborhoods you actually draw from, and the specific things people look for once they are ready, beginner yoga, a style you teach like vinyasa, hot yoga, yin, or restorative, prenatal yoga, a class at a time you actually run. Pages built around the styles and the areas you genuinely serve are what search engines, and newcomers ready to book, reward with the click, because a national app has no reason to write a real page about your neighborhood or your Saturday beginner class.</p>'},
        {"h2_html": "A visitor on their phone should see the schedule and <em>start in one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A newcomer is almost always on a phone, often late at night just after deciding it is finally time, and will not read long paragraphs or hunt for a way in. The site has to load fast, show real photos and short clips of the room and the classes right at the top, put your reviews where they cannot be missed, and above all make the class schedule and the intro offer impossible to miss, because for a studio the schedule is the product, the first thing a newcomer needs to see and the very thing a class-booking app tends to bury. Give them one clear button to claim the intro offer or book a first class that works in a single tap, day or night. It should never make someone create an account or download an app just to see the schedule or the price, because every extra step between the impulse and the booking is one more chance to close the tab and lose the nerve. A beautiful site that makes starting hard is a wasted opportunity, and a visitor should never leave without an easy way onto a mat.</p>'},
        {"h2_html": "The sign-ups are <em>yours</em>, not a marketplace's",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A sign-up that comes through a class-booking app or a pay-per-lead service always skims its cut, was never fully yours in the first place, and vanishes the moment you stop paying the platform. A site you own goes on ranking, goes on showing your schedule and your intro offer, and goes on taking first-class bookings for as long as it is up, and it sits under your name, not under a platform that can rewrite its terms, raise its take, or cut you loose. It feeds straight into the same CRM that turns a first class into a membership and the same answering service that fields the newcomers who would sooner send a DM than tap a button, so none of what it earns you ever slips through the cracks. What you are building is an asset that gains value over time, not a rent you keep paying forever just to reach your own students.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late-night 'beginner yoga near me' search finds <em>you</em>, not an app",
        "body_html": "Someone has been telling themselves for weeks that they will finally try yoga, and at nine at night they search for beginner yoga near them on their phone. Instead of a class-booking marketplace that would take a cut and line up ten studios side by side, they find your site ranking for that exact search, with photos of the real room, the class schedule right there on the page, a clearly marked beginner class, honest reviews underneath, and one button to claim the intro offer. They see a place they could actually belong, tap to book Saturday morning, and start before they close the tab and talk themselves back out of it. The sign-up is yours, nobody skimmed a cut, and no app ever sat between you and your new student. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and class-booking apps?",
         "Not for the broadest terms overnight. It can realistically rank for your studio name, your specific neighborhoods, and the beginner and style searches a national app has no reason to target well, beginner yoga, vinyasa, hot yoga, yin, and prenatal yoga in your area, which is exactly where a local studio can win."),
        ("How is this different from paying a class-booking marketplace?",
         "A marketplace shows a newcomer ten studios at once and takes a cut of a sign-up that could have been yours directly, and it stops the day you stop paying. A website you own captures students that are yours alone, with no cut taken, and keeps working long after it is built."),
        ("Do I need a page for every style and neighborhood?",
         "You start with the ones that matter most: your top styles or classes and your core areas. We build those pages first, around what people actually search and what you most want to fill, then expand, rather than spreading thin across everything at once."),
        ("Most of my new students come from Instagram. Does a website even help?",
         "Yes, because social is where they first notice you, not where they finally decide. A clip catches the eye, but a newcomer checks your site, your schedule, and your reviews before they commit to a first class, and that is where a fast, welcoming, schedule-forward page with easy intro-offer booking turns a curious scroll into a booked mat."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms build more slowly and compound over the months that follow. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-salon-spa-fitness.html", "Everything Top Shelf does for yoga studios"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-yoga-studios.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own 'yoga near me' in <em>your own town</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and class-booking apps taking your students, whether you work with us or not. No credit card, never a call center.",
},
]
