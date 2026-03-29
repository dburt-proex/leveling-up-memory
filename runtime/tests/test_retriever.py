from pathlib import Path
from app.parser import parse_markdown_file
from app import indexer
from app.retriever import search_memory


def test_search_memory_returns_match(tmp_path: Path):
    file_path = tmp_path / "project.md"
    file_path.write_text(
        """# Leveling Up

## Project Info
- Name: Leveling Up
- Status: active
- Objective: Build operator memory runtime
""",
        encoding="utf-8",
    )

    record = parse_markdown_file(file_path, "projects")
    indexer.INDEX = [record]

    results = search_memory("runtime")
    assert len(results) >= 1
    assert results[0]["title"] == "Leveling Up"
