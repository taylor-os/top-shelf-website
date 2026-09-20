"""Per-page content specs for the SEO corpus (plan §5), criminal defense lawyers batch. Same
contract as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics
(shell, schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict
below owns the UNIQUE, hand-written, criminal-defense-firm-specific substance that clears the
uniqueness gate. Never templated find-and-replace, never the plumber or personal-injury
content reworded.

Legal hub, and the personal-injury batch shares this hub, so the CRM, marketing, and
websites-seo dicts here are written to be criminal-defense-distinct on purpose: a ticking
court date, arraignments and hearings, bail bondsmen and conflict referrals, charge-specific
local search (DUI, drug, assault, domestic, theft, white-collar), fear and discretion, the
2am family-member search. Four service angles are here in one file (the ai-receptionist dict
carries "demo": True). Each example body ends with the literal "Illustrative example, not a
client." per the honesty rule; if the generator also appends that line, dedupe there.
Attorney advertising ethics: nothing here promises or implies an outcome, dismissal, or
verdict, and the AI intake never gives legal advice.
"""

SPECS = [
# ==================== AI Receptionist for Criminal Defense Lawyers ====================
{
    "slug": "ai-receptionist-for-criminal-defense-lawyers", "demo": True,
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "AI Receptionist for Criminal Defense Lawyers",
    "title": "AI Receptionist for Criminal Defense Lawyers | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Criminal Defense Lawyers",
    "meta_desc": "A criminal defense answering service picks up every arrest and jail call day or night, captures the charge and court date, and alerts your on-call attorney.",
    "service_schema_name": "AI Receptionist for Criminal Defense Lawyers",
    "eyebrow": "For Criminal Defense Lawyers",
    "h1_html": "AI Receptionist <em>for Criminal Defense Lawyers</em>",
    "answer_block": "A criminal defense answering service answers every call the moment it rings, day or night, stays calm with a frightened family member, captures the charge, the jurisdiction, and the court date, and routes a true emergency to your on-call attorney while you are in court or asleep. You keep your own number, and every caller belongs to your firm.",
    "sections": [
        {"h2_html": "The call you miss is the case that <em>hires the next firm</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone who was just arrested, or a spouse or parent calling from the parking lot of a county jail, is not going to leave a voicemail and wait until morning. They call the next criminal defense firm on the list, and the one after that, until a real person picks up and starts helping. In this practice more than almost any other, the firm that answers first and sounds calm and in control is usually the one that gets retained, because a frightened family is choosing on trust in the middle of the worst night of their life. But you are in trial, in a jail meeting with another client, or asleep at 2am, so the call rolls to voicemail and a case that could carry your firm for months goes to whoever answered.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An AI receptionist answers on the first ring, stays steady with a panicked caller, finds out who was arrested, what the charge is, and which county is holding them, and either books the consultation or flags a true emergency to your on-call attorney on the spot. The case is captured and moving instead of lost to the firm down the street.</p>'},
        {"h2_html": "Built around how <em>arrest calls actually come in</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Your calls do not keep office hours. A DWI arrest happens late on a Friday, a domestic call turns into a booking on a Saturday night, and the person who dials you is often not the one in custody, it is a mother, a spouse, or a friend who just found out and does not know what a bond hearing even is. A voicemail box cannot calm that caller or gather what a defense file needs, and a generic call center reading a script does not know which questions matter or which call cannot wait until Monday.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers 24/7, including the nights, weekends, and holidays when most arrests happen and every other firm sends the caller to voicemail.</li><li>Captures the intake your staff would: who was arrested, the charge, the arresting agency and county, whether they are still in custody, the bond amount if it is set, and the date of the first court appearance.</li><li>Flags a true emergency, someone still in a holding cell, a bond hearing in the morning, an arraignment that is close, to your on-call attorney at once so a person can call back fast.</li><li>Handles a returning client or a referral differently from a first-time caller, so the people who already trust your firm never hit a machine.</li></ul>'},
        {"h2_html": "The math is <em>one retained case</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You do not need to catch many calls for this to pay for itself. A single serious matter you would have lost over a weekend is worth far more to your firm than the system costs, and the calm, complete intake captured on that first call is often what convinces a scared family to retain you rather than keep dialing. Everything it captures after that first save is on top. The point is to stop handing your best cases to the firm that simply answered faster.</p>'},
        {"h2_html": "You <em>own</em> the number, the intake, and the client list",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing firm number, or a new one registered in your name, not ours. Every caller, every intake, and every detail is yours and exportable any time, so the leads you work hard to earn are an asset your firm keeps instead of something you rent back month to month. There is no long contract holding your data. The AI receptionist is one piece of the Top Shelf platform, and it hands every intake it captures to the same CRM that follows up, so a consultation you have not signed yet never goes cold. Just as important, it answers, reassures, and records the facts, and it never gives legal advice or discusses the case; your attorneys make every legal decision and every call about whether to take a matter.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A midnight DWI arrest, <em>captured while you sleep</em>",
        "body_html": 'It is nearly 1am when a woman whose husband was just booked for DWI starts calling defense lawyers from the jail parking lot. She tries the first three she finds. Two go to voicemail. Yours answers, stays calm, gets his name, the charge, the county holding him, and whether bond has been set, then books a morning consultation and flags it to your on-call attorney as time-sensitive. You wake up to the intake already written up, with her number attached, instead of hearing the family retained someone else before sunrise. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current firm phone number?",
         'Yes. It can answer on your existing number, or set up a new one registered in your name. Either way the number and every intake that comes through it belong to your firm and go with you if you ever leave.'),
        ("Can it actually run intake, not just take a message?",
         'Yes, that is the point. It asks the questions your intake staff would, who was arrested, the charge, the county and arresting agency, custody and bond status, and the first court date, and writes it up so an attorney can pick it up cold. You decide exactly which questions it asks.'),
        ("Will it alert my on-call attorney for a real emergency?",
         'It flags the calls you tell it to treat as urgent, someone still in custody, a bond hearing in the morning, a court date that is close, and alerts your on-call attorney right away so a person can call back fast. You set what counts as drop-everything.'),
        ("Is it going to give the caller legal advice?",
         'No, and this matters. It answers, reassures, and captures the facts; it never advises on the charge, the odds, or what to do, and it never promises anything about the outcome. Every legal question and every decision about taking a case stays with your attorneys. A frightened family mostly needs to know a real firm is handling it, and a steady voice that gets the details beats a voicemail box.'),
        ("How fast can it be running?",
         'Setup is included with no separate onboarding fee. We build your intake questions, your booking, and your emergency rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for criminal defense lawyers"),
        ("solution-ai-phone.html", "How the AI phone and intake system works"),
        ("crm-for-criminal-defense-lawyers.html", "The CRM that follows up on every intake you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop losing cases to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls and after-hours intakes your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Criminal Defense Lawyers =========================
{
    "slug": "crm-for-criminal-defense-lawyers",
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "CRM for Criminal Defense Lawyers",
    "title": "CRM for Criminal Defense Lawyers | Top Shelf Business Solutions",
    "og_title": "CRM for Criminal Defense Lawyers",
    "meta_desc": "A CRM for criminal defense lawyers follows up with callers before their court date arrives and keeps clients steady through arraignment, hearings, and trial.",
    "service_schema_name": "CRM for Criminal Defense Lawyers",
    "eyebrow": "For Criminal Defense Lawyers",
    "h1_html": "CRM <em>for Criminal Defense Lawyers</em>",
    "answer_block": "A CRM for criminal defense lawyers chases the callers who have not retained yet before their court date arrives, keeps signed clients steady through every arraignment and hearing, and stays in front of the bondsmen and past clients who send you cases. The family that called three firms in one night retains yours because it followed up in time.",
    "sections": [
        {"h2_html": "Before the court date, the retainer goes to whoever <em>reaches back out first</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A person who has just been charged is not weighing a decision at leisure. An arraignment or a first setting is bearing down, often only days away, and they feel the clock. So they call several firms in a single night and mean to decide fast. But fast does not mean they pick on the first call. Half the time they intend to call you back once they have scraped together a retainer or heard from a bondsman, and then the days slide by while they wait. The firm holding the file when the deadline finally forces their hand is the one that circled back before it, and that return call or text is exactly what does not happen while you are stuck in court all week.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every caller who has not retained on a short clock tied to how close their case is, and sends the check-in for you while the court date is still ahead of them. They hear from you again inside the window that decides it, not a week after they have already walked into another office.</p>'},
        {"h2_html": "Between arraignment and trial, silence reads as <em>bad news</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Signing the retainer is where the fear starts, not where it ends. A criminal matter moves in a series of settings, an arraignment, pretrial conferences, motions, maybe a trial, with long dead air in between, and a client scared of what a conviction could do to their job, their family, or their freedom hears that silence as the worst. They start calling the office for reassurance, or worse, they start wondering whether they hired the wrong lawyer and quietly shopping again mid-case. Keeping every client updated ahead of each court date is what settles them, and it is the first thing that gets buried when your own week is packed with other people\'s hearings.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every caller, client, court date, and note sits in one place instead of scattered across message slips, a shared inbox, and whatever three people happen to remember.</li><li>A check-in before each setting, so a client walks into court knowing what to expect rather than calling you the night before in a panic.</li><li>A clear view of who has gone quiet on your calendar, so you reach the anxious client before they reach for another lawyer\'s number.</li></ul>'},
        {"h2_html": "The people who send you cases are <em>bondsmen, past clients, and other lawyers</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Criminal work runs on its own web of referrals, and it is not the web an injury or family practice has. A bail bondsman meets defendants at the exact moment they are scrambling for a lawyer. A civil or family attorney who does not touch criminal cases hands off the ones that land on their desk as conflicts or out-of-area matters. And a past client who felt treated like a person, not a case number, is the one who vouches for you when a relative or a coworker gets that call, because people who have faced charges sometimes face them again and come back to the lawyer who stood with them. None of that stays warm on its own. A CRM keeps a light, steady touch on every source, a thank-you when a bondsman sends someone over, a periodic hello to a referring attorney, a check on a former client, so your name is first in mind the next time trouble finds someone they know.</p>'},
        {"h2_html": "One database, wired to your calls and your <em>court calendar</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every caller and every note is yours and exportable any time, never trapped inside a tool you rent by the month. The CRM is one piece of the Top Shelf platform: it takes the intakes the AI receptionist captures overnight and starts the follow-up on its own, and it hangs each consultation and court date on the right person so nothing is tracked in two places or forgotten in one. Your case-management software holds the legal file, the deadlines, and the discovery; the CRM works the people around it, the callers, the clients, the sources, and keeps the reminders moving. It runs the relationship; your attorneys run the defense and make every call about the case.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The caller who retains <em>the day before arraignment</em>",
        "body_html": 'A mother calls on Monday after her son is charged and tells you the family is still deciding, they want to speak with one more lawyer and sort out a bondsman first. Normally the week swallows it and you never learn how it ended. Instead the CRM, seeing his arraignment is that Friday, sends a short check-in Wednesday and another Thursday, both written to sound like your firm. With the court date now a day away and yours the only office still in touch, she calls back and retains you that afternoon. Nobody on your team had to remember the deadline. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import the callers and cases I already have?",
         'Yes. Your current clients, past callers, and intake notes come in and live in one place, all of it yours and exportable. The point is to put the contacts your firm has already earned to work instead of letting them sit in a phone and an inbox.'),
        ("Can it follow up on people before their court date, not just whenever?",
         'Yes. You can tie the follow-up to how close a caller\'s case is, so someone with an arraignment this week gets reached now while the decision is still live, rather than a generic check-in that lands after they have already retained someone else.'),
        ("Will it keep a signed client calm between hearings?",
         'Yes. You set the rhythm, and it sends an update before each setting and through the quiet stretches, so a client who is frightened about what comes next hears from your firm first instead of stewing and shopping around mid-case.'),
        ("Does it handle bondsmen and other referral sources?",
         'Yes. It keeps a light, scheduled touch on the bail bondsmen, prior clients, and referring attorneys who send you work, a thank-you, a periodic hello, a check-in, so your name stays first in mind the next time one of them meets someone who just got charged.'),
        ("How is this different from my case-management software?",
         'That software runs the legal file, the deadlines, the documents, and the discovery. This runs everything around it: the callers who have not retained, the clients who need reassurance between court dates, and the sources who refer you. The two sit side by side and do different jobs.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for criminal defense lawyers"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-criminal-defense-lawyers.html", "The AI receptionist that feeds it every intake"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Catch the callers before their <em>court date</em>",
    "cta_sub": "Get a free audit of how many callers, clients, and referral sources your firm is letting slip right now, whether you work with us or not. No credit card, never a call center.",
},
# ====================== Marketing for Criminal Defense Lawyers ======================
{
    "slug": "marketing-for-criminal-defense-lawyers",
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Marketing for Criminal Defense Lawyers",
    "title": "Marketing for Criminal Defense Lawyers | Top Shelf Business Solutions",
    "og_title": "Marketing for Criminal Defense Lawyers",
    "meta_desc": "Criminal defense attorney marketing gets your firm found in the minutes after an arrest and builds local trust for the exact charges you defend.",
    "service_schema_name": "Marketing for Criminal Defense Lawyers",
    "eyebrow": "For Criminal Defense Lawyers",
    "h1_html": "Marketing <em>for Criminal Defense Lawyers</em>",
    "answer_block": "Criminal defense attorney marketing puts your firm in front of the person, or the frightened family member, searching in the minutes after an arrest, and builds a local reputation for the exact charges you defend. When someone looks up a DUI or drug lawyer nearby at 2am, your name is the one that looks active, respected, and safe to call.",
    "sections": [
        {"h2_html": "The search happens in minutes, and often it is <em>not the defendant searching</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When someone is arrested, the hunt for a lawyer does not wait for business hours or a clear head. It happens in the first minutes anyone can get to a phone, and just as often the one searching is a spouse, a parent, or a friend, because the person who was arrested is still being booked and cannot call out. That searcher is scared, moving fast, and has no referral to lean on, so they trust what they can see: who comes up first in the local map and results, who looks like a real firm, who has recent reviews. Be present and credible in that window and you get the call. A thin, neglected profile is simply not in the running, and you never hear the phone that did not ring.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">This is a different job than reaching people who might need you someday. It is about being unmistakably there, in your own county, at the odd hours and on the weekends when arrests actually happen, so the family scrambling at 2am finds you and not just whoever bought the top ad slot.</p>'},
        {"h2_html": "A decision made in fear, so the profile has to <em>reassure, not boast</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody is proud to be looking for a criminal defense lawyer. There is dread about what comes next and often real embarrassment about the situation, and the person searching is braced to be judged before they even dial. A loud, chest-thumping listing reads as exactly the wrong thing. What settles someone in that state is a profile that looks calm, current, and human: a real firm with real people, clear information, and reviews that describe being treated with respect and not talked down to. Discretion is part of what you are selling here in a way it is not for most trades, and the marketing has to signal from the first glance that they will be handled with care and without judgment. Getting that tone right is often the difference between a call and a closed tab.</p>'},
        {"h2_html": "Build a name for the <em>charges you actually defend</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A generic criminal defense banner blends into every other firm on the page. What people actually search, and what earns real local standing, is the specific charge weighing on them: a DUI, a drug possession or distribution charge, an assault or domestic violence arrest, a theft, a white-collar matter. Being known in your county as the firm for the charges you genuinely handle is worth far more than a wide, shallow presence across every category at once, and it pulls in the cases you want instead of calls you have to refer out.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Profile categories and local content built around the charges you defend, so a search for that specific charge nearby actually finds you.</li><li>The counties and courthouses you truly practice in, named plainly, instead of a vague region you cannot really cover.</li><li>The questions a frightened first-timer asks, what happens after an arrest, what a bond hearing is, answered where they will see them.</li><li>An honest picture of your firm and how you work, with no claims about how a case will turn out.</li></ul>'},
        {"h2_html": "Reviews that reassure, earned <em>without crossing a line</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Reviews carry enormous weight with a scared searcher, but they behave differently for a criminal firm. Clients are often reluctant to post publicly about a case they would rather forget, so the reviews you do have need to be genuine, handled with care, and gathered only from people willing to give them, never pressured or paid for. When a review speaks to being treated with respect, kept informed, and defended without judgment, it reassures the next person far more than any claim you could make about yourself. And all of it stays inside the rules for attorney advertising: no promising or implying an outcome, no fabricated or incentivized reviews, no misleading claims. This is the public face of the firm; the private follow-up to the people already in your database is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A 2am arrest, and the family finds <em>your firm first</em>",
        "body_html": 'A father gets the call that his daughter has been arrested, and at 2am, wide awake and frightened, he searches for a defense lawyer in their county on his phone. Two firms show profiles that look abandoned, old reviews, missing hours, no sign anyone is home. Yours looks current, with recent reviews that describe people being treated with respect, and the charge she is facing named right there in plain language. He calls you first, because in that moment yours is the only firm that looks both real and safe to trust. Illustrative example, not a client.'},
    "faqs": [
        ("Who is actually searching, the person arrested or their family?",
         'Often the family. Someone in custody may not be able to call anyone for hours, so a spouse or parent does the searching, fast and frightened, in the middle of the night. We build your presence for that person, at the hours arrests happen, so you are found when the search really occurs.'),
        ("Can you help me be known for a specific charge, like DUI?",
         'Yes. We shape your profile and local content around the charges you genuinely defend, DUI, drug, assault, domestic, theft, or whatever your firm handles, so a search for that charge in your county surfaces you instead of one generic listing lost among the rest.'),
        ("Is this even allowed, given attorney advertising rules?",
         'Yes, and staying inside those rules is the whole approach. No promising or implying outcomes, no fake or paid reviews, no misleading claims. We keep your real profile active and your genuine reviews visible, which is both permitted and what actually earns a nervous person\'s trust.'),
        ("My clients do not want to leave public reviews. How does that work?",
         'We only ever ask the willing, and never pressure or pay for a review. Even a few honest ones that speak to being treated with respect and kept informed do the reassuring, and we help you reply to each with care, which matters more here than sheer volume.'),
        ("How is this different from the CRM?",
         'The CRM works privately on the people already in your world, callers who have not retained, current clients, referral sources. Marketing is the public side: being visible, current, and trustworthy to the frightened stranger who has never heard of you and needs a defense lawyer tonight.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for criminal defense lawyers"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-criminal-defense-lawyers.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the firm they find <em>at 2am</em>",
    "cta_sub": "Get a free audit of how your firm looks to a frightened family searching for a defense lawyer in your county right now, whether you work with us or not. No credit card, never a call center.",
},
# =================== Websites & SEO for Criminal Defense Lawyers ===================
{
    "slug": "websites-seo-for-criminal-defense-lawyers",
    "trade_slug": "criminal_defense_lawyers", "trade_plural": "criminal defense lawyers",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Websites & SEO for Criminal Defense Lawyers",
    "title": "Websites & SEO for Criminal Defense Lawyers | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Criminal Defense Lawyers",
    "meta_desc": "A criminal defense lawyer website built for SEO ranks for DUI, drug, and criminal-defense-near-me searches and turns a frightened visitor into a call.",
    "service_schema_name": "Websites & SEO for Criminal Defense Lawyers",
    "eyebrow": "For Criminal Defense Lawyers",
    "h1_html": "Websites &amp; SEO <em>for Criminal Defense Lawyers</em>",
    "answer_block": "A criminal defense lawyer website built for SEO ranks for the charge and the county someone types in a panic, DUI lawyer, drug charge attorney, criminal defense near me, and greets them with a site that looks discreet, credible, and ready to respond tonight. The call comes to your firm directly, not a directory selling it on.",
    "sections": [
        {"h2_html": "In a crisis, your site is the first read on whether you are <em>safe to trust</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone who was just arrested, or a relative acting for them, lands on your site already frightened and braced to be judged. In a few seconds they decide whether this is a real firm that will take them seriously or a page to bounce off. A site that opens instantly, states plainly that you defend the charge they are facing, shows real people and honest reviews, and makes it obvious they can reach a human right now does the reassuring. A slow, generic template does the opposite: it tells a scared person you might not be there when the setting arrives in a matter of days. For criminal work the site is not a brochure, it is the first evidence that you can be trusted with the most frightening problem someone has ever faced.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">And the clock is usually already running. An arraignment or first setting is often just days out, so the page has to carry a visitor from frightened to a booked consultation without friction, whatever hour they found you.</p>'},
        {"h2_html": "Rank for the <em>charge and the county</em>, not a broad slogan",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not top a national legal directory for a broad term this year, and you do not need to. The searches that turn into criminal cases are specific and local: the charge, plus where it happened. People type the exact thing weighing on them, a DUI lawyer in your city, a drug charge attorney nearby, an assault or domestic violence lawyer in your county, criminal defense attorney near me. Pages built around the charges you truly defend and the courthouses you actually appear in are what a search engine can rank and what an anxious searcher clicks. A single page that only says criminal defense competes with everyone and stands out to no one.</p>'},
        {"h2_html": "Frightened, on a phone, with a way to reach you <em>quietly</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The visitor is on a phone, rattled, and not about to read pages of legal history before they act. The site has to put a way to call you directly in front of them at once, and, just as important for this kind of trouble, a private way to reach out for the person who is not ready to say any of it out loud. Discretion is not a nicety here, it is the reason some people hesitate to make contact at all, so the path to you has to feel safe as well as fast.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Opens fast on a phone, because a frightened person will not wait on a heavy page to load.</li><li>A tap-to-call button in view the instant the page appears, for the family that needs a human now.</li><li>A short, private message option for the person who cannot talk freely or is too embarrassed to call.</li><li>Plain, honest information about the charge and what happens next, with no claims about how a case will end.</li></ul>'},
        {"h2_html": "Own the calls instead of <em>renting them from a directory</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search your own city and the top results are often not local firms at all, they are directories and pay-per-lead services that outrank everyone and then sell the contact, sometimes to several firms at once, sometimes back to you for a slice of the case. Every month you have no real site of your own, that traffic, and the frightened people behind it, belongs to a middleman instead of you. A site your firm owns and ranks flips it: the caller reaches you and only you, there is no per-lead fee skimming a defense a family is already stretching to afford, and the page keeps working and compounding for as long as it stands. It is registered to your firm, not a platform that can drop you or raise the rate, and it feeds the same CRM and after-hours receptionist that catch and follow up on every call it earns.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A charge-specific search finds <em>your firm, not a middleman</em>",
        "body_html": 'A man arrested over the weekend, with a court date the following week, searches for a DUI lawyer in his county from his phone. Instead of a directory that would harvest his information and sell it on to three firms, he finds your site ranking for that charge in that city, with a page that speaks to exactly what he is facing and a button to call you right away. He reaches your firm directly, talks to a real person, and books before his setting. You paid no middleman a cent for the call. Illustrative example, not a client.'},
    "faqs": [
        ("What criminal terms can my site realistically rank for?",
         'The specific and local ones: your firm name, the charges you defend paired with your city or county, DUI, drug, assault, domestic, theft, and criminal-defense-near-me searches. That is where a local firm can win, not the broadest national terms a directory has spent years dominating.'),
        ("Directories sit above me in the results. How do I get around that?",
         'By owning the searches they do not bother to serve well, your county, your specific charges, real reviews, a real firm. A directory rents you a shared contact and stops the day you stop paying; a site you own keeps the call to itself and keeps ranking long after it is built.'),
        ("Can a website really convey discretion for something this sensitive?",
         'Yes, and it should. A calm, professional page, honest information with no outcome claims, and a private way to make contact tell a frightened person they will be handled with care. That is often what decides whether someone reaches out at all.'),
        ("Most of my cases come from referrals. Do I even need this?",
         'You still do. A referred client looks you up before they call, and a family with no one to ask turns straight to a search the night of an arrest. A site that ranks and reads as credible turns both into calls instead of sending them to a directory.'),
        ("Someone I help may have a court date next week. Can the site handle that urgency?",
         'That is what it is built for. It opens fast, makes calling or messaging you effortless, and moves a frightened visitor to a booked consultation without friction, so the days before a setting are not lost to phone tag.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for criminal defense lawyers"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-criminal-defense-lawyers.html", "Staying visible in your market beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the calls your <em>own city</em> is already making",
    "cta_sub": "Get a free audit of how much of your local criminal-defense traffic is going to directories and lead-sellers instead of you, whether you work with us or not. No credit card, never a call center.",
},
]
