"""Give each industry its own sample surnames. Keeps the first letter so avatar initials stay right."""
import re, pathlib, collections, sys, json
ROOT = pathlib.Path(__file__).parent / "screens"
ORDER = ["home-services","real-estate","legal","medical-dental","restaurants","retail","salon-spa","fitness","car-lots","auto-repair","auto-detailing"]
KEEP = {"Marsh":"real-estate","Holloway":"legal","Larkspur":"fitness","Kessler":"home-services","Vane":"legal"}
STOP = set("""Today Tomorrow Monday Tuesday Wednesday Thursday Friday Saturday Sunday Mon Tue Wed Thu Fri Sat Sun Sample Call Text Done Open New Book Booked Next Up Ready Waiting Paid Pay The Your Owner Front Desk Card Cash Check Total
Settings Texts More Phone Reviews Talk Inbox Money Payments Setup Customers Office Review Reports Home Grow Reputation Automations Reply Notes Tasks Team Clients Calendar Confirmed Family Messages Website Services Deposit Estate Repairs Help Deals Pipeline Title Sold Financing Inventory Schedule Estimates Active Sent Coming Name Mobile Anniversary Mine Week Last Let Answer Edit Here About All Asked Morning Work Full Add Checked Customer Jobs Google Reschedule Texting Lane Ridge Hollow Bend Prairie Pecan Elm Cedar Trl Realty Kitchen Law Dental Motor Strength Club Goods Studio Salon Spa Detail Auto Repair Air Heat Chevrolet Honda Toyota Nissan Kia Ford Hyundai Subaru Tahoe Odyssey Camry Altima Dec Nov Oct November December Price Bramble Quail Haven Mesquite Clover Larder""".split())
def visible(p):
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"<style.*?</style>|<script.*?</script>", "", t, flags=re.S)
    return re.sub(r"<[^>]+>", " ", t)
texts = {d.name: " ".join(visible(f) for f in d.glob("*.html")) for d in ROOT.iterdir() if d.is_dir()}
last = collections.defaultdict(set); first = collections.defaultdict(set)
for ind, t in texts.items():
    for a, b in re.findall(r"\b([A-Z][a-z]+)\s+([A-Z][a-z]{2,})\b", t):
        if a in STOP or b in STOP: continue
        last[b].add(ind); first[a].add(ind)
allwords = set(re.findall(r"\b[A-Z][a-z]+\b", " ".join(texts.values())))
POOL = {c: [] for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for n in """Abbington Ainsley Ashby Aldridge Ashcroft Babcock Barlow Beckett Blakely Bramwell Burrows Carrow Castell Colfax Crandall Cutler Dalby Darrow Dunmore Delacroix Draper Eastwood Ellery Embry Everly Fairley Farrow Fenwick Foyle Fulbright Galloway Garrity Gilchrist Gorman Greeley Hadley Halverson Harwick Hennessy Hobart Ingram Inman Irving Iverson Jessup Jolley Judson Kearny Kendrick Kilgore Kimball Kirkland Langford Larrabee Lindell Lockridge Lowell Maddox Marlow Mayhew Merriman Mulligan Nash Nesbitt Norcross Northam Nyland Oakes Odell Ogilvie Orwell Osgood Padgett Pembrook Pettis Prescott Pryor Quaid Quarles Quill Quimby Quintero Radcliffe Ramsdell Redding Rowley Rutledge Salter Sexton Shelby Stroud Sutter Tabor Talley Thorne Tolliver Truitt Upton Usher Underhill Vail Varner Vaughn Voss Vickers Wadley Warrick Weldon Winslow Wexford Yancey Yardley Yates Zeller Zimmer Zavala Keane Kirby Lassiter Holcomb Hensley Gentry Beaumont Ellison Paxton Pendleton Purcell Pickett Poindexter Platt Penrose Wakefield Wheatley Winfield Wilder Woodall Worley Ralston Rennick Rigsby Royce Rosenthal Oldham Ormsby Overton Mabry Mercer Merritt Morland Mosley Dempsey Dorsett Tillman Trent Tuttle Vinson Valentine Varney Benton Bradshaw Galvin Greenway Gladwell Hargrove Hutchins Ingle Nolan Newcomb Kittredge Kesterson Brightman Buckley Crowell Cooksey Chandler Seaver Sinclair Strickland Lyle Leland Locke Feld Fenn Quayle Quentin Graves Osborne Oxley Otis Orr Paley Prater Pope Penn Pullman Parrish Lyndale Linwood Lorimer""".split():
    if n not in allwords: POOL[n[0]].append(n)
SURNAMES = """Pruitt Whitfield Lindqvist Okafor Pike Ochoa Ruiz Delgado Marsh Reyes Monroe Tran Ortiz Vega Holloway Brandt Whitaker Lowry Pratt Whitlock Vance Bell Calder Navarro Garza Kessler Whitley Greer Ibarra Holt Brooks Brennan Doyle Bishop Mendez Natarajan Moreno Oyelaran Quinn Fox Shore Shaw Callahan Raman Cho Larkspur Burkhart""".split()
def where(w): return sorted([i for i,t in texts.items() if re.search(r"\b%s\b" % w, t)], key=ORDER.index)
plan = collections.defaultdict(dict)  # ind -> {old: new}
for w in SURNAMES:
    users = where(w)
    if len(users) < 2: continue
    keeper = KEEP.get(w, users[0])
    for ind in users:
        if ind == keeper: continue
        if not POOL[w[0]]: print("POOL EMPTY", w); continue
        plan[ind][w] = POOL[w[0]].pop(0)
print(json.dumps(plan, indent=1))
if "--apply" in sys.argv:
    for ind, m in plan.items():
        for f in (ROOT / ind).glob("*.html"):
            s = f.read_text(encoding="utf-8"); o = s
            for old, new in m.items():
                s = re.sub(r"\b%s(?=s?\b|'s\b)" % old, new, s)
            if s != o: f.write_text(s, encoding="utf-8"); print("changed", f)
