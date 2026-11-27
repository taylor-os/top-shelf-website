# Auto detailing: screen brief

Source of truth: the Detail Suite in the real Top Shelf CRM (`app/Support/DetailSuite.php`, `DetailDemo.php`, `DetailMenu::SAMPLE`, `ShopWords::DETAIL`, `resources/js/lib/detail-process.json`, `pages/location/repairs/*`, `components/calendars/detail-bookings.tsx`, `pages/book-detail.tsx`). Every label in quotes below is a real app string unless marked (new).

One story runs through all six screens: Saturday, Dec 6, one shop, two bays. Screens 1 to 4 are at about 10:45 AM, screen 5 at 10:40 AM, screen 6 at 2:25 PM.

## 1. Business and cast

**Kestrel Lane Detail Co.**, Rowlett, TX. One shop, 2 bays (the booking page runs "2 cars at a time"), open daily 8:00 AM to 5:00 PM. 4 people. Shop phone (972) 555-0172. Drop-off detailing; no mobile van on these screens (mobile routes are not built, see Watch-outs).

| Person | Role in the app | Notes |
|---|---|---|
| Dee Hargrove | Owner | Prices the big jobs (coatings, paint correction) herself |
| Paloma Ruiz | Front desk | Phones, check-in, deposits, pickups |
| Trey Ashford | Detailer | Full details, interiors |
| Minh Tran | Detailer | Paint correction, coatings |

Customers (all fictional, 555 numbers, size per the real list: Car / SUV / Truck or van):

| # | Customer | Car | Size | Today |
|---|---|---|---|---|
| 1 | Whitney Calder, (972) 555-0131 | 2022 Chevrolet Tahoe, Black, Plate NHT-4182 | SUV | WO 2047, Full detail, pet hair found at check-in |
| 2 | Jordan Pike, (972) 555-0164 | 2020 Ford F-150, Silver, Plate JPX-2020 | Truck or van | WO 2043, done Friday, balance $250.00 |
| 3 | Sam Whitfield, (214) 555-0125 | 2024 Tesla Model Y, White, Plate SWM-2401 | SUV | WO 2046, wash and wax, paid by link with a tip; on a maintenance wash every 2 weeks |
| 4 | Ana Lucia Ferreira, (214) 555-0108 | 2023 Kia Telluride, White, Plate AFR-2390 | SUV | WO 2044, ceramic coating, waiting on the coating kit |
| 5 | Lauren Beck, (972) 555-0186 | 2017 Honda Civic, Red, Plate LBK-1717 | Car | WO 2045, headlight restore, in Quality check |
| 6 | Derek Hollis, (214) 555-0161 | 2018 BMW 340i, Blue, Plate DHX-1840 | Car | WO 2048, paint correction (custom hourly) |
| 7 | Raymond Ochoa, (972) 555-0156 | 2019 Toyota 4Runner, Green, Plate RCX-6612 | SUV | WO 2049, booked online, checked in 10:30 |
| 8 | Keisha Monroe, (214) 555-0177 | 2021 Honda Odyssey, Gray | Truck or van | Booked online for 11:00 AM |
| 9 | Erin Matsuda, (469) 555-0148 | 2021 Subaru Forester, Blue | SUV | Booking online right now for next Saturday |
| 10 | Gabriel Soto, (469) 555-0119 | 2016 Ram 1500, Black | Truck or van | Didn't show Friday 2:00 PM, deposit paid |

Prices (the real sample menu, `DetailMenu::SAMPLE`), deposit 25% of the booking:
- Packages: Full detail Car $180 / SUV $220 / Truck or van $250 (3 h). Interior shampoo $120 (2 h). Exterior wash and wax $90 (1.5 h). Ceramic coating, 3-year $900 (8 h).
- Add-ons (one price): Pet hair removal $40 (30 min). Headlight restore $60 (1 h). Engine bay $50 (1 h).
- Custom hourly (not on the booking page): Paint correction (1-step), $75 an hour, 4 h = $300.

## 2. Roles and what they need first

**Owner (Dee), desktop, before the first car rolls in and again mid-morning**
1. Money: deposits held for today, what's owed on cars ready for pickup, what came in today, tips.
2. The bays: what's in each column and whether every "Ready by" promise is still safe.
3. Upsells waiting on a customer's OK, with the dollars waiting.
4. No-shows, and whether the deposit was kept.
5. What the phone did while closed (AI receptionist bookings, missed calls texted back), new reviews, who is due to rebook.
- Trusts it when: the deposit math is right to the cent and Check in carries the booked package and price onto the work order. Dismisses it when: she sees car-lot or repair-shop words (stock number, recon, RO, technician) or a generic "jobs and dispatch" home.

**Front desk (Paloma), desktop at the counter, phone ringing**
1. Who arrives next, which package, which size, deposit paid or not.
2. One tap to Check in.
3. Cars ready to hand back: who to text, who still owes.
4. The no-show call: mark it, keep the deposit, without a fight with the screen.
5. Unread texts and missed calls.
- Trusts it when: no retyping between the booking and the work order. Dismisses it when: a deposit can be refunded or kept by one stray tap (the real app asks first).

**Detailer (Trey), phone in one gloved hand, car door open**
1. My next car and what's on it (package, add-ons).
2. Start / Stop the clock with a thumb.
3. Which jobs the customer has OK'd (can I do the pet hair yet?).
4. Snap check-in and finished photos fast.
5. My hours today.
- Trusts it when: big buttons, nothing to type, no prices or customer phone numbers (the real detailer view hides both). Dismisses it when: it looks like an office app.

**Car owner (customer), phone, evenings**
1. The price for my vehicle size before I book.
2. How long it takes and when I can drop off.
3. How much the deposit is.
4. A text that I'm booked, with a link to see it again.
5. Approve an add-on by text, pay by link, add a tip.
- Trusts it when: the price is right there. Dismisses it when: "call for a quote".

## 3. Words

| Bone | Detailing word on screen |
|---|---|
| Customer | Customer |
| Visit | Booking (on Calendars); "Ready by" on the work order |
| Deal | Estimate: "Send for approval", "Waiting on Whitney's OK" (a detail shop has no pipeline) |
| Work item | Work order, "WO 2047", its jobs (packages and add-ons) |
| Money | Deposit, Bill, Balance, Pay link, Tip, Receipt, Refund it / Keep it |
| Conversation | Texts, Phone, Inbox; AI receptionist |
| Automation | Reminders, review requests, rebook reminders, "Text it's ready" |
| Team | Owner, Front desk, Detailer |

Shop board columns (real, in order): "Waiting", "In progress", "Waiting on parts", "Quality check", "Done" (Done splits into "Ready for pickup" and "Picked up"). Phone chips: Waiting, In progress, Parts, QC, Done.

**Nav, owner (desktop sidebar, group labels in small caps):**
EVERY DAY: Home, Customers, Tasks · TALK: Texts, Phone, Inbox · OFFICE: Work orders, Calendars · GROW: Reputation, Automations · MONEY: Payments · SETUP: Settings, Help.

**Nav, front desk:** EVERY DAY: Home, Customers, Tasks · TALK: Texts, Phone, Inbox · OFFICE: Work orders, Calendars · GROW: Reputation · MONEY: Payments · SETUP: Help.

**Nav, detailer (phone bottom tabs):** Home, Work orders, Tasks, Account. (Real: a detailer opens only Home, Tasks and Work orders; Work orders sits right after Home.)

**Must NOT appear:** repair order, RO, technician, service advisor, stock number, recon, Rush, inventory, lot, deal, pipeline, opportunity, lead stage, financing, title work, sales, mechanic, diagnosis, "Whole store", labor (price-list jobs read "Price"), job site, dispatch, crew, service call, truck roll, patient, member, class, session, table, reservation, matter, listing, showing, "call for a quote", "Marketing", "Subscriptions".

## 4. The 6 screens

Every image: emerald kit, light canvas, white cards, and the bottom strip "Sample screens · sample data, not a real business". Staff screens show the business switcher "Kestrel Lane Detail Co." at the top of the sidebar.

### Screen 1. Owner Home (Dee), desktop 1440x900
Job: everything Dee checks in one pass: money, the bays, upsells waiting, today's bookings, the phone, rebooks.

- **Sidebar (emerald):** switcher "Kestrel Lane Detail Co. · Dee Hargrove · Owner"; owner nav as above, Home active; badges: Tasks 2, Texts 3, Phone 1 (missed). User chip at the bottom "DH Dee Hargrove".
- **Header band (emerald):** "Home"; search box "Search customers or WO numbers".
- **Title row:** "Kestrel Lane Detail Co." with small grey line "Saturday, Dec 6 · 10:45 AM"; right link "How your shop runs".
- **Next step card (full width, outlined):** eyebrow "NEXT STEP", text "1 work order waits on the customer's OK", button "Open the board".
- **Money strip (4 small tiles, full width) (new layout, real figures):** "Deposits held for today $62.50" (Keisha, 11:00) · "In today $105.00" (sub: "incl. tips $15.00") · "Owed $250.00" (sub: "1 car ready") · "Did they come? 1" (sub: "Gabriel Soto, Fri · $62.50 deposit paid", amber).
- **Left column (60%), section label "SERVICE TODAY":**
  - Card "Ready for pickup · 2" (arrow right):
    - "Jordan Pike" / "2020 Ford F-150 · WO 2043" / "Balance $250.00" (accent) / "Last text Fri 4:52 PM" · buttons Call, Text.
    - "Sam Whitfield" / "2024 Tesla Model Y · WO 2046" / "Paid" / "Texted 9:34 AM" · buttons Call, Text.
  - Card "Waiting on the customer's OK · 1":
    - "Whitney Calder" / "2022 Chevrolet Tahoe · WO 2047" / "sent 4 min ago · $40.00 waiting".
  - Card "Bookings today" (link "Calendars →"):
    - "11:00 AM · Keisha Monroe · 2021 Honda Odyssey" / "Full detail · $250.00 · Deposit $62.50 paid".
    - Amber sub-row "Did they come? Gabriel Soto · 2016 Ram 1500 · Fri, Dec 5 at 2:00 PM · Deposit $62.50 paid" with link "Open Calendars".
- **Right column (40%):**
  - Figure tiles 2x2 (real): "1 Waiting to start" · "2 In progress" · "1 Waiting on parts" · "1 Quality check".
  - By-detailer list (real): "Trey Ashford · 2 open work orders · 4 jobs"; "Minh Tran · 2 open work orders · 3 jobs".
  - Card "Phone since you closed" (new layout): "AI receptionist answered 4 calls · 2 booked online · 1 missed call texted back" and one row "Ceramic coating price on a 2024 Silverado · asked for Dee · callback task due 12:00 PM".
  - Card "Rebook reminders" (new layout, Automations): "Sam Whitfield · Model Y · Maintenance wash every 2 weeks · next reminder Fri, Dec 19"; "Jordan Pike · F-150 · Full detail every 4 months · reminder after pickup". Footer "6 more due this month".
  - Card "Reputation": "★★★★★ Keisha M.: Third row looked brand new after the kids got to it." button "Reply"; line "Review requests sent this week: 9".

### Screen 2 (signature). The work order, desktop 1440x900, owner view
Job: one car's whole visit on one page: the booked package at its size price, the deposit already on it, the add-on waiting on a text OK, check-in photos, the clock.

- **Sidebar:** owner nav, "Work orders" active.
- **Header band:** breadcrumb "Home › Work orders › WO 2047".
- **Title row:** "WO 2047" + status pill "In progress" + grey "Ready by Today 2:30 PM". Buttons right: "Move to…" (outline), "Send for approval" (outline, with grey hint under it "Sent 10:41 AM by text").
- **Left column (65%):**
  - **Car and customer card:** bold "2022 Chevrolet Tahoe · Black" / "Customer car · Plate NHT-4182 · 41,260 mi in" / field "Car size" with value "SUV" / "Whitney Calder · (972) 555-0131" / line "Booked online · Sat, Dec 6, 8:00 AM · Deposit $55.00 paid" / concern in quotes: "Full detail. Two labs ride in the back."
  - **Jobs card** (heading "Jobs", button "Add a job"):
    - Row 1: "Full detail" · grey "Priced from your list · SUV" · "Price $220.00" · "Trey Ashford" · chip "Approved" · clock "Clocked 0.2 h of 3 h" with a small green running dot.
    - Row 2: "Pet hair removal" · grey "Add-on" · "Price $40.00" · "Trey Ashford" · chip (sky) "Waiting on the customer" · grey "Sent 10:41 AM by text" · button "Record a decision".
  - **Photos card** (heading "Photos · 6", button "Add photo"): a 3x2 grid of real-looking car photos, each with a caption under it: "Check-in · front", "Check-in · driver side", "Check-in · rear bumper scuff, was there", "Check-in · 2nd row", "Check-in · 3rd row", "Check-in · cargo, dog hair".
  - **Notes card:** "Trey Ashford · 10:38 AM: Hair packed into the cargo carpet and the 3rd row. Needs the pet hair add-on." Grey footnote "Detailers see this. No names or phone numbers." (real wording with the shop's word).
- **Right column (35%):**
  - **Estimate card:** rows "Full detail · Approved · $220.00", "Pet hair removal · Waiting on OK · $40.00", "Deposit paid online · −$55.00", divider, bold "Due at pickup if approved $205.00". Grey line "The customer can add a tip on the pay link." Two disabled buttons "Text it's ready" and "Take payment" with grey hint "When the work order is Done".
  - **Customer card:** "Whitney Calder", "4th work order · last: Full detail, Sep 6", tag chips "2 dogs" and "Full detail every 3 months", task row "Call to rebook next full detail · due Mar 6", buttons Text, Call.
  - **History card:** "Wed 7:46 PM · Booked online, deposit $55.00 paid" · "8:05 AM · Checked in by Paloma Ruiz" · "10:35 AM · Trey Ashford started Full detail" · "10:41 AM · Paloma Ruiz sent the estimate by text".

### Screen 3. Front desk Calendars (Paloma), desktop 1440x900
Job: the counter: the no-show decision, who's coming, held deposits, cars to hand back.

- **Sidebar:** switcher "Kestrel Lane Detail Co. · Paloma Ruiz · Front desk"; front desk nav, "Calendars" active; badges Texts 3, Phone 1.
- **Header band:** breadcrumb "Home › Calendars".
- **Title:** "Calendars" / grey "Booking pages your customers use to book with you."
- **Left column (62%):**
  - **"Needs you" card (amber border, amber tint):** row "Gabriel Soto · 2016 Ram 1500" / grey "Did they come? Fri, Dec 5 at 2:00 PM. Deposit $62.50 paid." Buttons "Check in", "No-show", "Cancel". Under it, the confirm step open (grey panel): "Mark as a no-show? The $62.50 deposit is kept." buttons "Yes, no-show" (red), "Never mind".
  - **"Bookings" card,** exactly 2 rows, each with buttons on the right:
    - "Keisha Monroe · 2021 Honda Odyssey" / grey "Today · 11:00 AM" / "Full detail · $250.00" / grey "Deposit $62.50 paid" · buttons "Check in" (primary), "No-show", "Cancel".
    - "Erin Matsuda · 2021 Subaru Forester" / grey "Sat, Dec 13 · 9:00 AM · Waiting on the deposit" / "Full detail, Pet hair removal · $260.00" / grey "Deposit $65.00 due" · button "Cancel" only.
- **Right column (38%):**
  - **"Booking pages" card:** calendar icon, "Detail bookings", chip "Active", grey "2 cars at a time · Open daily 8:00 AM to 5:00 PM · 25% deposit", link row "Copy booking link".
  - **"Ready for pickup" card:** "Jordan Pike · 2020 Ford F-150 · WO 2043 · Balance $250.00" buttons "Text it's ready", "Take payment"; "Sam Whitfield · 2024 Tesla Model Y · WO 2046 · Paid" button "Picked up".
  - **"Phone" card:** "AI receptionist booked Raymond Ochoa for 10:30 AM (checked in)" · "Missed call 9:12 AM, (469) 555-0130, texted back" · "3 unread texts" link "Open Texts".

### Screen 4. Detailer My jobs (Trey), phone 390x844
Job: the detailer's whole day under one thumb: clock, which jobs are OK'd, photos.

- **Top bar:** menu icon, "Work orders", search icon.
- **Title row:** "My jobs" + link "My hours ›".
- **Summary link:** "Today: 2 done · 2.5 h booked · 2.4 h clocked ⌄".
- **Section "Ready",** one car card:
  - Header: "2022 Chevrolet Tahoe · Black · Customer car · Plate NHT-4182 · VIN …418823".
  - Job 1: "Full detail ›" / grey "WO 2047 · In progress · Booked 3 h · Clocked 0.2 h" / grey "Ready by Today 2:30 PM". Full-width red-outline button "Stop 0:11:32" (counting). Full-width "Done". Half buttons "Add photo", "Notes (1)". Photo strip of 3 thumbnails: "Check-in · cargo, dog hair", "Check-in · 3rd row", "Check-in · rear bumper scuff, was there".
  - Job 2 at 60% opacity: "Pet hair removal ›" / grey "WO 2047 · In progress · Booked 0.5 h · Clocked 0 h". Full-width disabled "Start" with grey reason under it "Waiting on the customer's OK. Don't start yet." Disabled "Done".
- **Section "Finished today":** "2017 Honda Civic · Red · Customer car · Plate LBK-1717" with two lines "Headlight restore · Booked 1 h · Clocked 0.9 h" and "Exterior wash and wax · Booked 1.5 h · Clocked 1.5 h", and a before/after pair of thumbnails side by side: "Check-in · left headlight" (yellowed) and "Finished · left headlight" (clear).
- **Bottom tabs:** Home, Work orders (active), Tasks, Account.
- No dollar amounts and no customer names or phone numbers anywhere on this screen.

### Screen 5. Customer booking page (Erin), phone 390x844
Job: price for her size before she books, a time, the deposit, done in a minute.

Styled as the shop's own page: "Kestrel Lane Detail Co." in a modest deep-blue accent (suggest #1F4E79), white background, no Top Shelf logo or emerald.
- **Header:** small "Kestrel Lane Detail Co." / big "Book your detail" / grey "You'll see the price before you book."
- **Done steps collapsed (each a row with a check and "Change"):** "1 · Your vehicle: SUV" · "2 · Package: Full detail · $220".
- **Step 3 "Add-ons" (open):** three check rows: "Pet hair removal +$40" (checked), "Headlight restore +$60", "Engine bay +$50".
- **Step 4 "Pick a day and time" (open):** day chips "Thu 11", "Fri 12", "Sat 13" (selected), "Sun 14"; grey "Takes about 3 h 30 min"; time chips "8:00 AM", "9:00 AM" (selected), "10:30 AM", "1:00 PM".
- **Step 5 "Your details" (collapsed, next):** "First name, phone, your car".
- **Sticky bottom card:** "What you booked" / "Full detail, Pet hair removal" / "Sat, Dec 13 · 9:00 AM" / "Total $260.00" / bold "Deposit due now $65.00" / grey "Next, we may ask for a deposit to hold your time." / full-width button "Continue".
- **Footer line:** "Kestrel Lane Detail Co. · Rowlett, TX · (972) 555-0172".

### Screen 6. The text thread (front desk view of Whitney), phone 390x844
Job: the whole job told in texts: AI receptionist books it, deposit confirmed, add-on approved by text, ready with a pay link.

- **Top bar:** back arrow, "Whitney Calder", grey "2022 Chevrolet Tahoe · (972) 555-0131", call icon.
- **Thread, oldest at top (time stamps between groups):**
  1. System card (emerald outline, mic icon) "AI receptionist · Wed 7:42 PM · 3 min call": "Wants a full detail on a 2022 Tahoe, Saturday morning, drop-off. Two dogs ride in the back. Sent the booking link for Sat 8:00 AM."
  2. Outgoing (shop), Wed 7:46 PM: "Kestrel Lane Detail Co.: You're booked for Full detail on Sat, Dec 6 at 8:00 am. We got your $55.00 deposit. Your booking: kestrellanedetail.com/b/7Hq2"
  3. Outgoing (Paloma), Sat 10:40 AM: "Morning Whitney, Trey found a lot of dog hair packed into the cargo carpet and 3rd row. Pet hair removal is $40. Sending it over now."
  4. Outgoing, 10:41 AM: "Hi Whitney, your estimate for the 2022 Chevrolet Tahoe at Kestrel Lane Detail Co. is ready. Tap to approve or decline each job: kestrellanedetail.com/e/R4m9 - Paloma"
  5. Incoming, 10:50 AM: "Yes please do it. They shed like crazy lol"
  6. Event chip (centered, green): "Whitney approved Pet hair removal · $40.00 · 10:51 AM"
  7. Outgoing, 2:18 PM: "Hi Whitney, your 2022 Chevrolet Tahoe is ready at Kestrel Lane Detail Co. Amount due: $205.00. You can pay at kestrellanedetail.com/p/W2k8 or at the counter. - Paloma"
  8. Incoming, 2:21 PM: "On my way, 15 min"
- **Above the composer:** chip "AI draft: See you soon, it's parked out front." with "Use" button.
- **Composer:** "Text Whitney…" and send icon. Bottom tabs: Home, Texts (active), Work orders, Calendars, More.

## 5. How it uses the bones

| Screen | Shared records read |
|---|---|
| 1 Owner Home | Work item (WO status counts), Visit (today's bookings, no-show), Money (deposits, owed, in today, tips), Deal (estimates waiting on OK), Conversation (AI calls, missed-call text-back), Automation (rebook reminders, review requests), Team (by detailer), Customer |
| 2 Work order | Work item (jobs, photos, notes, clock), Customer, Visit (the booking it came from), Deal (estimate approval), Money (deposit, estimate total), Team, Automation (rebook task) |
| 3 Front desk Calendars | Visit (bookings, no-show, check-in), Money (deposits held, kept, due), Customer, Work item (check-in opens the WO; ready for pickup), Conversation (phone card), Website link (booking page) |
| 4 Detailer My jobs | Work item (jobs, clock, photos), Team |
| 5 Booking page | Customer view, Website link, Visit, Money (deposit) |
| 6 Text thread | Conversation, Automation (booking and ready texts), Deal (estimate link), Money (pay link), Customer |

## 6. Watch-outs

- **Keep the real kit's rules.** The detailer's view (screen 4) shows no prices, no customer name and no phone number. A detail shop has no pipeline, Deals, Inventory or Rush. Words come from `ShopWords::DETAIL`: "work order"/"WO", "Detailer", "Front desk". Sizes are only Car / SUV / Truck or van. Paint correction is custom hourly at $75 an hour and is not on the booking page. Deposit is the shop's 25%, rounded to the cent.
- **Money actions always ask first.** No-show, Cancel, Refund it and Keep it show the confirm step ("Mark as a no-show? The $62.50 deposit is kept."). Draw one open, as on screen 3.
- **Not built yet, do not draw as features:** signed damage walkaround, package checklists, after photos sent to the customer, coating warranty tracker or certificates, wash clubs billed monthly, prepaid wash packs, gift cards, mobile routes, on-my-way and rain-day texts, fleet accounts. Photos on screens 2 and 4 are the staff's work order photos with captions (real). Rebooks are reminders and tasks (Automations, Tasks), not a billed plan; the "Maintenance wash every 2 weeks" line is a reminder cadence, not a subscription.
- **Tone.** Check-in photos are "as it came in" and note marks that "was there"; never accuse the customer or blame the detailer. One no-show, one car waiting on a kit, one estimate waiting: busy, not broken. No tax lines, no review counts that look bought.
- **Customer-facing pages** (screen 5, the links in screen 6) carry the shop's name only, not Top Shelf and not "Helcim". The tip is added by the customer on the pay link.
- **What changed from the current drafts:** the old set showed a home-services Home, a bare Calendars list and a booking page stuck on step 1, all in dark gold. The new set leads with the work order (size price, deposit, add-on OK, photos), shows the detailer's thumb view and a filled-in booking, and drops "Marketing" and "Subscriptions" from the nav.
