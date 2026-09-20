"""Per-page content specs for the SEO corpus (plan §5), orthodontists batch. Same contract as
scripts/specs_plumbers.py: generate_corpus.py imports SPECS and owns the mechanics (shell,
schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict below owns
the UNIQUE, hand-written, orthodontist-specific substance that clears the uniqueness gate. Never
templated find-and-replace, never the dentist, optometry, or dermatology content reworded.

Medical & Dental hub, alongside dentists, optometrists, and dermatology. Four service angles are
here in one file (the ai-receptionist dict carries "demo": True). Kept deliberately distinct from
the sibling medical trades: orthodontics is a high-ticket, consult-driven practice where starting
a case (braces or Invisalign) is a shopped decision a parent or adult makes after calling a couple
of offices, and one started case is an eighteen-to-twenty-four-month treatment relationship plus
the siblings and referrals that follow, so the value of a single captured consult is large. The
levers no sibling touches are capturing every consult inquiry off a chairside front desk, nurturing
the "thinking about it" consult that heard the plan and walked, tending the referring-dentist
pipeline, reactivating stalled and retainer patients, and a modern site that is upfront about
financing and shows finished smiles so the free consult is easy to book. Kept clear of general
dentistry (routine cleanings and fillings) and the other medical trades. Each example body ends
with the literal "Illustrative example, not a client." per the honesty rule; if the generator also
appends that line, dedupe there.
"""

SPECS = [
# ========================= AI Receptionist for Orthodontists =========================
{
    "slug": "ai-receptionist-for-orthodontists", "demo": True,
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "AI Receptionist for Orthodontists",
    "title": "AI Receptionist for Orthodontists | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Orthodontists",
    "meta_desc": "An orthodontist answering service answers every consult and new-patient call your front desk misses while chairside, and books the free consult.",
    "service_schema_name": "AI Receptionist for Orthodontists",
    "eyebrow": "For Orthodontists",
    "h1_html": "AI Receptionist <em>for Orthodontists</em>",
    "answer_block": "An orthodontist answering service answers every consult call the moment it rings, days, nights, and weekends, handles the insurance and financing questions that tie up your front desk, and books the free consult on your calendar while your team is chairside. You keep your number, and every patient belongs to you.",
    "sections": [
        {"h2_html": "The consult call you miss is the case that <em>starts somewhere else</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A parent who just decided to look into braces for their child, or an adult who has finally talked themselves into straightening their own teeth, does not leave a voicemail and wait. Starting orthodontic treatment is a big decision and a bigger check, so they call two or three offices, and they book the free consult at the one that actually answers, asks a few warm questions, and makes getting in easy. Your front desk is not ignoring them. In an orthodontic office the person up front is often chairside too, seating a patient for an adjustment, handing an assistant an archwire, or checking someone out between appointments, so the consult call rings through to voicemail while they are a few feet away with their hands full. The call that got missed was not a wrong number. It was a case, and one orthodontic case is never just one visit.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">An orthodontist answering service picks up on the first ring no matter what the front desk is in the middle of. It greets a nervous parent or a self-conscious adult warmly, answers the questions that come up on almost every consult call, and books the free consultation while they are still on the line. The case is captured instead of lost to the office down the road that happened to pick up.</p>'},
        {"h2_html": "Built around the calls an <em>orthodontic front desk</em> actually fields",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every call is a new consult, but the phone at an orthodontic office rarely stops, and the questions are specific to how you work. People call to ask what braces or Invisalign will cost and whether you offer payment plans, whether their insurance covers orthodontics, how old a child should be for a first visit, or because a wire is poking, a bracket popped off, or a retainer got lost or broken. A voicemail box cannot answer one of them, and a generic call center reading a script does not know a consult from a poking-wire problem or a payment-plan question from an insurance one.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers days, evenings, and weekends, so the parent calling after work and the teenager with a poking wire on a Sunday reach a real answer instead of a recording.</li><li>Handles the questions that decide whether someone books: whether the first consult is free, roughly what treatment involves, whether you take their insurance, and that payment plans exist so cost does not scare them off the call.</li><li>Books the free consult straight onto your calendar, so your team is not re-keying it later or playing phone tag with a parent who works the same hours you do.</li><li>Tells a comfort issue apart from a real problem, a poking wire, a broken bracket, a lost retainer, and flags the ones you mark urgent to your team the moment they come in.</li></ul>'},
        {"h2_html": "One consult is <em>two years of treatment</em>, siblings, and referrals",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This is why a missed consult call costs an orthodontic practice more than it first looks. A case that starts is not a single appointment. It is eighteen to twenty-four months of scheduled adjustment visits, a relationship that runs through a child right across their adolescence or an adult through a busy year, and the retainer checks that follow it. On top of that, one family rarely stops at one mouth: the younger sibling comes of age for their own consult, a parent decides to finally fix their own smile, and a happy family sends friends from the same school and neighborhood your way. So the call you lose on a busy afternoon is not one consult. It is the treatment, the siblings, and the referrals that come with keeping that family for years. You do not need to catch many of those for it to change the year, and everything the receptionist books after the first save is on top. When the phone is covered, the case your marketing and your reputation worked to earn actually lands on the schedule instead of slipping to the office that answered first.</p>'},
        {"h2_html": "You own the number, the patients, and the <em>schedule it fills</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">This runs on your existing office number, or a new one registered to your practice, not to us. Every caller, every consult it books, and every patient record is yours and exportable any time, so the patient list you are building stays an asset you own instead of something you rent back month to month. Because a caller may be describing a child in treatment or their own health history, it is built to handle what they share with the discretion a medical or dental office is held to, collecting only what it needs to book the visit and keeping it inside your systems. The answering service is one piece of the Top Shelf platform, so a consult it books lands in the same CRM that nurtures the parents still thinking it over and reminds the patients whose treatment stalled, and the case it books today is the one your system keeps working for years.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A dad's lunch-break call, booked while the desk is <em>chairside</em>",
        "body_html": "It is a Tuesday and a father finally gets a free minute at lunch to look into Invisalign for his daughter, whose dentist mentioned her crowding at the last cleaning. He calls two orthodontists. Your front desk is chairside, seating a patient for an adjustment, so his call would normally ring to voicemail and he would move on to the next office before his break is over. Instead your answering service picks up, tells him the consult is free, confirms you take the family's insurance and that payment plans are available, and books the consult for a Thursday evening when he is off work. Your assistant never has to step away from the chair. You gain a consult, and likely the whole family, without anyone touching the phone. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my current office number?",
         "Yes. It can answer on the number your patients already call, or set up a new one registered to your practice. Either way the number and every call that comes through it belong to you and stay with you if you ever leave."),
        ("Can it answer the cost, insurance, and financing questions parents always ask?",
         "Yes, those are the calls it handles best. It can say that the first consult is free, that payment plans are available so cost does not end the call, whether you take their insurance, and what a first visit involves, and it books the consult right on your calendar. You decide exactly what it is allowed to say about pricing and coverage."),
        ("What about a patient with a poking wire or a broken bracket?",
         "It tells a real problem apart from a routine question. A poking wire, a broken bracket, a lost or cracked retainer, or real pain gets booked into your soonest opening and flagged to your team at once, while a consult or a billing question is handled without pulling anyone off the chair. You set what counts as urgent."),
        ("Will it handle both new consults and patients already in treatment?",
         "Yes. It books the free consult for someone new, and for a patient already in braces it can schedule an adjustment, handle a comfort issue, or hand anything unusual to a person, so nobody has to leave the chair to answer the phone."),
        ("How fast can it be answering?",
         "Setup is included with no separate onboarding fee. We configure your questions, your consult and financing answers, and your scheduling rules for you, so it is picking up in days, not weeks. Start with a free audit and we will show you how many consult calls your front desk is missing while it is chairside.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for orthodontists"),
        ("solution-ai-phone.html", "How the AI phone and chat system works"),
        ("crm-for-orthodontists.html", "The CRM that follows up on every call you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending consults to <em>voicemail</em>",
    "cta_sub": "Get a free audit that finds the gap in your consult calls: how many roll to voicemail and book elsewhere while your front desk is chairside, whether you work with us or not. No credit card, never a call center.",
},
# ================================ CRM for Orthodontists ================================
{
    "slug": "crm-for-orthodontists",
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "CRM for Orthodontists",
    "title": "CRM for Orthodontists | Top Shelf Business Solutions",
    "og_title": "CRM for Orthodontists",
    "meta_desc": "A CRM for orthodontists follows up on every consult a parent is thinking over and every referring dentist, so cases start instead of drifting away.",
    "service_schema_name": "CRM for Orthodontists",
    "eyebrow": "For Orthodontists",
    "h1_html": "CRM <em>for Orthodontists</em>",
    "answer_block": "A CRM for orthodontists keeps every lead, consult, and unstarted treatment plan in one place and reaches out for you, so the parent who is still thinking it over and the referring dentist who sends you cases both stay warm instead of drifting away. Your patient list and referral network quietly become your schedule.",
    "sections": [
        {"h2_html": "The consult you already gave is the case you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most orthodontic practices are not short on consults. They are short on follow-up. A parent brings their child in for a free consult, hears the plan and the price, and says they need to think it over, talk to a spouse, wait until the new year, or check what insurance will cover. An adult does the same, then gets busy. They walk out without starting, and between a full schedule of adjustments nobody circles back, so a case that was genuinely interested quietly goes cold. It was never a no. It just needed a warm, well-timed nudge a few days later, and a little reassurance about the money, which is exactly the thing a busy front desk never has time for.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every unstarted consult in front of you and follows up on a schedule you set, with messages that go out on time whether or not anyone remembers, and that can gently remind a family that payment plans make it doable. The parent who meant to start hears from you again while the smile is still on their mind, and the case you already earned the consult for actually begins.</p>'},
        {"h2_html": "Your referring dentists are a pipeline most practices <em>never tend</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Orthodontics runs on two engines, and the CRM feeds both. Alongside the families who find you directly, a general dentist who spots crowding, a bad bite, or a child ready for evaluation sends patients your way, and those referrals are some of the best cases you get. But a referral relationship goes cold without tending, and most practices never systematically stay in front of the dentists who feed them.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every lead, consult, treatment plan, and referral source lives in one place instead of scattered across your practice software and whatever the front desk remembers.</li><li>A referred patient is tracked from the day the dentist sends them, so you can see who was referred, who booked, and who slipped, and thank the dentist either way.</li><li>Referring offices stay warm with the occasional update and a closed loop when their patient finishes treatment, so the next case comes to you instead of the orthodontist down the road.</li><li>You can see exactly which families and which dentists have gone quiet and reach the right one with the right message at the right time.</li></ul>'},
        {"h2_html": "The patient who <em>stalled or finished</em> is still yours to bring back",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Not every lost case is a cold consult. Some patients did the paperwork and never started, some paused treatment and never came back, and every finished case turns into a retainer patient who should be checked and, eventually, needs a replacement. There is also the family you already treated: the younger sibling who is now the right age, the parent who saw what treatment did for their child and has quietly wanted their own smile fixed ever since. A light, steady touch, a note to the family whose paperwork stalled, a retainer-check reminder, a message to a past family that a sibling may be ready, is often all it takes to restart a case that was always yours. It costs almost nothing next to chasing brand-new consults with ads, and a single reactivation message to every family with a sibling coming of age can fill your consult book with people who already trust you.</p>'},
        {"h2_html": "You own the patient list, and it works with the <em>rest of the practice</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every patient, referral source, and note is yours and exportable any time, handled with the discretion a dental office is held to, not locked away inside software you only rent. Because one family is often several cases over many years, keeping them on a single record matters: the front desk can see that the mom booking an adjustment for her son once asked about Invisalign for herself, and that a younger sibling is coming of age, and handle all of it instead of treating each as a stranger. The CRM is one piece of the Top Shelf platform. It connects to the answering service, so a consult it books lands in your database ready to nurture, and to online booking, so a scheduled visit is logged against the right family with the full history already attached. For a practice whose value lives in its cases and its referral network, owning that list outright, and being able to take it with you, is not a small thing.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The consult that <em>finally starts</em>",
        "body_html": "A mother brings her twelve-year-old in for a free consult in October. She likes the plan but wants to wait until January, when the new insurance year resets and she has a better sense of the budget, and she leaves without starting. Normally that is the last anyone thinks of it, until she forgets or books somewhere else. Instead the CRM holds the plan and sends her a friendly note in early January that her benefits are fresh, that payment plans make the monthly number manageable, and that her son's spot is waiting, written to sound like the office she already trusts. She books the start that week. Nobody at the front desk had to remember. Illustrative example, not a client."},
    "faqs": [
        ("Does it work with my practice management software?",
         "It sits alongside it as your follow-up and outreach layer. Your leads, patients, referral sources, and treatment plans come in and stay yours and exportable, so the list you already have starts actively bringing cases back instead of just recording who came in."),
        ("Will it really follow up on consults that did not start?",
         "Yes, on the schedule you approve. A family that had the consult but did not begin gets a warm reminder a few days later, and another when their benefits reset, all sent for you and able to reassure them that payment plans make it doable. You can jump in and message anyone directly whenever you want."),
        ("Can it help me stay in front of referring dentists?",
         "Yes. It tracks every referred patient from the day the dentist sends them and keeps referring offices warm with occasional updates and a closed loop when their patient finishes, so the relationships that feed you cases do not go cold."),
        ("Can it bring back stalled and retainer patients?",
         "Yes. It can nudge a family whose paperwork stalled, remind finished patients about retainer checks, and reach past families when a younger sibling is coming of age, all from the same record and on a cadence you set."),
        ("How long until it is set up?",
         "Setup is included with no separate onboarding fee. We bring in your patients and referral sources, build your consult-nurture and reactivation sequences, and connect it to your phones and calendar, so it is working in days. Start with a free audit and we will show you where cases are slipping today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for orthodontists"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-orthodontists.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting consults and referrals <em>go cold</em>",
    "cta_sub": "Get a free audit that finds the gap in your follow-up: how many consults that did not start, referring dentists, and stalled patients are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ============================== Marketing for Orthodontists ==============================
{
    "slug": "marketing-for-orthodontists",
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Marketing for Orthodontists",
    "title": "Marketing for Orthodontists | Top Shelf Business Solutions",
    "og_title": "Marketing for Orthodontists",
    "meta_desc": "Orthodontist marketing keeps your Google profile active and your smile-transformation reviews fresh, so a parent searching for braces nearby finds you first.",
    "service_schema_name": "Marketing for Orthodontists",
    "eyebrow": "For Orthodontists",
    "h1_html": "Marketing <em>for Orthodontists</em>",
    "answer_block": "Orthodontist marketing keeps your practice visible where parents and adults look for braces and Invisalign, your Google Business Profile, the map, and your reviews, so the family searching for an orthodontist nearby finds an active, well-reviewed office and picks you instead of the one that let its profile go stale. It is how new cases find you before they call.",
    "sections": [
        {"h2_html": "A family picks the orthodontist they can <em>find and trust</em> first",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a parent decides it is time to look into braces, or an adult finally commits to fixing their smile, they do not ask around for weeks. They search for an orthodontist near them, glance at the map, and look at who has the most reviews and the highest ratings close by. They are about to commit to a long treatment and a real investment in their child or in their own smile, so those stars and that recent activity are the fastest trust they can get before they ever call. A practice with a thin, untouched profile quietly loses those searches to the office with a fuller one, and you never see the family that scrolled right past you.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The results you produce are probably beautiful, and your team may be the reason families in town recommend you. The problem is that a great practice with a neglected online presence looks, to a stranger searching at 9pm, about the same as a mediocre one. Marketing closes that distance so the reputation you have actually earned is the one a new family sees first.</p>'},
        {"h2_html": "Your Google Business Profile is the <em>front door</em> now",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">When a parent searches for an orthodontist near them, the map with its three local listings sits at the top, above the websites and above the ads. A profile that has not been touched in months, with old hours, no recent photos, and stale reviews, looks abandoned next to an office that keeps it current. Keeping yours active, complete, and honest, real photos of the office and the team, accurate hours, the insurance you take, whether you offer free consults and payment plans, and that you do both braces and clear aligners, is a quiet advertisement running in the exact spot people look when they are ready to book. It matters even more for orthodontics, because a parent is weighing a long relationship and a big check, and a profile that shows a real, friendly office and finished smiles tells them this is a place worth trusting with two years of visits. Wrong hours or a missing phone number does more than look sloppy. It quietly sends a ready-to-book family to an office whose information they can actually trust.</p>'},
        {"h2_html": "Win the neighborhoods you serve, on the strength of your <em>reviews and results</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A family wants an orthodontist they can get to easily, close to home, school, or work, because they are signing up for eighteen to twenty-four months of regular visits, so the people worth reaching live in a fairly tight radius around your office. Marketing to a whole metro just brings clicks from families who will never make that drive twice a month. Focusing your profile, your reviews, and your local content on the areas you truly serve is what puts you on the map for the searches that turn into booked consults. And reviews carry unusual weight here, because a parent is trusting you with a visible result on their child and a long commitment, so they read them closely. A review that describes a shy kid who now cannot stop smiling, or an adult thrilled they finally did it, speaks straight to what a new family is hoping for, and it does more to win them than anything you can say about yourself. Asking every happy family the day the braces come off, and replying to each review that comes back, feeds the profile that feeds the map, and the whole thing compounds.</p>'},
        {"h2_html": "Time your visibility to when families <em>actually start</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Orthodontic demand has a rhythm worth getting ahead of. Summer is when a lot of parents start kids in treatment so they settle in before the school year, so consults climb in late spring and summer. The new year brings adults resolving to finally fix their smile and families whose insurance benefits just reset, and tax-refund season gives families the lump sum that makes starting feel possible. Being visible right before each of those waves beats scrambling once they hit. A steady local presence, timely posts, fresh reviews, and current information keeps you top of mind for the family deciding now. This is the public-facing side of the practice, aimed at families who are not your patients yet. The private follow-up to the families and referring dentists already in your system is the CRM, and the two work best together.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "Summer, and you are the office <em>they can see</em>",
        "body_html": "It is May, and a mother decides she wants her son's crowding handled over the summer so he is used to his braces before the school year starts. She searches for an orthodontist nearby. Because your Google profile has been kept active all year, with recent photos of the office and finished smiles, accurate hours, the insurance you take listed, a note that consults are free, and a steady flow of reviews, you sit near the top of the map when she looks. She sees an office that is clearly busy, trusted, and easy to start with, and she books a consult with you instead of the one two listings down with a few old reviews. The practice that let its profile go quiet never comes up. Illustrative example, not a client."},
    "faqs": [
        ("Do you keep my Google Business Profile updated for me?",
         "Yes. We keep it active with photos of the office, the team, and finished smiles, posts, and accurate information on a regular schedule, and we keep your hours, the insurance you take, and whether you offer free consults and payment plans current, so it looks alive whenever someone searches for an orthodontist nearby."),
        ("What does focusing on my area actually mean?",
         "It means building your profile, reviews, and content around the neighborhoods your families realistically come from, since they will drive to you twice a month for two years, instead of spreading a budget across a whole metro. That is what gets you into the local map where families are choosing a practice."),
        ("How is this different from the CRM?",
         "The CRM follows up privately with families and referring dentists already in your system, nurturing consults and reactivating patients. Marketing is the public-facing side, your Google profile, reviews, and local visibility, aimed at families who need to find and trust you before they have ever called."),
        ("Can you help me get ahead of seasonal demand?",
         "Yes. We time your visibility to the waves that matter for orthodontics, the summer start before school, the new-year resolvers and benefit resets, and tax-refund season, so you are visible before families start searching instead of catching up after."),
        ("How long before it starts working?",
         "A neglected profile can climb in the local map within weeks once it is active and complete, and it compounds as reviews and content build. Setup is included, and a free audit will show you exactly how visible your practice looks to a family searching nearby today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for orthodontists"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-orthodontists.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the orthodontist they <em>can already see</em>",
    "cta_sub": "Get a free audit that finds the gap in your local visibility and reviews: how easily a family nearby can actually find and trust you right now, whether you work with us or not. No credit card, never a call center.",
},
# ========================= Websites & SEO for Orthodontists =========================
{
    "slug": "websites-seo-for-orthodontists",
    "trade_slug": "orthodontists", "trade_plural": "orthodontists",
    "hub_name": "Medical & Dental", "hub_slug": "industry-medical-dental.html",
    "breadcrumb_leaf": "Websites & SEO for Orthodontists",
    "title": "Websites & SEO for Orthodontists | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Orthodontists",
    "meta_desc": "An orthodontist website built for SEO ranks for braces and Invisalign near me, shows your financing and finished smiles, and books the free consult.",
    "service_schema_name": "Websites & SEO for Orthodontists",
    "eyebrow": "For Orthodontists",
    "h1_html": "Websites &amp; SEO <em>for Orthodontists</em>",
    "answer_block": "An orthodontist website built for SEO ranks for what a family searches, braces near me, Invisalign, orthodontist near me, and your city, shows your financing and finished smiles, and books the free consult the moment they land, so the case is yours instead of a directory renting your own families back to you.",
    "sections": [
        {"h2_html": "A family trusting you with a smile judges your practice by your <em>website in seconds</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A parent who just decided to look into braces, or an adult finally ready to fix their smile, is on their phone opening the first few practices they find. In a few seconds they decide whether each one looks like a place worth two years of visits and a real investment. A site that loads slowly, looks like it was built a decade ago, or does not work right on a phone tells them the office might be just as behind, and they back out and try the next one. It matters even more for orthodontics, because the site is selling a long relationship and a visible result, and a dated one quietly undercuts the confidence a family needs before they commit.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The site does not have to be flashy. It has to load fast, put your treatments, your location and hours, the insurance you take, and, above all, that consults are free and payment plans exist right in front of a visitor, and make booking that consult a single tap. Cost is the first thing a family worries about with braces, so a site that is upfront about financing and makes the free consult easy removes the exact hesitation that sends people to the next office. A beautiful site that hides how to book, or stays silent on cost, wastes the family it just earned.</p>'},
        {"h2_html": "Rank for what a family <em>actually searches</em>, braces and Invisalign",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not outrank a national aligner brand or a health directory this year for the broadest terms, and you do not need to. You can rank for your own name, for the specific towns and neighborhoods you serve, and for the exact searches families make: orthodontist near me, braces near me, Invisalign and clear aligners in your city, braces for kids, adult braces, and how much braces cost. Pages built around the treatments you provide and the areas you cover are what search engines, and a family deciding where to go, reward with the click. A page that explains, in plain language, what a first consult is like, the difference between braces and aligners, or how payment plans work also answers the quiet questions a nervous parent is already typing, which is the kind of content that earns both the ranking and the trust. That is depth a faceless directory has no reason to write for your town.</p>'},
        {"h2_html": "Stop letting a directory or an aligner brand <em>rent you your own patients</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Search for an orthodontist in your town and the top of the page is often a health directory, an insurance find-a-doctor tool, or a national mail-order aligner brand, not a local office. Those sites publish thousands of pages and carry years of authority, so a family lands there first, gets funneled into a list or a mail-order product, and your own prospective patient is treated as a lead someone else controls. Your site not ranking is not a vanity problem. It is the reason a family who should have found you directly gets routed through a middleman that lines your competitors up beside you or sells them a product you could have delivered better in person, and in orthodontics that skims the value of a relationship that could have spanned a whole family over years. A website that ranks on its own keeps the family yours from the first click, with no middleman between you and the person searching for exactly what you do, and it means they meet your office, your finished smiles, and your reviews before anyone can put a competitor in front of them.</p>'},
        {"h2_html": "The cases it earns are <em>yours to keep</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every dollar you put into a pay-per-lead service disappears the day you stop paying, and the family was never really yours. A website you own keeps ranking, keeps earning consults, and keeps compounding in value for as long as it exists, registered to your practice, not to a platform that can drop you or raise the rent. It plugs into the same CRM that follows up on every consult it captures and nurtures the parents still deciding, and the answering service that picks up the calls it drives, so a family the site earns at midnight is booked, followed up, and worked for years instead of slipping away before morning. It also does something a rented ad never will: a good site shows your finished smiles and is upfront about financing, so a family arrives at the consult already trusting you and already past the money worry. In a field where one case can mean two years of treatment plus the siblings and referrals that follow, an asset that keeps earning quietly is worth far more than a burst of paid clicks that stops the moment the invoice does.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A dentist's referral finds <em>you, not an aligner ad</em>",
        "body_html": "A family's dentist tells them their daughter is ready for braces and they should see an orthodontist. That evening the mother searches for an orthodontist near her to compare a couple of options. Instead of a national aligner ad that would sell her a mail-order product, or a directory that would route her to whoever paid for the spot, she finds your site ranking for that search, loading fast, with a page about braces and Invisalign for kids, your finished smiles, a clear note that the consult is free and payment plans are available, and a booking button right at the top. She books the consult that week, and that first visit is the start of treatment, and likely her younger son and her own long-postponed smile after it. You paid nothing per lead, and no middleman ever touched the booking. Illustrative example, not a client."},
    "faqs": [
        ("Will my site actually outrank the big directories and aligner brands?",
         "Not for the broadest terms overnight. It can realistically rank for your name, your specific towns and neighborhoods, and the braces, Invisalign, kids, and adult searches a national directory or aligner brand has no reason to target well for your town, which is exactly where a local practice can win."),
        ("How is this different from paying for leads or a directory listing?",
         "A pay-per-lead service or directory rents you a family it may also show to other offices, and it stops the day you stop paying. A website you own captures families who are yours alone and keeps working long after it is built, with no per-lead fee skimming the years of treatment a case is worth."),
        ("Can a website really help with the cost objection?",
         "Yes. Being upfront about free consults and payment plans, and making the consult easy to book, meets the first worry a family has about braces head on, so they arrive already past the money hesitation instead of never calling because they assumed they could not afford it."),
        ("Do I need a page for every treatment?",
         "You start with the ones that matter most, the braces, Invisalign, kids, and adult searches you want to grow, then expand. A focused set of strong treatment and location pages ranks better than one thin page trying to cover everything at once."),
        ("How long until it starts ranking?",
         "Local, specific searches can start moving within weeks, while broader terms take longer and compound over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.")],
    "related": [
        ("industry-medical-dental.html", "Everything Top Shelf does for orthodontists"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-orthodontists.html", "Staying visible in your area beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the search results for <em>your own town</em>",
    "cta_sub": "Get a free audit that finds the gap between your website and the directories and aligner brands taking your consult searches, whether you work with us or not. No credit card, never a call center.",
},
]
