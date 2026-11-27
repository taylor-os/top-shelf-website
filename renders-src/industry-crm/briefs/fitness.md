# Fitness: screen brief (gyms and fitness studios)

Sources read: BONES.md, `industry-salon-spa-fitness.html` (gym half: members fading by month three, after-hours calls, review requests), the real Fitness Suite in `top-shelf-crm` (FitnessSuite.php, FitnessDemo.php, app-sidebar.tsx, gym-tabs.ts, gym/dashboard.tsx, classes/week.tsx + session.tsx, GymDashboard.php payment lines, BillingNotices.php texts, F3a/F3b ledgers and decisions, the Nov 8 owner and front desk tester reviews), Repkin README and docs, and the 5 current drafts (dark gold, Iron Bayou, workout logging and floor map front and center: do not repeat).

Sample date and time for the whole set: **Tuesday, Dec 1, 2026**, early morning. Every screen carries the bottom strip "Sample screens · sample data, not a real business".

---

## 1. Business and cast

**Larkspur Strength Club**, Rowlett, TX. One location (4410 Bayside Commons Dr, Rowlett, TX 75088, made up). Group classes plus open gym, about 410 members, 9 staff. Open 5:00 AM to 10:00 PM weekdays, front desk staffed 6:00 AM to 9:00 PM. Phone (469) 555-0110.

Plans (follow the real kit's shape: name, monthly price, sign-up fee):
- **Monthly** (open gym): $59/mo, $25 sign-up fee
- **Unlimited classes**: $119/mo, no sign-up fee, 30 days' notice to cancel

Class types (capacity): Strength & Conditioning (16), HIIT 45 (16), Barbell Club (12), Mobility (20), Intro / Foundations (8; real kit's name for the first-timer class).

Staff who appear:
- **Graham Pruitt**, owner
- **Tessa Villanueva**, front desk
- **Malik Odom**, head coach (also teaches Intro / Foundations)
- **Dez Fuller** and **Erin Sato**, coaches (names only, on the schedule)
- **Hannah Strickland**, personal trainer (named only in the nav/role notes, no screen)

Members and leads who appear:
- **Deja Monroe**: Unlimited classes, uses the member app, booked into tonight's 5:30 PM
- **Brianna Holt**: Monthly, past due ($59.00), walks in at the desk at 7:04 AM
- **Luis Cardenas**: Unlimited classes, card declined once, retrying Dec 4
- **Omar Haddad**: Monthly, card declined once, retrying Dec 3
- **Rosa Delgado**: moved up from the 5:30 PM waitlist last night
- **Ethan Kowalski**, **Lindsey Brandt**, **Tre Washington**: haven't been in for 2+ weeks (the check-in list)
- **Caleb Whitaker**, **Priscilla Nguyen**, **Marisol Vega** (her first class today): in the 6:30 AM class
- **Jasmine Pham**: new lead, called at 9:48 PM, AI receptionist booked her Intro / Foundations

All names are fictional. Avoid the real demo's names (Iron Bayou, Dana Whitfield, Marcus Lee, Priya Shah, Jordan Reyes, Sam Ortiz, Kelsey Tran, Alicia Moreau, Maria Garcia, Kevin Perez). A web check found no "Larkspur Strength" gym in Texas.

---

## 2. Roles and what they need first

**Owner (Graham), desktop, 7:00 AM with coffee**
1. Today's classes: how full each one is, which are full with a waitlist, any class with no coach.
2. Money problems: whose card declined, who's past due, how much is owed. (The real dashboard's "Payments · whole gym" card.)
3. Members slipping away: who hasn't checked in for two weeks, so someone texts them before they cancel.
4. What came in overnight: calls the AI receptionist answered, intro classes it booked, missed calls it texted back.
5. Reviews: rating, new ones, any waiting on a reply.
Trust: the class counts and the declined cards are real and current, with a name he can tap. Dismiss: revenue charts, "leads pipeline" stages, or anything that says job/customer/invoice. He runs a gym, not a sales floor.

**Front desk (Tessa), desktop at the counter, phone ringing, line of people**
1. Check someone in fast: scan the code or type two letters of a name.
2. The member's status on that one card: paid through when, or past due and how much.
3. What to do about a problem without holding up the line: collect at the desk, let in anyway, text later.
4. Who's in the next class and whether it's full (people ask at the counter).
5. Today's first-timers, so she can greet them by name.
Trust: check-in is one action and Undo is right there. Dismiss: making her click through a member profile to see if they've paid.

**Coach (Malik), phone in hand on the floor, class on now**
1. Their classes today, the one on now at the top.
2. The roster: who's booked, tap Here or No-show.
3. Who's new today (greet them, watch their form).
4. Waitlist: let someone in when a booked member doesn't show.
5. Reach a member (text) without going to the desk.
Trust: big tap targets, one tap per person. Dismiss: any billing on his screen. In the real kit coaches never see billing, and they shouldn't here either.

**Member (Deja), phone, before work**
1. Her next class: booked, when, which coach.
2. Spots left in today's classes, and book one in one tap.
3. Her check-in code for the desk.
4. Her membership: paid through when.
5. A text when something changes (booking confirmed, card declined, class cancelled).
Trust: it's her gym's name and logo, and "5 spots left" is true. Dismiss: being sold to, or a generic booking widget that could be any business.

---

## 3. Words

| Bone | Fitness word (real kit) |
|---|---|
| Customer | **Member** (before joining: **Lead**). A trainer may say "my clients" (real dashboard: "Your clients") for PT only. |
| Visit | **Class** (a class session at a time with a coach and a capacity), a member's **booking** ("Booked", "Waitlist"), a **check-in**, a **PT session** |
| Deal | **Lead** to **membership started** (the real kit turns the Pipeline page off for gyms, so no stage board) |
| Work item | The class **roster** with attendance (**Here** / **No-show**) |
| Money | **Membership** on a **plan**, **monthly charge**, **sign-up fee**, **card on file**, states **Paid through**, **Retrying**, **Past due**, **Collect** (at the desk), **receipt** |
| Conversation | **Texts** (calls with AI receptionist summaries land in the same thread), **Inbox** |
| Automation | booking confirmation, class reminder, card declined / past due texts, check-in-with-them reminders, review request |
| Team | **Owner, Manager, Front desk, Coach, Trainer** (real gym roles) |
| Customer view | the **member app** (Repkin, wearing the gym's name and logo), texts |
| Website link | website "Try a class" / "Book a class" feeds the same schedule; the AI chatbot on the site books intros |

**Nav, owner (desktop sidebar), in this order.** Work: Dashboard, Members, Check-in, Classes, Personal training, Texts, Inbox, Leads, Tasks. Money: Plans. Grow: Reputation. Setup: Settings. (Real gym order puts Money right after Work; group labels "Work", "Money", "Grow", "Setup".)

**Nav, front desk (desktop sidebar).** Work: Dashboard, Members, Check-in, Classes, Personal training, Texts, Inbox, Leads, Tasks. Grow: Reputation. (No Plans, no Settings.)

**Nav, coach (phone bottom bar, real default when the floor map is off).** Classes, Members, Texts, More.

**Nav, member app (Repkin bottom bar, real).** Today, Train, Start (round + button), Classes, You.

**Words that must NOT appear:** job, work order, dispatch, technician, route, on my way, estimate, quote, invoice (for dues), deal, pipeline, opportunity, customer, patient, guest, client (except a trainer's PT clients), appointment (say class or session), service call, chair, stylist, ticket, tab, subscription (say membership), "CrossFit" (trademark; this gym is not an affiliate), WOD.

---

## 4. The 6 screens

Kit: emerald sidebar, emerald header band on desktop, light canvas, white cards, the homepage CRM type, chips and buttons. Tags in the real kit's words: "On now", "Ended", "Full", "No coach", "Here", "No-show".

### Screen 1. Owner home ("Dashboard"), desktop 1440x900
Job: Graham sees today's classes, the money to fix and the members to win back before 7:30.

- **Sidebar (left, 248 px, emerald):** top: logo chip "LS", "Larkspur Strength Club", under it "Graham Pruitt · Owner". Owner nav from section 3, Dashboard active. Badges: Texts "2", Tasks "3". Bottom: avatar "GP Graham Pruitt".
- **Header band (emerald, 64 px):** left "Dashboard". Right: search field "Search members…", bell.
- **Title row:** H1 "Larkspur Strength Club" (serif like the real dashboard). Sub line "412 members · 6 new this week" ("6 new this week" in emerald). Right side: "Tuesday, Dec 1".
- **Tile strip (4 small white tiles, one row):**
  1. "Booked today" · **88 of 120 spots** · "8 classes"
  2. "Checked in so far" · **41** · "since 5:00 AM"
  3. "Overnight calls" · **4** · "AI receptionist booked 2"
  4. "Reviews" · **4.8 ★** · "3 new this week · 1 to reply"
- **Left column (about 58%): card "Today"**, link "All classes" top right. Rows (time bold, class type bold, tag, then grey line "Coach · booked of capacity", chevron right):
  - 5:30 AM Strength & Conditioning · tag "Ended" · Malik Odom · 14 of 16
  - 6:30 AM Strength & Conditioning · tag "On now" (emerald) · tag "Full" (amber) · Malik Odom · 16 of 16
  - 9:00 AM Mobility · Erin Sato · 7 of 20
  - 12:00 PM HIIT 45 · Erin Sato · 11 of 16
  - 4:30 PM Barbell Club · Malik Odom · 9 of 12
  - 5:30 PM Strength & Conditioning · tag "Full" · Dez Fuller · 16 of 16 · 3 waiting
  - 6:30 PM HIIT 45 · Dez Fuller · 12 of 16
  - 7:30 PM Intro / Foundations · Malik Odom · 3 of 8 · small grey "3 first-timers"
  Each row has a thin capacity bar under the count (emerald, amber when full).
- **Right column (about 42%), three stacked cards:**
  1. **"Payments · whole gym"** (real card). Header right link: "2 retrying · 1 past due". Lines (icon, text, grey sub line "date, time", chevron):
     - red icon: "Brianna Holt is past due: their card was declined three times and we've stopped trying. They owe $59.00. Update the card to retry." · "Nov 29, 6:01 AM"
     - amber icon: "Luis Cardenas's card was declined. We'll try again on Dec 4." · "Nov 30, 6:02 AM"
     - amber icon: "Omar Haddad's card was declined. We'll try again on Dec 3." · "Nov 30, 6:02 AM"
  2. **"Check in with them"** (follow-up reminders). Sub line "Haven't been in for 14 days or more". Rows with a "Text" button each:
     - Ethan Kowalski · Unlimited classes · last in Nov 14
     - Lindsey Brandt · Monthly · last in Nov 12
     - Tre Washington · Unlimited classes · joined Oct 20 · 3 visits
     Footer link: "5 follow-up reminders due this week".
  3. **"Overnight"** (calls and texts). Rows:
     - phone icon · "9:48 PM · Jasmine Pham · AI receptionist booked Intro / Foundations, Sat 9:00 AM"
     - phone-missed icon · "10:21 PM · (469) 555-0143 · missed call, texted back"
     - chat icon · "5:52 AM · Caleb Whitaker · "Running 5 min late to 6:30, still coming""

### Screen 2. Signature: "Classes" week with capacity, desktop 1440x900
Job: the week's schedule at a glance (who's full, who's waiting, which class needs a coach), and one class's roster without leaving the page.

- **Sidebar:** owner nav, Classes active. **Header band:** "Classes".
- **Title row:** H1 "Classes", sub "The week at Larkspur Strength Club." Right: week switcher "‹ Nov 30 - Dec 6 ›", buttons "Class types" (outline) and "Set the schedule" (emerald).
- **Week grid (left ~70%):** 7 columns Mon 30 to Sun 6, Tue 1 column tinted pale emerald with "Today" label. Rows by time, 5:30 AM to 7:30 PM. Each class is a small card: time + type on line 1, coach on line 2, "14 of 16" + a capacity bar on line 3. Tags inside cards: "Full" (amber), "3 waiting" (amber text), "Ended"/"On now" for today's earlier ones, one card with tag "No coach" (amber outline) on **Sat 6, 8:00 AM Barbell Club** (real kit flags it; one is believable, not alarming). Weekend has fewer classes: Sat 8:00 AM Barbell Club, 9:00 AM Intro / Foundations (Jasmine's, "4 of 8"), 10:00 AM Strength & Conditioning; Sun 9:00 AM Mobility only. Weekday pattern: 5:30 AM S&C, 6:30 AM S&C, 9:00 AM Mobility (Tue/Thu) or HIIT 45 (Mon/Wed/Fri), 12:00 PM HIIT 45, 4:30 PM Barbell Club, 5:30 PM S&C, 6:30 PM HIIT 45, 7:30 PM Intro / Foundations (Tue/Thu). Vary the counts (e.g. 9 of 16, 12 of 16, 16 of 16); evenings fuller than midday. The selected card (Tue 5:30 PM S&C) has an emerald outline.
- **Right panel (~30%), the selected class:**
  - Title "Strength & Conditioning", sub "Tue, Dec 1 · 5:30 PM · 60 min · Coach Dez Fuller", tags "Full", "16 of 16".
  - Section **"Booked · 16"**: first 8 names visible with initials avatars, then "+ 8 more": Deja Monroe, Rosa Delgado (small grey "moved up from the waitlist"), Grant Hollis, Ava Brooks, Jerome Tatum, Kira Lindqvist, Sean Mahoney, Bianca Ruiz.
  - Section **"Waitlist · 3"**, numbered: 1 Nate Brennan, 2 Keisha Lowry, 3 Aaron Silva. Grey note under it: "When a booked member cancels, the next person moves up."
  - Small activity line: "Mon 9:12 PM · Josh Fenner cancelled · Rosa Delgado moved up".
  - **"Texts for this class"** box (Automation): "Booking confirmation · on" and "Reminder 2 hours before · on" with toggles.
  - Buttons: "Open roster" (emerald), "Text the class" (outline).

### Screen 3. Front desk "Check-in", desktop 1440x900
Job: Tessa checks members in one after another and handles a past-due member without stopping the line.

- **Sidebar:** front desk nav, Check-in active; bottom "Tessa Villanueva · Front desk".
- **Header band:** "Check-in", search "Search members…".
- **Main (left ~68%):**
  - H1 "Check-in", label "Scan a member's check-in code or type a name". Row: outline button "Scan with camera" (scan icon) + wide focused input "Code or name" (emerald focus ring).
  - **Member card (just scanned, amber left edge):** initials "BH", "Brianna Holt", grey "Monthly · member since Mar 2025", "Last in Sat, Nov 28, 9:04 AM". Red chip "Past due · owes $59.00". Grey line "Card ending 4417 declined three times (Nov 22, 25, 29)." Buttons in a row: "Collect $59.00" (emerald), "Let in anyway" (outline, real kit asks for a reason), "Text her" (outline). Small grey "We texted her on Nov 29 to update her card."
  - **"Checked in today"** list (time, initials, name, chips right, "Undo" link on the newest only):
    - 7:02 AM · Caleb Whitaker · "Paid" · "6:30 AM S&C"
    - 6:58 AM · Priscilla Nguyen · "Paid" · "6:30 AM S&C"
    - 6:55 AM · Luis Cardenas · amber "Retrying card"
    - 6:49 AM · Marisol Vega · "Paid" · emerald "First class"
    - 6:31 AM · Jerome Tatum · "Paid"
    - 6:12 AM · Fatima Siddiqui · "Paid"
- **Right rail (~32%), three cards:**
  1. **"Next class"**: "9:00 AM Mobility · Erin Sato · 7 of 20", link "See roster".
  2. **"First-timers today"**: "Marisol Vega · 6:30 AM S&C · checked in"; "7:30 PM Intro / Foundations: Paige Corbin, Luke Ammons, Rina Desai".
  3. **"Phones"**: "AI receptionist is answering while you're busy" with a green dot; "Today: 2 calls answered, 1 class booked"; link "Open Texts".

### Screen 4. Coach's class roster, phone 390x844
Job: Malik marks who's here in the class that's on now, one tap per person.

- **Header (emerald):** back chevron, "Strength & Conditioning", sub "6:30 AM · On now".
- **Info strip (white card):** "Coach Malik Odom · 60 min", chips "Full", "16 of 16".
- **Note bar (pale emerald):** "First class today: Marisol Vega".
- **"Booked · 16"** list, each row 56 px: initials avatar, name, then two pill buttons "Here" and "No-show" (selected Here = solid emerald with check, selected No-show = solid grey). Visible rows:
  - Caleb Whitaker · Here (selected)
  - Priscilla Nguyen · Here (selected)
  - Luis Cardenas · Here (selected) (no billing badge: coaches never see billing)
  - Marisol Vega · small emerald chip "First class" · Here (selected)
  - Jerome Tatum · Here (selected)
  - Fatima Siddiqui · Here (selected)
  - Kira Lindqvist · Here (selected)
  - Noah Pratt · neither selected
  - Megan Doyle · neither selected
  - (cut off by the bar; list scrolls)
- **Toast floating above the bar:** "Kira Lindqvist marked Here" with "Undo" (real 5-second undo).
- **Bottom bar:** Classes (active), Members, Texts (badge 1), More.

### Screen 5. Member's view: the member app (Repkin) "Today", phone 390x844
Job: Deja sees her booked class, books another, and has her check-in code ready, in her gym's colors.

Styled as the gym, not the staff app: dark canvas (the real member app is dark), gym accent burnt orange #E0702E (modest: buttons and the active tab only). No emerald here.
- **Top:** logo chip "LS" + "Larkspur Strength Club ▾".
- Eyebrow "TODAY", H1 "Good morning, Deja".
- **Card "Your next class":** "TUE 1 DEC" left, chip "Booked" right. Big "5:30 PM", "Strength & Conditioning · 60 min", "Coach Dez", chevron. Text link "Cancel booking". Grey line "We'll text you a reminder at 3:30 PM."
- **Card row "Check-in code":** QR icon, "Show this at the front desk", chevron.
- **Card "Classes today":** rows with time, type, coach, right side spots + button:
  - 9:00 AM Mobility · Coach Erin · "13 spots left" · button "Book"
  - 12:00 PM HIIT 45 · Coach Erin · "5 spots left" · button "Book"
  - 4:30 PM Barbell Club · Coach Malik · "3 spots left" · button "Book"
  - 6:30 PM HIIT 45 · Coach Dez · "4 spots left" · button "Book"
- **Membership line (small, at the bottom of the scroll):** "Unlimited classes · Paid through Dec 14".
- **Bottom bar (real Repkin):** Today (active), Train, Start (round + button, center), Classes, You.

### Screen 6. Text/call moment: AI receptionist books an intro, phone 390x844
Job: show the after-hours call that became a booked first class, and the desk picking up the thread in the morning.

Staff app (emerald), Texts thread as Tessa sees it at 7:12 AM.
- **Header (emerald):** back chevron, "Jasmine Pham", sub "(469) 555-0187", chip "Lead · Intro booked", call icon right.
- **Thread (top to bottom):**
  1. Day divider "Monday, Nov 30".
  2. **Call card** (grey, phone icon): "Call · 9:48 PM · answered by AI receptionist · 2 min". Summary: "Asked about trying a class and what a membership costs. Booked Intro / Foundations, Sat Dec 5, 9:00 AM. Told her Monthly is $59 and Unlimited classes is $119." Link "Play recording".
  3. **Outgoing text (emerald bubble, label "Automatic"), 9:50 PM:** "Larkspur Strength Club: you're booked for Intro / Foundations on Sat, Dec 5 at 9:00 AM with Coach Malik. Wear shoes you can move in and bring water. Reply here if you need to change it."
  4. **Incoming (white bubble), 9:53 PM:** "Perfect. Is there parking?"
  5. Day divider "Today".
  6. **Outgoing (emerald), 7:12 AM, "Tessa":** "Hi Jasmine, it's Tessa at the front desk. Yes, free parking right out front. See you Saturday!"
  7. **Scheduled chip (dashed outline):** "Reminder text · Fri, Dec 4, 9:00 AM".
- **Composer:** field "Text Jasmine…", send button.

---

## 5. How it uses the bones

| Screen | Shared records it reads |
|---|---|
| 1 Owner home | Visit (classes today + capacity), Money (membership charges: declined / past due), Customer (last check-in, follow-up reminders), Conversation (overnight calls/texts), Automation (missed-call text-back), reviews |
| 2 Classes week | Visit (class sessions, capacity, bookings, waitlist), Team (coach), Customer (roster names), Automation (confirmation, reminder) |
| 3 Check-in | Customer, Visit (check-ins, next class), Money (membership state, collect), Conversation (text her), Team |
| 4 Coach roster | Visit (one class session), Work item (attendance), Customer (names, first class) |
| 5 Member app | Customer view (member's bookings, check-in code, membership), Visit, Money (paid through), Automation (reminder) |
| 6 Text thread | Conversation (call + texts), Visit (intro class booking), Customer (lead), Automation (confirmation, reminder) |

---

## 6. Watch-outs

- **No body or health data anywhere.** No weights, body fat, injuries, PRs or workout scores on staff screens (the real demo has a refund reason "knee injury": don't reuse it). Front desk never sees training data in the real kit.
- **Coaches see no billing.** Real rule: coach and trainer logins carry no billing. Screen 4 must show no paid/past-due badges.
- **Past due copy stays neutral**, word for word from the real kit ("…is past due: their card was declined three times and we've stopped trying. They owe $59.00."). Three payment issues out of 412 members, not dozens.
- **No minors.** The real kit has households and teen members (13 to 17); keep every sample member an adult.
- **Not "CrossFit."** The real demo names a class type CrossFit; a fictional unaffiliated gym can't. Use Strength & Conditioning.
- **Real kit to keep:** "Today" card wording and order (Ended / On now / Full / No coach, "X of Y", "N waiting"); "Payments · whole gym" lines; "Booked · N" roster with Here / No-show and 5-second Undo; check-in's "Scan with camera" + "Code or name" and Undo; the waitlist moving up automatically on a cancel; Pipeline off for gyms (so no deal board); Repkin's dark layout, "spots left", and Today / Train / Start / Classes / You bar; the decline text pattern "{gym}: we couldn't charge your card… open Repkin and go to You > Membership."
- **Not in the real Fitness Suite yet, but Signature features:** class reminder texts and the booking confirmation text (real kit: PT reminders are planned for F4, class reminders not built), the "Check in with them" list (real kit records check-ins; the reminder list is the Signature follow-up feature), "Text the class", AI receptionist booking an intro class. Fine to show; Taylor should know they're Signature automations on top of the gym kit.
- **In the real suite but beyond the Signature plan (left out of these screens):** the Floor map with numbered machines, out-of-order flags and member machine reports (plus stickers/NFC and machine cards); Workouts and Exercises (posting the class workout, whiteboard scores, TV display); the member app's training log (Train and Start tabs are drawn as labels only, nothing from them shown); desk Products and Sales (water, bars, tees: a POS register); PT packs and the trainer calendar (nav item only); membership freezes; households and teens; multiple sites with a site switcher and join codes; the Helcim recurring-billing engine itself (shown only as membership charge states). If Taylor sells the Fitness Suite with the gym plan, the Floor map is the strongest alternate for screen 2 or 4.
- Phone numbers: 555 only. No real Rowlett business names.
