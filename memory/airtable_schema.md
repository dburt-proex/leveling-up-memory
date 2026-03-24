# Leveling Up — Memory OS (Airtable Schema)

## Base Name
Leveling Up – Memory OS

---

## TABLE: Projects

| Field | Type | Notes |
|------|------|------|
| Name | Primary (text) | Project name |
| Status | Single Select | Active / Paused / Done |
| Next Action | Long Text | Immediate next move |
| Revenue Potential | Number (1–5) | ROI weighting |
| Last Updated | Date | Auto/manual |

---

## TABLE: Assets

| Field | Type | Notes |
|------|------|------|
| Name | Text | Asset name |
| Type | Single Select | prompt / system / code / offer / content |
| Project | Link → Projects | Parent project |
| Reusable | Checkbox | Yes/No |
| Location | URL/Text | GitHub / Notion / etc |
| Value Score | Number (1–5) | Reuse leverage |

---

## TABLE: Decisions

| Field | Type | Notes |
|------|------|------|
| Decision | Long Text | What was decided |
| Project | Link → Projects | Context |
| Reason | Long Text | Why |
| Outcome | Long Text | Result |
| Timestamp | Date | When |

---

## TABLE: Opportunities

| Field | Type | Notes |
|------|------|------|
| Title | Text | Opportunity |
| Project | Link → Projects | Context |
| Type | Single Select | revenue / system / distribution |
| Effort | Single Select | low / med / high |
| Leverage Score | Number (1–5) | ROI potential |
| Status | Single Select | queued / executing / done |

---

## TABLE: Sessions

| Field | Type | Notes |
|------|------|------|
| Date | Date | Session date |
| Project | Link → Projects | Context |
| Objective | Long Text | Goal |
| Assets Created | Long Text | Outputs |
| Decisions Made | Long Text | Key decisions |
| Issues | Long Text | Problems |
| Next Actions | Long Text | Next steps |
