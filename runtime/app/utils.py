def ensure_markdown_extension(filename: str) -> str:
    filename = filename.strip()
    if not filename.endswith(".md"):
        filename += ".md"
    return filename


def safe_text(value: str) -> str:
    return value.replace("\r\n", "\n").strip()
