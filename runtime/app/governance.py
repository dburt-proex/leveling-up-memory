from pathlib import Path


def classify_write_risk(path: Path, content: str) -> dict:
    exists = path.exists()
    content_size = len(content.strip())

    if not exists and content_size > 0:
        return {
            "gate": "AUTO",
            "reason": "new append-safe record",
        }

    if exists and path.suffix == ".md":
        return {
            "gate": "REVIEW",
            "reason": "existing record update requires review",
        }

    return {
        "gate": "HALT",
        "reason": "ambiguous or unsafe write",
    }
