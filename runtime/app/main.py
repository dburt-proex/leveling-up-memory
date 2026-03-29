from fastapi import FastAPI, HTTPException, Query
from .indexer import rebuild_index, get_index
from .retriever import search_memory
from .writer import write_record
from .models import GenericWriteRequest
from .config import VALID_TYPES

app = FastAPI(title="Leveling Up Memory Runtime")


@app.on_event("startup")
def startup():
    rebuild_index()


@app.get("/health")
def health():
    return {
        "status": "ok",
        "indexed_records": len(get_index()),
    }


@app.post("/index/rebuild")
def rebuild():
    return rebuild_index()


@app.get("/memory/search")
def memory_search(q: str = Query(..., min_length=1)):
    return {"results": search_memory(q)}


@app.get("/memory/type/{record_type}")
def memory_by_type(record_type: str):
    if record_type not in VALID_TYPES:
        raise HTTPException(status_code=400, detail="invalid record type")

    records = [
        {
            "path": r.path,
            "title": r.title,
            "date": r.date,
            "status": r.status,
            "objective": r.objective,
            "next_action": r.next_action,
        }
        for r in get_index()
        if r.record_type == record_type
    ]
    return {"results": records}


@app.get("/project/{name}")
def get_project(name: str):
    lowered = name.lower()
    for record in get_index():
        if record.record_type == "projects" and record.title.lower() == lowered:
            return record.model_dump()
    raise HTTPException(status_code=404, detail="project not found")


@app.get("/next-actions")
def next_actions():
    data = []
    for r in get_index():
        if r.next_action:
            data.append({
                "title": r.title,
                "type": r.record_type,
                "next_action": r.next_action,
                "path": r.path,
            })
    return {"results": data}


@app.post("/write/{record_type}")
def write(record_type: str, request: GenericWriteRequest):
    if record_type not in VALID_TYPES:
        raise HTTPException(status_code=400, detail="invalid record type")

    result = write_record(record_type, request.filename, request.content)

    if not result["ok"]:
        raise HTTPException(status_code=403, detail=result)

    rebuild_index()
    return result
