from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

MEMORY_DIRS = {
    "sessions": REPO_ROOT / "sessions",
    "projects": REPO_ROOT / "projects",
    "decisions": REPO_ROOT / "decisions",
    "assets": REPO_ROOT / "assets",
    "opportunities": REPO_ROOT / "opportunities",
}

VALID_TYPES = set(MEMORY_DIRS.keys())
