🧭 JobPilot — AI-Powered Job Application Assistant

Fast • Global • Practical

JobPilot is an AI-powered job application assistant that helps job seekers analyze job ads, optimize CVs, generate cover letters, translate documents into multiple languages, and prepare for interviews — all in one streamlined workflow.

🌍 Global Language Support

JobPilot supports a fully localized UI and multilingual processing pipeline in:

English

Finnish

Swedish

Spanish

Portuguese (Brazil)

French

German

All UI elements, buttons, warnings, summaries, and outputs are language-aware.

✨ Core Features
AI Job Match Analysis

Match score (%)

Missing skills detection (shown in the CV’s original language)

AI-generated summary (shown in UI language)

CV Rewrite Engine

Rewrite CVs into:

Bullet format

Paragraph format

Hybrid format

Cover Letter Generator

One-click, job-specific cover letters

CV & Cover Letter Translation

Translate documents into any supported language

AI Interview Preparation

Generates:

Behavioral questions (STAR)

Cultural fit questions

Leadership questions

Salary & expectation questions

CV red flags

Expert tips

ATS & Quality Tools

ATS compatibility scanner

Bias & authenticity auditor

TXT and PDF exports

🗂 Project Structure
JobPilot/
├── app/
│   └── app.py
├── backend/
│   ├── ai_tools.py
│   ├── cv_parser.py
│   ├── comparator.py
│   ├── cv_rewriter.py
│   ├── cover_letter.py
│   ├── translator.py
│   └── language_utils.py
├── assets/
├── README.md
├── LICENSE
└── requirements.txt

🛠 Tech Stack

Python 3.11

Streamlit

OpenAI API

PyPDF2

Custom AI pipelines for rewriting, matching, and interviews

🧪 Running Locally
cd JobPilot
streamlit run app/app.py


Set your API key:

export OPENAI_API_KEY="your_key_here"

📝 License

MIT License.

⭐ Support

If you find this project useful, consider giving the repository a star.