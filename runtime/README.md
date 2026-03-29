# Leveling Up Memory Runtime

## Purpose
Executable runtime for the `leveling-up-memory` repository.

## Capabilities
- parse markdown memory records
- build deterministic index
- search memory
- expose next actions
- govern writes with AUTO / REVIEW / HALT

## Folder Assumptions
This runtime expects to live inside the root of the `leveling-up-memory` repository.

Expected structure:
- sessions/
- projects/
- decisions/
- assets/
- opportunities/
- runtime/

## Run

```bash
cd runtime
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
cd runtime
pytest
```

## First Endpoints
- `GET /health`
- `POST /index/rebuild`
- `GET /memory/search?q=leveling`
- `GET /memory/type/projects`
- `GET /project/Leveling%20Up`
- `GET /next-actions`
- `POST /write/sessions`
- `POST /write/projects`
- `POST /write/decisions`
- `POST /write/assets`
- `POST /write/opportunities`

## Notes
- new files are `AUTO`
- updates to existing files are `REVIEW`
- ambiguous or unsafe writes are `HALT`
