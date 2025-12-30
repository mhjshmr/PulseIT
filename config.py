# Paths
REPORTS_DIR = "reports"
LOG_DB = "logs/healthcheck.db"
TEMPLATE_FILE = "report_template.html"

# Network Settings
DEFAULT_GATEWAY = "192.168.1.1"
INTERNET_TEST_HOST = "8.8.8.8"
INTERNET_TEST_PORT = 53

# PDF export settings (future)
# config.py

REPORTS_DIR = "reports"
PDF_OUTPUT_DIR = "reports/pdf"
WKHTMLTOPDF_PATH = r"C:\wkhtmltopdf\bin\wkhtmltopdf.exe"  # <-- update to your installed path
TEMPLATE_FILE = "template.html"  # if using a Jinja2 template
