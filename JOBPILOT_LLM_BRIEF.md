# JobPilot – LLM Brief (Dec 2025)

## Tech stack
- Frontend: Streamlit app (`app/app.py`)
- Backend modules (in `backend/`):
  - `ai_tools.py` – keyword extractor
  - `cv_parser.py` – clean & normalize CV text
  - `comparator.py` – AI match scoring + summary (JSON)
  - `cv_rewriter.py` – rewrites CV in CV language
  - `cover_letter.py` – cover letter in job-ad language
  - `translator.py` – EN/FI/SV full translation
  - `language_utils.py` – all UI strings in 3 languages

## Core flow (8 steps)
1. Paste job ad
2. Upload CV
3. Run match analysis (score + missing skills + summary)
4. Rewrite CV in different style
5. Generate cover letter (job-ad language)
6. Translate CV (target language dropdown)
7. Translate cover letter (target language dropdown)
8. Generate interview prep (job-ad language)

## Language rules (VERY IMPORTANT)
- `ui_lang` (en/fi/sv) controls:
  - All UI text (titles, labels, buttons)
  - Summary language in Step 3
- Summary (Step 3):
  - Must always be generated in **UI language**
  - If flags change UI language after generation → summary is translated accordingly
- Cover letter + interview prep:
  - Must always be in **job-ad language**
- Flags:
  - Implemented as big PNG buttons (fi/gb/se) at top of app

## LLM behaviour rules
- Always return **full files**, not single lines.
- Do NOT refactor architecture unless explicitly asked.
- Do NOT change language rules above.
- When editing a step, send the full step block with its header comments.
