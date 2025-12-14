# backend/bias_auditor.py
# ------------------------------------------------------------
# STEP 11 — Bias & Authenticity Auditor (Pure Python)
# ------------------------------------------------------------
# Rules:
# - NO LLM calls
# - NO content invention
# - Must score the text based on:
#   Slop (0–40), Bias (0–40), Length/Authenticity (0–20)
# - Must return a dict used by app.py

import re


# ------------------------------------------------------------
# 1. SLOP DETECTION
# ------------------------------------------------------------
SLOP_PHRASES = [
    "proven track record",
    "results-driven",
    "results oriented",
    "highly motivated",
    "dynamic professional",
    "strong communication skills",
    "team player",
    "detail oriented",
    "fast learner",
    "hard worker",
    "self starter",
    "strategic thinker",
    "ability to work under pressure",
]


def score_slop(text: str):
    text_l = text.lower()
    count = 0
    issues = []

    for phrase in SLOP_PHRASES:
        if phrase in text_l:
            count += 1
            issues.append(f"Contains cliché phrase: '{phrase}'")

    # Score scale: 0–40 (more slop → lower score)
    # Max penalty at 10 occurrences
    penalty = min(count, 10) * 4
    score = max(40 - penalty, 0)

    return score, issues


# ------------------------------------------------------------
# 2. BIAS PHRASE DETECTION
# ------------------------------------------------------------
MASCULINE_WORDS = [
    "assertive", "dominant", "competitive", "decisive", "fearless", "ambitious"
]
FEMININE_WORDS = [
    "supportive", "nurturing", "emotional", "compassionate", "warm", "sensitive"
]
AGE_BIAS = [
    "young professional", "energetic", "millennial", "digital native"
]
OTHER_BIAS = [
    "native speaker", "cultural fit", "fit into our culture",
]


def score_bias(text: str):
    text_l = text.lower()
    count = 0
    issues = []

    def check_list(lst, label):
        nonlocal count
        for w in lst:
            if w in text_l:
                count += 1
                issues.append(f"Potential biased wording: '{w}' ({label})")

    check_list(MASCULINE_WORDS, "masculine-coded")
    check_list(FEMININE_WORDS, "feminine-coded")
    check_list(AGE_BIAS, "age bias")
    check_list(OTHER_BIAS, "bias/general")

    # Score scale: 0–40
    penalty = min(count, 10) * 4
    score = max(40 - penalty, 0)

    return score, issues


# ------------------------------------------------------------
# 3. LENGTH & AUTHENTICITY CHECK
# ------------------------------------------------------------
def score_length_and_authenticity(text: str):
    issues = []

    # Sentence length check
    sentences = re.split(r"[.!?]+", text)
    long_sentences = [s for s in sentences if len(s.split()) > 30]
    short_sentences = [s for s in sentences if 0 < len(s.split()) < 4]

    if long_sentences:
        issues.append("Some sentences may be overly long or formal.")
    if short_sentences:
        issues.append("Some sentences may be too short or abrupt.")

    # Paragraph check
    paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
    very_long_paragraphs = [p for p in paragraphs if len(p.split()) > 180]
    very_short_paragraphs = [p for p in paragraphs if len(p.split()) < 10]

    if very_long_paragraphs:
        issues.append("One or more paragraphs are excessively long.")
    if very_short_paragraphs:
        issues.append("Some paragraphs may be too short to feel natural.")

    # Repetition check
    words = re.findall(r"\b\w+\b", text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    repeated = [w for w, c in freq.items() if c > 8 and len(w) > 3]
    if repeated:
        issues.append("Some words appear too frequently, reducing authenticity.")

    # Score: 0–20
    penalty = 0
    if long_sentences:
        penalty += 5
    if very_long_paragraphs:
        penalty += 5
    if repeated:
        penalty += 5
    if very_short_paragraphs or short_sentences:
        penalty += 5

    score = max(20 - penalty, 0)
    return score, issues


# ------------------------------------------------------------
# MAIN PUBLIC FUNCTION FOR APP.PY
# ------------------------------------------------------------
def audit_text(text: str):
    slop_score, slop_issues = score_slop(text)
    bias_score, bias_issues = score_bias(text)
    length_score, length_issues = score_length_and_authenticity(text)

    final_score = slop_score + bias_score + length_score

    issues = slop_issues + bias_issues + length_issues
    return {
        "final_score": final_score,
        "slop_score": slop_score,
        "bias_score": bias_score,
        "length_score": length_score,
        "issues": issues,
    }
