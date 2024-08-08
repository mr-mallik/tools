from xhtml2pdf import pisa

def generate_pdf(html_content, pdf_path):
    """
    Generates a PDF from HTML content and saves it to the specified path.

    :param html_content: HTML content to convert to PDF.
    :param pdf_path: Path where the PDF will be saved.
    """
    try:
        with open(pdf_path, 'wb') as output_pdf:
            pisa.CreatePDF(html_content, dest=output_pdf)
        print(f"PDF generated successfully: {pdf_path}")
    except Exception as e:
        print(f"Error generating PDF: {e}")
        exit(1)
