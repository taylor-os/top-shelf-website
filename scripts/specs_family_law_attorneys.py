"""Per-page content specs for the SEO corpus (plan §5), family law attorneys batch. Same
contract as scripts/corpus_specs.py: generate_corpus.py imports SPECS and owns the mechanics
(shell, schema, events, interlinks, keyword-first title/slug/H1/first-sentence); each dict
below owns the UNIQUE, hand-written, family-law-firm-specific substance that clears the
uniqueness gate. Never templated find-and-replace, never the plumber, personal-injury,
criminal-defense, or immigration content reworded.

Legal hub, shared with the personal-injury, criminal-defense, and immigration batches, so
these dicts are written family-law-distinct on purpose: divorce, custody, child and spousal
support, and modifications; a caller in an emotionally raw, private moment who needs a calm
human, not a voicemail; discretion that decides whether someone reaches out at all; the
consultation as the front door while a person is still deciding whether to proceed; consult
cancels and no-shows; cases that run months with emotional ups and downs where steady contact
holds the client; and empathetic, non-salesy marketing where reassurance beats bravado. Four
service angles are here in one file (the ai-receptionist dict carries "demo": True). Each
example body ends with the literal "Illustrative example, not a client." per the honesty rule;
if the generator also appends that line, dedupe there. Attorney advertising ethics: nothing
here promises or implies an outcome on custody, a divorce, or support, and the AI intake never
gives legal advice.
"""

SPECS = [
# ==================== AI Receptionist for Family Law Attorneys ====================
{
    "slug": "ai-receptionist-for-family-law-attorneys", "demo": True,
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "AI Receptionist for Family Law Attorneys",
    "title": "AI Receptionist for Family Law Attorneys | Top Shelf Business Solutions",
    "og_title": "AI Receptionist for Family Law Attorneys",
    "meta_desc": "A family law answering service answers every divorce and custody call with a calm human, runs intake, and books the consultation while you are in court.",
    "service_schema_name": "AI Receptionist for Family Law Attorneys",
    "eyebrow": "For Family Law Attorneys",
    "h1_html": "AI Receptionist <em>for Family Law Attorneys</em>",
    "answer_block": "A family law answering service answers every call the moment it rings, day or night, meets a divorce or custody caller with a calm, private human voice instead of a voicemail, captures the intake, and books the consultation while you are in court. Your number stays yours, and so does every caller who comes through it.",
    "sections": [
        {"h2_html": "A caller who finally worked up the nerve will not <em>leave a voicemail</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone deciding to call a family law attorney has usually carried that decision for weeks or months. Picking up the phone means admitting out loud that a marriage may be over, or that a custody arrangement has to change, and it is a private, painful step. When they finally dial and reach a voicemail, the nerve they spent so long building drains away, or they simply move down the list and call the next name until a calm human answers. In this practice the firm that answers gently, in the moment a person is most raw, is very often the firm they retain, because they are not shopping on price. They are looking for someone who feels safe to trust with their family.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">But you are in a hearing, in a mediation, or across the desk from another client whose life is also coming apart, so the call rolls to voicemail and the consultation goes to whoever picked up. A family law answering service answers on the first ring, stays warm and unhurried with a caller who may be in tears, learns what is going on and whether anyone is in danger, and books the consultation on your calendar instead of letting it slip away. You come back to the intake already written up, with the caller\'s name and situation attached.</p>'},
        {"h2_html": "Built for a caller who may be <em>speaking in a whisper</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Family law calls do not sound like any other kind. The person may be calling from a parked car, a locked bathroom, or a break at work, keeping their voice down because the other spouse is in the next room and does not know yet. They may not be able to say much, and they may have to hang up without warning. A voicemail box cannot meet that person with any warmth, and a generic call center reading a script does not understand that a question about a child being kept from a parent is nothing like a routine question about filing fees.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Answers day and night, so the parent who can only call once the kids are asleep, or the spouse who can only talk from the car, reaches a patient, real conversation instead of a machine.</li><li>Meets the caller gently and gathers what a matter actually starts with: what they are facing, whether it is a divorce, custody, child or spousal support, or a change to an existing order, whether children are involved, and whether anything has already been filed or served.</li><li>Keeps that first contact private and calm, so a frightened caller feels heard rather than processed, which is often what decides whether they trust you with the rest.</li><li>Treats a returning client or a referral differently from a first-time caller, so someone who already knows your firm never lands in a voicemail box.</li></ul>'},
        {"h2_html": "Most family law calls are not 2am emergencies, which is why the <em>urgent ones slip through</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most of what comes in is not a middle-of-the-night crisis, and that is exactly why the genuine emergencies get buried. A parent whose child was just taken or kept in violation of an order, a spouse who is afraid for their safety and needs an emergency protective order, a person who was just served with papers that carry a fast deadline, these cannot wait until Monday, and a message left in a voicemail box over a weekend can cost someone dearly. A family law answering service can tell those apart from a caller who is only beginning to think about a divorce and wants to understand their options.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">You decide what counts as urgent, and when a caller describes one of those situations the service flags it to your on-call attorney at once so a real person can respond quickly, while the routine consultations land on your calendar. And the math is forgiving: a single matter you would have lost to a voicemail on a weekend is usually worth far more to your firm than the service costs, and everything it captures after that is on top.</p>'},
        {"h2_html": "You <em>own</em> the number, the intake, and the client list",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The service runs on the number your firm already advertises, or a new one put in your name, and the number and everything that comes through it stay yours. Every caller, every intake, every private detail is exportable whenever you want it, so the people you spend real money to reach become an asset your firm holds onto instead of a list you effectively rent back each month. Nothing locks your data behind a long contract. The answering service is one piece of the Top Shelf platform, and it hands each consultation it books straight to the same CRM that follows up, so a person who has not decided yet is never left to go cold. And it stays firmly in its lane: it listens, reassures, and writes down the facts, and it never offers legal advice or predicts anything about how a divorce, a custody dispute, or a support question will resolve. Those calls belong to your attorneys alone.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A late call from a locked bathroom, <em>captured while you sleep</em>",
        "body_html": 'It is late, the children are finally asleep, and a mother decides she needs to find out what leaving would actually take. She calls from the one room with a door that locks, keeping her voice low. The first two firms she tries send her to voicemail, and she almost loses her nerve. Yours answers gently, does not rush her, learns there are two young children and that she has not been threatened but is frightened and unsure, and books her a private consultation for later that week. You arrive in the morning to the intake already written up, with a note that she asked for discretion, instead of never knowing she called. Illustrative example, not a client.'},
    "faqs": [
        ("Does it work with my current firm phone number?",
         'Yes. It can answer on your existing number, or set up a new one registered in your name. Either way the number and every intake that comes through it belong to your firm and go with you if you ever leave.'),
        ("Can it actually handle an emotional caller with care, not just take a message?",
         'Yes, that is the point. It answers warmly and unhurried, keeps the first contact private, and gathers what a matter actually starts with, what the person is facing, whether children are involved, whether anything has been filed, and writes it up so you can pick it up cold. You decide exactly what it asks and how gently it asks it.'),
        ("Will it flag a true emergency, like a safety concern or a child being withheld, to my attorney?",
         'It flags the calls you tell it to treat as urgent, a caller afraid for their safety, a child taken or kept against an order, papers just served with a fast deadline, and alerts your on-call attorney right away so a real person can respond. You set what counts as drop-everything.'),
        ("Is it going to give the caller legal advice or promise how their case will go?",
         'No, and this matters. It listens, reassures, and captures the facts; it never advises on the matter, never guesses at custody or support, and never promises an outcome. What to do, whether to take the matter, and every legal judgment stay with your attorneys. A frightened caller mostly needs to feel heard and to know a real firm is handling it, and a calm voice that gets the details beats a voicemail box.'),
        ("How fast can it be running?",
         'Setup is included with no separate onboarding fee. We build your intake questions, your booking, and your urgent-case rules for you, so it is answering in days, not weeks. Start with a free audit and we will show you what your current phone setup is missing.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for family law attorneys"),
        ("solution-ai-phone.html", "How the AI phone and intake system works"),
        ("crm-for-family-law-attorneys.html", "The CRM that follows up on every consultation you capture"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop sending your hardest callers to <em>voicemail</em>",
    "cta_sub": "Get a free audit of how many calls and after-hours consultations your current setup is missing, whether you work with us or not. No credit card, never a call center.",
},
# ========================= CRM for Family Law Attorneys =========================
{
    "slug": "crm-for-family-law-attorneys",
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "CRM for Family Law Attorneys",
    "title": "CRM for Family Law Attorneys | Top Shelf Business Solutions",
    "og_title": "CRM for Family Law Attorneys",
    "meta_desc": "A CRM for family law attorneys follows up with every consultation and no-show and keeps clients steady through a long divorce or custody case.",
    "service_schema_name": "CRM for Family Law Attorneys",
    "eyebrow": "For Family Law Attorneys",
    "h1_html": "CRM <em>for Family Law Attorneys</em>",
    "answer_block": "A CRM for family law attorneys chases the consultations that cancel or no-show while someone is still deciding whether to file, and keeps signed clients steady through the long, emotional months of a divorce or custody case. The person who almost walked away hires you because your firm followed up with care.",
    "sections": [
        {"h2_html": "The consultation someone books while wavering is the one that <em>quietly cancels</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most family law firms do not have a call problem. They have a follow-through problem, and it is a particular kind. Someone books a consultation while they are still deciding whether to go through with anything at all. Then the fear settles in, or a spouse promises to change, or the thought of what it will do to the kids stops them cold, and they cancel, no-show, or simply go quiet. They were not a bad lead. They were an ambivalent one, and ambivalence is the normal state of a person standing at the edge of ending a marriage or a custody arrangement. What they needed was a gentle, patient reminder that you are there when they are ready, and that is the touch there is never time for between hearings.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM keeps every consultation that has not turned into a case in front of you and follows up for you, on a schedule you set, with messages that sound like your firm and never pressure. It is not a sales chase; it is a quiet, respectful nudge that you are still here. The person who canceled once because they lost their nerve hears from you again at the right moment, instead of drifting to the firm that happened to check in, or letting the whole matter sit unaddressed for another year.</p>'},
        {"h2_html": "The long, quiet stretches are when a scared client <em>starts to spiral</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Signing the client is the start of a long, uneven road. A divorce or custody case moves in fits and starts, temporary orders, discovery, mediation, waiting on the other side, waiting on the court, with long quiet stretches in between, and unlike most matters this one is wrapped in raw emotion the whole way. A client who hears nothing during a quiet stretch does not assume things are fine. They assume the worst, that their case has been forgotten, that they are losing, and a scared client is the one who calls your office again and again, posts a hurt review, or fires you mid-case. Keeping every client gently in the loop is exactly what slips when your own week is buried in other people\'s hearings.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every client, consultation, court date, and note sits in one place instead of scattered across message slips, a shared inbox, and three people remembering different things.</li><li>A check-in before each step and through the quiet weeks, so a client hears a steadying word before they start to panic, not after they have already called five times.</li><li>Reminders reach the client ahead of a temporary-orders hearing, a mediation, or a deadline to exchange documents, so the date does not slip because everyone assumed someone else was watching it.</li><li>A clear view of who has gone quiet on your calendar, so you reach the anxious client before they reach for another firm\'s number.</li></ul>'},
        {"h2_html": "The people who send you cases are <em>past clients, therapists, and financial advisors</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Family law runs on its own quiet web of referrals, and it is not the web an injury or criminal practice has. A past client who felt guided with patience through the worst chapter of their life is the one who tells a coworker or a sister, when their turn comes, exactly who to call. A marriage therapist, a financial advisor untangling a couple\'s accounts, a real estate agent handling the sale of a shared home, all meet people at the moment a family is coming apart and can point them to a lawyer they trust. None of that stays warm on its own, and it is delicate, because people are private about a divorce and a referral is a personal vouch. A CRM keeps a light, respectful touch on past clients and referral sources, a check-in after a case closes, a thank-you when someone sends a person your way, so your firm is the first name that comes up the next time a person in that circle needs help.</p>'},
        {"h2_html": "One list, wired to your calls and every <em>step of a long case</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every client and every note belongs to you and can be exported whenever you like, never sealed inside a tool you lease by the month. The CRM is one piece of the Top Shelf platform: the consultations your answering service books flow into it and the follow-up begins on its own, and each meeting, hearing, and next step hangs on the right person so nothing lives in two systems or falls out of both. Your family law case-management software still holds the official file, the pleadings, and the court deadlines. The CRM works the human side of a long, emotional case: the people still deciding, the clients who need a steadying word through the quiet weeks, and the past clients and professionals who send you work. It carries the relationship while your attorneys carry the case and make every legal call, and it never promises a client a thing about how their matter will end.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The consult that canceled, and <em>signed a month later</em>",
        "body_html": 'A man books a consultation about filing for divorce, then cancels the morning of, telling your front desk he wants to try counseling one more time. Normally that is the last you hear of it. Instead the CRM, seeing the consult never converted, sends a gentle, no-pressure check-in a couple of weeks later and another a few weeks after that, both written to sound like your firm. When counseling does not hold and he is finally ready, yours is the only firm that stayed kindly in touch, so he calls back and retains you without shopping around again. Nobody on your team had to remember him. Illustrative example, not a client.'},
    "faqs": [
        ("Does it import the clients and consultations I already have?",
         'Yes. Your current clients, the people who came in for a consultation, and your notes all come in and live in one place, and every bit of it stays yours and exportable. The point is to put the relationships your firm has already built to work instead of letting them sit forgotten in a phone and an inbox.'),
        ("Will it follow up on someone who booked a consult but got cold feet?",
         'Yes, on the schedule you approve. A consultation that cancels or never converts gets a gentle, no-pressure check-in later and another after that, sent for you, so an ambivalent person keeps hearing that you are there while other firms forget them. You can step in and reach anyone yourself any time.'),
        ("Can it keep a client calm through the long quiet stretches of a case?",
         'Yes, and that is often the biggest win. You set the rhythm, and it sends steadying check-ins before each step and through the waits, so a frightened client hears from your firm before they spiral, instead of calling your office over and over or drifting away hurt.'),
        ("How is this different from my family law case-management software?",
         'It sits alongside it. That software runs the legal file, the pleadings, and the filing deadlines. This runs everything around it: the consultations you have not signed, the clients who need reassurance through a long case, and the past clients and professionals who refer you. The two do different jobs.'),
        ("How long until it is set up?",
         'Setup is included with no separate onboarding fee. We import your contacts, set up your follow-up and check-in sequences, and tie it into your calls and booking, so it is running within days. Start with a free audit and we will show you where consultations and clients are slipping today.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for family law attorneys"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-family-law-attorneys.html", "The AI receptionist that feeds it every consultation"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting unsure consultations <em>slip away</em>",
    "cta_sub": "Get a free audit of how many of your consultations, no-shows, and past clients are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ====================== Marketing for Family Law Attorneys ======================
{
    "slug": "marketing-for-family-law-attorneys",
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Marketing for Family Law Attorneys",
    "title": "Marketing for Family Law Attorneys | Top Shelf Business Solutions",
    "og_title": "Marketing for Family Law Attorneys",
    "meta_desc": "Family law firm marketing keeps your Google profile active and your reviews warm, so a person facing divorce trusts your firm enough to call.",
    "service_schema_name": "Marketing for Family Law Attorneys",
    "eyebrow": "For Family Law Attorneys",
    "h1_html": "Marketing <em>for Family Law Attorneys</em>",
    "answer_block": "Family law firm marketing keeps your firm visible and trusted where people quietly look for help, your Google Business Profile and your reviews, so when someone facing a divorce or a custody fight searches nearby, your name is the calm, compassionate one they feel safe enough to call.",
    "sections": [
        {"h2_html": "Choosing a family lawyer is a <em>private, high-trust decision made in pain</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Nobody hires a family lawyer on impulse, and nobody is proud to be looking. This is a decision about their children, their home, and their future, made in the middle of grief, anger, or fear, and often kept secret from the people around them. So they research quietly, late at night, on their own phone, comparing a couple of firms and reading reviews before they let anyone in. That changes what your marketing has to do. You are not catching someone in a single frantic moment the way an accident or an arrest does; you are staying visible and looking trustworthy through the private, drawn-out stretch of time a person spends working up to the call.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">Get found and look trustworthy through that window and the consultation is usually yours. A firm that shows up thin, stale, and barely reviewed loses to the one that looks present, human, and kind, no matter how skilled the lawyer behind the quiet profile actually is. Because so much of this search happens in private, without a friend to ask, what a person can see about you online carries the weight a personal referral would carry in another field.</p>'},
        {"h2_html": "The aggressive-lawyer act repels more clients than it <em>wins</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A lot of family law advertising leans on the aggressive angle, the pit bull, the fighter, the promise to destroy the other side. For a slice of clients that lands, but for many more it is exactly wrong. Someone who still has to co-parent with their ex for the next decade, or who simply wants to get through this with their dignity intact, is frightened off by a lawyer who looks like they will pour gasoline on the fire. What reassures the person searching in pain is a profile that looks calm, current, and genuinely human: a real firm with real people, clear information, and reviews that describe being treated with compassion and kept informed. Striking that tone is frequently what separates a call from a closed tab.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Reviews that speak to being treated with care, kept informed, and guided with patience, which reassure a frightened person far more than any boast about winning.</li><li>Accurate practice areas, hours, address, and phone number, so someone reaching out in a hard moment never hits wrong or missing information.</li><li>Current photos and an honest picture of how you work, so your firm reads as approachable people rather than a billboard.</li><li>The questions a scared first-timer actually asks, what a consultation is like, whether it stays confidential, answered right where they will see them.</li></ul>'},
        {"h2_html": "Be known for the <em>help someone is actually searching for</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A generic family law banner blends into every other firm on the page. What people actually search, and what earns real local standing, is the specific thing weighing on them: a divorce, a child custody dispute, child or spousal support, or a modification to an order that no longer fits their life. Being known in your area as a firm that handles the matters you genuinely take, with a profile and content built around them, is worth far more than a wide, shallow presence across every category at once, and it draws the cases you want instead of calls you have to turn away. It matters more in family law than in most fields, because word of mouth here is muted: people going through a divorce rarely broadcast it, so the referral that would carry another business travels quietly, if at all, and being easy to find for the exact matter someone faces has to do that work instead. It also keeps you anchored to the community you actually serve, so the people close enough to sit down with you are the ones who find you.</p>'},
        {"h2_html": "Reviews that speak to <em>compassion</em>, earned within the rules",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Reviews carry enormous weight with someone choosing a family lawyer, but they behave differently here than in most trades. Clients are often deeply private about a divorce or a custody fight and reluctant to post publicly about the hardest chapter of their life, so the reviews you do have need to be genuine, gathered with care, and collected only from the people willing to give them, never pressured or paid for. When a review speaks to being treated with dignity, kept informed through a long case, and helped without judgment, it reassures the next frightened caller more than anything you could say about yourself. And all of it stays inside the rules for attorney advertising: no promising or implying an outcome on custody, a divorce, or support, no fabricated or incentivized reviews, no misleading claims. This is the side of your firm the public sees, aimed at people who are not yours yet; the quiet follow-up with the people already in your database is the CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A quiet, late-night search that ends <em>at your firm</em>",
        "body_html": 'A woman who has not told anyone she is thinking about divorce spends two weeks reading quietly at night before she trusts anyone with it. Every time she looks, your firm\'s profile is active, with recent reviews that describe people being treated with compassion and kept informed through a hard year. The firm one listing down looks abandoned, old reviews, missing hours, no sign anyone is home, and another shouts about being the most aggressive attorney in town, which is the last thing she wants. She books a consultation with you, because yours is the only one that feels both real and safe. Illustrative example, not a client.'},
    "faqs": [
        ("Do you post to my Google Business Profile for me?",
         'Yes. We keep it active with updates, real replies to reviews, and local content on a regular schedule, and keep your practice areas, hours, and service area accurate, so it looks current and cared for whenever someone searches for a family lawyer near them.'),
        ("I do not want to look like an aggressive divorce lawyer. Can marketing reflect that?",
         'Yes, and for many family firms that is the smarter position. We build your profile and reviews around calm, compassionate, capable guidance, which is what most people quietly searching for help are actually looking for, rather than the combative image that scares off a parent who still has to co-parent for years.'),
        ("My clients are very private and will not post reviews. How does that work?",
         'We ask only the clients who are willing, and never pressure anyone or pay for a review. Even a few honest ones that speak to being treated with dignity and kept informed do the reassuring, and we help you reply to each with care, which matters more here than sheer volume.'),
        ("Is this allowed under attorney advertising rules?",
         'Yes, and working within those rules is the entire point. No promising or implying an outcome on a divorce, custody, or support, no fake or paid reviews, no misleading claims. We keep your real profile active and your honest reviews visible, which is both allowed and what actually earns a frightened person\'s trust.'),
        ("How is this different from the CRM follow-up?",
         'The CRM works quietly on the people already in your world: consultations you have not signed, current and past clients, and the sources who refer you. Marketing is the public side: being visible, current, and trustworthy to the person in pain who has never heard of you and is quietly searching for a family lawyer tonight.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for family law attorneys"),
        ("solution-marketing.html", "How the marketing and reputation system works"),
        ("websites-seo-for-family-law-attorneys.html", "The website that captures the demand this drives"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Be the firm they feel <em>safe enough to call</em>",
    "cta_sub": "Get a free audit of how visible and trustworthy your firm looks to someone quietly searching for a family lawyer in your area right now, whether you work with us or not. No credit card, never a call center.",
},
# =================== Websites & SEO for Family Law Attorneys ===================
{
    "slug": "websites-seo-for-family-law-attorneys",
    "trade_slug": "family_law_attorneys", "trade_plural": "family law attorneys",
    "hub_name": "Legal", "hub_slug": "industry-legal.html",
    "breadcrumb_leaf": "Websites & SEO for Family Law Attorneys",
    "title": "Websites & SEO for Family Law Attorneys | Top Shelf Business Solutions",
    "og_title": "Websites & SEO for Family Law Attorneys",
    "meta_desc": "A family law attorney website built for SEO ranks for divorce and custody lawyer searches in your city and turns a private researcher into a consultation.",
    "service_schema_name": "Websites & SEO for Family Law Attorneys",
    "eyebrow": "For Family Law Attorneys",
    "h1_html": "Websites &amp; SEO <em>for Family Law Attorneys</em>",
    "answer_block": "A family law attorney website built for SEO ranks for what a person quietly types at night, a divorce lawyer near me, a child custody attorney, help changing a support order, and meets them with a calm, private, trustworthy page that turns a careful researcher into a consultation that belongs to your firm.",
    "sections": [
        {"h2_html": "Your site is the first proof you will handle a family <em>with care</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Someone weighing a divorce or a custody case is not landing on your site in a panic, they are researching, carefully and often secretly, because it is their children and their future and the hardest decision of their life. They arrive raw and a little ashamed to be there at all, and in the first few seconds they are asking one quiet question: does this feel like a firm that will treat me with care, or one to click away from. A site that opens cleanly, explains the process in plain and gentle language, speaks to the exact matter they are facing, and shows real people and honest reviews answers that with a yes. A cold, generic template answers it with a no, no matter how good the firm behind it is.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">For family law the website is not a brochure, it is the first proof that you are someone safe to hand a family\'s future to. That proof is what carries a cautious, hurting visitor from reading to requesting a consultation, instead of closing the tab and telling themselves they will deal with it some other day.</p>'},
        {"h2_html": "Rank for the <em>matter someone is facing</em>, not a slogan",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">You will not top a national legal directory this year for a broad phrase like family lawyer, and you do not have to. The searches that turn into consultations are narrow and local: a divorce lawyer in your city, a child custody attorney nearby, help with child or spousal support, a modification to an order that no longer fits. Those are exactly the searches a national directory has no reason to serve well, and exactly where a real local firm can win. Pages built around the matters you genuinely handle and the community you actually serve are what a search engine can rank and what an anxious searcher clicks. A single page that only says family law competes with everyone and stands out to no one, while a page that speaks to the specific situation someone is in feels like it was written for them. Each focused page you add quietly claims a little more of your own area\'s family law traffic, one matter and one neighborhood at a time.</p>'},
        {"h2_html": "Private, unsure, and needing to reach you <em>without a phone call</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The visitor is often on a phone, emotional, and not ready to say any of this out loud to a stranger, sometimes not even ready for anyone in the house to know they are looking. The site has to make the first step easy and low-pressure, and it has to offer a private way to reach out, not just a phone number, because for many people that discretion is the very thing that decides whether they make contact at all. Every extra click, every demanding form, every wall of dense legal language is a reason for an already-overwhelmed person to give up and close the tab.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Opens fast and reads calmly on a phone, because that is where most of your visitors are quietly looking.</li><li>A private, low-pressure way to reach out for the person who cannot say it out loud yet, alongside a clear phone option for the person who wants to talk now.</li><li>Plain, gentle explanations of a confusing and frightening process, with no jargon and no claims about how a case will end.</li><li>Real people and honest reviews up front, so a wary visitor can decide in seconds that your firm is real and safe to contact.</li></ul>'},
        {"h2_html": "The consultations belong to <em>you</em>, not a directory",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Run a search for a divorce or custody lawyer in your town and look at who actually sits on top. Often it is not a single local firm, it is a directory or a pay-per-lead company that has outranked every attorney in the county and now sells the person who clicks, sometimes to three firms at once, sometimes back to you for a cut of a fee a splitting family is already struggling to cover. For as long as you have no real site of your own, those quiet, hurting searchers belong to a middleman, not to you. Owning the page changes the whole arrangement: the person reaches your firm and no one else, nothing is skimmed off the top of every matter, and the site keeps ranking and compounding for years rather than vanishing the day you stop paying a lead bill. It is registered to your firm, not to a platform that can drop you or raise your rate, and it feeds the same CRM and answering service that catch and follow up on every consultation it brings in. It brings people to your door; it never promises a single one of them an outcome.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A custody search that finds <em>your firm, not a middleman</em>",
        "body_html": 'A father worried about losing time with his kids searches for a child custody attorney in his city, late, after everyone else is asleep. Instead of a directory that would take his information and sell it to three firms, he finds your site ranking for exactly that, calm and plainly written, clearly a real firm with real people, with reviews from parents who felt guided with care. He sees a private way to reach out, sends a short message rather than making a call he is not ready to make out loud, and it comes straight to you with no middleman in between. Illustrative example, not a client.'},
    "faqs": [
        ("What family law terms can my site realistically rank for?",
         'The specific and local ones: your firm name, and the matters you handle paired with your city, a divorce lawyer, a child custody attorney, child or spousal support, a modification near you. That is the ground a local firm can take, not the broad national terms a directory locked up years ago.'),
        ("Can the site offer a private way to reach out, not just a phone number?",
         'Yes, and for family law it should. Many people are not ready to say it out loud, or cannot talk freely at home, so a discreet, low-pressure message option turns a hesitant visitor into a consultation you would otherwise have lost to a phone call they were not ready to make.'),
        ("How is this different from paying for leads or a directory?",
         'A lead service or directory sells you a contact it hands to other firms too, and the day you stop paying it goes dark. A site your firm owns keeps the consultation to itself, and it goes on ranking for years after it is built, with nothing skimmed off each case you take.'),
        ("My clients are private and cautious. Can a website really build that trust?",
         'Yes, and it is one of the site\'s central jobs. A clean, calm page that explains the process gently, shows real people and real reviews, and makes no claims about outcomes tells a hurting person you are safe to contact. That is frequently what tips someone from lurking to reaching out.'),
        ("How long until it starts ranking?",
         'The narrow, local searches can begin to move within weeks; the broader and more competitive ones take longer and build over months. Setup is included with no separate fee, and a free audit will show you where your current site, or lack of one, stands today.')],
    "related": [
        ("industry-legal.html", "Everything Top Shelf does for family law attorneys"),
        ("solution-websites-seo.html", "How the website and SEO system works"),
        ("marketing-for-family-law-attorneys.html", "Staying visible in your community beyond your site"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Own the family law searches in <em>your own city</em>",
    "cta_sub": "Get a free audit of how your website and local search presence compare to the directories and lead-sellers taking your divorce and custody consultations, whether you work with us or not. No credit card, never a call center.",
},
]
