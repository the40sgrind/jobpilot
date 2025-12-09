# backend/ats_scanner.py
# Premium ATS Engine — Keyword Match + Formatting Scan
# -----------------------------------------------------

import re
from collections import Counter
from backend.ai_tools import extract_keywords


# -----------------------------------------------------
# 1. SMART JOB-AD KEYWORD REFINER (OPTION B)
# -----------------------------------------------------

def refine_job_keywords(tokens: set) -> set:
    """
    Refines job-ad keywords to keep only meaningful skill-related tokens.

    Removes:
    - HR/marketing verbs (etsimme, tarjoamme, haemme, haluamme...)
    - Company/location names
    - Adjectives with no skill meaning
    - Very generic words
    """

    HR_NOISE = {
        "etsimme","tarjoamme","haemme","haluamme","kiinnostuitko","kuvaus","tehtäväkuvaan",
        "mahdollisuuden","mahtavaa","mahtavat","juuri","parissa","osa","yhdessä",
        "hakemus","lähetä","päätös","sydämesi","yhteisön","kanssa","edut","hyvät",
        "apply","send","looking","seeking","description","team","great","amazing",
        "join","now","about","role","offer","benefits"
    }

    ENTITY_NOISE = {
        "osuuspankki","poppankki","lappajärven","minna","haapoja","antti",
        "suomen","suomalaista","iso","isopellinen"
    }

    refined = set()

    for t in tokens:
        tl = t.lower()

        # HR noise
        if tl in HR_NOISE:
            continue

        # Company/location noise
        if tl in ENTITY_NOISE:
            continue

        # Remove Finnish adjectives ending in -inen
        if tl.endswith("inen") and len(t) < 12:
            continue

        refined.add(t)

    return refined


# -----------------------------------------------------
# 2. SMART CV KEYWORD FILTER (OPTION B)
# -----------------------------------------------------

def filter_cv_keywords(tokens: set) -> set:
    """
    Filters CV keywords using Option B rules:
    - Keep ALL CAPS skills (CRM, SQL, AWS…)
    - Keep alphanumeric short tokens (APV1, ISO9001…)
    - Keep Finnish skill words containing: tutkinto, lisenssi, kortti, pätevyys
    - Remove pure numbers and filler
    """
    SKILL_PATTERNS = ("tutkinto", "lisenssi", "kortti", "pätevyys")

    filtered = set()

    for t in tokens:
        tl = t.lower()

        # Keep ALL CAPS skills
        if t.isupper() and len(t) <= 12:
            filtered.add(t)
            continue

        # Keep short alphanumeric skill tokens
        if re.match(r"^[A-Za-z0-9]+$", t) and any(c.isdigit() for c in t) and len(t) <= 12:
            filtered.add(t)
            continue

        # Keep Finnish certifications
        if any(p in tl for p in SKILL_PATTERNS):
            filtered.add(t)
            continue

        # Remove pure numbers
        if t.isdigit():
            continue

        filtered.add(t)

    return filtered


# -----------------------------------------------------
# 3. MULTILINGUAL HEADING DETECTION
# -----------------------------------------------------

HEADING_WORDS = {
    "experience","education","skills","summary","profile","projects","certifications",
    "kokemus","koulutus","taidot","yhteenveto","projektit","sertifikaatit",
    "erfarenhet","utbildning","färdigheter",
    "experiencia","educación","habilidades",
    "erfahrung","ausbildung","kenntnisse",
    "expérience","éducation","compétences"
}

def score_headings(cv_text: str) -> int:
    count = 0
    for line in cv_text.split("\n"):
        words = line.strip().lower().split()
        if words and words[0] in HEADING_WORDS:
            count += 1
    return min(10, count * 2)  # max 10/10


# -----------------------------------------------------
# 4. DATE FORMATTING SCAN
# -----------------------------------------------------

DATE_PATTERNS = [
    r"\b20\d{2}\b",           # 2018, 2020…
    r"\b\d{4}–\d{4}\b",       # 2018–2020
    r"\b\d{2}/\d{4}\b",       # 08/2022
]

def score_dates(cv_text: str) -> int:
    count = 0
    for p in DATE_PATTERNS:
        if re.search(p, cv_text):
            count += 1
    return min(10, count * 3)  # max 10


# -----------------------------------------------------
# 5. STRUCTURE CLEANLINESS SCAN
# -----------------------------------------------------

def score_structure(cv_text: str) -> int:
    penalties = 0

    # +1 penalty: line longer than 200 chars → poor ATS readability
    for line in cv_text.split("\n"):
        if len(line) > 200:
            penalties += 1

    # +1 penalty: bullet styles that break ATS parsing
    if "*" in cv_text or "•" in cv_text:
        penalties += 1

    score = 10 - penalties
    return max(0, score)


# -----------------------------------------------------
# 6. MAIN ATS ANALYSIS
# -----------------------------------------------------

def run_ats_analysis(job_keywords: set, cv_text: str):
    """
    Returns ATS result dict expected by app.py Step 4.1
    """

    # Extract CV keywords
    raw_cv_kw = extract_keywords(cv_text)
    cv_keywords = filter_cv_keywords(raw_cv_kw)

    # Intersection
    found = sorted(set(k for k in cv_keywords if k in job_keywords))
    missing = sorted(set(k for k in job_keywords if k not in cv_keywords))

    # Keyword score (70%)
    if job_keywords:
        keyword_score = (len(found) / len(job_keywords)) * 70
    else:
        keyword_score = 0

    # Formatting score (30%)
    headings_score = score_headings(cv_text)
    dates_score = score_dates(cv_text)
    structure_score = score_structure(cv_text)
    formatting_score = (headings_score + dates_score + structure_score) / 3

    # Final score
    final_score = round((keyword_score + formatting_score) / 5) * 5
    final_score = max(0, min(100, final_score))

    return {
        "final_score": final_score,
        "keyword_score": round(keyword_score),
        "formatting_score": round(formatting_score),
        "headings_score": headings_score,
        "dates_score": dates_score,
        "structure_score": structure_score,
        "job_keywords": sorted(job_keywords),
        "cv_keywords": sorted(cv_keywords),
        "found_keywords": found,
        "missing_keywords": missing,
    }
