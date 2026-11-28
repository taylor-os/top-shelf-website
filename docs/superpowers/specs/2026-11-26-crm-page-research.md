# CRM page research (2026-11-26)

Read-only research for the CRM and Websites pages: competitor teardown, what buyers want and fear, and an inventory of what our CRM really does. Sources were read live on 2026-11-26. Reddit, G2, Capterra, Software Advice and TrustRadius blocked fetching, so buyer evidence comes from about 180 Trustpilot reviews across 7 vendors, vendor FAQs and pricing pages, an ACHR survey of HVAC techs, and comparison articles (some written by competitors). The repos read were FieldPro (FP, HEAD 2eaf3c0) and top-shelf-crm (TS, HEAD 9387c454).

## Read first: claims the site must not make yet
1. **"AI chatbot added to your current website": not built.**
   - `top-shelf-crm/config/essentials.php` has `chat_widget: pending`.
   - The only chatbot running is the one on Top Shelf's own site.
2. **"Automatically asks for reviews": requests are manual.**
   - FieldPro's `NotificationEvent` says "no automatic send yet". Requests go out only from the Ask / Ask all buttons.
   - The Top Shelf CRM sends them one at a time.
   - Honest wording: "One tap texts and emails your review link."
3. **"Review replies": saved in the app only, never posted to Google.**
   - TS `ReviewController::respond` stores the reply in the app.
   - FP can read Google reviews but can't post a reply back.
4. **Possible review gating (compliance risk).**
   - The TS `PublicReviewController` sends ratings at or above `positive_threshold` (default 4 stars) to Google and keeps lower ratings private.
   - Google's policy appears to prohibit this. Verify, and never advertise it.
5. **"AI answers and books" is FieldPro only.**
   - TS `AiReceptionist` only captures the caller's details; it doesn't book.
   - TS missed-call text-back is off by default.
6. **Which app do Signature customers get?**
   - Dispatch board, on-my-way texts, estimates, the customer hub and AI booking are built in FieldPro (Contractor Pro mirrors it).
   - top-shelf-crm has contacts, pipelines, inbox, booking calendars, workflows, invoices, review requests, CSV import/export and the industry suites.

## Competitors (headline · public price · contract · card rate · trial · proof)
- **ServiceTitan:** "AI software for commercial and residential trades" · no public price · contract not stated · rate not shown · demo only · 100,000+ pros
- **Housecall Pro:** "Everything to run and grow your business" · $79 for 1 user, $189 for 5, $329 for 8, +$35 per extra user · "No long-term contracts" · cards from 2.59%, ACH 1% · 14-day trial · 4.7 from 2,700+ reviews
- **Jobber:** "Run a stronger service business" · 10 users about $299 · monthly or annual, both auto-renew · 2.9% + 30¢ (tap to pay 2.7% + 30¢), ACH 1% · 14-day trial · 4.8 App Store
- **Workiz:** "AI growth engine for home service businesses" · price on request · billed annually · rate not shown · 7-day trial
- **GoHighLevel:** "AI-powered business operating system" · $97 / $297 / $497, unlimited users · month-to-month · you bring Stripe · 14-day trial
- **Podium:** "#1 converting AI Employee for local businesses" · no public price · demo only · message caps and a 10DLC fee
- **Thryv:** "Less Stress. More Bookings." · $99 for 1 user, $399 for 5 · $250 onboarding fee "waived" · its plan is also called "Signature"
- **Tekmetric (auto):** $199 to $439, unlimited users · "No contracts or hidden fees" · "live the same day" · migration from 150+ systems
- **Shopmonkey (auto):** $239 for 3 users, +$20 per user · $500 migration fee in the footnotes
- **Vagaro (salon/fitness):** from $23.99, +$10 per calendar · payments need a 12-month minimum or a $150 fee · 15-minute setup claim · free data transfer · 30-day trial
- **Square Appointments:** $0 / $49 / $149 · 2.6% / 2.5% / 2.4% + 15¢

**What they lead with, by how many of the 11 do it:**
1. All-in-one (~10)
2. Get paid (~8)
3. Win leads (~8)
4. AI in the headline (7)
5. Growth percentages, mostly unsourced (~7)
6. Built for your trade (~7)
7. Reviews (~6)
8. Run it from your phone (~5)
9. Hours saved (3 to 4)

**How they show ease of use:**
- No-card trials
- Guided tours
- Setup-speed claims
- Free migration
- Onboarding specialists
- 24/7 or US-based support
- Badges

None of them uses a 3-step "how it works" section.

**FAQ topics that come up on 3 or more sites:**
- Contract or cancel
- Cost or plan
- Trial
- My industry or size
- Changing plans
- QuickBooks and integrations
- Users
- Hidden or setup fees
- Setup time
- Getting data in and out
- Mobile app

**Weak spots we can use:**
- Per-user pricing: 10 users costs $299 to $399 a month at Jobber, Housecall Pro and Shopmonkey. Add these figures to the facts file before using them.
- Hidden prices.
- Intro prices that jump later.
- Annual lock-in.
- Add-on creep: Jobber charges +$99 for its AI receptionist.
- Paid onboarding.
- No local presence.
- The website costs extra, usually monthly.

## What buyers want and fear
**Why they buy:**
1. Everything in one place
2. Scheduling and dispatch
3. Never missing a call (Invoca: 27% of home-services calls go unanswered)
4. Easy to use
5. Getting paid on the spot
6. Automation
7. Reviews
8. Room to grow

Owners praise outcomes, not features (inference).

**Complaints and switching triggers (mentions in about 180 reviews):**
1. Support you can't reach (~39)
2. Price hikes (~26)
3. Contracts, auto-renew, or being billed after cancelling (~21)
4. Upsells and bait-and-switch (~19)
5. Bugs, and updates that move things around (~14)
6. Setup and migration pain (~7)
7. Bloat
8. Data lock-in (~5)
9. Payment holds (~4)
10. Number porting stuck for 1 to 3+ months
11. Mobile app problems
12. Per-user fees

**Questions they ask before buying:**
1. Contract and cancelling
2. QuickBooks
3. Trial
4. True total cost
5. Keeping their number
6. Who owns the data and how to export it
7. Which plan
8. Paying by text, and when payouts land
9. Importing customers and time to go live
10. Spanish
11. Whether it fits their industry
12. Techs seeing only their own jobs
13. Support
14. Reviews

**What "easy" means to them:**
- The crew uses it without training.
- It's built for the field (only 21% of techs say their tools feel that way, per ACHR).
- Updates don't move things around.
- They don't have to hire setup help.
- A real person walked them through it.

## Our feature inventory
Key: (a) in the facts file · (b) in the code but not in facts, needs Taylor's OK · (c) not present.

**(a) In the facts file:**
- CRM (contacts, pipeline, follow-up reminders)
- AI receptionist that answers and books (FP only)
- Missed-call text-back
- Online booking
- Dispatch board (FP)
- Customer hub
- Invoice by text, plus payment reminders
- Review requests (manual)
- Review replies (in-app only)
- On-my-way texts (FP)
- Estimates
- Card payments through **Helcim** (card + ACH; no rate anywhere in either repo)
- Website chatbot (**NOT BUILT**)
- Phone line $50/mo, port or new number (the porting promise is in the 11-21 spec; add it to facts)
- Custom layout or industry CRM at $99
- No setup fee, month to month
- $499 website with a form into the CRM

**(b) In the code, needs Taylor's OK before we advertise it:**

*Estimates and payments*
- Good/better/best estimates
- Typed-name e-signature approval, with time and IP saved
- "Customer signs now" on the tech's phone
- Deposits
- Approved lines flow onto the invoice
- Automatic estimate follow-ups
- Automatic overdue-invoice reminders
- Tips
- Google Pay in the customer hub (no Apple Pay found)
- Office-side split and partial payments
- Refunds
- Recurring invoices
- Wisetack financing (only if the customer connects it)

*Team and field*
- Techs see only their own jobs (enforced on the server)
- Appointment reminders
- Inspections
- Job photos
- Timesheets
- Price book
- Inventory
- Memberships
- Referrals

*Phone, data and mobile*
- Call recording, and call tracking by lead source
- Workflow builder
- CSV customer import (FP and TS)
- CSV export (TS only)
- LedgerPro bookkeeping feed
- Mobile app with push notifications (store listing not verified)

**(c) Not present, so don't claim it:**
- Tap to pay
- QuickBooks
- Spanish interface
- Offline mode
- GPS tracking
- Apple Pay
- Published card rates

## Recommended CRM page order, (a) items only
1. **Never miss a job:** the AI receptionist and missed-call text-back. Confirm the app's AI actually books.
2. **Get paid from the customer's phone:** invoice by text, card payments.
3. **Estimates they say yes to,** plus the customer hub.
4. **Everything in one place.**
5. **One schedule board,** plus on-my-way texts.
6. **Customers book themselves,** and the $499 site's form feeds the CRM.
7. **More 5-star reviews:** say "one tap", not automatic.
8. **Plain terms:** prices, no setup fee, month to month, the phone line, custom layout at the same price.
9. **Website chatbot:** hold, or label it "coming soon" (Taylor's call).

## Buyer questions with draft answers (FLAG means we need a fact from Taylor)
1. **Contract?** No, month to month.
2. **Setup fee?** None.
3. **Cost?** $99/mo for 1 to 10 users, $199/mo for 11 to 25, 26+ call for pricing.
4. **Per-user fees?** No, one price up to 10 users.
5. **Other costs?** The $50/mo phone line covers normal use, heavier use is billed. The website is $499 one time. FLAG: overage rate.
6. **Card fees?** FLAG: rate unknown. The processor is Helcim.
7. **Can I keep my number?** Yes, we move it over or set up a new one. Add this to facts.
8. **How long does setup take?** FLAG.
9. **Who sets it up?** FLAG.
10. **Is there a trial?** Tap Try the CRM; we call you, then send a demo.
11. **Does it work on my phone?** (b) Yes, in the browser, plus an app with push notifications.
12. **Do techs see only their own jobs?** (b) Yes.
13. **Can customers pay from their phone?** Yes, by text and card. Google Pay and tips are (b).
14. **When do I get paid?** FLAG: payout timing.
15. **Estimates?** Yes. Good/better/best options and typed-name approval are (b).
16. **Does it answer when I'm busy?** Yes, it answers and books, and missed calls get a text (FP).
17. **Does it get me reviews?** One tap sends your review link.
18. **Can I bring my customer list?** (b) Yes, by CSV upload.
19. **Who owns my data?** FLAG: no policy yet. TS can export; FP can't.
20. **QuickBooks?** No. (b) It feeds LedgerPro.
21. **Does it fit my industry?** Yes. We change the layout, or build a custom industry CRM at $99/mo.
22. **Website?** $499 one time: mobile-friendly custom design, built so Google can read it, a form into the CRM, and a logo if needed.
23. **Chatbot on my current site?** FLAG: not built yet.
24. **Who helps me?** Call or text (469) 833-3033, a local number. FLAG: support hours.
25. **Spanish?** Don't claim it.

## Showing "easy to use", honestly
1. **A 3-step "how it works"** (no competitor has one): tap Try the CRM → Taylor calls, demos it, and sets up your layout and line → text your first estimate or invoice. The setup details need Taylor's OK.
2. **A benefit-by-screen walkthrough** using the sample screens.
3. **"From the tech's phone" moments that really exist:** on my way, customer signs now, mark the rest OK, a one-tap text invoice.
4. **A day-one checklist:** number live, customers imported (b), review link set, first invoice texted.
5. **An "anti-trap" box beside the price:** no contract, no setup fee, no per-user fee up to 10 users, the same price every month, a one-time website.
6. **A local human promise:** a local number and "Taylor calls you". Add support hours to facts first.
7. **Plain outcome words, not AI hype.**

Don't copy unsourced growth percentages, "#1" badges or customer counts.


> **Update 2026-11-28:** the owner confirmed review requests can be set to send automatically when a job is finalized ("It can be set up so when the job is finalized it automatically sends a review request"). Copy now says they go out on their own, with one-tap manual sending also available. Earlier lines in this doc that limit it to "one tap" are superseded.
