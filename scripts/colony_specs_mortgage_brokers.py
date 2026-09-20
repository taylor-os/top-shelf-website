"""Colony page specs for MORTGAGE BROKERS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a mortgage-broker owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, mortgage-specific substance (the generator owns shell,
schema, events, keyword placement). It leads with the mortgage reality, not the generic template:
rate-shopping borrowers who apply with whoever answers FIRST (speed-to-lead is decisive),
pre-approval and refinance inquiries, the realtor-referral relationship that feeds the pipeline,
the long application-to-close process with many touchpoints, and rate-driven refinance surges.

Honesty rules (same as the money specs, stricter for regulated lending): no invented stats,
prices, or clients; only Top Shelf's real prices ($299/$899/$2,500 plans, $1,500 one-time site)
ever appear; no invented interest rates or fees; no em/en dashes anywhere; no "leak" as a metaphor;
illustrative scenarios, never a named client or competitor. Ethics: make NO promise about a rate,
an approval, the "best rate", or a dollar saving, and the AI receptionist does intake and
scheduling ONLY, never quoting a rate or suggesting anyone is approved.

Six questions, mixed cost / problem / how-to, spread across four Real Estate money pages:
  1 mortgage-broker-website-cost              (cost)     -> websites-seo-for-mortgage-brokers
  2 mortgage-answering-service-cost           (cost)     -> ai-receptionist-for-mortgage-brokers
  3 is-a-crm-worth-it-for-a-mortgage-broker   (cost)     -> crm-for-mortgage-brokers
  4 why-mortgage-brokers-miss-calls           (problem)  -> ai-receptionist-for-mortgage-brokers
  5 why-mortgage-leads-go-cold                (problem)  -> crm-for-mortgage-brokers
  6 how-do-mortgage-brokers-get-more-leads    (how-to)   -> marketing-for-mortgage-brokers
"""

TOPICS = [
# ============ How Much Does a Mortgage Broker Website Cost? (cost -> websites-seo) ============
{
    "slug": "mortgage-broker-website-cost",
    "h1": "How Much Does a Mortgage Broker Website Cost?",
    "title": "How Much Does a Mortgage Broker Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A mortgage broker website runs from a cheap template to a few thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A mortgage broker website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more than the sticker price is whether it earns a borrower's trust and gets found. Top Shelf builds a custom site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a mortgage broker website has to <em>do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare prices, it helps to know what the site is actually for, because a mortgage broker website earns its keep differently from most. A borrower deciding on the largest loan of their life sizes you up online before they ever call, so the site has a specific job: give a rate shopper a clear way to start a pre-approval or request a consultation the moment they land, show plainly who you are and where you are licensed so a stranger trusts you in seconds, and get found when someone nearby searches for a mortgage broker.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A clear way to start a pre-approval or request a consultation, visible the second the page opens, so a motivated borrower does not bounce to a national lender.</li><li>Trust signals up front: your license and NMLS ID, real reviews, and a real photo, because someone about to share their income and Social Security number needs to know you are legitimate.</li><li>Plain-English education and a payment estimator, so a first-time buyer or someone weighing a refinance gets their bearings on your site instead of a portal. A calculator estimates a payment, it never quotes a rate or promises approval.</li><li>Built to rank for a mortgage broker near me and your city, because the borrower with no referral starts at Google.</li></ul>'},
        {"h2_html": "What that costs, and what you should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Now the price. A do-it-yourself template is cheap monthly but you build and maintain it, and it is rarely made to rank or to turn a nervous borrower into a booked consultation. A custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found. An agency retainer bundles the build with that ongoing work, which is where most of the long-term value lives. A polished site that never ranks and gives a borrower no way to start is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you, with no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit will show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that turns searches into consultations",
    "bridge_text": "A mortgage broker website is only worth what it brings in. Ours is built to rank for your city and the searches borrowers actually make, earn the trust a financial decision needs, and capture the lead directly instead of a portal renting your own borrowers back to you, then feed it to the CRM that works the loan to closing.",
    "bridge_slug": "websites-seo-for-mortgage-brokers",
    "bridge_label": "Websites & SEO for mortgage brokers",
    "faqs": [
        ("Does a mortgage broker need a custom site, or is a template enough?",
         "A template can get you online, but it is rarely built to rank for your city or to earn the trust a borrower needs before handing over their financial life, and you maintain it yourself. If a site does not get found or turn visitors into consultations, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere, registered in your name. On a monthly plan the site is built and hosted for you as part of the plan, and we tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ======== What Does a Mortgage Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "mortgage-answering-service-cost",
    "h1": "What Does a Mortgage Answering Service Cost?",
    "title": "What Does a Mortgage Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for mortgage brokers often bill per call or minute. Top Shelf's AI receptionist answers and qualifies leads 24/7 in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for mortgage brokers usually bill per call, per minute, or on a monthly retainer, so a busy stretch gets expensive fast. Top Shelf takes a different route: an AI receptionist that answers 24/7, qualifies the lead, and books the consultation comes in the Signature plan at $899 a month flat, with no per-call fee. It never quotes a rate.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A broker also gets the highest-intent calls at the worst hours for a live service: the 10pm rate-form lead, the weekend pre-approval request, the past client asking about a refinance after dinner, all of which tend to hit when after-hours minutes cost the most. It is worth knowing the common models before you sign one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a run of rate shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a rate shopper or a buyer who just went under contract does not leave a voicemail and wait, they call the next broker on the list. The real cost of no coverage is not a monthly fee, it is the funded loan, and the commission on it, that closed with whoever picked up first. But a generic call center reading a script cannot qualify a mortgage lead, cannot tell a serious purchase from someone idly curious, and must never be put in a position to quote a rate or imply an approval, so you can pay for coverage and still get the wrong outcome.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, qualifies the way you would, purchase or refinance, timeline, whether they already have a pre-approval or an agent, and books the consultation or flags an urgent lead to your phone. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter. One funded loan you would have lost to voicemail is worth far more than the plan costs. It does intake and scheduling only: it never quotes a rate, states terms, or suggests anyone is approved, and anything that needs a licensed conversation waits for you.</p>'}],
    "bridge_h2": "Answer every lead without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, qualifies a purchase from a refinance, and books the consultation, all on a flat monthly plan. It captures the lead and hands it off, and it never quotes a rate or promises an approval.",
    "bridge_slug": "ai-receptionist-for-mortgage-brokers",
    "bridge_label": "AI receptionist for mortgage brokers",
    "faqs": [
        ("Is an AI receptionist cheaper than a live mortgage answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the after-hours lead it qualifies and books instead of losing to voicemail."),
        ("Will it quote a rate or tell someone they are approved?",
         "No, and that is by design. It captures the lead, qualifies it, and books the meeting, but it never quotes a rate, states terms, or suggests anyone is approved. Anything that needs a licensed conversation is handed straight to you.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Is a CRM Worth It for a Mortgage Broker? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-for-a-mortgage-broker",
    "h1": "Is a CRM Worth It for a Mortgage Broker?",
    "title": "Is a CRM Worth It for a Mortgage Broker? | Top Shelf Business Solutions",
    "meta_desc": "For most mortgage brokers a CRM pays for itself by reviving one aging pre-approval or one past client's refinance. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most mortgage brokers, yes. A CRM pays for itself the first time it revives a pre-approved buyer still house hunting, brings a past client back for a refinance, or keeps a referral agent warm. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a mortgage broker when you have more leads, past clients, and referral partners than you can keep straight in your head, which is most established shops, because a loan is a long pipeline and few of them close the week they come in. It is not worth it if you fund a handful of loans a year and genuinely stay in touch with everyone, though that rarely holds as you grow. The honest test is simple: how many pre-approved buyers are house hunting right now without hearing from you, how many past clients have not heard a word since closing, and how many referral agents have quietly gone cold. Those are the loans a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a broker is not the software, it is the business that stops slipping through the long stretch between the first call and the closing table. A pre-approved buyer who keeps getting outbid, a family whose loan you closed two years ago, an agent who sent you three buyers last year and none since: each is business you have already half-earned and are one timely touch away from keeping.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It keeps every open loan moving from first call to closing, reminding you who is waiting on you so nobody drifts while you are heads-down on another file.</li><li>It nurtures the pre-approved buyer still shopping and keeps a light, steady touch on past clients, so the next purchase and the rate-driven refinance come back to you.</li><li>It keeps your referral agents in their own track, warm between deals, because an agent sends buyers to the broker who stayed top of mind, not the one who did a good job a year ago.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. Recover one loan you would have lost and it has paid for itself, and it does all of this while staying compliant, never promising a rate or a result.</p>'}],
    "bridge_h2": "Put your pipeline and your past clients to work",
    "bridge_text": "The pre-approved buyers, past clients, and referral agents you already have are the cheapest loans you will ever earn. A CRM works every one of them for you on a schedule you set, from first call to closing and long after, so they come back to you instead of the broker who kept in touch, and it never promises a rate or a result.",
    "bridge_slug": "crm-for-mortgage-brokers",
    "bridge_label": "CRM for mortgage brokers",
    "faqs": [
        ("Is a CRM overkill for a small mortgage shop?",
         "Not usually. Even a one-person shop carries more pre-approvals, past clients, and referral partners than anyone can track by memory across a months-long pipeline. The point is not size, it is whether follow-up is falling through. If aging pre-approvals and past clients go quiet, a CRM earns its keep."),
        ("How is a CRM different from my loan origination software?",
         "Your loan origination software runs the loan file itself. A CRM works the relationship and the pipeline around it: who to follow up with, which lead went quiet, which past client is due for a check-in. It sits alongside the origination software you already use without getting in the way.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do Mortgage Brokers Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-mortgage-brokers-miss-calls",
    "h1": "Why Do Mortgage Brokers Miss So Many Calls?",
    "title": "Why Do Mortgage Brokers Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Mortgage brokers miss calls because they ring mid-application, at a closing, or after hours, and a rate shopper who hits voicemail just calls the next broker.",
    "answer": "You miss calls because they come when you cannot pick up, deep in an application, on with an underwriter, sitting at a closing, or home at night when a portal lead lands. A rate shopper who reaches voicemail does not wait, they call the next broker on the list. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Mortgage work is heads-down work. When the phone rings you are often deep in an application with a client, on the line with an underwriter, sitting at a closing table, or home with your family when a portal lead comes in at 10pm, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best stretches are also the ones where the most leads slip away. It is not a discipline problem. One person cannot work the file in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a rate shopper it is not one. Borrowers rarely call just one broker, they grab a few numbers or fill out a form and go with whoever picks up first and sounds like they know the process. A buyer who just got outbid or a homeowner who saw a headline about rates is not going to leave a message and wait, and by the time you check your phone, the loan is already gone.</p>'},
        {"h2_html": "Speed to lead decides who funds the <em>loan</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal, but in this business a missed one is rarely a small job. It is a whole loan, and the commission on it, gone to the broker who happened to answer faster. Those high-intent calls, the pre-approval before a weekend offer, the refinance question the night a rate headline runs, are exactly the ones most likely to roll to voicemail and exactly the ones worth the most. So the calls you are most likely to miss are the ones you can least afford to.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can actually qualify a mortgage caller: purchase or refinance, the timeline, whether they already have a pre-approval or an agent. A voicemail box cannot do that, and a generic call center should never be quoting rates or implying approvals. What works is something that answers on the first ring day or night, qualifies the lead, and either books the consultation or flags an urgent one to your phone, all without ever quoting a rate or promising approval, so the loan never rolls to voicemail in the first place.</p>'}],
    "bridge_h2": "Stop losing loans to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, qualifies a purchase from a refinance, and books the consultation or flags an urgent lead to you, so the borrower never rolls to voicemail and calls the next broker. It does intake and scheduling only, and never quotes a rate or promises an approval.",
    "bridge_slug": "ai-receptionist-for-mortgage-brokers",
    "bridge_label": "AI receptionist for mortgage brokers",
    "faqs": [
        ("Would a borrower rather reach a real person?",
         "What a borrower needs most is a fast, professional response, and a calm voice that captures their details and books a time beats a voicemail box every time. The AI receptionist is upfront about what it is, qualifies the lead, and hands anything that needs a licensed conversation straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are in an application, at a closing, or already on another call. Something that always answers and qualifies is what catches the leads a forward would still miss.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do My Mortgage Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-mortgage-leads-go-cold",
    "h1": "Why Do My Mortgage Leads Go Cold?",
    "title": "Why Do My Mortgage Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Mortgage leads go cold because a loan is a long process and most borrowers are not ready the day they call. Without steady follow-up they forget who they spoke to.",
    "answer": "Mortgage leads go cold because a loan is a long process and most borrowers are not ready the day they inquire. A pre-approved buyer keeps getting outbid, a refinance caller is waiting to move. Without steady follow-up they forget which broker they spoke to and go with whoever kept in touch. The lead was rarely bad, just neglected.",
    "sections": [
        {"h2_html": "The lead was fine, the pipeline is just <em>long</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A mortgage is rarely won or lost in one conversation. A pre-approved buyer can house hunt for months before an offer sticks. A homeowner asking about a refinance may sit and wait for the right moment. A purchase lead goes quiet in the weeks between the first call and an accepted contract. None of those are bad leads, they simply need a light touch across a long stretch, and that stretch is exactly where there is no time to work every one by hand between applications and closings.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The broker who funds the loan is usually not the one with the sharpest pitch on day one. It is the one who stayed in front of the borrower the whole way, a friendly check-in, a quick answer to the question they were stuck on, so their name is still the one the borrower has saved when the moment finally comes. That second, third, and tenth touch is what turns a maybe into a closing, and it is the first thing to fall off a busy week.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Brokers do not skip follow-up because they are lazy. They skip it because the day fills up. You finish an application, roll to the next file, handle the buyer who needs a pre-approval letter before the weekend, and by evening the lead from three weeks ago is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest leads to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system flagging which pre-approvals are aging or which leads went quiet after the first call.</li><li>The follow-up depends on you remembering, so it competes with the loans on your desk and loses.</li><li>By the time you circle back, the borrower has locked with the broker who beat you to it.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and it just runs. When every lead and open loan gets timed check-ins automatically, written to sound like you, the borrower comparing brokers keeps hearing from you while the others go silent, and it all stays compliant, never promising a rate or a result.</p>'}],
    "bridge_h2": "Work every lead through the whole pipeline",
    "bridge_text": "A CRM keeps every lead and open loan in front of you and sends timed check-ins for you, from the first call to closing and beyond, so a pre-approved buyer still shopping and a refinance that is months out keep hearing from you while the other brokers go quiet. Your name stays the one they call, and it never promises a rate or a result.",
    "bridge_slug": "crm-for-mortgage-brokers",
    "bridge_label": "CRM for mortgage brokers",
    "faqs": [
        ("How often should I follow up on a mortgage lead?",
         "It depends on how far out they are, which is the point: a pre-approved buyer still shopping needs a light touch every few weeks, a refinance lead needs to hear from you when the timing shifts. The key is that it happens at all and on schedule, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not spammy, and it stays on the right side of compliance, never promising a rate or a result. You can always jump in and reach out to anyone directly.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ How Do Mortgage Brokers Get More Leads? (how-to -> marketing) ============
{
    "slug": "how-do-mortgage-brokers-get-more-leads",
    "h1": "How Do Mortgage Brokers Get More Leads?",
    "title": "How Do Mortgage Brokers Get More Leads? | Top Shelf Business Solutions",
    "meta_desc": "The steadiest mortgage leads come from referral agents and past clients, with local search catching the rest. A consistent, trusted presence beats one big ad push.",
    "answer": "The steadiest mortgage leads come from two places most brokers underwork: real estate agents who refer buyers, and past clients who refinance, buy again, or send family. Being easy to find for a mortgage broker near me catches the rest. A consistent, trusted presence across all three, not one big ad push, is what fills the pipeline.",
    "sections": [
        {"h2_html": "Referral agents are the <em>engine</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The most reliable pipeline a broker can build is a handful of real estate agents who send every buyer who needs financing. Those relationships are worth more than any single ad, and they run on trust: an agent puts their own reputation on the line with every referral, so they hand buyers to the broker who looks established, is well reviewed, and picks up when their client calls. A broker who is invisible online or slow to answer makes the agent look bad, and the next referral goes elsewhere.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So more referral business is less about asking and more about being the obvious, safe choice when an agent needs a name. That means a public presence an agent can point to, recent reviews that back up the introduction, and a phone that always gets answered so the buyer they send never hits voicemail. Stay visible and responsive and you become the broker they recommend by default, deal after deal.</p>'},
        {"h2_html": "Past clients and being found when someone <em>searches</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The other steady source is the business you have already earned. A past client is the cheapest loan you will ever get again, they refinance when the timing moves, buy again, and send family your way, but only if they still have your name when the moment comes. A light, steady presence keeps you the broker they think of instead of whoever comes up first in a search.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And when a borrower with no referral goes looking, they usually start by searching for a mortgage broker near me, where your Google Business Profile is often the first thing they see, above your website. A profile that is active, complete, and full of recent reviews beats one that looks abandoned, and it is a quiet advertisement running in the exact spot people look when deciding who to trust with the largest loan of their life. No honest company can promise you a specific spot on the map, but a free audit will show you what a borrower or an agent sees when they look you up today.</p>'}],
    "bridge_h2": "Be the broker borrowers and agents already know",
    "bridge_text": "Marketing for mortgage brokers keeps you visible and trusted where borrowers and referral agents look before they ever call, your Google profile, your reviews, and a steady public presence, so when someone is ready to hand over their financial life or an agent needs a broker to recommend, your name is the one they already know. It pairs with the CRM that follows up privately with everyone in your database, and it stays compliant, never promising a rate or an approval.",
    "bridge_slug": "marketing-for-mortgage-brokers",
    "bridge_label": "Marketing for mortgage brokers",
    "faqs": [
        ("What is the best source of mortgage leads?",
         "For most brokers it is referral agents and past clients, not cold ads. Those leads close faster and cost almost nothing to earn, because the trust is already there. Being findable when a stranger searches for a mortgage broker near you catches the rest, but the relationships are the engine."),
        ("How long before marketing brings in leads?",
         "Recognition and reviews build over months, not days, which is exactly why most brokers give up before it pays off. There is no honest shortcut to being the name an agent or a borrower already trusts, but a steady presence compounds, and a free audit shows you where you stand today.")],
    "trade_slug": "mortgage_brokers", "trade_plural": "mortgage brokers",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
]
