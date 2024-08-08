import argparse
import os
from config import Config
from lib.utils import read_file, convert_markdown_to_html, save_temp_html
from lib.pdf_generation import generate_pdf

def main():
    """
    Main function to parse arguments, read files, convert Markdown to HTML, and generate PDFs.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert a Markdown file to a PDF with a fixed header and external CSS styling.')
    parser.add_argument('company_name', type=str, help='Company Name')
    parser.add_argument('--cover_letter', type=str, choices=['y', 'n'], default='n', help='Generate Cover letter Y/N (default: n)')
    args = parser.parse_args()

    # Define folder path
    company_folder = os.path.join('RESUME', args.company_name)
    os.makedirs(company_folder, exist_ok=True)

    # Read Markdown content
    resume_content = read_file('resume.md')
    cover_content = read_file('cover_letter.md')

    # Convert Markdown to HTML
    resume_html = convert_markdown_to_html(resume_content)
    cover_html = convert_markdown_to_html(cover_content)

    # Combine CSS link, header, and Markdown content
    resume_html_content = f'<!DOCTYPE html><html><head>{Config.get_css_link(Config.resume_style)}</head><body>{Config.get_header_html()}{resume_html}{Config.get_footer_html()}</body></html>'
    cover_html_content = f'<!DOCTYPE html><html><head>{Config.get_css_link(Config.cover_letter_style)}</head><body>{Config.get_addressee_html()}{cover_html}{Config.get_signature_html()}</body></html>'

    # Save the HTML content to temporary HTML files in the company folder
    if Config.saveHtml:
        save_temp_html(resume_html_content, company_folder, 'tmp_resume.html')
        save_temp_html(cover_html_content, company_folder, 'tmp_cover_letter.html')

    # Generate PDFs
    resume_filename = os.path.join(company_folder, f"GULGER_MALLIK_RESUME_{args.company_name}.pdf")
    cover_filename = os.path.join(company_folder, f"GULGER_MALLIK_LETTER_{args.company_name}.pdf")
    generate_pdf(resume_html_content, resume_filename)
    if args.cover_letter.lower() == 'y':
        generate_pdf(cover_html_content, cover_filename)

if __name__ == '__main__':
    main()
