# JobPilot – Bug & Fix Log

> Start date: 2025-12-03

---

## [BUG-001] Summary language mismatch (EN/FI)

- Date: 2025-12-03
- Status: ✅ Fixed
- Area: Step 3 – Match Analysis summary
- Symptom:
  - UI = FI → summary showed in EN
  - UI = EN → summary sometimes showed in FI
- Root cause:
  - Summary generation did not receive `ui_lang`, so it used job-ad / CV language heuristics.
  - Later, translation logic and UI language got out of sync.
- Fix:
  - Pass `ui_lang` into `compare_cv_to_job(...)`.
  - In the comparator prompt, force summary to always be generated in UI language.
  - If flags change UI language, translate summary *from* original UI language → new UI language.
- Files touched:
  - `backend/comparator.py`
  - `app/app.py` (Step 3 block)
