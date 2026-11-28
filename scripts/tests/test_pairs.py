"""Pairs registry and shared site content checks."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAIRS = ROOT / "renders-src" / "industry-crm" / "pairs.json"
CONTENT = ROOT / "renders-src" / "site-content" / "content.json"


def test_pairs_registry():
    pairs = json.loads(PAIRS.read_text(encoding="utf-8"))
    assert len(pairs) == 12
    slugs = [p["slug"] for p in pairs]
    assert len(set(slugs)) == 12
    for p in pairs:
        # The vet CRM set is built in Task 2, so its folder may not exist yet.
        assert p["slug"] == "vet" or (ROOT / p["crm_dir"]).is_dir(), p["crm_dir"]
        if not p.get("new_website"):
            assert (ROOT / p["website_dir"] / "index.html").is_file(), p["website_dir"]


def test_content_prices():
    text = CONTENT.read_text(encoding="utf-8")
    for price in ["$99", "$199", "$50", "$499"]:
        assert price in text, price
    for banned in ["$299", "$899", "$2,500", "$1,500", "$495", "Essentials",
                   "Platinum", "free audit", "Local SEO"]:
        assert banned.lower() not in text.lower(), banned


def test_content_no_em_dash():
    assert "—" not in CONTENT.read_text(encoding="utf-8")
