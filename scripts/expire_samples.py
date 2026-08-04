"""
expire_samples.py — take down sample-site folders past their expiry date.

The expiry window itself is owned by the skill (ss_build.EXPIRY_DAYS, currently
60 days); this script only reads the `expires` date each build already stamped
into demo/manifest.json.  It never computes an expiry of its own.

What "takedown" means here
--------------------------
The demo folders are served straight off this git repo (Hostinger auto-deploys
on push), so a sample stops being public the moment its folder is no longer at
demo/<slug>/.  Rather than delete, this moves the folder to demo/_archive/<slug>/,
which .htaccess serves as a 404:

    RedirectMatch 404 ^/demo/_archive(/|$)

That removes public access to all three pages at once (hub, website/, audit/)
while keeping the files recoverable.  Nothing is deleted.

Exempting a sample
------------------
Set "keep": true on a manifest entry and the takedown skips it forever, no
matter how far past its expires date it is.  The expiry window exists to stop
sample sites for cold prospects accumulating on the domain indefinitely; a
sample that is deliberately staying up (a signed customer, a demo we point
people at, a favour for a friend) is not that, and should not depend on someone
remembering to intervene before the nightly job runs.  Opting out is a decision
recorded in the manifest, not a race against a cron schedule.

Usage (CLI):
    python scripts/expire_samples.py 2026-08-28              # dry run, default
    python scripts/expire_samples.py 2026-08-28 --apply      # actually take down

    A bare run only reports what WOULD be taken down and touches nothing.
    Pass --apply to move folders and update the manifest.

Public API:
    expire(demo_dir: str, today_iso: str, apply: bool = False) -> list[str]
        demo_dir  — path to the demo/ folder (absolute or relative)
        today_iso — ISO date string (YYYY-MM-DD) to compare against expires dates
        apply     — False (default) reports only; True performs the takedown
        Returns the list of slugs that were (or would be) taken down.
"""

import json
import os
import shutil
import sys
from datetime import date


def expire(demo_dir: str, today_iso: str, apply: bool = False) -> list:
    """
    Take down sample folders whose expires date is earlier than today_iso.

    - Reads <demo_dir>/manifest.json
    - Selects each slug where entry["expires"] < today_iso, the slug is still
      present in the manifest without a taken_down stamp, is not marked
      "keep": true, AND <demo_dir>/<slug>/ exists on disk
    - When apply=True:
        * Moves the folder to <demo_dir>/_archive/<slug>/ (no deletion)
        * Stamps the manifest entry with taken_down = today_iso
        * Writes the manifest back
    - When apply=False (the default) nothing on disk is touched at all
    - Returns the list of slug names taken down, or that would be

    Only slugs listed in the manifest are ever considered, and an entry whose
    expires date has not passed is never selected.  A slug already carrying a
    taken_down stamp is skipped, so re-running is a no-op.  An entry marked
    "keep": true is skipped no matter how old it is, and stays skipped.
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

    taken_down = []
    for slug, entry in list(manifest.items()):
        expires_str = entry.get("expires", "")
        if not expires_str:
            continue
        # Already taken down on an earlier run — leave it alone.
        if entry.get("taken_down"):
            continue
        # Deliberately exempt: staying up regardless of age.
        if entry.get("keep"):
            continue
        if date.fromisoformat(expires_str) >= today:
            continue
        slug_dir = os.path.join(demo_dir, slug)
        if not os.path.isdir(slug_dir):
            continue

        taken_down.append(slug)
        if apply:
            os.makedirs(archive_dir, exist_ok=True)
            dest = os.path.join(archive_dir, slug)
            # A previous archive of the same slug would make shutil.move nest
            # the folder inside it; clear the stale copy first.
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            shutil.move(slug_dir, dest)
            entry["taken_down"] = today_iso

    # A dry run must not touch the manifest either.
    if apply:
        with open(manifest_path, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2)

    return taken_down


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--apply"]
    apply_flag = "--apply" in sys.argv
    if not args:
        print("Usage: python expire_samples.py <YYYY-MM-DD> [--apply]", file=sys.stderr)
        sys.exit(1)
    today_arg = args[0]
    hits = expire("demo", today_arg, apply=apply_flag)
    if not hits:
        print("No samples are past their expiry date.")
    elif apply_flag:
        print(f"Took down {len(hits)} sample(s): {', '.join(hits)}")
        print("Commit and push demo/ to publish the takedown.")
    else:
        print(f"DRY RUN: {len(hits)} sample(s) would be taken down: {', '.join(hits)}")
        print("Re-run with --apply to move them to demo/_archive/.")
