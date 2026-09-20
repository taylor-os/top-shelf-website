"""Colony page specs for AUTO BODY SHOPS / collision repair (plan §5 "Problem/symptom"
colony + §6 link-sculpting). generate_colony.py loads every scripts/colony_specs_*.py and
reads TOPICS from each. A colony page is ONE real question an auto body shop owner would
search, answered directly up top (the 40-60 word AEO answer), then two body sections, then a
"the fix" bridge that funnels the page's authority into the ONE money page the question
implies. Lighter than a money page.

Each dict owns UNIQUE, hand-written, collision-specific substance (the generator owns shell,
schema, events, keyword placement). The angle is AUTO BODY / COLLISION, distinct from general
auto repair: a driver who just had a wreck or fender-bender, the insurance claim and estimate
process, "do you work with my insurance", rental and total-loss questions, the estimate-to-
scheduled-repair gap, and competing to be the shop chosen right after an accident.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear;
no em/en dashes anywhere; "find the gap", never "leak" as a money metaphor (a literal fluid leak
is fine). ETHICS: the AI does intake and scheduling only, it never quotes a repair or decides an
insurance claim; no repair-outcome or insurance guarantees; name no insurer as a client.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 auto-body-shop-website-cost              (cost)    -> websites-seo-for-auto-body-shops
  2 auto-body-answering-service-cost         (cost)    -> ai-receptionist-for-auto-body-shops
  3 is-a-crm-worth-it-for-an-auto-body-shop  (cost)    -> crm-for-auto-body-shops
  4 why-auto-body-shops-miss-calls           (problem) -> ai-receptionist-for-auto-body-shops
  5 why-auto-body-estimates-go-cold          (problem) -> crm-for-auto-body-shops
  6 how-do-auto-body-shops-get-more-customers(how-to)  -> marketing-for-auto-body-shops
"""

TOPICS = [
# ============ How Much Does an Auto Body Shop Website Cost? (cost -> websites-seo) ============
{
    "slug": "auto-body-shop-website-cost",
    "h1": "How Much Does an Auto Body Shop Website Cost?",
    "title": "How Much Does an Auto Body Shop Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An auto body shop website ranges from cheap templates to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An auto body shop website can run from a couple hundred dollars for a DIY template to several thousand for a custom build, but the price matters less than whether it does the collision job: letting a driver request an estimate, reassuring them you handle the insurance claim, and ranking for collision repair near me. Top Shelf builds one for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What an auto body shop website actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The moment that sends someone to your website is rarely a calm one. A driver just had a wreck or backed into a post, they are shaken, and they are searching on a phone for a shop that can fix it. Before they think about price they want to know three things: can this shop handle the damage, will they deal with the insurance claim, and are they any good. A body shop website earns its keep by answering those fast, so the number you pay matters far less than whether the site does that job.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>An estimate request that lets a driver describe the damage and send photos from their phone, so the conversation starts before they even call.</li><li>Plain reassurance that you handle the insurance claim, and that in most cases a driver can choose their own shop rather than only the one the insurer names.</li><li>Before and after photos of real repairs, because a nervous driver is trusting you with a car they need back on the road.</li><li>Built to rank and load fast for the searches people make after an accident, like collision repair near me and auto body shop near me, with a tap to call in reach the whole time.</li></ul>'},
        {"h2_html": "What that costs, and what you should <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A body shop website earns its money one way: it turns a driver searching after a wreck into an estimate on your schedule. That is worth keeping in mind when you compare quotes, because you are not all buying the same thing. A do-it-yourself builder is cheap each month, but you do the work and it is rarely built to rank or to reassure a rattled caller. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is doing the ongoing SEO to get it found. A plan bundles the build with the SEO and updates, which is where most of the long-term value lives.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you, and there is no setup fee either way. Before you sign anything, with anyone, ask who owns the site, what a change costs, and whether you keep it if you leave. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site built for the after-accident search",
    "bridge_text": "An auto body shop website is only worth what it brings in. Ours is built to rank for collision repair near me, reassure a driver about the claim, and turn the estimate request into a car on your schedule.",
    "bridge_slug": "websites-seo-for-auto-body-shops",
    "bridge_label": "Websites & SEO for auto body shops",
    "faqs": [
        ("Is a cheap template site good enough for a body shop to start with?",
         "It can get you online, but a template you fill in yourself is rarely built to rank for collision searches or to reassure a driver about the insurance claim, and you do the upkeep. If it is not getting found or turning an estimate request into a booked car, the low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. The one-time $1,500 site is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== What Does an Auto Body Shop Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "auto-body-answering-service-cost",
    "h1": "What Does an Auto Body Shop Answering Service Cost?",
    "title": "What Does an Auto Body Shop Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for auto body shops often bill per call or per minute. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for auto body shops usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call around the clock, gathers the vehicle and claim details, and books the estimate comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A body shop also gets its best calls at the worst moments for a live pickup: an after-accident driver, an adjuster calling back on a supplement, an estimate request, all landing while your crew is in the paint booth or on the frame machine. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of tire-kickers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a shaken caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a driver who just had a wreck does not leave a voicemail, they call the next shop. The real cost of no coverage is not a monthly fee, it is the collision job that went to whoever picked up. But a generic call center reading a script cannot take an adjuster callback properly, gather a claim number, or ask whether the car is drivable or needs a tow, so you can pay for coverage and still get a caller who was not really helped.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, gathers the insurer, claim number, and vehicle details, and books the estimate on your real schedule. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. It does intake and scheduling only: it explains the claim process in plain terms, but it never decides a claim or quotes the repair, and it hands anything that needs your judgment straight to you. One after-accident job you would have lost to voicemail can be worth well more than the plan costs, and everything it captures after that is on top.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers around the clock, gathers the claim and vehicle details, and books the estimate, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-auto-body-shops",
    "bridge_label": "AI receptionist for auto body shops",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-accident job it books instead of losing to voicemail."),
        ("Does it decide the insurance claim or quote the repair?",
         "No. It handles intake and scheduling only. It gathers the insurer, claim number, and vehicle details, explains the next step in plain terms, and books the estimate, then hands the claim decision and the actual estimate to you. It never quotes a repair or promises a claim outcome.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Is a CRM Worth It for an Auto Body Shop? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-an-auto-body-shop",
    "h1": "Is a CRM Worth It for an Auto Body Shop?",
    "title": "Is a CRM Worth It for an Auto Body Shop? | Top Shelf Business Solutions",
    "meta_desc": "For most body shops a CRM pays for itself by reviving one cold estimate and staying the shop past customers refer. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most auto body shops, yes. A CRM pays for itself the first time it revives a collision estimate a driver let sit while they waited on a claim, or brings a past customer back for the next repaint or fender-bender. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a body shop when you write more estimates and have served more customers than you can personally keep track of, which is most established shops. It is not worth it if you are a one-bay operation closing every estimate the day you write it, though that rarely stays true as you grow. The honest test is simple: how many estimates did you write last month that went quiet after the driver said they would check with their insurer, and how many past customers have not heard from you since their car left the lot. Those are the cars a CRM is built to recover.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Body work has a long repeat cycle, since a driver may only need real collision work every few years, so the value is less about frequency and more about not losing the estimates you already wrote and staying the name a happy customer refers. That is exactly the kind of follow-up that falls apart on a busy week and runs on its own once a system is doing it.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a body shop is not the software, it is the work that stops slipping through. A driver sitting on an estimate while a claim gets approved, a customer whose bumper you fixed two years ago, a happy customer who would refer you if reminded: each one is a car you have already half-earned and are one touch away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on a schedule, so a driver comparing shops keeps hearing from you while the other two go quiet.</li><li>It keeps you top of mind with past customers, so the next wreck, repaint, or hail season, and the friend they refer, come back to you.</li><li>It keeps every customer, vehicle, estimate, and repair photo in one place instead of a drawer of paper tickets and your memory.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one collision job you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your estimates and customer list to work",
    "bridge_text": "The estimates you already wrote and the customers you already served are the cheapest cars you can book. A CRM follows up on every one for you, so they come back to you instead of the shop that stayed in touch.",
    "bridge_slug": "crm-for-auto-body-shops",
    "bridge_label": "CRM for auto body shops",
    "faqs": [
        ("Body shop customers do not come back often. Is a CRM still worth it?",
         "That is exactly why it is worth it. When a driver only needs real collision work every few years, staying the name they remember and refer is the whole game. A CRM works your unconverted estimates and keeps you top of mind for the next wreck or repaint, instead of relying on repeat visits a body shop does not get."),
        ("How is a CRM different from my estimating system?",
         "Most estimating and management systems store the file but do not chase the work. A CRM follows up on cold estimates, nudges past customers, and tells you who has gone quiet, on a schedule, so the deferred and referral work actually shows up instead of depending on someone to remember.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Auto Body Shops Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-auto-body-shops-miss-calls",
    "h1": "Why Do Auto Body Shops Miss So Many Calls?",
    "title": "Why Do Auto Body Shops Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Auto body shops miss calls because the crew is in the booth or on a frame machine, and a driver who just had a wreck will not leave a voicemail. They call the next shop.",
    "answer": "Auto body shops miss calls because they ring while the crew is heads down in the paint booth, on the frame machine, or blocking a panel, and a driver who just had a wreck does not leave a voicemail. They hang up and call the next shop. The fix is not working harder, it is making sure every estimate and after-accident call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when the crew <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Body work is a hands-full, eyes-down trade. When the phone rings someone is masking for paint, matching color under the lights, on the frame machine, or spraying, and none of those are moments you can stop and take a call. The busier the shop, the more calls slip, which means your best weeks are also the ones where the most work gets away. It is not a discipline problem. A crew cannot do the repair in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a driver who just had a wreck it is not one. Someone who was just rear-ended wants to hear a calm voice tell them what to do next, not leave a message and wait. They move down the list until a shop answers, and by the time you check your phone the car is already at the shop down the road.</p>'},
        {"h2_html": "The calls you miss are your most <em>expensive misses</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. An after-accident call is high-value collision work, and it comes when the caller is most anxious and most likely to book the first shop that answers. Adjuster callbacks and estimate requests land mid-repair too. So the calls you are most likely to miss are also the ones worth the most, and letting them roll to voicemail is the quiet way a shop loses cars it never knew it had a shot at.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that answers every time and can handle a collision intake. A voicemail box cannot take an adjuster callback, and a generic call center does not know to ask whether the car is drivable or needs a tow, or to capture the claim number. What actually works is something that answers on the first ring day or night, gathers the vehicle and insurance details, and either books the estimate or flags it to your phone. It takes the intake and schedules the car; it does not decide the claim or quote the repair, so you never miss the call and you keep every judgment call that matters.</p>'}],
    "bridge_h2": "Stop losing wrecks to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, gathers the claim and vehicle details, and books the estimate or flags it to you, so the after-accident call never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-auto-body-shops",
    "bridge_label": "AI receptionist for auto body shops",
    "faqs": [
        ("Would a driver rather reach a real person after an accident?",
         "After a wreck, what a driver needs most is to know a real shop is handling it, and a calm voice that captures the vehicle and claim details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands anything that needs your judgment straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are in the booth, on the frame machine, or with a customer at the counter. Something that always answers and takes the collision intake is what catches the calls a forward would still miss.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ============ Why Do Auto Body Estimates Go Cold? (problem -> crm) ============
{
    "slug": "why-auto-body-estimates-go-cold",
    "h1": "Why Do Auto Body Estimates Go Cold?",
    "title": "Why Do Auto Body Estimates Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most auto body estimates go cold not over price but because nobody followed up while the driver waited on a claim. The car goes to whoever checked back in.",
    "answer": "Most auto body estimates go cold not because your number was wrong, but because nobody followed up. The driver said they needed to check with their insurer, wait on the claim, or think it over, then the shop got busy and no one circled back. A quiet estimate is usually not a no, it is a maybe stuck between the accident and an approved claim.",
    "sections": [
        {"h2_html": "Silence usually means waiting, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet estimate as a no on price, so you drop it and move on. But most of the time the driver did not decide against you at all. They asked for an estimate on a dented door or a bumper, meant to move forward, and then got caught between the insurer, the claim, a rental, and a busy life. They collected two other estimates, and a week later they could not tell the three shops apart.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The gap between a written estimate and a scheduled repair is where collision work is won or lost. The shop that stays in front of the driver while the claim moves is the one that books the car, and it is usually not the lowest number, it is the one who checked back in. That second touch, a friendly note a few days later while the claim is still in motion, is exactly the thing there is never time for between cars in the booth.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Shops do not skip follow-up because they are lazy. They skip it because cars keep coming through the booth. You write the estimate, the next tow shows up, an adjuster calls, and by the end of the week the estimate you wrote Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest estimates to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which estimates are still open and going cold while a claim is pending.</li><li>The follow-up depends on you remembering, so it competes with the cars on the floor and loses.</li><li>By the time you circle back, the claim was approved and the driver already booked the shop that stayed in touch.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open estimate gets a couple of timed check-ins automatically, written to sound like your shop, the driver waiting on a claim keeps hearing from you while the other shops go silent, and the collision work you already priced stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every estimate, automatically",
    "bridge_text": "A CRM keeps every open estimate in front of you and sends timed check-ins for you, so a driver waiting on a claim decision keeps hearing from you while the other shops go quiet, and the car comes back.",
    "bridge_slug": "crm-for-auto-body-shops",
    "bridge_label": "CRM for auto body shops",
    "faqs": [
        ("How many times should I follow up on a collision estimate?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the estimate, then a short note while the claim is still in motion. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your shop and sent at a sensible pace. A short, friendly check-in reads as attentive, not pushy, and a driver stuck waiting on a claim usually appreciates the nudge. You can always jump in and message anyone directly.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
# ======== How Do Auto Body Shops Get More Customers? (how-to -> marketing) ========
{
    "slug": "how-do-auto-body-shops-get-more-customers",
    "h1": "How Do Auto Body Shops Get More Customers?",
    "title": "How Do Auto Body Shops Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Auto body shops get more customers by being easy to find and choose right after an accident: the Google map pack, real reviews, and clear answers on insurance.",
    "answer": "Auto body shops get more customers by being the easy choice at the moment a driver needs one, right after an accident. That means showing up in the Google map pack for collision repair near me, having recent reviews a nervous driver trusts, and answering the questions they lead with, like whether you work with their insurance and how the estimate works.",
    "sections": [
        {"h2_html": "Drivers choose a shop the moment <em>after a wreck</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Unlike a lot of local work, body shop demand is event-driven. Nobody plans a collision. Someone gets in a wreck or a fender-bender and needs a shop now, they are not loyal to a name yet, they search on their phone, and they pick from the first few shops that look trustworthy and answer their questions. So getting more customers is really about being findable and convincing inside that narrow window right after the accident.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The questions a collision caller leads with are specific: do you work with my insurance, can I choose my own shop, how long will it take, will it look right after. Some shops have direct-repair relationships with insurers, and a driver often asks up front whether you work with theirs, so making that answer easy to find matters. The shop that answers those plainly, on the phone and on the site, tends to win the car, because a shaken driver hires the one who made them feel taken care of.</p>'},
        {"h2_html": "The handful of things that actually <em>bring cars in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more customers is less about a clever trick and more about doing the basics consistently, which is what tends to fall apart when the booth is full. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Show up in the map pack for the searches drivers make after an accident, like collision repair near me and auto body shop near me, with a verified, complete Google Business Profile.</li><li>Build a steady flow of real reviews, because a wreck is memorable and a nervous driver leans hard on what other people said.</li><li>Answer the insurance and estimate questions plainly, on your site and on the phone, so a driver choosing under stress picks you.</li><li>Make it one tap to request an estimate or call, and answer every one of those calls, because a driver who cannot reach you calls the next shop.</li><li>Stay in touch with past customers and ask happy ones to refer you, since the next wreck a friend has is a car that can come straight to you.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Reactivating the customers already in your list and earning referrals are some of the cheapest cars you will book. What no one can honestly promise is a specific ranking or a set number of cars, because no one controls Google, but the levers above are the ones that move it, and a free audit can show you where you stand today.</p>'}],
    "bridge_h2": "Get found and chosen after the accident",
    "bridge_text": "Most collision work starts with a search right after a wreck. Marketing that puts you in the map pack, builds real reviews, and answers the insurance questions is how you get chosen at the moment a driver needs a shop.",
    "bridge_slug": "marketing-for-auto-body-shops",
    "bridge_label": "Marketing for auto body shops",
    "faqs": [
        ("What is the fastest way for a body shop to get more collision jobs?",
         "Be findable and reachable at the moment a driver searches after an accident. That means a verified Google Business Profile in the map pack, recent reviews, and a phone that always gets answered. A car that can reach you and trust you at that moment is the one you book."),
        ("Do reviews really matter for an auto body shop?",
         "A great deal. A wreck is stressful and memorable, so a driver handing over a car they need back leans heavily on what other customers said. A steady stream of recent, genuine reviews is often what tips a nervous driver toward your shop over the one next door.")],
    "trade_slug": "auto_body_shops", "trade_plural": "auto body shops",
    "hub_name": "Auto", "hub_slug": "industry-auto.html",
},
]
