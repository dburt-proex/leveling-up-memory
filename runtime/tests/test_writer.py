from pathlib import Path
from app import writer


def test_write_record_auto_for_new_file(tmp_path: Path, monkeypatch):
    monkeypatch.setitem(writer.MEMORY_DIRS, "sessions", tmp_path)

    result = writer.write_record(
        "sessions",
        "test-session.md",
        "# Session Log\n\n## Session Info\n- Date: 2026-03-29",
    )

    assert result["ok"] is True
    assert result["gate"] == "AUTO"
    assert (tmp_path / "test-session.md").exists()


def test_write_record_review_for_existing_file(tmp_path: Path, monkeypatch):
    existing = tmp_path / "existing.md"
    existing.write_text("# Existing", encoding="utf-8")
    monkeypatch.setitem(writer.MEMORY_DIRS, "sessions", tmp_path)

    result = writer.write_record("sessions", "existing.md", "# Updated")
    assert result["ok"] is False
    assert result["gate"] == "REVIEW"
