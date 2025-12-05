import sys
import os

# Ensure backend imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import PyPDF2

from backend.ai_tools import extract_keywords
from backend.cv_parser import parse_cv_text
from backend.comparator import compare_cv_to_job
from backend.cv_rewriter import rewrite_cv, detect_cv_language, detect_language_of_job_ad
from backend.cover_letter import generate_cover_letter
from backend.translator import translate_text
from backend.language_utils import ui_text

# --------------------------------------------------------------
# BASIC SETUP
# --------------------------------------------------------------

st.set_page_config(page_title="JobPilot", page_icon="🧭", layout="centered")

if "ui_lang" not in st.session_state:
    st.session_state.ui_lang = "en"

ui_lang = st.session_state.ui_lang.strip().lower()



# --------------------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------------------
st.markdown("""
<style>

    .flag-bar button,
    div[data-testid="stButton"] > button[title="🇫🇮"],
    div[data-testid="stButton"] > button[title="🇬🇧"],
    div[data-testid="stButton"] > button[title="🇸🇪"] {
        font-size: 52px !important;
        line-height: 1 !important;
        padding: 0px 6px !important;
        background: none !important;
        border: none !important;
        cursor: pointer !important;
    }

    .card {
        background-color: #2e2e2e !important;
        border: 1px solid #444 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        color: #f1f1f1 !important;
    }

    div.stButton > button {
        background-color: #3c3c3c !important;
        border: 1px solid #666 !important;
        color: #ffffff !important;
        padding: 8px 16px !important;
        border-radius: 6px !important;
    }

</style>
""", unsafe_allow_html=True)



# --------------------------------------------------------------
# FLAG SWITCHER — WORKING VERSION
# --------------------------------------------------------------

fi_png = "https://flagcdn.com/w40/fi.png"
en_png = "https://flagcdn.com/w40/gb.png"
sv_png = "https://flagcdn.com/w40/se.png"

col1, col2, col3 = st.columns([0.15, 0.15, 0.15])

with col1:
    if st.button(f"![]({fi_png})", key="flag_fi"):
        st.session_state.ui_lang = "fi"

with col2:
    if st.button(f"![]({en_png})", key="flag_en"):
        st.session_state.ui_lang = "en"

with col3:
    if st.button(f"![]({sv_png})", key="flag_sv"):
        st.session_state.ui_lang = "sv"

ui_lang = st.session_state.ui_lang.strip().lower()

# --------------------------------------------------------------
# LANGUAGE SANITY CHECK — FORCE ui_lang TO ALWAYS BE A STRING
# --------------------------------------------------------------

val = st.session_state.ui_lang

# Normalize ANY weird Streamlit type into a clean string: "en", "fi", "sv"
if isinstance(val, list):
    ui_lang = val[0].strip().lower()
else:
    ui_lang = str(val).strip().lower()


# --------------------------------------------------------------
# TRANSLATOR CONFIG
# --------------------------------------------------------------

TRANSLATOR_LANGS = {
    "en": "English",
    "fi": "Finnish",
    "sv": "Swedish",
}

TRANSLATOR_DROPDOWN = {
    "en": ["English", "Finnish", "Swedish"],
    "fi": ["Englanti", "Suomi", "Ruotsi"],
    "sv": ["Engelska", "Finska", "Svenska"],
}[ui_lang]

TRANSLATOR_MAP = {
    "English": "English",
    "Finnish": "Finnish",
    "Swedish": "Swedish",
    "Englanti": "English",
    "Suomi": "Finnish",
    "Ruotsi": "Swedish",
    "Engelska": "English",
    "Finska": "Finnish",
    "Svenska": "Swedish",
}


# --------------------------------------------------------------
# MAIN TITLE
# --------------------------------------------------------------

st.title(ui_text("title", ui_lang))



# --------------------------------------------------------------
# STEP 1 — JOB AD
# --------------------------------------------------------------

st.markdown(f"### {ui_text('step1_jobad', ui_lang)}")

job_ad = st.text_area(
    ui_text("job_ad_input", ui_lang),
    height=200,
    key="job_ad_box"
)

if job_ad.strip():
    st.session_state["job_ad"] = job_ad
else:
    job_ad = st.session_state.get("job_ad", "")



# --------------------------------------------------------------
# STEP 2 — UPLOAD CV
# --------------------------------------------------------------

st.markdown(f"### {ui_text('step2_upload', ui_lang)}")

uploaded_file = st.file_uploader(
    ui_text("upload_cv_short", ui_lang),   # ← translated label
    type=["pdf", "txt"],
    help=ui_text("upload_cv_short", ui_lang),   # ← matching help text
    key="cv_uploader"
)

cv_text = None
cv_lang = None

if uploaded_file:
    st.write(ui_text("processing_cv", ui_lang))

    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        raw_text = "".join([(page.extract_text() or "") + "\n" for page in reader.pages])
    else:
        raw_text = uploaded_file.read().decode("utf-8")

    cv_text = parse_cv_text(raw_text)
    cv_lang = detect_cv_language(cv_text)

    st.session_state["cv_text"] = cv_text
    st.session_state["cv_lang"] = cv_lang

    keywords = extract_keywords(cv_text)

    st.subheader(ui_text("extracted_skills", ui_lang))
    if keywords:
        st.success(", ".join(keywords))
    else:
        st.info(ui_text("no_keywords", ui_lang))

else:
    cv_text = st.session_state.get("cv_text")
    cv_lang = st.session_state.get("cv_lang")

# --------------------------------------------------------------
# EMPTY STATE CARD
# --------------------------------------------------------------

if not (cv_text and job_ad.strip()):
    list_items = "<br>".join(ui_text("empty_state_list", ui_lang))
    st.markdown(
        f"""
        <div class="card">
            <h4>{ui_text("empty_state_header", ui_lang)}</h4>
            <p>{ui_text("empty_state_text", ui_lang)}</p>
            <p>{list_items}</p>
        </div>
        """,
        unsafe_allow_html=True
    )



# --------------------------------------------------------------
# RUN ANALYSIS
# --------------------------------------------------------------

analysis_ready = cv_text and job_ad.strip()

if analysis_ready:
    if st.button(ui_text("run_analysis", ui_lang), key="analysis_btn"):
        with st.spinner("Analyzing…"):
            # ✅ FIXED: Pass ui_lang to comparator
            result = compare_cv_to_job(cv_text, job_ad.strip(), ui_lang)
        st.session_state["analysis_result"] = result

result = st.session_state.get("analysis_result")

# --------------------------------------------------------------
# STEP 3 — MATCH ANALYSIS (FIXED — Summary translates with flag changes)
# --------------------------------------------------------------

if result:
    st.markdown(f"### {ui_text('step3_analysis', ui_lang)}")

    score = result["score"]
    missing = result["missing_skills"]
    summary = result["summary"]   # This is in the language when analysis was run
    
    # Store the original summary language if not already stored
    if "original_summary_lang" not in st.session_state:
        st.session_state["original_summary_lang"] = ui_lang
    
    st.metric(ui_text("match_score", ui_lang), f"{score}%")

    if missing:
        st.warning(ui_text("missing_skills", ui_lang) + " " + ", ".join(missing))
    else:
        st.success("✔")

    st.subheader(ui_text("summary", ui_lang))
    
    # ✅ FIXED: Translate summary if UI language changed
    TARGET_LANGUAGE = {
        "en": "English",
        "fi": "Finnish",
        "sv": "Swedish",
    }[ui_lang]
    
    original_lang = st.session_state.get("original_summary_lang", "en")
    
    # If UI language is different from when summary was created, translate it
    if ui_lang != original_lang:
        translated_summary = translate_text(summary, TARGET_LANGUAGE)
        st.write(translated_summary)
    else:
        # Same language, no translation needed
        st.write(summary)

# --------------------------------------------------------------
# STEP 4 — CV REWRITE
# --------------------------------------------------------------

if result:
    st.markdown(f"### {ui_text('step4_rewrite', ui_lang)}")

    CV_STYLE_OPTIONS = {
        "en": [
            "📌 Bullet Points (recruiter-friendly)",
            "✏️ Paragraphs (easy to read)",
            "🧩 Hybrid Format"
        ],
        "fi": [
            "📌 Luettelopisteet (rekrytoijaystävällinen)",
            "✏️ Kappaleet (helppolukuiset)",
            "🧩 Hybridimalli"
        ],
        "sv": [
            "📌 Punktlista (rekryterarvänlig)",
            "✏️ Stycken (lättlästa)",
            "🧩 Hybridmodell"
        ]
    }[ui_lang]

    st.markdown('<div class="select-style">', unsafe_allow_html=True)
    selection = st.selectbox(
        ui_text("cv_style", ui_lang),
        CV_STYLE_OPTIONS,
        key="cv_style_box"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # NORMALIZATION
    if (
        "Luettelo" in selection or
        "Luettelopiste" in selection or
        "Bullet" in selection or
        "Punkt" in selection
    ):
        cleaned_format = "Bullet Points (recruiter-friendly)"
    elif (
        "Kappale" in selection or
        "Paragraph" in selection or
        "Stycke" in selection
    ):
        cleaned_format = "Paragraphs (easy to read)"
    else:
        cleaned_format = "Hybrid"

    if st.button(ui_text("rewrite_button", ui_lang), key="rewrite_btn"):
        with st.spinner("Rewriting your CV…"):
            rewritten = rewrite_cv(cv_text, job_ad.strip(), cleaned_format)
        st.session_state["rewritten"] = rewritten

    if "rewritten" in st.session_state:
        st.text_area(ui_text("step4_rewrite", ui_lang) + ":", st.session_state["rewritten"], height=350)

# --------------------------------------------------------------
# STEP 5 — COVER LETTER (UNCHANGED - WORKS PERFECTLY)
# --------------------------------------------------------------

if result:
    st.markdown(f"### {ui_text('step5_cover_letter', ui_lang)}")

    if st.button(ui_text("generate_cover_letter", ui_lang), key="cover_btn"):
        with st.spinner("Generating cover letter…"):
            letter = generate_cover_letter(cv_text, job_ad.strip())
        st.session_state["letter"] = letter

    if "letter" in st.session_state:
        st.text_area(ui_text("step5_cover_letter", ui_lang) + ":", st.session_state["letter"], height=350)

# --------------------------------------------------------------
# STEP 6 — CV TRANSLATOR
# --------------------------------------------------------------

if cv_text:
    st.markdown(f"### {ui_text('step6_translate_cv', ui_lang)}")

    display_choice = st.selectbox(
        ui_text("target_language", ui_lang),
        TRANSLATOR_DROPDOWN,
        key="cv_lang_dd"
    )

    internal_choice = TRANSLATOR_MAP[display_choice]

    if st.button(ui_text("translator_button", ui_lang), key="cv_translate_btn"):
        with st.spinner("Translating CV…"):
            tcv = translate_text(cv_text, internal_choice)
        st.session_state["translated_cv"] = tcv

    if "translated_cv" in st.session_state:
        st.text_area("Translated CV:", st.session_state["translated_cv"], height=300)

# --------------------------------------------------------------
# STEP 7 — COVER LETTER TRANSLATOR
# --------------------------------------------------------------

if "letter" in st.session_state:
    st.markdown(f"### {ui_text('step7_translate_cover', ui_lang)}")

    display_choice = st.selectbox(
        ui_text("target_language", ui_lang),
        TRANSLATOR_DROPDOWN,
        key="letter_lang_dd"
    )

    internal_choice = TRANSLATOR_MAP[display_choice]

    if st.button(ui_text("translator_button_cover", ui_lang), key="translate_letter_btn"):
        with st.spinner("Translating cover letter…"):
            new_letter = translate_text(st.session_state["letter"], internal_choice)
        st.session_state["translated_letter"] = new_letter

    if "translated_letter" in st.session_state:
        st.text_area("Translated Cover Letter:", st.session_state["translated_letter"], height=300)

# --------------------------------------------------------------
# STEP 8 — INTERVIEW PREP (UNCHANGED - WORKS PERFECTLY)
# --------------------------------------------------------------

if result:
    st.markdown(f"### {ui_text('step8_interview', ui_lang)}")

    if st.button(ui_text("interview_button", ui_lang), key="prep_btn"):

        job_lang = detect_language_of_job_ad(job_ad)

        HEADERS = {
            "English": {
                "behavioral": "Behavioral Questions (STAR)",
                "cultural": "Cultural Fit Questions",
                "leadership": "Leadership & Responsibility Questions",
                "redflags": "Red Flags Based on This CV",
                "salary": "Salary & Expectation Questions",
                "tips": "Final Expert Tips",
            },
            "Finnish": {
                "behavioral": "Käyttäytymiskysymykset (STAR)",
                "cultural": "Kulttuurisopivuuden kysymykset",
                "leadership": "Johtajuus- ja vastuukysymykset",
                "redflags": "CV:n mahdolliset heikot kohdat",
                "salary": "Palkka- ja odotuskysymykset",
                "tips": "Asiantuntijan vinkit",
            },
            "Swedish": {
                "behavioral": "Beteendefrågor (STAR)",
                "cultural": "Kulturell passningsfrågor",
                "leadership": "Ledarskaps- och ansvarfrågor",
                "redflags": "Eventuella svagheter i detta CV",
                "salary": "Löne- och förväntningsfrågor",
                "tips": "Experttips",
            },
        }[job_lang]

        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
Generate interview preparation in **{job_lang}** using this CV and job advertisement.

CV:
{cv_text}

Job Ad:
{job_ad}

Format:
1. {HEADERS['behavioral']} — 4 questions + model answers
2. {HEADERS['cultural']} — 4 questions + answers
3. {HEADERS['leadership']} — 4 questions + answers
4. {HEADERS['redflags']} — explain how the applicant should answer them
5. {HEADERS['salary']} — 3 questions + answers
6. {HEADERS['tips']} — 5 concise bullet points
"""

        with st.spinner("Preparing interview questions…"):
            response = client.chat.completions.create(
                model="gpt-4.1",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )

        st.session_state["interview_prep"] = response.choices[0].message.content.strip()

    if "interview_prep" in st.session_state:
        st.text_area(
            ui_text("step8_interview", ui_lang) + ":",
            st.session_state["interview_prep"],
            height=500
        )