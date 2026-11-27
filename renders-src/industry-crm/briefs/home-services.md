# Home services: screen brief (slug `home-services`)

Source of truth: the FieldPro app (`C:\Users\taylo\FieldPro`, read at `edadca0`, Nov 23 2026) and the homepage screens in `top-shelf-website-focus\assets\img\crm\`. Every label, status word, button and default text message below is copied from FieldPro unless marked **(sample)**. The homepage hero already shows the owner's Today screen on Tue Nov 24, so this set is the **next day, Wed Nov 25, 2026** (day before Thanksgiving, first cold snap, lots of no-heat calls). The set leans toward the dispatch board, the tech at the door, the estimate the homeowner picks from, and the texts.

---

## 1. Business and cast

**Prairie Air & Heat**, Allen, TX (same business as the homepage screens). Residential heating and cooling: repair, tune-ups, system replacements. One shop, 6 people. Service area: Allen, McKinney, Plano, Frisco, Wylie, Murphy, Fairview, Lucas. Main line (469) 555-0130.

| Person | Role | Notes |
|---|---|---|
| Travis Boone | Owner | Still runs calls and does the big replacement estimates himself. Initials TB (as on the homepage). |
| Brandi Kessler | Office manager / dispatcher | Answers what the AI doesn't, builds the board, assigns techs. Role name in the app: Dispatcher. |
| Kyle Danner | Technician | Service tech; on call last night. |
| Marcus Reed | Technician | Service tech. |
| Luis Ortega | Technician (installer) | Runs full-day system replacements. |
| Jake Whitt | Technician | Tune-ups and service. |

Customers (all fictional, 555 numbers):

| Customer | City | Today's story |
|---|---|---|
| Gloria Banks, (469) 555-0182 | 2208 Hollyberry Ln, McKinney, TX 75071 | Called 2:14 AM, no heat. AI receptionist answered and booked 1:00–3:00 PM. Thread runs through screens 1, 2, 3, 6. |
| Hannah Cole, (972) 555-0147 | 5527 Brookhollow Dr, Frisco, TX 75034 | Heat pump short cycling (homepage, Tue). Got a repair-or-replace estimate with 3 options. Screen 5. |
| Carla Mendez | 3017 Cedar Elm Dr, Wylie | AI booked Wed 8–10 AM (matches the homepage call log). |
| Dale Pruitt | 1409 Ashwood Ct, Allen | 7:00 AM no-heat call, done and paid $389.00. |
| Dennis Okafor | 912 Willow Bend Dr, Allen | System replacement install today (Luis). |
| Priya Natarajan, (469) 555-0119 | Allen | $11,482.60 replacement estimate waiting 6 days. Screen 4. |
| Owen Fitch | McKinney | Still owes $267.61 (carried over from the homepage). |
| Lorraine Pike | 6104 Larkspur Ln, Plano | New booking at 10:12 AM, not assigned yet. |
| Raymond Ochoa, Rita Castellano, Victor Ramsey, Bev Halloran, Marisol Vega, Curtis Lyle, Carol Strickland, Tom Reyes, Greg Tolliver, Derek Mott | DFW suburbs | Fill the board and lists. |

---

## 2. Roles and what they need first

**Owner (Travis), 7 AM at the kitchen table, then from the truck**
1. Did anything come in overnight, and is it on the board?
2. Who is not assigned yet today.
3. Who is waiting on a reply (calls and texts).
4. Money: collected today, still owed, anything finished but not billed.
5. Big estimates sitting out there with no answer.
Trust: the 2 AM no-heat call is already a booked job with an address and a time window. Dismiss: a "leads" funnel, marketing charts, or anything that makes him type at 7 AM.

**Dispatcher (Brandi), phone ringing, board open**
1. The day board: every tech's row, what time, what town.
2. The unassigned tray.
3. Where each tech actually is (On my way / Working / Done).
4. Gaps big enough to squeeze in another call.
5. One tap to tell the customer the new time after a move.
Trust: drag a job to another tech and the app offers to text the customer. Dismiss: a calendar that hides which tech has what, or needs 4 clicks to reassign.

**Technician (Kyle), one hand, standing in a utility room or at the front door**
1. Next stop: name, address, Directions.
2. "On my way" (texts the customer for him).
3. What's wrong, per the booking.
4. Line items from the price book, then get paid on the spot (card, split, tip).
5. What he earned today.
Trust: Get paid opens right on the job, the card is charged from his phone, and the job can't be finished until the checklist and payment are done. Dismiss: tiny desktop tables, or anything that makes him call the office for a price.

**Homeowner (Gloria, Hannah)**
1. Someone answered and I have a time window.
2. Who is coming and when ("Your technician is Kyle", "on the way").
3. What it costs, in plain lines, before work starts.
4. Choices on a big repair (repair vs replace), approve from the couch.
5. Pay by card from a text link; reply to a text to reschedule.
Trust: texts signed with the company name, prices with tax shown, no surprise fees. Dismiss: an app download, a login, or a page that looks like a software company instead of the HVAC company.

---

## 3. Words

**Bones to industry words**

| Bone | Home-services word (as in FieldPro) |
|---|---|
| Customer | Client (nav and records); "customer" in actions ("Tell the customer") |
| Visit | Visit (on the Schedule), shown inside a Job; time shown as a window "1:00–3:00 PM" |
| Deal | Estimate (statuses: Draft, Awaiting response, Changes requested, Approved) with options Good · Better · Best |
| Work item | Job, with line items grouped **Services** and **Materials**, Inspection checklist, photos, Close out |
| Money | Invoice, Payment, Balance, Collected, Still owed, Tips ("100% to the tech"), Earnings (tech) |
| Team | Owner, Dispatcher, Technician |
| Field status | Scheduled → On my way → Working → Done |
| Conversation | Inbox (texts + calls in one thread), Phone |

**Nav labels in order (from FieldPro `config/navigation.php` + role access)**
- Owner desktop sidebar: Today, Jobs, Clients, Inbox, Schedule, Mail; MONEY: Invoices, Estimates, Payroll, Cash; MORE: Reports, Reviews, Inventory, Automations, Settings. (Same as the homepage image.)
- Owner phone tabs: Today, Invoices, Phone, Reports, More.
- Dispatcher desktop sidebar: Today, Jobs, Clients, Inbox, Schedule; MONEY: Invoices, Estimates; MORE: Reports, Settings.
- Dispatcher phone tabs: Today, Schedule, Inbox, Jobs, More.
- Technician phone tabs: Today, Jobs, Schedule, Earnings, More.
- Customer pages: no nav. Company name, document type, total, contact.

**Must NOT appear** (other industries): patient, chart, copay, provider, guest, reservation, table, cover, server, tab, chair, stylist, service advisor, repair order, RO, vehicle, VIN, bay, matter, retainer, case, listing, showing, buyer, seller, member, membership, class, session, coach, treatment plan, deal, lead, opportunity, prospect, work order, ticket, booking fee, "appointment" on staff screens (it is fine in customer texts, where FieldPro uses it).

---

## 4. The 6 screens

Shared kit: emerald sidebar/header band, light canvas, white cards, chips, phone bottom-tab bar, as in `hero-dash-d.jpg` / `hero-dash-m.jpg` / `s2-job-m.jpg`. Phone status bars show the time given. Every image ends with the strip **"Sample screens · sample data, not a real business"**.

### Screen 1. Owner home ("Today"), desktop 1440x900
Job: what Travis checks at 7:50 AM before the trucks are all rolling. Layout identical to `hero-dash-d.jpg`; only the data changes.

- **Sidebar (left, emerald):** "Prairie Air & Heat"; owner nav as in section 3 with **Today** active; **Inbox** red badge "1"; footer "TB · Travis Boone · Owner" and "P · Prairie Air & Heat · Active company". Right edge: the thin rail with the phone icon, red badge "1".
- **Header band:** "Good morning, Travis" / "Wed, Nov 25 · 10 jobs today · 4 things need you". Avatar TB.
- **KPI row (5 tiles):**
  - Jobs done: **1** of 10 / "9 still open"
  - Booked today: **$15,186.42** / "today's job totals"
  - Collected today: **$389.00** (green) / "+ $15.00 tips"
  - Still owed: **$14,797.42** (orange) / "on today's jobs"
  - Finished at $0: **0** / "every job finished today billed"
- **Left column, "TODAY'S JOBS 10 · 1 of 10 done · Schedule →"**
  - NEXT UP card: chips "Kyle Danner", "Scheduled", "Skip →". "8:00 AM" time tile. **Carla Mendez**. "Heat runs but blows cool air" (green). Pin "3017 Cedar Elm Dr, Wylie, TX". Call + map buttons.
  - Row: 7:00 AM · **Dale Pruitt** · 1409 Ashwood Ct, Allen, TX · "No heat, furnace won't light" · chips "Kyle Danner", "Done" · sub-line "No notes · Card · Paid".
  - Row: 8:00 AM · **Raymond Ochoa** · 815 Kingsbridge Dr, McKinney, TX · "Upstairs bedroom won't warm up" · chips "Marcus Reed", "On my way".
  - Row: 8:00 AM · **Dennis Okafor** · 912 Willow Bend Dr, Allen, TX · "System replacement, 4-ton heat pump" · chips "Luis Ortega", "On my way".
  - (list continues below the fold: 8:30 AM Bev Halloran, Jake Whitt)
- **Right column, "NEEDS ATTENTION 4":**
  - **Unassigned today** (red icon, badge 1): red dot · Gloria Banks · "1:00 PM"
  - **Needs reply** (red, badge 1): red dot · (214) 555-0166 · "YES. Heater clicks but w…" (a reply to the missed-call text-back)
  - **Unpaid invoices** (amber, badge "$267.61"): amber dot · Owen Fitch · $267.61
  - **Signed, not scheduled** (amber, badge 1): amber dot · Greg Tolliver · $8,912.40

### Screen 2. Signature: Dispatch board (Schedule, Day view), desktop 1440x900
Job: Brandi places every visit on a tech's row against the clock, at 10:40 AM. This is FieldPro's real Day board (`resources/views/livewire/schedule/index.blade.php`).

- **Sidebar:** dispatcher nav (section 3), **Schedule** active, Inbox badge "1"; footer "BK · Brandi Kessler · Dispatcher".
- **Page header:** title "Schedule"; subtitle "Drag a visit to another day to move it. In Day view, drag it along a tech's row to change the time or onto another row to reassign it, or click it to edit." Right: segmented Month / Week / **Day** (Day filled emerald), "<", "Today", ">".
- **Date line** (emerald text): "Wednesday, Nov 25, 2026 · Today".
- **Unassigned tray** (card with red dashed border): "Unassigned (1)" in red; right "Drag onto a tech's row, or pick one on the card" + chevron. One card (240px wide, emerald left accent): "3:30 PM – 5:00 PM" / **Lorraine Pike** / "Thermostat blank, no heat" / pin "6104 Larkspur Ln, Plano" / a small select reading "Unassigned".
- **Timeline card:** hour labels across the top 7 AM, 8 AM … 5 PM. Left name column (144px) per row: tech name bold + "N visits". Thin hour gridlines. Each visit is a rounded block placed by time: top line time window (small grey) + status pill at right when not Scheduled, then **client name** bold, job title, street + city. Left accent: green when Done, emerald otherwise. Done blocks at 60% opacity. Green "free" text sits centered in gaps between stops.
  - **Kyle Danner · 3 visits:** 7:00–7:45 AM Dale Pruitt, "No heat, furnace won't light", 1409 Ashwood Ct, Allen, pill **Done** · 8:00–10:00 AM Carla Mendez, "Heat runs but blows cool air", 3017 Cedar Elm Dr, Wylie, pill **Done** · gap "3h free" · 1:00–3:00 PM Gloria Banks, "No heat, upstairs and down", 2208 Hollyberry Ln, McKinney (no pill).
  - **Marcus Reed · 3 visits:** 8:00–9:30 AM Raymond Ochoa, "Upstairs bedroom won't warm up", 815 Kingsbridge Dr, McKinney, **Done** · 10:00–11:30 AM Rita Castellano, "Furnace tune-up & filter change", 2650 Pecan Hollow Dr, Allen, pill **Working** (amber) · gap "2h 30m free" · 2:00–3:30 PM Victor Ramsey, "Thermostat follow-up", 3390 Lakeshore Trl, McKinney.
  - **Luis Ortega · 1 visit:** one long block 8:00 AM–4:00 PM Dennis Okafor, "System replacement, 4-ton heat pump", 912 Willow Bend Dr, Allen, pill **Working**.
  - **Jake Whitt · 3 visits:** 8:30–10:00 AM Bev Halloran, "Fall tune-up, two systems", 418 Brookview Ln, Murphy, **Done** · 10:30 AM–12:00 PM Marisol Vega, "Weak airflow, back bedrooms", 1127 Cypress Point Dr, Fairview, pill **On my way** (amber) · gap "2h 30m free" · 2:30–4:00 PM Curtis Lyle, "AC won't shut off", 77 Ranch Gate Rd, Lucas.
  - No overlaps (no red outlines).
- **Toast** (bottom center, white, emerald ring): "Moved Curtis Lyle to Wed, Nov 25, 2:30 PM – 4:00 PM. Tell the customer the new time?" Buttons: "Not now" (text) and **"Tell the customer"** (emerald, chat icon).
- **Floating pill** bottom right: "+ New job".

### Screen 3. Technician at the door: Get paid, phone 390x844
Job: Kyle finishes Gloria's no-heat call at 2:40 PM and charges her card on the spot. Kit: job page (`s2-job-m.jpg` layout) with the **Record payment** sheet (`invoices/payment-actions.blade.php`) open over it.

- **Behind the sheet (dimmed 50%, top 200px visible):** emerald header "← Jobs", wrench tile, "No heat, upstairs and down", pill "Working", "Gloria Banks", "2208 Hollyberry Ln, McKinney, TX".
- **Bottom sheet (white, rounded top, from y≈200 to the tab bar):**
  - "Record payment" (bold) / "How did the customer pay?"
  - Method grid, 3 columns: Cash, Check, Cash App / Zelle, Venmo, **Card** (selected: emerald border + light emerald fill) / Other.
  - "Amount ($)" field: **406.17**. Helper: "Defaults to the full balance; lower it to split across cards or methods."
  - "Add a tip · 100% to the tech" (the "· 100% to the tech" in green). Buttons: **10%** "$40.62" (selected), 20% "$81.23", 30% "$121.85", "No tip", "Custom".
  - Big emerald button: **"Charge card · $446.79"**.
  - Row under it: "Cancel" (text).
- **Tab bar:** Today, **Jobs** (active), Schedule, Earnings, More.
- Status bar 2:40.

(Job math, sample: Services "Diagnostic & service call" 1 × $89.00; Materials "Hot surface igniter" 1 × $165.00, "Flame sensor" 1 × $128.00; tax 8.25% on materials $24.17; total $406.17.)

### Screen 4. Owner on the go: estimates waiting on an answer, phone 390x844
Job: at 12:20 PM between stops, Travis works the chase list of estimates nobody has answered. Kit: Estimates page, **Awaiting** tab (`livewire/quotes/index.blade.php`).

- **Header (emerald band):** "Estimates" / "Quote your clients for upcoming work."; white button "+ New estimate" at right.
- **Overview row:** "**Overview** $38,906.05 open · 5 awaiting ⌄".
- **Status tabs (wrap to 2 rows, counts in small pills):** All 14 · Draft 2 · **Awaiting 5** (selected, emerald tint + ring) · Approved 6 · Archived 1.
- **Cards** (white, one per estimate; each followed by two small outlined buttons "📞 Call" and "💬 Text"):
  1. **Priya Natarajan** · pill "Awaiting response" · "New 3-ton heat pump, 16 SEER2" · divider · "#EST-1187 · Nov 19, 2026" left, **$11,482.60** right · amber line "Waiting 6 days · Last contact Nov 21" (the "Last contact" part grey).
  2. **Carol Strickland** · pill "Changes requested" · "Attic duct replacement" · "#EST-1179 · Nov 17, 2026" · **$4,315.00** · "Waiting 8 days · Last contact Nov 20".
  3. **Tom Reyes** · pill "Awaiting response" · "Furnace + coil replacement" · "#EST-1191 · Nov 22, 2026" · **$7,268.45** · "Waiting 3 days · No contact yet" (card cut off by the tab bar).
- **Tab bar:** Today, Invoices, Phone, Reports, **More** (active).
- Status bar 12:20.

### Screen 5. Homeowner's view: the estimate with options, phone 390x844
Job: Hannah opens the estimate link from her text at 8:47 PM and picks between repair and replace. Kit: Client Hub estimate (`resources/views/hub/quote.blade.php` + `components/hub/doc.blade.php`). Styled as Prairie Air & Heat, not the staff app: no emerald, no tab bar.

Business styling (sample): rail color deep navy #1F2D3D, accent burnt orange #C25E17 with white text. Page background light grey; the document is a white card with large rounded corners.

- **Top rail (navy, stacked on phone; use the kit's compact phone spacing, contact block hidden):**
  - Orange square tile "P" + "Prairie Air & Heat" (white, semibold).
  - Big centered "ESTIMATE" (white, extra-bold, wide letter spacing); under it a gold chip "Valid 30 days".
  - Centered "ESTIMATE FROM" (small caps, white 70%) / **$289.26** (large white) / "Sent Nov 24, 2026" (white 80%).
  - No estimate number (customer pages hide it by default).
- **White column:**
  - "PREPARED FOR" (small caps grey) / **Hannah Cole** / "5527 Brookhollow Dr, Frisco, TX 75034" / "(972) 555-0147".
  - "Choose the option that works best for you, then sign to approve."
  - **Option card 1** (grey border, radio empty): "Repair: new capacitor" **$289.26**. SERVICES: "Diagnostic & service call · 1 × $89.00" $89.00. MATERIALS: "Dual run capacitor (45/5 MFD) · 1 × $185.00" $185.00. Divider row "Subtotal + tax" **$289.26**.
  - **Option card 2** (selected: orange border, light orange tint, radio filled): "New heat pump, 15.2 SEER2" **$10,405.85**. SERVICES: "Heat pump system install · 1 × $2,850.00" $2,850.00. MATERIALS: "3-ton heat pump + air handler, 15.2 SEER2 · 1 × $6,980.00" $6,980.00. "Subtotal + tax" **$10,405.85**.
  - **Option card 3** (top edge only, cut by the screen bottom): "New variable-speed heat pump, 17 SEER2" **$12,827.55**.
- Status bar 8:47. Browser chrome minimal or none.

(Below the fold, not drawn: name field, "I agree that typing my name acts as my electronic signature approving this estimate.", orange "Approve & sign", "Request changes instead", "Decline this estimate", "Download estimate (PDF)", "Thank you, Hannah.")

### Screen 6. The 2 AM call and the texts after it, phone 390x844
Job: one thread shows the AI receptionist booking Gloria's no-heat call at 2:14 AM, the confirmation, her reply and the on-my-way text. Kit: Inbox conversation (`livewire/comms/hub.blade.php` + `comms/_timeline.blade.php`), on Brandi's phone at 12:43 PM.

- **Header (white card top):** "← Inbox"; **Gloria Banks** / "(469) 555-0182"; round emerald-tint call button at right.
- **Action pills row:** "+ Book job", "Assign to me", "View client".
- **Thread (top to bottom):**
  - Centered emerald-tint pill: "↙ Incoming call · 3:41 · 2:14 AM" with a small play button.
  - Small card under it: sparkles icon + "AI SUMMARY" label, text: "Gloria Banks, 2208 Hollyberry Ln, McKinney. Furnace stopped overnight, no heat upstairs or down. Booked no-heat service for Wed, Nov 25, 1:00–3:00 PM."
  - Outgoing bubble (right, emerald gradient, white text), time "8:02 AM": "Hi Gloria, this is Prairie Air & Heat. Your appointment is confirmed for Wednesday, Nov 25, 1:00 PM – 3:00 PM at 2208 Hollyberry Ln, McKinney, TX 75071. Your technician is Kyle. Need to reschedule? Just reply to this text."
  - Incoming bubble (left, light grey), "8:05 AM": "Thank you! Side gate is unlocked, the unit is in the attic."
  - Outgoing bubble, "12:41 PM": "Hi Gloria, this is Prairie Air & Heat. Your technician is on the way and will be there shortly."
- **Composer:** textarea "Text back…" + emerald "Send".
- **Tab bar:** Today, Schedule, **Inbox** (active), Jobs, More.
- Status bar 12:43.

---

## 5. How it uses the bones

| Screen | Shared records read |
|---|---|
| 1 Owner Today | Visit, Customer, Work item (job status), Money (collected, owed, tips, invoices), Conversation (needs reply), Deal (signed estimates), Team |
| 2 Dispatch board | Visit, Team, Customer (name, address), Work item (field status), Automation (tell-the-customer text) |
| 3 Tech get paid | Work item (line items), Money (payment, tip), Customer, Team |
| 4 Estimates chase list | Deal, Customer, Conversation (last contact), Money (totals) |
| 5 Homeowner estimate | Customer view, Deal (options), Customer |
| 6 Call and texts | Conversation (call + AI summary + texts), Automation (confirmation, on-my-way), Visit, Team |

---

## 6. Watch-outs

1. **Cast clash to decide.** The industry page tells the story of "Marcus", owner of **Ridgeline Comfort & Repair**. The homepage screens use **Prairie Air & Heat**, with a *technician* named **Marcus Reed**. I kept Prairie (ties to the homepage) and kept Marcus Reed as a tech, but on this page a tech named Marcus sitting next to an owner named Marcus could confuse a reader. Pick one: rename the page character, rename the tech (e.g. "Mason Reed" on these 6 screens only), or switch these screens to Ridgeline.
2. **E-signature vs BONES.** BONES bans e-signature, but FieldPro's estimate approval *is* a typed-name signature ("Approve & sign", and "Signed, not scheduled" already shows on the homepage). Screen 5 is drawn above that block so no signature UI shows. If Taylor wants the approve button visible, it has to say "Approve & sign" to match the app.
3. **Em dashes in real app text.** FieldPro's estimate/invoice texts ("is ready [dash] review and approve it here") and the options card ("when approving [dash] the chosen tier") use an em dash. None of those strings are on these screens. If one gets added, use a colon instead.
4. **App bug the samples must not copy.** The Client Hub's thank-you footer is hardcoded to "Thanks for trusting us with your garage door." (`components/hub/doc.blade.php`). That's wrong for HVAC. It's below the fold on screen 5, but don't draw it; it needs a fix in FieldPro and Contractor Pro.
5. **AI summary in the thread.** FieldPro's conversation timeline shows the call as a pill. The "AI summary" card comes from the app's call-recording component (`components/comms/recording.blade.php`), which isn't shown inline in the timeline today. Use the same styling. If strict app parity matters more, drop the card and keep the pill.
6. **Leave out things that aren't in the plan list:** no live GPS map or ETA countdown (on-my-way is a text), no financing / "pay over time" (FieldPro has it, but it's not a Signature feature), no maintenance-plan or membership screens, no inventory counts, no payroll runs. Payroll and Cash show only as owner sidebar labels, the same as the homepage. Never open them.
7. **Card processor name.** The real pay sheet has a line naming the processor ("Opens Helcim's secure window…"). Leave it off screen 3.
8. **Tone and safety.** No gas leak, carbon monoxide, fire or "unsafe" wording. No-heat is as serious as it gets. Keep amounts plausible for DFW: Texas 8.25% tax on materials only, matching the app's "SERVICES · no tax". Estimate numbers (#EST-…) appear only on staff screens, never on the homeowner's page.
9. **Keep from the real kit:** status words (Scheduled / On my way / Working / Done), "Unassigned (N)" in red, the "Xh Ym free" gap labels, "Tell the customer", "Waiting N days · Last contact …", the Services/Materials grouping, "Subtotal + tax", "Add a tip · 100% to the tech", tip presets 10/20/30%, "Charge card · $X", and the owner's 5 KPI tiles in their order.
