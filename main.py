from rich.console import Console
from rich.progress import track
import time
import webbrowser
from system_checks import get_system_info
from network_checks import network_report
from security_checks import security_report
from database import init_db, save_report
from report_generator import generate_html_report, generate_pdf_report
from config import REPORTS_DIR
import schedule
import threading

console = Console()

def run_full_report():
    console.print("\n[bold cyan][INFO][/bold cyan] Starting full ITHealthCheck...\n")
    
    report = {}

    # SYSTEM CHECKS
    console.print("[bold yellow][INFO][/bold yellow] Collecting system information...")
    for _ in track(range(10), description="System Check..."):
        time.sleep(0.05)  # simulate progress
    try:
        report["system"] = get_system_info()
    except Exception as e:
        console.print(f"[red][ERROR][/red] Failed to get system info: {e}")
        report["system"] = {}

    # NETWORK CHECKS
    console.print("[bold yellow][INFO][/bold yellow] Checking network connectivity...")
    for _ in track(range(10), description="Network Check..."):
        time.sleep(0.05)
    try:
        report["network"] = network_report()
    except Exception as e:
        console.print(f"[red][ERROR][/red] Failed to get network info: {e}")
        report["network"] = {}

    # SECURITY CHECKS
    console.print("[bold yellow][INFO][/bold yellow] Checking security status...")
    for _ in track(range(10), description="Security Check..."):
        time.sleep(0.05)
    try:
        report["security"] = security_report()
    except Exception as e:
        console.print(f"[red][ERROR][/red] Failed to get security info: {e}")
        report["security"] = {}

    # Save to SQLite
    try:
        save_report(report)
        console.print("[bold green][INFO][/bold green] Report saved to SQLite database.")
    except Exception as e:
        console.print(f"[red][ERROR][/red] Failed to save report: {e}")

    # Generate HTML and PDF reports
    try:
        html_file = generate_html_report(report)
        console.print(f"[bold green][INFO][/bold green] HTML report generated: {html_file}")
        webbrowser.open(html_file)

        pdf_file = generate_pdf_report(html_file)
        if pdf_file:
            console.print(f"[bold green][INFO][/bold green] PDF report generated: {pdf_file}")
    except Exception as e:
        console.print(f"[red][ERROR][/red] Failed to generate reports: {e}")

    console.print("\n[bold cyan][INFO][/bold cyan] ITHealthCheck completed.\n")

# Scheduler
def start_scheduler():
    schedule.every().day.at("09:00").do(run_full_report)
    threading.Thread(target=run_scheduler, daemon=True).start()
    console.print("[bold magenta][INFO][/bold magenta] Scheduler started: Daily report at 09:00 AM.")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(60)

# Menu
def menu():
    while True:
        console.print("\n[bold cyan]===== ITHealthCheck Menu =====[/bold cyan]")
        console.print("1. Run System Checks")
        console.print("2. Run Network Checks")
        console.print("3. Run Security Checks")
        console.print("4. Run Full Report")
        console.print("5. Enable Daily Scheduler")
        console.print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            try:
                data = get_system_info()
                for k, v in data.items():
                    console.print(f"[bold]{k}[/bold]: {v}")
            except Exception as e:
                console.print(f"[red][ERROR][/red] {e}")
        elif choice == "2":
            try:
                data = network_report()
                for k, v in data.items():
                    console.print(f"[bold]{k}[/bold]: {v}")
            except Exception as e:
                console.print(f"[red][ERROR][/red] {e}")
        elif choice == "3":
            try:
                data = security_report()
                for k, v in data.items():
                    console.print(f"[bold]{k}[/bold]: {v}")
            except Exception as e:
                console.print(f"[red][ERROR][/red] {e}")
        elif choice == "4":
            run_full_report()
        elif choice == "5":
            start_scheduler()
        elif choice == "6":
            console.print("[bold cyan][INFO][/bold cyan] Exiting ITHealthCheck. Goodbye!")
            break
        else:
            console.print("[yellow][WARNING][/yellow] Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    init_db()
    menu()
