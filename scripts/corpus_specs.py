"""Per-page content specs for the SEO corpus (plan §5). generate_corpus.py imports SPECS
from here. Each dict is one page's UNIQUE, hand-written, trade-specific content — the
generator owns the mechanics (shell, schema, events, interlinks, keyword placement), the
spec owns the substance that clears the uniqueness gate. Never templated find-and-replace.

Realtor batch. Payments is deliberately omitted for solo agents (they are paid through
title/escrow, not card, so a payment-processing page would be forced/thin).
"""

SPECS = [
# ============================ CRM for Real Estate Agents ============================
{
    "slug": "crm-for-real-estate-agents",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "CRM for Real Estate Agents",
    "title": "CRM for Real Estate Agents | Top Shelf Business Solutions",
    "og_title": "CRM for Real Estate Agents",
    "meta_desc": "A CRM for real estate agents follows up on every lead, past client, and sphere contact for you, so the ones who take months to transact still close with you.",
    "service_schema_name": "CRM for Real Estate Agents",
    "eyebrow": "For Real Estate Agents",
    "h1_html": "CRM <em>for Real Estate Agents</em>",
    "answer_block": "A CRM for real estate agents keeps every lead, past client, and sphere contact in one place and follows up for you, so a buyer who is months from moving and a seller who is only thinking about it stay yours instead of going cold. Your database quietly becomes your pipeline.",
    "sections": [
        {"h2_html": "The leads you already have are the ones you are <em>losing</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Most agents do not have a lead problem. They have a follow-up problem. A buyer calls in March, they are not ready until August, and by August they have forgotten your name because nobody stayed in touch. The lead was never bad. It just needed thirty seconds of attention every few weeks, and that is the thing there is never time for between showings and closings.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A CRM catches every lead the moment it comes in and works it on a schedule you set, with texts and emails that go out on time whether or not you remember. The buyer who is half a year out still gets a check-in, still sees your name, and still calls you when they are ready instead of the agent who happened to follow up last.</p>'},
        {"h2_html": "Your database <em>is</em> the business",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Past clients and your sphere are the cheapest business in real estate. A repeat seller and a referral cost you nothing to acquire and close faster than any cold lead. But you cannot personally remember to touch four hundred people on the right cadence, so most of that goodwill sits unused and slowly forgets you.</p><ul style="color:var(--ink-2);line-height:2;max-width:64ch;margin-top:.8rem"><li>Every contact, note, and conversation lives in one place instead of your head and three apps.</li><li>Closing anniversaries, market updates, and check-ins go out on schedule, so your sphere hears from you without you setting a single reminder.</li><li>You see who is heating up, so the ten-minute call you do have time for goes to the person about to transact.</li></ul>'},
        {"h2_html": "Answer first, without living on your phone",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A new online lead that hears back in the first few minutes is far more likely to convert than one that waits an hour, and in real estate the first agent to respond usually wins the client. The CRM replies instantly with a text-back the moment a lead comes in and hands it to you with the details, so you are first without refreshing your inbox at a closing table.</p>'},
        {"h2_html": "You own the database, even if you change brokerages",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Every contact and every note is yours and exportable any time. Change offices, change brokerages, and your book comes with you instead of staying behind on someone else\'s system. The CRM is one piece of the Top Shelf platform and plugs into the AI receptionist, so a call it captures lands in your database and gets followed up on automatically, and into online booking, so an appointment is logged against the right contact.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "The lead you <em>forgot about</em> calls you back",
        "body_html": 'A buyer inquires on one of your listings in the spring, tells you they are not moving until their lease ends, and you would normally lose track of them by summer. Instead the CRM keeps a light touch going, a market update here, a quick check-in there, all sent for you. In August the buyer texts that they are ready, and they text you, because yours is the name that stayed in front of them. You did not lift a finger to keep that lead warm.'},
    "faqs": [
        ("Does it import my existing contacts and past clients?",
         'Yes. Your current contacts, leads, and past clients come in and live in one place, and everything stays yours and exportable. The point is to make the database you already have actually work for you.'),
        ("Will it really text and email clients automatically?",
         'Yes, on the schedule you approve. New leads get an instant response, and your sphere gets the check-ins, market notes, and anniversary touches on a cadence you set, all sent for you. You can always jump in and message someone directly.'),
        ("Does this help with my sphere and past clients, or just new leads?",
         'Both, and the sphere is where the quiet money is. Repeat business and referrals close faster and cost nothing to acquire, and the CRM keeps you in front of those people so that business actually shows up instead of going to whoever they saw most recently.'),
        ("Do I keep my data if I change brokerages?",
         'Yes. Your contacts and notes are in your name and exportable any time, so if you switch offices your book goes with you. You are not renting access to your own database.'),
        ("How long until it is set up?",
         'Setup is included with no separate onboarding fee. We bring in your contacts, set up the follow-up sequences, and connect it to your calls and calendar, so it is working in days. Start with a free audit and we will show you where leads are slipping through today.')],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for real estate agents"),
        ("solution-crm.html", "How the CRM and follow-up system works"),
        ("ai-receptionist-for-real-estate-agents.html", "The AI receptionist that feeds it every call"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Stop letting good leads <em>go cold</em>",
    "cta_sub": "Get a free audit of how many of your leads and past clients are going unworked right now, whether you work with us or not. No credit card, never a call center.",
},
# ======================= Online Booking for Real Estate Agents =======================
{
    "slug": "online-booking-for-real-estate-agents",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "Online Booking for Real Estate Agents",
    "title": "Online Booking for Real Estate Agents | Top Shelf Business Solutions",
    "og_title": "Online Booking for Real Estate Agents",
    "meta_desc": "Online booking for real estate agents lets buyers and sellers self-schedule a showing or listing consult on your real availability, straight onto your calendar.",
    "service_schema_name": "Online Booking for Real Estate Agents",
    "eyebrow": "For Real Estate Agents",
    "h1_html": "Online Booking <em>for Real Estate Agents</em>",
    "answer_block": "Online booking for real estate agents lets a buyer or seller pick a showing or a listing consult straight from your website, your listings, or a text link, on your real availability, so you stop playing phone tag and the appointment lands on your calendar with the details you need to show up ready.",
    "sections": [
        {"h2_html": "Phone tag is quietly costing you <em>appointments</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A buyer wants to see a place. You are with another client, so you call back an hour later, they do not pick up, you trade voicemails, two days pass, and they tour it with the agent who could lock in a time on the spot. The appointment was never the problem. The back and forth was. When someone is motivated enough to book, the worst thing you can do is make them wait for a callback.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">A booking link lets them grab an open slot the moment they feel it, day or night, without reaching you first. You wake up to the appointment already set instead of a missed call you now have to chase.</p>'},
        {"h2_html": "It qualifies <em>before</em> it books",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Self-scheduling does not mean letting anyone onto your calendar. The booking form asks the questions that matter, buying or selling, price range, whether they are pre-approved, so a serious buyer books a showing and a maybe gets a quick call first. You set the rules: how much notice you need, how long each appointment runs, buffer time between them, and which hours are open at all.</p>'},
        {"h2_html": "A booking link everywhere a lead <em>finds you</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The link goes anywhere a lead already meets you: your website, each listing page, your email signature, the text you send after a sign call, and your Google Business Profile. Every one of those turns from a dead end that needs a callback into a place someone can book you in one tap. A seller comparing three agents on a Sunday night can put a listing consult on your calendar before they close the tab.</p>'},
        {"h2_html": "On your real calendar, and the appointment shows up",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">It syncs to the calendar you already use so it can never double-book you, and it sends the client a confirmation and a reminder, which is what actually cuts down no-shows. Every booking is logged against the right contact in your CRM, and it works alongside the AI receptionist, which can also book a caller who would rather talk than tap. The leads and the calendar stay yours.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "A Sunday-night seller books you <em>while you sleep</em>",
        "body_html": 'It is 9 p.m. Sunday and a homeowner is deciding which agent to call about listing. They land on your site, see you have real reviews, and instead of leaving a voicemail they will regret in the morning, they book a listing consult for Tuesday at 10 from the calendar right there on the page. You wake up Monday to the appointment already set, with their name, the property, and their timeline attached. No phone tag, no lost lead.'},
    "faqs": [
        ("Does it sync to my Google or Outlook calendar?",
         'Yes. It reads your real calendar so it only ever offers times you are actually free, and new bookings drop straight onto it. It cannot double-book you against a showing or a closing you already have scheduled.'),
        ("Can it respect buffers and stop back-to-back bookings?",
         'Yes. You set how much notice you need, how long each appointment runs, and how much buffer to leave between them, so you are never booked with no time to drive across town.'),
        ("Can buyers book showings and sellers book consults differently?",
         'Yes. You can offer different appointment types with their own questions and lengths, so a buyer books a showing and a seller books a listing consult, each capturing the details you need for that kind of meeting.'),
        ("Will it cut down on no-shows?",
         'It helps. Automatic confirmations and reminders by text and email are the single biggest lever on no-shows, and every booking includes them. Someone who booked themselves and got a reminder is far more likely to show than a loosely agreed callback.'),
        ("How fast can it be live?",
         'Setup is included, no separate fee. We connect your calendar, set up your appointment types and rules, and put the link on your site and listings, so it is taking bookings in days. Start with a free audit and we will show you where you are losing appointments today.')],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for real estate agents"),
        ("solution-booking.html", "How the online booking system works"),
        ("ai-receptionist-for-real-estate-agents.html", "The AI receptionist that can book callers too"),
        ("crm-for-real-estate-agents.html", "The CRM every booking is logged into"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Let clients book you <em>while you work</em>",
    "cta_sub": "Get a free audit of how many appointments your current callback process is costing you, whether you work with us or not. No credit card, never a call center.",
},
# ==================== Review Software for Real Estate Agents ====================
{
    "slug": "review-software-for-real-estate-agents",
    "trade_slug": "real-estate-agents", "trade_plural": "real estate agents",
    "hub_name": "Real Estate", "hub_slug": "industry-real-estate.html",
    "breadcrumb_leaf": "Review Software for Real Estate Agents",
    "title": "Review Software for Real Estate Agents | Top Shelf Business Solutions",
    "og_title": "Review Software for Real Estate Agents",
    "meta_desc": "Review software for real estate agents asks every happy client for a Google review at the right moment and makes it one tap, so your reputation earns referrals.",
    "service_schema_name": "Review Software for Real Estate Agents",
    "eyebrow": "For Real Estate Agents",
    "h1_html": "Review Software <em>for Real Estate Agents</em>",
    "answer_block": "Review software for real estate agents asks every happy buyer and seller for a review at the right moment, makes leaving one a single tap, and helps you respond to each, so your reputation keeps bringing referrals instead of depending on the few clients who remember to post on their own.",
    "sections": [
        {"h2_html": "Referrals run on reviews <em>now</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Before a seller picks a listing agent, they Google you and read what your past clients said. A thin profile with a handful of old reviews quietly costs you listings you never even hear about, because the homeowner just called the agent with the wall of recent five-star reviews instead. Your reputation is doing the selling whether you manage it or not.</p><p style="color:var(--ink-2);line-height:1.85;max-width:64ch;margin-top:1rem">The problem is not that your clients are unhappy. It is that happy clients forget to post, and asking feels awkward in the moment. Review software solves the timing and the awkwardness so the reputation you have actually earned shows up online.</p>'},
        {"h2_html": "Ask at the moment they are <em>happiest</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">The best time to ask is right after closing, when the client loves you and the keys just changed hands. The software sends the ask automatically at that moment, by text and email, with a link that takes them straight to your Google profile in one tap. No cornering people, no sticky notes to remember, and no asking three weeks later when the glow has worn off.</p>'},
        {"h2_html": "Respond to every review, good or <em>bad</em>",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">A thoughtful reply to each review tells the next homeowner reading it that you are engaged and professional, and responding is one of the signals that helps you show up in local search. The software flags every new review the moment it lands and helps you reply quickly, so a rare critical one gets a calm, professional response instead of silence, and every good one gets a thank you.</p>'},
        {"h2_html": "More reviews, more listings, compounding",
         "body_html": '<p style="color:var(--ink-2);line-height:1.85;max-width:64ch">Recent reviews feed your Google Business Profile, which lifts you in the local results a buyer or seller sees when they search for an agent, which brings more clients, which brings more reviews. It builds on itself. Your reputation is yours, tied to your own profile, not the brokerage. Review requests are part of the Top Shelf platform and fire automatically off a closing logged in your CRM.</p>'}],
    "example": {
        "eyebrow": "How it plays out",
        "h2_html": "One closing becomes <em>your next listing</em>",
        "body_html": 'You close a sale on a Friday. That afternoon, the software texts your happy seller a thank-you with a one-tap link, and they post a warm review before dinner. Three months later a neighbor a few doors down is thinking about selling, Googles agents in the area, and reads that exact review at the top of your profile. They call you instead of the sign down the street. You never asked twice, and you were not even in the office when it happened.'},
    "faqs": [
        ("Which review sites does it work with?",
         'It focuses on Google, which is where most buyers and sellers look first and what feeds your local search ranking. It can also point past clients to your other profiles. We follow each platform\'s own rules, including that a review should come from someone you actually worked with.'),
        ("When does it ask for the review?",
         'Right after closing, when the client is happiest, sent automatically by text and email with a one-tap link. You can adjust the timing and the wording so it sounds like you.'),
        ("Is automating review requests allowed?",
         'Asking every client for an honest review is fine and encouraged. What is not allowed is filtering out unhappy clients or paying for reviews, and this does not do that. It simply asks everyone at the right moment and makes it easy to say yes.'),
        ("What happens if I get a bad review?",
         'You find out immediately instead of weeks later, and the software helps you post a calm, professional response. One thoughtful reply to a critical review, sitting under a wall of genuine positive ones, often reassures the next reader more than a perfect record would.'),
        ("How long until it is running?",
         'Setup is included with no separate fee. We connect your Google profile, set the timing and the message, and tie it to your closings, so requests start going out in days. Start with a free audit and we will show you how your reputation stacks up against the agents you compete with.')],
    "related": [
        ("industry-real-estate.html", "Everything Top Shelf does for real estate agents"),
        ("solution-reviews.html", "How the review system works"),
        ("crm-for-real-estate-agents.html", "The CRM that triggers the ask at closing"),
        ("booking.html", "Book a 15-minute call to see it"),
        ("contact.html", "Get your free business audit")],
    "cta_h2_html": "Turn happy closings into <em>your next listing</em>",
    "cta_sub": "Get a free audit of how your online reputation compares to the agents you compete with, whether you work with us or not. No credit card, never a call center.",
},
]
