# backend/translator.py
# Universal translator for CV + Cover Letter + Summary
# Supports EN / FI / SV / ES / PT-BR / FR / DE

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --------------------------------------------------------------
# GLOBAL LANGUAGE MAP
# --------------------------------------------------------------

LANGUAGE_CODES = {
    "English": "en",
    "Finnish": "fi",
    "Swedish": "sv",
    "Spanish": "es",
    "Portuguese": "pt",
    "French": "fr",
    "German": "de",
}

TRANSLATION_INSTRUCTIONS = {
    "en": "Translate the text into fluent, natural, professional English.",
    "fi": "Käännä teksti luonnolliselle, sujuvalle ja ammattimaiselle suomen kielelle.",
    "sv": "Översätt texten till naturlig, flytande och professionell svenska.",
    "es": "Traduce el texto al español de manera natural, fluida y profesional.",
    "pt": "Traduza o texto para um português natural, fluente e profissional.",
    "fr": "Traduire le texte en français naturel, fluide et professionnel.",
    "de": "Übersetze den Text ins natürliche, flüssige und professionelle Deutsch.",
}


# --------------------------------------------------------------
# CORE TRANSLATION FUNCTION
# --------------------------------------------------------------

def translate_text(input_text: str, target_language: str) -> str:
    """
    Translates text across all 7 supported languages.
    Always returns a translated version.
    Never returns unchanged source text.
    """

    lang_code = LANGUAGE_CODES.get(target_language, "en")
    instruction = TRANSLATION_INSTRUCTIONS[lang_code]

    prompt = f"""
You are a senior professional translator specializing in job applications.

Translate the following text into **{target_language}**.

### HARD RULES
- ALWAYS output a full translation.
- NEVER keep original sentences.
- NEVER respond with “no translation needed”.
- Do NOT shorten or change meaning.
- Preserve structure.
- Output only the translated text.

### STYLE
{instruction}

### TEXT
{input_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )

    translated = response.choices[0].message.content.strip()

    # Extra safety check
    if translated.strip() == input_text.strip():
        retry_prompt = f"""
Translate EVERYTHING into {target_language}.
Do NOT leave any parts unchanged.

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
