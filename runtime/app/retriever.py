from .indexer import get_index


def score_record(record, query: str) -> float:
    q = query.lower().strip()
    if not q:
        return 0.0

    score = 0.0

    if q in record.title.lower():
        score += 5.0

    if q in record.raw_content.lower():
        score += 2.0

    if record.objective and q in record.objective.lower():
        score += 2.0

    if record.next_action and q in record.next_action.lower():
        score += 1.5

    for section_name, section_body in record.sections.items():
        if q in section_name.lower():
            score += 2.5
        if q in section_body.lower():
            score += 1.0

    type_bias = {
        "projects": 0.4,
        "sessions": 0.2,
        "decisions": 0.2,
        "assets": 0.1,
        "opportunities": 0.1,
    }
    score += type_bias.get(record.record_type, 0.0)

    return score


def make_snippet(content: str, query: str, radius: int = 160) -> str:
    text = content.replace("\n", " ")
    lower = text.lower()
    q = query.lower()
    idx = lower.find(q)

    if idx == -1:
        return text[:radius].strip()

    start = max(0, idx - radius // 2)
    end = min(len(text), idx + radius // 2)
    return text[start:end].strip()


def search_memory(query: str):
    results = []

    for record in get_index():
        score = score_record(record, query)
        if score > 0:
            results.append({
                "path": record.path,
                "record_type": record.record_type,
                "title": record.title,
                "score": round(score, 2),
                "snippet": make_snippet(record.raw_content, query),
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
