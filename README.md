🧭 JobPilot — AI-Powered CV & Job Application Assistant

Your complete AI career companion: CVs, cover letters, ATS optimization, and interview prep — for the Nordics and beyond.

JobPilot is a multi-language, AI-powered tool that helps job seekers improve their job applications fast.
It analyzes your CV and job ad, shows a match score, rewrites your CV, generates tailored cover letters, translates documents (EN/FI/SV), and prepares you for interviews.

The app is built with Streamlit (frontend) and Python modules (backend), with a strong focus on:

Nordic job market standards (Finland, Sweden, Nordics)

Clean UX

GDPR compliance (no CV storage)

ATS-aware CV structure

Authentic, human-sounding writing

✨ Features (MVP v1.0)

Current features:

Job Ad Input

Paste any job advertisement text

JobPilot analyzes requirements and key skills

CV Upload & Parsing

Upload CV as PDF or TXT

Extracts text and skills

Detects CV language (EN/FI/SV)

Match Analysis

Match score (0–100)

Missing skills list

Summary of fit in UI language (EN/FI/SV), independent of CV or job ad language

Designed for consistency and predictability (no random language flips)

CV Rewrite
Rewrite CV into:

Bullet-point format (recruiter friendly)

Paragraph format (easy to read)

Hybrid format
Uses job ad context to highlight relevant strengths.

Cover Letter Generator

Always generated in the job ad language

Tailored to the specific job and CV content

Translations (EN / FI / SV)

CV translation

Cover letter translation

Full-text output (never “no translation needed”)

Interview Preparation AI
Generates interview questions + model answers:

Behavioral (STAR)

Cultural fit

Leadership/responsibility

Potential weaknesses/red flags

Salary expectations

Final expert tips
Always generated in the job ad language.

🔥 Upcoming Features (v2+ Roadmap)

ATS Scanner (High Priority)
Ensures CVs & cover letters pass real Applicant Tracking Systems.

Formatting checks

Keyword coverage

ATS flags (green/yellow/red)

Improvement suggestions

(Future) One-click ATS optimization for premium users

Human-Expert Template Library
Blend user CVs with anonymized Nordic writing structures.

30–100 EN/FI/SV templates

More human, less “AI-slop”

Boosts recruiter trust

Major value for premium tiers

Bias & Authenticity Auditor
Detects and improves issues like:

Biased wording

Overly formal / repetitive AI phrasing

Readability problems

AI detectability patterns
Helps meet EU AI Act & Nordic fairness expectations.

🧱 Project Structure

JobPilot/
app/
app.py
backend/
ai_tools.py
cv_parser.py
comparator.py
cv_rewriter.py
cover_letter.py
translator.py
language_utils.py
JOBPILOT_LLM_BRIEF.md
JOBPILOT_BUGLOG.md
requirements.txt
README.md
LICENSE

🛠 Tech Stack

Frontend: Streamlit

Backend: Python (modular architecture)

Parsing: PyPDF2 + custom normalization

AI Models: OpenAI / Grok style LLMs

Languages: English, Finnish, Swedish

Planned Hosting:

Streamlit Cloud → app.getjobpilot.fi

WordPress → getjobpilot.fi

🔐 Privacy & GDPR

JobPilot follows GDPR-first principles:

CVs, job ads, rewrites, and analyses are not stored

All processing happens temporarily in-memory during the session

No user accounts in MVP

No profiling with legal effects

Payments (future) handled by Stripe — JobPilot never stores card data

Full Privacy Policy: https://getjobpilot.fi/privacy-policy

🚀 Running JobPilot Locally (for contributors)

If you want to run JobPilot on your own machine:

1. Clone the repository
(Contributors only — Rode already has the project locally.)

git clone https://github.com/YOUR_USERNAME/jobpilot.git

cd jobpilot

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate # macOS / Linux

venv\Scripts\activate.bat # Windows

3. Install dependencies

pip install -r requirements.txt

4. Set your API key

export OPENAI_API_KEY="your_real_api_key_here"

5. Run the app

streamlit run app/app.py

Open the browser link shown (usually http://localhost:8501
).

🌐 Deployment (Planned)
Streamlit Cloud Deployment

Push repo to GitHub

Log into Streamlit Cloud

Create “New App” → select JobPilot repo

Set entry point to: app/app.py

Add OPENAI_API_KEY in Streamlit Secrets

Deploy

Custom Domain (Planned)

Marketing site → https://getjobpilot.fi

App domain → https://app.getjobpilot.fi
 (CNAME → Streamlit)

🛣 Roadmap (High Level)

✔ MVP Completed

CV parsing

Job ad analysis

Match score

CV rewrites

Cover letters

Translation

Interview prep

🚧 v2+ In Development

ATS Scanner

Template Library

Bias & Authenticity Auditor

Pricing + Stripe billing

Analytics (Plausible)

User accounts + saved CVs

Mobile app (FlutterFlow)

Better UI & localization

🤝 Contributing

JobPilot is early-stage.
If you’re interested in contributing to:

Nordic job market logic

ATS parsing

UX/UI

Language outputs

You can open an issue or submit a pull request.

📬 Contact

Founder: Rodrigo (“Rode”)
Email: support@getjobpilot.fi

Website: https://getjobpilot.fi

📄 License (Proprietary)

You may:

Read the code

Run it locally

Learn from it

You may NOT:

Use it commercially

Host it publicly

Sell derivative versions

See LICENSE for full terms.