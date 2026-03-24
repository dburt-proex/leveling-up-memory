# WEBHOOK LAYER — AI → AIRTABLE DIRECT WRITE

## OBJECTIVE

Eliminate manual Airtable entry by:
- sending structured JSON from AI
- ingesting directly into Airtable
- triggering automations automatically

---

## SYSTEM FLOW

AI OUTPUT → WEBHOOK → AIRTABLE → AUTOMATIONS → MEMORY + OPPORTUNITIES

---

## STEP 1 — CREATE AIRTABLE WEBHOOK

### METHOD: Airtable Automation Webhook Trigger

1. Go to Airtable
2. Open base: "Leveling Up – Memory OS"
3. Go to Automations
4. Create new automation

---

### TRIGGER

Choose:
"Webhook" → "When webhook received"

Airtable will generate:
→ Webhook URL

SAVE THIS URL

---

## STEP 2 — WEBHOOK PAYLOAD STRUCTURE

AI must send JSON in this format:

{
  "date": "YYYY-MM-DD",
  "project": "Project Name",
  "objective": "string",
  "assets": ["asset 1", "asset 2"],
  "decisions": ["decision 1"],
  "next_actions": "string"
}

---

## STEP 3 — AUTOMATION ACTIONS

### ACTION 1 — CREATE SESSION RECORD

Table: Sessions

Field Mapping:
- Date → date
- Project → project (linked)
- Objective → objective
- Assets Created → assets (join as string)
- Decisions Made → decisions (join as string)
- Next Actions → next_actions

---

### ACTION 2 — CREATE ASSETS (LOOP)

For each item in assets:

- Create record in Assets:
  - Name → asset
  - Project → project
  - Type → "system"
  - Reusable → true
  - Value Score → 3

---

### ACTION 3 — CREATE DECISIONS

For each item in decisions:

- Create record in Decisions:
  - Decision → decision
  - Project → project
  - Timestamp → date

---

### ACTION 4 — UPDATE PROJECT

- Update Projects:
  - Next Action → next_actions
  - Last Updated → date

---

### ACTION 5 — CREATE OPPORTUNITY

- Create record in Opportunities:
  - Title → "Derived: {objective}"
  - Project → project
  - Type → "system"
  - Effort → "low"
  - Leverage Score → 3
  - Status → "queued"

---

## STEP 4 — AI OUTPUT PROMPT (CRITICAL)

Use this at end of every session:

Convert the session into webhook JSON.

Return ONLY valid JSON.

Format:

{
  "date": "",
  "project": "",
  "objective": "",
  "assets": [],
  "decisions": [],
  "next_actions": ""
}

No explanation. No extra text.

---

## STEP 5 — SENDING DATA

### OPTION A — MANUAL (FAST START)

Use:
- Postman
- curl
- browser webhook tool

Example:

curl -X POST "WEBHOOK_URL" \
-H "Content-Type: application/json" \
-d '{
  "date": "2026-03-24",
  "project": "Leveling Up",
  "objective": "Built webhook layer",
  "assets": ["Webhook system", "Memory automation"],
  "decisions": ["Use Airtable as v1 memory"],
  "next_actions": "Test full pipeline"
}'

---

### OPTION B — AUTOMATED (RECOMMENDED NEXT)

Use:
- Make.com
- Zapier
- Manus API

Flow:
AI → webhook → Airtable

---

## RULES

- JSON must be valid
- No empty fields
- Arrays required for assets + decisions

---

## SUCCESS CONDITION

You finish work →

AI generates JSON →

Webhook fires →

Airtable updates automatically →

Opportunities generated →

System ready for next session

---

## RESULT

No manual logging
No context loss
Continuous system memory
Automatic leverage tracking
