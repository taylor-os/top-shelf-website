"""
expire_samples.py — archive sample-site folders past their 30-day expiry.

Usage (CLI):
    python scripts/expire_samples.py 2026-08-28

    Reads demo/manifest.json, moves expired slug folders to demo/_archive/<slug>/,
    removes those slugs from the manifest, and writes the manifest back.
    Prints the list of archived slugs.

Public API:
    expire(demo_dir: str, today_iso: str) -> list[str]
        demo_dir  — path to the demo/ folder (absolute or relative)
        today_iso — ISO date string (YYYY-MM-DD) to compare against expires dates
        Returns the list of slugs that were archived.
"""

import json
import os
import shutil
import sys
from datetime import date


def expire(demo_dir: str, today_iso: str) -> list:
    """
    Archive sample folders whose expires date is earlier than today_iso.

    - Reads <demo_dir>/manifest.json
    - For each slug where entry["expires"] < today_iso AND <demo_dir>/<slug>/ exists:
        * Moves the folder to <demo_dir>/_archive/<slug>/
        * Removes the slug from the manifest
    - Writes the updated manifest back to disk
    - Returns the list of archived slug names
    """
    today = date.fromisoformat(today_iso)
    manifest_path = os.path.join(demo_dir, "manifest.json")
    archive_dir = os.path.join(demo_dir, "_archive")

    # Load manifest (empty dict if file is missing or blank)
    if os.path.isfile(manifest_path):
        with open(manifest_path, "r", encoding="utf-8") as fh:
            manifest = json.load(fh) or {}
    else:
        manifest = {}

    archived = []
    for slug, entry in list(manifest.items()):
        expires_str = entry.get("expires", "")
        if not expires_str:
            continue
        if date.fromisoformat(expires_str) < today:
            slug_dir = os.path.join(demo_dir, slug)
            if os.path.isdir(slug_dir):
                os.makedirs(archive_dir, exist_ok=True)
                dest = os.path.join(archive_dir, slug)
                shutil.move(slug_dir, dest)
                archived.append(slug)
                del manifest[slug]

    # Write manifest back even if nothing expired (keeps it tidy)
    with open(manifest_path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2)

    return archived


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python expire_samples.py <YYYY-MM-DD>", file=sys.stderr)
        sys.exit(1)
    today_arg = sys.argv[1]
    expired = expire("demo", today_arg)
    if expired:
        print(f"Archived {len(expired)} sample(s): {', '.join(expired)}")
    else:
        print("No samples expired.")
