"""Colony page specs for YOGA STUDIOS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a yoga studio owner would search, answered directly up top (the 40-60
word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

A YOGA STUDIO is CLASS-based: it runs a schedule of group classes, converts newcomers with an
INTRO OFFER (a free first class, an intro week or month), then lives on class packs, memberships,
retention, and the win-back of students who drifted, with workshops and teacher training as the
higher-ticket upsell sold to the community it already built. Every dict here owns UNIQUE,
hand-written, yoga-studio-specific substance (the generator owns shell, schema, events, keyword
placement): teachers on the mat while the phone rings out, "which class do I start with / how does
the intro offer work / do you rent mats" inquiries and late-night DMs, filling capped classes and
handling waitlists and cancellations, the intro-offer-to-membership funnel, and lapsed-student
win-back. This is NOT a gym facility membership (equipment, 24/7 access) and NOT a 1:1 personal
trainer's per-session coaching; do not write it as either.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real Top Shelf prices ($299/$899 plans, $1,500 one-time site) ever appear,
and the studio's OWN intro, class-pack, and membership pricing stays generic with no numbers so it
is never confused with Top Shelf pricing; no em or en dashes anywhere; never "leak" as a metaphor;
illustrative scenarios only, no named clients or competitors. ETHICS: the AI receptionist does
scheduling and intake ONLY, never advice, and nothing here promises a health, fitness, or wellness
outcome of any kind.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 yoga-studio-website-cost              (cost)     -> websites-seo-for-yoga-studios
  2 yoga-studio-answering-service-cost    (cost)     -> ai-receptionist-for-yoga-studios
  3 is-a-crm-worth-it-for-a-yoga-studio   (cost)     -> crm-for-yoga-studios
  4 why-yoga-studios-miss-calls           (problem)  -> ai-receptionist-for-yoga-studios
  5 why-yoga-students-dont-return         (problem)  -> crm-for-yoga-studios
  6 how-do-yoga-studios-get-more-students (how-to)   -> marketing-for-yoga-studios
"""

TOPICS = [
# ==================== How Much Does a Yoga Studio Website Cost? (cost -> websites-seo) ====================
{
    "slug": "yoga-studio-website-cost",
    "h1": "How Much Does a Yoga Studio Website Cost?",
    "title": "How Much Does a Yoga Studio Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A yoga studio website ranges from a cheap template to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A yoga studio website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more is whether it shows your class schedule and intro offer and books a first class in one tap. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a yoga studio website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For a yoga studio the website has one real job, and it is not to look pretty. A newcomer who has finally worked up the nerve to try a class lands on your site from a search or your profile, and within seconds she is deciding whether this looks like a place for someone like her and whether there is a class that fits both her schedule and her level. So the class schedule is the product. It has to be the first thing she sees, not buried three taps deep the way a class-booking app tends to bury it. The intro offer, a free first class or an intro month, belongs right next to it with one clear button to claim it, because every extra step between the impulse and the booking is one more chance to close the tab.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site also has to be found in the first place, ranking for what she actually types, yoga near me, yoga classes, beginner yoga, or a style you teach, and it has to load fast on the phone she is holding late at night. Judge a quote by whether the site does those things: shows the schedule, makes the intro offer obvious, books a first class in a tap, and ranks for the searches that bring new students. A studio with a genuinely good practice and a slow, schedule-hiding website loses newcomers it never even hears about.</p>'},
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once you know what the site has to do, the range of quotes makes more sense, because you are not all buying the same thing. A do-it-yourself builder is cheap each month, but you do the work and it rarely ranks or reads as welcoming to a first-timer. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is handling the ongoing SEO that gets it found. An agency plan bundles the build with that ongoing SEO and the booking and follow-up behind it, which is where most of the lasting value lives, and also where the monthly cost lives. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that fills your classes",
    "bridge_text": "A yoga studio website is only worth the students it books. Ours is built to rank for the classes and areas you serve, put your schedule and intro offer front and center, and turn a late-night search into a booked first class.",
    "bridge_slug": "websites-seo-for-yoga-studios",
    "bridge_label": "Websites & SEO for yoga studios",
    "faqs": [
        ("Is a cheap template site good enough for a yoga studio to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks for the searches new students make or reads as welcoming to a nervous first-timer, and you do the upkeep. If the site hides your schedule or makes booking a first class hard, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ What Does a Yoga Studio Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "yoga-studio-answering-service-cost",
    "h1": "What Does a Yoga Studio Answering Service Cost?",
    "title": "What Does a Yoga Studio Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for yoga studios often bill per call or minute, which adds up. Top Shelf includes an AI receptionist that answers 24/7 in the $899 Signature plan.",
    "answer": "Traditional answering services for yoga studios usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call and DM and books the intro offer comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A yoga studio also gets a lot of its inquiries at the worst times for a live service to be cheap: evenings and weekends, when someone finally decides this is the week they start, and by text or social message rather than a call. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of quick questions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a nervous first-timer with a lot of questions costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands, and many live services do not answer a text or a DM at all.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a newcomer trying to figure out how to start will not leave a voicemail, she books the studio that picked up or the app that replied. The real cost of no coverage is not a monthly fee, it is the membership that never began because a first class was never booked. But a generic call center reading a script cannot tell a nervous beginner which class to start with, explain how your intro offer works, or say whether you rent mats, so you can pay for coverage and still lose the newcomer.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers calls, texts, and DMs around the clock, sounds warm rather than rushed, answers the beginner questions, and books the intro offer or a first class straight onto your schedule. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One new student it books while you are teaching, and everything it catches after that, can be worth well more than the plan costs. It does scheduling and intake only, never advice, and it hands anything that needs a person, a membership freeze or a billing question, straight to your team.</p>'}],
    "bridge_h2": "Answer every inquiry without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers calls, texts, and DMs 24/7, explains the intro offer and which class fits a beginner, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-yoga-studios",
    "bridge_label": "AI receptionist for yoga studios",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the new student it books instead of losing to voicemail while your teachers are on the mat."),
        ("Does it cost extra to answer texts and DMs after hours?",
         "No. It answers calls, texts, and social messages around the clock as part of the plan, including the Sunday-night message from someone deciding to finally try a class, with no after-hours surcharge or overage.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============== Is a CRM Worth It for a Yoga Studio? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-yoga-studio",
    "h1": "Is a CRM Worth It for a Yoga Studio?",
    "title": "Is a CRM Worth It for a Yoga Studio? | Top Shelf Business Solutions",
    "meta_desc": "For most yoga studios a CRM pays for itself by converting one intro offer or winning back a drifted student. It comes in Top Shelf's $899 Signature plan.",
    "answer": "For most yoga studios, yes. A CRM pays for itself the first time it converts an intro offer that would have quietly expired, or brings back a student who drifted away. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a yoga studio when you have more intro-offer sign-ups, members, and past students than you can personally keep track of, which is most studios past the first year. It is not worth it if you are a single teacher with a handful of regulars you genuinely stay in touch with, though that rarely stays true as the roster grows. The honest test is simple: how many intro offers ran out last month without anyone reaching out, and how many students who used to come regularly have not been on the mat in months? The same goes for the class packs students prepaid and never finished, and the regulars who would fill a workshop or a teacher training if anyone thought to reach out. Those are the students a CRM is built to recover, and they are far warmer than any stranger a new-student push would reach.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a studio is not the software, it is the work that stops slipping through. A first-timer sitting on an intro offer, a member who quietly went quiet, a class pack running low, a regular who once mentioned being curious about a training: each is revenue you have already half-earned and are one timely message away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every intro offer on a schedule, timed to the window before it expires, so a newcomer on the fence keeps hearing from you while the other studios go quiet.</li><li>It onboards new members over their first weeks and flags the students who have not been in lately, so you can reach a quiet one before she becomes a cancellation.</li><li>It reminds students to use a class pack before it lapses, and reaches the right regulars about a workshop or teacher training so the higher-ticket seats fill from the community you already built.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: convert one intro offer or bring back one drifted student and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your student list to work",
    "bridge_text": "The intro offers and past students you already have are the cheapest way to fill a class. A CRM follows up on every one for you, so a first-timer converts and a drifted student comes back instead of drifting to the studio down the street.",
    "bridge_slug": "crm-for-yoga-studios",
    "bridge_label": "CRM for yoga studios",
    "faqs": [
        ("Is a CRM overkill for a small yoga studio?",
         "Not usually. Even a small studio signs more intro offers and serves more students than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If intro offers expire unworked and past students forget your name, a CRM earns its keep."),
        ("How is a CRM different from my class-booking app?",
         "A booking app takes reservations, but it rarely follows up on an intro offer before it expires, flags a member who has gone quiet, or reaches out to win a lapsed student back. A CRM does all of that on a schedule, and every student stays yours and exportable rather than locked inside software you only rent.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Do Yoga Studios Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-yoga-studios-miss-calls",
    "h1": "Why Do Yoga Studios Miss So Many Calls?",
    "title": "Why Do Yoga Studios Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Yoga studios miss calls because teachers are on the mat and the desk is empty, and a nervous newcomer will not leave a voicemail. She books the studio that answered.",
    "answer": "Yoga studios miss calls because they come while your teachers are on the mat leading a class and no one is free at the desk, and a nervous newcomer will not leave a voicemail. She books the studio that answered, or the app that replied. The fix is not teaching less, it is making sure every call and DM gets answered.",
    "sections": [
        {"h2_html": "The call comes while your teachers are <em>on the mat</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A yoga class runs sixty, seventy-five, or ninety minutes with no break to step out for a ringing phone, so during a class the phone is silenced and nobody is at the desk to pick it up. Plenty of studios run lean, with a teacher who is also the front desk, so a call that lands mid-class simply goes unanswered by anyone. The busier your schedule, the more inquiries you miss, which means your fullest weeks are also the ones where the most new students slip away. It is not a discipline problem. One person cannot lead the room in front of them and answer the phone at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a newcomer it is not one. Someone working up the nerve to try a first class will not leave a message and wait for a callback tomorrow. She moves down the map until a person answers or an online booking replies. And much of the interest never comes as a call at all: a class clip catches someone mid-scroll and she sends a DM, or a friend talks her into going and she texts once the studio is already dark. If that message sits until a teacher finishes the last class, the resolve has cooled and she has booked somewhere that replied.</p>'},
        {"h2_html": "A missed newcomer is a missed <em>membership</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed first-timer is not one lost drop-in, because a studio lives on turning that first visit into a membership, so the inquiry you let roll to voicemail is a whole membership that never got the chance to begin. Those are also the ones most likely to be missed, since a beginner is exactly the person who reaches out at night or by DM, when the studio is closed or the class is full and no one is watching the phone.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can handle a newcomer the way an attentive front desk would. A voicemail box cannot explain the intro offer, and a generic call center does not know your schedule or which class is safe for a beginner to start with. What actually works is something that answers calls, texts, and DMs on the first ring day or night, sounds warm rather than rushed, answers the beginner questions, points to a class on the schedule that fits, and books the intro offer, so the newcomer is on your calendar instead of the studio that happened to be free when the phone rang.</p>'}],
    "bridge_h2": "Stop losing new students to voicemail",
    "bridge_text": "An AI receptionist answers every call, text, and DM on the first ring, day or night, explains the intro offer and which class suits a beginner, and books it, so the newcomer never rolls to voicemail while you teach.",
    "bridge_slug": "ai-receptionist-for-yoga-studios",
    "bridge_label": "AI receptionist for yoga studios",
    "faqs": [
        ("Would a new student rather reach a real person?",
         "What a nervous first-timer needs most is a warm, quick reply that tells her she can get in, which class to start with, and that a real studio has her booked, and that beats a voicemail box every time. The AI receptionist is upfront about what it is, answers the beginner questions, and hands anything that needs a person to your team."),
        ("Can I just forward the studio line to my cell instead?",
         "You can, but that only helps when your hands are free, and they are not while you are leading a class. Forwarding still rolls to voicemail mid-class, and it does nothing for the texts and DMs new students actually send. Something that always answers and books is what catches the inquiries a forward would still miss.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Don't My Yoga Students Come Back? (problem -> crm) ============
{
    "slug": "why-yoga-students-dont-return",
    "h1": "Why Don't My Yoga Students Come Back?",
    "title": "Why Don't My Yoga Students Come Back? | Top Shelf Business Solutions",
    "meta_desc": "Most yoga students who do not return were never followed up with. The intro offer expired or a member drifted off, and no one reached out before the habit faded.",
    "answer": "Most yoga students who do not come back were not unhappy, they were never followed up with. The intro offer quietly expired, or a member got busy and drifted off, and nobody reached out while the habit was still forming. A student who stops coming is usually a maybe that faded, not a firm no.",
    "sections": [
        {"h2_html": "A student who drifts off was rarely <em>unhappy</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a student who did not return as someone who did not like the class, so you let it go and move on. But most of the time she did not decide against you at all. She claimed the intro offer, came to a class or two, fully meant to sign up, and then the intro period quietly ended with nobody reaching out. Or she was a regular who got busy for a few weeks, the routine broke, and she kept meaning to come back. Neither of them chose the studio down the street. They just needed a friendly nudge while the habit was still fresh, and a nudge is exactly what slips when your teachers are leading classes all day.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The studio that keeps her is usually not the cheapest or the closest. It is the one that stayed in front of her: a warm note a day or two after the first class, a gentle reminder before the intro offer runs out, a check-in when she has not been in for a while. That second touch is what turns a first class into a membership and a quiet stretch back into a routine, and it is exactly the thing there is no time for between classes.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Studio owners do not skip follow-up because they are lazy. They skip it because the day fills with classes to teach and a room to run. You finish teaching, set up the next class, handle the member with a question at the desk, and by evening the first-timer from Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest new students to keep.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which intro offers are about to expire or which students have quietly stopped coming.</li><li>The follow-up depends on someone remembering, so it competes with teaching the room and loses.</li><li>By the time anyone circles back, the intro window has closed or the routine has fully broken.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and then it just runs. When every intro offer gets a couple of timed check-ins automatically, written to sound like you, and every quiet student gets a warm reason to come back before she is gone for good, the first-timers convert and the regulars stay, without a single reminder written by hand.</p>'}],
    "bridge_h2": "Follow up on every student, automatically",
    "bridge_text": "A CRM keeps every intro offer and every student in front of you and sends timed, personal check-ins for you, so a first-timer converts before the offer expires and a quiet student comes back before she is gone for good.",
    "bridge_slug": "crm-for-yoga-studios",
    "bridge_label": "CRM for yoga studios",
    "faqs": [
        ("How soon should I follow up with a new yoga student?",
         "A friendly note a day or two after the first class, while the experience is fresh, then a gentle reminder before the intro offer expires, catches most of the maybes without being pushy. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, warm check-in reads as a studio that noticed she came, not as spam, and most newcomers appreciate the nudge because they meant to come back and life got busy. You can always jump in and message anyone directly.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ======== How Do Yoga Studios Get More Students? (how-to -> marketing) ========
{
    "slug": "how-do-yoga-studios-get-more-students",
    "h1": "How Do Yoga Studios Get More Students?",
    "title": "How Do Yoga Studios Get More Students? | Top Shelf Business Solutions",
    "meta_desc": "Yoga studios get more students by being easy to find and obviously welcoming where beginners look, your Google Business Profile, the map pack, reviews, and social.",
    "answer": "Yoga studios get more students by being easy to find and plainly welcoming right where a beginner looks, your Google Business Profile, the map pack, reviews, and social, so when someone nearby searches for a yoga class, yours is the current, well-reviewed name they book instead of the studio that let its profile go stale.",
    "sections": [
        {"h2_html": "A beginner chooses a studio on trust and <em>welcome</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Trying yoga for the first time takes a little nerve. A lot of newcomers quietly worry that they will not be able to keep up, or that everyone else in the room will be far more advanced, so before they ever walk in they look you up, study the schedule, and read a handful of reviews to decide whether this feels like a place a beginner belongs. All of that plays out on a screen, inside a minute or two, well before anyone picks up the phone. So the whole task for a studio is to be easy to find, obviously current, and plainly welcoming right where a new student is already looking, rather than buying clever ads aimed at people who have no interest in yoga yet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Search for a yoga studio nearby, or for a beginner class or a specific style in your town, and the map pack, that trio of local listings carrying the star ratings, sits at the very top, ahead of the websites and even the ads. Get found, look active, and read as welcoming in that moment, and the booking is usually yours. Look neglected or invisible, and they book the studio that showed up looking current and glad to have a beginner, no matter how good your teachers actually are.</p>'},
        {"h2_html": "Show up, look active, and let real students <em>do the selling</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your Google Business Profile is the storefront a new student sees first. A listing left untouched for months, with a dim photo and hours that may or may not still be right, reads as a studio that might not even be open. One with a real photo of a class in progress, current hours, the styles you teach, and a steady stream of fresh reviews reads as an active studio with a real community, and it settles the practical questions at a glance: the schedule, whether there is an intro offer, which classes suit a beginner, whether you rent mats.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep the profile complete and current, with real photos of real classes, so a nervous first-timer can see before she calls that a beginner belongs there.</li><li>Ask happy students for honest reviews and reply to the ones that come in, since reviews both reassure the next reader and lift you in the map pack.</li><li>Keep social specific to your studio, a class clip or a schedule post, rather than staged stock photos, because that is usually where a newcomer first notices you.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">All of that is the public-facing side, aimed at people who are not students yet. The private, one-to-one follow-up with the people already on your roster is the CRM, and the two run as a pair. One rule keeps you honest: gather real reviews from real students and never buy them or filter out the unhappy ones.</p>'}],
    "bridge_h2": "Be the studio a beginner finds first",
    "bridge_text": "Keeping your Google profile active, your reviews steady, and your social full of real classes is how a nearby beginner finds you, trusts you, and books a first class instead of scrolling past to the studio that showed up looking current.",
    "bridge_slug": "marketing-for-yoga-studios",
    "bridge_label": "Marketing for yoga studios",
    "faqs": [
        ("What is the single best way to get more yoga students?",
         "For most studios it is a complete, active Google Business Profile with a steady flow of honest reviews, because the map pack is where nearby searches for a yoga class start. It costs nothing to keep current, and it puts you in front of beginners at the exact moment they are deciding where to go."),
        ("Do I need to run ads to get more students?",
         "Not to start. Most new students come from finding you on Google or social and trusting what they see, so getting your profile, reviews, and posts right usually moves the needle further than ad spend, and it keeps working without a meter running. Ads can come later, once the free groundwork is solid.")],
    "trade_slug": "yoga_studios", "trade_plural": "yoga studios",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
]
