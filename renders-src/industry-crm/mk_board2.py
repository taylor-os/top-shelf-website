"""Review board v2: 11 industries x 6 screens, each built around its own roles."""
import shutil, pathlib, html, json
S = pathlib.Path(__file__).parent
V = S / "industry-v2" / "screens"
B = S / "board"
shutil.rmtree(B, ignore_errors=True)
(B / "img").mkdir(parents=True)
IND = [
 ("home-services", "Home Services", "Prairie Air & Heat · Allen", "Built around the dispatch board, getting paid at the door, and good/better/best estimates the homeowner picks from.", [
  ("Owner · Today", "The owner's morning: jobs, money, and the 2 AM no-heat call still waiting for a tech."),
  ("Dispatcher · Day board", "One row per tech, the unassigned tray, free gaps between stops, and a moved visit with \"tell the customer?\"."),
  ("Technician · Get paid", "Paid at the front door: card, a tip that goes to the tech, tax on materials only."),
  ("Owner · Estimates waiting", "Estimates going cold, with who to call and when they were last contacted."),
  ("Homeowner · Estimate", "The company's own estimate page: repair or replace as good, better, best."),
  ("Inbox · 2 AM call", "The AI receptionist booked a no-heat call overnight, then the confirmation and on-my-way texts.")]),
 ("car-lots", "Car Lots", "Bramlett Motor Co. · Garland", "Built around the car, the deal and the in-house loan: money in today, what's owed, and deals not finished.", [
  ("Owner · Home", "The lot's day: loan and down payments in, what's past due, cars by stage, sold deals still needing paperwork."),
  ("Owner · Deal jacket", "One deal from car to title: how they pay, the trade, the payment grid, the figures."),
  ("Finance · Collections", "Past-due loans sorted by missed promises and promises due today, with pay links and a contact log."),
  ("Salesperson · My day", "New leads to take, test drives, find a car. No cost or gross on the salesperson's screen."),
  ("Buyer · Car payment", "The lot's own pay page: first name, amount due, pay by card."),
  ("Texts · After-hours call", "The AI receptionist answered an 8:47 pm call and booked a test drive, then one confirmation text.")]),
 ("auto-repair", "Auto Repair", "Turnbuckle Auto Repair · Garland", "Built around the shop board and the repair order the customer approves job by job from a text.", [
  ("Owner · Service today", "Who to call: ready for pickup, money owed, waiting on an OK, and declined work to follow up."),
  ("Advisor · Shop board", "Cars by stage, rush flags, ready-by times, waiting on parts, the tech's clock."),
  ("Advisor · Repair order", "The concern, each job with labor and parts, photos, and approved / not answered / declined."),
  ("Technician · My jobs", "A big job clock, add photo, notes, waiting on parts. No prices or customer names."),
  ("Car owner · Estimate", "Approve or decline each job from a texted link, with photos of their own worn parts."),
  ("Advisor · Stranded driver", "The AI receptionist answered a driver whose car died and booked her drop-off.")]),
 ("auto-detailing", "Auto Detailing", "Kestrel Lane Detail Co. · Rowlett", "Built around packages priced by vehicle size, deposits, add-ons the customer approves, and no-shows.", [
  ("Owner · Home", "Deposits held, money in, cars ready for pickup, add-ons waiting on the customer, detailer load."),
  ("Owner · Work order", "The Tahoe's work order: size price, deposit applied, a pet-hair add-on waiting on an OK, check-in photos."),
  ("Front desk · Calendars", "Did they come? The no-show step that keeps the deposit, plus check-ins and pickups."),
  ("Detailer · My jobs", "Start/stop clock, photos, and an add-on locked until the customer says yes."),
  ("Customer · Booking", "The shop's booking page: the price for her vehicle size, add-ons, and the deposit due now."),
  ("Texts · Add-on approval", "Booked by the AI receptionist, the add-on approved by text, then the ready text with a pay link.")]),
 ("real-estate", "Real Estate", "Elena Marsh Real Estate · Cedar Ridge", "Built around contract deadlines, who to call today, and listings that publish to her website.", [
  ("Agent · Today", "Contract deadlines in the next 48 hours first, then who to call and why, then today's calendar."),
  ("Agent · Listings", "Each listing's MLS status next to what her website shows; a price change already live."),
  ("Coordinator · Deal", "The TREC contract timeline: option period, earnest money, title, lender, each with a phone number."),
  ("Agent · Buyer on the go", "The buyer's pre-approval, wish list, matching homes, and today's showings."),
  ("Buyer · Her website", "The listing page on Elena's own website, with Book a showing."),
  ("Texts · Listing call", "The AI receptionist booked a listing appointment while she was at a showing.")]),
 ("fitness", "Gyms & Fitness", "Larkspur Strength Club · Rowlett", "Built around classes and capacity, check-in, keeping members coming, and membership payments.", [
  ("Owner · Dashboard", "Today's classes and how full, payments to fix, members who haven't been in for two weeks."),
  ("Owner · Classes week", "The class schedule with capacity, waitlists and one class's roster."),
  ("Front desk · Check-in", "Scan or type a member; a past-due member at the counter with collect, let in, or text."),
  ("Coach · Roster", "Here or no-show for the class on now. No billing on the coach's screen."),
  ("Member · Gym app", "The gym's own app: her booked class, spots left today, her check-in code."),
  ("Texts · Intro class", "The AI receptionist booked an intro class from a 9:48 PM call.")]),
 ("salon-spa", "Salon & Spa", "Studio Marlowe Salon & Spa · McKinney", "Built around each person's chair, color processing time, the ticket with tips, and rebooking.", [
  ("Owner · Today", "Every chair's day, open hours, who hasn't confirmed, who's due back, yesterday's day close."),
  ("Owner · Day by chair", "One column per person; another client booked inside a color client's processing time."),
  ("Front desk · Checkout", "The ticket by person, deposit taken off, the tip split by who did what, book next visit."),
  ("Stylist · My day", "The client in the chair with her last formula and photos, and who's next."),
  ("Client · Booking", "The salon's own booking page: pick the person, see the deposit and the 48-hour rule."),
  ("Texts · Rebook", "An after-hours booking, the deposit hold, the reminder, and her \"C\" to confirm.")]),
 ("restaurants", "Restaurants & Bars", "Wrenfield Kitchen & Bar · McKinney", "Built around covers, the floor plan, guest notes and allergies, and private events.", [
  ("Owner · Tonight", "Covers by 15 minutes against the booking limit, and the regulars, occasions and allergies to know."),
  ("Host · Floor plan", "Tables by section: open, reserved, seated, clearing; who's arriving next and the waitlist."),
  ("Events · Pipeline", "Private events from inquiry to final count, with the event sheet and deposits."),
  ("Server · My tables", "Only their own tables, with the anniversary, the regular, and a red allergy band."),
  ("Guest · Reserve", "The restaurant's own reservation page: party size, times, allergy field."),
  ("Inbox · Table for 6", "The AI receptionist took \"table for 6 at 7?\", offered times, and noted a tree nut allergy.")]),
 ("medical-dental", "Medical & Dental", "Alderbrook Family Dental · Little Elm", "Built around the day by chair, confirmations, filling open time, recall, and patient balances. No health details anywhere.", [
  ("Dentist · Today", "Are the chairs full, who hasn't confirmed, new patients booked while you were busy, balances to collect."),
  ("Front desk · Schedule", "The day by operatory, and a cancellation filled from the ASAP list by text."),
  ("Front desk · Counter", "Checkouts, tomorrow's confirmations, and the recall list that books families together."),
  ("Hygienist · My chair", "Book the next cleaning before the patient leaves, then send them to checkout."),
  ("Patient · Family page", "The practice's page: the family's visits, a balance to pay, office details."),
  ("Inbox · Lunch call", "The AI receptionist booked a new patient and her daughter at lunch. Texts never say why anyone is coming in.")]),
 ("legal", "Law Firms", "Holloway & Vane Law · Frisco", "Built around intake speed, conflict checks before consults, the matter pipeline, court dates and retainers. No case facts anywhere.", [
  ("Attorney · Today", "Everything that came in since Friday and how it was handled, plus today's consults and court."),
  ("Attorney · Matters", "Consult booked, retainer sent, active, closed, with one matter's dates and fees open."),
  ("Intake · Desk", "A ringing line, the conflict check, and a new client's consult with the fee paid."),
  ("Attorney · Back from court", "What happened while in court, the next meeting, and a conflict check to clear."),
  ("Client · Firm page", "The firm's own page: next date, the fee and what's left, pay now, the team."),
  ("Texts · 11 PM call", "The AI receptionist screened an 11 PM call, said it can't give legal advice, and booked a consult.")]),
 ("retail", "Retail & Local Shops", "Larkhaven Goods · Grapevine", "Built around regulars, holds and special orders, the want list, and telling people when it's in.", [
  ("Owner · Today", "Holds going home today, items that came in, house accounts, and who to reach out to."),
  ("Owner · Hold shelf", "The hold shelf by cubby: who it's for, what they owe, how long it's held."),
  ("Shop lead · Customer card", "Knowing the customer at the counter: what she loves and the wish list she shared."),
  ("Owner · Want list", "Who asked for what, and one personal text to each person when it comes in."),
  ("Customer · It's in", "The shop's own page: her order is in, on shelf A2, pay now or at pickup."),
  ("Texts · After hours", "The AI receptionist took an after-hours call and never claims stock; the owner texts back in the morning.")]),
]


def card(ind, fn, role, cap):
    rel = f"{ind}/{fn}"
    dst = B / "img" / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(V / ind / fn, dst)
    cls = "ph" if fn.endswith("-m.jpg") else "dk"
    return (f'<figure class="{cls}"><button class="zoom" type="button" data-src="img/{rel}" aria-label="Enlarge {html.escape(role)}">'
            f'<img src="img/{rel}" alt="{html.escape(role + ": " + cap)}" loading="lazy"></button>'
            f'<figcaption><b>{html.escape(role)}</b>{html.escape(cap)}</figcaption></figure>')


secs, jump, files = [], [], []
for slug, name, biz, why, caps in IND:
    fns = sorted(p.name for p in (V / slug).glob("*.jpg"))
    assert len(fns) == 6, slug
    figs = [card(slug, fn, r, c) for fn, (r, c) in zip(fns, caps)]
    files += [f"img/{slug}/{fn}" for fn in fns]
    desk = "".join(f for f in figs if 'class="dk"' in f)
    ph = "".join(f for f in figs if 'class="ph"' in f)
    secs.append(f'<section class="ind" id="{slug}"><header><h3>{name}</h3><span class="co">Sample business: {html.escape(biz)}</span></header>'
                f'<p class="lede">{html.escape(why)}</p><div class="grid">{desk}</div><div class="grid phones">{ph}</div></section>')
    jump.append(f'<a href="#{slug}">{name}</a>')
tpl = (S / "board2_tpl.html").read_text(encoding="utf-8")
(B / "index.html").write_text(tpl.replace("{{JUMP}}", "".join(jump)).replace("{{SECS}}", "".join(secs)), encoding="utf-8")
json.dump({f: f for f in files}, open(S / "board_files.json", "w"))
print("ok", len(files))
