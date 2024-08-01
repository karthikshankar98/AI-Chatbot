from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    This function extracts text from a PDF file (handbook.pdf)

    Args:
        pdf_path (str): Path to the PDF file

    Returns:
        str: Extracted text from the PDF
    """

    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text_content = ""
        for page in reader.pages:
            text_content += page.extract_text()

    return text_content
