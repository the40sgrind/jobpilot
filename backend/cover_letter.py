import os
from openai import OpenAI
from backend.language_utils import ui_text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(cv_text: str, job_ad: str) -> str:
    """
    Generates a tailored cover letter using the CV + job description.
    This file should NOT import from cv_rewriter.py (fixes circular import).
    """

    prompt = f"""
Write a professional, concise cover letter based on the following CV and job description.

CV:
{cv_text}

Job Description:
{job_ad}

Rules:
- Keep it factual, do not invent new experience.
- Tone: professional, confident, and ATS-friendly.
- Length: 2–3 short paragraphs.
- Return only the letter itself.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.35
    )

    return response.choices[0].message.content.strip()
