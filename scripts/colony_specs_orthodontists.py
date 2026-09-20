"""Colony page specs for ORTHODONTISTS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question an orthodontic practice owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Orthodontics is NOT routine dentistry. The business runs on consult-driven case starts: braces
and Invisalign are big-ticket cases that run eighteen to twenty-four months, parents book for
teens and adults self-refer, the free consult converts to a signed case start over weeks (which
a CRM nurtures), general dentists refer, and financing questions decide calls. A missed consult
call or an un-followed-up consult is a whole case lost. Every dict keeps that reality, distinct
from a general dentist doing cleanings and checkups.

Same honesty rules as the money specs: no invented stats, percentages, or clients; only the real
prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear; no em/en dashes anywhere;
never "leak" as a metaphor. Ethics: the AI does scheduling and intake only, never clinical or
treatment advice; no treatment, smile, or outcome guarantees; caller information is handled with
HIPAA-aware discretion.

Six questions, mixed cost / problem / how-to, funneling into four money pages:
  1 orthodontist-website-cost              (cost)    -> websites-seo-for-orthodontists
  2 orthodontic-answering-service-cost     (cost)    -> ai-receptionist-for-orthodontists
  3 is-a-crm-worth-it-for-an-orthodontist  (cost)    -> crm-for-orthodontists
  4 why-orthodontic-offices-miss-calls     (problem) -> ai-receptionist-for-orthodontists
  5 why-orthodontic-consults-dont-convert  (problem) -> crm-for-orthodontists
  6 how-do-orthodontists-get-more-patients (how-to)  -> marketing-for-orthodontists
"""

TOPICS = [
# ==================== How Much Does an Orthodontist Website Cost? (cost -> websites-seo) ====================
{
    "slug": "orthodontist-website-cost",
    "h1": "How Much Does an Orthodontist Website Cost?",
    "title": "How Much Does an Orthodontist Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "An orthodontist website's job is booking free consults, not looking pretty. Top Shelf builds one that ranks and books for $1,500 one-time, or free on a plan.",
    "answer": "An orthodontist website can run from a few hundred dollars to several thousand, but the number that matters is how many consults it books. An orthodontic site has one main job: turn a researching parent or adult into a booked free consult. Top Shelf builds a custom five page site for $1,500 one-time, or free on any monthly plan.",
    "sections": [
        {"h2_html": "What an orthodontic website is actually <em>for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you weigh what a website costs, get clear on what an orthodontic one is for, because it is not a brochure. Its single most important job is booking the free consult. Everything else on the page exists to move a researching parent or a self-conscious adult toward one action: booking that consult. So the real money question is whether the site does that job, not what it costs to build.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A free-consult request that is obvious on every screen, phone included, because that booking is the whole funnel, not a buried contact form.</li><li>A gallery of real finished cases the practice has treated, so a nervous parent can see the actual work before they pick up the phone.</li><li>A plain-language explainer of braces versus Invisalign, with clear financing and payment-plan information, since cost and options are what visitors want answered first.</li><li>An experience that speaks to both audiences at once, the parent booking for a teen and the adult booking for themselves, rather than to one and not the other.</li><li>Pages and words built to show up for the searches people actually make, braces, Invisalign, and orthodontist near me, in the towns you serve.</li></ul>'},
        {"h2_html": "What it should <em>earn back</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Judge the cost against what one case is worth. An orthodontic case is eighteen to twenty-four months of treatment, often the siblings after it, and the referrals a happy family sends, so a site that books even a handful of extra consults a year has paid for itself many times over. That is why a cheap template that never ranks and buries the consult button is the most expensive option: you paid for it and it starts no cases. A site that loads fast, ranks for your towns, and makes booking effortless is the one that earns its price back.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps the pricing plain. A custom five page site on its own is $1,500 one-time, yours to keep and host anywhere, with no plan and no commitment. Or it is included free, built and hosted, on any monthly plan starting at $299, where the ongoing SEO that gets it ranking for braces, Invisalign, and orthodontist near me is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site built to start cases",
    "bridge_text": "An orthodontic website is only worth the consults it books. Ours is built to rank for the towns you serve, speak to parents and adults alike, and make requesting the free consult effortless, then wired to follow up on every one.",
    "bridge_slug": "websites-seo-for-orthodontists",
    "bridge_label": "Websites & SEO for orthodontists",
    "faqs": [
        ("Can the website show my before-and-after cases and explain financing?",
         "Yes, and it should. A gallery of your real finished cases lets a nervous parent see the work, and a clear braces-versus-Invisalign explainer with financing and payment-plan details answers what visitors ask first, so more of them book the free consult instead of leaving to look elsewhere."),
        ("Do I own the website, and does it work with my scheduling?",
         "Yes. If you buy the one-time $1,500 site it is yours to keep and host anywhere; on a monthly plan it is built and hosted for you. Either way the free-consult requests it captures flow to you and can feed the same system that follows up on the ones who do not book right away.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ What Does an Orthodontic Answering Service Cost? (cost -> ai-receptionist) ============
{
    "slug": "orthodontic-answering-service-cost",
    "h1": "What Does an Orthodontic Answering Service Cost?",
    "title": "What Does an Orthodontic Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for orthodontists often bill per call or minute. Top Shelf includes an AI receptionist that books consults 24/7 in the $899 Signature plan.",
    "answer": "Traditional answering services for orthodontists usually bill per call, per minute, or on a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different path: an AI receptionist that answers every consult call, books the free consult, and runs 24/7 comes in the Signature plan at $899 a month flat, with no per-call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. An orthodontic office also fields calls at the times a live service charges the most: evenings and weekends, when a working parent finally has a minute to call about braces. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price-shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so the insurance and financing questions parents always ask, the long ones, cost you the most.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: a parent who just decided to look into braces does not leave a voicemail, they call the next office on the list. The real cost of no coverage is not a monthly fee, it is the consult that booked somewhere else, and one orthodontic case is eighteen to twenty-four months of treatment, siblings, and referrals. But a generic call center reading a script cannot tell a new consult from a poking wire, or a financing question from an insurance one, so you can pay for coverage and still lose the case.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, days, nights, and weekends, and does one job well: it warmly answers the cost, insurance, and financing questions, books the free consult on your calendar, and flags a real problem like a broken bracket to your team. It does scheduling and intake only, never clinical advice, and treats what a caller shares with the discretion a dental office is held to. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter. One case you would have lost on a weekend can be worth well more than the plan, and what it books after that is on top.</p>'}],
    "bridge_h2": "Answer every consult without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers 24/7, handles the cost and financing questions, and books the free consult, all on a flat monthly plan. It schedules and intakes only, and hands anything clinical to your team.",
    "bridge_slug": "ai-receptionist-for-orthodontists",
    "bridge_label": "AI receptionist for orthodontists",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when parents are calling most, while the AI receptionist is a flat part of the $899 Signature plan with no meter. The bigger saving is the after-hours consult it books instead of losing to voicemail."),
        ("Does it give patients dental or treatment advice?",
         "No. It handles scheduling and intake only: it books the free consult, answers what you allow about cost, insurance, and financing, and flags a broken bracket or real pain to your team. It never offers clinical or treatment advice, and you set exactly what it can say.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============== Is a CRM Worth It for an Orthodontic Practice? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-an-orthodontist",
    "h1": "Is a CRM Worth It for an Orthodontic Practice?",
    "title": "Is a CRM Worth It for an Orthodontic Practice? | Top Shelf Business Solutions",
    "meta_desc": "For most orthodontists a CRM pays for itself by starting one stalled consult and reviving referrals. It is in Top Shelf's $899 Signature plan, not a separate bill.",
    "answer": "For most orthodontic practices, yes. A CRM pays for itself the first time it starts a consult that would have gone cold, or brings a family back when a younger sibling is ready. It only stops being worth it if you already follow up on every consult and referral by hand. Top Shelf includes it in the $899 Signature plan.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for an orthodontic practice when you give more consults than anyone can personally chase, and when cases start weeks after the first visit rather than the same day, which describes almost every practice. It is not worth it if you are giving a handful of consults a month and genuinely following up on each one, plus every referring dentist and every stalled patient, from memory. The honest test is simple: how many consults in the last few months did someone hear the plan, say they would think it over, and never come back to? Every one of those is a multi-thousand-dollar case a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for an orthodontist is not the software, it is the case that stops slipping away. A parent who walked out to think about braces, an adult waiting for the insurance year to reset, a referring dentist who has not heard from you in months, a family whose younger child is now the right age: each one is a case you have already half-earned and are one well-timed message away from starting.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every unstarted consult on a schedule you set, so the parent weighing three offices keeps hearing from you, with a gentle reminder that payment plans make it doable.</li><li>It keeps referring dentists warm and closes the loop when their patient finishes, so the offices that feed you cases do not go quiet.</li><li>It brings back stalled, retainer, and sibling patients from the same record, which costs almost nothing next to chasing brand-new consults with ads.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and follow-up that feed it. The math is the same as the answering service: start one case you would have lost and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your consults and referrals to work",
    "bridge_text": "The consults you already gave and the dentists who already refer you are the cheapest cases you can start. A CRM follows up on every one for you, so the parent thinking it over books with you instead of the office that stayed in touch.",
    "bridge_slug": "crm-for-orthodontists",
    "bridge_label": "CRM for orthodontists",
    "faqs": [
        ("Is a CRM overkill for a small orthodontic practice?",
         "Not usually. Even a single-doctor practice gives more consults and treats more families than anyone can track by memory, and cases start weeks later. The point is not size, it is whether follow-up is falling through. If consults go cold and referring dentists forget your name, a CRM earns its keep."),
        ("How is a CRM different from my practice management software?",
         "Practice software records who came in; it does not chase the consult that never started, keep a referring dentist warm, or reach a family when a sibling is ready. A CRM sits alongside it as the follow-up layer that actively brings cases back, on a schedule you set.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Do Orthodontic Offices Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-orthodontic-offices-miss-calls",
    "h1": "Why Do Orthodontic Offices Miss So Many Calls?",
    "title": "Why Do Orthodontic Offices Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Orthodontic offices miss calls because the front desk is chairside when consults ring, and a parent researching braces calls the next office, not voicemail.",
    "answer": "Orthodontic offices miss calls because the person up front is often chairside, seating a patient or handing over an archwire, when the phone rings. A parent researching braces does not leave a voicemail; they call the next office and book where someone answers. The fix is not working harder, it is making sure every consult call gets picked up.",
    "sections": [
        {"h2_html": "The consult call rings while the desk is <em>chairside</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">An orthodontic front desk is rarely just a front desk. The same person greeting patients is often chairside too, seating someone for an adjustment, passing an assistant an archwire, or checking a family out between appointments. So when a consult call comes in during a busy clinic, it rings through to voicemail while the team is a few feet away with their hands full. It is not a discipline problem. One person cannot seat a patient and answer every call at the same moment, and the busier the schedule, the more calls slip.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for a new consult it is not one. A parent who just talked themselves into looking into braces, or an adult finally ready to fix their own smile, is not going to leave a message and wait. They move down the list until someone picks up, and by the time anyone checks the voicemail, the consult is already booked down the road.</p>'},
        {"h2_html": "A missed consult is a whole case that <em>starts elsewhere</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. A missed consult is not one lost appointment; it is eighteen to twenty-four months of treatment, the siblings who come of age after, and the referrals a happy family sends from the same school and neighborhood. Many of those calls come in the evening or on a weekend, exactly when a working parent has a free minute and exactly when a busy office is least able to answer. So the calls you are most likely to miss are also the ones worth the most.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and can tell a new consult from a poking wire. A voicemail box cannot triage, and a generic call center does not know what to say when a parent asks about financing. What works is something that answers on the first ring day or night, warmly handles the cost and insurance questions, books the free consult on your calendar, and flags a real problem like a broken bracket to your team, so the case your marketing worked to earn actually lands on the schedule.</p>'}],
    "bridge_h2": "Stop sending consults to voicemail",
    "bridge_text": "An AI receptionist answers every call on the first ring, days, nights, and weekends, handles the questions a parent asks first, and books the free consult or flags a real problem to your team, so the case never rolls to voicemail.",
    "bridge_slug": "ai-receptionist-for-orthodontists",
    "bridge_label": "AI receptionist for orthodontists",
    "faqs": [
        ("Would a parent rather reach a real person?",
         "What a parent wants most is a warm, clear answer and an easy way to book, and that beats a voicemail box every time. The AI receptionist is upfront about what it is, answers what you allow about cost and insurance, books the consult, and hands anything clinical or urgent to your team."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when the whole team is chairside or already on another call, which is exactly when consults come in. Something that always answers and books is what catches the calls a forward would still miss.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ Why Don't My Orthodontic Consults Convert? (problem -> crm) ============
{
    "slug": "why-orthodontic-consults-dont-convert",
    "h1": "Why Don't My Orthodontic Consults Convert?",
    "title": "Why Don't My Orthodontic Consults Convert? | Top Shelf Business Solutions",
    "meta_desc": "Most orthodontic consults that do not start were never a no. The family got busy, waited on insurance or budget, and nobody followed up, so the case went cold.",
    "answer": "Most orthodontic consults that do not convert were never a no. The parent liked the plan but wanted to talk it over, wait for the insurance year, or fit the budget, then got busy, and between a full schedule of adjustments nobody circled back. A stalled consult is usually a maybe that needed one warm, well-timed follow-up.",
    "sections": [
        {"h2_html": "A stalled consult is a maybe, not a <em>no</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a consult that did not start as a no on price, so you let it go. But most of the time the family did not decide against you at all. Starting braces or Invisalign is a considered, multi-thousand-dollar decision, so a parent hears the plan, means to talk it over with a spouse, wait until the new insurance year, or line up the budget, and then life crowds it out. An adult does the same, then gets busy. They walk out genuinely interested and simply never get back to it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The consult that converts is usually not the cheapest office. It is the one that stayed in touch: a warm check-in a few days later, a note when the new benefits reset, a gentle reminder that payment plans make the monthly number manageable. That second touch is what turns a maybe into a started case, and it is exactly what there is no time for between chairside appointments.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Practices do not skip follow-up because they do not care. They skip it because the clinic day fills up. You finish an adjustment, seat the next patient, handle the poking wire that jumped the line, and by evening the consult from Tuesday is out of sight. Doing it from memory means it only happens when things are slow, which is exactly when you have the fewest consults to nurture.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system holding the unstarted treatment plans and telling you which ones are going cold.</li><li>The follow-up depends on someone remembering, so it competes with a room full of patients and loses.</li><li>By the time anyone circles back, the family has forgotten the details or booked the office that reached out first.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not an effort problem, and it is the kind of thing you fix once and it just runs. When every unstarted consult gets a few timed, warm check-ins automatically, written to sound like the office the family already trusts and able to reassure them about the money, the parent who meant to start hears from you again while the smile is still on their mind, and the case you already earned begins.</p>'}],
    "bridge_h2": "Follow up on every consult, automatically",
    "bridge_text": "A CRM holds every unstarted treatment plan and sends warm, timed check-ins for you, reassuring a family that payment plans make it doable, so the parent thinking it over books with you instead of drifting away.",
    "bridge_slug": "crm-for-orthodontists",
    "bridge_label": "CRM for orthodontists",
    "faqs": [
        ("How many times should I follow up on a consult that did not start?",
         "A few light touches over the first weeks catches most of the maybes without being pushy: a check-in a few days after the consult, a note when the insurance year resets, and a reminder that payment plans make it manageable. What matters is that it happens on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal to families?",
         "Not when it is written to sound like your office and sent at a sensible pace. A short, warm note reads as attentive, not pushy, and most families appreciate the nudge because they meant to start and got busy. You can always step in and message anyone directly.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
# ============ How Do Orthodontists Get More Patients? (how-to -> marketing) ============
{
    "slug": "how-do-orthodontists-get-more-patients",
    "h1": "How Do Orthodontists Get More Patients?",
    "title": "How Do Orthodontists Get More Patients? | Top Shelf Business Solutions",
    "meta_desc": "Orthodontists get more patients by showing up on Google, earning reviews, tending referring dentists, and answering and following up on every consult call.",
    "answer": "Orthodontists get more patients on two fronts: being found by families searching for braces or Invisalign, and being fed by the general dentists who refer. That means a Google Business Profile and a site that rank, steady reviews, and warm referral relationships. The catch is that new demand only pays off if every consult call is answered and followed up.",
    "sections": [
        {"h2_html": "Get found where families and <em>dentists both look</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Orthodontics runs on two engines, so growth means feeding both. When a parent searches for braces or Invisalign near them, the first thing Google shows is the map pack, the three local listings with star ratings, and most people choose from those without scrolling further. Getting there runs on your Google Business Profile: whether it is verified, complete, and active, how close you are to the searcher, and how many recent, genuine reviews you have. A neglected profile sits below the offices that keep theirs active, no matter how good your work is.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep the Google Business Profile verified, complete, and active, with recent photos and posts, so it does not read as abandoned.</li><li>Build a steady flow of real reviews and reply to every one, which reassures the next parent and helps your local ranking.</li><li>Rank the website for the towns you serve and the searches parents and adults make when they are weighing treatment.</li><li>Tend the referring dentists who send you cases, since those relationships are some of the best patients you get.</li></ul>'},
        {"h2_html": "New demand only pays off if <em>you catch it</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Here is the part most marketing advice skips: getting found is only half the job. A parent who finds you in the map pack still has to reach a person, get their cost and insurance questions answered, and book the free consult, and an adult weighing Invisalign still needs a warm reply before the interest fades. If the calls your visibility earns ring to voicemail while the desk is chairside, or the consult that came in never gets a follow-up, you paid to earn cases that start somewhere else anyway.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the practices that grow treat visibility and follow-through as one system: rank and get reviewed to earn the call, answer every call and book the consult, then nurture the families who do not start the same day and the dentists who refer. What no honest company can promise is a specific ranking or a set number of new patients, because no one controls Google, but keeping the profile active, the reviews steady, and every consult answered and followed up is what actually moves the number. A free audit can show you where patients are slipping today.</p>'}],
    "bridge_h2": "Get seen, then catch every case",
    "bridge_text": "Most orthodontic patients begin with a Google search or a dentist referral. Marketing keeps your profile ranking, your reviews steady, and your referral network warm, then makes sure every consult it earns is answered and followed up.",
    "bridge_slug": "marketing-for-orthodontists",
    "bridge_label": "Marketing for orthodontists",
    "faqs": [
        ("Do I need a new website to get more orthodontic patients?",
         "Not to appear in the map pack, which runs on your Google Business Profile. A verified, active, well-reviewed profile is often the fastest way to get found. A site that ranks helps you show up in the results below the map and gives families a place to book, so the two work together."),
        ("What is the highest-value marketing for an orthodontist?",
         "Usually the two you already partly own: a steady flow of real reviews on an active Google profile, and warm relationships with the general dentists who refer. Both are low-cost next to ads, and both compound, as long as the consults they produce are answered and followed up.")],
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
},
]
