# backend/comparator.py
# AI-powered CV ↔ Job Ad comparison
# Returns: match score, missing skills, summary
# Output is ALWAYS valid JSON
# ✅ FIXED: Summary now generated in UI language from the start

import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def compare_cv_to_job(cv_text: str, job_ad_text: str, ui_lang: str = "en") -> dict:
    """
    Compare a CV to a job advertisement and return:
    - match score (0–100)
    - missing skills (list)
    - summary (string) — IN THE UI LANGUAGE
    
    Args:
        cv_text: The CV content
        job_ad_text: The job advertisement content
        ui_lang: UI language code ("en", "fi", "sv")
    
    Returns:
        dict with keys: score, missing_skills, summary
    """
    
    # ✅ Map ui_lang to full language name
    LANGUAGE_MAP = {
        "en": "English",
        "fi": "Finnish",
        "sv": "Swedish"
    }
    
    target_language = LANGUAGE_MAP.get(ui_lang, "English")

    prompt = f"""
You are an expert CV/job matching analyzer.

Analyze the following CV and Job Ad.

### CV:
{cv_text}

### Job Ad:
{job_ad_text}

### TASKS:
1. Extract required skills from the job advertisement.
2. Identify which of those skills appear in the CV.
3. Identify missing skills.
4. Compute a match score (0–100%).
5. Write a clear, recruiter-friendly 3–5 sentence summary.

### ⚠️ CRITICAL LANGUAGE REQUIREMENT — READ CAREFULLY:
- The summary MUST be written in **{target_language}**.
- The missing_skills array MUST be in **{target_language}**.
- IGNORE the language of the CV.
- IGNORE the language of the job advertisement.
- Write the summary directly in {target_language} — do NOT translate from English.
- Think and compose natively in {target_language}.

### OUTPUT REQUIREMENTS:
- Output MUST be valid JSON only.
- No explanations outside JSON.
- JSON fields:
  - "score": number (0–100)
  - "missing_skills": array of strings (in {target_language})
  - "summary": string (in {target_language})

Return ONLY JSON. No commentary.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": f"You are a CV analyzer. You MUST output all text fields in {target_language}, regardless of the input languages."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
    )

    raw = response.choices[0].message.content.strip()

    # --- JSON Fail-Safe ---
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = {
            "score": 0,
            "missing_skills": [],
            "summary": "AI failed to output valid JSON."
        }

    return data