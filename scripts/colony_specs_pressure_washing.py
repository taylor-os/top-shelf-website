"""Colony page specs for PRESSURE WASHING (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a pressure-washing-business owner would search, answered directly up
top (the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels
the page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, pressure-washing-specific substance (the generator owns
shell, schema, events, keyword placement). Never the plumber or home-services content reworded.
Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear, and
never an invented wash price; no em/en dashes anywhere; no banned water metaphors in the copy.
Ethics: the AI receptionist does scheduling and intake ONLY, never a firm price sight unseen.

The trade's reality, and what keeps each page distinct from the money pages and from each other:
pressure washing runs on the dramatic before-and-after reveal (house wash, driveway, deck, roof
soft wash), a hard spring and early-summer rush, a mix of one-off homeowner jobs and recurring
commercial and HOA contracts, and estimate-shopping homeowners who book whoever answers while the
crew is soaked and running loud gear.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 pressure-washing-website-cost                       (cost)    -> websites-seo-for-pressure-washing
  2 pressure-washing-answering-service-cost             (cost)    -> ai-receptionist-for-pressure-washing
  3 is-a-crm-worth-it-for-a-pressure-washing-business   (cost)    -> crm-for-pressure-washing
  4 why-pressure-washers-miss-calls                     (problem) -> ai-receptionist-for-pressure-washing
  5 why-pressure-washing-quotes-go-cold                 (problem) -> crm-for-pressure-washing
  6 how-do-pressure-washers-get-more-customers          (how-to)  -> marketing-for-pressure-washing
"""

TOPICS = [
# ============ How Much Does a Pressure Washing Website Cost? (cost -> websites-seo) ============
{
    "slug": "pressure-washing-website-cost",
    "h1": "How Much Does a Pressure Washing Website Cost?",
    "title": "How Much Does a Pressure Washing Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A pressure washing website runs from cheap templates to a few thousand for a custom build. What counts is a before-and-after gallery that sells and captures the quote. Top Shelf builds yours for $1,500, or free on any plan.",
    "answer": "A pressure washing website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it shows your before-and-after work, ranks for pressure washing near me, and captures the quote request. Top Shelf builds a custom site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a pressure washing site actually <em>has to do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A pressure washing website has one job, and it is not to look pretty. It is to take a homeowner who just looked at a black driveway or a streaked roof and turn them into a quote request on your phone. Before you think about price, know what you are actually paying for, because a site that cannot do these things is not cheap, it is wasted money no matter what it cost.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A before-and-after gallery front and center. Pressure washing sells itself when a homeowner sees a driveway or roof like theirs go from filthy to clean, so real reveal photos do most of the convincing.</li><li>An instant quote request that takes one tap. Most of these searches happen on a phone, so a visitor should be able to snap a photo of the surface, enter the address, and ask for a price in under a minute.</li><li>A clear service list. House wash, driveway and concrete, deck and fence, roof soft wash, and commercial or HOA work, so a caller knows at a glance that you do their specific job.</li><li>Pages built to rank for pressure washing near me and the towns you cover, so the homeowner searching in a hurry finds you instead of a national directory.</li></ul>'},
        {"h2_html": "What a pressure washing site should actually <em>cost you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Once the site does those things, the price question gets simpler. A do-it-yourself builder is cheap every month, but you do the work and it is rarely built to rank or to capture a quote. A one-time custom build costs more up front and is yours to keep, though a site alone does little if nobody is doing the ongoing SEO to get it found. An agency that bundles the build with ongoing SEO carries a monthly cost, and that is where most of the long-term value lives.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it plain. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking is handled for you. There is no setup fee either way. Before you sign with anyone, ask who owns the site, what a change costs, and whether you keep it if you leave. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that captures the quote",
    "bridge_text": "A pressure washing website is only worth the jobs it brings in. Ours puts your before-and-after work up front, ranks for the towns you cover, and captures the quote request directly, so the call is yours instead of a lead-seller's.",
    "bridge_slug": "websites-seo-for-pressure-washing",
    "bridge_label": "Websites & SEO for pressure washing",
    "faqs": [
        ("Is a cheap template site good enough to start with?",
         "It can get you online, but a template you fill in yourself rarely ranks, and it usually buries the before-and-after photos and the quote button that actually book pressure washing jobs. If a site is not getting found or turning visitors into quote requests, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== What Does a Pressure Washing Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "pressure-washing-answering-service-cost",
    "h1": "What Does a Pressure Washing Answering Service Cost?",
    "title": "What Does a Pressure Washing Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for pressure washing companies often bill per call or minute, which spikes in the spring rush. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for pressure washing companies usually bill per call, per minute, or a monthly retainer, so a busy spring turns into a big bill right when the estimate calls are flooding in. Top Shelf takes a different approach: an AI receptionist that answers every call and books the job comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until spring hits. Pressure washing demand spikes the first warm weekend of the year, when every homeowner notices the winter buildup at once, so the month you get the most calls is the month a per-call or per-minute service costs you the most. It is worth knowing the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a spring flood of homeowners pricing a house wash runs the bill straight up.</li><li>Per-minute pricing: you pay for talk time, so a caller asking about a driveway, a deck, and a roof all at once costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of calls, and you pay extra past it, usually right in the busy season when you blow through the bucket.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner pricing a house wash is calling three or four companies and books whoever picks up and sounds professional. The real cost of no coverage is not a monthly fee, it is the estimate that went to the company that answered while your crew was soaked and running a surface cleaner. But a generic call center reading a script cannot tell a soft wash from a driveway job, or ask the right questions about a roof, so you can pay for coverage and still hand the caller a poor first impression.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, asks what needs washing and where the way you would, and books the estimate or the job onto your calendar. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running, and it does the scheduling and intake only, never a firm price sight unseen. One house wash you would have lost while your hands were full can be worth more than the plan costs, and everything it books after that is on top.</p>'}],
    "bridge_h2": "Answer every estimate without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7 through the spring rush, asks the right questions for a house wash or a roof, and books it, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-pressure-washing",
    "bridge_label": "AI receptionist for pressure washing",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and far more predictable. A live service that bills per call or per minute climbs exactly during the spring rush when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the estimate it books instead of losing to voicemail while your crew is heads-down on a job."),
        ("Does it cost extra for nights, weekends, or the busy season?",
         "No. It answers 24/7 as part of the plan, including the first warm Saturday of spring when every homeowner searches at once, with no after-hours surcharge and no overage for a heavy month. A flat plan is what makes the busy season profitable instead of expensive.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ========= Is a CRM Worth It for a Pressure Washing Business? (cost -> crm) =========
{
    "slug": "is-a-crm-worth-it-for-a-pressure-washing-business",
    "h1": "Is a CRM Worth It for a Pressure Washing Business?",
    "title": "Is a CRM Worth It for a Pressure Washing Business? | Top Shelf Business Solutions",
    "meta_desc": "For most pressure washing companies a CRM pays for itself by reviving one cold estimate and rebooking past customers for an annual wash. It comes in Top Shelf's Signature plan at $899/mo, not a separate bill.",
    "answer": "For most pressure washing companies, yes. A CRM pays for itself the first time it wins back an estimate you would have let go cold, or brings a past customer back for a yearly wash when the grime creeps back in. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a pressure washing company when you have more estimates and past customers than you can keep in your head, which is most crews past their first season. It is not worth it if you are a one-person operation doing a handful of washes a week and genuinely calling everyone back, though that rarely lasts as you grow. The honest test is simple: how many estimates have you sent this spring that you never circled back on, and how many houses did you wash last year that have not heard from you since?</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Those two questions point straight at the money a CRM is built to recover, and pressure washing has an unusual amount of it. Unlike a trade where a repair is done and forgotten, the grime you strip off a house or a driveway starts coming back the day you leave, so every customer you have ever washed is a re-wash waiting to be booked. That is what makes the worth-it math lean so hard toward yes in this trade.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a pressure washer is not the software, it is the work that stops slipping away. A homeowner sitting on a house-wash quote, a driveway you cleaned two springs ago, a storefront that should be on a monthly rotation: each one is a job you have already half-earned and are one reminder away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open estimate on a schedule, so a homeowner comparing a few companies keeps hearing from you while the others go quiet.</li><li>It fires annual reminders, a yearly house wash, a driveway before the holidays, a roof soft wash, so the re-wash comes back around without you tracking a single date.</li><li>It holds your commercial and HOA accounts and their rotation, so the monthly storefront and the quarterly HOA route stay booked and invoiced instead of slipping.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one job you would have lost, or rebook one past customer, and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Turn one wash into a customer for life",
    "bridge_text": "The grime always comes back, so every house you have washed is a re-wash waiting to be booked. A CRM follows up on every estimate and reminds every past customer for you, so they call you next instead of searching Google again.",
    "bridge_slug": "crm-for-pressure-washing",
    "bridge_label": "CRM for pressure washing",
    "faqs": [
        ("Is a CRM overkill for a small pressure washing business?",
         "Not usually. Even a one or two truck crew sends more estimates and washes more houses in a season than anyone can track by memory, and every one of those houses gets dirty again. The point is not size, it is whether follow-up is falling through. If estimates go cold and past customers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping numbers in my phone?",
         "A phone full of contacts does not follow up on an estimate, does not remember which house is due for its yearly wash, and does not track a commercial rotation. A CRM does all of that on a schedule, so the repeat work and the recurring accounts show up instead of depending on you to remember.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Pressure Washers Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-pressure-washers-miss-calls",
    "h1": "Why Do Pressure Washers Miss So Many Calls?",
    "title": "Why Do Pressure Washers Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Pressure washers miss calls because they ring while the crew is soaked behind a surface cleaner, and a homeowner shopping for a quote does not leave a voicemail, they call the next company.",
    "answer": "Pressure washers miss calls because they come while your hands are full, up a ladder soft washing a roof, behind a surface cleaner, or driving between jobs, and a homeowner pricing a wash does not leave a voicemail. They hang up and call the next company on their list. The fix is not working harder, it is making sure every estimate call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pressure washing is a hands-full, loud trade. When the phone rings you are usually standing in the spray with a wand, up a ladder soft washing a second story, behind a surface cleaner that drowns out everything, or driving to the next job soaked and worn out, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One crew cannot run the machine in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a homeowner shopping around it is not one. Someone who just looked at a black driveway and wants a price is not loyal to anyone yet. They found three or four companies on Google, they are dialing down the list, and they book the first one that answers and sounds professional. They will not leave a message and wait. By the time you check your phone, the estimate is already gone.</p>'},
        {"h2_html": "The spring rush is when the <em>most calls fall through</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pressure washing demand is not steady, it arrives in a wave. The phone starts ringing the first warm weekend of spring, when every homeowner notices the winter buildup at once, and it stays loud through early summer. That is exactly when a single phone gets buried: three estimate calls come in the same hour your crew is heads-down on a driveway, and two of them roll to voicemail and move on. So the season that makes your year is also the one where you quietly lose the most work to whoever happened to be free to pick up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and knows the trade. A voicemail box cannot ask a question, and a generic call center does not know a soft wash from a driveway job. What actually works is something that answers on the first ring, asks what needs washing, how big it is, and where, and either books the estimate onto your calendar or flags it to your phone, all as scheduling and intake, never a firm price sight unseen. The call gets captured instead of lost, even when every homeowner in town is searching at the same moment.</p>'}],
    "bridge_h2": "Stop losing estimates to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, even mid-wash and through the spring rush, asks the right questions for a house wash or a roof, and books it or flags it to you, so the estimate never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-pressure-washing",
    "bridge_label": "AI receptionist for pressure washing",
    "faqs": [
        ("Would a customer rather reach a real person?",
         "A homeowner pricing a wash mostly needs to know a real company is handling it and someone will come give a price, and a steady voice that captures the address and the surface beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the details, and hands the job to you to quote."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are behind a surface cleaner, up a ladder, or already on another call, which is most of the day in season. Something that always answers and gathers the details is what catches the calls a forward would still miss.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do My Pressure Washing Quotes Go Cold? (problem -> crm) ============
{
    "slug": "why-pressure-washing-quotes-go-cold",
    "h1": "Why Do My Pressure Washing Quotes Go Cold?",
    "title": "Why Do My Pressure Washing Quotes Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most pressure washing quotes go cold not over price but because nobody followed up. The homeowner got other estimates or got busy, and the job went to whoever checked back in.",
    "answer": "Most pressure washing quotes go cold not because your price was wrong, but because nobody followed up. The homeowner gathered a couple of other estimates, got busy, or simply forgot, and the job went to whoever checked back in. A quote that goes quiet is usually not a no, it is a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet estimate as a no on price, so you drop it and move on to the next job. But most of the time the homeowner did not decide against you at all. They wanted their house or driveway washed, they had two or three companies come give a price, and they meant to think it over. Then the weekend filled up, work got busy, and your quote slid down the pile. A week later they honestly could not tell you the difference between the companies that came out, and the winner is not usually the cheapest.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It is the one who stayed in front of them. A friendly check-in a couple of days later, a quick note answering the question they were stuck on, and suddenly yours is the only name they still remember when they are finally ready to book. That second touch is what turns a maybe into a scheduled wash, and it is exactly the thing there is no time for when you are on a job from dawn to dark all season.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Pressure washers do not skip follow-up because they are lazy. They skip it because the day fills up. You finish a driveway, drive to the next house, squeeze in the estimate that came in this morning, and by evening the quote you sent Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which in this trade is the off-season, exactly when you have the fewest fresh quotes to chase anyway.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which estimates are still open and going cold.</li><li>The follow-up depends on you remembering, so it competes with the actual washing and loses.</li><li>By the time you circle back, the homeowner has already booked the company that beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every open estimate gets a couple of timed check-ins automatically, written to sound like you, the homeowner comparing companies keeps hearing from you while the others go silent, and the work you already quoted stops slipping away. The same list, worked the same way, brings last year customers back when the grime returns.</p>'}],
    "bridge_h2": "Follow up on every estimate, automatically",
    "bridge_text": "A CRM keeps every open estimate in front of you and sends timed check-ins for you, so a homeowner comparing companies keeps hearing from you while the others go quiet, and the quote you already gave turns into a booked wash.",
    "bridge_slug": "crm-for-pressure-washing",
    "bridge_label": "CRM for pressure washing",
    "faqs": [
        ("How many times should I follow up on a pressure washing quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the estimate, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and most homeowners appreciate the nudge because they meant to get back to you and forgot. You can always jump in and message anyone directly.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======= How Do Pressure Washers Get More Customers? (how-to -> marketing) =======
{
    "slug": "how-do-pressure-washers-get-more-customers",
    "h1": "How Do Pressure Washers Get More Customers?",
    "title": "How Do Pressure Washers Get More Customers? | Top Shelf Business Solutions",
    "meta_desc": "Pressure washers get more customers by putting before-and-after photos and reviews first in the map pack, ranking in the towns they cover, and rebooking past customers when the grime returns.",
    "answer": "Pressure washers get more customers by being impossible to miss where homeowners search, the map pack and Google, and by leading with the before-and-after photos that sell the work on sight. Show that transformation constantly, keep your profile active and full of reviews in the towns you cover, and turn the customers you already washed into repeat and referral work.",
    "sections": [
        {"h2_html": "The before-and-after photo is the <em>whole engine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Almost nothing in home services sells itself the way pressure washing does. A single side-by-side of a black, algae-streaked driveway next to a clean one, or a dingy roof brought back to its real color, does more than any slogan could, because the result is instant, obvious, and satisfying to look at. Getting more customers starts with treating that transformation as your main advertisement and putting it everywhere a homeowner might see it, so someone staring at their own filthy concrete pictures their house next.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The place most of them look is the map pack, the three local listings with star ratings that sit at the top when someone searches for pressure washing near them. Most people choose from those three without scrolling. A profile stacked with fresh before-and-after shots, current services, and a steady stream of recent reviews looks like the obvious choice next to one with two old photos. The mistake is doing great work and never capturing it, because a clean driveway with no photo is a marketing asset thrown away.</p>'},
        {"h2_html": "Cover your towns, ride the season, and <em>rebook what you have</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Chasing a whole metro is expensive and sends you calls from an hour outside your range. Focusing on the specific towns and neighborhoods you serve, with a profile, photos, and content built around those areas, is what puts you in the map pack where you can actually take the work, and it turns into a route of jobs close together instead of a day lost to driving. A neighborhood of similar driveways and north-facing roofs streaking at the same time is a tight, reachable target.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Timing matters just as much. Demand arrives the first warm weekend of spring, when everyone notices the winter buildup at once, so your profile should be full and climbing before the season opens, not after the calls have started going to someone else. And the cheapest customers you will ever get are the ones you already washed: the grime always comes back, so a reminder next spring turns one job into a standing appointment, and a happy customer who saw the reveal tends to tell a neighbor. Getting more customers is the visible side of this, your Google profile, reviews, and local presence, while the website that captures the quote and the follow-up that rebooks past customers finish the job.</p>'}],
    "bridge_h2": "Be the pressure washer they can already see",
    "bridge_text": "Most pressure washing jobs start with a search and a glance at the map pack. Keeping your Google profile active, full of before-and-after work, and stacked with reviews is how you become the name a homeowner calls the moment they notice the dirt.",
    "bridge_slug": "marketing-for-pressure-washing",
    "bridge_label": "Marketing for pressure washing",
    "faqs": [
        ("What is the single best way to get more pressure washing customers?",
         "Be visible in the map pack with your before-and-after photos and recent reviews front and center. That is where local searches start and where the transformation you deliver does the selling for you. Everything else, your website and your follow-up, builds on being found there first."),
        ("Do social media before-and-afters actually bring in work?",
         "They help, because the reveal is naturally shareable and keeps you top of mind, but a post disappears down a feed fast. Your Google Business Profile is where a homeowner is actively looking to hire the moment they decide the house needs doing, so that is where those photos earn the most.")],
    "trade_slug": "pressure_washing", "trade_plural": "pressure washing companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
