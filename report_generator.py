import os
import datetime
from jinja2 import Environment, FileSystemLoader
import pdfkit
from config import REPORTS_DIR, PDF_OUTPUT_DIR, TEMPLATE_FILE, WKHTMLTOPDF_PATH

def generate_html_report(data):
    """Generate HTML report"""
    env = Environment(loader=FileSystemLoader(REPORTS_DIR))
    template = env.get_template(TEMPLATE_FILE)

    rendered = template.render(
        timestamp=str(datetime.datetime.now()),
        system=data["system"],
        network=data["network"],
        security=data["security"]
    )

    filename = os.path.join(REPORTS_DIR, f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
    with open(filename, "w") as f:
        f.write(rendered)

    return filename


def generate_pdf_report(html_file):
    """Convert HTML report to PDF"""
    if not os.path.exists(PDF_OUTPUT_DIR):
        os.makedirs(PDF_OUTPUT_DIR)

    pdf_filename = os.path.join(
        PDF_OUTPUT_DIR,
        os.path.basename(html_file).replace(".html", ".pdf")
    )

    try:
        config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
        pdfkit.from_file(html_file, pdf_filename, configuration=config)
        return pdf_filename
    except Exception as e:
        print(f"[ERROR] Failed to generate PDF: {e}")
        return None
