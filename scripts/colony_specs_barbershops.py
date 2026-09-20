"""Colony page specs for BARBERSHOPS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a barbershop owner would search, answered directly up top (the 40-60
word AEO answer), then two body sections, then a "the fix" bridge that funnels the page's
authority into the ONE money page the question implies. Lighter than a money page.

Salon, Spa & Fitness hub, shared with the hair-salon, nail-salon, and massage colonies. This file
must stay clearly distinct from the HAIR SALON one. Where a hair salon rebooks a five-to-six-week
color appointment built around a named stylist, color formulas, and Instagram color reveals, a
barbershop runs on a much tighter two-to-four-week cut cadence (a fade grows out fast, a lineup
faster), on a live mix of walk-ins and appointments, on booth-rent barbers who each keep their own
book and their own following so a man asks for one chair by name, on fast turnover, and on
years-long loyalty to a single barber. The recurring "am I open, how long is the wait, can I get in
with my barber" call is the engine, and a barber mid-fade cannot stop to answer it. So every dict
here is written around the walk-in call, the walk-in wait, booking a specific barber by name, the
short rebook cadence, winning back a lapsed regular, and men who pick a shop on proximity and vibe.
Never the six-week color rebook, the formula card, or the stylist model.

Same honesty rules as the money specs: no invented stats, percentages, prices, or clients; hedge
instead of overpromise; only the real Top Shelf prices ($299 and $899 monthly plans, $1,500
one-time site) ever appear, the Signature plan at $899 carries the CRM and the AI receptionist, and
the shop's own cut, fade, and beard pricing always stays generic with no numbers; no em or en dashes
anywhere; never "leak" as a metaphor. ETHICS: the AI receptionist does scheduling and intake ONLY,
it answers, reads the wait, books the right chair, and hands anything that needs the owner's call to
the owner; it never gives advice or promises a result.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 barbershop-website-cost              (cost)     -> websites-seo-for-barbershops
  2 barbershop-answering-service-cost    (cost)     -> ai-receptionist-for-barbershops
  3 is-a-crm-worth-it-for-a-barbershop   (cost)     -> crm-for-barbershops
  4 why-barbershops-miss-calls           (problem)  -> ai-receptionist-for-barbershops
  5 why-barbershop-clients-dont-rebook   (problem)  -> crm-for-barbershops
  6 how-do-barbershops-get-more-clients  (how-to)   -> marketing-for-barbershops
"""

TOPICS = [
# ==================== How Much Does a Barbershop Website Cost? (cost -> websites-seo) ====================
{
    "slug": "barbershop-website-cost",
    "h1": "How Much Does a Barbershop Website Cost?",
    "title": "How Much Does a Barbershop Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A barbershop website ranges from a cheap template to several thousand for a custom build. What matters is whether it fills the chair. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A barbershop website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more is whether it ranks for barber near me, shows the walk-in wait, and books a specific barber in one tap. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a barbershop site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barbershop website has a narrower job than most, and it is worth knowing that job before you look at any price. A man who needs a cut is on his phone, usually the same day, and he wants three things answered in seconds: are you open, how long is the wait, and can he get in with his barber. A site that loads slow, buries the hours, or makes him call to learn the wait, when every barber is mid-fade and cannot pick up, is a site he backs out of for the next shop on the map. So the site is not a brochure, it is the front door a man walks through when the phone cannot be answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That means a few things a generic template rarely does. It has to rank for the short local searches men actually type, barbershop near me, barber near me, a fade or a beard trim in your neighborhood. It has to put real cut photos and honest reviews up front, because a man is deciding whether you cut hair the way he wears it. And because a barbershop is often a room of booth-rent barbers who each keep their own following, it should let a regular book his specific chair by name in one tap while a first-timer grabs the next open one. A site built around that fills chairs. A pretty one that hides the booking and the wait does not.</p>'},
        {"h2_html": "What that costs, and what you should <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number swings widely because a cheap template you fill in yourself and a custom site built to rank and book are different products with the same name. A do-it-yourself builder is cheap by the month, but you do the work and it rarely ranks or turns a searching man into a booked chair. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody handles the ongoing SEO that gets it found. The bar in this trade is low, since a lot of shops never build a real site at all and lean on a listing or a feed, so the ground for your own name and neighborhoods is often wide open to whoever claims it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that fills the chair",
    "bridge_text": "A barbershop website is only worth the chairs it fills. Ours ranks for the men searching near you, shows whether you are open and the walk-in wait, and lets a regular book his barber in one tap.",
    "bridge_slug": "websites-seo-for-barbershops",
    "bridge_label": "Websites & SEO for barbershops",
    "faqs": [
        ("Is a cheap template site good enough for a barbershop to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks for barber near me, shows the walk-in wait, or lets a man book a specific barber, and you do the upkeep. A site that does not get found or turn a searching man into a booked chair is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ What Does a Barbershop Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "barbershop-answering-service-cost",
    "h1": "What Does a Barbershop Answering Service Cost?",
    "title": "What Does a Barbershop Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for barbershops often bill per call or per minute, which adds up on a busy Saturday. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services usually bill per call, per minute, or a monthly retainer, so a busy Saturday runs up the bill fast. Top Shelf takes a different approach: an AI receptionist that answers every call, reads the walk-in wait, and books the chair comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good Saturday turns into a big bill. A barbershop also gets its heaviest run of calls at exactly the times a live service charges most, the packed weekend, the after-school rush, the stretch before a holiday, when every barber is already mid-fade and the phone will not stop. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy Saturday or a run of "you guys open" questions runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs more than a quick answer would.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when the shop is slammed.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a man in his truck deciding where to get a cut does not leave a voicemail, he calls the next shop on the map and drives there. The real cost of a missed call is not a monthly fee, it is the walk-in who sat in another chair twenty minutes later, and often a regular who would have come back every couple of weeks for years. But a generic call center reading a script cannot tell him the wait, cannot say whether you take walk-ins, and does not know half your barbers keep their own books, so you can pay for coverage and still lose the chair.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, gives an honest read on the wait, and books the man with the barber he asks for by name or points him to the shortest open chair. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One walk-in it books instead of losing, turned into a regular on the short cut cadence, can be worth well more than the plan costs, and everything it catches after that is on top. It sticks to scheduling and intake, and hands anything that needs your call, a big group before a wedding, a straight-razor booking you want to place yourself, straight to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, tells a man the walk-in wait, and books his barber, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-barbershops",
    "bridge_label": "AI receptionist for barbershops",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when your Saturday is packed, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the walk-in it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or the Saturday rush?",
         "No. It answers around the clock as part of the plan, including the packed Saturday and the man checking at nine at night whether you open tomorrow, with no after-hours surcharge or overage.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============== Is a CRM Worth It for a Barbershop? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-barbershop",
    "h1": "Is a CRM Worth It for a Barbershop?",
    "title": "Is a CRM Worth It for a Barbershop? | Top Shelf Business Solutions",
    "meta_desc": "For most barbershops a CRM pays for itself by rebooking regulars on the tight cut cadence and winning back the ones who drifted. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most barbershops, yes. A CRM pays for itself the first time it rebooks a regular whose fade is growing out, or brings back one who drifted off the rotation. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a barbershop when you have more regulars than one barber can keep straight in his head, which is most shops, and especially a room of booth-rent barbers each carrying his own book. It is not worth it if you are a single chair cutting a handful of men a week and genuinely texting each one when he is due, though that rarely stays true as the book grows. The honest test is simple: how many regulars are overdue for a cut on the two to three week rhythm a fade runs on, and how many have not been in for a couple of months? Those are the chairs a CRM is built to refill.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The tight cadence is what makes it pay in a barbershop specifically. Because a fade looks grown out in two to three weeks and a lineup faster, a regular who slips even a little is already overdue, and it does not take long for a couple of missed cuts to turn into months gone and a man sitting in whatever chair was convenient. A trade with a six-week rhythm can coast on memory longer; a barbershop cannot.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a barbershop is not the software, it is the standing revenue that stops slipping. A regular growing out his fade, a man who has drifted for a couple of months, a standing every-other-Friday slot: each one is a chair you have already earned and are one timely nudge away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It sends the rebooking nudge on the short cadence a cut runs on, so regulars come back around without anyone at the desk tracking dates.</li><li>It holds and confirms standing slots, the every-other-week kind, so a man who wants the same time forever actually keeps it.</li><li>It keeps every client tied to his barber, with his usual cut, guard numbers, and beard preference in one place instead of one barber\'s memory and a stack of cards.</li><li>It tracks loyalty punch cards and prepaid packages against the right client, so the man one cut from a free one comes in to claim it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: rebook one regular you would have lost off the rotation and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your book of regulars to work",
    "bridge_text": "The regulars you already cut are the easiest chairs to fill. A CRM rebooks each one on the cadence his cut needs, so he comes back to your chair instead of whatever shop is convenient when his fade grows out.",
    "bridge_slug": "crm-for-barbershops",
    "bridge_label": "CRM for barbershops",
    "faqs": [
        ("Is a CRM overkill for a small barbershop?",
         "Not usually. Even a two or three chair shop cuts more regulars than anyone can track by memory, especially when each barber keeps his own book. The point is not size, it is whether rebooking is falling through on the short cadence a fade runs on. If regulars go overdue and drift off, a CRM earns its keep."),
        ("How is a CRM different from a barber keeping regulars in his phone?",
         "A phone full of numbers does not nudge a rebook, does not remember guard numbers or who is overdue, and does not win back a regular who has gone quiet. A CRM does all of that on the cadence, and in a booth-rent shop each barber keeps his own book inside it, so a regular stays tied to his chair.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Do Barbershops Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-barbershops-miss-calls",
    "h1": "Why Do Barbershops Miss So Many Calls?",
    "title": "Why Do Barbershops Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Barbershops miss calls because they ring while every barber is mid-fade, and a man checking the wait will not leave a voicemail, he drives to the shop that answered.",
    "answer": "Barbershops miss calls because they come while every barber is mid-fade with clippers in hand and a client in the chair, and a man calling to check the wait will not leave a voicemail. He drives to the next shop that picks up. The fix is not cutting faster, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The phone rings when every barber is <em>heads-down</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A barbershop is a hands-full trade. When the phone rings a barber is halfway through a fade with clippers in one hand and a man in the chair, and he is not going to stop a lineup and make the next client wait to take a call. The busier the shop is, the more calls ring out, which means your best Saturdays are also the ones where the most chairs slip away. It is not a discipline problem. A barber cannot cut the head in front of him and answer the phone at the same time, and most shops do not have a spare hand at a desk to do it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a walk-in it is not one. A man deciding where to get a cut is usually already in his truck, and he is not going to leave a message and sit waiting for a callback. He moves down the map until someone answers live, tells him the wait, and says come on in. By the time you check the phone between cuts, he has been sitting in another chair for twenty minutes.</p>'},
        {"h2_html": "Those missed calls are booked chairs, not <em>nuisances</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Almost every call to a barbershop is one of three questions, and all three are money. Are you open right now. How long is the wait if I come in. Can I get in with a specific barber, because a lot of men will only sit in one chair. Miss those and you are not missing a nuisance, you are missing a booked chair, and often a regular who would have come back every couple of weeks for years on the short cut cadence.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and can handle those three questions the way a sharp front desk would. A voicemail box cannot read the wait, and a generic call center does not know your hours, whether you take walk-ins, or that half your barbers keep their own books. What actually works is something that picks up on the first ring, gives an honest read on the wait, tells him whether to come now or grab a chair for later, and books him with the barber he asks for, all without a barber putting down the clippers. It sticks to scheduling and intake and hands anything that needs your judgment to you, so the call never rolls to voicemail in the first place.</p>'}],
    "bridge_h2": "Stop losing walk-ins to voicemail",
    "bridge_text": "An AI receptionist answers every call the second it rings, tells a man the wait honestly, and books him with the barber he asks for, so the walk-in never rolls to voicemail while your barbers cut.",
    "bridge_slug": "ai-receptionist-for-barbershops",
    "bridge_label": "AI receptionist for barbershops",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "What a man calling a barbershop wants most is to know he can get in, what the wait is, and that a real shop has him down, and a straight answer that books him beats a voicemail box every time. The AI receptionist is upfront about what it is, reads the wait, books the chair, and hands anything that needs your call to you."),
        ("Can I just let calls go to voicemail and call back between cuts?",
         "A walk-in will not wait for it. By the time you finish the fade in your chair and check the phone, the man who called is already sitting in another shop. Something that always answers and gives the wait catches the call a callback would have lost.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ Why Don't My Barbershop Clients Rebook? (problem -> crm) ============
{
    "slug": "why-barbershop-clients-dont-rebook",
    "h1": "Why Don't My Barbershop Clients Rebook?",
    "title": "Why Don't My Barbershop Clients Rebook? | Top Shelf Business Solutions",
    "meta_desc": "Most barbershop regulars do not rebook because they head out the door and back to their day, not because they were unhappy. On a two to four week cadence, drift happens fast.",
    "answer": "Most barbershop clients do not rebook because they head out the door and back to their day without booking the next cut, not because they were unhappy. On a two to four week cadence a couple of missed cuts turns into months gone fast, and a man ends up in whatever chair is convenient when his fade finally bothers him.",
    "sections": [
        {"h2_html": "Walking out without the next cut booked is the <em>quiet loss</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most barbershops the problem is not filling a chair once, it is keeping a man on the tight rhythm his cut needs. A fade or a tapered cut starts looking grown out in about two to three weeks, a lineup even faster, so a man who cares how he looks is a standing appointment every couple of weeks for as long as he keeps coming. But he usually walks out without booking the next one, the way most men do when they are already late getting back to work, and it is easy to read that as normal rather than as a loss.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It is a loss, though, because that chair time does not disappear. It sits empty or a walk-in fills it, and the steady every-two-weeks revenue that man represented walks out the door with him. Worse, the short cadence works against you: he is overdue within weeks, and once his fade gets shaggy he is just as likely to drop into whatever shop is close and open that day as to drive back to you. The rebook that keeps him yours is the one nobody had time to ask for on his way out.</p>'},
        {"h2_html": "Why the rebook <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Barbers do not skip the rebook because they are lazy. They skip it because the chair is always full. You finish a fade, wave in the next man, keep the lineup moving, and there is no one at a desk to catch each client on the way out and get the next cut on the calendar. Leaving it to memory means it only happens on a slow week, which is exactly when you have the fewest regulars due.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which regulars are coming due on the short fade cadence and which have already slipped past it.</li><li>The rebook depends on the man remembering to call, so it competes with his day and loses.</li><li>By the time anyone would reach out, his fade has grown out and he has been cut somewhere else.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every regular gets a friendly nudge timed to when his cut is growing out, written to sound like the shop, he books the next one before his hair bothers him and stays on the rotation. In a booth-rent shop each barber\'s regulars stay tied to his own book, so the right barber gets the rebook and the loyalty stays where it belongs.</p>'}],
    "bridge_h2": "Rebook every regular, automatically",
    "bridge_text": "A CRM keeps every regular and his barber in front of you and sends the rebook nudge itself, timed to when his cut grows out, so he books the next one instead of drifting to whatever chair is convenient.",
    "bridge_slug": "crm-for-barbershops",
    "bridge_label": "CRM for barbershops",
    "faqs": [
        ("How often should a barbershop nudge a regular to rebook?",
         "On the cadence his cut runs, which is short: roughly every two to three weeks for a fade, faster for a lineup. A single light, well-timed text right as it is growing out catches most of the ones who simply forgot, without being pushy. The point is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does an automatic rebook text feel impersonal?",
         "Not when it is written to sound like the shop and timed sensibly. A short reminder right as his fade grows out reads as helpful, not spammy, because most men meant to come back and just got busy. You can always jump in and message anyone directly too.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
# ============ How Do Barbershops Get More Clients? (how-to -> marketing) ============
{
    "slug": "how-do-barbershops-get-more-clients",
    "h1": "How Do Barbershops Get More Clients?",
    "title": "How Do Barbershops Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Barbershops get more clients by being the close, active, well-reviewed shop with fresh-cut photos a man finds the minute he searches, on Google and Instagram, not by clever ads.",
    "answer": "Barbershops get more clients by being easy to find and obviously good the minute a man searches, on Google and Instagram. He picks a shop that is close, open, and looks like his kind of place in under a minute. Keeping your profile active, well reviewed, and full of real cuts is what wins that decision.",
    "sections": [
        {"h2_html": "Men pick a barber by who is <em>close and looks right</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A man choosing a barbershop does not agonize over it. He searches, glances at the map, and picks a shop that is close, open, and looks like his kind of place with cuts that match how he wears his hair. That whole decision happens on a phone in under a minute, usually the day he needs a cut, and it turns on two things: are you near him, and do you look like you cut hair the way he wants it. So the whole game for a barbershop is being easy to find and obviously good in the exact spot a man looks, not clever ads aimed at people who are not thinking about their hair yet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">When someone searches for a barbershop near them, the first thing Google shows is the map pack, the little map with three local listings, star ratings, and a call button. Most men pick from those three without scrolling to the regular results below. It is where he settles the practical questions at a glance, are you open now, do you take walk-ins, do you cut the style he wants, is it his kind of shop. Show up there looking busy and current and the walk-in is usually yours; show a dead profile and he picks the shop that looked alive, no matter how sharp your barbers actually are.</p>'},
        {"h2_html": "Get found on Google, then show the <em>work</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more clients runs on two places a man actually looks, and it is less a clever trick than doing the simple things steadily. The first is your Google Business Profile, and the levers on it are plain, not mysterious.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Verify and complete the profile, with the right hours, service area, and whether you take walk-ins, so it does not look like a shop that might not be open.</li><li>Keep a steady flow of recent, genuine reviews, since they lift you in local search and tell the next man whether the fade was clean and the wait was honest.</li><li>Post fresh cut photos and updates, so the profile reads as an active shop instead of a stale one.</li><li>Reply to the reviews that land, because responding is itself a signal that helps your local ranking.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The second is a visual feed, which for a barbershop is the portfolio and the vibe check in one. A man scrolls to see the fades, the lineups, and the beard work before he trusts a stranger near his head, and a lot of men follow a barber, not just a shop, so featuring each chair lets a new client find the barber whose work he likes and ask for him. This is the public-facing side aimed at men who are not your regulars yet; the private follow-up to the men already in your book is the CRM. What no one can honestly promise is a specific spot on the map, because Google decides that, but a free audit can show you where you stand today.</p>'}],
    "bridge_h2": "Be the shop they can already see",
    "bridge_text": "Most men pick a barber from the map and a quick scroll of the work. Keeping your Google profile active and full of recent cuts and reviews is how you become the close, trusted shop he walks into.",
    "bridge_slug": "marketing-for-barbershops",
    "bridge_label": "Marketing for barbershops",
    "faqs": [
        ("What is the fastest way to get more barbershop clients?",
         "Get your Google Business Profile verified, complete, and well reviewed, because the map pack is where a man actually decides. A neglected profile can start climbing within a few weeks once it is active, and it compounds as reviews and cut photos build. No one controls Google, so no honest company promises a specific spot, but those are the levers that move it."),
        ("Do I need to run ads to get more clients?",
         "Usually not first. Most barbershop clients come from a man searching nearby and picking from the map and your photos, so a complete, active, well-reviewed profile and a steady feed of real cuts does more than ads aimed at people who are not thinking about a cut yet. Get those working before you spend on ads.")],
    "trade_slug": "barbershops", "trade_plural": "barbershops",
    "hub_name": "Salon, Spa & Fitness", "hub_slug": "industry-salon-spa-fitness.html",
},
]
