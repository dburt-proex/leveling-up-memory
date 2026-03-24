# MEMORY SYNC AGENT — BUILD SPEC (AIRTABLE)

## OBJECTIVE
Convert Airtable into a live memory system that:
- auto-ingests session outputs
- distributes data across tables
- generates opportunities automatically
- reduces manual work to near-zero

---

## SYSTEM OVERVIEW

Flow:

Session Entry → Airtable Automations → Memory Tables Updated → Opportunities Created

---

## AUTOMATION 1 — SESSION → MEMORY DISTRIBUTION

### TRIGGER
When record created in:
TABLE: Sessions

---

### ACTION 1 — CREATE ASSET RECORDS

CONDITION:
Field "Assets Created" is not empty

ACTION:
Create record in TABLE: Assets

FIELD MAPPING:
- Name → Assets Created
- Project → Project (linked)
- Type → "system"
- Reusable → checked
- Value Score → 3

NOTE:
If multiple assets exist, keep as single string for v1

---

### ACTION 2 — CREATE DECISION RECORD

CONDITION:
Field "Decisions Made" is not empty

ACTION:
Create record in TABLE: Decisions

FIELD MAPPING:
- Decision → Decisions Made
- Project → Project
- Timestamp → Date

---

### ACTION 3 — UPDATE PROJECT STATE

ACTION:
Update linked record in TABLE: Projects

FIELD MAPPING:
- Next Action → Next Actions
- Last Updated → Date

---

## AUTOMATION 2 — SESSION → OPPORTUNITY GENERATION

### TRIGGER
When record created in:
TABLE: Sessions

---

### ACTION — CREATE OPPORTUNITY RECORD

TABLE: Opportunities

FIELD MAPPING:
- Title → "Derived from session: {Objective}"
- Project → Project
- Type → "system"
- Effort → "low"
- Leverage Score → 3
- Status → "queued"

---

## INPUT STANDARD (AI COMPATIBLE)

At end of each session, structure output as:

OBJECTIVE:
- 

ASSETS:
- 

DECISIONS:
- 

NEXT ACTIONS:
- 

---

## AI PARSING PROMPT

Use this prompt when converting outputs:

Convert the following into structured memory:

OBJECTIVE:
{input}

ASSETS:
{input}

DECISIONS:
{input}

NEXT ACTIONS:
{input}

Output JSON:

{
  "assets": [],
  "decisions": [],
  "next_actions": ""
}

---

## USAGE FLOW

1. Complete work session

2. Fill Airtable "Sessions" record with:
- Objective
- Assets Created
- Decisions Made
- Next Actions

3. Automations trigger automatically:
- Assets created
- Decisions logged
- Project updated
- Opportunity generated

---

## RULES

- Every session must be logged
- Every asset must be captured
- Every decision must be recorded
- No skipped entries

---

## V1 LIMITATIONS

- Assets stored as single string (no splitting yet)
- No direct AI → Airtable write (manual input required)
- Opportunity generation is templated

---

## UPGRADE PATH (NEXT PHASE)

- Add webhook ingestion
- Auto-parse multiple assets
- AI-generated opportunity scoring
- Direct API write to Airtable

---

## SUCCESS CONDITION

System operates as:

Minimal Input → Automatic Memory Update → Continuous Opportunity Generation

No manual duplication
No lost context
No idle sessions
