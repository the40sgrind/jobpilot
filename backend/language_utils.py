# backend/language_utils.py
# Centralized translations for ALL UI-visible text
# Supports EN / FI / SV / ES / PT-BR / FR / DE

UI_TEXT = {
    # ----------------------------------------------------------
    # MAIN TITLE
    # ----------------------------------------------------------
    "title": {
        "en": "🧭 JobPilot — Your AI Job Application Assistant",
        "fi": "🧭 JobPilot — Älykäs työnhakutyökalusi",
        "sv": "🧭 JobPilot — Din AI-jobbansökningsassistent",
        "es": "🧭 JobPilot — Tu asistente de solicitudes laborales con IA",
        "pt-br": "🧭 JobPilot — Seu assistente de candidatura com IA",
        "fr": "🧭 JobPilot — Votre assistant de candidature IA",
        "de": "🧭 JobPilot — Ihr KI-Bewerbungsassistent"
    },

    # ----------------------------------------------------------
    # STEP HEADERS
    # ----------------------------------------------------------
    "step1_jobad": {
        "en": "1️⃣ Paste the Job Advertisement",
        "fi": "1️⃣ Kopioi ja liitä työpaikkailmoitus",
        "sv": "1️⃣ Klistra in jobbannonsen",
        "es": "1️⃣ Pega la oferta de trabajo",
        "pt-br": "1️⃣ Cole a vaga de emprego",
        "fr": "1️⃣ Collez l'offre d’emploi",
        "de": "1️⃣ Fügen Sie die Stellenausschreibung ein"
    },
    "step2_upload": {
        "en": "2️⃣ Upload Your CV",
        "fi": "2️⃣ Lataa CV",
        "sv": "2️⃣ Ladda upp ditt CV",
        "es": "2️⃣ Sube tu CV",
        "pt-br": "2️⃣ Envie seu CV",
        "fr": "2️⃣ Téléversez votre CV",
        "de": "2️⃣ Laden Sie Ihren Lebenslauf hoch"
    },
    "step3_analysis": {
        "en": "3️⃣ Match Analysis (AI)",
        "fi": "3️⃣ Vastaavuusanalyysi (AI)",
        "sv": "3️⃣ Matchningsanalys (AI)",
        "es": "3️⃣ Análisis de compatibilidad (IA)",
        "pt-br": "3️⃣ Análise de compatibilidade (IA)",
        "fr": "3️⃣ Analyse de correspondance (IA)",
        "de": "3️⃣ Übereinstimmungsanalyse (KI)"
    },
    "step4_rewrite": {
        "en": "4️⃣ Rewrite Your CV",
        "fi": "4️⃣ Kirjoita CV uudelleen",
        "sv": "4️⃣ Skriv om ditt CV",
        "es": "4️⃣ Reescribe tu CV",
        "pt-br": "4️⃣ Reescreva seu CV",
        "fr": "4️⃣ Réécrivez votre CV",
        "de": "4️⃣ Schreiben Sie Ihren Lebenslauf neu"
    },
    "step5_cover_letter": {
        "en": "5️⃣ Cover Letter",
        "fi": "5️⃣ Hakemuskirje",
        "sv": "5️⃣ Personligt brev",
        "es": "5️⃣ Carta de presentación",
        "pt-br": "5️⃣ Carta de apresentação",
        "fr": "5️⃣ Lettre de motivation",
        "de": "5️⃣ Anschreiben"
    },
    "step6_translate_cv": {
        "en": "6️⃣ Translate Your CV",
        "fi": "6️⃣ Käännä CV",
        "sv": "6️⃣ Översätt ditt CV",
        "es": "6️⃣ Traduce tu CV",
        "pt-br": "6️⃣ Traduza seu CV",
        "fr": "6️⃣ Traduisez votre CV",
        "de": "6️⃣ Übersetzen Sie Ihren Lebenslauf"
    },
    "step7_translate_cover": {
        "en": "7️⃣ Translate Cover Letter",
        "fi": "7️⃣ Käännä hakemuskirje",
        "sv": "7️⃣ Översätt personligt brev",
        "es": "7️⃣ Traduce la carta de presentación",
        "pt-br": "7️⃣ Traduza a carta de apresentação",
        "fr": "7️⃣ Traduisez la lettre de motivation",
        "de": "7️⃣ Übersetzen Sie das Anschreiben"
    },
    "step8_interview": {
        "en": "8️⃣ Interview Preparation (AI)",
        "fi": "8️⃣ Haastatteluun valmistautuminen (AI)",
        "sv": "8️⃣ Intervju­förberedelse (AI)",
        "es": "8️⃣ Preparación para entrevista (IA)",
        "pt-br": "8️⃣ Preparação para entrevista (IA)",
        "fr": "8️⃣ Préparation à l’entretien (IA)",
        "de": "8️⃣ Vorbereitung auf das Vorstellungsgespräch (KI)"
    },

    # ----------------------------------------------------------
    # SHORT TEXTS
    # ----------------------------------------------------------
    "upload_cv_short": {
        "en": "Upload your CV",
        "fi": "Lataa CV",
        "sv": "Ladda upp ditt CV",
        "es": "Sube tu CV",
        "pt-br": "Envie seu CV",
        "fr": "Téléversez votre CV",
        "de": "Laden Sie Ihren Lebenslauf hoch"
    },
    "processing_cv": {
        "en": "Processing your CV...",
        "fi": "Käsitellään CV:tä...",
        "sv": "Bearbetar ditt CV...",
        "es": "Procesando tu CV...",
        "pt-br": "Processando seu CV...",
        "fr": "Traitement de votre CV…",
        "de": "Lebenslauf wird verarbeitet…"
    },

    # ----------------------------------------------------------
    # MATCH ANALYSIS
    # ----------------------------------------------------------
    "extracted_skills": {
        "en": "Extracted Skills / Keywords",
        "fi": "Havaitut taidot / avainsanat",
        "sv": "Identifierade färdigheter / nyckelord",
        "es": "Habilidades detectadas / palabras clave",
        "pt-br": "Competências identificadas / palavras-chave",
        "fr": "Compétences détectées / mots-clés",
        "de": "Erkannte Fähigkeiten / Schlüsselwörter"
    },
    "no_keywords": {
        "en": "No keywords detected.",
        "fi": "Avainsanoja ei havaittu.",
        "sv": "Inga nyckelord hittades.",
        "es": "No se detectaron palabras clave.",
        "pt-br": "Nenhuma palavra-chave identificada.",
        "fr": "Aucun mot-clé détecté.",
        "de": "Keine Schlüsselwörter gefunden."
    },

    # ----------------------------------------------------------
    # JOB AD
    # ----------------------------------------------------------
    "job_ad_input": {
        "en": "Job Advertisement",
        "fi": "Työpaikkailmoitus",
        "sv": "Jobbannons",
        "es": "Oferta de trabajo",
        "pt-br": "Vaga de emprego",
        "fr": "Offre d’emploi",
        "de": "Stellenanzeige"
    },

    # ----------------------------------------------------------
    # EMPTY STATE CARD
    # ----------------------------------------------------------
    "empty_state_header": {
        "en": "💡 Unlock Full Features",
        "fi": "💡 Avaa kaikki toiminnot",
        "sv": "💡 Lås upp alla funktioner",
        "es": "💡 Desbloquea todas las funciones",
        "pt-br": "💡 Desbloqueie todas as funções",
        "fr": "💡 Débloquez toutes les fonctionnalités",
        "de": "💡 Schalten Sie alle Funktionen frei"
    },
    "empty_state_text": {
        "en": "Upload your CV and paste a job advertisement to enable:",
        "fi": "Lataa CV ja liitä työilmoitus käyttääksesi:",
        "sv": "Ladda upp ditt CV och klistra in jobbannonsen för att använda:",
        "es": "Sube tu CV y pega una oferta para habilitar:",
        "pt-br": "Envie seu CV e cole a vaga para habilitar:",
        "fr": "Téléversez votre CV et collez une offre pour activer :",
        "de": "Laden Sie Ihren Lebenslauf hoch und fügen Sie eine Anzeige ein, um zu aktivieren:"
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
        ],
        "es": [
            "• Análisis de compatibilidad IA",
            "• Reescritura de CV",
            "• Creación de carta de presentación",
            "• Traducción de CV",
            "• Traducción de carta",
            "• Preparación de entrevista IA"
        ],
        "pt-br": [
            "• Análise de compatibilidade com IA",
            "• Reescrita de CV",
            "• Criação de carta de apresentação",
            "• Tradução de CV",
            "• Tradução de carta",
            "• Preparação para entrevista com IA"
        ],
        "fr": [
            "• Analyse de correspondance IA",
            "• Réécriture du CV",
            "• Création d’une lettre de motivation",
            "• Traduction du CV",
            "• Traduction de lettre",
            "• Préparation d’entretien IA"
        ],
        "de": [
            "• KI-Übereinstimmungsanalyse",
            "• Lebenslauf-Neuschreibung",
            "• Erstellung eines Anschreibens",
            "• Lebenslauf-Übersetzung",
            "• Anschreiben-Übersetzung",
            "• KI-Interviewvorbereitung"
        ]
    },

    # ----------------------------------------------------------
    # MATCH ANALYSIS
    # ----------------------------------------------------------
    "match_score": {
        "en": "Match Score",
        "fi": "Vastaavuusprosentti",
        "sv": "Matchningspoäng",
        "es": "Nivel de compatibilidad",
        "pt-br": "Pontuação de compatibilidade",
        "fr": "Score de correspondance",
        "de": "Übereinstimmungsgrad"
    },
    "missing_skills": {
        "en": "Missing skills:",
        "fi": "Puuttuvat taidot:",
        "sv": "Saknade färdigheter:",
        "es": "Habilidades faltantes:",
        "pt-br": "Competências faltantes:",
        "fr": "Compétences manquantes :",
        "de": "Fehlende Fähigkeiten:"
    },
    "summary": {
        "en": "Summary",
        "fi": "Yhteenveto",
        "sv": "Sammanfattning",
        "es": "Resumen",
        "pt-br": "Resumo",
        "fr": "Résumé",
        "de": "Zusammenfassung"
    },
    "run_analysis": {
        "en": "Run Analysis 🔍",
        "fi": "Aja analyysi 🔍",
        "sv": "Kör analys 🔍",
        "es": "Ejecutar análisis 🔍",
        "pt-br": "Executar análise 🔍",
        "fr": "Lancer l’analyse 🔍",
        "de": "Analyse starten 🔍"
    },

    # ----------------------------------------------------------
    # CV STYLE OPTIONS
    # ----------------------------------------------------------
    "cv_style": {
        "en": "CV Style",
        "fi": "CV-tyyli",
        "sv": "CV-stil",
        "es": "Estilo de CV",
        "pt-br": "Estilo do CV",
        "fr": "Style du CV",
        "de": "Lebenslauf-Stil"
    },
    "cv_style_option_bullets": {
        "en": "📌 Bullet Points (recruiter-friendly)",
        "fi": "📌 Luettelopisteet (rekrytoijaystävällinen)",
        "sv": "📌 Punktlista (rekryterarvänlig)",
        "es": "📌 Viñetas (amigable para reclutadores)",
        "pt-br": "📌 Tópicos (bom para recrutadores)",
        "fr": "📌 Puces (lisible pour recruteurs)",
        "de": "📌 Stichpunkte (recruiterfreundlich)"
    },
    "cv_style_option_paragraphs": {
        "en": "✏️ Paragraphs (easy to read)",
        "fi": "✏️ Kappaleet (helppolukuiset)",
        "sv": "✏️ Stycken (lättlästa)",
        "es": "✏️ Párrafos (fáciles de leer)",
        "pt-br": "✏️ Parágrafos (fáceis de ler)",
        "fr": "✏️ Paragraphes (faciles à lire)",
        "de": "✏️ Absätze (leicht zu lesen)"
    },
    "cv_style_option_hybrid": {
        "en": "🧩 Hybrid Format",
        "fi": "🧩 Hybridimalli",
        "sv": "🧩 Hybridmodell",
        "es": "🧩 Formato híbrido",
        "pt-br": "🧩 Formato híbrido",
        "fr": "🧩 Format hybride",
        "de": "🧩 Hybridformat"
    },

    # ----------------------------------------------------------
    # BUTTONS
    # ----------------------------------------------------------
    "rewrite_button": {
        "en": "Rewrite My CV ✨",
        "fi": "Kirjoita CV uudelleen ✨",
        "sv": "Skriv om CV ✨",
        "es": "Reescribir CV ✨",
        "pt-br": "Reescrever CV ✨",
        "fr": "Réécrire CV ✨",
        "de": "Lebenslauf neu schreiben ✨"
    },
    "generate_cover_letter": {
        "en": "Generate Cover Letter ✉️",
        "fi": "Luo hakemuskirje ✉️",
        "sv": "Skapa personligt brev ✉️",
        "es": "Generar carta de presentación ✉️",
        "pt-br": "Gerar carta de apresentação ✉️",
        "fr": "Générer lettre de motivation ✉️",
        "de": "Anschreiben erstellen ✉️"
    },

    # ----------------------------------------------------------
    # TRANSLATOR UI
    # ----------------------------------------------------------
    "target_language": {
        "en": "Target Language",
        "fi": "Kohdekieli",
        "sv": "Målspråk",
        "es": "Idioma de destino",
        "pt-br": "Idioma de destino",
        "fr": "Langue cible",
        "de": "Zielsprache"
    },
    "translator_button": {
        "en": "Translate CV 🌍",
        "fi": "Käännä CV 🌍",
        "sv": "Översätt CV 🌍",
        "es": "Traducir CV 🌍",
        "pt-br": "Traduzir CV 🌍",
        "fr": "Traduire CV 🌍",
        "de": "Lebenslauf übersetzen 🌍"
    },
    "translator_button_cover": {
        "en": "Translate Cover Letter 🌍",
        "fi": "Käännä hakemuskirje 🌍",
        "sv": "Översätt personligt brev 🌍",
        "es": "Traducir carta de presentación 🌍",
        "pt-br": "Traduzir carta 🌍",
        "fr": "Traduire lettre 🌍",
        "de": "Anschreiben übersetzen 🌍"
    },

    # ----------------------------------------------------------
    # INTERVIEW
    # ----------------------------------------------------------
    "interview_button": {
        "en": "Generate Interview Prep 🎤",
        "fi": "Luo haastattelukysymykset 🎤",
        "sv": "Skapa intervjufrågor 🎤",
        "es": "Generar preparación para entrevista 🎤",
        "pt-br": "Gerar preparação para entrevista 🎤",
        "fr": "Générer préparation à l’entretien 🎤",
        "de": "Interviewvorbereitung erstellen 🎤"
    },
}


def ui_text(key: str, lang: str) -> str:
    """
    Returns UI text in the correct language.
    Falls back to English gracefully.
    """
    try:
        return UI_TEXT.get(key, {}).get(lang) or UI_TEXT.get(key, {}).get("en", "")
    except:
        return UI_TEXT.get(key, {}).get("en", "")
