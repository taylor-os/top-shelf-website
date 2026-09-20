"""Colony page specs for ESTATE PLANNING ATTORNEYS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an estate planning firm owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Each dict here owns UNIQUE, hand-written, estate-planning-specific substance (the generator owns
shell, schema, events, keyword placement). Same honesty rules as the money specs: no invented
stats, prices, or clients; hedge instead of overpromise; only the real prices ($299/$899/$2,500
plans, $1,500 one-time site) ever appear; no em/en dashes anywhere; never "leak" as a metaphor.
LEGAL ETHICS: no promised outcomes, tax savings, or results ever; the AI handles intake and
booking, never legal advice; every page reads as attorney-advertising compliant, and only
illustrative scenarios appear, never a named client or competitor.

Estate planning is the deferred task, not the urgent one. People finally act after a death in the
family, a new baby, a diagnosis, a marriage, or retirement. The clients skew older and value a
calm, unhurried, trustworthy first contact. Work arrives by referral from financial advisors and
CPAs and by seminar, the consideration window runs long, and probate is the reactive side. Patient
follow-up wins. That reality, not urgency, leads every page.

Six questions, mixed cost / problem / how-to, spread across three money pages:
  1 estate-planning-attorney-website-cost             (cost)    -> websites-seo-for-estate-planning-attorneys
  2 estate-planning-answering-service-cost            (cost)    -> ai-receptionist-for-estate-planning-attorneys
  3 is-a-crm-worth-it-estate-planning                 (cost)    -> crm-for-estate-planning-attorneys
  4 why-estate-planning-firms-miss-calls              (problem) -> ai-receptionist-for-estate-planning-attorneys
  5 why-estate-planning-leads-go-cold                 (problem) -> crm-for-estate-planning-attorneys
  6 how-do-estate-planning-attorneys-get-more-clients (how-to)  -> marketing-for-estate-planning-attorneys
"""

TOPICS = [
# ========= How Much Does an Estate Planning Attorney Website Cost? (cost -> websites-seo) =========
{
    "slug": "estate-planning-attorney-website-cost",
    "h1": "How Much Does an Estate Planning Attorney Website Cost?",
    "title": "How Much Does an Estate Planning Attorney Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An estate planning attorney website ranges from a cheap template to several thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "An estate planning attorney website can run from a couple hundred dollars for a DIY template to several thousand for a custom build. What matters more than the price is whether it ranks and earns the trust of a cautious client. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What actually drives the <em>price</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The number you see quoted for an estate planning attorney website swings widely because you are not all buying the same thing. A template you fill in yourself and a custom site built to rank in your area and reassure an anxious visitor are different products with the same name. Before you compare quotes, it helps to know what you are actually paying for.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A do-it-yourself website builder is cheap monthly, but you do the work, and it is rarely built to rank or to make an older, careful client feel they have reached an established firm.</li><li>A one-time custom build costs more up front and is yours to keep, but a site alone does little if nobody is doing the ongoing SEO to get it found.</li><li>An agency retainer bundles the build with ongoing SEO and updates, which is where most of the long-term value lives, and also where the monthly cost lives.</li><li>Hidden costs to ask about before you sign: who owns the site, what a change costs, and whether you keep it if you leave.</li></ul>'},
        {"h2_html": "What an estate planning firm should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An estate planning website earns its money one way: it turns a person who has finally decided to deal with their will or trust into a booked consultation. That means it has to load fast, rank for the towns you cover and the searches people make when they are ready, a will, a trust, a power of attorney, probate, and put a clear way to book a consultation in front of a visitor who values a calm, unhurried first impression. A handsome site that never ranks and buries your number is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that actually gets it ranking is handled for you. There is no setup fee either way. What no honest firm can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you exactly where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that earns trust and ranks",
    "bridge_text": "An estate planning website is only worth what it brings in. Ours is built to rank for the towns you cover and to meet a cautious client with a calm, established first impression, then wired to follow up on every consultation.",
    "bridge_slug": "websites-seo-for-estate-planning-attorneys",
    "bridge_label": "Websites & SEO for estate planning attorneys",
    "faqs": [
        ("Is a cheap template site good enough for an estate planning firm?",
         "It can get you online, but a template you fill in yourself is rarely built to rank or to make a careful, often older client feel they have reached an established firm, and you do the work of maintaining it. For a practice built on trust, a site that does not get found or does not reassure is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep and host anywhere. On a monthly plan the site is built and hosted for you as part of the plan, and we will tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ======= What Does an Estate Planning Answering Service Cost? (cost -> ai-receptionist) =======
{
    "slug": "estate-planning-answering-service-cost",
    "h1": "What Does an Estate Planning Answering Service Cost?",
    "title": "What Does an Estate Planning Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for estate planning firms often bill per call or per minute. Top Shelf includes an AI receptionist that answers 24/7 and books consultations in the Signature plan at $899/mo.",
    "answer": "Traditional answering services for estate planning firms usually bill per call, per minute, or a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every call, runs the intake, and books the consultation comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a steady month turns into a big bill. An estate practice also tends to get calls that are not quick, an adult child worried about a parent, someone who just lost a spouse and does not know where to start, so a per-minute meter runs longer than you would expect. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a good stretch of inbound interest runs up the cost.</li><li>Per-minute pricing: you pay for talk time, and an estate caller with a lot on their mind is rarely a quick call.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when interest is highest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a person who has spent years meaning to make a will does not leave a voicemail and wait, the resolve drains and the whole matter slides back to someday. The real cost of no coverage is not a monthly fee, it is the estate plan or the probate matter that quietly never happens. But a generic call center reading a script cannot tell a simple will from a trust, cannot recognize a referral handed over by a financial advisor, and cannot meet an anxious caller with the patience the moment calls for. A person deciding to put their affairs in order deserves better than a message pad.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, runs the intake the way your staff would, and books the consultation or flags a time-sensitive matter to your on-call attorney. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One estate plan you would have lost to a voicemail is usually worth well more than the plan costs, and everything it captures after that is on top. It stays in its lane: it handles intake and booking, and it never gives legal advice or predicts how an estate will be handled or taxed.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers day and night, runs a real estate intake, and books the consultation, all on a flat monthly plan.",
    "bridge_slug": "ai-receptionist-for-estate-planning-attorneys",
    "bridge_label": "AI receptionist for estate planning attorneys",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when interest picks up, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the long-postponed will or the probate matter it books instead of losing to voicemail."),
        ("Does it cost extra for nights, weekends, or holidays?",
         "No. It answers around the clock as part of the plan, including the evening call from an adult child worried about an aging parent, with no after-hours surcharge or overage. Setup is included too, with no separate onboarding fee.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Is a CRM Worth It for an Estate Planning Firm? (cost -> crm) ============
{
    "slug": "is-a-crm-worth-it-estate-planning",
    "h1": "Is a CRM Worth It for an Estate Planning Firm?",
    "title": "Is a CRM Worth It for an Estate Planning Firm? | Top Shelf Business Solutions",
    "meta_desc": "For most estate planning firms a CRM pays for itself by reviving one unsigned plan and reminding past clients to update aging documents. It comes in Top Shelf's Signature plan at $899/mo.",
    "answer": "For most estate planning firms, yes. A CRM pays for itself the first time it revives a consultation that never turned into a signed plan, or brings a past client back to update an aging will. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an estate planning firm when you have more unsigned consultations, past clients, and referral partners than you can keep track of by memory, which is most established practices. It is not worth it if you are brand new, taking a handful of matters, and genuinely staying in touch with everyone, though that rarely stays true as you grow. The honest test is simple: how many people sat through a consultation in the last year and never came back to finish, and how many past clients signed a plan that no one has reviewed since? Those are the matters a CRM is built to recover, and in estate work they are the ones most easily forgotten, because nothing forces them and nobody complains when they slip.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for an estate planning firm is not the software, it is the work that stops slipping away. A person who took the folder home to name a guardian and stalled, a couple whose trust was signed six years ago and never revisited, an advisor who used to send you clients and has gone quiet: each one is a matter you have already half-earned and are one patient touch away from booking.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every unsigned consultation on a schedule, with gentle, no-pressure messages, so the person who meant to finish keeps hearing that you are ready whenever they are.</li><li>It reminds past clients when a will or trust is aging or a life change means the plan should be revisited, so the update work comes back instead of never happening.</li><li>It keeps a light, organized touch on the financial advisors and CPAs who refer you, so the pipeline that sends the most work stays warm.</li><li>It keeps every client, plan, and note in one place instead of scattered across a phone and an inbox.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: recover one plan you would have lost and it has paid for itself, and everything after that is margin. It carries the relationship while your attorneys carry the law, and it never promises a client anything about how their estate will be handled or taxed.</p>'}],
    "bridge_h2": "Put your client list to work",
    "bridge_text": "The unsigned consultations, past clients, and referral partners you already have are the cheapest matters you can get. A CRM follows up on every one for you, so they stay with your firm instead of drifting away.",
    "bridge_slug": "crm-for-estate-planning-attorneys",
    "bridge_label": "CRM for estate planning attorneys",
    "faqs": [
        ("Is a CRM overkill for a small estate planning firm?",
         "Not usually. Even a solo practice sees more consultations, past clients, and referral partners than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If unsigned plans go cold and aging documents never get reviewed, a CRM earns its keep."),
        ("How is a CRM different from my drafting and practice-management software?",
         "That software holds the documents, the matter files, and the legal deadlines. A CRM runs everything around them: the consultations you have not signed, the past clients whose plans are going stale, and the advisors who refer you. The two do different jobs and work alongside each other.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do Estate Planning Firms Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-estate-planning-firms-miss-calls",
    "h1": "Why Do Estate Planning Firms Miss So Many Calls?",
    "title": "Why Do Estate Planning Firms Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Estate planning firms miss calls because they ring during signings, drafting, and client meetings, and the caller who finally decided to make a will does not leave a voicemail.",
    "answer": "Estate planning firms miss calls because they come while you are in a signing, drafting, or already gone for the day, and the person who finally worked up the resolve to make a will does not leave a voicemail. They hang up, and the plan slides back to someday. The fix is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes when your firm <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An estate practice is not a phone bank. When a call comes in you are often in a signing, drafting a trust, sitting with a grieving family, or gone for the evening, and none of those are moments you can stop and take a call. A solo or small firm rarely has a full-time receptionist waiting by the phone, so the calls that arrive during a meeting or after five simply roll to voicemail. It is not a discipline problem. A small team cannot do the work in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for this kind of caller it is not one. Someone who has spent years meaning to make a will and finally picked up the phone is fragile in that moment. Reach a machine and the resolve tends to drain away, and the whole matter slides back onto the someday pile, sometimes for another year, sometimes until a family is left sorting out an estate with no plan at all.</p>'},
        {"h2_html": "The race is against putting it off, not a <em>faster firm</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Unlike an emergency trade, this is not a race against the office that answers one ring faster. It is a race against how easily people put off something they would rather not think about. A calm, patient voice on the line, right when they have finally decided to deal with it, is what turns a long-postponed intention into a booked consultation. A voicemail box cannot do that, and a generic call center reading a script does not know a simple will from a trust, does not recognize the office of a financial advisor calling to refer a client, and cannot tell which caller the attorney should hear about today.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">What actually closes the gap is something that answers on the first ring, day or night, meets the caller with patience, and runs the intake an estate matter starts with, whether it is for them or a parent, whether there are minor children or a business, whether someone has passed and they need probate help, and then books the consultation or flags a time-sensitive matter straight to your on-call attorney. It handles intake and booking only. It never gives legal advice and never tells a caller which documents they need, so the moment gets captured while every legal judgment still waits for your attorney.</p>'}],
    "bridge_h2": "Stop letting a long-put-off decision go to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, day or night, meets the caller with patience, runs the intake, and books the consultation or flags it to you, so the moment never slips away.",
    "bridge_slug": "ai-receptionist-for-estate-planning-attorneys",
    "bridge_label": "AI receptionist for estate planning attorneys",
    "faqs": [
        ("Would a client rather reach a real person?",
         "What a caller needs most is to feel that a real, steady firm is handling it, and a calm voice that captures the details beats a voicemail box every time. The AI receptionist is upfront about what it is, gathers the facts, and hands a time-sensitive matter straight to your attorney."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when you are free to answer. Forwarding still rolls to voicemail when you are in a signing, with a client, or after hours. Something that always answers and runs the intake is what catches the calls a forward would still miss.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ============ Why Do My Estate Planning Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-estate-planning-leads-go-cold",
    "h1": "Why Do My Estate Planning Leads Go Cold?",
    "title": "Why Do My Estate Planning Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Most estate planning leads go cold not over price but because the decision is easy to defer and nobody followed up. The client took the folder home, life closed over it, and months passed.",
    "answer": "Most estate planning leads go cold not because your fee was wrong, but because the decision is easy to defer and nobody followed up. The person sat through a consultation, took the folder home, and life closed back over it. A quiet lead is usually not a no, it is a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means deferred, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet lead as a no on price, so you let it go. But most of the time the person did not decide against you at all. They came in about a will or a trust, agreed they needed one, took the folder home to gather account numbers and decide who they want as guardian and executor, and then life got in the way. There is no deadline forcing it, nobody is chasing them, and the task sits with unpleasant questions most people would rather not face, so it slides to the bottom of the list. Months pass. They were never a bad prospect. They simply needed a reason to pick it back up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The firm that gets the matter is usually not the cheapest. It is the one that stayed in front of them, a gentle check-in a couple of weeks later, a note that the plan still matters and you are ready whenever they are. That second touch is what turns a maybe into a signed plan, and it is exactly the thing there is no time for between drafting and signings.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Estate attorneys do not skip follow-up because they are careless. They skip it because the day fills up. You finish a draft, meet the next client, sit with a family through probate, and by evening the consultation from three weeks ago is out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest matters to chase. And estate planning has the longest consideration window of almost any legal work, so a lead can sit for months before it is ready, far longer than anyone can hold in their head.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which consultations never turned into a signed plan and are quietly going cold.</li><li>The follow-up depends on you remembering, so it competes with billable work and loses.</li><li>The window is so long that even a good prospect drifts away before anyone circles back.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every unsigned consultation gets patient, no-pressure check-ins automatically, written to sound like your firm, the person who took the folder home keeps hearing from you at the right moment, instead of quietly getting the plan done somewhere else, or never at all.</p>'}],
    "bridge_h2": "Follow up on every consultation, automatically",
    "bridge_text": "A CRM keeps every unsigned consultation in front of you and sends patient check-ins for you, so the person who has not finished their plan keeps hearing from your firm instead of drifting away.",
    "bridge_slug": "crm-for-estate-planning-attorneys",
    "bridge_label": "CRM for estate planning attorneys",
    "faqs": [
        ("How many times should I follow up on an estate planning lead?",
         "A few light, patient touches spread over weeks or months catches most of the maybes without pressure: a check-in a couple of weeks after the consultation, then gentle reminders that the plan still matters. Because the consideration window is so long, what counts is that it keeps happening on schedule, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like your firm and sent at a calm, respectful pace. A short, no-pressure note reads as attentive, not pushy, and most people appreciate it because they meant to finish and simply let it slide. You can always step in and reach anyone yourself.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
# ======= How Do Estate Planning Attorneys Get More Clients? (how-to -> marketing) =======
{
    "slug": "how-do-estate-planning-attorneys-get-more-clients",
    "h1": "How Do Estate Planning Attorneys Get More Clients?",
    "title": "How Do Estate Planning Attorneys Get More Clients? | Top Shelf Business Solutions",
    "meta_desc": "Estate planning attorneys get more clients from referral partners, education, past clients, and local search, then patient follow-up over a long consideration window. Here is where the work comes from.",
    "answer": "Estate planning attorneys get more clients from a few steady sources: referrals from financial advisors and CPAs, educational seminars and content, past clients returning to update plans, and showing up in local search when someone is ready. None of it is urgent, so the firm that stays visible and follows up patiently over a long consideration window wins the work.",
    "sections": [
        {"h2_html": "Where estate planning clients <em>actually come from</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Estate planning is not an impulse purchase, so the marketing that works is different from an urgent trade. Almost nobody wakes up needing a will today; they act after a death in the family, a new baby, a diagnosis, a marriage, or retirement finally makes it feel real. That means the goal is to be the trusted, familiar name at the moment a person is ready, not the loudest ad in the meantime. A handful of channels carry most of the work.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Referrals from financial advisors, CPAs, and insurance agents, who each sit on a book of clients who all need a plan. For most firms this professional network is the single largest source of new matters.</li><li>Education, the classic seminar or workshop and plain-English content that answers what a will, a trust, or probate actually involves, which builds trust long before a person ever calls.</li><li>Past clients and their families, who come back to update an aging plan and return for administration and probate when someone passes.</li><li>Local search, so that when someone finally looks for an estate planning attorney near them, your firm is there with genuine reviews that reassure a cautious buyer.</li></ul>'},
        {"h2_html": "How to actually get more, <em>consistently</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting more clients is less about one clever campaign and more about staying visible and following up over a window that can run months, which is exactly what falls apart when a firm is busy. A repeatable process beats good intentions.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep your referral partners warm with a steady, organized touch, a thank-you when they send someone, a check-in so you stay top of mind, so the network that sends the most work does not quietly go cold.</li><li>Keep your Google Business Profile verified, complete, and gathering honest reviews, because trust signals matter more to an older, careful client than to almost any other buyer.</li><li>Publish patient, educational content that meets people while they are still deciding, so your firm is the one that taught them what they needed to know.</li><li>Follow up on every consultation and remind past clients when a plan is aging, so the interest you already earned turns into signed work.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this promises a result, and no honest firm markets that way. What it does is keep you visible and trusted so that when a person is finally ready, yours is the name that comes to mind. A free audit can show you which of these channels your firm is leaving on the table right now.</p>'}],
    "bridge_h2": "Become the name they call when they are ready",
    "bridge_text": "Estate planning clients arrive on their own schedule, not yours. Marketing that keeps your firm visible, trusted, and in front of your referral partners is how you are the one they call when the moment finally comes.",
    "bridge_slug": "marketing-for-estate-planning-attorneys",
    "bridge_label": "Marketing for estate planning attorneys",
    "faqs": [
        ("What is the best source of estate planning clients?",
         "For most firms it is referral relationships with financial advisors, CPAs, and insurance agents, who each know many people who need a plan. Those relationships send steady work for years, but they go cold when neglected, so the firms that win keep a patient, organized touch on every partner."),
        ("How long does estate planning marketing take to work?",
         "Longer than an urgent trade, because people act on their own timeline, after a life event rather than a search alone. The work is to stay visible and trusted so you are the name they remember when they are ready. Nobody controls Google or a person's timing, so no honest firm promises a specific result.")],
    "trade_slug": "estate_planning_attorneys", "trade_plural": "estate planning attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
},
]
