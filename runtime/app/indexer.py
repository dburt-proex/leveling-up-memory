from .config import MEMORY_DIRS
from .parser import parse_markdown_file

INDEX = []


def rebuild_index():
    global INDEX
    records = []

    for record_type, folder in MEMORY_DIRS.items():
        if not folder.exists():
            continue

        for path in folder.glob("*.md"):
            records.append(parse_markdown_file(path, record_type))

    INDEX = records

    return {
        "count": len(INDEX),
        "types": {
            key: sum(1 for r in INDEX if r.record_type == key)
            for key in MEMORY_DIRS.keys()
        },
    }


def get_index():
    return INDEX
