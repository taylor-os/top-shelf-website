"""Colony topics for HVAC companies (plan §5 colony template). generate_colony.py imports
TOPICS from every scripts/colony_specs_*.py. Each dict is ONE real question an HVAC-business
owner searches, answered directly in 40-60 words, backed by two short body sections, then
funneled to the one money page that solves it via the "the fix" bridge.

9 distinct questions, mix of problem / how-to / cost, drawn from real HVAC reality: the
first-heat-wave and hard-freeze call floods, no-AC and no-heat emergencies, maintenance-
agreement renewals, aging systems and unsold replacement quotes, shoulder-season slowdowns,
and the reviews and website homeowners check before they call. Bridges spread across all 7
HVAC money pages (ai-receptionist and marketing each carry two, on distinct questions).

Honest: no invented stats, prices, or clients; the only prices cited are Top Shelf's real
ones ($299 / $899 / $2,500 monthly plans, $1,500 one-time standalone site). No em or en
dashes. "find the gap", never "leak" as a money or customer metaphor.
"""

TOPICS = [
# ============================ Missed calls during a heat wave (ai-receptionist) ============================
{
    "slug": "missed-calls-during-a-heat-wave",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "Why Do I Miss So Many Calls During a Heat Wave?",
    "title": "Why Do I Miss So Many Calls During a Heat Wave? | Top Shelf Business Solutions",
    "meta_desc": "The first heat wave floods your phones while techs are on jobs, so calls roll to voicemail and callers dial the next company. Here is how to stop losing them.",
    "answer": "When the first heat wave hits, everyone with a struggling AC calls at once, your techs are already on jobs, and the office cannot pick up fast enough, so calls roll to voicemail. Most homeowners will not leave one. They just dial the next company, and that booked job was yours to lose.",
    "sections": [
        {"h2_html": "The <em>first hot week</em> is when it happens",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The pattern is the same every year. The temperature crosses ninety, every marginal AC system in town gives up in the same forty-eight hours, and your phone rings more in two days than it did all spring. Your techs are already booked solid, the one person in the office cannot pick up three lines at once, and the overflow rolls to voicemail.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The problem is not that the calls are bad. It is that a homeowner sweating in a hot house does not leave a message and wait. They hang up and call the next HVAC company on the list, and if that company answers, the job is theirs. You never saw the call, so you never knew what it cost you.</p>'''},
        {"h2_html": "Every call answered, even at your <em>busiest</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You cannot hire a full front desk for two weeks of chaos and then carry that cost through a slow October. That is the trap. The volume that overwhelms you shows up in bursts, exactly when you have the least time to deal with it.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every call gets answered on the first ring, even when ten come in at once and your team is on rooftops.</li><li>The caller hears a real, professional greeting in your company name instead of hold music or a voicemail beep.</li><li>The details, name, address, and whether it is a no-cool emergency, are captured and sent to you so nothing waits on a callback.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist handles that surge without a surge in payroll. It answers around the clock, sounds like your company, and hands you a booked, qualified job instead of a missed call you have to chase. When the heat breaks, there is no extra headcount left to carry. And you stop guessing how many jobs slipped away while your line was tied up, because the calls that used to vanish into voicemail now land on your schedule as booked work instead.</p>'''}],
    "bridge_h2": "Answer every call without hiring a <em>front desk</em>",
    "bridge_text": "An AI receptionist for HVAC companies picks up every call around the clock, in your company name, and books the job while your crew stays on the roof. A free audit finds the gap by showing how many calls you are missing right now.",
    "bridge_slug": "ai-receptionist-for-hvac-companies",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("Can it handle several calls at the same time?",
         'Yes, and that is the point. When ten calls hit at once during a heat wave, each one is answered on the first ring instead of stacking up in a queue or rolling to voicemail. Nobody sits on hold, and nobody hangs up to call your competitor.'),
        ("What happens to the calls it answers?",
         'Each caller gets a professional greeting in your company name, and the receptionist gathers the name, address, and problem, then sends it straight to you or books it on your calendar. You get a qualified job ready to run, not a voicemail to return hours later.')],
},
# ============================ More maintenance agreements (crm) ============================
{
    "slug": "get-more-maintenance-agreements",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Get More HVAC Maintenance Agreements?",
    "title": "How Do I Get More HVAC Maintenance Agreements? | Top Shelf Business Solutions",
    "meta_desc": "Sell the plan right after a repair or tune-up, then let a CRM track who is due, who declined, and who is up for renewal, so fewer slip through the cracks.",
    "answer": "Sell the plan at the moment of value, right after a repair or a tune-up, then let a system track who is due, who declined, and who is up for renewal. A CRM follows up for you so agreements do not depend on a tech remembering to ask or you remembering to call.",
    "sections": [
        {"h2_html": "Ask at the moment the value is <em>obvious</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The easiest maintenance agreement to sell is the one you offer right after you have fixed the problem. The customer is standing in a comfortable house, they can see what you just did, and the plan is an easy yes. Ask a week later by mail and the moment is gone. Most agreements are lost not because the customer said no, but because nobody asked while it mattered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The trouble is that the ask depends on a tech remembering, in the truck, at the end of a long call, to bring it up the same way every time. Some do, most forget, and there goes the recurring revenue that would carry you through the slow months.</p>'''},
        {"h2_html": "Your plan list is only worth what you <em>work</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting the agreement signed is half the job. The other half is renewing it and actually booking the visits it promises, and that is where most shops quietly lose members. A plan nobody reminds you to schedule turns into a refund request and a customer who does not renew.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every member, their plan, and the visits they are owed live in one place instead of a spreadsheet nobody updates.</li><li>Renewals and due tune-ups surface on time, so you reach out before the plan lapses instead of after.</li><li>Repair customers who are not members yet get a follow-up with the offer, so your plan list keeps growing.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM does that quiet work for you. It keeps the list, times the reminders, and follows up so the recurring revenue you sold does not depend on anyone remembering to keep it alive. That steady base of plan revenue is what lets you plan your hiring, ride out the mild-weather months, and stop treating every spring like the business is starting over from zero. It is the closest thing an HVAC shop has to income you can actually count on before the phone even rings.</p>'''}],
    "bridge_h2": "Turn one repair into a <em>member for years</em>",
    "bridge_text": "A CRM for HVAC companies keeps every member, renewal date, and owed visit in one place and follows up automatically, so your maintenance base grows instead of quietly shrinking. Start with a free audit to find the gap between the plans you sell and the ones you keep.",
    "bridge_slug": "crm-for-hvac-companies",
    "bridge_label": "See the CRM",
    "faqs": [
        ("When is the best time to offer a maintenance plan?",
         'Right after a repair or a tune-up, while the customer can see the value of what you just did. That is when the answer is most often yes. A CRM prompts the follow-up so the ask happens every time, not only when a tech remembers.'),
        ("Does it help me keep members, not just sign them?",
         'Yes, and that is where the money is. It tracks renewal dates and the visits each plan owes and surfaces them on time, so you reach out before a plan lapses and actually deliver the tune-ups you promised. Retained members are far cheaper than signing new ones.')],
},
# ============================ HVAC website cost (websites-seo) ============================
{
    "slug": "how-much-hvac-website-costs",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Much Does an HVAC Company Website Cost?",
    "title": "How Much Does an HVAC Company Website Cost? | Top Shelf Business Solutions",
    "meta_desc": "It depends on who builds it: DIY builders are cheap, agencies run to thousands. A custom five-page HVAC site from Top Shelf is $1,500 once, or free with a plan.",
    "answer": "It depends on who builds it. A do-it-yourself builder is cheap but the work is yours, and a freelancer or agency can range widely into the thousands. A custom five-page HVAC site from Top Shelf is $1,500 one-time to own outright, or included free with any monthly plan.",
    "sections": [
        {"h2_html": "Why the price is <em>all over the map</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Ask three companies what a website costs and you will get three very different numbers, because you are not comparing the same thing. A do-it-yourself site builder is cheap up front, but you are the one building it, writing it, and keeping it working. A freelancer costs more and varies with who you find. A full agency build can run well into the thousands, sometimes with a separate monthly retainer on top.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">None of those numbers means much on its own, because the real question is not what the site costs. It is whether the site brings you booked jobs. A cheap page nobody finds and an expensive page that does not convert are both a waste, just at very different prices.</p>'''},
        {"h2_html": "What actually decides the <em>return</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A website earns its cost when it shows up where homeowners search for AC and furnace help, loads fast on a phone, and makes calling or booking you the obvious next step. A pretty site that does not rank, or a fast site with no clear way to reach you, will not pay for itself no matter what you spent.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Top Shelf keeps it simple and honest. A custom five-page HVAC site is $1,500 one-time to own outright and host wherever you like, with no plan and no commitment. Or it comes included free with any monthly plan, Essentials at $299, Signature at $899, or Platinum at $2,500, with no setup fee. If the site you already have is solid, we optimize that one instead of charging you for a new build. Either way, you are paying for a site that works for you around the clock, not a brochure that just sits there, and you own the result instead of renting your presence from a portal or a platform that can change its rules on you whenever it likes.</p>'''}],
    "bridge_h2": "A site built to <em>bring you jobs</em>",
    "bridge_text": "Websites and SEO for HVAC companies means a fast, findable site that turns searches for AC and furnace help into booked calls, not just a good-looking page. A free audit shows where your current site stands and what it is costing you in missed work.",
    "bridge_slug": "websites-seo-for-hvac-companies",
    "bridge_label": "See websites & SEO",
    "faqs": [
        ("Is a cheap website builder good enough for an HVAC company?",
         'It can get you online, but you are doing all the work, and a page that does not rank or convert is not really cheap. The cost that matters is jobs booked, not the monthly fee. A site built to be found and to convert usually earns back its price many times over.'),
        ("Do I have to pay a setup fee?",
         'No. A custom five-page site is included free on every Top Shelf plan with nothing up front, and there is no separate onboarding fee. If you would rather own a site outright without a plan, it is $1,500 one-time, yours to keep and host anywhere.')],
},
# ============================ More Google reviews (review-software) ============================
{
    "slug": "get-more-hvac-reviews",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Get More Google Reviews for My HVAC Business?",
    "title": "How Do I Get More Google Reviews for My HVAC Business? | Top Shelf Business Solutions",
    "meta_desc": "Ask every happy customer right after the visit with a one-tap text to your Google profile, and reply to every review. Software handles the timing so more show up.",
    "answer": "Ask every happy customer right after the visit, while the house is comfortable again and they are glad they called you. Send the request by text with a one-tap link to your Google profile, and reply to every review. Software handles the timing so good reviews stop depending on customers remembering on their own.",
    "sections": [
        {"h2_html": "Homeowners <em>check reviews</em> before they call",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before someone lets an HVAC company into their home to work on the system that heats and cools it, they read your reviews. A profile with a handful of old ones, sitting next to a competitor with a wall of recent five-star reviews, quietly loses you calls you never even hear about. The homeowner just dials the company that looks trusted, and you are not in the room to make your case.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The issue is almost never that your customers are unhappy. It is that a happy customer forgets to post, and asking face to face feels awkward at the end of a job. The reviews you have earned are real. They just are not showing up online where the next customer is looking.</p>'''},
        {"h2_html": "Ask at the right moment, make it <em>one tap</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The best time to ask is right after the visit, while the house is comfortable again and the customer is glad they called you. Wait a few days and the goodwill fades and the request gets forgotten.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>The ask goes out automatically by text and email the moment a job is closed, with a link straight to your Google profile.</li><li>Leaving a review takes one tap, so a busy homeowner actually finishes instead of giving up halfway.</li><li>Every new review is flagged so you can reply, which reassures the next reader and helps you show up in local search.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Review software handles the timing and the awkwardness for you. You keep working, and the reputation you already earned starts showing up where the next customer decides who to call. And it compounds. Every recent review makes your profile a little stronger in local search, which brings the next customer, who leaves the next review, so the reputation you built job by job keeps working for you long after the tech has packed up and driven home.</p>'''}],
    "bridge_h2": "Put your <em>real reputation</em> online",
    "bridge_text": "Review software for HVAC companies asks every happy customer at the right moment, makes leaving a review one tap, and helps you reply to each, so your Google profile reflects the work you actually do. A free audit shows how your reviews stack up against the shops you compete with.",
    "bridge_slug": "review-software-for-hvac-companies",
    "bridge_label": "See review software",
    "faqs": [
        ("Is it allowed to automate asking for reviews?",
         'Asking every customer for an honest review is fine and encouraged. What is not allowed is filtering out unhappy customers or paying for reviews, and this does neither. It simply asks everyone at the right moment and makes saying yes easy.'),
        ("What if I get a bad review?",
         'You find out right away instead of weeks later, and you can post a calm, professional reply. One thoughtful response sitting under a wall of genuine positive reviews often reassures the next homeowner more than a spotless record would.')],
},
# ============================ Fill the slow season (marketing) ============================
{
    "slug": "fill-hvac-slow-season",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Fill My HVAC Schedule in the Slow Season?",
    "title": "How Do I Fill My HVAC Schedule in the Slow Season? | Top Shelf Business Solutions",
    "meta_desc": "In spring and fall, fill the calendar off demand you built. Push tune-ups to past customers, stay visible on Google, and market to the neighborhoods you serve.",
    "answer": "In spring and fall, when nobody has an emergency, you fill the calendar off the demand you already built. Push tune-ups and maintenance plans to past customers, stay visible on Google so you catch what searches do happen, and keep your name in front of the neighborhoods you serve before the next season hits.",
    "sections": [
        {"h2_html": "The slow weeks are <em>predictable</em>, so plan for them",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every HVAC shop knows the pattern. Summer and the deep freeze keep you slammed, and then spring and fall go quiet because nobody has an emergency when the weather is mild. The mistake is treating that lull as a surprise every year instead of the schedule it actually is. The work to fill those weeks has to happen before they arrive, not during them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Shoulder season is also the wrong time to go dark on marketing. When you disappear in the slow months, you are invisible right when homeowners are booking the tune-ups that prevent a summer breakdown, and right when a competitor who stayed visible is picking those jobs up.</p>'''},
        {"h2_html": "Fill it off the demand you <em>already built</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The cheapest work in a slow month comes from people who already know you. A past customer, a lapsed maintenance member, a homeowner who declined a repair last year, all of them are easier to book than a stranger, and a slow week is exactly when you have time to reach them.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Push seasonal tune-ups and maintenance plans to your past-customer list before the next hot or cold snap.</li><li>Keep your Google Business Profile active so you still catch the searches that do happen in the off months.</li><li>Stay visible in the neighborhoods you serve, so when the season turns you are the name people already know.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Marketing that runs steadily, instead of only when you are desperate, is what smooths the slow weeks out. It keeps a base of work coming in year round rather than swinging between slammed and silent. It also means you are not forced into deep discounts just to keep the crew busy in April, because the work is already booked from people who trust you, at your normal rates, before the desperation of an empty calendar ever sets in.</p>'''}],
    "bridge_h2": "Stay busy when the <em>weather is mild</em>",
    "bridge_text": "Marketing for HVAC companies keeps you visible year round, on Google and in the neighborhoods you serve, and turns your past-customer list into booked tune-ups during the slow months. A free audit finds the gap between your busy season and your quiet one.",
    "bridge_slug": "marketing-for-hvac-companies",
    "bridge_label": "See HVAC marketing",
    "faqs": [
        ("What kind of work can I actually book in the slow season?",
         'Mostly maintenance: seasonal tune-ups, filter and system checks, and maintenance-plan visits. It is preventive work homeowners are glad to do when they are not in a crisis, and it fills the exact weeks that would otherwise sit empty.'),
        ("Should I cut marketing when things are slow?",
         'That is usually backward. Going quiet in the slow months makes you invisible right when homeowners are booking the tune-ups that lead to summer and winter work, and hands those jobs to whoever stayed visible. Steady marketing is what smooths the slow weeks out.')],
},
# ============================ Stop no-shows (online-booking) ============================
{
    "slug": "stop-hvac-service-call-no-shows",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Stop No-Shows on HVAC Service Calls?",
    "title": "How Do I Stop No-Shows on HVAC Service Calls? | Top Shelf Business Solutions",
    "meta_desc": "Confirm the appointment the moment it is set and remind the customer before you roll a truck. Let people pick a real time slot themselves so fewer no-shows happen.",
    "answer": "Confirm the appointment the moment it is set, then remind the customer by text before you roll a truck. Let people pick a real time slot themselves instead of a loose callback, because someone who chose their own window and got a reminder is far more likely to be home when your tech arrives.",
    "sections": [
        {"h2_html": "A no-show is a <em>whole slot</em> gone",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a customer is not home, it is not just an awkward knock on the door. It is a truck, a tech, the fuel, and a block of your day spent on nothing, in a slot another paying job could have filled. A couple of those a week adds up to real money, and it is money you never see on any invoice.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Most no-shows are not people blowing you off. They are people who forgot, who never got a clear time, or who agreed to a vague callback window and moved on with their day. The appointment was soft from the start, so it did not hold.</p>'''},
        {"h2_html": "A booked slot the customer <em>chose and confirmed</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">People show up for appointments they picked themselves and got reminded about. That is the whole fix, and it is mostly about taking the guesswork out of how the appointment gets set in the first place.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>The customer picks a real time slot from your actual availability, not a loose promise to call back.</li><li>A confirmation goes out the moment it is booked, so there is a clear time on record instead of a fuzzy maybe.</li><li>A reminder by text lands before you roll the truck, so the appointment is fresh instead of forgotten.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Online booking with automatic confirmations and reminders is the single biggest lever on no-shows. Someone who chose their own window and got a reminder is far more likely to be standing there when your tech pulls up. There will always be the occasional last-minute cancellation, and that is fine. The goal is not a perfect record, it is that every truck leaving the shop is headed to a driveway where someone is actually waiting, so a full day on the schedule is a full day of paying work instead of windshield time chasing people who forgot.</p>'''}],
    "bridge_h2": "Fewer empty driveways, fuller <em>days</em>",
    "bridge_text": "Online booking for HVAC companies lets customers pick a real time slot and sends the confirmations and reminders that actually cut no-shows, so your trucks roll to jobs that are there. A free audit shows what missed appointments are costing you now.",
    "bridge_slug": "online-booking-for-hvac-companies",
    "bridge_label": "See online booking",
    "faqs": [
        ("Do reminders really cut down on no-shows?",
         'They are the single biggest lever you have. Automatic confirmations and reminders by text and email keep the appointment fresh and give the customer an easy way to reschedule instead of just not being home. It will not end every no-show, but it takes a real bite out of them.'),
        ("Will it book jobs onto my real calendar?",
         'Yes. It reads your actual availability, so a customer can only pick a slot you are truly open for, and the booking drops straight onto your calendar. You set the hours, the job lengths, and the buffer between calls so a truck is never double-booked.')],
},
# ============================ Follow up on unsold estimates (automation) ============================
{
    "slug": "follow-up-unsold-hvac-estimates",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Follow Up on HVAC Estimates That Never Closed?",
    "title": "How Do I Follow Up on HVAC Estimates That Never Closed? | Top Shelf Business Solutions",
    "meta_desc": "Put every unsold estimate on automatic follow-up. A big replacement quote rarely closes on the first visit, so scheduled check-ins bring customers back when ready.",
    "answer": "Put every unsold estimate on an automatic follow-up instead of a mental note. A big system replacement rarely gets approved on the first visit, so scheduled check-ins, a financing reminder, and a nudge when the season turns keep the quote alive and bring the customer back when they are finally ready to move.",
    "sections": [
        {"h2_html": "Big jobs <em>rarely close</em> on the first visit",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A system replacement is one of the biggest expenses a homeowner faces, and most do not say yes on the spot. They want to think it over, check financing, or wait until the old unit finally quits. That is normal. The mistake is treating a quote that did not close that day as a dead one, when most of them are simply not ready yet.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">What actually loses those jobs is silence. The quote goes in a folder, the week gets busy, and nobody follows up. Months later the customer replaces the system with whoever happened to call them, and it was not you, because you never called. The estimate was never the problem. The follow-up was.</p>'''},
        {"h2_html": "Follow-up that happens <em>without you remembering</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You are not going to keep a mental list of every open quote and the right day to check back on each one. Nobody can, which is exactly why the follow-up falls off. A system does it for you, on a schedule, so no quote goes quiet by accident.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every unsold estimate goes on an automatic sequence of check-ins instead of into a drawer.</li><li>A financing reminder goes out, because for a big job the payment plan is often what turns a maybe into a yes.</li><li>A nudge lands when the season turns and that aging system is about to be tested again.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Automation keeps every open quote warm on its own timing. You still handle the real conversation when they are ready. It just makes sure they hear from you before they hear from someone else. And when the customer finally is ready, you are not starting cold. The quote is already in front of them, they already know your name, and the call to book the install is a short one instead of a fresh sales pitch you have to win all over again.</p>'''}],
    "bridge_h2": "Keep every quote <em>alive</em> until they are ready",
    "bridge_text": "Automation for HVAC companies puts every unsold estimate on a follow-up schedule with check-ins, a financing reminder, and a seasonal nudge, so big jobs come back to you instead of going quiet. A free audit finds the gap between the quotes you write and the ones you close.",
    "bridge_slug": "automation-for-hvac-companies",
    "bridge_label": "See automation",
    "faqs": [
        ("How long should I keep following up on an old estimate?",
         'Longer than most shops do. A replacement quote can close months later, when the system finally fails or the customer sorts out financing. A scheduled sequence keeps a light touch going that whole time, so you are the one they call when they are ready, without you tracking it by hand.'),
        ("Does automated follow-up feel pushy to the customer?",
         'Not when it is spaced right and useful. A check-in, a financing reminder, and a seasonal note are helpful, not nagging. You control the timing and the wording, and you step in personally the moment a customer is ready to talk.')],
},
# ============================ After-hours calls (ai-receptionist) ============================
{
    "slug": "after-hours-hvac-calls",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Do I Handle After-Hours HVAC Calls?",
    "title": "How Do I Handle After-Hours HVAC Calls? | Top Shelf Business Solutions",
    "meta_desc": "After-hours no-heat calls go to whoever picks up. An AI receptionist answers around the clock in your name and books or flags the emergency, with no overnight staff.",
    "answer": "Most after-hours no-heat calls come from people who will not wait until morning, so if yours goes to voicemail they call whoever picks up. An AI receptionist answers every one around the clock, sounds like your company, gathers the details, and books or flags the emergencies, without you paying someone to sit by a phone all night.",
    "sections": [
        {"h2_html": "The emergency call does not <em>wait for morning</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A furnace that quits at ten at night, or an AC that dies over a holiday weekend, is exactly the call you want, and exactly the one that is hardest to catch. The homeowner is not going to wait until you open. They are uncomfortable, sometimes worried about pipes or a sick kid, and they are calling down the list until someone answers. If that someone is not you, the job, and often the customer for good, goes to whoever picked up.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Voicemail does not save it. A person in that situation does not leave a message and sit tight. They hang up and dial the next number, so an after-hours voicemail box is really just a list of jobs you already lost.</p>'''},
        {"h2_html": "Answer all night without <em>paying for all night</em>",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The old options are both bad. Staffing a phone overnight is expensive and hard to keep covered, and forwarding calls to your own cell means you never really clock out and still miss the ones that come while you are asleep. Neither is a real fix, and both wear you down.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every after-hours call is answered live, around the clock, in your company name.</li><li>Real emergencies get identified and flagged or dispatched, while routine calls get booked for the morning.</li><li>You get the details waiting for you instead of a voicemail, so nothing sits unanswered until you open.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist covers the nights and weekends without a payroll line for it. You decide what counts as an emergency worth waking up for, and everything else is captured and booked, so you are not choosing between losing sleep and losing jobs. Over a season, those late-night and weekend calls are some of the most profitable work you do, because a homeowner without heat or cooling is ready to book right now, and being the company that actually answered is most of the battle.</p>'''}],
    "bridge_h2": "Never send an <em>emergency call</em> to voicemail",
    "bridge_text": "An AI receptionist for HVAC companies answers every after-hours call live, in your company name, and books or flags it so nights and weekends stop going to voicemail. A free audit shows how many off-hours calls you are missing right now.",
    "bridge_slug": "ai-receptionist-for-hvac-companies",
    "bridge_label": "See the AI receptionist",
    "faqs": [
        ("Can it tell a real emergency from a call that can wait?",
         'Yes. You set the rules for what counts as an after-hours emergency, and it flags or dispatches those while booking routine calls for the next morning. You are not woken up for a filter question, and a true no-heat call does not sit in voicemail until you open.'),
        ("Is this cheaper than an overnight answering service or on-call staff?",
         'For most shops, yes. Instead of paying per call or covering an overnight shift, it is part of the Signature plan at $899 a month, and it answers every call with no separate per-minute charge. A free audit can compare it to what after-hours coverage costs you today.')],
},
# ============================ Marketing budget (marketing) ============================
{
    "slug": "hvac-marketing-budget",
    "trade_slug": "hvac-companies", "trade_plural": "HVAC companies",
    "hub_name": "Home Services", "hub_slug": "industry-home-services.html",
    "h1": "How Much Should an HVAC Company Spend on Marketing?",
    "title": "How Much Should an HVAC Company Spend on Marketing? | Top Shelf Business Solutions",
    "meta_desc": "There is no single right number. It depends on your market, competition, and growth goals. Top Shelf folds marketing into one flat monthly plan starting at $299.",
    "answer": "There is no single right number. It depends on your market, your competition, and how fast you want to grow, so any flat percentage you read is a starting guess, not an answer. Rather than a separate ad-agency retainer, Top Shelf folds marketing into one flat monthly plan starting at $299, alongside the tools that convert it.",
    "sections": [
        {"h2_html": "Why the <em>flat-percentage answer</em> is useless",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search this question and you will find rules of thumb that tell you to spend some fixed share of revenue. The honest answer is that those numbers do not tell you much. A shop fighting for attention in a crowded metro, a shop that already owns its small town, and a shop trying to double this year all have very different needs, and a single percentage treats them as if they were the same.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">What actually decides the right spend is your market, how much competition is bidding for the same customers, how strong your reputation and past-customer base already are, and how fast you are trying to grow. A brand-new shop starting from nothing has to spend differently than one coasting on twenty years of referrals.</p>'''},
        {"h2_html": "Spend on what <em>converts</em>, not just what is seen",
         "body_html": '''<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Getting seen is only half of it. Money spent driving calls to a slow website, a phone nobody answers, or a business with thin reviews is money poured through a business that cannot hold it. The highest-return spend is often not a bigger ad budget at all. It is fixing what happens after someone is interested.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>A findable website and an active Google profile, so the searches happening near you actually reach you.</li><li>A way to answer and book every call the marketing earns, so you are not paying to generate voicemails.</li><li>Reviews and follow-up that turn interest into booked, repeat work instead of a one-time click.</li></ul><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That is why Top Shelf does not sell marketing as a separate ad-agency retainer. It comes folded into one flat monthly plan, Essentials at $299, Signature at $899, or Platinum at $2,500, alongside the website, reviews, booking, and follow-up that turn attention into jobs. One bill, and the pieces work together instead of a spend that leads nowhere.</p>'''}],
    "bridge_h2": "Marketing that <em>connects to the jobs</em>",
    "bridge_text": "Marketing for HVAC companies works best when it is tied to the website, reviews, and follow-up that convert the attention it earns, not bought as a standalone ad budget. A free audit finds the gap between what you spend to get seen and what actually turns into booked work.",
    "bridge_slug": "marketing-for-hvac-companies",
    "bridge_label": "See HVAC marketing",
    "faqs": [
        ("Is there a percentage of revenue I should spend?",
         'You will see rules of thumb, but they are a rough starting point, not an answer. The right number depends on your market, your competition, your reputation, and how fast you want to grow. A shop starting from scratch and one living on referrals should not spend the same way.'),
        ("Is it better to spend more on ads or fix my website and reviews first?",
         'Usually fix the foundation first. Driving paid clicks to a slow site, an unanswered phone, or a thin review profile wastes the spend. Money often returns more when it goes into converting the interest you already get before you pay to get more of it.')],
},
]
