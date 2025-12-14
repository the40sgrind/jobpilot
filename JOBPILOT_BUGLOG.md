# JobPilot – Bug & Fix Log

> Start date: 2025-12-03

---

## Final Stabilization Summary (v1.1)

During the final stabilization phase, multiple issues were resolved iteratively
while refining multilingual support, ATS scanning, UI consistency, and exports.

These fixes were applied rapidly during active development and are summarized
here instead of being logged individually:

- Fixed multilingual UI inconsistencies across all steps
- Corrected language alignment between CV, job ad, and analysis outputs
- Stabilized ATS scanner flow and regeneration logic
- Removed PDF layout issues and ensured consistent exports
- Cleaned translation mappings and fallback logic
- Improved overall app stability before public release

No known critical bugs remain at release time.


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
