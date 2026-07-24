# assets/build-vault.py — regenerate assets/services-vault.json from the Drive catalog.
# Run: python assets/build-vault.py
import json, re, pathlib

SRC = r"G:/My Drive/Taylor OS/Projects/Top Shelf/Portfolio/service-catalog-data.json"
OUT = pathlib.Path(__file__).with_name("services-vault.json")
STOP = set("the a an and or for of to your you with we our that so more into it is are on in".split())

def kw(*parts):
    words = re.findall(r"[a-z0-9]+", " ".join(p for p in parts if p).lower())
    seen, out = set(), []
    for w in words:
        if len(w) > 2 and w not in STOP and w not in seen:
            seen.add(w); out.append(w)
    return out[:14]

data = json.load(open(SRC, encoding="utf-8"))
services = []
for s in data:
    blurb = " ".join(x for x in [s.get("what_it_is",""), s.get("how_ts_solves",""), s.get("what_it_means","")] if x).strip()
    services.append({
        "name": s["name"],
        "section": s["section"],
        "keywords": kw(s["name"], s["section"], s.get("great_for",""), s.get("what_it_is","")),
        "blurb": blurb,
        "great_for": s.get("great_for",""),
    })
sections = sorted({s["section"] for s in services})
OUT.write_text(json.dumps({"sections": sections, "services": services}, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"wrote {OUT} — {len(services)} services, {len(sections)} sections")
