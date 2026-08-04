"""
test_expire.py — tests for scripts/expire_samples.expire()
"""

import json
import os

import pytest

from expire_samples import expire


@pytest.fixture()
def demo_dir(tmp_path):
    """
    Build a temp demo/ structure:
      manifest.json  — one expired slug (expires 2026-07-01) + one live (2026-08-27)
      expired-biz/   — folder for the expired slug
      live-biz/      — folder for the live slug
    """
    demo = tmp_path / "demo"
    demo.mkdir()

    manifest = {
        "expired-biz": {"published": "2026-06-01", "expires": "2026-07-01"},
        "live-biz":    {"published": "2026-07-28", "expires": "2026-08-27"},
    }
    (demo / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    # Create slug folders (each needs at least one file so shutil.move works)
    (demo / "expired-biz").mkdir()
    (demo / "expired-biz" / "index.html").write_text("<html/>", encoding="utf-8")

    (demo / "live-biz").mkdir()
    (demo / "live-biz" / "index.html").write_text("<html/>", encoding="utf-8")

    return str(demo)


def test_expired_slug_moved_to_archive(demo_dir):
    """The expired slug's folder should be moved to _archive/."""
    expire(demo_dir, "2026-07-29", apply=True)
    assert os.path.isdir(os.path.join(demo_dir, "_archive", "expired-biz"))
    assert not os.path.isdir(os.path.join(demo_dir, "expired-biz"))


def test_live_slug_untouched(demo_dir):
    """The live slug's folder must remain in place."""
    expire(demo_dir, "2026-07-29", apply=True)
    assert os.path.isdir(os.path.join(demo_dir, "live-biz"))


def test_manifest_stamps_expired_slug_as_taken_down(demo_dir):
    """The manifest must record WHEN the slug was taken down, not forget it."""
    expire(demo_dir, "2026-07-29", apply=True)
    with open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    assert manifest["expired-biz"]["taken_down"] == "2026-07-29"


def test_manifest_retains_live_slug(demo_dir):
    """The manifest must still contain the live slug with its original dates."""
    expire(demo_dir, "2026-07-29", apply=True)
    with open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    assert "live-biz" in manifest
    assert manifest["live-biz"]["expires"] == "2026-08-27"
    assert "taken_down" not in manifest["live-biz"]


def test_returns_list_of_archived_slugs(demo_dir):
    """expire() must return the exact list of slugs it took down."""
    result = expire(demo_dir, "2026-07-29", apply=True)
    assert result == ["expired-biz"]


def test_nothing_expired_returns_empty_list(demo_dir):
    """When today is before all expiry dates, nothing is taken down."""
    result = expire(demo_dir, "2026-06-30", apply=True)
    assert result == []
    # Both folders should still exist
    assert os.path.isdir(os.path.join(demo_dir, "expired-biz"))
    assert os.path.isdir(os.path.join(demo_dir, "live-biz"))


# ---------------------------------------------------------------------------
# Safety: dry run, idempotence, and the expiry boundary
# ---------------------------------------------------------------------------

def test_dry_run_is_the_default_and_changes_nothing(demo_dir):
    """A bare call must report the expired slug without touching disk."""
    before = json.load(open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8"))

    result = expire(demo_dir, "2026-07-29")

    assert result == ["expired-biz"]
    # Folder still live, nothing archived, manifest byte-identical.
    assert os.path.isdir(os.path.join(demo_dir, "expired-biz"))
    assert not os.path.isdir(os.path.join(demo_dir, "_archive"))
    after = json.load(open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8"))
    assert after == before


def test_second_run_after_takedown_is_a_noop(demo_dir):
    """Re-running must not try to take the same slug down twice."""
    first = expire(demo_dir, "2026-07-29", apply=True)
    assert first == ["expired-biz"]

    second = expire(demo_dir, "2026-07-30", apply=True)
    assert second == []
    # The archived copy is still the one the first run made.
    assert os.path.isdir(os.path.join(demo_dir, "_archive", "expired-biz"))


def test_slug_expiring_today_is_not_taken_down(demo_dir):
    """Expiry is exclusive: the folder stays up through its expires date."""
    result = expire(demo_dir, "2026-07-01", apply=True)
    assert result == []
    assert os.path.isdir(os.path.join(demo_dir, "expired-biz"))


def test_slug_not_in_manifest_is_never_touched(demo_dir):
    """A stray folder with no manifest entry must be left alone."""
    stray = os.path.join(demo_dir, "stray-biz")
    os.makedirs(stray)
    with open(os.path.join(stray, "index.html"), "w", encoding="utf-8") as fh:
        fh.write("<html/>")

    expire(demo_dir, "2026-09-30", apply=True)

    assert os.path.isdir(stray)
    assert not os.path.isdir(os.path.join(demo_dir, "_archive", "stray-biz"))


def test_takedown_archives_all_three_pages_together(tmp_path):
    """Hub, website/ and audit/ live under one slug folder, so one move takes
    down all three at once."""
    demo = tmp_path / "demo"
    demo.mkdir()
    (demo / "manifest.json").write_text(
        json.dumps({"trio-biz": {"published": "2026-06-01", "expires": "2026-07-01"}}),
        encoding="utf-8",
    )
    slug = demo / "trio-biz"
    for rel in ("index.html", "website/index.html", "audit/index.html"):
        target = slug / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("<html/>", encoding="utf-8")

    expire(str(demo), "2026-07-29", apply=True)

    archived = demo / "_archive" / "trio-biz"
    assert (archived / "index.html").is_file()
    assert (archived / "website" / "index.html").is_file()
    assert (archived / "audit" / "index.html").is_file()
    assert not slug.exists()
