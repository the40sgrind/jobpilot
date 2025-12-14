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
    Enhanced language detection using word frequency scoring.
    Returns one of:
    English / Finnish / Swedish / Spanish / Portuguese / French / German
    """
    if not text:
        return "English"
    
    text_l = text.lower()
    
    # Score-based detection (count matches for each language)
    scores = {
        "English": 0,
        "Finnish": 0,
        "Swedish": 0,
        "Spanish": 0,
        "Portuguese": 0,
        "French": 0,
        "German": 0
    }
    
    # English markers (more specific)
    en_words = ["experience", "skills", "education", "worked", "managed", "developed", "responsibilities", "achievements"]
    scores["English"] = sum(1 for word in en_words if word in text_l)
    
    # Finnish markers
    fi_words = ["työkokemus", "osaaminen", "koulutus", "vastuualueet", "saavutukset", "työssä", "projektit", "ja", "että", "olen"]
    scores["Finnish"] = sum(1 for word in fi_words if word in text_l)
    
    # Swedish markers
    sv_words = ["erfarenhet", "kunskaper", "utbildning", "ansvar", "arbete", "projekt", "och", "som", "att", "har"]
    scores["Swedish"] = sum(1 for word in sv_words if word in text_l)
    
    # Spanish markers
    es_words = ["experiencia", "habilidades", "educación", "responsabilidades", "logros", "trabajé", "proyectos", "que", "con", "en"]
    scores["Spanish"] = sum(1 for word in es_words if word in text_l)
    
    # Portuguese markers
    pt_words = ["experiência", "habilidades", "educação", "responsabilidades", "conquistas", "trabalhei", "projetos", "que", "com", "em"]
    scores["Portuguese"] = sum(1 for word in pt_words if word in text_l)
    
    # French markers
    fr_words = ["expérience", "compétences", "éducation", "responsabilités", "réalisations", "travaillé", "projets", "que", "avec", "dans"]
    scores["French"] = sum(1 for word in fr_words if word in text_l)
    
    # German markers
    de_words = ["erfahrung", "fähigkeiten", "bildung", "verantwortung", "erfolge", "arbeitete", "projekte", "und", "mit", "bei"]
    scores["German"] = sum(1 for word in de_words if word in text_l)
    
    # Return language with highest score
    max_lang = max(scores, key=scores.get)
    
    # If no matches at all, default to English
    if scores[max_lang] == 0:
        return "English"
    
    return max_lang
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

    # Build LLM prompt - detect if ATS keywords are being injected
    has_ats_guidance = "## INTERNAL LLM GUIDANCE" in job_ad

    if has_ats_guidance:
        prompt = f"""
Rewrite the following CV using the style: {style}.

CV:
{cv_text}

Job Ad (for relevance and alignment):
{job_ad}

Template snippet (light tone only):
{template_snippet or "[No template available]"}

STRICT RULES:
- Write the rewritten CV in the SAME language as the original CV ({lang.capitalize()}).
- DO NOT invent roles, dates, employers, or achievements.
- DO NOT fabricate metrics or responsibilities.
- Keep all facts exactly as they appear in the CV.
- IMPORTANT: The job ad contains a list of ATS keywords that are MISSING from the CV.
- You MUST naturally incorporate these keywords into existing CV sections where they fit.
- Match keywords to the candidate's actual experience - if they used Python, ensure "Python" appears.
- If they managed projects, ensure "project management" appears.
- Weave keywords naturally into bullet points and descriptions.
- DO NOT create a separate "keywords" section.
- DO NOT add fake experience just to include keywords.
- DO NOT output markdown (no **, ##, _, *, ---).
- Use plain text headings only.
- Return ONLY the rewritten CV.
"""
    else:
        prompt = f"""
Rewrite the following CV using the style: {style}.

CV:
{cv_text}

Job Ad (for relevance and alignment):
{job_ad}

Template snippet (light tone only):
{template_snippet or "[No template available]"}

STRICT RULES:
- Write the rewritten CV in the SAME language as the original CV ({lang.capitalize()}).
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
