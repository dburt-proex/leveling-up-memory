from pathlib import Path
from app.parser import parse_markdown_file, parse_sections


def test_parse_sections():
    content = """# Test

## One
alpha

## Two
beta
"""
    sections = parse_sections(content)
    assert sections["One"] == "alpha"
    assert sections["Two"] == "beta"


def test_parse_project_file(tmp_path: Path):
    file_path = tmp_path / "sample.md"
    file_path.write_text(
        """# Leveling Up

## Project Info
- Name: Leveling Up
- Status: active
- Objective: Build operator system

## Next Action (Single Highest Leverage)
- create runtime
""",
        encoding="utf-8",
    )

    record = parse_markdown_file(file_path, "projects")
    assert record.title == "Leveling Up"
    assert record.status == "active"
    assert record.objective == "Build operator system"
    assert record.next_action == "create runtime"
