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

## Instructions

The `instructions/` folder contains the system prompts and operating rules:

- [`codex_instruction_box.txt`](instructions/codex_instruction_box.txt) — full system prompt and operating instructions
- [`execution_engine.txt`](instructions/execution_engine.txt) — execution loop and rules
- [`memory_layer.txt`](instructions/memory_layer.txt) — session continuity and asset tracking
- [`opportunity_engine.txt`](instructions/opportunity_engine.txt) — 3-option generation at session start
- [`project_instruction_box.txt`](instructions/project_instruction_box.txt) — project-mode operating rules
- [`validation_layer.txt`](instructions/validation_layer.txt) — output validation criteria