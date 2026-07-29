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
    expire(demo_dir, "2026-07-29")
    assert os.path.isdir(os.path.join(demo_dir, "_archive", "expired-biz"))
    assert not os.path.isdir(os.path.join(demo_dir, "expired-biz"))


def test_live_slug_untouched(demo_dir):
    """The live slug's folder must remain in place."""
    expire(demo_dir, "2026-07-29")
    assert os.path.isdir(os.path.join(demo_dir, "live-biz"))


def test_manifest_removes_expired_slug(demo_dir):
    """The manifest must no longer contain the expired slug."""
    expire(demo_dir, "2026-07-29")
    with open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    assert "expired-biz" not in manifest


def test_manifest_retains_live_slug(demo_dir):
    """The manifest must still contain the live slug with its original dates."""
    expire(demo_dir, "2026-07-29")
    with open(os.path.join(demo_dir, "manifest.json"), encoding="utf-8") as fh:
        manifest = json.load(fh)
    assert "live-biz" in manifest
    assert manifest["live-biz"]["expires"] == "2026-08-27"


def test_returns_list_of_archived_slugs(demo_dir):
    """expire() must return the exact list of slugs it archived."""
    result = expire(demo_dir, "2026-07-29")
    assert result == ["expired-biz"]


def test_nothing_expired_returns_empty_list(demo_dir):
    """When today is before all expiry dates, nothing is archived."""
    result = expire(demo_dir, "2026-06-30")
    assert result == []
    # Both folders should still exist
    assert os.path.isdir(os.path.join(demo_dir, "expired-biz"))
    assert os.path.isdir(os.path.join(demo_dir, "live-biz"))
