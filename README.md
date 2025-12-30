# PulseIT – Automated System Diagnostics Tool

PulseIT is a Python-based system diagnostics and IT support tool designed to automate routine checks for system performance, network connectivity, and security status. 
It generates detailed HTML and PDF reports to support IT troubleshooting, monitoring, and preventive maintenance.

<br>

<div align="center">
  <img src="https://github.com/mhjshmr/PulseIT/blob/main/reports/PulseIT%20Output.png" alt="PulseIT Output" width="400">
</div>


## Overview

PulseIT helps students, IT staff, and system administrators understand the health and status of their computers. The tool performs technical checks across system resources, network 
infrastructure, and security components, providing an easy-to-read report with actionable insights.

helps students, IT staff, and system administrators understand the health and status of their computers. The tool performs technical checks across system resources, network infrastructure, and 
security components, providing an easy-to-read report with actionable insights.

## Features

### System Checks
- Operating system and kernel version
- CPU usage monitoring
- RAM usage monitoring
- Disk health and usage
- Disk health and usage

### Network Checks
- IP address detection
- Gateway connectivity and ping test
- Internet connectivity check
- Internet connectivity check

### Security Checks
- Firewall status
- Antivirus detection (Windows/Linux)
- Windows Defender signature and engine version
- Last update timestamp
- Linux patch status (apt list --upgradable)

### Report Generation

- Console output with real-time progress and colored messages
- Human-readable HTML and PDF reports
- Historical logs stored in SQLite
- Unique timestamped report filenames
- Automatic report opening in the browser

### Scheduler

- Daily or weekly automated report generation using Python `schedule` module
- Optional automatic report generation for routine IT audits
  
## Getting Started

### Prerequisites

- Python 3.10+
- Required Python modules: `psutil`, `platform`, `socket`, `subprocess`, `datetime`, `json`, `sqlite3`, `schedule`, `tqdm`, `rich`, `reportlab`, `jinja2`
- Optional: `wmi` (Windows antivirus detection)
- Optional: `wkhtmltopdf` (for PDF generation)

### Installation

Clone the repository:
```bash
git clone https://github.com/mhjshmr/PulseIT.git
cd PulseIT
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage

Run the main program:
```bash
python main.py
```
Follow the interactive menu to:
1. Run system checks
2. Run network checks
3. Run security checks
4. Generate a full diagnostic report (HTML + PDF)
5. Enable daily scheduler
6. Exit

## How It Works

Analysis Flow
1. Collect system information (CPU, RAM, Disk, OS version, uptime)
2. Check network connectivity (IP, gateway, internet)
3. Perform security checks (firewall, antivirus, Windows Defender, updates)
4. Store results in SQLite database for historical reference
5. Generate HTML and PDF reports with unique timestamps
6. Optional scheduling for automated daily/weekly reports

## Best Practices

- Use PulseIT on all critical systems regularly to monitor health
- Combine report insights with other monitoring tools for full IT management
- Review scheduled reports to detect potential performance or security issues early

## Security Considerations

- Designed for monitoring and diagnostics; not a replacement for full antivirus or patch management solutions
- Windows Defender and Linux patch detection is based on available system APIs
- Reports should be reviewed manually before acting on critical alerts

## Technical Details

- Language: Python 3.x
- Libraries Used:
     - `psutil`, `platform`, `subprocess`, `socket`, `datetime`, `json`, `sqlite3`
     - `schedule`, `tqdm`, `rich`, `reportlab`, `jinja2`
     - Optional: `wmi` (Windows), `wkhtmltopdf` (PDF generation)

## Core Functions

- `get_system_info()` – System resource and uptime checks
- `network_report()` – IP, gateway, and internet connectivity
- `security_report()` – Firewall, antivirus, Windows Defender, updates
- `generate_html_report()` / `generate_pdf_report()` – Create human-readable reports
- `save_report()` – Save results to SQLite database
- `menu()` – Interactive CLI interface
- `run_full_report()` – Run complete system, network, and security checks

## Use Case

- IT support training and simulations
- Academic exercises in system monitoring and cybersecurity
- Small business or personal system maintenance
- SOC analyst training and IT audits

## References

- Python `psutil` documentation
- Windows Defender WMI API
- Linux package management (`apt`)
- `wkhtmltopdf` for PDF report generation
<br><br>

**Stay proactive. Keep your systems healthy. 🔧💻**
