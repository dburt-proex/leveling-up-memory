# leveling-up-memory

A structured memory and execution system for the "Leveling Up" AI operator. It stores session logs, project notes, strategic decisions, opportunities, and reusable instruction prompts across work sessions.

---

## Repository Structure

```
assets/          — reusable outputs (code snippets, offers, prompts, specs, templates)
decisions/       — decision log and lessons learned
instructions/    — system prompt and operating instructions
opportunities/   — active opportunities and monetization pipeline
projects/        — per-project notes (CASA, JobTap, Leveling-Up)
sessions/        — chronological session logs + template
```

---

## Health Analysis (2026-03-22)

### ✅ Fixed

| Issue | Files Removed | Resolution |
|---|---|---|
| **Duplicate instruction files** — `execution_engine.txt`, `memory_layer.txt`, `opportunity_engine.txt`, `project_instruction_box.txt`, and `validation_layer.txt` were all subset/condensed copies of `codex_instruction_box.txt` | 5 files removed | `instructions/codex_instruction_box.txt` is now the single source of truth |

### ⚠️ Noted (stubs — populate as work progresses)

| File | Status |
|---|---|
| `decisions/decision-log.md` | Empty placeholder |
| `decisions/lessons-learned.md` | Empty placeholder |
| `opportunities/active-opportunities.md` | Empty placeholder |
| `opportunities/monetization-pipeline.md` | Empty placeholder |
| `projects/CASA.md` | Empty placeholder |
| `projects/JobTap.md` | Empty placeholder |
| `projects/Leveling-Up.md` | Empty placeholder |
| `sessions/2026-03-22-session-001.md` | Empty placeholder |
| `sessions/2026-03-23-session-002.md` | Empty placeholder |
| `assets/` sub-folders | All `.gitkeep` placeholders |

---

## Instructions

The single authoritative system prompt lives in [`instructions/codex_instruction_box.txt`](instructions/codex_instruction_box.txt). It defines:

- Role and primary objective
- Core rules and default output structure
- Execution loop (Direction Check → Plan → Build → Verify → Iterate)
- Validation layer
- Memory layer (session continuity, asset reuse)
- Opportunity engine (3-option generation at session start)
- Decision priority and anti-patterns