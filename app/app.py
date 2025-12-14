import sys
import os

# Ensure backend imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import PyPDF2
from io import BytesIO

from backend.ai_tools import extract_keywords
from backend.cv_parser import parse_cv_text
from backend.comparator import compare_cv_to_job
from backend.cv_rewriter import rewrite_cv, detect_cv_language, detect_language_of_job_ad
from backend.cover_letter import generate_cover_letter
from backend.translator import translate_text
from backend.language_utils import ui_text
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def make_pdf_proper(text: str, filename: str = "document.pdf"):
    """
    Creates a properly formatted PDF with text wrapping.
    No text cutoff issues.
    """
    if not text or not isinstance(text, str):
        # Return empty buffer if invalid input
        buffer = BytesIO()
        buffer.write(b'')
        buffer.seek(0)
        return buffer
    
    buffer = BytesIO()
    
    # Import inside function to avoid namespace issues
    from reportlab.lib.pagesizes import letter as page_letter
    from reportlab.lib.units import inch as page_inch
    
    try:
        # Create PDF with standard letter size
        doc = SimpleDocTemplate(
            buffer,
            pagesize=page_letter,
            rightMargin=0.75*page_inch,
            leftMargin=0.75*page_inch,
            topMargin=0.75*page_inch,
            bottomMargin=0.75*page_inch
        )
        
        # Container for PDF elements
        story = []
        
        # Get default styles
        styles = getSampleStyleSheet()
        
        # Create a custom style for body text
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            spaceAfter=6,
        )
        
        # Split text into paragraphs and add to PDF
        paragraphs = text.split('\n')
        
        for para_text in paragraphs:
            if para_text.strip():
                # Escape special XML/HTML characters that break ReportLab
                para_text = (para_text
                    .replace('&', '&amp;')
                    .replace('<', '&lt;')
                    .replace('>', '&gt;')
                )
                try:
                    # Create paragraph with automatic wrapping
                    para = Paragraph(para_text, normal_style)
                    story.append(para)
                except Exception as e:
                    # If paragraph fails, skip it
                    continue
            else:
                # Add small space for empty lines
                story.append(Spacer(1, 0.1*page_inch))
        
        # Build PDF
        doc.build(story)
        
    except Exception as e:
        # If PDF generation fails completely, return empty buffer
        print(f"PDF generation error: {e}")
        buffer = BytesIO()
        buffer.write(b'')
    
    buffer.seek(0)
    return buffer

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
.flag-bar button {
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
# FLAG SWITCHER — GLOBAL VERSION (7 LANGUAGES)
# --------------------------------------------------------------
fi_png = "https://flagcdn.com/w40/fi.png"
en_png = "https://flagcdn.com/w40/gb.png"
sv_png = "https://flagcdn.com/w40/se.png"
es_png = "https://flagcdn.com/w40/es.png"
pt_png = "https://flagcdn.com/w40/br.png"
fr_png = "https://flagcdn.com/w40/fr.png"
de_png = "https://flagcdn.com/w40/de.png"

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button(f"![]({fi_png})", key="flag_fi"):
        st.session_state.ui_lang = "fi"

with col2:
    if st.button(f"![]({en_png})", key="flag_en"):
        st.session_state.ui_lang = "en"

with col3:
    if st.button(f"![]({sv_png})", key="flag_sv"):
        st.session_state.ui_lang = "sv"

with col4:
    if st.button(f"![]({es_png})", key="flag_es"):
        st.session_state.ui_lang = "es"

with col5:
    if st.button(f"![]({pt_png})", key="flag_pt"):
        st.session_state.ui_lang = "pt-br"

with col6:
    if st.button(f"![]({fr_png})", key="flag_fr"):
        st.session_state.ui_lang = "fr"

with col7:
    if st.button(f"![]({de_png})", key="flag_de"):
        st.session_state.ui_lang = "de"

ui_lang = st.session_state.ui_lang.strip().lower()

# --------------------------------------------------------------
# LANGUAGE SANITY CHECK
# --------------------------------------------------------------
val = st.session_state.ui_lang
if isinstance(val, list):
    ui_lang = val[0].strip().lower()
else:
    ui_lang = str(val).strip().lower()

# --------------------------------------------------------------
# TRANSLATION SYSTEM — CLEAN GLOBAL VERSION
# --------------------------------------------------------------
TRANSLATOR_LANGS = {
    "en": "English",
    "fi": "Finnish",
    "sv": "Swedish",
    "es": "Spanish",
    "pt-br": "Portuguese",
    "fr": "French",
    "de": "German"
}

TRANSLATOR_DROPDOWN = {
    "en": ["English", "Finnish", "Swedish", "Spanish", "Portuguese", "French", "German"],
    "fi": ["Englanti", "Suomi", "Ruotsi", "Espanja", "Portugali", "Ranska", "Saksa"],
    "sv": ["Engelska", "Finska", "Svenska", "Spanska", "Portugisiska", "Franska", "Tyska"],
    "es": ["Inglés", "Finés", "Sueco", "Español", "Portugués", "Francés", "Alemán"],
    "pt-br": ["Inglês", "Finlandês", "Sueco", "Espanhol", "Português", "Francês", "Alemão"],
    "fr": ["Anglais", "Finnois", "Suédois", "Espagnol", "Portugais", "Français", "Allemand"],
    "de": ["Englisch", "Finnisch", "Schwedisch", "Spanisch", "Portugiesisch", "Französisch", "Deutsch"],
}[ui_lang]

TRANSLATOR_MAP = {
    # English UI
    "English": "English",
    "Finnish": "Finnish",
    "Swedish": "Swedish",
    "Spanish": "Spanish",
    "Portuguese": "Portuguese",
    "French": "French",
    "German": "German",

    # FI
    "Englanti": "English",
    "Suomi": "Finnish",
    "Ruotsi": "Swedish",
    "Espanja": "Spanish",
    "Portugali": "Portuguese",
    "Ranska": "French",
    "Saksa": "German",

    # SV
    "Engelska": "English",
    "Finska": "Finnish",
    "Svenska": "Swedish",
    "Spanska": "Spanish",
    "Portugisiska": "Portuguese",
    "Franska": "French",
    "Tyska": "German",

    # ES
    "Inglés": "English",
    "Finés": "Finnish",
    "Sueco": "Swedish",
    "Español": "Spanish",
    "Portugués": "Portuguese",
    "Francés": "French",
    "Alemán": "German",

    # PT-BR
    "Inglês": "English",
    "Finlandês": "Finnish",
    "Sueco": "Swedish",
    "Espanhol": "Spanish",
    "Português": "Portuguese",
    "Francês": "French",
    "Alemão": "German",

    # FR
    "Anglais": "English",
    "Finnois": "Finnish",
    "Suédois": "Swedish",
    "Espagnol": "Spanish",
    "Portugais": "Portuguese",
    "Français": "French",
    "Allemand": "German",

    # DE
    "Englisch": "English",
    "Finnisch": "Finnish",
    "Schwedisch": "Swedish",
    "Spanisch": "Spanish",
    "Portugiesisch": "Portuguese",
    "Französisch": "French",
    "Deutsch": "German"
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

    # Extract job keywords (raw) then refine them using ATS engine
    from backend.ats_scanner import refine_job_keywords

    raw_kw = extract_keywords(job_ad)
    st.session_state["job_keywords"] = refine_job_keywords(raw_kw)
else:
    job_ad = st.session_state.get("job_ad", "")

# --------------------------------------------------------------
# STEP 2 — UPLOAD CV
# --------------------------------------------------------------
st.markdown(f"### {ui_text('step2_upload', ui_lang)}")

uploaded_file = st.file_uploader(
    ui_text("upload_cv_short", ui_lang),
    type=["pdf", "txt"],
    help=ui_text("upload_cv_short", ui_lang),
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
            result = compare_cv_to_job(cv_text, job_ad.strip(), ui_lang)
            st.session_state["analysis_result"] = result

result = st.session_state.get("analysis_result")

# --------------------------------------------------------------
# STEP 3 — MATCH ANALYSIS (FULL FIXED BLOCK)
# --------------------------------------------------------------
if result:
    st.markdown(f"### {ui_text('step3_analysis', ui_lang)}")

    score = result["score"]
    missing = result["missing_skills"]
    summary = result["summary"]

    # Store the language that produced the summary
    if "original_summary_lang" not in st.session_state:
        st.session_state["original_summary_lang"] = ui_lang

    # Match score
    st.metric(ui_text("match_score", ui_lang), f"{score}%")

    # ----------------------------------------------------------
    # MISSING SKILLS CARD — LABEL IN UI LANGUAGE, CONTENT IN JOB-AD LANGUAGE
    # ----------------------------------------------------------
    if missing:
        # Get the label in UI language
        label = ui_text("missing_skills", ui_lang)

        # Detect job-ad language for translating the actual skills
        job_lang_name = detect_language_of_job_ad(job_ad) if job_ad else "English"
        
        # Create the missing skills text
        missing_sentence = ", ".join(missing)
        
        # Only translate if languages are different
        cv_lang_name = detect_cv_language(cv_text) if cv_text else "English"
        
        # If job ad and CV are in the same language, no translation needed
        if job_lang_name.lower() == cv_lang_name.lower():
            translated_missing = missing_sentence
        else:
            translated_missing = translate_text(missing_sentence, job_lang_name)

        # Display: UI language label + job-ad language content
        st.warning(f"**{label}:** {translated_missing}")
    else:
        st.success("✔")

    # ----------------------------------------------------------
    # SUMMARY TRANSLATION (UNCHANGED — STAYS IN UI LANGUAGE)
    # ----------------------------------------------------------
    st.subheader(ui_text("summary", ui_lang))

    TARGET_LANGUAGE = {
        "en": "English",
        "fi": "Finnish",
        "sv": "Swedish",
        "es": "Spanish",
        "pt-br": "Portuguese",
        "fr": "French",
        "de": "German"
    }[ui_lang]

    original_lang = st.session_state.get("original_summary_lang", "en")

    # Always re-translate when UI changes OR Portuguese is selected
    must_translate = (ui_lang != original_lang) or (ui_lang == "pt-br")

    if must_translate:
        translated_summary = translate_text(summary, TARGET_LANGUAGE)
        st.write(translated_summary)
    else:
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
        ],
        "es": [
            "📌 Viñetas (amigable para reclutadores)",
            "✏️ Párrafos (fáciles de leer)",
            "🧩 Formato híbrido"
        ],
        "pt-br": [
            "📌 Tópicos (bom para recrutadores)",
            "✏️ Parágrafos (fácil de ler)",
            "🧩 Formato híbrido"
        ],
        "fr": [
            "📌 Puces (lisible pour recruteurs)",
            "✏️ Paragraphes (faciles à lire)",
            "🧩 Format hybride"
        ],
        "de": [
            "📌 Stichpunkte (recruiterfreundlich)",
            "✏️ Absätze (leicht zu lesen)",
            "🧩 Hybridformat"
        ]
    }[ui_lang]

    st.markdown('<div class="select-style">', unsafe_allow_html=True)
    selection = st.selectbox(
        ui_text("cv_style", ui_lang),
        CV_STYLE_OPTIONS,
        key="cv_style_box"
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if any(word in selection.lower() for word in ["bullet", "luettelo", "punkt", "viñ", "tóp", "puce", "stich"]):
        cleaned_format = "Bullet Points (recruiter-friendly)"
    elif any(word in selection.lower() for word in ["paragraph", "kappale", "stycke", "pár", "pará", "paragraphe", "absatz"]):
        cleaned_format = "Paragraphs (easy to read)"
    else:
        cleaned_format = "Hybrid"

    # ----------------------------------------------------------
    # REWRITE BUTTON (with ATS keyword boost)
    # ----------------------------------------------------------
    if st.button(ui_text("rewrite_button", ui_lang), key="rewrite_btn"):
        with st.spinner("Rewriting your CV…"):

            rewrite_boost = st.session_state.get("rewrite_hint", "")
            if rewrite_boost:
                boosted_job_ad = (
                    job_ad.strip()
                    + "\n\n"
                    + "## INTERNAL LLM GUIDANCE (Do NOT include this section verbatim in the CV output)\n"
                    + "The following keywords are important for ATS alignment. Use them naturally and contextually.\n"
                    + "Do NOT copy this list into the CV. Do NOT create a section for it.\n"
                    + "KEYWORDS:\n"
                    + rewrite_boost
                )
            else:
                boosted_job_ad = job_ad.strip()

            rewritten = rewrite_cv(cv_text, boosted_job_ad, cleaned_format)

            st.session_state["rewritten"] = rewritten
            st.session_state["rewrite_hint"] = ""

# ----------------------------------------------------------
# SHOW REWRITTEN CV + TXT DOWNLOAD ONLY
# ----------------------------------------------------------
if "rewritten" in st.session_state:
    st.text_area(
        ui_text("step4_rewrite", ui_lang) + ":",
        st.session_state["rewritten"],
        height=350
    )

    # Two download buttons side by side
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["rewritten"],  # ← FIXED: Use "rewritten" not "letter"
            file_name="cv.txt",                  # ← FIXED: Correct filename
            mime="text/plain",
            key="dl_cv_txt"                      # ← FIXED: Correct key
        )

    with col2:
        # Generate PDF only when button is ready to download
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["rewritten"]),  # ← FIXED
            file_name="cv.pdf",                                     # ← FIXED
            mime="application/pdf",
            key="dl_cv_pdf"                                        # ← FIXED
        )
        
    # ATS hint preview
    if st.session_state.get("rewrite_hint"):
        st.info(
            ui_text("ats_missing_add_these", ui_lang)
            + ": "
            + st.session_state["rewrite_hint"]
        )
# --------------------------------------------------------------
# STEP 4.1 — ATS COMPATIBILITY REPORT — CV SCORE & FIXES
# --------------------------------------------------------------
from backend.ats_scanner import run_ats_analysis

st.markdown(f"### {ui_text('step4_1_ats_header', ui_lang)}")

# Require a rewritten CV
if "rewritten" not in st.session_state or not st.session_state["rewritten"].strip():
    st.info(ui_text("ats_rewrite_first", ui_lang))

else:
    rewritten_cv = st.session_state["rewritten"]
    job_keywords = st.session_state.get("job_keywords", set())

    # ----------------------------------------------------------
    # RUN ATS BUTTON
    # ----------------------------------------------------------
    if st.button(ui_text("ats_scan_button", ui_lang), key="ats_scan_btn"):
        with st.spinner(ui_text("processing_cv", ui_lang)):
            try:
                ats = run_ats_analysis(job_keywords, rewritten_cv)
                st.session_state["ats_result"] = ats
            except Exception as e:
                st.error(f"ATS scan failed: {e}")

    ats_result = st.session_state.get("ats_result")

    if ats_result:

        final_score = ats_result["final_score"]
        keyword_score = ats_result["keyword_score"]
        formatting_score = ats_result["formatting_score"]
        found = ats_result["found_keywords"]
        missing = ats_result["missing_keywords"]
        job_kw = ats_result["job_keywords"]

        # ---------- SCORE CIRCLE ----------
        if final_score < 60:
            score_color = "#FF3B30"
        elif final_score < 80:
            score_color = "#FF9500"
        else:
            score_color = "#34C759"

        st.markdown(f"""
        <div style="
            width: 160px;
            height: 160px;
            border-radius: 100%;
            background-color: {score_color}22;
            border: 4px solid {score_color};
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 20px auto;
        ">
            <h1 style="color:{score_color}; font-size:48px; margin:0;">
                {final_score}
            </h1>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(
            f"<p style='text-align:center; color:#d1d1d7;'>{ui_text('ats_score_explanation', ui_lang)}</p>",
            unsafe_allow_html=True
        )

        # ---------- FOUND / MISSING ----------
        st.markdown(f"### {ui_text('ats_keyword_coverage', ui_lang)}")

        colA, colB = st.columns(2)

        with colA:
            st.markdown(f"**{ui_text('ats_keywords_found', ui_lang)}**")
            if found:
                tags = " ".join(
                    [
                        f"<span style='background:#32D74B33; color:#32D74B; padding:4px 10px; border-radius:8px; margin:2px; display:inline-block;'>{kw}</span>"
                        for kw in found
                    ]
                )
                st.markdown(tags, unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<span style='color:#999;'>{ui_text('ats_tag_none', ui_lang)}</span>",
                    unsafe_allow_html=True
                )

        with colB:
            st.markdown(f"**{ui_text('ats_keywords_missing', ui_lang)}**")
            if missing:
                tags = " ".join(
                    [
                        f"<span style='background:#FF696122; color:#FF453A; padding:4px 10px; border-radius:8px; margin:2px; display:inline-block;'>{kw}</span>"
                        for kw in missing
                    ]
                )
                st.markdown(tags, unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<span style='color:#32D74B;'>{ui_text('ats_passed', ui_lang)}</span>",
                    unsafe_allow_html=True
                )

        # ---------- FORMATTING CARD ----------
        st.markdown(f"### {ui_text('ats_formatting_quality', ui_lang)}")

        card_html = f"""
        <div style="
            background:#1C1C1E;
            border:1px solid #333;
            border-radius:12px;
            padding:16px;
            color:#eee;
        ">
            <p><strong>{ui_text('ats_headings_score', ui_lang)}:</strong> {ats_result['headings_score']}/10</p>
            <p><strong>{ui_text('ats_dates_score', ui_lang)}:</strong> {ats_result['dates_score']}/10</p>
            <p><strong>{ui_text('ats_formatting_score', ui_lang)}:</strong> {ats_result['structure_score']}/10</p>
            <p><strong>{ui_text('ats_overall_rating', ui_lang)}:</strong> {formatting_score}/10</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)

        # ---------- FIX & REGENERATE ----------
        if missing:
            st.warning(
                ui_text("ats_overwrite_warning", ui_lang)
            )

            if st.button(ui_text("ats_fix_and_regenerate", ui_lang), key="ats_fix_btn"):

                injected_job_ad = (
                    st.session_state["job_ad"].strip()
                    + "\n\n"
                    + "## INTERNAL LLM GUIDANCE (Do NOT include this section verbatim in the CV output)\n"
                    + "Use these keywords naturally; do not output this list.\n"
                    + "KEYWORDS:\n"
                    + ", ".join(missing)
                )

                with st.spinner("Regenerating your CV with missing ATS keywords…"):
                    try:
                        updated_cv = rewrite_cv(
                            st.session_state["cv_text"],
                            injected_job_ad,
                            "Hybrid"
                        )
                    except Exception as e:
                        st.error(f"Rewrite failed: {e}")
                        updated_cv = st.session_state["rewritten"]

                st.session_state["rewritten"] = updated_cv

                with st.spinner(ui_text("processing_cv", ui_lang)):
                    new_ats = run_ats_analysis(job_keywords, updated_cv)
                    st.session_state["ats_result"] = new_ats

                st.success(ui_text("ats_scan_complete", ui_lang))
                st.rerun()

# --------------------------------------------------------------
# STEP 5 — COVER LETTER
# --------------------------------------------------------------
if result:
    st.markdown(f"### {ui_text('step5_cover_letter', ui_lang)}")

    if st.button(ui_text("generate_cover_letter", ui_lang), key="cover_btn"):
        with st.spinner("Generating cover letter…"):
            letter = generate_cover_letter(cv_text, job_ad.strip())
            st.session_state["letter"] = letter

# --------------------------------------------------------------
# SHOW COVER LETTER + TXT DOWNLOAD ONLY
# --------------------------------------------------------------
if "letter" in st.session_state:
    st.text_area(
        ui_text("step5_cover_letter", ui_lang) + ":",
        st.session_state["letter"],
        height=350
    )

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["letter"],
            file_name="cover_letter.txt",
            mime="text/plain",
            key="dl_cover_txt"
        )

    with col2:
        # Generate PDF only when button is ready to download
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["letter"]),  # Called inline
            file_name="cover_letter.pdf",
            mime="application/pdf",
            key="dl_cover_pdf"
        )
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


# --------------------------------------------------------------
# SHOW TRANSLATED CV + TXT DOWNLOAD ONLY
# --------------------------------------------------------------
if "translated_cv" in st.session_state:
    st.text_area(
        ui_text("step6_translate_cv", ui_lang) + ":",
        st.session_state["translated_cv"],
        height=300
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["translated_cv"],
            file_name="translated_cv.txt",
            mime="text/plain",
            key="dl_translated_cv_txt"
        )
    
    with col2:
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["translated_cv"]),  # ← Call inline
            file_name="translated_cv.pdf",
            mime="application/pdf",
            key="dl_translated_cv_pdf"
        )
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

# --------------------------------------------------------------
# SHOW TRANSLATED COVER LETTER + TXT DOWNLOAD ONLY
# --------------------------------------------------------------
if "translated_letter" in st.session_state:
    st.text_area(
        ui_text("step7_translate_cover", ui_lang) + ":",
        st.session_state["translated_letter"],
        height=300
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["translated_letter"],
            file_name="translated_cover_letter.txt",
            mime="text/plain",
            key="dl_translated_letter_txt"
        )
    
    with col2:
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["translated_letter"]),  # ← Call inline
            file_name="translated_cover_letter.pdf",
            mime="application/pdf",
            key="dl_translated_letter_pdf"
        )

# --------------------------------------------------------------
# STEP 8 — INTERVIEW PREP
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
            "Spanish": {
                "behavioral": "Preguntas Conductuales (STAR)",
                "cultural": "Preguntas de Encaje Cultural",
                "leadership": "Preguntas de Liderazgo y Responsabilidad",
                "redflags": "Posibles puntos débiles del CV",
                "salary": "Preguntas sobre salario y expectativas",
                "tips": "Consejos finales del experto",
            },
            "Portuguese": {
                "behavioral": "Perguntas Comportamentais (STAR)",
                "cultural": "Perguntas de Adequação Cultural",
                "leadership": "Perguntas de Liderança y Responsabilidad",
                "redflags": "Possíveis pontos fracos do CV",
                "salary": "Perguntas sobre salário y expectativas",
                "tips": "Dicas finais do especialista",
            },
            "French": {
                "behavioral": "Questions comportementales (STAR)",
                "cultural": "Questions d'adéquation culturelle",
                "leadership": "Questions de leadership et responsabilité",
                "redflags": "Points faibles possibles du CV",
                "salary": "Questions sur le salaire et les attentes",
                "tips": "Conseils d'expert",
            },
            "German": {
                "behavioral": "Verhaltensfragen (STAR)",
                "cultural": "Fragen zur kulturellen Passung",
                "leadership": "Führungs- und Verantwortungsfragen",
                "redflags": "Mögliche Schwächen im Lebenslauf",
                "salary": "Fragen zu Gehalt und Erwartungen",
                "tips": "Expertentipps",
            },
        }[job_lang]

        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        Generate interview preparation in **{job_lang}** using this CV and job advertisement.

        CV: {cv_text}

        Job Ad: {job_ad}

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

# --------------------------------------------------------------
# SHOW INTERVIEW PREP + TXT DOWNLOAD ONLY
# --------------------------------------------------------------
if "interview_prep" in st.session_state:
    st.text_area(
        ui_text("step8_interview", ui_lang) + ":",
        st.session_state["interview_prep"],
        height=500
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["interview_prep"],
            file_name="interview_prep.txt",
            mime="text/plain",
            key="dl_interview_txt"
        )
    
    with col2:
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["interview_prep"]),  # ← Call inline
            file_name="interview_prep.pdf",
            mime="application/pdf",
            key="dl_interview_pdf"
        )
# --------------------------------------------------------------
# STEP 11 — BIAS & AUTHENTICITY AUDITOR
# --------------------------------------------------------------

from backend.bias_auditor import audit_text

st.markdown(f"### {ui_text('step11_bias_header', ui_lang)}")

# Determine which text we audit
text_to_audit = ""

if "rewritten" in st.session_state and st.session_state["rewritten"]:
    text_to_audit = st.session_state["rewritten"]
elif "letter" in st.session_state and st.session_state["letter"]:
    text_to_audit = st.session_state["letter"]
else:
    st.info(ui_text("ats_no_rewritten_cv", ui_lang))
    text_to_audit = ""

audit_input = st.text_area(
    ui_text("bias_text_to_audit", ui_lang),
    value=text_to_audit,
    height=300
)

run_audit = st.button(ui_text("bias_run_button", ui_lang))

if run_audit and audit_input.strip():

    result = audit_text(audit_input)

    st.subheader(ui_text("bias_score_label", ui_lang))
    st.metric(
        label=ui_text("bias_score_label", ui_lang),
        value=f"{result['final_score']} / 100"
    )

    st.subheader(ui_text("bias_breakdown_header", ui_lang))
    st.table({
        ui_text("bias_category_header", ui_lang): [
            ui_text("bias_slop", ui_lang),
            ui_text("bias_bias", ui_lang),
            ui_text("bias_length", ui_lang)
        ],
        ui_text("bias_score_header", ui_lang): [
            result["slop_score"],
            result["bias_score"],
            result["length_score"]
        ]
    })

    st.subheader(ui_text("bias_found_issues", ui_lang))
    if result["issues"]:
        for issue in result["issues"]:
            translated_issue = translate_text(issue, TRANSLATOR_LANGS[ui_lang])
            st.write(f"- {translated_issue}")

    else:
        st.write(ui_text("bias_no_issues", ui_lang))

    # TXT download of the audited text
    st.download_button(
        label=ui_text("download_txt", ui_lang),
        data=audit_input,
        file_name="audited_text.txt",
        mime="text/plain",
        key="dl_audit_txt"
    )

    st.download_button(
        label=ui_text("download_pdf", ui_lang),
        data=make_pdf_proper(audit_input),
        file_name="audited_text.pdf",
        mime="application/pdf",
        key="dl_audit_pdf"
    )

# --------------------------------------------------------------
# OPTIONAL — HUMAN QUIRKS & VARIATIONS
# --------------------------------------------------------------
enable_quirks = st.checkbox(ui_text("bias_add_quirks", ui_lang))

if enable_quirks and audit_input.strip():

    modified = audit_input

    replacements = [
        ("Additionally,", "Also,"),
        ("Furthermore,", "Plus,"),
        ("In addition,", "On top of that,"),
        ("Moreover,", "What's more,"),
    ]
    for a, b in replacements:
        modified = modified.replace(a, b)

    modified = modified.replace(". ", ".  ")

    st.session_state["quirky_text"] = modified
    st.write(f"### {ui_text('bias_modified_header', ui_lang)}")
    st.text_area(
        ui_text("bias_modified_label", ui_lang),
        value=st.session_state["quirky_text"],
        height=300
    )


    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label=ui_text("download_txt", ui_lang),
            data=st.session_state["quirky_text"],
            file_name="modified_text.txt",
            mime="text/plain",
            key="dl_modified_txt"
        )

    with col2:
        st.download_button(
            label=ui_text("download_pdf", ui_lang),
            data=make_pdf_proper(st.session_state["quirky_text"]),
            file_name="modified_text.pdf",
            mime="application/pdf",
            key="dl_modified_pdf"
        )