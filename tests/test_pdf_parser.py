import pytest
from utils.pdf_parser import extract_text_from_pdf

def test_extract_text_from_pdf():
    text = extract_text_from_pdf('handbook.pdf')
    assert len(text) > 0