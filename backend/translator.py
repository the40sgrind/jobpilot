# backend/translator.py
# Universal translator for CV + Cover Letter + Summary
# Always returns a FULL translation — never "no translation needed"

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Supported target language mapping
LANGUAGE_CODES = {
    "English": "en",
    "Finnish": "fi",
    "Swedish": "sv",
}

# High-quality linguistic instructions
TRANSLATION_INSTRUCTIONS = {
    "en": "Translate the text into natural, fluent, professional English.",
    "fi": "Käännä teksti luonnolliselle, sujuvalle ja ammattimaiselle suomen kielelle.",
    "sv": "Översätt texten till naturlig, flytande och professionell svenska.",
}


def translate_text(input_text: str, target_language: str) -> str:
    """
    Translates text between EN/FI/SV.
    ALWAYS produces a translated version.
    NEVER returns the original text unless target is English.
    """

    lang_code = LANGUAGE_CODES.get(target_language, "en")
    instruction = TRANSLATION_INSTRUCTIONS[lang_code]

    # ----------- IMPORTANT FIX -----------
    # GPT was sometimes keeping English when translating → FI.
    # These rules HARD-FORCE a real translation.
    # -------------------------------------

    prompt = f"""
You are a professional translator specializing in job applications.

Translate the following text into **{target_language}** with the following rules:

### HARD RULES
- ALWAYS output a full translation.
- NEVER keep the original English sentences.
- NEVER reply with “no translation needed”.
- Do NOT skip or shorten anything.
- Preserve structure and facts exactly.
- Keep tone natural, fluent, and professional.
- Output *only* the translated text.

### TARGET LANGUAGE STYLE
{instruction}

### TEXT TO TRANSLATE
{input_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )

    translated = response.choices[0].message.content.strip()

    # Safety fallback: if GPT returns identical English text when target ≠ English
    if target_language != "English" and translated.strip() == input_text.strip():
        # Force a retry using a stricter directive
        retry_prompt = f"""
Translate EVERYTHING below into {target_language}.
Do NOT leave any English words unchanged.

TEXT:
{input_text}
"""
        retry = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": retry_prompt}],
            temperature=0.0,
        )
        return retry.choices[0].message.content.strip()

    return translated
