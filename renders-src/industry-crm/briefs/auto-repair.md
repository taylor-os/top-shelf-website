# Auto repair: screen brief

Source of truth: the shop side of the real Top Shelf CRM (Repairs: shop board, repair order, texted estimate approved job by job, technician job clock). Screens below follow those pages' layout and words. What changes: a repair shop has no car lot, so everything about stock, recon, inventory and sales is gone (the same cut the Detail Suite makes).

Sample day for every screen: **Tuesday, November 24, 2026, about 10:40 AM.** All numbers below agree across screens; keep them that way.

## 1. Business and cast

**Turnbuckle Auto Repair**, Garland, TX. One location, 5 bays, general repair, brakes, A/C, check-engine work, oil changes. 5 people. Shop line (972) 555-0148. Address 1450 Turnbuckle Dr, Garland, TX 75041 (fictional street). Labor rate $130/h.

Team:
- **Ray Delgado**, owner. Was the lead tech for 15 years, now runs the business and still works the counter on Saturdays.
- **Dana Whitfield**, service advisor. Writes every repair order, sends estimates, answers texts, takes payments.
- **Marcus Bell**, technician (lead).
- **Tony Huynh**, technician.
- **Caleb Ortiz**, technician.

Customers (all fictional, 555 numbers, area codes 972/214/469):
- **Brenda Ochoa**, 2018 Toyota Camry, silver. Brakes grinding. The estimate story (screens 2, 3, 4, 5).
- **Keisha Monroe**, 2017 Nissan Altima. Died on I-635 this morning; the AI receptionist booked her (screen 6).
- **Maria Esquivel**, 2016 Honda Odyssey, white. Rush belt job.
- **Walt Hendricks**, 2012 Chevrolet Tahoe, black. Check engine light, hasn't answered his estimate yet.
- **Darnell Price**, 2015 Ford F-150, blue. A/C, waiting on a compressor.
- **Priya Raman**, 2020 Honda CR-V, gray. Oil change done, ready for pickup, $89.94 owed.
- **Gary Lindqvist**, 2019 Jeep Wrangler, green. In for an oil change; declined front struts last month (follow-up due).
- **Alicia Navarro**, 2021 Kia Sorento, gray. Booked online last night.
- Also on the board: Tom Burleson (2011 Ford Ranger), Andre Whitley (2020 Hyundai Tucson), Hannah Pruitt (2017 Subaru Outback), Luis Carrasco (2014 Toyota Tacoma), Rhonda Faulk (2017 Chevrolet Malibu), Javier Montoya (2018 GMC Sierra 1500), Ed Saldana (2010 Toyota Corolla).

Name check: avoid anything like "Redline Auto & Tire" (the industry page's story shop) and "Mesquite Creek Motors" (the real demo lot). Turnbuckle is not a DFW shop name I know of.

### The board at 10:40 AM (the one source for every count)

| Column | RO | Car | Customer | Tech | Ready by | Done | Approval | Extra |
|---|---|---|---|---|---|---|---|---|
| Waiting | 2052 | 2018 Toyota Camry, Silver | Brenda Ochoa | Marcus | Today 5:00 PM | 0 of 2 done | 2 of 3 approved | 2 h |
| Waiting | 2053 | 2012 Chevrolet Tahoe, Black | Walt Hendricks | Tony | Wed 12:00 PM | 0 of 1 done | Waiting on Walt's OK | 1 h 45 m |
| Waiting | 2055 | 2021 Kia Sorento, Gray | Alicia Navarro | No tech yet | Wed 5:00 PM | 0 of 2 done | Waiting on Alicia's OK | 35 m |
| Waiting | 2054 | 2011 Ford Ranger, Red | Tom Burleson | Caleb | Today 4:00 PM | 0 of 1 done | 1 of 1 approved | 1 h |
| In progress | 2049 | 2016 Honda Odyssey, White | Maria Esquivel | Marcus | RUSH needed by Today 12:00 PM | 1 of 2 done | 2 of 2 approved | Clock running 0:41 |
| In progress | 2047 | 2019 Jeep Wrangler, Green | Gary Lindqvist | Tony | Today 3:00 PM | 0 of 1 done | 1 of 1 approved | Clock running 0:22 |
| In progress | 2050 | 2020 Hyundai Tucson, Blue | Andre Whitley | Caleb | Today 2:00 PM | 0 of 1 done | 1 of 1 approved | Clock running 0:18 |
| Waiting on parts | 2043 | 2015 Ford F-150, Blue | Darnell Price | Tony | Thu 5:00 PM | 0 of 1 done | 1 of 1 approved | Waiting on: A/C compressor, ETA Thu · 2 d |
| Waiting on parts | 2045 | 2017 Subaru Outback, Silver | Hannah Pruitt | Caleb | Wed 3:00 PM | 1 of 2 done | 2 of 2 approved | Waiting on: Rear wheel bearing, ETA Wed AM · 1 d |
| Quality check | 2046 | 2014 Toyota Tacoma, White | Luis Carrasco | Marcus | Today 11:00 AM | 2 of 2 done | 2 of 2 approved | 1 d |
| Done · Ready for pickup | 2041 | 2020 Honda CR-V, Gray | Priya Raman | Caleb | | 1 of 1 done | | Balance $89.94 · Not picked up · 40 m |
| Done · Ready for pickup | 2044 | 2017 Chevrolet Malibu, Black | Rhonda Faulk | Tony | | 2 of 2 done | | Paid · Not picked up · 1 h |
| Done · Picked up today | 2042 | 2018 GMC Sierra 1500, Gray | Javier Montoya | Marcus | | 3 of 3 done | | Paid $1,148.20 · Picked up 9:05 AM |

Counts: Waiting 4 · In progress 3 · Waiting on parts 2 · Quality check 1 · Done 3. Cars in the shop: 12 (all but the picked-up Sierra).

Tech load: Marcus Bell, 3 open repair orders · 6 jobs · 2.9 h clocked today. Tony Huynh, 3 open repair orders · 3 jobs · 2.4 h. Caleb Ortiz, 3 open repair orders · 4 jobs · 1.6 h. No tech yet: 1 repair order.

Money today: In today $1,504.95 (Javier $1,148.20 at pickup, Rhonda $356.75 by card from the text link at 10:12 AM). Owed $302.34 (Priya $89.94; Ed Saldana $212.40, RO 2031, picked up 6 d ago).

Brenda's estimate (RO 2052, Estimate 1, sent Tue 9:48 AM by Dana, answered 10:22 AM):
- Replace front brake pads and rotors · Labor $234 (1.8 h) · Parts $186 · **$420** · Approved. Parts: Front brake pads × 1, Front rotor × 2.
- Replace rear brake pads · Labor $143 (1.1 h) · Parts $52 · **$195** · Approved. Parts: Rear brake pads × 1.
- Brake fluid flush · Labor $65 (0.5 h) · Parts $18 · **$83** · Declined.
- Totals: Approved $615 · Not answered $0 · Declined $83.

## 2. Roles and what they need first

**Owner (Ray), desktop at 7 AM and again mid-morning**
1. What needs him right now (one next step).
2. Car count: what's in each stage, what's stuck, any rush.
3. Money: in today, owed, work approved today.
4. Who is loaded and who is idle (each tech's open ROs and clocked hours).
5. Calls the shop would have missed, and declined work that's due a follow-up.
- Trust: it uses his words (RO, ready by, waiting on parts, the customer's OK) and the numbers add up. Dismiss: anything that looks like a car lot (inventory, stock numbers) or a plumber's dispatch map.

**Service advisor (Dana), desktop at the counter, phone ringing**
1. Who replied or answered an estimate.
2. Who's waiting on their OK and how long.
3. What's ready for pickup and whether it's paid.
4. The repair order: car, concern, jobs, prices, approvals, photos, in one page.
5. One-tap Call / Text the customer from the RO.
- Trust: approvals are recorded per job with the customer's name and the time, so "I never said yes to that" is answered. Dismiss: having to retype a job's price in two places.

**Technician (Marcus), phone in one greasy hand**
1. The job clock: running or not, big Stop / Start.
2. What's next, rush first.
3. The parts for this job.
4. Add photo of what he found (worn pads, cracked belt), add a note.
5. Mark Done, or flag the whole RO Waiting on parts.
- Trust: one big button and it keeps his hours honest. Dismiss: prices, customer phone numbers, or anything he has to type a lot into.

**Customer (Brenda), phone, from a text**
1. Which car and which shop (so it's not spam).
2. Each job in plain words with the price, split labor and parts.
3. Photos of what they found.
4. Approve or decline each job herself, not all-or-nothing.
5. A Call button, and the running total she's agreeing to.
- Trust: seeing the photo of her own worn rotor and choosing job by job. Dismiss: a single lump price with an "Approve all" button.

## 3. Words

| Bone | Shop word |
|---|---|
| Customer | Customer (and their car: year make model, color, VIN end, miles in) |
| Visit | Appointment / drop-off on the calendar; once the car is in, it's a Repair order |
| Deal | Estimate (Estimate 1, Estimate 2 on the same RO) |
| Work item | Repair order (RO 2052), made of Jobs; each job has labor hours, parts, outside work, photos, notes |
| Money | Estimate, bill, balance, pay link, card payment, Paid |
| Conversation | Texts, Phone, the shop line |
| Automation | Estimate text, ready-for-pickup text with pay link, review request, follow-up on declined work |
| Team | Owner, Service advisor, Technician |
| Customer view | The estimate page (Approve / Decline each job), the pay page, the booking page on the shop's website |

Status words (exact, from the kit): Waiting · In progress · Waiting on parts · Quality check · Done · Ready for pickup · Picked up · RUSH · needed by · Ready by · Waiting on Brenda's OK · 2 of 3 approved · 0 of 2 done · Clock running · Booked 1.8 h · Clocked 0.68 h · Move to... · Open repair order · Rush first · Oldest first · My jobs · My hours.

Nav, owner (desktop sidebar, grouped as the kit groups it):
- Every day: Home · Repairs · Appointments · Customers · Tasks
- Talk: Texts · Phone
- Office: Payments · Reviews · Reports
- Setup: Team · Settings · Help

Nav, service advisor (desktop): Every day: Home · Repairs · Appointments · Customers · Tasks / Talk: Texts · Phone / Office: Payments · Reviews / Setup: Help. Phone bottom tabs: Home · Repairs · Customers · Texts · More.

Nav, technician (phone bottom tabs): Home · Repairs · Tasks · More. Nothing else.

The Repairs page is titled **Shop board**. Home's "How your lot runs" link becomes **How your shop runs**.

Must NOT appear: Inventory, Stock / stock number, recon, Rush recon, lot, the lot line, deal, deal jacket, salesperson, lender, loan, down payment, title, Buyers Guide, "Our own car" (car-lot words); job site, on site, crew, dispatch map, route, service area, on my way, en route (home-services words); patient, appointment type codes, chart, menu, table, listing, matter, class (other industries); invoice (the kit says bill), sign / signature / e-sign (the customer types their name and ticks a box); plate numbers; "DMO-"; "Demo: nothing was really sent".

## 4. The 6 screens

Every image: bottom strip "Sample screens · sample data, not a real business". Staff screens use the emerald kit (emerald sidebar, emerald header band on desktop, light canvas, white cards). Rush chip red; running clock Stop button red; Start clock emerald; approval chips: green "N of N approved", blue "Waiting on X's OK"; declined in grey with strike-free text "Declined".

### Screen 1. Owner home ("the shop's day"), desktop 1440x900, Ray Delgado

Job: in ten seconds Ray knows what needs him, how full the shop is, and the money.

- **Sidebar (left, emerald):** top: shop mark + "Turnbuckle Auto Repair", under it "Ray Delgado · Owner". Owner nav from section 3, Home active. Tasks badge "2". Bottom: avatar "RD Ray Delgado".
- **Header band (emerald):** "Home" on the left, "Search customers..." box on the right.
- **Title row:** "Turnbuckle Auto Repair" (large), right: "? How your shop runs".
- **Next step card (full width, outlined):** label "NEXT STEP". Text "Brenda Ochoa approved 2 of 3 jobs on the 2018 Toyota Camry ($615)". Primary button "Open the RO".
- **Left column (about 60%), heading "SERVICE TODAY":**
  - Card "Ready for pickup · 2  →". Rows (each with Call and Text buttons on the right):
    - Priya Raman · 2020 Honda CR-V · RO 2041 · **Balance $89.94** · "Done 40 m ago · not texted yet"
    - Rhonda Faulk · 2017 Chevrolet Malibu · RO 2044 · **Paid** · "Ready text sent 9:58 AM"
  - Card "Money owed · 2" with right side "$302.34 owed · $1,504.95 in today  →". Rows with Call / Text:
    - Priya Raman · 2020 Honda CR-V · RO 2041 · Balance $89.94 · Not picked up · done 40 m ago
    - Ed Saldana · 2010 Toyota Corolla · RO 2031 · Balance $212.40 · Picked up 6 d ago
  - Card "Waiting on the customer's OK · 2  →". Rows with Call / Text:
    - Walt Hendricks · 2012 Chevrolet Tahoe · RO 2053 · Estimate $130 · sent 8:55 AM
    - Alicia Navarro · 2021 Kia Sorento · RO 2055 · Estimate $512 · sent 10:05 AM
  - Card "Declined work to follow up · 3  →". Rows with Text:
    - Gary Lindqvist · 2019 Jeep Wrangler · Replace front struts $860 · declined Oct 21 · **due today** (his car is in the shop now: RO 2047)
    - Shawna Riggs · 2016 Mazda CX-5 · Replace rear brake pads $210 · declined Nov 4 · due Dec 4
    - Brenda Ochoa · 2018 Toyota Camry · Brake fluid flush $83 · declined today · due Dec 22
- **Right column (about 40%):**
  - Five stat tiles in a row of 3 + 2: "4 Waiting", "3 In progress", "2 Waiting on parts", "1 Quality check", "3 Done today".
  - Card "Rush": one row "RO 2049 · 2016 Honda Odyssey · Maria Esquivel" with red RUSH chip, "needed by 12:00 PM · 1 of 2 done · Marcus".
  - Card "Today's money": three figures side by side: "Approved today $1,342.00", "In today $1,504.95", "Owed $302.34". Under it, small: "Average RO this week $418".
  - Card "Calls today": "AI receptionist answered 7 · booked 3 · missed-call texts 1". One line under: "10:31 AM Keisha Monroe · 2017 Nissan Altima · booked drop-off 1:00 PM".
  - Card "Coming in today": 1:00 PM Keisha Monroe · 2017 Nissan Altima · tow-in, won't start / 2:30 PM Ben Okafor · 2019 Toyota Corolla · oil change / 4:15 PM Lupe Garza · 2015 Honda Pilot · A/C check.
  - Team card (kit style, one row per tech): "Marcus Bell · 3 open repair orders · 6 jobs · 2.9 h today" / "Tony Huynh · 3 open repair orders · 3 jobs · 2.4 h today" / "Caleb Ortiz · 3 open repair orders · 4 jobs · 1.6 h today".
  - Small card "Reviews: 11 requests sent this week · 5 new · 1 to reply to  →".

### Screen 2. Shop board (signature), desktop 1440x900, Dana Whitfield

Job: every car in the shop, by stage, at a glance; move a car in one click.

- **Sidebar:** advisor nav, Repairs active; "Turnbuckle Auto Repair / Dana Whitfield · Service advisor".
- **Header band:** breadcrumb "Home > Repairs", "Search customers..." right.
- **Title row:** "Shop board" left. Right buttons: "Rush first" (sort icon), "List", "My jobs", primary "+ Open repair order".
- **Five equal columns**, header "name ... count": Waiting 4 · In progress 3 · Waiting on parts 2 · Quality check 1 · Done 3. Draw every card from the board table in section 1, in this order within each column (Rush first sort: rush on top, then by Ready by).
- **Card anatomy (top to bottom, kit order):** "RO 2049" bold; RUSH chip + red "needed by Today 12:00 PM" when rush; car "2016 Honda Odyssey" bold; grey line "White · Maria Esquivel"; "Ready by Today 12:00 PM"; tech first name "Marcus"; chip "1 of 2 done"; approval chip ("2 of 2 approved" green, or "Waiting on Walt's OK" blue); "Waiting on: A/C compressor, ETA Thu" where set; clock icon + age ("1 h 45 m", "2 d"); red wrench line "Clock running 0:41" where running; outlined button "Move to...".
- **Done column:** sub-heading "Ready for pickup 2", the two cards with "Balance $89.94 · Not picked up" (amber) and "Paid · Not picked up" (green); then sub-heading "Picked up today 1" with the Sierra card "Paid $1,148.20 · Picked up 9:05 AM" (no Move button).
- At 900 px tall, show the first 2 cards fully in each column and let the third peek; the Waiting column shows RO 2052 (Brenda) first with the green "2 of 3 approved" chip.

### Screen 3. The repair order, desktop 1440x900, Dana Whitfield

Job: one page that holds the car, the customer, the jobs, the prices and exactly what the customer approved.

- **Sidebar / header** as screen 2; breadcrumb "Home > Repairs > RO 2052".
- **Main column (left ~65%):**
  - Header card: "RO 2052" + chip "Waiting"; right button "Move". Car "2018 Toyota Camry". Grey line "Silver · VIN ...604417 · 61,280 mi in". Customer "Brenda Ochoa" (underlined link) with Call and Text buttons on the right. Line "Ready by Today 5:00 PM · Written by Dana Whitfield · 2 h in Waiting". Concern box: "Grinding from the front when braking. Brake light came on Sunday." Link "Edit concern and Ready by". Small red link "Cancel this repair order".
  - Notice band (emerald tint, check icon): "Brenda answered Estimate 1 Tue 10:22 AM: 2 approved, 1 declined. Answered by Brenda Ochoa."
  - "Jobs" heading, right button "+ Add a job". Three job cards, each: job title; line "Marcus · Booked 1.8 h · Clocked 0 h"; "Labor $234 · Parts $186"; "Parts: Front brake pads × 1, Front rotor × 2"; price right "$420"; chip "Approved Tue 10:22 AM" (green). Second card: "Replace rear brake pads" · Marcus · Booked 1.1 h · Clocked 0 h · Labor $143 · Parts $52 · Parts: Rear brake pads × 1 · $195 · "Approved Tue 10:22 AM". Third: "Brake fluid flush" · Booked 0.5 h · Labor $65 · Parts $18 · $83 · grey chip "Declined Tue 10:22 AM" + small line "Follow-up reminder Dec 22".
  - Sticky totals bar at the bottom of the main column: "Approved $615   Not answered $0   Declined $83". Nothing may sit half-cut below it.
- **Right column (~35%):**
  - "Photos": two thumbnails with captions "Front pads, 2 mm left" and "Rotor scoring, driver side"; button "Add photo".
  - "Notes": one note "Rear pads about 4 mm. Fluid is dark. — Marcus, 9:31 AM"; empty "Add a note" box; hint "No customer names or phone numbers. Technicians can see this."; button "Add note".
  - "History" (newest first): "Brenda answered Estimate 1 · Tue 10:22 AM" / "Estimate 1 sent by text · Tue 9:48 AM · Dana Whitfield" / "Job added: Brake fluid flush · 0.5 h · Rate $130 · Total $83" / "Photos added · 9:30 AM · Marcus Bell" / "Repair order opened · 8:40 AM · Dana Whitfield".

### Screen 4. Technician: My jobs with the job clock, phone 390x844, Marcus Bell

Job: start, stop and finish his jobs one-handed, rush first, with the parts and photos right there.

- **Top bar:** sidebar icon, "My jobs".
- **Title row:** "My jobs", link "My hours >", segmented toggle "Rush first" (active) | "Oldest first".
- **Card 1 (rush, expanded):** "2016 Honda Odyssey · White · Customer car" (no customer name). RUSH chip + red "needed by Today 12:00 PM". Divider. Job "Replace serpentine belt and tensioner  >". Grey "RO 2049 · In progress · Booked 1.2 h · Clocked 0.68 h". "Ready by Today 12:00 PM". "Parts: Serpentine belt × 1, Belt tensioner × 1". Full-width red button "■ Stop 0:41:07". Full-width outlined "✓ Done". Two half buttons "Add photo" | "Notes (1)". Full-width outlined "Whole repair order: Waiting on parts". Two real-looking photo tiles (not grey placeholders) captioned "Old belt, cracked" and "Tensioner pulley wobble".
- **Card 2 (peeking at the bottom):** "2018 Toyota Camry · Silver · Customer car". Job "Replace front brake pads and rotors". "RO 2052 · Waiting · Booked 1.8 h". Full-width emerald button "▶ Start clock".
- **Bottom tabs:** Home · Repairs (active) · Tasks · More.
- No prices anywhere on this screen.

### Screen 5. The customer's estimate, phone 390x844, Brenda Ochoa

Job: Brenda sees what they found and picks job by job, then sends her answers. Styled as Turnbuckle's own page (white page, the shop name in a modest dark red accent, not the emerald staff app).

- **Shop header:** "Turnbuckle Auto Repair" bold, "1450 Turnbuckle Dr, Garland, TX 75041", phone icon "(972) 555-0148".
- **Title:** "Estimate 1 for Brenda, from Dana". Grey "November 24, 2026".
- **Car card:** "2018 Toyota Camry" / "Silver · VIN ends 604417 · RO 2052 · 61,280 miles in".
- **Heading:** "Approve or decline each job".
- **Job card 1:** "Replace front brake pads and rotors" with "$420" right. "Labor $234 · Parts $186". Two photo thumbnails captioned "Front pads, 2 mm left" and "Rotor scoring, driver side". Two buttons "Approve" (selected: filled accent, check icon) | "Decline".
- **Job card 2:** "Replace rear brake pads" "$195". "Labor $143 · Parts $52". "Approve" selected.
- **Job card 3:** "Brake fluid flush" "$83". "Labor $65 · Parts $18". "Decline" selected.
- **Total card:** "You are approving  $615.00". Grey: "Prices are before any tax or fees on your final bill."
- The form (may run below the fold; draw it if the canvas is a tall crop, else show its top): "Your full name" field filled "Brenda Ochoa"; checkbox (ticked) with the words exactly "I authorize Turnbuckle Auto Repair to do the work I approved above, for the prices shown. Turnbuckle Auto Repair will ask me again before doing other work or charging more."; full-width button "Send my answers"; outlined button "Call Turnbuckle Auto Repair".
- No "Preview" banner, no staff nav.

### Screen 6. The call the shop would have missed, phone 390x844, Dana Whitfield

Job: a stranded driver called while everyone was under a car; the AI receptionist answered, booked her and texted her, and it's all in one thread.

- **Top bar:** sidebar icon, "Texts", search icon.
- **Thread header:** back arrow, "Keisha Monroe", grey "Texting from the shop line, (972) 555-0148", button "Call".
- **Chip row:** "Dana Whitfield" (assigned) · chip "Appointment Today 1:00 PM" · chip "New customer".
- **Call card (centered, full width, phone icon):** "Call answered by the AI receptionist · 10:31 AM · 2 min 40 s". Summary lines: "2017 Nissan Altima died on I-635 near Jupiter Rd. Cranks but won't start." / "A wrecker is bringing it in." / "Booked: drop-off today 1:00 PM." / "Wants a call with the estimate before any work." Link "Play recording".
- **Outgoing text (right, emerald bubble), 10:34 AM, small tag "Sent automatically":** "Hi Keisha, this is Turnbuckle Auto Repair. You're booked today at 1:00 PM for your 2017 Nissan Altima. Have the wrecker drop it at 1450 Turnbuckle Dr, Garland. If we're with a customer, keys go in the drop box by the office door. We'll text you the estimate before we do any work."
- **Incoming (left, grey), 10:36 AM:** "ok thank you. tow truck says about 12:30"
- **Outgoing (right), 10:38 AM, "Dana":** "Got it, Keisha. We'll watch for it and call you once Marcus has a look."
- **Composer:** paperclip, "Text message" field, send button.
- **Bottom tabs:** Home · Repairs · Customers · Texts (active) · More.

## 5. How it uses the bones

| Screen | Records read |
|---|---|
| 1 Owner home | Work item (ROs by status, rush, approvals), Money (balances, payments today, approved totals), Team (tech load, clocked hours), Visit (today's appointments), Conversation (AI receptionist calls), Automation (declined-work follow-ups, review requests), Customer |
| 2 Shop board | Work item (RO status, jobs done, approvals, waiting-on), Team (tech), Customer, Money (balance on Done cards), Visit (ready by) |
| 3 Repair order | Work item (concern, jobs, parts, photos, notes, history), Deal (Estimate 1 and its answers), Money (job prices, totals bar), Customer, Team, Automation (follow-up on the declined job) |
| 4 Technician My jobs | Work item (jobs, parts, photos, notes, status), Team (job clock punches, hours), Visit (ready by) |
| 5 Customer estimate | Customer view (estimate link), Deal (estimate version), Work item (jobs, photos), Money (labor/parts/price) |
| 6 Text thread | Conversation (AI receptionist call + texts), Visit (appointment booked), Automation (booking confirmation text), Customer, Team (assigned advisor) |

## 6. Watch-outs

- **Keep from the real kit, exactly:** the five board columns and their names; "Waiting on Brenda's OK"; "N of N approved" / "N of N done" chips; "Ready by"; RUSH + "needed by"; "Move to..."; "Open repair order"; the RO totals bar "Approved / Not answered / Declined"; the customer page's Approve / Decline per job, "You are approving", the tax note and the authorization sentence word for word (it's written for counsel; only the shop name changes); "Send my answers"; the tech clock's big red Stop with a running timer, Done, Add photo, Notes (n), "Whole repair order: Waiting on parts"; "Booked h · Clocked h"; the notes hint "No customer names or phone numbers. Technicians can see this."
- **Technicians see no customer names, phone numbers or prices.** Their cards say "Customer car".
- **Customer approval is a typed name plus a ticked box, not a signature.** Don't draw a signature pad or say "sign".
- **Strip every car-lot trace:** no Inventory tab, stock numbers, recon, "Rush recon", "our own cars", lenders, titles. The kit's screenshots show these; the shop version must not.
- **No plates.** The kit showed "DMO-1019" style plates and owners noticed. Show color, VIN end and miles in instead.
- **Use "bill", not "invoice", inside the staff app** (kit word). The customer can see "Pay your bill".
- **No alarming numbers:** nothing past due more than a week except one $212.40 balance; no "dozens overdue"; Tasks badge stays 2.
- **No unsupported features:** no parts ordering, no parts catalog or VIN decoder, no inspection checklist builder, no tire/parts inventory, no payroll, no flat-rate pay calculations, no fleet accounts. Average RO and clocked hours are Reports figures only.
- **No demo labels** in the art ("Demo: nothing was really sent", "Preview: this is what the customer sees"); the bottom strip is the only sample label.
- **Prices plausible for DFW:** $130/h labor; brake jobs $195 to $420; nothing that reads as gouging.
- Tone for the customer: plain words, no jargon beyond the job name; the photos do the convincing.
