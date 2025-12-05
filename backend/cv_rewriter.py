# backend/cv_rewriter.py

import os
from openai import OpenAI
from backend.translator import LANGUAGE_CODES

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def detect_cv_language(text: str) -> str:
    t = text.lower()

    fi_hits = ["työ", "vastuu", "asiakas", "kokemus", "suomi", "osaaminen"]
    sv_hits = ["erfarenhet", "kund", "ansvar", "svenska", "kompetens"]
    en_hits = ["experience", "customer", "responsible", "english", "skills"]

    fi_score = sum(w in t for w in fi_hits)
    sv_score = sum(w in t for w in sv_hits)
    en_score = sum(w in t for w in en_hits)

    if fi_score >= max(sv_score, en_score):
        return "Finnish"
    if sv_score >= max(fi_score, en_score):
        return "Swedish"
    return "English"


def detect_language_of_job_ad(text: str) -> str:
    t = text.lower()

    fi_hits = ["vastaa", "työ", "hakemus", "kokemus", "asiakas", "suomi"]
    sv_hits = ["ansvar", "tjänst", "kund", "erfarenhet", "svenska"]
    en_hits = ["responsibilities", "requirements", "customer", "english"]

    fi_score = sum(w in t for w in fi_hits)
    sv_score = sum(w in t for w in sv_hits)
    en_score = sum(w in t for w in en_hits)

    if fi_score >= max(sv_score, en_score):
        return "Finnish"
    if sv_score >= max(fi_score, en_score):
        return "Swedish"
    return "English"


def rewrite_cv(cv_text: str, job_ad_text: str, format_style: str) -> str:

    cv_lang = detect_cv_language(cv_text)

    # --- PATCHED STYLE MAPPING ---
    clean_style = (
        "Bullet Points (recruiter-friendly)" if "📌" in format_style else
        "Paragraphs (easy to read)" if "✏️" in format_style else
        "Hybrid Format"
    )

    style_instructions = {
        "Bullet Points (recruiter-friendly)": "Use clean, simple bullet points that recruiters can scan fast.",
        "Paragraphs (easy to read)": "Use short, clean paragraphs that read naturally.",
        "Hybrid Format": "Combine short paragraphs followed by relevant bullet points."
    }[clean_style]

    language_instruction = {
        "English": "Write the rewritten CV in English.",
        "Finnish": "Kirjoita uudelleenkirjoitettu CV suomeksi.",
        "Swedish": "Skriv det omskrivna CV:t på svenska."
    }[cv_lang]

    prompt = f"""
You are a senior CV writer.

Rewrite the following CV so it matches the job advertisement more strongly.

### ORIGINAL CV:
{cv_text}

### JOB AD:
{job_ad_text}

### RULES:
- Keep 100% factual accuracy.
- No invented experience.
- Increase clarity and relevance.
- Use the requested CV style.
- Do NOT change the language.

### FORMAT STYLE:
{style_instructions}

### LANGUAGE:
{language_instruction}

Return ONLY the rewritten CV text.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.25
    )

    return response.choices[0].message.content.strip()


def generate_cover_letter(cv_text: str, job_ad_text: str) -> str:
    job_lang = detect_language_of_job_ad(job_ad_text)

    lang_instruction = {
        "English": "Write the cover letter in English.",
        "Finnish": "Kirjoita hakemuskirje suomeksi.",
        "Swedish": "Skriv det personliga brevet på svenska."
    }[job_lang]

    prompt = f"""
You are a professional recruitment writer.

Create a tailored cover letter using the CV and job advertisement.

### CV:
{cv_text}

### JOB AD:
{job_ad_text}

### RULES:
- Write ONLY in the job ad language.
- No fabricated experience.
- Use professional, clear tone.

### LANGUAGE INSTRUCTION:
{lang_instruction}

Return ONLY the letter text.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.25
    )

    return response.choices[0].message.content.strip()
