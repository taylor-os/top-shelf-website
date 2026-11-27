# Real estate: screen brief (solo agent with a small team)

Sources followed: the real realtor kit (spec `top-shelf-crm/docs/superpowers/specs/2026-11-18-industry-kit-realtor-design.md`, `docs/realtor/broker-review.md`, the two daily-user reviews, renders 06-08) and the industry page (`industry-real-estate.html`). Where the kit and the earlier Elena Marsh mockups (01-05) disagree, the kit wins. The visual kit is the emerald Top Shelf look from BONES, not the real kit's dark-and-gold theme; the kit's structure, words and order are kept.

Sample day for every screen: **Tuesday, Oct 20, 2026**, about 7:15 AM on screen 1. All weekdays below are checked against the 2026 calendar.

---

## 1. Business and cast

**Marsh & Vale Realty**, Little Elm, TX (Denton County). One small office, but the work happens in the car and at kitchen tables. 3 people on the CRM, Signature plan, one phone line. Most business is downsizing retirees, couples moving near grandkids, and past-client referrals. Business line (940) 555-0100.

| Person | Role in the CRM | Who they are |
|---|---|---|
| Elena Marsh | Owner | Broker-owner. Lists homes and works with her own buyers. Checks Today on her phone at 7 AM and between showings; laptop at night for listings and offers. |
| Marcus Bell | Agent | Licensed buyer's agent on her team. Sees only his own contacts and deals (visibility switches off). |
| Dana Whitlock | Assistant | Transaction coordinator, part time. Lives in Deals: dates, documents, title company, lender. No Settings. |

Clients (all sample):

| Client | Phone | Situation on Oct 20 |
|---|---|---|
| Greg & Tina Sorensen | (940) 555-0151 | Sellers, 1180 Prairie Clover Ln, Aubrey. Under contract; option period ends tomorrow 5:00 PM; buyers asked for $3,200 in repairs. |
| Carol Mendez | (940) 555-0128 | Seller, 9032 Mesquite Hollow Dr, Little Elm. Price cut this morning $549,000 to $535,000. |
| Dan & Judy Ostrowski | (972) 555-0136 | Sellers, 4217 Larkspur Ridge Ct, Prosper. Active, 9 days on market. |
| Linda & Ray Whitfield | Linda (940) 555-0142, Ray (940) 555-0143 | Buyers, retirees selling their Plano home, want single story. Wish list changed today. |
| Diane Cho | (972) 555-0131 | Buyer. Offer out on 418 Lantana Ln, $455,000; seller's answer due 6:00 PM today. |
| Ade & Funmi Okafor | (940) 555-0158 | Buyers, under contract on 2209 Fieldstone Bend, Corinth; financing approval due tomorrow. |
| Grace Liu | (469) 555-0187 | Website lead, 13 hours waiting, asked about 9032 Mesquite Hollow. |
| Walter & June Pruett | (940) 555-0164 | New sellers. Called during Elena's 10:00 showing; the AI receptionist booked a listing appointment. |
| Evelyn Shaw | (940) 555-0119 | Seller lead, walkthrough at her home today 1:30 PM. |
| Marjorie Kline | (940) 555-0122 | Past client, 5-year home anniversary today at 2604 Pecan Creek Trl, Denton. |

Outside parties (sample): Cedar Fork Title, escrow officer Renee Albright (940) 555-0190; Copper Lane Mortgage, loan officer Nora Pruitt (972) 555-0145; buyer's agent Jason Kirby, Prairie Line Realty, (214) 555-0177. Buyers on 1180 Prairie Clover: Nathan & Keisha Doyle.

---

## 2. Roles and what they need first

**Owner (Elena)**
1. Contract deadlines in the next 48 hours, with the time (option period ends 5:00 PM).
2. Who to call today and why, phone number on the row, Call as the first button.
3. New leads waiting: how long, and what they asked about.
4. Today's showings and appointments with addresses.
5. Listings: is the new price and status on my website, is a seller update due.
Trust: the option period card is first, red, says "tomorrow 5:00 PM", and uses TREC words. Dismiss: a birthday above a contract deadline, or any job/invoice wording.

**Agent (Marcus, phone)**
1. Today's showings, address, showing instructions.
2. The buyer's pre-approval amount, good-through date and lender, without scrolling.
3. Wish list and matching homes, with over-budget homes flagged.
4. Log a call or showing feedback in three taps.
5. Only his own deadlines.
Trust: he can book a showing on another brokerage's listing. Dismiss: a CRM that only knows the office's own listings.

**Assistant / TC (Dana, desktop)**
1. Every team contract deadline, with the agent's name on each.
2. Which dates are confirmed and which are drafts ("Check against the contract").
3. Phone numbers for title, lender and the other agent on the deal page.
4. Which documents are in.
5. Weekend and holiday flags.
Trust: the timeline counts a TREC resale contract right (only earnest money and option fee roll; option ends 5:00 PM). Dismiss: dates that move on their own, or a "Done" button on an option period.

**Customer (buyers and sellers, many over 60)**
1. Plain status ("For sale", "Under contract, accepting backups"), price, beds, baths, photos.
2. Book a showing time without phone tag.
3. A real answer fast, day or night.
4. The agent's name and number, big.
5. A text confirming what was booked.
Trust: Elena's name on the reply within minutes. Dismiss: MLS jargon ("AOC", "Pending") on the public page, or a chatbot that will not say who it works for.

---

## 3. Words

| Bone | Real estate word on screen |
|---|---|
| Customer | Contact (types: Buyer, Seller, Both, Past client). "Client" in sentences. |
| Visit | Showing, Listing appointment, Walkthrough, Buyer consult |
| Deal (pipeline card) | Pipeline card on the Buyers or Sellers pipeline; once under contract it is a **Deal** (kit menu "Deals"); an offer before acceptance is "Offer out" |
| Work item | Contract timeline (steps), Listing (fields, photos, description, private showing notes), Documents |
| Money | Price, Sales price, Earnest money, Option fee, Seller contribution, Pre-approval. No invoices. |
| Conversation | Texts, Phone, Log call (Reached / Left voicemail / No answer) |
| Automation | Follow-up reminder, Showing reminder, On my way text, Weekly seller update, Review request after closing, Update MLS task |
| Team | Owner, Manager, Agent, Assistant |
| Customer view | Your website: listing page, Book a showing, Ask about this home, website chat |
| Website link | "On your website", "Hidden", "Website is live", Save & publish |

Pipeline stages (kit): Buyers: New lead, Contacted, Agreement signed, Showing, Offer out, Under contract, Closed, Lost. Sellers: New lead, Listing appointment, Listed, Under contract, Closed, Lost.

MLS status to website label (kit): Coming Soon to "Coming soon"; Active to "For sale"; Active Option Contract, Active Contingent, Active Kick Out to "Under contract, accepting backups"; Pending to "Pending"; Sold to "Sold"; Withdrawn, Expired, Cancelled, Temp Off Market to hidden.

**Nav, desktop sidebar (groups as in the kit)**
- Owner: *Every day*: Today, Listings, Contacts, Pipeline, Deals, Calendar, Website leads. *Talk*: Texts, Phone. *Setup*: Settings.
- Agent: same, no Settings.
- Assistant: Today, Listings, Contacts, Deals, Calendar, Texts, Phone. No Pipeline, Website leads or Settings. (Builder: confirm against the realtor role's hidden pages in the kit; if it differs, follow the kit.)

**Phone bottom tabs (owner and agent):** Today, Listings, Contacts, Pipeline, More.

**Must NOT appear:** job, work order, ticket, technician, tech, crew, dispatch, service call, estimate, quote, invoice, pay now, balance due, deposit (use earnest money), customer hub, inventory, vehicle, dealer, credit application, Social Security, patient, appointment type, escrow (use title company), contingency period or attorney review (not Texas; use option period), close of escrow, commission, GCI, split, lead score, hot/warm/cold lead, e-sign, DocuSign, Zillow or any portal name, "new MLS matches", "opened your email".

---

## 4. The 6 screens

Every image: bottom strip "Sample screens · sample data, not a real business". Every address carries "(sample)" at least once per screen (kit rule). Photos: exteriors and rooms with no yard signs, no brokerage logos, no readable house numbers.

### Screen 1. Owner home: Today (desktop 1440x900)
Role: Elena, Owner. Job: who to call today and why, with tomorrow's contract deadline first.

**Sidebar (240 px, emerald):** top: "Marsh & Vale Realty" / small "Realtor CRM". Nav groups as above; Today active; Website leads badge "1". Near the bottom, a card: green dot "Website is live" / "5 listings showing · published 7:42 AM". Footer: avatar EM, "Elena Marsh", "Owner".

**Header band (emerald):** search "Name, street or phone number" (left, 380 px). Right: outline "New contact", filled "Log a call". Below in the band: "Good morning, Elena" (serif) and "Tuesday, Oct 20 · 6 people to call · 3 appointments · 2 contract deadlines in the next 48 hours". Right side of band: pill toggle "Mine" (selected) / "Whole team".

**Count strip (4 small white tiles, one row):** "Offers out 1 · Diane Cho, answer by 6:00 PM" · "Under contract 2 · Option ends tomorrow" · "Active buyers 6 · 2 showing this week" · "Leads waiting 2 · longest 13 hrs".

**Main column (left, ~760 px)**

Block A, first thing on the page: heading in red "Contract deadlines (next 48 hours) (2)". Two cards, red outline, white fill:
1. Title "Option period ends: 1180 Prairie Clover Ln (sample)". Sub: "Your sellers, Greg & Tina Sorensen · Buyers asked for $3,200 in repairs". Right, red bold: "Tomorrow 5:00 PM". Buttons: filled "Call", outline "Log call", outline "Option passed, still under contract".
2. Title "Buyer's financing approval: 2209 Fieldstone Bend (sample)". Sub: "Your buyers, Ade & Funmi Okafor · Loan officer Nora Pruitt, (972) 555-0145". Right, red bold: "Tomorrow". Buttons: "Call", "Log call", "Done".

Block B: "Call today (6)". Rows: avatar initials, **Name · phone** (16 px, bold), one-line reason, a status chip, then buttons Call (filled) / Text / Log call / check.
1. Diane Cho · (972) 555-0131. "Offer on 418 Lantana Ln, $455,000. Seller's answer due 6:00 PM. Check with the listing agent at 3." Chip red "Due 6:00 PM today".
2. Greg & Tina Sorensen · (940) 555-0151. "Decide on the $3,200 repair request before the option period ends tomorrow at 5:00 PM." Chip red "Deadline tomorrow".
3. Grace Liu · (469) 555-0187. "Website lead, waiting 13 hours. Asked about 9032 Mesquite Hollow Dr. Has an agent: not asked yet." Chip blue "Website lead".
4. Walter & June Pruett · (940) 555-0164. "Called during your 10:00 showing yesterday. The AI receptionist booked a listing appointment Thu 10:00 AM. Confirm and ask for the HOA name." Chip green "Booked by phone". (Make this "yesterday" so it is consistent with screen 6 showing it as a past conversation; see screen 6 dates.)
5. Carol Mendez · (940) 555-0128. "New price $535,000 is on your website. Weekly update ready: 6 showings, 2 feedback notes." Chip "Seller update".
6. Evelyn Shaw · (940) 555-0119. "Wants to know what her home is worth. Walkthrough today 1:30 PM. Send the IABS first." Chip "Seller lead".

**Right column (~380 px)**

Card "Today's calendar":
- 10:00 AM · Showing · Linda & Ray Whitfield · 4217 Larkspur Ridge Ct, Prosper
- 1:30 PM · Listing walkthrough · Evelyn Shaw · 7804 Cottonwood Bend, Denton
- 4:00 PM · Showing · Linda & Ray Whitfield · 115 Sycamore Run, Denton · small tag "Other agent's listing"

Card "New leads (2)" with link "All leads":
- Grace Liu · amber pill "13 hrs, not answered" · "From the Mesquite Hollow page: 'Is the flex room big enough for a home office? Can we see it this weekend?'" · checkboxes "Has an agent" / "IABS sent" · buttons "Call" / "Mark replied".
- (214) 555-0172 · pill "Missed call, texted back" · "7:58 PM last night. Text-back sent. They replied: 'Is the Larkspur Ridge house still available?'" · button "Call".

Card "Next 10 days" (dot timeline): red dot "Wed 10/21 5:00 PM · Option period ends · 1180 Prairie Clover"; red dot "Wed 10/21 · Financing approval · 2209 Fieldstone Bend"; amber dot "Sat 10/24 · Survey delivered · 1180 Prairie Clover" with amber tag "Falls on Saturday: check whether it moves"; green dot "Fri 10/30 · Closing and funding · 2209 Fieldstone Bend · Cedar Fork Title".

Card at the bottom, "Past clients" (kit puts these last): "Home anniversary: Marjorie Kline, 5 years at 2604 Pecan Creek Trl" [Text] [Call] · "Birthday: Gloria Vance" [Text] · "Review: Bill & Joan Hartley left 5 stars on Google, Sun 10/18" [Reply].

### Screen 2. Signature: Listings with website status (desktop 1440x900)
Role: Elena, Owner. Job: every listing's MLS status, what the public website shows, and proof that this morning's price change is already live.

Sidebar as screen 1, Listings active. Header band: search, "New contact", "Log a call".

**Title row:** "Listings" (serif). Under it, grey 15 px: "Statuses match MLS. Each one shows a plain label on your website. Drafts stay private until you publish." Next line bold: "Website is live: 5 listings on your website · last published Tue Oct 20 at 7:42 AM" (underlined link with external icon). Right: outline "Import from MLS" (kit shows it; it opens "MLS sync needs your broker feed and is coming"), filled "+ Add listing".

**Success banner (green, full width):** check icon, "Saved and published. 9032 Mesquite Hollow Dr (sample) now shows $535,000 on your website. 'Update MLS: price change' is on your Today list." Buttons: outline "View on your website", filled "Send Carol this week's update".

**Tiles (3 across):** "Website views, 7 days · 642 · Most views: 9032 Mesquite Hollow Dr" · "Average days on market · 12 · Across your last 6 listings" · "Questions from your website, this week · 9 · 1 waiting for a reply".

**Tabs (pills):** All (5) · Coming soon (1) · Active (2) · Under contract (1) · Sold (1) · Off market (0) · Drafts (0). All selected.

**Table** columns: Listing | Price | MLS status | Beds · Baths · Sq ft | Days on market | On your website | Questions / Showings (30 days) | (Edit).

| Listing (thumb, address, area, seller, agent) | Price | MLS status (chip) + small website label | Details | Days on market | On your website | Q / S | |
|---|---|---|---|---|---|---|---|
| 9032 Mesquite Hollow Dr (sample), Little Elm. Seller: Carol Mendez. Elena Marsh. **Row lightly highlighted.** | $535,000, small "was $549,000 · changed today" | Active (green) / "For sale" | 3 · 2 · 2,212 | 16 days / "Listing agreement ends Mar 31, 2027" | green "For sale" / "Updated today 7:42 AM" | 5 / 6 | Edit |
| 4217 Larkspur Ridge Ct (sample), Prosper. Sellers: Dan & Judy Ostrowski. Elena Marsh. | $724,900 | Active / "For sale" | 3 · 2.5 · 2,846 | 9 days / "ends Apr 2, 2027" | "For sale" / "Updated Oct 16" | 3 / 4 | Edit |
| 1180 Prairie Clover Ln (sample), Aubrey. Sellers: Greg & Tina Sorensen. Elena Marsh. | $612,500 | Active Option Contract (amber) / "Option ends Wed 10/21, 5:00 PM" | 3 · 3 · 2,540 | 11 days / "ends Feb 15, 2027" | amber "Under contract, accepting backups" / "Updated Oct 14" | 7 / 9 | Edit |
| 2318 Bluestem Trl (sample), Denton. Sellers: Harold & Bev Lindqvist. Marcus Bell. | $389,000 | Coming Soon (blue) / "Coming soon" | 3 · 2 · 1,764 | Not on market yet / "ends May 8, 2027" | "Coming soon" / "Updated Oct 19" | 2 / 0 | Edit |
| 1412 Quarry Bend (sample), Denton. Sellers: Bill & Joan Hartley. Elena Marsh. | $402,000, small "sold Oct 16, 2026" | Sold (dark) / "Sold" | 4 · 2 · 2,105 | 21 days | "Sold" / "Price not shown" | 4 / 11 | Edit |

Below the table, one slim card: "Coming up: Price review Friday with Dan & Judy Ostrowski (4217 Larkspur Ridge). After any price change, Save & publish updates your website; MLS you update yourself."

### Screen 3. Transaction coordinator: the Deal page (desktop 1440x900)
Role: Dana Whitlock, Assistant. Job: run the TREC contract timeline on one deal and see every team deadline at a glance.

Sidebar: assistant nav (Today, Listings, Contacts, Deals active, Calendar, Texts, Phone). Footer "Dana Whitlock · Assistant". Header band: search, filled "Log a call".

**Team strip (top of canvas, slim, white):** "Team deadlines, next 48 hours:" then three chips, each with the agent name in 14 px dark text (not small grey): "1180 Prairie Clover · Option ends Wed 5:00 PM · Elena Marsh" (red) · "2209 Fieldstone Bend · Financing approval Wed · Elena Marsh" (red) · "5527 Kingfisher Ln · Earnest money and option fee Thu · Marcus Bell" (amber).

**Deal header:** breadcrumb "Deals / 1180 Prairie Clover Ln (sample)". Title "1180 Prairie Clover Ln (sample), Aubrey". Chips: "Seller side" · "Under contract" · "Agent: Elena Marsh". Right: three outline buttons, same weight: "Amendment signed", "Terminated", "Closed and funded".

**Red banner:** "Option period ends tomorrow, Wed Oct 21 at 5:00 PM. Buyers asked for $3,200 in repairs. Sellers have not answered." Buttons: filled "Call Greg & Tina", outline "Log call".

**Left column (~700 px): "Contract timeline"**, sub "TREC One to Four Family Resale Contract · Effective Wed Oct 14, 2026 · Dates confirmed by Elena Marsh, Oct 14". Rows: date | step | note | who | action.
1. Check · Fri 10/16 · Earnest money and option fee received by title · "Due Mon 10/19 (day 3 fell on Saturday, so it moved) · Done Fri 10/16" · Dana.
2. Check · Fri 10/16 · HOA information delivered · "Done Fri 10/16" · Dana.
3. Check · Mon 10/19 · Buyer's HOA review ends · "3 days from delivery · Passed" · Elena.
4. **Red** · Wed 10/21, 5:00 PM · Option period ends · red pill "Tomorrow" · Elena · three buttons instead of a checkbox: "Option passed, still under contract" / "Buyer terminated" / "Amendment signed".
5. **Amber** · Sat 10/24 · Survey delivered · "Existing survey + T-47, seller provides" + amber tag "Falls on Saturday: check whether it moves" · Dana · checkbox.
6. Hollow · Tue 11/3 · Title commitment · grey "Expected, not a contract deadline" · Cedar Fork Title.
7. Hollow · (no date) · Title objections due · grey "Its date shows once the title commitment and survey are checked off."
8. Dot · Wed 11/4 · Buyer's financing approval · "21 days · Conventional" · Elena.
9. Hollow · (no date) · Appraisal · grey "No appraisal days entered, so not a contract deadline."
10. Hollow · Thu 11/12 · Final walkthrough · grey "Expected, not a contract deadline".
11. Dot · Fri 11/13 · Closing and funding · "Cedar Fork Title" · Elena.

**Right column (~380 px)**
- Card "Terms": Sales price $600,000 · Earnest money $6,000 · Option fee $300 for 7 days · Financing Conventional · Seller contribution $4,000 · Survey Existing survey + T-47, seller provides · Possession At closing and funding · Closing Fri Nov 13. Link "Edit terms".
- Card "People" (each with a phone icon button): Sellers Greg & Tina Sorensen (940) 555-0151 · Buyers Nathan & Keisha Doyle · Buyer's agent Jason Kirby, Prairie Line Realty (sample), (214) 555-0177 · Title Cedar Fork Title (sample), Renee Albright, (940) 555-0190 · Lender Copper Lane Mortgage (sample), Nora Pruitt, (972) 555-0145.
- Card "Documents" with "+ Upload": Signed contract · Oct 14 · Seller's disclosure · Oct 9 · HOA resale certificate · Oct 16 · Other: "Repair request from buyer's agent" · Oct 19.
- Card "Notes": "Elena · Mon 4:10 PM: Sorensens leaning toward a $2,000 credit instead of repairs." · "Dana · Fri 11:02 AM: Cedar Fork confirmed earnest money and option fee received."

### Screen 4. On the go: buyer page between showings (phone 390x844)
Role: Elena on her phone at 12:30 PM, after the 10:00 showing, before the 4:00. Job: see the buyer's money facts, log what changed on the wish list, and get ready for the next showing.

**Header (emerald band):** back "Contacts". "Linda & Ray Whitfield" (serif, 24 px). Chips: "Buyer" · "Selling their Plano home". Big button row (48 px tall): filled "Call Linda" with small caret "or Ray", outline "Text", outline "Log call".

**Key facts card (white, 16 px text):** "Pre-approved $650,000 · Conventional · good through Jan 24, 2027" / "Nora Pruitt, Copper Lane Mortgage · (972) 555-0145" (tap to call) / "Buyer agreement signed Sep 30 · ends Mar 31, 2027".

**Card "Showing today":**
- "4:00 PM · 115 Sycamore Run, Denton (sample)" · tag "Other agent's listing · MLS # 20455188" · buttons "Text: on my way" (filled) and "Add feedback".
- Divider, grey row: "10:00 AM · 4217 Larkspur Ridge Ct · Feedback saved: 'Loved the patio. Stairs to the bonus room are a worry for Ray's knees.'"

**Card "Wish list"**, right link "Edit", sub "Changed today 12:21 PM":
- "$550,000 to $650,000 · 3+ beds · 2+ baths · single story"
- "Areas: Denton, Aubrey, Little Elm · Move by March"
- Must have (chips): Single story · Study or office · Covered patio · Fenced yard (dog) · Walk-in shower
- Deal-breakers (red-outline chips): Stairs · Pool to maintain · Backs to a busy road · **HOA over $150 a month** (with a small "New today" label)

**Card "Matching homes (1)", peeking above the tab bar:** thumb + "9032 Mesquite Hollow Dr · $535,000 · 3 bd · 2 ba" · green "Matches 5 of 5 must-haves" · tag "Your listing: intermediary".

**Bottom tabs:** Today, Listings, Contacts (active), Pipeline, More.

### Screen 5. Customer view: Elena's listing page on her website (phone 390x844)
Role: a buyer browsing at night (styled as Elena's site, not the CRM). Job: see the home in plain words, book a showing time, or ask a question.

Style: Elena's own site colors (porcelain #FBFAF7 background, pine #2E5C4A accent, serif headings). No emerald app chrome, no CRM nav.

- Browser URL bar: "marshandvale.example/homes/9032-mesquite-hollow".
- Site bar: house mark + "Elena Marsh" / small "Marsh & Vale Realty"; right: pine pill "Call (940) 555-0100", menu icon.
- Hero photo (single-story brick exterior, no sign), corner counter "1 / 24".
- Label chip "For sale". Price "$535,000" (serif, large). "9032 Mesquite Hollow Dr, Little Elm, TX 75068 (sample)".
- Facts row: "3 beds · 2 baths · 2,212 sq ft · Single story · Built 2016". Second row: "Little Elm ISD · HOA $95 a month".
- Card "Book a showing": "Pick a time. Elena confirms by text." Day chips: Wed 10/21 · **Thu 10/22** (selected) · Sat 10/24. Time chips: 10:00 AM · **1:30 PM** (selected) · 4:00 PM. Fields: Name, Mobile number. Question "Are you working with an agent?" Yes / No. Full-width pine button "Request Thu 1:30 PM".
- Text link below: "Or ask a question about this home".
- Floating chat bubble bottom right, open to one line: "Hi, I'm Elena's website assistant. Ask me anything about this home."
- Footer line (small but readable, 13 px): "Information About Brokerage Services · TREC Consumer Protection Notice · Broker license # 0000000 (sample)".

### Screen 6. Call and text moment: the AI receptionist booked a listing appointment (phone 390x844)
Role: Elena, Texts tab, on the evening of Mon Oct 19 (so screen 1's "called yesterday" holds). Job: see what the AI receptionist did while she was showing a home, and pick up the thread herself.

- Header: back "Texts". "Walter & June Pruett" · "(940) 555-0164". Right: Call icon button. Under it, chip row: "New contact, from a call" · "Pipeline: Sellers · Listing appointment".
- **Card "AI receptionist answered" (top, white, pine left border):** "Mon 10:14 AM · 3 min · you were at a showing". Summary (16 px): "Wants to sell his home on Briar Glen Ct in Aubrey and move closer to the grandkids in Frisco. 4 beds, built 2004. Asked what it might sell for." Bold line: "Booked: Listing appointment, Thu Oct 22, 10:00 AM, at the home." Buttons: "Read transcript", "Log call".
- Thread:
  - Out, 10:17 AM, small label "Sent by the AI receptionist": "Hi Walter, this is Elena Marsh with Marsh & Vale Realty. Thanks for calling. You're set for Thursday, Oct 22 at 10:00 AM at your home. I'll bring recent sales from your street. Reply here or call (940) 555-0100 anytime."
  - In, 10:31 AM: "Thank you. June wants to know if we need to clean out the garage before you come."
  - Out, 12:05 PM (Elena): "Not at all, Walter. I just want to see the house the way you live in it. If your survey and HOA name are handy, set them out. See you Thursday."
  - In, 12:09 PM: "Will do. It's the Briar Glen Owners Association."
- Grey system line: "Reminder text goes out Wed 6:00 PM".
- Composer: "Text Walter..." with send button. Bottom tabs: Today, Listings, Contacts, Pipeline, More (none active, or More active since Texts lives under More).

---

## 5. How it uses the bones

| Screen | Shared records it reads |
|---|---|
| 1 Owner Today | Deal (timeline steps, offer respond-by), Customer (birthdays, anniversaries, pre-approval), Visit (showings, walkthrough), Conversation (call log, missed-call text-back), Website link (leads), Automation (follow-ups, Update MLS, review request), Team (Mine / Whole team) |
| 2 Listings | Deal (seller-side card), Work item (listing fields, photos, status), Website link (publish, views, questions), Visit (showing counts), Automation (Update MLS task, weekly seller update), Customer (seller) |
| 3 Deal page | Deal, Work item (timeline steps, documents), Customer (parties), Money (price, earnest money, option fee, contribution as figures only), Team (step owners, agent names), Conversation (notes, calls) |
| 4 Buyer page | Customer (profile fields, wish list criteria), Money (pre-approval), Visit (showings, feedback), Deal (matching listings), Automation (on my way text), Conversation |
| 5 Website listing | Website link (published listing), Customer view (booking request, chat), Visit (requested slot), Customer (new contact) |
| 6 AI call + texts | Conversation (AI receptionist call, texts), Customer, Visit (listing appointment), Deal (Sellers pipeline card), Automation (reminder) |

Note: the kit's listings, wish lists and deal timelines are shared blocks; here they map onto Work item (listing, timeline) attached to a Deal, and Customer (wish list). No new record type.

---

## 6. Watch-outs

- **Texas words exactly as the kit has them:** "Option period ends" at 5:00 PM; "Option passed, still under contract" (never "Done" on the option period); "Expected, not a contract deadline"; "Falls on Saturday: check whether it moves"; "Your listing: intermediary"; IABS; "TREC One to Four Family Resale Contract". Only earnest money and option fee roll for weekends; nothing else moves on its own. The kit's rules are pending a broker's review, so don't add new Texas claims beyond them.
- **Deadline order is the trust test.** The red 48-hour block is always first on Today; past-client items always last. Say "Tomorrow" or "Today", not just a date. Agent names on team items in 14 px dark text, not small grey.
- **Fair housing:** wish lists, notes and showing feedback talk about the house only. No "family neighborhood", "safe area", "good schools for the kids", church, age or ethnicity words. School district as a plain listing field is fine.
- **Intermediary:** a showing note from Elena's own buyer on Elena's own listing is not shown to the seller by default.
- **Don't show what the kit doesn't do:** no live MLS sync, no "new MLS matches", no email-open tracking (mockup 04's "Opened the Larkspur listing you emailed 3 times" must not come back), no e-sign, no commission math, no invoices, pay links or customer hub. Money appears only as contract figures and pre-approval.
- **Sample data:** every address "(sample)"; no real brokerages, title companies or lenders; license number "0000000 (sample)"; .example domain; 555-01xx numbers. Never "Sarah Laos" or "Ready Real Estate". Use different names from the kit's sample business (Pecan Hollow Realty, Lauren Pike, Tessa Nguyen) so the two don't mix.
- **Tone:** few late items, no alarming counts. One deal under pressure (the option period) is the drama; everything else is on track.
- **Readability for older clients and car use:** 16 px minimum body on phone, Call always the first, filled button, phone numbers next to names.
- **Brand check for Taylor:** the existing website demo at `websites/elena-marsh-realty` says "Elena Marsh Real Estate" in "Cedar Ridge". This brief uses "Marsh & Vale Realty" in Little Elm per the brief I was given. Screen 5 borrows that demo's colors; Taylor should pick one name before the screens ship.
