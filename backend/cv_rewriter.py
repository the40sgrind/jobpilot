import re
import random
import os
from openai import OpenAI

from backend.language_utils import ui_text  # kept for possible future UI text usage
from backend.translator import translate_text  # compatibility, not used here
from backend.cv_parser import parse_cv_text  # compatibility

# Load OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ------------------------------------------------------------
# BASIC FALLBACK LANGUAGE DETECT (safe + local)
# ------------------------------------------------------------
def simple_lang_detect(text: str) -> str:
    """
    Very small internal fallback to detect main CV language
    without depending on language_utils.
    Returns one of:
    English / Finnish / Swedish / Spanish / Portuguese / French / German
    """
    text_l = (text or "").lower()

    if any(word in text_l for word in ["the", "and", "experience", "skills"]):
        return "English"
    if any(word in text_l for word in ["työkokemus", "osaaminen", "suomi"]):
        return "Finnish"
    if any(word in text_l for word in ["erfarenhet", "kunskaper"]):
        return "Swedish"
    if any(word in text_l for word in ["experiencia", "habilidades"]):
        return "Spanish"
    if any(word in text_l for word in ["experiência", "habilidades"]):
        return "Portuguese"
    if any(word in text_l for word in ["expérience", "compétences"]):
        return "French"
    if any(word in text_l for word in ["erfahrung", "fähigkeiten"]):
        return "German"

    return "English"  # fallback


# ------------------------------------------------------------
# TEMPLATE LOADING (LIGHT BLEND – SAFE)
# ------------------------------------------------------------
def load_random_template(lang: str) -> str:
    """
    Loads one random template snippet for the selected language.
    Falls back to English if missing.
    Safe: if nothing is available, returns "".
    """
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "templates"))
    lang_folder = os.path.join(base_path, lang)
    english_fallback = os.path.join(base_path, "en")

    # Try target language folder
    if os.path.isdir(lang_folder):
        all_templates = []
        for fname in os.listdir(lang_folder):
            if fname.endswith(".txt"):
                try:
                    with open(os.path.join(lang_folder, fname), "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            # Extract only one snippet — templates may contain multiple separated by ===
                            snippets = [s.strip() for s in content.split("=== TEMPLATE") if s.strip()]
                            all_templates.extend(snippets)
                except:
                    pass
        if all_templates:
            return random.choice(all_templates)

    # Fallback to English
    if os.path.isdir(english_fallback):
        all_templates = []
        for fname in os.listdir(english_fallback):
            if fname.endswith(".txt"):
                try:
                    with open(os.path.join(english_fallback, fname), "r", encoding="utf-8") as f:
                        content = f.read().strip()
                        if content:
                            snippets = [s.strip() for s in content.split("=== TEMPLATE") if s.strip()]
                            all_templates.extend(snippets)
                except:
                    pass
        if all_templates:
            return random.choice(all_templates)

    return ""  # safe fallback: no template used


# ------------------------------------------------------------
# POST-PROCESS SANITATION (markdown removal + heading soft-normalization)
# ------------------------------------------------------------
def clean_markdown(text: str) -> str:
    """Remove markdown characters from headings or body."""
    if not text:
        return ""

    # Remove common markdown: **bold**, __bold__, #, ##, etc.
    text = re.sub(r"\*{1,3}", "", text)
    text = re.sub(r"_+", "", text)
    text = re.sub(r"^#+", "", text, flags=re.MULTILINE)
    text = text.replace("---", "")
    text = text.replace("—", "-")

    # Clean repeated whitespace
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def soft_normalize_headings(text: str) -> str:
    """
    Converts headings to ATS-safe standard ones ONLY when they already match closely.
    Never invents content or adds new sections.
    """
    if not text:
        return ""

    heading_map = {
        # SUMMARY
        r"^(professional summary|summary of qualifications|profile)$": "Summary",

        # EXPERIENCE
        r"^(work experience|professional experience|experience|employment history|career history)$": "Experience",

        # EDUCATION
        r"^(education|academic background|educational background)$": "Education",

        # SKILLS
        r"^(skills|core skills|key skills|technical skills|competencies)$": "Skills",

        # CERTIFICATIONS
        r"^(certifications|licenses|certifications & licenses)$": "Certifications",

        # PROJECTS
        r"^(projects|selected projects|relevant projects)$": "Projects",

        # LANGUAGES
        r"^(languages|language skills)$": "Languages",
    }

    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        stripped = line.strip().lower()

        # Check if this line matches any heading pattern
        normalized = None
        for pattern, replacement in heading_map.items():
            if re.fullmatch(pattern, stripped):
                normalized = replacement
                break

        if normalized:
            cleaned_lines.append(normalized)
        else:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def sanitize_output(text: str) -> str:
    """Apply full ATS-safety cleanup."""
    if not text:
        return ""
    text = clean_markdown(text)
    text = soft_normalize_headings(text)
    return text.strip()


# ------------------------------------------------------------
# MAIN CV REWRITER — OPTION B (Enhanced Light Blend)
# ------------------------------------------------------------
def rewrite_cv(cv_text: str, job_ad: str, style: str) -> str:
    """
    Light-blend rewrite with strong safety rules:
    - Uses job ad for relevance
    - Applies style (bullets / paragraphs / hybrid)
    - Blends template tone safely (no facts added)
    - Enforces ATS-friendly output
    - Sanitizes markdown + normalizes headings
    """
    cv_text = cv_text or ""
    job_ad = job_ad or ""

    # Detect language of CV
    lang = simple_lang_detect(cv_text).lower()

    lang_map = {
        "english": "en",
        "finnish": "fi",
        "swedish": "sv",
        "spanish": "es",
        "portuguese": "pt-br",
        "french": "fr",
        "german": "de",
    }
    lang_code = lang_map.get(lang, "en")

    # Load a template snippet safely
    template_snippet = load_random_template(lang_code)

    # Build LLM prompt
    prompt = f"""
Rewrite the following CV using the style: {style}.

CV:
{cv_text}

Job Ad (for relevance and alignment):
{job_ad}

Template snippet (light tone only):
{template_snippet or "[No template available]"}

STRICT RULES:
- DO NOT invent roles, dates, employers, or achievements.
- DO NOT fabricate metrics or responsibilities.
- Keep all facts exactly as they appear in the CV.
- DO NOT add new sections.
- DO NOT output markdown (no **, ##, _, *, ---).
- Use plain text headings only.
- Maintain readability and ATS-friendly formatting.
- Improve tone, clarity, flow, and conciseness.
- Blend template tone LIGHTLY (phrasing only; no content from it).
- Return ONLY the rewritten CV.
"""

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.25
    )

    rewritten = response.choices[0].message.content.strip()

    # Final ATS-safe processing
    cleaned = sanitize_output(rewritten)
    return cleaned


# ------------------------------------------------------------
# PUBLIC WRAPPERS — compatibility with app.py
# ------------------------------------------------------------
def detect_cv_language(text: str) -> str:
    return simple_lang_detect(text or "")


def detect_language_of_job_ad(text: str) -> str:
    return simple_lang_detect(text or "")
