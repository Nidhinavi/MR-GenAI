
import pandas as pd

def load_csv(path):
    return pd.read_csv(path)

def load_text(path):
    with open(path) as f:
        return f.read()

# PDF loader (requires PyMuPDF / pdfplumber in real use)
def load_pdf(path):
    return "Extracted PDF text (placeholder)"
