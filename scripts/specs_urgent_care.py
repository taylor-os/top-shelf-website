"""Per-page content specs for the SEO corpus (plan §5), urgent care batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, urgent-care-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the dentist, optometry, or physical-therapy content reworded.

Medical & Dental hub, alongside dentists, optometrists, and physical therapists. Four service
angles are here in one file (the ai-receptionist dict carries "demo": True). Kept deliberately
distinct from the sibling medical trades: urgent care is EPISODIC ACUTE CARE, not a primary-care
relationship or a recall practice, so the levers no sibling touches are a front desk swamped with
walk-ins while the phone rings with logistics ("are you open, what is the wait, do you take my
insurance, do you do X-rays / stitches / COVID / physicals") that a caller who cannot get through
takes to the next clinic or an ER; extended / weekend / holiday hours as the whole value; online
check-in / save-my-spot instead of appointment booking; and OCCUPATIONAL-HEALTH / employer accounts
(drug screens, physicals, DOT exams, workers-comp) as the recurring B2B goldmine that stands in for
the dentist's recall. Reviews about short waits and friendly care, plus a fast site that shows hours,
wait, services, and insurances, win the local "urgent care near me" search. Hard guardrail woven
into the copy: the AI answers logistics only, never medical questions, and directs any true
emergency to 911 or the ER, and nothing here makes a clinical claim. Each example body ends with the
literal "Illustrative example, not a client." per the honesty rule; if the generator also appends
that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Urgent Care =========================
{
    "slug": "ai-receptionist-for-urgent-care", "demo": True,
    "trade_slug": "urgent_care", "trade_plural": "urgent care clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Urgent Care",
    "title": "AI Receptionist for Urgent Care | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Urgent Care",
    "meta_desc": "An urgent care answering service answers every are-you-open, wait-time, and insurance call your front desk misses, and points patients to online check-in.",
    "service_schema_name": "AI Receptionist for Urgent Care",
    "eyebrow": "For Urgent Care",
    "h1_html": "AI Receptionist <em>for Urgent Care</em>",
    "answer_block": "An urgent care answering service answers every call the moment it rings, days, nights, weekends, and holidays, so the are-you-open, wait-time, and insurance questions that swamp a busy front desk all get a real answer. You keep your number, and every patient belongs to you.",
    "sections": [
        {"h2_html": "The call you miss is the patient who <em>drives to the next clinic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A parent whose child just spiked a fever, a man who cut his hand in the garage, a worker sent over for an injury on the clock, none of them are going to leave a voicemail and wait. They call your clinic, and if the line is busy or rings out, they do not try again. They tap the next urgent care on the map, or they give up and go to a hospital emergency room. The call was not a wrong number. It was a patient walking into another clinic, and often the whole household that would have come with them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Your front desk is not ignoring the phone. They are checking in a lobby full of walk-ins, verifying insurance, rooming the patient who just arrived hurt, and handing a clipboard to the next person in line, all at once. The phone rings straight through while the one or two people up front already have their hands full. An urgent care answering service picks up on the first ring no matter how busy the lobby is, answers the question the caller actually has, and points them to online check-in so they hold a place in line instead of hanging up and leaving.</p>'},
        {"h2_html": "Built around the calls an <em>urgent care front desk</em> actually fields",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every call is an emergency, and most are not. The phone at an urgent care rings all day with the same handful of logistics questions, and every one of them is a person deciding in the moment whether to come to you or go somewhere else. A voicemail box cannot answer a single one, and a generic call center reading a script does not know your hours, your services, or which plans you take.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers the four questions that decide the visit: are you open right now, how long is the wait, do you take my insurance, and do you do the thing I need, whether that is an X-ray, stitches, a flu or COVID test, or a physical.</li><li>Works your real hours, including the nights, weekends, and holidays that are the whole reason a patient chooses urgent care over waiting days for their regular doctor.</li><li>Points callers to online check-in or save-my-spot so they claim a place in line from the car instead of guessing at the wait and driving somewhere else.</li><li>Takes a call from a local employer about drug screens, physicals, or a worker hurt on the job and routes it to the right person, so a standing account never sits in voicemail during a rush.</li><li>Handles logistics only. It does not give medical advice or assess symptoms, and anyone describing a serious emergency is told to call 911 or go to the nearest emergency room.</li></ul>'},
        {"h2_html": "Extended hours are your whole pitch, so the phone <em>cannot be the bottleneck</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The reason a patient picks urgent care is simple: you are open when their regular doctor is not. Evenings, weekends, the holiday when a kid wakes up with an earache and nothing else is open, that is when the demand is highest and, in a lot of clinics, when the front desk is thinnest. A single staffer registering a full lobby cannot also catch every ring, so the calls that come at your busiest and most valuable hours are the ones most likely to go unanswered. An answering service that never steps away means the patient calling at 8pm on a Sunday gets a real answer and comes in, instead of reaching a recording and driving to the emergency room down the road.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It protects the business side too. When a local employer calls to set up pre-employment screenings, or to send a worker in after an injury, that call is the start of a standing account worth many visits a year, and it should never be the one that slips to voicemail while the lobby is full.</p>'},
        {"h2_html": "You own the number and the patients, and it <em>never plays doctor</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing clinic number, or a new one registered to your practice, not to us. Every caller, every visit it sends into your check-in flow, and every employer contact is yours and exportable any time, so the patient base you are building stays an asset you own instead of something you rent back month to month. Because a caller may start describing what is wrong, it is built to handle what they share with the discretion a medical office is held to, collecting only what it needs and keeping it inside your systems. And it stays firmly in its lane: it answers logistics, never clinical questions, and sends any true emergency to 911 or the emergency room. It is one piece of the Top Shelf platform, so every call it captures lands in the same CRM that keeps employer accounts warm and brings patients back.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Sunday-night fever, answered while the <em>lobby is full</em>",
        "body_html": "It is 7pm on a Sunday and a mother's toddler is running a fever that will not come down. She searches for an urgent care and calls the first two she finds. One rings out to a weekend recording, the other leaves her on hold while the front desk registers a waiting room full of walk-ins. Yours answers on the first ring, confirms you are open until nine, tells her you take her plan, and points her to check in online so she holds her place before she even leaves the house. She comes straight in instead of spending the evening in a hospital emergency room, and your staff never had to step away from the patients in front of them. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current clinic number?",
         "Yes. It can answer on the number your patients already call, or set up a new one registered to your clinic. Either way the number and every call that comes through it belong to you and stay with you if you ever leave."),
        ("What questions can it actually answer?",
         "The ones that decide whether a patient comes in: whether you are open right now, roughly how long the wait is, whether you take their insurance, and whether you offer what they need, from X-rays to stitches to a flu test to a physical. It can also point them to online check-in so they hold a place in line. You decide exactly what it says."),
        ("Does it give medical advice or assess symptoms?",
         "No, and that is deliberate. It handles logistics only, never clinical questions, and anyone who describes a serious emergency is told to call 911 or go to the nearest emergency room. It captures the details your team needs and leaves every medical judgment to your staff."),
        ("Can it handle calls from employers about physicals or drug screens?",
         "Yes. A call from a local business about pre-employment physicals, drug screens, or a worker hurt on the job is routed to the right person and captured in your CRM, so a standing occupational-health account never sits forgotten in voicemail during a busy afternoon."),
        ("How fast can it be answering?",
         "Setup is included with no separate onboarding fee. We configure your hours, your services, your insurance answers, and your check-in links for you, so it is picking up in days, not weeks. Start with a free audit and we will show you how many calls your front desk is missing while it is with walk-ins.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for urgent care clinics"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-urgent-care.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing walk-ins to <em>a busy signal</em>",
    "cta_sub": "Get a free audit that finds the gap in your patient calls: how many roll to voicemail and drive to the next clinic or an emergency room while your front desk is with walk-ins, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Urgent Care ================================
{
    "slug": "crm-for-urgent-care",
    "trade_slug": "urgent_care", "trade_plural": "urgent care clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Urgent Care",
    "title": "CRM for Urgent Care | Top Shelf Business Solutions",
    "og_title": "CRM for Urgent Care",
    "meta_desc": "A CRM for urgent care manages your employer and occupational-health accounts and brings one-time patients back, so repeat visits keep coming.",
    "service_schema_name": "CRM for Urgent Care",
    "eyebrow": "For Urgent Care",
    "h1_html": "CRM <em>for Urgent Care</em>",
    "answer_block": "A CRM for urgent care keeps every patient, employer account, and occupational-health job in one place and follows up for you, so the local businesses that send drug screens and physicals stay booked and the family you saw once thinks of you first the next time someone is sick or hurt.",
    "sections": [
        {"h2_html": "In urgent care, the steady money is the <em>employer down the street</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most advice about a medical CRM assumes a practice built on recall, a dentist reminding you about a cleaning or an eye doctor about an annual exam. Urgent care does not work that way. Your patients come once, for a specific fever or sprain or cut, get better, and get on with their lives, and that is how it should be. So the recurring, predictable book of business is not the patient you saw one time. It is the employer down the street.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Local businesses need pre-employment physicals, workplace drug screens, DOT physicals, and a place to send a worker hurt on the job, over and over, all year. Landing one of those accounts is worth dozens of visits, and keeping it is worth far more than chasing a single walk-in. But an account started with one batch of screenings quietly goes cold if nobody follows up, and the office manager drifts to whichever clinic stays in touch. A CRM keeps every employer account in front of you and follows up on a schedule you set, so the standing relationships that pay your rent do not slip away between busy shifts.</p>'},
        {"h2_html": "Every employer account is <em>dozens of visits a year</em>, kept in one place",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The occupational-health side of urgent care runs on relationships and paperwork, and both are easy to lose track of when the lobby is full. A CRM built for it does the remembering for you.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every employer, the services they use, their contacts, and the visits they send live in one place instead of scattered across a spreadsheet and whatever the office manager keeps in their head.</li><li>Follow-ups go out on the schedule you set, so an account that sent one round of screenings hears from you again and becomes a standing relationship instead of a one-time job.</li><li>You can see which employers have gone quiet and reach out before they settle on another clinic, and reach every local business at once when you add a service or a new location.</li><li>Workers-comp and physical paperwork stays attached to the right account, so nothing holds up a visit or a bill because a form went missing.</li></ul>'},
        {"h2_html": "The patient you saw once should <em>remember you</em>, not search again",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The other half is the walk-in patient. You will not put them on a recall schedule, because they are healthy until the next time they are not. But when that next time comes, a fever at midnight, a kid who rolls an ankle at a game, a cut that needs a couple of stitches, you want to be the clinic already in their phone, not a fresh search they run from scratch. A patient who had a fast, friendly visit and then heard from you once or twice, a thank-you, a quick note that you are open late all winter, remembers your name when it counts, and brings the rest of the household with them.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">That light touch is also how you earn the reviews that win the next patient. A short message after the visit, sent at the moment someone is relieved their child is fine, is what turns a good visit into a public review and a patient who comes back to you instead of the clinic one exit up the highway.</p>'},
        {"h2_html": "You own the list, and it works with the <em>rest of the clinic</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient, every employer contact, and every note is yours and exportable any time, handled with the discretion a medical office is held to, not locked inside software you only rent. The CRM is one piece of the Top Shelf platform. It connects to the answering service, so a call about physicals or a feverish kid lands in your database ready for follow-up, and to your online check-in, so a visit is logged against the right record. For a clinic whose quiet, dependable revenue lives in its employer accounts and its reputation, owning that list outright, and being able to take it with you, is not a small thing.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The warehouse account that <em>almost slipped away</em>",
        "body_html": "A new warehouse opens across town and sends a batch of pre-employment drug screens one week in the spring. The visits go smoothly, everyone is happy, and normally that is the last you hear from them until they happen to think of you again, if they ever do. Instead, your CRM holds the account and sends the office manager a friendly check-in a few weeks later, offering to set up a standing arrangement for their ongoing hiring and their annual screenings. She says yes, because no one else followed up, and a one-time batch becomes a monthly account worth more than a lobby full of walk-ins. No one at the front desk had to remember to call her. Illustrative example, not a client."},
    "faqs": [
        ("Does it import my existing patients and employer accounts?",
         "Yes. Your current patients, employer contacts, and visit history come in and live in one place, and everything stays yours and exportable. The point is to make the relationships you have already built actually work for you."),
        ("Urgent care is mostly one-time visits, so why a CRM?",
         "Because two things do recur. Local employers need physicals, drug screens, and injury care all year, which is a standing book of business a CRM keeps warm, and every walk-in is someone you want remembering your name the next time they are sick or hurt. The CRM handles both without a front desk chasing anyone by hand."),
        ("Can it really manage occupational-health and employer accounts?",
         "Yes, that is where it earns its keep. It keeps each employer, the services they use, and their paperwork in one place, follows up so a one-time batch of screenings becomes a standing account, and flags which businesses have gone quiet so you can reach them before they settle on another clinic."),
        ("Is patient data kept private?",
         "Yes. Patient and employee information is handled with the care a medical office is held to and stays inside your systems, and it is always yours to export. You control what the CRM stores and what each message says."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your patients and employer accounts, build your follow-up sequences, and connect it to your phones and check-in, so it is working in days. Start with a free audit and we will show you which accounts and patients are going unworked today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for urgent care clinics"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-urgent-care.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting employer accounts <em>go cold</em>",
    "cta_sub": "Get a free audit that finds the gap in your occupational-health accounts and patient follow-up: how many employer relationships and past patients are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ============================== Marketing for Urgent Care ==============================
{
    "slug": "marketing-for-urgent-care",
    "trade_slug": "urgent_care", "trade_plural": "urgent care clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Marketing for Urgent Care",
    "title": "Marketing for Urgent Care | Top Shelf Business Solutions",
    "og_title": "Marketing for Urgent Care",
    "meta_desc": "Urgent care marketing keeps your Google profile hours accurate and reviews fresh, so a patient searching urgent care near me finds you open and picks you.",
    "service_schema_name": "Marketing for Urgent Care",
    "eyebrow": "For Urgent Care",
    "h1_html": "Marketing <em>for Urgent Care</em>",
    "answer_block": "Urgent care marketing keeps you visible where a sick or hurt patient looks first, your Google Business Profile, the map, and your reviews, so the person searching urgent care near me at 8pm finds an open, well-reviewed clinic with the right hours and picks you instead of the one whose profile says closed.",
    "sections": [
        {"h2_html": "Urgent care demand is <em>immediate and local</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody plans an urgent care visit. A fever spikes, a kid falls off a bike, a cut will not stop bleeding, and the search happens in the same minute the problem does. The patient pulls out a phone, types urgent care near me, and goes to whoever is closest, clearly open, and trusted enough to walk into right now. They are not comparing clinics for a week the way someone shops for a dentist. The whole decision is made in the moment they need care, which means being found and trusted in that moment is the entire game.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">It is also intensely local. A patient in pain is not driving across the metro, they want the clinic a few minutes from where they already are. So the goal is not clever advertising to people who feel fine. It is showing up first, open and well-reviewed, for the people near you the instant something goes wrong.</p>'},
        {"h2_html": "Your hours on Google are <em>the whole decision</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For most businesses a wrong hour on the Google profile is a small annoyance. For an urgent care it is the difference between getting the patient and sending them somewhere else, because being open when their regular doctor is closed is the only reason they chose urgent care in the first place. If your profile shows the wrong holiday hours, or says closed when you are open, a sick person takes one look and taps the next result, and you never know the visit did not come. Worse, a patient who drives over on stale hours and finds the doors locked leaves the kind of angry review that scares off the next ten people.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Keeping the profile exactly right, current evening, weekend, and holiday hours, the services you offer, from X-rays to physicals to flu and COVID testing, and the insurances and self-pay options you accept, is a quiet advertisement running in the precise spot a patient looks when they need you. It is the cheapest visibility a clinic can own, and it is the one most likely to be out of date.</p>'},
        {"h2_html": "Short waits and friendly care are the <em>reviews that win the click</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a patient compares two urgent cares on the map, they read the reviews, and for urgent care the reviews that decide are about two things: how long people waited and how they were treated. A wall of recent reviews that mention getting in and out quickly and being treated kindly beats a higher-rated competitor with nothing recent to show. Those reviews do not appear on their own, though. A happy patient forgets to post, and asking feels awkward at a busy front desk.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The best moment to ask is right after a visit, when someone is relieved their child is fine or their hand is bandaged up. Asking every patient then, with a one-tap link, and replying to each review that comes back, good or bad, feeds the profile that feeds the map. It compounds: more recent reviews lift you in the local results, which brings more patients, which brings more reviews.</p>'},
        {"h2_html": "Get ahead of the <em>seasons that fill your lobby</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Urgent care demand comes in waves you can see coming. Cold and flu season packs the lobby for months, back-to-school time brings a rush of sports and camp physicals, and summer brings the sprains, cuts, and heat that come with people being active outdoors. Being visible and current right before each wave beats scrambling once it hits, and a steady stream of posts, photos, and fresh reviews keeps you the clinic people already recognize when the season turns.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">There is a second audience worth reaching, the local employers who send physicals, drug screens, and injured workers. Being findable when an office manager searches for a clinic that does pre-employment physicals or DOT exams opens a standing account, not a single visit. This is the public-facing side of the clinic, aimed at patients and employers who are not yours yet. The private follow-up to the people and accounts already in your system is the CRM, and the two work best together.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Flu season Monday, and you are <em>the one that shows open</em>",
        "body_html": "It is the first bad Monday of flu season and half the town wakes up sick at once. Every one of them reaches for a phone and searches for an urgent care nearby. Because your Google profile has been kept exactly current all year, hours right, services listed, a steady flow of recent reviews about short waits and kind staff, you sit at the top of the map showing clearly open. The clinic a mile away that let its holiday hours go stale shows closed, and the sick patients scrolling past it never give it a second look. Your lobby fills while theirs stays empty. Illustrative example, not a client."},
    "faqs": [
        ("Do you keep my Google profile and hours updated for me?",
         "Yes, and for an urgent care that is the most important thing we do. We keep your evening, weekend, and holiday hours exactly right, list the services you offer and the insurances you take, and post photos and updates on a regular schedule, so a patient searching in a hurry sees a clinic that is clearly open and current."),
        ("What does focusing on my area actually mean?",
         "It means building your profile, reviews, and content around the neighborhoods your patients actually come from, instead of spreading a budget across a whole metro. A patient in pain goes to the closest clinic they trust, so being strong nearby is what turns a search into a walk-in."),
        ("Which reviews matter most for an urgent care?",
         "The ones about wait time and how patients were treated. People choosing between two clinics on the map read those closely, so we help you ask every patient at the right moment, right after their visit, and reply to each review, so the short-wait, friendly-care reputation you earn is the one strangers see."),
        ("Can you help with seasonal demand and employer outreach?",
         "Yes. We time your visibility to the waves that matter, cold and flu season, back-to-school physicals, summer injuries, and help you get found by local employers looking for physicals, drug screens, and DOT exams, so you are in front of both patients and accounts before they start searching."),
        ("How long before it starts working?",
         "A neglected profile can climb in the local map within weeks once it is active, accurate, and gathering reviews, and it compounds from there. Setup is included, and a free audit will show you exactly how your clinic looks to someone searching for urgent care nearby today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for urgent care clinics"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-urgent-care.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the urgent care they <em>can already see</em>",
    "cta_sub": "Get a free audit that finds the gap in your local visibility, your hours, and your reviews: how easily a sick or hurt patient nearby can find you, see you are open, and trust you right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Websites & SEO for Urgent Care =========================
{
    "slug": "websites-seo-for-urgent-care",
    "trade_slug": "urgent_care", "trade_plural": "urgent care clinics",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites & SEO for Urgent Care",
    "title": "Websites & SEO for Urgent Care | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Urgent Care",
    "meta_desc": "An urgent care website built for SEO ranks for urgent care near me and open now, shows your hours, wait, and services, and lets patients check in online.",
    "service_schema_name": "Websites & SEO for Urgent Care",
    "eyebrow": "For Urgent Care",
    "h1_html": "Websites &amp; SEO <em>for Urgent Care</em>",
    "answer_block": "An urgent care website built for SEO ranks for what a sick or hurt patient types, urgent care near me, open now, walk-in clinic, and the services they need, shows your hours, wait, and insurances at a glance, and lets them hold a spot in one tap, so the visit is yours instead of a directory's.",
    "sections": [
        {"h2_html": "A sick or hurt patient decides in <em>seconds, on a phone</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A parent with a feverish child at 8pm, or someone holding a towel on a cut, is on a phone opening the first few clinics they find, and they decide in seconds whether each one can help them right now. They are looking for three things fast: are you open, how close are you, and can you handle what is wrong. A site that loads slowly, looks a decade old, or hides its hours makes them back out and tap the next result, often a directory or a hospital emergency room, before they ever see that you were the better choice.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site does not have to be fancy. It has to load fast on a phone, put your hours, your location, your services, and the insurances you take right in front of a visitor, and make holding a spot or calling a single tap. A clean, current site signals a clinic that has its act together, which is exactly what someone about to walk in with a sick child wants to believe. A beautiful site that buries how to reach you wastes the patient it just earned.</p>'},
        {"h2_html": "Rank for <em>urgent care near me</em>, open now, and the service they need",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national health directory or a big hospital system this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches a patient makes when something is wrong: urgent care near me, walk-in clinic, urgent care open now, and the services they are looking for, an X-ray, stitches, a flu or COVID test, a sports or school physical. Pages built around the services you offer and the areas you cover are what search engines, and a patient deciding where to go, reward with the click.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">There is a whole second stream of searches worth owning, the ones local employers type: pre-employment physicals near me, workplace drug screen, DOT physical. A page built for occupational health puts you in front of the office manager choosing a clinic for their whole company, which is a standing account a directory listing will never hand you. That is depth a faceless directory has no reason to write for your town.</p>'},
        {"h2_html": "Show open, show the wait, and let them <em>hold a spot in one tap</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">For an urgent care the website is not a brochure, it is the front door, and it has one job the moment a patient lands: tell them, immediately, whether you are open and how to get in line. That means honest, current hours right at the top, a clear view of the wait or a save-my-spot and online check-in button, and your services and insurances visible without hunting. A patient who can see you are open until nine, that the wait is manageable, and that you take their plan, and who can claim a place from the car, is a patient who is already yours.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is the piece no generic template gets right, and it is exactly where a walk-in is won or lost. The check-in a patient starts on the site flows into the same system your front desk works from, so the person who held a spot online is expected when they arrive instead of starting over at the counter.</p>'},
        {"h2_html": "The patients and accounts it earns are <em>yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for an urgent care in your town and the top of the page is often a directory or a hospital-system locator, not your clinic. Those sites publish thousands of pages and carry years of authority, so a patient lands there first and gets routed through a platform that treats your own walk-in as a lead it controls, sometimes selling it, sometimes burying you below whoever paid more. Your site not ranking is not a vanity problem. It is the reason a patient who should have found you directly gets handed to a middleman standing between you and the person searching for exactly what you do.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A website you own keeps ranking, keeps earning visits, and keeps compounding in value for as long as it exists, registered to your clinic, not to a platform that can drop you or raise the rent. It plugs into the same CRM that keeps your employer accounts warm and the answering service that picks up the calls it drives, and its occupational-health pages quietly win the employer searches a directory never will. In a business where one visit can lead to a household of future visits and one employer page can open a standing account, an asset that keeps earning is worth far more than a burst of paid clicks that stops the moment the invoice does.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A 7pm fever search finds <em>you, not a directory</em>",
        "body_html": "A father whose daughter spikes a fever after dinner searches urgent care open now near me on his phone. Instead of a national directory that would route him to whoever paid for the spot, he finds your site ranking for that search, loading fast, showing clearly that you are open until nine, that the wait is short, and that you take his insurance, with a save-my-spot button right at the top. He holds a place in one tap and drives over, and he is checked in before he arrives. You paid nothing per lead, no middleman ever touched the visit, and that first good experience is why he calls you, not a hospital, the next time someone at home is sick. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and hospital systems?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the near-me, open-now, service, and employer searches a national directory or hospital locator has no reason to target well, which is exactly where a local clinic can win."),
        ("How is this different from paying for leads or a directory listing?",
         "A pay-per-lead service or directory rents you a patient it may also show to other clinics, and it stops the day you stop paying. A website you own captures patients who are yours alone and keeps working long after it is built, with no per-lead fee skimming every visit."),
        ("Can the site show my real hours and let patients check in online?",
         "Yes, and for an urgent care that is the whole point. It can show honest, current hours, a save-my-spot or online check-in button, and your services and insurances up front, and the check-in flows into the same system your front desk uses, so a patient who claimed a spot is expected when they walk in."),
        ("Do I need a page for every service I offer?",
         "You start with the ones that matter most, the near-me and open-now searches, your top services, and a page for occupational health so employers can find you, then expand. A focused set of strong service and location pages ranks better than one thin page trying to cover everything."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for urgent care clinics"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-urgent-care.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search for <em>urgent care near me</em>",
    "cta_sub": "Get a free audit that finds the gap between your website and the directories and hospital systems taking your urgent care searches, whether you work with us or not. No credit card, never a call center.",
},
]
