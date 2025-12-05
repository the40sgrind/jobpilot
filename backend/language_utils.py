# backend/language_utils.py
# Centralized translations for all UI-visible text
# Supports EN / FI / SV

UI_TEXT = {
    # MAIN TITLE
    "title": {
        "en": "🧭 JobPilot — Your AI Job Application Assistant",
        "fi": "🧭 JobPilot — Älykäs työnhakutyökalusi",
        "sv": "🧭 JobPilot — Din AI-jobbansökningsassistent"
    },

    # STEP HEADERS
    "step1_jobad": {
        "en": "1️⃣ Paste the Job Advertisement",
        "fi": "1️⃣ Kopioi ja liitä työpaikkailmoitus",
        "sv": "1️⃣ Klistra in jobbannonsen"
    },
    "step2_upload": {
        "en": "2️⃣ Upload Your CV",
        "fi": "2️⃣ Lataa CV",
        "sv": "2️⃣ Ladda upp ditt CV"
    },
    "step3_analysis": {
        "en": "3️⃣ Match Analysis (AI)",
        "fi": "3️⃣ Vastaavuusanalyysi (AI)",
        "sv": "3️⃣ Matchningsanalys (AI)"
    },
    "step4_rewrite": {
        "en": "4️⃣ Rewrite Your CV",
        "fi": "4️⃣ Kirjoita CV uudelleen",
        "sv": "4️⃣ Skriv om ditt CV"
    },
    "step5_cover_letter": {
        "en": "5️⃣ Cover Letter",
        "fi": "5️⃣ Hakemuskirje",
        "sv": "5️⃣ Personligt brev"
    },
    "step6_translate_cv": {
        "en": "6️⃣ Translate Your CV",
        "fi": "6️⃣ Käännä CV",
        "sv": "6️⃣ Översätt ditt CV"
    },
    "step7_translate_cover": {
        "en": "7️⃣ Translate Cover Letter",
        "fi": "7️⃣ Käännä hakemuskirje",
        "sv": "7️⃣ Översätt personligt brev"
    },
    "step8_interview": {
        "en": "8️⃣ Interview Preparation (AI)",
        "fi": "8️⃣ Haastatteluun valmistautuminen (AI)",
        "sv": "8️⃣ Intervju­förberedelse (AI)"
    },

    # SHORT TEXTS
    "upload_cv_short": {
        "en": "Upload your CV",
        "fi": "Lataa CV",
        "sv": "Ladda upp ditt CV"
    },
    "processing_cv": {
        "en": "Processing your CV...",
        "fi": "Käsitellään CV:tä...",
        "sv": "Bearbetar ditt CV..."
    },

    # MATCH ANALYSIS
    "extracted_skills": {
        "en": "Extracted Skills / Keywords",
        "fi": "Havaitut taidot / avainsanat",
        "sv": "Identifierade färdigheter / nyckelord"
    },
    "no_keywords": {
        "en": "No keywords detected.",
        "fi": "Avainsanoja ei havaittu.",
        "sv": "Inga nyckelord hittades."
    },

    # JOB AD
    "job_ad_input": {
        "en": "Job Advertisement",
        "fi": "Työpaikkailmoitus",
        "sv": "Jobbannons"
    },

    # EMPTY STATE CARD
    "empty_state_header": {
        "en": "💡 Unlock Full Features",
        "fi": "💡 Avaa kaikki toiminnot",
        "sv": "💡 Lås upp alla funktioner"
    },
    "empty_state_text": {
        "en": "Upload your CV and paste a job advertisement to enable:",
        "fi": "Lataa CV ja kopioi ja liitä työpaikkailmoitus käyttääksesi:",
        "sv": "Ladda upp ditt CV och klistra in jobbannonsen för att använda:"
    },
    "empty_state_list": {
        "en": [
            "• AI Match Analysis",
            "• CV Rewrite",
            "• Cover Letter Creation",
            "• CV Translation",
            "• Cover Letter Translation",
            "• AI Interview Preparation"
        ],
        "fi": [
            "• AI-vastaavuusanalyysi",
            "• CV:n uudelleenkirjoitus",
            "• Hakemuskirjeen luonti",
            "• CV:n kääntäminen",
            "• Hakemuskirjeen kääntäminen",
            "• AI-haastatteluun valmistautuminen"
        ],
        "sv": [
            "• AI-matchningsanalys",
            "• CV-omskrivning",
            "• Personligt brev",
            "• Översättning av CV",
            "• Översättning av personligt brev",
            "• AI-intervju­förberedelse"
        ]
    },

    # MATCH ANALYSIS
    "match_score": {
        "en": "Match Score",
        "fi": "Vastaavuusprosentti",
        "sv": "Matchningspoäng"
    },
    "missing_skills": {
        "en": "Missing skills:",
        "fi": "Puuttuvat taidot:",
        "sv": "Saknade färdigheter:"
    },
    "summary": {
        "en": "Summary",
        "fi": "Yhteenveto",
        "sv": "Sammanfattning"
    },
    "run_analysis": {
        "en": "Run Analysis 🔍",
        "fi": "Aja analyysi 🔍",
        "sv": "Kör analys 🔍"
    },

    # CV STYLE
    "cv_style": {
        "en": "CV Style",
        "fi": "CV-tyyli",
        "sv": "CV-stil"
    },
    "cv_style_option_bullets": {
        "en": "📌 Bullet Points (recruiter-friendly)",
        "fi": "📌 Luettelopisteet (rekrytoijaystävällinen)",
        "sv": "📌 Punktlista (rekryterarvänlig)"
    },
    "cv_style_option_paragraphs": {
        "en": "✏️ Paragraphs (easy to read)",
        "fi": "✏️ Kappaleet (helppolukuiset)",
        "sv": "✏️ Stycken (lättlästa)"
    },
    "cv_style_option_hybrid": {
        "en": "🧩 Hybrid Format",
        "fi": "🧩 Hybridimalli",
        "sv": "🧩 Hybridmodell"
    },

    # BUTTONS
    "rewrite_button": {
        "en": "Rewrite My CV ✨",
        "fi": "Kirjoita CV uudelleen ✨",
        "sv": "Skriv om CV ✨"
    },
    "generate_cover_letter": {
        "en": "Generate Cover Letter ✉️",
        "fi": "Luo hakemuskirje ✉️",
        "sv": "Skapa personligt brev ✉️"
    },

    # TRANSLATIONS
    "target_language": {
        "en": "Target Language",
        "fi": "Kohdekieli",
        "sv": "Målspråk"
    },
    "translator_button": {
        "en": "Translate CV 🌍",
        "fi": "Käännä CV 🌍",
        "sv": "Översätt CV 🌍"
    },
    "translator_button_cover": {
        "en": "Translate Cover Letter 🌍",
        "fi": "Käännä hakemuskirje 🌍",
        "sv": "Översätt personligt brev 🌍"
    },

    # INTERVIEW
    "interview_button": {
        "en": "Generate Interview Prep 🎤",
        "fi": "Luo haastattelukysymykset 🎤",
        "sv": "Skapa intervjufrågor 🎤"
    },
}


def ui_text(key: str, lang: str) -> str:
    return UI_TEXT.get(key, {}).get(lang) or UI_TEXT.get(key, {}).get("en", "")
