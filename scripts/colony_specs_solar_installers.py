"""Colony page specs for SOLAR INSTALLERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a solar-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, solar-specific substance (the generator owns shell,
schema, events, keyword placement). Residential solar is a high-ticket, consultative, multi-touch
sale on a long cycle of consult, custom proposal, financing, permitting, and install, not a
same-day emergency, so the substance leans on speed-to-lead on fresh internet leads (homeowners
comparing three or four quotes at once), relentless follow-up over the weeks a proposal sits quiet,
trust and education for a cautious researcher, and owning expensive leads instead of renting them.

Same honesty rules as the money specs: no invented stats, no invented solar prices, no named
clients or competitors; only the real Top Shelf prices ($299/$899/$2,500 plans, $1,500 one-time
site, CRM + AI = the $899 Signature plan) ever appear; no em/en dashes anywhere; never "leak" as a
metaphor. ETHICS (solar is regulated): the AI does scheduling and intake ONLY, and NOTHING here
promises a saving, payback, ROI, bill elimination, or a tax-credit amount; financing, incentives,
and net metering are referred to only as questions a homeowner researches, never as a number.

Six questions, mixed cost / problem / how-to, spread across four money pages:
  1 solar-company-website-cost               (cost)     -> websites-seo-for-solar-installers
  2 solar-answering-service-cost             (cost)     -> ai-receptionist-for-solar-installers
  3 is-a-crm-worth-it-for-a-solar-company    (cost)     -> crm-for-solar-installers
  4 why-solar-companies-miss-calls           (problem)  -> ai-receptionist-for-solar-installers
  5 why-solar-leads-go-cold                  (problem)  -> crm-for-solar-installers
  6 how-do-solar-companies-get-more-leads    (how-to)   -> marketing-for-solar-installers
"""

TOPICS = [
# ==================== How Much Does a Solar Company Website Cost? (cost -> websites-seo) ====================
{
    "slug": "solar-company-website-cost",
    "h1": "How Much Does a Solar Company Website Cost?",
    "title": "How Much Does a Solar Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A solar company website ranges from a cheap template to a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A solar company website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more is whether it earns a cautious homeowner's trust and turns a research visit into a booked consultation. Top Shelf builds a custom site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What a solar site actually has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A solar company website is not a brochure you put up and forget. A homeowner about to spend a large sum on a considered purchase reads it carefully, often late at night after the kids are asleep, comparing you against the other companies they are looking at, before they ever pick up the phone. So the real question is not how cheap you can get a site, it is whether the site does the job of turning a cautious researcher into a booked consultation.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A solar site earns its money when it does a handful of specific things well:</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Puts a clear consultation or quote request within reach on every page, so a homeowner ready to talk can raise their hand in a tap instead of hunting for your number.</li><li>Shows the proof a wary buyer looks for: photos of real local installs, honest reviews, and your license and insurance stated plainly, so you read as an established company rather than a fly-by-night one.</li><li>Answers the questions a researcher actually carries, how the process works, how financing generally works, whether solar makes sense in their area, honestly and without ever promising a number.</li><li>Ranks for what people type while researching solar, solar installers near me and solar company in their city, so they find you instead of a national lead-seller.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A beautiful site that ranks for nothing and buries the quote request three clicks deep is the most expensive kind of all, because you paid for it and it books nothing.</p>'},
        {"h2_html": "What a solar company should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Prices for a solar website swing widely because a template you fill in yourself and a custom site built to rank and convert are different products with the same name. A do-it-yourself builder is cheap monthly, but you do the work and it is rarely built to rank or to earn a nervous buyer\'s trust. A custom build is yours to keep, but a site alone does little if nobody is doing the ongoing SEO that gets it found. Before you sign anything, ask who owns the site, what a change costs, and whether you keep it if you leave.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because nobody controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books consults",
    "bridge_text": "A solar website is only worth the consultations it books. Ours ranks for the towns you serve, earns a cautious homeowner's trust, and turns a research visit into a booked consult, then hands it to the system that follows up.",
    "bridge_slug": "websites-seo-for-solar-installers",
    "bridge_label": "Websites & SEO for solar installers",
    "faqs": [
        ("Is a cheap template site good enough for a solar company?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to earn the trust of a homeowner spending this much, and you do the work of maintaining it. For a considered purchase like solar, a site that does not get found or does not look credible is not really the bargain its price suggests."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ What Does a Solar Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "solar-answering-service-cost",
    "h1": "What Does a Solar Answering Service Cost?",
    "title": "What Does a Solar Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Solar answering services often bill per call or minute. Top Shelf's AI receptionist answers every quote call and web lead 24/7 in the Signature plan at $899 a month.",
    "answer": "Traditional answering services for solar companies usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every quote call and web lead and books the consult comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good run of leads turns into a big bill. Solar makes it worse, because your leads do not arrive politely during office hours. A homeowner sits down to research and request quotes late at night or over the weekend, exactly when after-hours minutes tend to cost the most, and exactly when your closers are already out on consults. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of unqualified inquiries runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty homeowner or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when the leads are flowing.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a homeowner requesting solar quotes is filling out three or four forms in one sitting, and the company that reaches them while they are still at the screen is the one that books the consult. The real cost of no coverage is not a monthly fee, it is the install that went to whoever called back first, plus the money you already spent on the ad or the lead that made the phone ring. But a generic call center reading a script cannot tell a serious homeowner who owns a sunny house from a renter who can never say yes, so you can pay for coverage and still get poor qualifying.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, qualifies the homeowner the way you would, and books the consultation or hands your closer a qualified lead. It handles scheduling and intake only; it never quotes a price or promises a saving. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. Because a solar company lives on a small number of large sales, one consultation you would have lost while your reps were out can be worth well more than the plan costs, and everything it books after that is on top.</p>'}],
    "bridge_h2": "Answer every lead without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every quote call and web lead the moment it lands, qualifies the homeowner, and books the consult, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-solar-installers",
    "bridge_label": "AI receptionist for solar installers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live solar answering service?",
         "Usually, and far more predictable. A live service that bills per call or per minute climbs exactly when your leads are flowing, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the consultation it books instead of losing to the company that answered first."),
        ("Does it cost extra for nights and weekends?",
         "No. It answers 24/7 as part of the plan, including the late nights and weekends when homeowners actually sit down to research solar and request quotes, with no after-hours surcharge or overage.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============== Is a CRM Worth It for a Solar Company? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-solar-company",
    "h1": "Is a CRM Worth It for a Solar Company?",
    "title": "Is a CRM Worth It for a Solar Company? | Top Shelf Business Solutions",
    "meta_desc": "For most solar companies a CRM pays for itself by reviving one proposal that went quiet over a long sales cycle. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most solar companies, yes. A CRM pays for itself the first time it wins back a proposal you would have let go quiet, or revives a homeowner who asked for a quote a year ago. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a solar company the moment you have more proposals and past inquiries than you can personally keep straight, which is most installers doing steady volume. It is not worth it if you close every homeowner in the room and genuinely follow up with each one yourself, though on a sale this slow that almost never holds. The honest test is simple: how many proposals have you sent in the last few months that you never circled back on, and how many homeowners asked for a quote a year ago and never heard from you again?</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A solar decision runs for weeks or months of comparing, financing, and second-guessing, and the deal usually goes to the company that stayed in touch, not the cheapest bid. Think of a CRM less as software you switch on and more as the thing that makes sure the work you already did at the kitchen table does not quietly expire while you are out running the next consult. Those half-earned sales, the quiet proposals and the not-ready leads, are exactly what it is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a solar company is not the software, it is the work that stops slipping through the long gap between the consult and the signature. A homeowner sitting on a custom proposal, a family still comparing your numbers against two other bids, an inquiry from last year whose roof just got replaced: each is a sale you have already half-earned and are one well-timed touch away from closing.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open proposal on a schedule you set, so a homeowner comparing three quotes keeps hearing from you while the other two go quiet.</li><li>It keeps a light, genuine touch on the not-ready leads, so when their situation finally changes your name is the one already in front of them instead of a brand new lead you pay for again.</li><li>It keeps every lead, proposal, financing conversation, and note in one place instead of a rep\'s notebook and whatever anyone remembers a month later.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one system you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your proposals back to work",
    "bridge_text": "The proposals you already sent and the homeowners already in your records are the cheapest systems you can sell. A CRM follows up on every one for you, so they sign with you instead of the company that stayed in touch.",
    "bridge_slug": "crm-for-solar-installers",
    "bridge_label": "CRM for solar installers",
    "faqs": [
        ("Is a CRM overkill for a small solar company?",
         "Not usually. Even a small installer sends more proposals and talks to more homeowners than anyone can track by memory, and a solar sale sits open for weeks. The point is not size, it is whether follow-up is falling through. If proposals go quiet and past inquiries are forgotten, a CRM earns its keep."),
        ("How is a CRM different from keeping leads in a spreadsheet?",
         "A spreadsheet does not follow up on a proposal, does not remind you which homeowner has gone quiet, and does not revive a lead whose situation finally changed. A CRM does all of that on a schedule, so the systems you already quoted actually turn into signed installs.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Solar Companies Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-solar-companies-miss-calls",
    "h1": "Why Do Solar Companies Miss So Many Calls?",
    "title": "Why Do Solar Companies Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Solar companies miss calls because leads arrive while every rep is out selling, and a homeowner requesting quotes from several companies never leaves a voicemail.",
    "answer": "Solar companies miss calls because the leads come in while every rep is out, on a roof, in a consult, or driving to the next appointment, and a homeowner requesting quotes from several companies at once does not leave a voicemail. They move on to whoever answers. The fix is making sure every quote call and web lead gets answered.",
    "sections": [
        {"h2_html": "The lead comes in exactly when your reps <em>are out selling</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Solar is a business where your best people are out of the office by design. When a quote call comes in, your closers are on a roof taking measurements, at a kitchen table walking a family through a proposal, or driving between appointments, and none of those are moments they can stop and take a call. The more consults your team is running, the more calls ring out, which means your busiest, best weeks are also the ones where the most expensive leads slip away. It is not a discipline problem. A closer cannot sit in one homeowner\'s living room and answer the next homeowner\'s call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a fresh solar lead it is not one. A homeowner who just filled out quote forms on four sites in one sitting is not going to leave a message and wait. They talk to whichever company calls back while they are still at the screen, and by the time anyone checks the voicemail, the consult is already booked with someone else.</p>'},
        {"h2_html": "Missed leads are the ones you <em>paid the most to earn</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call costs the same. A missed solar lead is often one you paid real money to generate, through an ad, a marketplace, or the work of ranking, and behind it sits a single large sale rather than a small ticket. So the calls you are most likely to miss, the ones that land while your whole team is out selling, are also the ones worth the most and the most expensive to replace. Losing one is losing the install and the marketing spend that produced it, both at once.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a real buyer from a browser. A voicemail box cannot qualify anyone, and a generic call center does not know a homeowner who owns a sunny single-family home from a renter who can never move forward. What actually works is something that answers on the first ring day or night, confirms the basics a consult needs, whether they own the home, roughly what their power bill runs, and what has them looking now, then books the consultation or hands a qualified lead straight to your closer, so the homeowner who was finally ready reaches an organized company instead of a recording.</p>'}],
    "bridge_h2": "Stop losing paid leads to voicemail",
    "bridge_text": "An AI receptionist answers every quote call and web lead on the first ring, day or night, qualifies the homeowner, and books the consult or hands it to your closer, so the lead you paid to earn never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-solar-installers",
    "bridge_label": "AI receptionist for solar installers",
    "faqs": [
        ("Would a homeowner rather reach a real person?",
         "For a purchase this size, what a homeowner wants most is to feel a real, organized company is handling it, and a calm voice that captures their details and books a consult beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands a qualified lead straight to your closer."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are on a roof, mid-consult, or already on another call, which is most of your day. Something that always answers and qualifies is what catches the leads a forward would still miss.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ============ Why Do Solar Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-solar-leads-go-cold",
    "h1": "Why Do Solar Leads Go Cold?",
    "title": "Why Do Solar Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most solar leads go cold not over price but because nobody followed up over the weeks a solar decision takes. The deal drifts to whoever stayed in touch.",
    "answer": "Most solar leads go cold not because your price was wrong, but because nobody followed up over the weeks the decision takes. The homeowner gathered other bids, weighed financing, talked it over, and drifted to whichever company stayed in touch. A proposal that goes quiet is usually not a no, it is a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means still deciding, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet proposal as a no on price, so you drop it and move on to the next consult. But most of the time the homeowner did not decide against you at all. A solar purchase is large, financed, and slow, so after the consult they are gathering two or three other bids, comparing your numbers, weighing whether to pay cash or finance, talking it over with a spouse, and waiting to feel sure. That takes weeks, sometimes months, and while it sits, life fills in around it. A month later they could not tell you the real difference between the companies that came out.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The one who wins is usually not the cheapest. It is the company that stayed present and organized the whole way through: a friendly check-in a week later, a plain answer to the financing question they were stuck on, a note when the season or their bill made solar feel worth revisiting. On a purchase this size the buyer is really deciding who to trust, and the company that never went quiet is the one that feels safe. That steady second, third, and fourth touch is exactly what there is no time for between consults.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Solar installers do not skip follow-up because they are lazy. They skip it because the calendar fills up. You run the consult, build the proposal, roll to the next appointment, and by the time the week is out the proposal you sent Tuesday is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest open proposals to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system showing which proposals are still open and going quiet.</li><li>The follow-up depends on you remembering, so it competes with running consults and loses.</li><li>The homeowner who asked for a quote last year, and whose situation may have changed, sits forgotten in a spreadsheet while you pay to generate a brand new lead.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open proposal gets timed check-ins automatically, written to sound like you, and the not-ready leads stay on a gentle touch, the homeowner comparing bids keeps hearing from you while the others go silent, and the systems you already quoted stop drifting away.</p>'}],
    "bridge_h2": "Follow up on every proposal, automatically",
    "bridge_text": "A CRM keeps every open proposal in front of you and sends timed check-ins for you over the weeks a solar decision takes, so the homeowner comparing bids keeps hearing from you while the other companies go quiet.",
    "bridge_slug": "crm-for-solar-installers",
    "bridge_label": "CRM for solar installers",
    "faqs": [
        ("How many times should I follow up on a solar proposal?",
         "A solar decision runs longer than most, so a handful of light touches spread across the weeks the homeowner is comparing catches most of the maybes without being pushy: a check-in after the proposal, a nudge while they weigh financing, a touch when the season or their bill changes. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace over a long decision. A short, friendly check-in reads as attentive and organized, which is exactly the signal a nervous buyer on a big purchase is looking for. You can always step in and message anyone directly.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
# ======== How Do Solar Companies Get More Leads? (how-to -> marketing) ========
{
    "slug": "how-do-solar-companies-get-more-leads",
    "h1": "How Do Solar Companies Get More Leads?",
    "title": "How Do Solar Companies Get More Leads? | Top Shelf Business Solutions",
    "meta_desc": "Solar companies get more leads by being easy to find and trust where homeowners research: an active Google profile, real reviews, and local pages, not rented leads.",
    "answer": "Solar companies get more leads by being easy to find and easy to trust in the exact spots a homeowner looks while researching: an active Google Business Profile, a steady stream of genuine reviews, and local pages that answer real questions. Owning that visibility, instead of renting leads from a marketplace, is what turns research into booked consults.",
    "sections": [
        {"h2_html": "The leads follow trust, because solar is a <em>researched purchase</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody buys solar on impulse. It is a large, financed, long-term decision, wrapped in more skepticism than almost any home upgrade, so a homeowner researches for weeks before they reach out. They read reviews, compare companies, ask a neighbor who already went solar, and quietly rule out anyone who looks thin or hard to trust before they ever make contact. That means getting more leads is less about shouting at people who have no interest yet and more about being the credible, easy-to-find company the moment someone does start looking.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The map pack, those local listings with the star ratings, is usually the first thing a homeowner sees, and right beside it sit your reviews. For solar they carry more weight than for almost any trade, because the buyer is cautious and looking for a reason to trust you or to walk away. A profile that has sat quiet for months with a thin trickle of reviews reads like a company that is struggling, no matter how good your installs are. An active profile backed by a steady flow of genuine reviews, with calm replies to the occasional critical one, looks like exactly the established installer a nervous homeowner hopes to find.</p>'},
        {"h2_html": "Own the channel, and stay in front of the <em>slow decider</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">More leads come from a handful of things done consistently, not a clever trick.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your Google Business Profile active, complete, and accurate, with photos of real local installs, so you show up and look current when a homeowner searches for a solar company near them.</li><li>Turn happy customers into a steady stream of genuine reviews, which are both the proof a cautious buyer wants and a signal that lifts you in local search.</li><li>Rank your own pages for the towns you serve and the questions people ask, solar installers near me, solar company in their city, so a homeowner finds you directly instead of a national marketplace that sells the inquiry back to you.</li><li>Answer the questions a researcher actually has, how the process works, how financing generally works, whether solar fits their area, honestly and without ever promising a number, so you read as a straight shooter rather than a hard sell.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A solar buyer spends weeks quietly researching before they are ready, so the company that stays visible and genuinely helpful through that whole stretch is the one they contact when they finally are. This public-facing work brings new researchers to your door, and the private follow-up with the leads already in your database keeps them from forgetting you; the two together are what steadily fill the pipeline. None of it requires overpromising a saving or a payback, just being the local company that shows up, speaks plainly, and looks like it will still be around in ten years.</p>'}],
    "bridge_h2": "Become the solar name they find first",
    "bridge_text": "More solar leads come from being easy to find and easy to trust where homeowners research. Keeping your Google profile active, your reviews growing, and your local pages answering real questions is how you show up when someone nearby starts looking.",
    "bridge_slug": "marketing-for-solar-installers",
    "bridge_label": "Marketing for solar installers",
    "faqs": [
        ("Do I need to buy leads from a marketplace to get started?",
         "No, and it is the most expensive way to grow. A marketplace rents you an inquiry it also sells to your competitors, and it stops the day you stop paying. Being findable and credible on your own Google profile, reviews, and local pages brings you leads that are yours alone and keeps working long after the work is done."),
        ("How long until better marketing brings in leads?",
         "A neglected Google profile can start climbing in local search within a few weeks once it is active and complete, and it compounds as reviews and local content build. Nobody controls Google, so no honest company promises a specific position, but consistency on the profile and reviews is what moves it.")],
    "trade_slug": "solar_installers", "trade_plural": "solar installers",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
},
]
