# backend/ai_tools.py
# Extract keywords from CV text using GPT

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_keywords(cv_text: str) -> list:
    """
    Extracts the most important skills and keywords from the CV.
    Returns a clean Python list of keyword strings.
    """

    prompt = f"""
You are an expert CV keyword extractor.

Extract the most important skills and keywords from the following CV.
Return ONLY a comma-separated list of keywords.
Do NOT add explanations, sentences, or formatting.

CV CONTENT:
{cv_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    raw = response.choices[0].message.content

    # Convert comma-separated values to list safely
    keywords = [k.strip() for k in raw.split(",") if k.strip()]
    return keywords
