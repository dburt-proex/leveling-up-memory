from typing import Optional, List, Dict
from pydantic import BaseModel


class MemoryRecord(BaseModel):
    path: str
    record_type: str
    title: str
    date: Optional[str] = None
    status: Optional[str] = None
    objective: Optional[str] = None
    next_action: Optional[str] = None
    linked_projects: List[str] = []
    sections: Dict[str, str] = {}
    raw_content: str


class GenericWriteRequest(BaseModel):
    filename: str
    content: str
