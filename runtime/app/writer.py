from .config import MEMORY_DIRS, VALID_TYPES
from .governance import classify_write_risk
from .utils import ensure_markdown_extension, safe_text


def write_record(record_type: str, filename: str, content: str):
    if record_type not in VALID_TYPES:
        return {
            "ok": False,
            "gate": "HALT",
            "reason": f"invalid record type: {record_type}",
            "path": None,
        }

    folder = MEMORY_DIRS[record_type]
    folder.mkdir(parents=True, exist_ok=True)

    filename = ensure_markdown_extension(filename)
    content = safe_text(content)

    path = folder / filename
    decision = classify_write_risk(path, content)

    if decision["gate"] != "AUTO":
        return {
            "ok": False,
            "gate": decision["gate"],
            "reason": decision["reason"],
            "path": str(path),
        }

    path.write_text(content + "\n", encoding="utf-8")

    return {
        "ok": True,
        "gate": decision["gate"],
        "reason": decision["reason"],
        "path": str(path),
    }
