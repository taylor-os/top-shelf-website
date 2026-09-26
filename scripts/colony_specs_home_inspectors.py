"""Colony page specs for HOME INSPECTORS (plan §5 "Problem/symptom" colony + §6 link-sculpting).
generate_colony.py loads every scripts/colony_specs_*.py and reads TOPICS from each. A colony
page is ONE real question a home-inspection-business owner would search, answered directly up top
(the 40-60 word AEO answer), then two body sections, then a "the fix" bridge that funnels the
page's authority into the ONE money page the question implies. Lighter than a money page.

Home inspectors sit under the Real Estate hub, and the substance is deliberately built around how
that business actually works, so these pages do NOT converge with the plumber template or the
real-estate-agent colony: the work runs on REALTOR REFERRALS (an agent recommends the inspector
who is responsive and easy to book inside a tight option or closing window) plus direct buyers; a
call missed while the inspector is up in an attic or a crawlspace sends the agent to the next name
on the list; the sample report, certifications, and reviews are the trust; and nurturing the
agent-referral network is the CRM and marketing engine.

Same honesty rules as the money specs: no invented stats, prices, or clients; hedge instead of
overpromise; only the real prices ($299/$899/$2,500 plans, $1,500 one-time site) ever appear and
no inspection fee is invented; no em/en dashes anywhere; never "leak" as a money metaphor. The AI
receptionist does scheduling and intake only, with no inspection-outcome or "we find everything"
promise ever implied.

Six questions, mixed cost / problem / how-to, across three money pages:
  1 home-inspector-website-cost               (cost)    -> websites-seo-for-home-inspectors
  2 home-inspection-answering-service-cost    (cost)    -> ai-receptionist-for-home-inspectors
  3 is-a-crm-worth-it-for-a-home-inspector    (cost)    -> crm-for-home-inspectors
  4 why-home-inspectors-miss-calls            (problem) -> ai-receptionist-for-home-inspectors
  5 why-home-inspection-leads-go-cold         (problem) -> crm-for-home-inspectors
  6 how-do-home-inspectors-get-more-referrals (how-to)  -> marketing-for-home-inspectors
"""

TOPICS = [
# ============ How Much Does a Home Inspector Website Cost? (cost -> websites-seo) ============
{
    "slug": "home-inspector-website-cost",
    "h1": "How Much Does a Home Inspector Website Cost?",
    "title": "How Much Does a Home Inspector Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "A home inspector website ranges from a cheap template to a few thousand for a custom build. Top Shelf builds yours for $1,500 one-time, or free on any monthly plan.",
    "answer": "A home inspector website can run from a couple hundred dollars for a template to several thousand for a custom build. What matters more is whether it books inspections and earns agent trust. Top Shelf builds a custom five page site for $1,500 one-time, or includes one free on any monthly plan.",
    "sections": [
        {"h2_html": "What a home inspection <em>website has to do</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before you compare quotes, it helps to know what a home inspection website actually has to accomplish, because that is what you are really paying for. An inspection business does not run on walk-in traffic. It runs on buyers who found you searching in a hurry and on the real estate agents who send you most of your work, and the site has to serve both of those people the moment they land on it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Easy online booking that works around a closing or option deadline, so a buyer or an agent can lock in an inspection date in a few taps instead of waiting for a callback.</li><li>A sample report and your certifications and license shown up front, because the report is the product and visible credentials are what make a nervous buyer and a cautious agent trust you.</li><li>A clear path for agents to refer you, so the person who sends you repeat work can hand your name to a client in one link.</li><li>Built to rank for home inspector near me and for the towns you cover, since that is exactly what a buyer types the day they go under contract.</li></ul>'},
        {"h2_html": "What a home inspector should actually <em>pay for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A home inspection website earns its money one way: it turns a buyer searching under a deadline, or an agent looking for someone reliable, into a booked inspection on your calendar. That means it has to load fast, rank for the towns you cover and for home inspector near me, show a sample report and your credentials, and put a booking button and your number in front of a visitor before they scroll. A good-looking site that never ranks and buries your booking link is the most expensive kind, because you paid for it and it brings you nothing.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple. A custom five page site on its own is $1,500 one-time, yours to keep, with no plan and no commitment. Or it is included free on any monthly plan starting at $299, where the ongoing SEO that actually gets it found is handled for you. There is no setup fee either way. What no honest company can promise is a specific ranking by a specific date, because no one controls Google, but a free audit can show you where your current site stands first.</p>'}],
    "bridge_h2": "Get a site that books inspections",
    "bridge_text": "A home inspector website is only worth the bookings it brings in. Ours is built to rank for the towns you cover and for home inspector near me, show a sample report and your certifications, and let a buyer or an agent book around a closing date, then hand every booking to the CRM that follows up.",
    "bridge_slug": "websites-seo-for-home-inspectors",
    "bridge_label": "Websites & SEO for home inspectors",
    "faqs": [
        ("Is a cheap template site good enough for a home inspector?",
         "It can get you online, but a template you fill in yourself is rarely built to rank for home inspector near me or to let a buyer book around a closing date, and you do the upkeep yourself. If it does not get found or turn visitors into booked inspections, its low price is not really a bargain."),
        ("Do I keep the website if I stop working with you?",
         "Yes. If you buy the one-time $1,500 site, it is yours to keep. On a monthly plan the site is built for you as part of the plan, and we tell you plainly what happens to it if you leave, before you sign anything.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ======== What Does a Home Inspection Answering Service Cost? (cost -> ai-receptionist) ========
{
    "slug": "home-inspection-answering-service-cost",
    "h1": "What Does a Home Inspection Answering Service Cost?",
    "title": "What Does a Home Inspection Answering Service Cost? | Top Shelf Business Solutions",
    "meta_desc": "Answering services for home inspectors often bill per call or minute. Top Shelf includes an AI receptionist that answers 24/7 in the Signature plan, $899 a month.",
    "answer": "Traditional answering services for home inspectors usually bill per call, per minute, or on a monthly retainer, so a busy month gets expensive fast. Top Shelf takes a different approach: an AI receptionist that answers every buyer and agent call and books the inspection comes in the Signature plan at $899 a month flat, with no per call fee.",
    "sections": [
        {"h2_html": "How answering services usually <em>charge</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most answering services price around how much they work, which sounds fair until a good month turns into a big bill. A home inspector also fields calls at the worst possible moments, while you are inside a house finishing the last job, and from agents who are working against a contract clock and will not wait on hold. It is worth knowing the common models before you sign up for one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Per-call pricing: you pay for each call answered, so a busy stretch or a wave of price shoppers runs up the cost.</li><li>Per-minute pricing: you pay for talk time, so a chatty caller or a slow operator costs you more than a quick one.</li><li>Monthly retainer plus overage: a base fee covers a bucket of minutes or calls, and you pay extra past it, usually right when you are busiest.</li><li>Setup and per-message fees that are easy to miss until the first invoice lands.</li></ul>'},
        {"h2_html": "What you are really paying for, and a <em>flat alternative</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason to have anyone answer is simple: an agent working a closing deadline does not leave a voicemail, they call the next inspector on their list. The real cost of no coverage is not a monthly fee, it is the inspection, and the agent relationship behind it, that went to whoever picked up. But a generic call center reading a script cannot capture a closing date, will not recognize the agent who feeds you steady work, and cannot book onto your calendar, so you can pay for coverage and still lose the job.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf handles this with an AI receptionist that answers on the first ring, day or night, captures the property address and the closing or option date, and books the inspection or texts you the details. It comes in the Signature plan, flat, at $899 a month, with no per-call or per-minute meter running. One booked inspection you would have lost on a busy afternoon can be worth well more than the plan costs. To be clear about what it does, it handles the call, the intake, and the scheduling only, and it leaves the inspection and the report entirely to you.</p>'}],
    "bridge_h2": "Answer every call without the meter",
    "bridge_text": "Instead of paying per call for a service that reads a script, an AI receptionist answers every buyer and agent call 24/7, captures the property address and the closing date, and books the inspection or texts it to you, all on a flat monthly plan. It handles the phone, the intake, and the scheduling, and leaves your inspection and your report entirely to you.",
    "bridge_slug": "ai-receptionist-for-home-inspectors",
    "bridge_label": "AI receptionist for home inspectors",
    "faqs": [
        ("Is an AI receptionist cheaper than a live answering service?",
         "Usually, and more predictable. A live service that bills per call or per minute climbs exactly when you are busiest, while the AI receptionist is a flat part of your plan with no meter. The bigger saving is the inspection it books instead of losing to the next inspector on the agent's list."),
        ("Does it cost extra for evenings or weekends?",
         "No. It answers around the clock as part of the plan, including the after-hours call from a buyer and the weekend agent trying to lock in a time before an option period closes, with no surcharge or overage.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============== Is a CRM Worth It for a Home Inspector? (cost -> crm) ==============
{
    "slug": "is-a-crm-worth-it-for-a-home-inspector",
    "h1": "Is a CRM Worth It for a Home Inspector?",
    "title": "Is a CRM Worth It for a Home Inspector? | Top Shelf Business Solutions",
    "meta_desc": "For most home inspectors a CRM pays off by keeping agent referrals warm and reviving past buyers. It is in the Signature plan at $899 a month, not a separate bill.",
    "answer": "For most home inspection businesses, yes. A CRM pays for itself the first time it keeps a referring agent from drifting to another inspector, or brings a past buyer back for a re-inspection. It only stops being worth it if you never follow up anyway. Top Shelf includes it in the Signature plan at $899 a month.",
    "sections": [
        {"h2_html": "When a CRM is worth it, and when it is <em>not</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A CRM is worth it for a home inspection business when you work with more agents and past buyers than you can personally keep track of, which is most established inspectors. It is not worth it if you are just starting out, doing a couple of inspections a week, and genuinely staying in touch with every agent and client yourself, though that rarely stays true as you grow. The honest test is simple: how many agents referred you once and never heard from you again, and how many past buyers have not heard a word from you in a year? Those referrals and repeat inspections are exactly the work a CRM is built to recover.</p>'},
        {"h2_html": "What it actually <em>earns you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The value of a CRM for a home inspector is not the software, it is the work that stops slipping through. An agent who sent you two jobs in the spring and then went quiet, a buyer whose builder warranty year is almost up and is due for a re-inspection, a quote you gave that never got booked: each one is work you have already half-earned and are one reminder away from winning.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>It follows up on every open quote and booking on a schedule, so a buyer comparing inspectors keeps hearing from you while the others go quiet.</li><li>It keeps a light, genuine touch with the agents who refer you and flags the ones who have gone silent, so you stay the name they call first.</li><li>It fires reminders to past buyers, a re-inspection or a warranty inspection before the builder year runs out, so repeat work comes back without you tracking dates.</li><li>It keeps every agent, buyer, and inspection history in one place instead of scattered across your phone and your report software.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">At Top Shelf the CRM is not a separate bill. It comes in the Signature plan at $899 a month, with no setup fee, alongside the phone and the follow-up that feed it. The math is the same as the answering service: keep one agent relationship alive or win back one booking and it has paid for itself, and everything after that is margin.</p>'}],
    "bridge_h2": "Put your agent list to work",
    "bridge_text": "The agents who already refer you and the buyers you already inspected for are the cheapest work you can get. A CRM keeps a light touch on every one for you, so the agent calls you first on the next deal and the past buyer comes back for the re-inspection, instead of forgetting your name.",
    "bridge_slug": "crm-for-home-inspectors",
    "bridge_label": "CRM for home inspectors",
    "faqs": [
        ("Is a CRM overkill for a solo home inspector?",
         "Not usually. Even a one-person shop works with more agents and inspects more homes than anyone can track by memory. The point is not size, it is whether follow-up is falling through. If agents drift and past buyers forget your name, a CRM earns its keep."),
        ("How is a CRM different from keeping agents in my phone?",
         "A phone full of contacts does not follow up on a quote, does not tell you which agent has gone quiet, and does not remember which buyer is due for a warranty inspection. A CRM does all of that on a schedule, so the referral work shows up instead of depending on you to remember it between inspections.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do Home Inspectors Miss So Many Calls? (problem -> ai-receptionist) ============
{
    "slug": "why-home-inspectors-miss-calls",
    "h1": "Why Do Home Inspectors Miss So Many Calls?",
    "title": "Why Do Home Inspectors Miss So Many Calls? | Top Shelf Business Solutions",
    "meta_desc": "Home inspectors miss calls because they ring while you are inside a house. An agent on a closing deadline will not wait, they call the next inspector on the list.",
    "answer": "You miss calls because they come while your hands are full, up in an attic, folded into a crawlspace, or out on a roof, and a buyer's agent working a closing deadline will not leave a voicemail. They dial the next inspector on their list. The fix is not working harder, it is making sure every call gets answered.",
    "sections": [
        {"h2_html": "The call comes exactly when you <em>cannot pick up</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Home inspection is a hands-full trade. When the phone rings you are usually up in an attic tracing a flue, folded into a crawlspace with no signal, or on a roof with a moisture meter in one hand, and none of those are moments you can stop and take a call. The busier you are, the more calls you miss, which means your best weeks are also the ones where the most work slips away. It is not a discipline problem. One person cannot inspect the house in front of them and answer every call at the same time.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail feels like a safety net, but for an agent on a deadline it is not one. A buyer and their agent working against the option period are not going to leave a message and wait for a callback. They move down the list until someone answers and books it, and by the time you climb down and check your phone, the inspection is already gone.</p>'},
        {"h2_html": "A missed call can quietly end a <em>referral relationship</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every missed call is equal. The one you least want to miss is from an agent who could feed you steady work for years, because to that agent you are only as good as how easily their client can get on your schedule. Miss the call once, at the wrong moment, and they quietly move on to an inspector who was easier to reach, and they rarely tell you why. So the calls that are most costly to miss are the ones that were never about a single job at all.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Closing that gap takes coverage that never sleeps and knows what an inspection booking needs. A voicemail box cannot schedule anything, and a generic call center does not know a contingency deadline from a casual price check. What actually works is something that answers on the first ring day or night, gets the property address, the type of inspection, and the closing date, and either books it or texts it to you as a priority. It handles the phone and the scheduling only, and hands anything that needs your judgment straight to you, so the inspection itself stays entirely yours.</p>'}],
    "bridge_h2": "Stop losing bookings to voicemail",
    "bridge_text": "An AI receptionist answers every buyer and agent call on the first ring, day or night, captures the property and the closing date, and books the inspection or texts it to you, so the call never rolls to voicemail and the agent never dials the next inspector. It handles the phone and the scheduling, and leaves the inspection to you.",
    "bridge_slug": "ai-receptionist-for-home-inspectors",
    "bridge_label": "AI receptionist for home inspectors",
    "faqs": [
        ("Would an agent rather reach a real person?",
         "What an agent needs most is to know the inspection is booked and the timeline works, and a calm voice that captures the details and schedules it beats a voicemail every time. The AI receptionist is upfront about what it is, gathers the facts, and hands anything that needs your judgment straight to you."),
        ("Can I just forward calls to my cell instead?",
         "You can, but that only helps when your hands are free. Forwarding still rolls to voicemail when you are in an attic, in a crawlspace, or on a roof mid-inspection. Something that always answers and books is what catches the calls a forward would still miss.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ============ Why Do My Home Inspection Leads Go Cold? (problem -> crm) ============
{
    "slug": "why-home-inspection-leads-go-cold",
    "h1": "Why Do My Home Inspection Leads Go Cold?",
    "title": "Why Do My Home Inspection Leads Go Cold? | Top Shelf Business Solutions",
    "meta_desc": "Home inspection leads go cold because nobody followed up. An agent got busy or a buyer gathered other quotes, and the booking went to whoever stayed in touch.",
    "answer": "Most home inspection leads go cold not because your price was wrong, but because nobody followed up. A referring agent got busy, a buyer gathered a couple of quotes, or someone simply forgot, and the booking went to whoever checked back in. A lead that goes quiet is usually a maybe that never got a second touch.",
    "sections": [
        {"h2_html": "Silence usually means forgotten, not <em>rejected</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It is easy to read a quiet quote as a no on price, so you drop it and move on. But most of the time the buyer did not decide against you at all. They asked for a price on an inspection, meant to think it over, and then the move consumed them. They are juggling a lender, a couple of other quotes, and a closing date, and yours slid down the pile. A few days later they could not tell you the difference between the inspectors who quoted them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Agents work the same way. An agent who used you once and did not hear from you again is not angry, they are just busy, and the next deal goes to whoever stayed in front of them. The inspector who gets the booking is usually not the cheapest, it is the one who followed up: a friendly check-in a couple of days later, a quick note answering the question they were stuck on. That second touch is what turns a maybe into a booked inspection, and it is exactly the thing there is no time for between jobs.</p>'},
        {"h2_html": "Why the follow-up <em>never happens</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Home inspectors do not skip follow-up because they are lazy. They skip it because the day fills up. You finish an inspection, write and send the report, drive to the next house, and by evening the quote you gave Tuesday and the agent you meant to thank are both out of sight. Doing it by memory means it only happens when things are slow, which is exactly when you have the fewest leads to chase.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>There is no system reminding you which quotes are still open and which agents have gone quiet.</li><li>The follow-up depends on you remembering, so it competes with the actual work and loses.</li><li>By the time you circle back, the buyer has booked whoever beat you to it and the agent has moved on.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a process gap, not a hustle problem, and it is the kind of thing you fix once and then it just runs. When every open quote and every referring agent gets a couple of timed check-ins automatically, written to sound like you, the buyer comparing inspectors keeps hearing from you and the agent stays warm, and the work you already earned stops slipping away.</p>'}],
    "bridge_h2": "Follow up on every lead, automatically",
    "bridge_text": "A CRM keeps every open quote, past buyer, and referring agent in front of you and sends timed check-ins for you, so a buyer comparing inspectors keeps hearing from you and an agent who went quiet gets a genuine touch before the next deal goes to someone else.",
    "bridge_slug": "crm-for-home-inspectors",
    "bridge_label": "CRM for home inspectors",
    "faqs": [
        ("How many times should I follow up on an inspection quote?",
         "A couple of light touches over the first week or two catches most of the maybes without being pushy: a check-in a few days after the quote, then a short note answering common questions. The key is that it happens at all and on time, which is what a CRM handles for you."),
        ("Does automated follow-up feel impersonal?",
         "Not when it is written to sound like you and sent at a sensible pace. A short, friendly check-in reads as attentive, not pushy, and most buyers and agents appreciate the nudge because they meant to get back to you and forgot. You can always step in and message anyone directly.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
# ======== How Do Home Inspectors Get More Referrals? (how-to -> marketing) ========
{
    "slug": "how-do-home-inspectors-get-more-referrals",
    "h1": "How Do Home Inspectors Get More Referrals?",
    "title": "How Do Home Inspectors Get More Referrals? | Top Shelf Business Solutions",
    "meta_desc": "Home inspectors get more referrals by being easy to book and staying in front of the agents who send work, and by reviews that make you the easy recommendation.",
    "answer": "Home inspectors get more referrals by being the inspector agents can recommend without worrying: easy to reach, quick to book around a closing date, and backed by reviews and a clean report. Then stay in front of those agents and past buyers so your name is the one they reach for on the next deal.",
    "sections": [
        {"h2_html": "Referrals come from being the <em>safe recommendation</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most home inspectors do not have a demand problem so much as a reputation-and-reach problem, and referrals are where the two meet. A real estate agent stakes their own name on who they recommend, so they refer the inspector who makes them look organized and reliable in front of a client: someone who answers, books quickly around the closing date, delivers a clear report on time, and treats the buyer well. One hard-to-reach moment, and the agent quietly stops referring, because the risk to their reputation is not worth it.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">So the groundwork of referrals is simply being easy to work with and easy to trust. A sample report a buyer can preview, your certifications and license shown plainly, and a steady stream of honest reviews all tell a first-time agent that sending you their client is a safe bet. Get that right and a single agent does not send one client, they send every buyer they represent for years, and they mention your name to the other agents in their office.</p>'},
        {"h2_html": "Then stay in front of them, on <em>purpose</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Being good is not enough if you fade from memory, because the next referral goes to whoever the agent saw most recently. Getting more referrals is less about a clever trick and more about doing a few simple things consistently, which is exactly what falls apart when you are busy in the field.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Keep a light, genuine touch with the agents who refer you, so you stay the inspector they think of the moment a deal goes under contract.</li><li>Ask every happy buyer and agent for a review at the right moment, and reply to each one, so your reputation keeps building on its own.</li><li>Keep your Google Business Profile active and complete, so a buyer searching home inspector near me actually finds you.</li><li>Stay in front of past buyers for re-inspections, warranty inspections, and the word of mouth they pass along.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of this is a shortcut. Recognition and a referral network build over months, not days, which is why most inspectors give up on it. A steady, mostly automated presence is what compounds, and a free audit will show you what your current visibility and reviews look like to an agent or a buyer searching today.</p>'}],
    "bridge_h2": "Become the inspector agents recommend",
    "bridge_text": "Marketing for home inspectors keeps you visible to the agents who send work and to buyers searching home inspector near me, through your Google Business Profile, steady reviews, and a light touch that keeps you top of mind, so the next referral is already yours. It pairs with the CRM that follows up privately with every agent and past buyer in your list.",
    "bridge_slug": "marketing-for-home-inspectors",
    "bridge_label": "Marketing for home inspectors",
    "faqs": [
        ("What is the fastest way to get more agent referrals?",
         "Be the easy recommendation. Answer the phone or have it answered, book quickly around the closing date, and deliver a clear report on time, so an agent never gets burned for sending you a client. Then keep a light, genuine touch with the agents who already trust you so you stay top of mind."),
        ("Do online reviews really matter for a home inspector?",
         "Yes. Before a buyer picks an inspector, and before an agent adds you to a short list, they read what past clients said. A steady stream of recent, honest reviews makes you the safe choice and helps you show up when someone searches for an inspector nearby. Asking every happy client at the right moment is what builds it.")],
    "trade_slug": "home_inspectors", "trade_plural": "home inspectors",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
},
]
