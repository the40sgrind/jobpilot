# backend/language_utils.py

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

    # ⭐ NEW PREMIUM ATS STEP 4.1 (header stays English in all languages)
    "step4_1_ats_header": {
        "en": "ATS Compatibility Report — CV Score & Fixes",
        "fi": "ATS Compatibility Report — CV Score & Fixes",
        "sv": "ATS Compatibility Report — CV Score & Fixes",
        "es": "ATS Compatibility Report — CV Score & Fixes",
        "pt-br": "ATS Compatibility Report — CV Score & Fixes",
        "fr": "ATS Compatibility Report — CV Score & Fixes",
        "de": "ATS Compatibility Report — CV Score & Fixes"
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
    # EMPTY STATE CARD (UNDER STEP 2)
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
    # BUTTONS (NON-ATS)
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

    # ==========================================================
    # ATS KEYWORD SECTIONS — PREMIUM STEP 4.1
    # ==========================================================

    "ats_keywords_from_job": {
        "en": "Keywords from the Job Ad",
        "fi": "Työpaikkailmoituksen avainsanat",
        "sv": "Nyckelord från jobbannonsen",
        "es": "Palabras clave de la oferta laboral",
        "pt-br": "Palavras-chave da vaga",
        "fr": "Mots-clés de l’offre d’emploi",
        "de": "Schlüsselwörter aus der Stellenausschreibung"
    },
    "ats_keywords_found": {
        "en": "Found in Your CV",
        "fi": "Löytyi CV:stäsi",
        "sv": "Hittades i ditt CV",
        "es": "Encontrado en tu CV",
        "pt-br": "Encontrado no seu CV",
        "fr": "Présents dans votre CV",
        "de": "In Ihrem Lebenslauf gefunden"
    },
    "ats_keywords_missing": {
        "en": "Missing Keywords",
        "fi": "Puuttuvat avainsanat",
        "sv": "Saknade nyckelord",
        "es": "Palabras clave faltantes",
        "pt-br": "Palavras-chave faltando",
        "fr": "Mots-clés manquants",
        "de": "Fehlende Schlüsselwörter"
    },
    "ats_missing_add_these": {
        "en": "Add these to improve your ATS score",
        "fi": "Lisää nämä parantaaksesi ATS-pisteitäsi",
        "sv": "Lägg till dessa för att förbättra din ATS-poäng",
        "es": "Añade estos para mejorar tu puntuación ATS",
        "pt-br": "Adicione estes para melhorar sua pontuação ATS",
        "fr": "Ajoutez-les pour améliorer votre score ATS",
        "de": "Fügen Sie diese hinzu, um Ihre ATS-Bewertung zu verbessern"
    },
    "ats_no_keywords_job_ad": {
        "en": "No keywords detected in the job advertisement.",
        "fi": "Työpaikkailmoituksesta ei löytynyt avainsanoja.",
        "sv": "Inga nyckelord hittades i jobbannonsen.",
        "es": "No se detectaron palabras clave en la oferta laboral.",
        "pt-br": "Nenhuma palavra-chave encontrada na vaga.",
        "fr": "Aucun mot-clé trouvé dans l’offre d’emploi.",
        "de": "Keine Schlüsselwörter in der Stellenausschreibung gefunden."
    },
    "ats_job_keywords_title": {
        "en": "Job Ad Keywords",
        "fi": "Työpaikan avainsanat",
        "sv": "Jobbannonsens nyckelord",
        "es": "Palabras clave de la oferta",
        "pt-br": "Palavras-chave da vaga",
        "fr": "Mots-clés de l’offre",
        "de": "Schlüsselwörter der Ausschreibung"
    },
    "ats_cv_keywords_title": {
        "en": "Keywords Detected in Your CV",
        "fi": "CV:stä havaitut avainsanat",
        "sv": "Nyckelord upptäckta i ditt CV",
        "es": "Palabras clave detectadas en tu CV",
        "pt-br": "Palavras-chave detectadas no seu CV",
        "fr": "Mots-clés détectés dans votre CV",
        "de": "Im Lebenslauf erkannte Schlüsselwörter"
    },
    "ats_found_keywords_title": {
        "en": "Matched Keywords",
        "fi": "Vastaavat avainsanat",
        "sv": "Matchade nyckelord",
        "es": "Palabras clave coincidentes",
        "pt-br": "Palavras-chave correspondentes",
        "fr": "Mots-clés correspondants",
        "de": "Übereinstimmende Schlüsselwörter"
    },
    "ats_missing_keywords_title": {
        "en": "Missing Keywords",
        "fi": "Puuttuvat avainsanat",
        "sv": "Saknade nyckelord",
        "es": "Palabras clave faltantes",
        "pt-br": "Palavras-chave faltantes",
        "fr": "Mots-clés manquants",
        "de": "Fehlende Schlüsselwörter"
    },
    "ats_no_rewritten_cv": {
        "en": "Rewrite your CV first to run the ATS compatibility report.",
        "fi": "Kirjoita CV uudelleen ennen ATS-tarkistusta.",
        "sv": "Skriv om ditt CV innan du kör ATS-rapporten.",
        "es": "Reescribe tu CV antes de ejecutar el informe ATS.",
        "pt-br": "Reescreva seu CV antes de executar o relatório ATS.",
        "fr": "Réécrivez votre CV avant d’exécuter le rapport ATS.",
        "de": "Schreiben Sie Ihren Lebenslauf neu, bevor Sie den ATS-Bericht ausführen."
    },
    "ats_no_cv_yet": {
        "en": "No CV detected.",
        "fi": "CV:tä ei löydetty.",
        "sv": "Inget CV hittades.",
        "es": "No se detectó ningún CV.",
        "pt-br": "Nenhum CV encontrado.",
        "fr": "Aucun CV détecté.",
        "de": "Kein Lebenslauf gefunden."
    },
    "ats_rewrite_first": {
        "en": "Rewrite your CV in Step 4 to enable ATS scanning.",
        "fi": "Kirjoita CV uudelleen vaiheessa 4 ottaaksesi ATS-tarkistuksen käyttöön.",
        "sv": "Skriv om ditt CV i steg 4 för att möjliggöra ATS-skanning.",
        "es": "Reescribe tu CV en el paso 4 para activar el análisis ATS.",
        "pt-br": "Reescreva seu CV na etapa 4 para ativar o escaneamento ATS.",
        "fr": "Réécrivez votre CV à l’étape 4 pour activer l’analyse ATS.",
        "de": "Schreiben Sie Ihren Lebenslauf in Schritt 4 neu, um die ATS-Prüfung zu aktivieren."
    },

    "ats_keyword_score": {
        "en": "Keyword Coverage Score",
        "fi": "Avainsanojen kattavuus",
        "sv": "Täckning av nyckelord",
        "es": "Cobertura de palabras clave",
        "pt-br": "Cobertura de palavras-chave",
        "fr": "Couverture des mots-clés",
        "de": "Schlüsselwortabdeckung"
    },
    "ats_headings_score": {
        "en": "Section Headings Score",
        "fi": "Otsikoiden pisteet",
        "sv": "Rubrikpoäng",
        "es": "Puntuación de encabezados",
        "pt-br": "Pontuação de seções",
        "fr": "Score des sections",
        "de": "Abschnittsbewertung"
    },
    "ats_dates_score": {
        "en": "Date Formatting Score",
        "fi": "Päivämäärien muotoilun pisteet",
        "sv": "Datumformatets poäng",
        "es": "Puntuación del formato de fechas",
        "pt-br": "Pontuação de datas",
        "fr": "Score du format des dates",
        "de": "Bewertung des Datumsformats"
    },
    "ats_formatting_score": {
        "en": "Formatting Quality Score",
        "fi": "Muotoilun laatupisteet",
        "sv": "Formateringspoäng",
        "es": "Puntuación de formato",
        "pt-br": "Pontuação de formatação",
        "fr": "Score de mise en forme",
        "de": "Formatierungsbewertung"
    },
    "ats_total_score": {
        "en": "Total ATS Score",
        "fi": "Kokonais-ATS-pisteet",
        "sv": "Total ATS-poäng",
        "es": "Puntuación ATS total",
        "pt-br": "Pontuação ATS total",
        "fr": "Score ATS total",
        "de": "Gesamt-ATS-Bewertung"
    },
    "ats_score_label": {
        "en": "ATS Score",
        "fi": "ATS-pisteet",
        "sv": "ATS-poäng",
        "es": "Puntuación ATS",
        "pt-br": "Pontuação ATS",
        "fr": "Score ATS",
        "de": "ATS-Bewertung"
    },

    "ats_formatting_issues": {
        "en": "Formatting Issues",
        "fi": "Muotoiluongelmat",
        "sv": "Formateringsproblem",
        "es": "Problemas de formato",
        "pt-br": "Problemas de formatação",
        "fr": "Problèmes de mise en forme",
        "de": "Formatierungsprobleme"
    },
    "ats_formatting_heading_issues": {
        "en": "Missing or unclear section headings",
        "fi": "Puuttuvat tai epäselvät otsikot",
        "sv": "Saknade eller oklara rubriker",
        "es": "Encabezados faltantes o poco claros",
        "pt-br": "Cabeçalhos ausentes ou pouco claros",
        "fr": "Rubriques manquantes ou peu claires",
        "de": "Fehlende oder unklare Überschriften"
    },
    "ats_formatting_date_issues": {
        "en": "Incorrect or inconsistent date formats",
        "fi": "Virheelliset tai epäjohdonmukaiset päivämäärämuodot",
        "sv": "Felaktiga eller inkonsekventa datumformat",
        "es": "Fechas incorrectas o inconsistentes",
        "pt-br": "Datas incorretas ou inconsistentes",
        "fr": "Formats de dates incorrects ou incohérents",
        "de": "Fehlerhafte oder uneinheitliche Datumsformate"
    },
    "ats_formatting_structure_issues": {
        "en": "Layout elements not ATS-friendly (tables, columns, images, text boxes)",
        "fi": "Asettelu ei ole ATS-yhteensopiva (taulukot, sarakkeet, kuvat, tekstilaatikot)",
        "sv": "Layout ej ATS-vänlig (tabeller, kolumner, bilder, textrutor)",
        "es": "Estructura no compatible con ATS (tablas, columnas, imágenes, cuadros de texto)",
        "pt-br": "Layout incompatível com ATS (tabelas, colunas, imagens, caixas de texto)",
        "fr": "Mise en page non compatible ATS (tableaux, colonnes, images, zones de texte)",
        "de": "Layout nicht ATS-konform (Tabellen, Spalten, Bilder, Textfelder)"
    },

    "ats_score_explanation": {
        "en": "Your ATS score is based on keyword relevance (70%) and formatting quality (30%).",
        "fi": "ATS-pisteet perustuvat avainsanoihin (70 %) ja muotoilun laatuun (30 %).",
        "sv": "Din ATS-poäng baseras på nyckelordsrelevans (70 %) och formateringskvalitet (30 %).",
        "es": "Tu puntuación ATS se basa en relevancia de palabras clave (70 %) y calidad de formato (30 %).",
        "pt-br": "Sua pontuação ATS é baseada em relevância das palavras-chave (70 %) e qualidade de formatação (30 %).",
        "fr": "Votre score ATS est basé sur la pertinence des mots-clés (70 %) et la qualité de mise en forme (30 %).",
        "de": "Ihre ATS-Bewertung basiert auf Schlüsselwortrelevanz (70 %) und Formatierungsqualität (30 %)."
    },

    "ats_keyword_coverage": {
        "en": "Keyword Coverage",
        "fi": "Avainsanojen kattavuus",
        "sv": "Täckning av nyckelord",
        "es": "Cobertura de palabras clave",
        "pt-br": "Cobertura de palavras-chave",
        "fr": "Couverture des mots-clés",
        "de": "Schlüsselwortabdeckung"
    },
    "ats_formatting_quality": {
        "en": "Formatting Quality",
        "fi": "Muotoilun laatu",
        "sv": "Formateringskvalitet",
        "es": "Calidad del formato",
        "pt-br": "Qualidade da formatação",
        "fr": "Qualité de mise en forme",
        "de": "Formatierungsqualität"
    },
    "ats_overall_rating": {
        "en": "Overall Rating",
        "fi": "Kokonaisarvio",
        "sv": "Totalbetyg",
        "es": "Valoración general",
        "pt-br": "Avaliação geral",
        "fr": "Évaluation globale",
        "de": "Gesamtbewertung"
    },

    "ats_scan_button": {
        "en": "Run ATS Scan 🔍",
        "fi": "Aja ATS-tarkistus 🔍",
        "sv": "Kör ATS-skanning 🔍",
        "es": "Ejecutar análisis ATS 🔍",
        "pt-br": "Executar análise ATS 🔍",
        "fr": "Lancer l’analyse ATS 🔍",
        "de": "ATS-Scan starten 🔍"
    },
    "ats_fix_and_regenerate": {
        "en": "Fix My CV & Regenerate ✨",
        "fi": "Korjaa CV ja luo uudelleen ✨",
        "sv": "Åtgärda CV och återskapa ✨",
        "es": "Corregir CV y regenerar ✨",
        "pt-br": "Corrigir CV e regenerar ✨",
        "fr": "Corriger le CV et régénérer ✨",
        "de": "Lebenslauf korrigieren & neu erstellen ✨"
    },

    "ats_scan_complete": {
        "en": "ATS scan complete.",
        "fi": "ATS-tarkistus valmis.",
        "sv": "ATS-skanningen klar.",
        "es": "Análisis ATS completado.",
        "pt-br": "Análise ATS concluída.",
        "fr": "Analyse ATS terminée.",
        "de": "ATS-Scan abgeschlossen."
    },
    "ats_passed": {
        "en": "Your CV is ATS-ready. Great work!",
        "fi": "CV:si on ATS-yhteensopiva. Hienoa työtä!",
        "sv": "Ditt CV är ATS-redo. Bra jobbat!",
        "es": "Tu CV está listo para ATS. ¡Excelente trabajo!",
        "pt-br": "Seu CV está pronto para ATS. Ótimo trabalho!",
        "fr": "Votre CV est compatible ATS. Excellent travail !",
        "de": "Ihr CV ist ATS-kompatibel. Gute Arbeit!"
    },
    "ats_risky": {
        "en": "Your CV may struggle with ATS filters.",
        "fi": "CV:si voi kohdata haasteita ATS-järjestelmissä.",
        "sv": "Ditt CV kan få problem med ATS-filter.",
        "es": "Tu CV podría tener dificultades con filtros ATS.",
        "pt-br": "Seu CV pode ter dificuldades nos filtros ATS.",
        "fr": "Votre CV pourrait rencontrer des difficultés avec les filtres ATS.",
        "de": "Ihr CV könnte Probleme mit ATS-Filtern haben."
    },
    "ats_failed": {
        "en": "Your CV is not ATS-friendly. Fixes strongly recommended.",
        "fi": "CV:si ei ole ATS-yhteensopiva. Korjaukset ovat erittäin suositeltavia.",
        "sv": "Ditt CV är inte ATS-vänligt. Åtgärder rekommenderas starkt.",
        "es": "Tu CV no es compatible con ATS. Se recomiendan mejoras urgentes.",
        "pt-br": "Seu CV não é compatível com ATS. Correções são fortemente recomendadas.",
        "fr": "Votre CV n’est pas compatible ATS. Des corrections sont fortement recommandées.",
        "de": "Ihr CV ist nicht ATS-freundlich. Verbesserungen werden dringend empfohlen."
    },

    "ats_tag_found": {
        "en": "Found",
        "fi": "Löytyi",
        "sv": "Hittad",
        "es": "Encontrado",
        "pt-br": "Encontrado",
        "fr": "Trouvé",
        "de": "Gefunden"
    },
    "ats_tag_missing": {
        "en": "Missing",
        "fi": "Puuttuu",
        "sv": "Saknas",
        "es": "Faltante",
        "pt-br": "Faltando",
        "fr": "Manquant",
        "de": "Fehlt"
    },
    "ats_tag_job_ad": {
        "en": "Job Ad",
        "fi": "Työpaikkailmoitus",
        "sv": "Jobbannons",
        "es": "Oferta laboral",
        "pt-br": "Vaga",
        "fr": "Offre d’emploi",
        "de": "Stellenanzeige"
    },
    "ats_tag_cv_contains": {
        "en": "Your CV Contains",
        "fi": "CV:ssäsi esiintyy",
        "sv": "Ditt CV innehåller",
        "es": "Tu CV contiene",
        "pt-br": "Seu CV contém",
        "fr": "Présent dans votre CV",
        "de": "Ihr CV enthält"
    },
    "ats_tag_add_these": {
        "en": "Add These",
        "fi": "Lisää nämä",
        "sv": "Lägg till dessa",
        "es": "Añade estos",
        "pt-br": "Adicione estes",
        "fr": "Ajoutez-les",
        "de": "Diese hinzufügen"
    },
    "ats_tag_none": {
        "en": "No keywords found yet.",
        "fi": "Avainsanoja ei löytynyt vielä.",
        "sv": "Inga nyckelord hittades ännu.",
        "es": "Todavía no se encontraron palabras clave.",
        "pt-br": "Nenhuma palavra-chave encontrada ainda.",
        "fr": "Aucun mot-clé trouvé pour le moment.",
        "de": "Noch keine Schlüsselwörter gefunden."
    },

    "ats_congrats": {
        "en": "Excellent! Your CV meets modern ATS standards.",
        "fi": "Erinomaista! CV:si täyttää nykyaikaiset ATS-vaatimukset.",
        "sv": "Utmärkt! Ditt CV uppfyller moderna ATS-standarder.",
        "es": "¡Excelente! Tu CV cumple con los estándares ATS modernos.",
        "pt-br": "Excelente! Seu CV atende aos padrões ATS modernos.",
        "fr": "Excellent ! Votre CV respecte les standards ATS modernes.",
        "de": "Ausgezeichnet! Ihr CV erfüllt moderne ATS-Standards."
    },
    "ats_warning": {
        "en": "Your CV needs improvements to pass recruiter filters reliably.",
        "fi": "CV:si tarvitsee parannuksia läpäistäkseen rekrytointisuodattimet luotettavasti.",
        "sv": "Ditt CV behöver förbättras för att pålitligt klara rekryteringsfilter.",
        "es": "Tu CV necesita mejoras para superar filtros de reclutamiento de forma confiable.",
        "pt-br": "Seu CV precisa de melhorias para passar de forma consistente pelos filtros de recrutadores.",
        "fr": "Votre CV doit être amélioré pour franchir les filtres de recrutement de manière fiable.",
        "de": "Ihr CV muss verbessert werden, um zuverlässig durch Recruiter-Filter zu kommen."
    },
    "ats_danger": {
        "en": "Your CV may be rejected automatically by ATS systems.",
        "fi": "CV:si voidaan hylätä automaattisesti ATS-järjestelmissä.",
        "sv": "Ditt CV kan avvisas automatiskt av ATS-system.",
        "es": "Tu CV puede ser rechazado automáticamente por sistemas ATS.",
        "pt-br": "Seu CV pode ser rejeitado automaticamente por sistemas ATS.",
        "fr": "Votre CV peut être rejeté automatiquement par les systèmes ATS.",
        "de": "Ihr CV könnte automatisch von ATS-Systemen abgelehnt werden."
    },
    "ats_tips": {
        "en": "Tips to improve your ATS score:",
        "fi": "Vinkkejä ATS-pisteiden parantamiseen:",
        "sv": "Tips för att förbättra din ATS-poäng:",
        "es": "Consejos para mejorar tu puntuación ATS:",
        "pt-br": "Dicas para melhorar sua pontuação ATS:",
        "fr": "Conseils pour améliorer votre score ATS :",
        "de": "Tipps zur Verbesserung Ihrer ATS-Bewertung:"
    }

}


def ui_text(key: str, lang: str) -> str:
    try:
        return UI_TEXT.get(key, {}).get(lang) or UI_TEXT.get(key, {}).get("en", "")
    except:
        return UI_TEXT.get(key, {}).get("en", "")
