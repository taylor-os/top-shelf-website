"""Every decision for the CRM + website focus, in one place.

Spec: docs/superpowers/specs/2026-11-21-crm-website-focus-design.md
REMOVED is a literal list (taken from origin/main 1a615bb) so it still names the
pages after they are deleted.
"""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXCLUDE_DIRS = ("demo", "websites", "preview", "node_modules", ".git")

# removed page -> where its 301 points
REMOVED = {
    "marketing-for-appliance-repair.html": "for-appliance-repair.html",
    "marketing-for-auto-body-shops.html": "for-auto-body-shops.html",
    "marketing-for-auto-detailers.html": "for-auto-detailers.html",
    "marketing-for-auto-repair-shops.html": "for-auto-repair-shops.html",
    "marketing-for-bankruptcy-attorneys.html": "for-bankruptcy-attorneys.html",
    "marketing-for-barbershops.html": "for-barbershops.html",
    "marketing-for-chiropractors.html": "for-chiropractors.html",
    "marketing-for-commercial-real-estate.html": "for-commercial-real-estate.html",
    "marketing-for-criminal-defense-lawyers.html": "for-criminal-defense-lawyers.html",
    "marketing-for-day-spas.html": "for-day-spas.html",
    "marketing-for-dentists.html": "for-dentists.html",
    "marketing-for-dermatologists.html": "for-dermatologists.html",
    "marketing-for-electricians.html": "for-electricians.html",
    "marketing-for-estate-planning-attorneys.html": "for-estate-planning-attorneys.html",
    "marketing-for-family-law-attorneys.html": "for-family-law-attorneys.html",
    "marketing-for-fence-companies.html": "for-fence-companies.html",
    "marketing-for-flooring-companies.html": "for-flooring-companies.html",
    "marketing-for-foundation-repair.html": "for-foundation-repair.html",
    "marketing-for-garage-door-companies.html": "for-garage-door-companies.html",
    "marketing-for-general-contractors.html": "for-general-contractors.html",
    "marketing-for-gyms.html": "for-gyms.html",
    "marketing-for-hair-salons.html": "for-hair-salons.html",
    "marketing-for-handyman-services.html": "for-handyman-services.html",
    "marketing-for-home-inspectors.html": "for-home-inspectors.html",
    "marketing-for-house-cleaning-companies.html": "for-house-cleaning-companies.html",
    "marketing-for-hvac-companies.html": "for-hvac-companies.html",
    "marketing-for-immigration-lawyers.html": "for-immigration-lawyers.html",
    "marketing-for-junk-removal.html": "for-junk-removal.html",
    "marketing-for-landscapers.html": "for-landscapers.html",
    "marketing-for-locksmiths.html": "for-locksmiths.html",
    "marketing-for-massage-therapists.html": "for-massage-therapists.html",
    "marketing-for-med-spas.html": "for-med-spas.html",
    "marketing-for-mobile-mechanics.html": "for-mobile-mechanics.html",
    "marketing-for-mortgage-brokers.html": "for-mortgage-brokers.html",
    "marketing-for-movers.html": "for-movers.html",
    "marketing-for-nail-salons.html": "for-nail-salons.html",
    "marketing-for-optometrists.html": "for-optometrists.html",
    "marketing-for-orthodontists.html": "for-orthodontists.html",
    "marketing-for-painters.html": "for-painters.html",
    "marketing-for-personal-injury-lawyers.html": "for-personal-injury-lawyers.html",
    "marketing-for-personal-trainers.html": "for-personal-trainers.html",
    "marketing-for-pest-control-companies.html": "for-pest-control-companies.html",
    "marketing-for-physical-therapists.html": "for-physical-therapists.html",
    "marketing-for-plumbers.html": "for-plumbers.html",
    "marketing-for-pool-service.html": "for-pool-service.html",
    "marketing-for-pressure-washing.html": "for-pressure-washing.html",
    "marketing-for-property-management.html": "for-property-management.html",
    "marketing-for-real-estate-agents.html": "for-real-estate-agents.html",
    "marketing-for-roofers.html": "for-roofers.html",
    "marketing-for-solar-installers.html": "for-solar-installers.html",
    "marketing-for-tire-shops.html": "for-tire-shops.html",
    "marketing-for-transmission-shops.html": "for-transmission-shops.html",
    "marketing-for-tree-services.html": "for-tree-services.html",
    "marketing-for-urgent-care.html": "for-urgent-care.html",
    "marketing-for-veterinary-clinics.html": "for-veterinary-clinics.html",
    "marketing-for-window-cleaning.html": "for-window-cleaning.html",
    "marketing-for-yoga-studios.html": "for-yoga-studios.html",
    "get-found-package.html": "pricing.html#website",
    "get-found-plus.html": "pricing.html#website",
    "custom-5-page-website.html": "pricing.html#website",
    "one-page-website.html": "pricing.html#website",
    "take-back-your-website.html": "pricing.html#website",
    "one-time-services.html": "pricing.html",
    "get-found-listing-reviews.html": "pricing.html",
    "google-business-profile-fix.html": "pricing.html",
    "map-pack-push.html": "pricing.html",
    "review-reply-catch-up.html": "pricing.html",
    "sample-report.html": "pricing.html",
    "sample-seo-report.pdf": "pricing.html",
    "solution-marketing.html": "solution-crm.html",
    "solution-pos.html": "solution-crm.html",
    "solution-memberships.html": "solution-crm.html",
    "answers-marketing.html": "answers-crm.html",
}

# Old Top Shelf prices. $3,390 / $452 / $678 stay legal: they are the
# hire-it-yourself figures in the comparison table, not our prices.
OLD_PRICE_RE = re.compile(r"\$(299|899|2,500|599|795|1,995|345|1,250|1,500|495|150|325|95|1,695|6,215|8,475)\b")
OLD_NAME_RE = re.compile(r"\b(Essentials|Platinum|Get Found|One-Time Services|Free Audit|[A-Z]\w* Blend)\b")

NEW_SOLUTIONS = [
    ("solution-crm.html", "CRM & Follow-Up"),
    ("solution-ai-phone.html", "AI Phone & Chat"),
    ("solution-reviews.html", "Reviews"),
    ("solution-booking.html", "Online Booking"),
    ("solution-payments.html", "Payments"),
    ("solution-automation.html", "AI & Automation"),
    ("solution-websites-seo.html", "Websites"),
]
CTA_LABEL = "Try the CRM"
CTA_HREF = "contact.html"
ALLOWED_PRICES = {"$99", "$199", "$50", "$499"}

# Exact sentences where an old-price number is not a Top Shelf price.
# Each entry is a deliberate call made in Task 4.
ALLOWED_CONTEXTS = []


def site_pages():
    return sorted(glob.glob(os.path.join(ROOT, "*.html")))


def source_files():
    here = os.path.join(ROOT, "scripts")
    return sorted(p for p in glob.glob(os.path.join(here, "*.py"))
                  if not os.path.basename(p).startswith("focus_"))
