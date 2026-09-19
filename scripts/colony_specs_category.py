"""Colony page specs for the CATEGORY set (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. These pages
are different from the trade colonies: they answer the CATEGORY-level questions a local-business
owner searches BEFORE they know Top Shelf exists, the "who does all of this at once" and
"is it worth it" and "what does it cost" questions. They are deliberately NOT trade-specific,
and they avoid the unwinnable generic "digital marketing agency" head term. Each funnels its
authority into the ONE money page the question implies (why-us, pricing, or websites-seo).

Same honesty rules as every other spec: no invented stats, prices, or clients; hedge instead of
overpromise; the ONLY prices that ever appear are the real ones (Essentials $299, Signature $899,
Platinum $2,500, and the $1,500 one-time standalone site); the CRM and AI receptionist are the
$899 Signature plan, never the $299 tier. No em or en dashes anywhere. "Find the gap", never
"leak" as a metaphor. hub is "Why Top Shelf" for all six; trade_slug is empty (not a trade page).

Six questions, mixed can-one / best / vs / cost / worth-it / how-to:
  1 can-one-company-do-website-crm-reviews        -> why-us
  2 best-all-in-one-software-for-local-business    -> why-us
  3 marketing-agency-vs-software-small-business    -> why-us
  4 cost-to-modernize-local-business-online        -> pricing
  5 is-done-for-you-marketing-worth-it             -> why-us
  6 how-local-business-gets-more-customers-online  -> solution-websites-seo
"""

TOPICS = [
# ============ Can One Company Handle Website, CRM, Reviews, Phone? (why-us) ============
{
    "slug": "can-one-company-do-website-crm-reviews",
    "h1": "Can One Company Handle My Website, SEO, Reviews, and Phone?",
    "title": "Can One Company Handle My Website, SEO, Reviews, and Phone? | Top Shelf Business Solutions",
    "meta_desc": "Yes, one company can handle your website, SEO, reviews, and phone. Here is what to look for so the pieces actually connect instead of five vendors who never talk.",
    "answer": "Yes, one company can handle your website, SEO, reviews, and phone, and for most local owners that beats stitching together five separate vendors. The part that matters is whether those pieces share one system, so a call, a lead, and a review all land in the same place instead of five logins that never talk.",
    "sections": [
        {"h2_html": "Why owners end up juggling <em>five vendors</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Almost nobody sets out to hire five companies. It happens one problem at a time. A web designer builds the site. Later you add a separate service for SEO, an app for review requests, an answering service for the phone, and someone to post on Facebook. Each one solves the problem in front of it, and none of them talk to each other.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The cost is not only five bills and five logins. It is the space between the tools, where the work falls through. A call comes in after hours and the answering service takes a message the CRM never sees. A job wraps up and no review request goes out, because that is a different app nobody opened. The pieces are fine on their own. The gaps between them are where customers slip away.</p>'},
        {"h2_html": "What one company should actually <em>connect</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">One company handling your website, SEO, reviews, and phone is worth it when those pieces share a single system, not just a single invoice. The reason to combine them is that each one should feed the next, so nothing has to be carried by hand from one tool to another.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Someone searches, finds you through SEO and your Google profile, and lands on a fast site that makes them want to call.</li><li>The call gets answered or captured, and the lead drops straight into the CRM instead of onto a sticky note.</li><li>Follow-up goes out on its own, and once the job is done the review request fires automatically.</li><li>Those reviews lift your ranking, so the next searcher finds you too.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">One question matters as much as whether it all connects: who owns it. With Top Shelf your website, domain, Google Business Profile, phone number, and full customer list are yours from day one and exportable any time. The CRM platform and the automations that run on it are the software you subscribe to, the same as any tool you rent. So you get one team and one bill without handing anyone the keys to your business.</p>'}],
    "bridge_h2": "One team instead of five vendors",
    "bridge_text": "You do not have to choose between a stack of disconnected tools and doing it all yourself. Top Shelf runs your website, SEO, reviews, and phone as one connected system, on one bill, with every asset still in your name.",
    "bridge_slug": "why-us",
    "bridge_label": "See how Top Shelf works",
    "faqs": [
        ("Isn't a specialist for each piece better than one company for everything?",
         "A specialist can do great work, but the handoffs between five of them are exactly where leads go cold. One connected system usually beats slightly better parts that never talk to each other. And if a piece ever underperforms, you can see it plainly instead of watching each vendor blame the others."),
        ("If one company runs everything, do they end up owning my business online?",
         "They should not, and with Top Shelf they do not. Your website, domain, phone number, Google Business Profile, and customer list are in your name from day one, and you can export the list whenever you want. Only the CRM software itself is rented, the way any subscription works.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
# ============ Best All-in-One Platform for a Local Business? (why-us) ============
{
    "slug": "best-all-in-one-software-for-local-business",
    "h1": "What's the Best All-in-One Marketing and Software Platform for a Local Business?",
    "title": "What's the Best All-in-One Marketing and Software Platform for a Local Business? | Top Shelf Business Solutions",
    "meta_desc": "The best all-in-one platform for a local business is the one where your website, CRM, reviews, and phone share one system and your customer list stays yours.",
    "answer": "The best all-in-one marketing and software platform for a local business is not the one with the longest feature list. It is the one where your website, CRM, reviews, and phone share a single system, the setup is done for you, and your customer list stays yours. A wall of features you never switch on is not value.",
    "sections": [
        {"h2_html": "Feature lists are the wrong <em>way to compare</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most all-in-one platforms sell you on the length of the feature list. You sign up for forty tools and use four. A pile of features you never switch on is not value, it is a pricier way to do the same three things you actually need. That makes the feature count close to useless for telling one platform from another.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Three questions tell you far more than any feature grid. Is the platform set up for you, or handed over as a login and a blank screen. Do the pieces genuinely connect, so a call becomes a lead becomes a follow-up on their own. And who owns the data if you decide to leave. Answer those and you have compared the only things that matter.</p>'},
        {"h2_html": "What actually makes a platform worth it for a <em>local business</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A local business does not need what a national brand needs. What moves the needle for you is a short list: showing up when people search nearby, answering the phone, following up before a competitor does, and collecting the reviews that pull in the next customer. A platform is only truly all-in-one for you if it covers that list and, ideally, runs it for you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is where most software stops. It hands you the tools and wishes you luck, and the tools sit half-used because running them is a full-time job you do not have. Top Shelf pairs the software with the team that runs it, on one bill starting at $299 a month, with no setup fee. Your website, number, and customer list stay yours the whole time. The honest test of any all-in-one is not what it can do, it is what it actually does for you every week.</p>'}],
    "bridge_h2": "Software plus the team that runs it",
    "bridge_text": "The best platform is the one you do not have to babysit. Top Shelf gives you the connected software and the people who run it for you, so the tools actually get used and your customers stay yours.",
    "bridge_slug": "why-us",
    "bridge_label": "See how Top Shelf works",
    "faqs": [
        ("Do I need every feature an all-in-one platform offers?",
         "No, and paying for forty features to use four is how these platforms get expensive. Start with the gap that is costing you the most right now, usually getting found, catching calls, or following up, and add the rest only when it earns its place. A free audit can tell you which gap to close first."),
        ("What happens to my data if the platform does not work out?",
         "That is the question to ask before you sign anything. With Top Shelf your customer list, website, domain, and phone number are yours and exportable any time, so leaving means you walk away with everything. If a platform makes it hard to get your own data out, treat that as your answer.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
# ============ Hire a Marketing Agency or Buy Software? (why-us) ============
{
    "slug": "marketing-agency-vs-software-small-business",
    "h1": "Should a Local Business Hire a Marketing Agency or Buy Software?",
    "title": "Should a Local Business Hire a Marketing Agency or Buy Software? | Top Shelf Business Solutions",
    "meta_desc": "Should a local business hire a marketing agency or buy software? The honest answer is usually both: the tools plus someone to run them. Here is how to choose.",
    "answer": "Whether a local business should hire a marketing agency or buy software depends on your time, not only your budget. Software costs less but sits unused if nobody runs it. An agency runs the work but often on tools you never own. For most busy owners the honest answer is both: the software, plus a team that runs it.",
    "sections": [
        {"h2_html": "The agency route and the software route each have a <em>catch</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Hiring a marketing agency is the hands-off option. Someone else does the work, which is worth a lot when you are busy running the business. The catch is the price, and the fact that many agencies build everything on their own platform, so the website, the data, and sometimes even the leads technically belong to them. When you leave, you can leave with nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Buying software is the cheaper, more independent option. You own more and you pay less every month. The catch is that software is only as good as the person running it, and that person is you. Between jobs and payroll and everything else, the follow-up and the review requests and the Google posts are exactly what slips. A tool you have no time to run is not really a bargain.</p>'},
        {"h2_html": "Why the choice is usually a <em>false one</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Owners agonize over agency versus software because the choice is framed wrong. What you actually want is the middle the framing leaves out: tools that are set up and run for you, without giving up ownership of your own business. That is the option worth hunting for.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built as that middle. You get the software and the team that runs it on one bill, starting at $299 a month with no setup fee and no long contract, and your website, number, Google profile, and customer list stay in your name. To be fair, the pure options can still fit: a big agency may suit you if you want managed ads at real scale, and do-it-yourself software can be plenty if you already have a marketing person on staff. For most owners with more work than hours, the answer is both together.</p>'}],
    "bridge_h2": "The middle between agency and software",
    "bridge_text": "You should not have to choose between paying an agency that owns your assets and running software you have no time for. Top Shelf gives you both at once: run for you, owned by you, on one bill.",
    "bridge_slug": "why-us",
    "bridge_label": "See how Top Shelf works",
    "faqs": [
        ("Is a marketing agency worth it for a small business?",
         "It can be, if two things are true: the work drives revenue you can actually measure, and the agency does not hold your assets hostage. Before you sign, ask who owns the website and the customer list, and whether the monthly report is in plain English tied to dollars or a wall of vanity metrics."),
        ("Can't I just run the software myself and save the money?",
         "You can, and some owners do it well. The savings are only real if the tool actually gets run every day. If reviews go unrequested and leads go cold because you are out on a job, the work you lose usually costs more than paying someone to run it. Be honest about whether you have the time.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
# ============ How Much to Get a Local Business Set Up Online? (pricing) ============
{
    "slug": "cost-to-modernize-local-business-online",
    "h1": "How Much Does It Cost to Get a Local Business Set Up Online?",
    "title": "How Much Does It Cost to Get a Local Business Set Up Online? | Top Shelf Business Solutions",
    "meta_desc": "Getting a local business online costs a one-time $1,500 for a website, or $299 to $2,500 a month managed. Here is the honest ladder of what each level buys.",
    "answer": "Getting a local business set up online costs less than most owners fear. A custom website is $1,500 one-time. A managed monthly setup that also gets you found, answers the phone, and follows up runs from $299 to $2,500 a month, depending on how much you want handled for you. There is no setup fee either way.",
    "sections": [
        {"h2_html": "The honest cost <em>ladder</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting set up online is not one price, it is a ladder, and where you land depends on how much you want handled for you. Here is the real ladder at Top Shelf, with no setup fee on any of it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A custom five-page website on its own is $1,500 one-time, yours to keep and host wherever you like, with no plan attached.</li><li>Essentials at $299 a month includes that website built and hosted free, Google Business Profile optimization, basic SEO, online booking, automated review requests, and missed-call text-back.</li><li>Signature at $899 a month adds the full CRM, an AI receptionist that answers 24/7 and books the job, advanced SEO every month, customer reactivation, and review responses written for you.</li><li>Platinum at $2,500 a month adds managed ads, social media, Google Business Profile posts, and email and SMS campaigns.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">One thing worth saying plainly, because it is easy to assume otherwise: the CRM and the AI receptionist are part of Signature at $899, not the $299 tier. Essentials gets you online and capturing calls, and Signature is where the system starts following up and answering the phone for you.</p>'},
        {"h2_html": "What actually changes the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number moves for one reason: how much of the work is done for you, and whether you are buying a one-time build or an ongoing system. A website on its own is a fixed, one-time cost, a strong first impression that then sits there. The monthly plans are the opposite, a system that keeps working, ranking you, answering calls, and chasing leads month after month.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A couple of honest notes on the edges. The only pass-through cost is telecom, the phone numbers and text messages billed at cost, the same everywhere in the industry. On Platinum your ad budget goes straight to Google or Meta and you set it, so it never runs through us. Beyond that there are no setup fees and no surprise line items. The fastest way to know which rung you actually need is a free audit of your real numbers, which often shows the cheapest fix is the one you were overlooking.</p>'}],
    "bridge_h2": "See exactly what each plan includes",
    "bridge_text": "The honest ladder runs from a one-time $1,500 website to $299, $899, and $2,500 a month depending on how much you want run for you. The pricing page lays out every plan line by line, with no setup fee and nothing hidden.",
    "bridge_slug": "pricing",
    "bridge_label": "See Top Shelf pricing",
    "faqs": [
        ("Is a one-time website cheaper than a monthly plan?",
         "Up front, yes. A standalone site is $1,500 once, while the plans are monthly. But a site on its own does not get you found or answer your phone, and the monthly plans include the website free and add the system that actually brings in calls. It comes down to whether you need a website or you need customers."),
        ("Does the $299 plan include the CRM and AI receptionist?",
         "No, and it is worth being clear about. Essentials at $299 covers the website, Google Business Profile, basic SEO, online booking, review requests, and missed-call text-back. The full CRM and the AI receptionist that answers 24/7 are on the Signature plan at $899 a month.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
# ============ Is Done-for-You Marketing Worth It? (why-us) ============
{
    "slug": "is-done-for-you-marketing-worth-it",
    "h1": "Is Done-for-You Marketing Worth It for a Local Business?",
    "title": "Is Done-for-You Marketing Worth It for a Local Business? | Top Shelf Business Solutions",
    "meta_desc": "Done-for-you marketing is worth it for a local business when the work would not get done otherwise. Here is how to tell if it pays before you sign.",
    "answer": "Done-for-you marketing is worth it for a local business when the alternative is that the work never happens. Reviews go unrequested, leads go cold, the Google profile sits stale. If you already do all of that consistently, you may not need it. If you are too busy to keep up, paying someone to run it usually pays off.",
    "sections": [
        {"h2_html": "When done-for-you <em>pays off</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The real question is not whether marketing is valuable. It is whether it actually gets done when it is one more thing on your plate. Most owners fully intend to ask every customer for a review, follow up on every quote, and keep the Google profile fresh, and then a full day of real work buries all of it. Done-for-you marketing is worth it precisely when those good intentions keep slipping.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is also where the math tends to work. When the review request goes out after every job instead of the ones you remember, and every lead gets a fast follow-up instead of the ones you get around to, the recovered work usually covers the cost several times over. If you are already doing all of it consistently on your own, you may genuinely not need it. Be honest with yourself about which of those is true.</p>'},
        {"h2_html": "What to check before you <em>sign</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Done-for-you is only worth it if it is the right kind of done-for-you. Plenty of companies do the work and quietly keep you trapped, so a few questions up front save a lot of regret later.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Do you own the results, the website, the phone number, and the customer list, or do they vanish the day you leave.</li><li>Is the reporting in plain English tied to actual money, or a dashboard of impressions that never answers whether it worked.</li><li>Are you locked into a long contract, or free to leave the month it stops earning its keep.</li><li>Is it one team that knows your business, or a call center reading a script.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf is built to pass its own checklist: your assets are yours from day one, reporting is in plain language tied to dollars, plans are month to month, and it is one team rather than a call center. And the fair caveat still stands. If you already have a capable marketing person in-house, doing it yourself can make more sense.</p>'}],
    "bridge_h2": "Done for you, owned by you",
    "bridge_text": "Done-for-you marketing is worth it when the work gets done, the results are yours to keep, and you can see in plain dollars that it is working. That is the standard Top Shelf is built to.",
    "bridge_slug": "why-us",
    "bridge_label": "See how Top Shelf works",
    "faqs": [
        ("Is done-for-you marketing just a pricier version of doing it myself?",
         "Only if you would actually do it yourself. In-house is cheaper on paper, but the savings vanish the moment it stops happening on a busy week. The value of done-for-you is consistency: every review asked for, every lead followed up, every time, which is exactly the part that slips when it is on your own list."),
        ("How do I know done-for-you marketing is actually working?",
         "Insist on reporting tied to dollars, not impressions and sessions: calls captured, leads followed up, reviews earned, money recovered. If a provider cannot show you that in plain English, treat it as a warning sign. You should be able to tell whether it is working without decoding a jargon dashboard.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
# ============ How Does a Local Business Get More Customers Online? (websites-seo) ============
{
    "slug": "how-local-business-gets-more-customers-online",
    "h1": "How Does a Local Business Get More Customers Online?",
    "title": "How Does a Local Business Get More Customers Online? | Top Shelf Business Solutions",
    "meta_desc": "A local business gets more customers online by getting found in local search, converting on a fast site, and answering every lead fast. Here is the order that works.",
    "answer": "A local business gets more customers online by fixing three things in order: getting found in local search and the map pack, turning visitors into calls with a fast, clear website, then answering and following up on every lead quickly. Most owners have one of the three and quietly lose customers at the two they are missing.",
    "sections": [
        {"h2_html": "Getting found is only the <em>first step</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Ask most owners how a local business gets more customers online and they say one word: ranking. Getting found does matter, and for a local business that means the map pack, an active Google Business Profile, and a steady flow of recent reviews. But being found is only the first of three steps, and it is the one people fixate on while the other two quietly cost them customers.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Think of it as a chain: get found, then convert, then capture. Traffic that lands on a slow or confusing website leaves without calling. A call that rings a phone nobody answers becomes a call to your competitor. A gap at any point in the chain is where the customers you already earned slip away, which is why more traffic alone rarely fixes a quiet phone.</p>'},
        {"h2_html": "The chain that turns searches into <em>booked jobs</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more customers online is really about closing every link in that chain, not winning one and losing the rest. Each piece feeds the next, which is what lets it compound over time.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Get found: a verified, active Google Business Profile, real reviews, and on-page SEO so you show up when someone nearby searches.</li><li>Convert: a fast, mobile-first website that makes clear what you do and puts a tap-to-call button in front of the visitor.</li><li>Capture: answer every call, even after hours, follow up within minutes, and ask for the review that lifts you in the next search.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">One honest note: nobody controls Google, so no one can promise you a specific ranking by a specific date. What is true is that these are the levers that move it, and they build on each other. It all starts with being found and having a website ready to turn that attention into a booked job, so that is the sensible place to begin.</p>'}],
    "bridge_h2": "Start where the customers start",
    "bridge_text": "More customers online begins with getting found and landing people on a site built to convert. That is the first link in the chain, and where the whole thing either works or falls apart.",
    "bridge_slug": "solution-websites-seo",
    "bridge_label": "Websites & SEO",
    "faqs": [
        ("What is the fastest way for a local business to get more customers online?",
         "Usually the Google Business Profile and reviews, because that is where local searches start and it can move within weeks. But speed only helps if the rest of the chain is ready, so a site that converts and a phone that gets answered have to be in place, or the new attention just slips away."),
        ("Do I have to pay for ads to get more customers online?",
         "Not to start. Most local customers come from organic local search, reviews, and fast follow-up long before ads enter the picture. Ads can add more on top once the basics convert, but paying for clicks that land on a weak site or an unanswered phone mostly wastes the budget.")],
    "trade_slug": "", "trade_plural": "local businesses",
    "hub_name": "Top Shelf", "hub_slug": "index.html",
},
]
