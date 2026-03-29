import re
from pathlib import Path
from typing import Optional
from .models import MemoryRecord

HEADER_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
SECTION_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def parse_sections(content: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(content))
    sections: dict[str, str] = {}

    for i, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        sections[name] = content[start:end].strip()

    return sections


def extract_field_value(section_text: str, field_name: str) -> Optional[str]:
    prefix = f"- {field_name}:"
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith(prefix):
            value = stripped[len(prefix):].strip()
            return value or None
    return None


def extract_first_bullet(section_text: str) -> Optional[str]:
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            return stripped[2:].strip()
        if re.match(r"^\d+\.\s+", stripped):
            return re.sub(r"^\d+\.\s+", "", stripped).strip()
    return None


def extract_linked_list(section_text: str) -> list[str]:
    items = []
    for line in section_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            items.append(stripped[2:].strip())
    return items


def parse_markdown_file(path: Path, record_type: str) -> MemoryRecord:
    raw = path.read_text(encoding="utf-8")
    title_match = HEADER_RE.search(raw)
    title = title_match.group(1).strip() if title_match else path.stem

    sections = parse_sections(raw)

    date = None
    status = None
    objective = None
    next_action = None
    linked_projects: list[str] = []

    if record_type == "sessions":
        session_info = sections.get("Session Info", "")
        date = extract_field_value(session_info, "Date")
        objective = extract_field_value(session_info, "Objective")
        next_actions = sections.get("Next Actions (Highest Leverage)", "")
        next_action = extract_first_bullet(next_actions)

    elif record_type == "projects":
        project_info = sections.get("Project Info", "")
        status = extract_field_value(project_info, "Status")
        objective = extract_field_value(project_info, "Objective")
        next_action = extract_first_bullet(
            sections.get("Next Action (Single Highest Leverage)", "")
        )

    elif record_type == "decisions":
        decision_info = sections.get("Decision Info", "")
        date = extract_field_value(decision_info, "Date")

    elif record_type == "assets":
        asset_info = sections.get("Asset Info", "")
        status = extract_field_value(asset_info, "Status")
        linked_projects = extract_linked_list(sections.get("Linked Projects", ""))

    elif record_type == "opportunities":
        opp_info = sections.get("Opportunity Info", "")
        objective = extract_field_value(opp_info, "Title")
        status = extract_first_bullet(sections.get("Status", ""))
        next_action = extract_first_bullet(sections.get("Next Action", ""))

    return MemoryRecord(
        path=str(path),
        record_type=record_type,
        title=title,
        date=date,
        status=status,
        objective=objective,
        next_action=next_action,
        linked_projects=linked_projects,
        sections=sections,
        raw_content=raw,
    )
