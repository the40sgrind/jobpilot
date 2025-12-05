# backend/cv_parser.py
# Extracts and cleans CV text (PDF or plain text)

import PyPDF2


def extract_text_from_pdf(file) -> str:
    """
    Extract raw text from a PDF file.
    Returns a clean string.
    """
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception as e:
        return f"Error reading PDF: {e}"


def parse_cv_text(text: str) -> str:
    """
    Clean and normalize CV text for keyword extraction.
    - Remove excess newlines
    - Collapse multiple spaces
    - Strip whitespace
    """
    # Replace line breaks with spaces
    text = text.replace("\n", " ")

    # Collapse multiple spaces into one
    text = " ".join(text.split())

    return text.strip()
