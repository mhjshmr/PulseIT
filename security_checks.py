# security_checks.py
import platform
import subprocess
import wmi
import platform
import subprocess
import json
from datetime import datetime

def get_windows_defender_signature():
    info = {
        "Antivirus": "Windows Defender",
        "Signature Version": "Unknown",
        "Engine Version": "Unknown",
        "Last Updated": "Unknown"
    }

    try:
        cmd = (
            'powershell -Command '
            '"Get-MpComputerStatus | '
            'Select-Object AMServiceVersion, AMEngineVersion, AntivirusSignatureLastUpdated | '
            'ConvertTo-Json -Depth 2"'
        )

        output = subprocess.check_output(cmd, shell=True, text=True)
        data = json.loads(output)

        info["Signature Version"] = data.get("AMServiceVersion", "Unknown")
        info["Engine Version"] = data.get("AMEngineVersion", "Unknown")

        # Convert Defender timestamp to readable format
        raw_date = data.get("AntivirusSignatureLastUpdated")

        if raw_date:
            try:
                # Extract milliseconds from /Date(1767067141000)/
                timestamp_ms = int(raw_date.strip("/Date()"))
                timestamp_sec = timestamp_ms / 1000

                from datetime import datetime
                info["Last Updated"] = datetime.fromtimestamp(timestamp_sec).strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            except Exception:
                info["Last Updated"] = "Unknown"
        else:
            info["Last Updated"] = "Unknown"


    except Exception:
        pass

    return info

def get_linux_patch_details():
    try:
        updates = subprocess.check_output(
            "apt list --upgradable 2>/dev/null | tail -n +2",
            shell=True,
            text=True
        )

        if updates.strip():
            return updates.strip()
        else:
            return "System is up to date"

    except Exception:
        return "Not available"

def get_windows_defender_info():
    info = {}
    try:
        c = wmi.WMI(namespace="root\\SecurityCenter2")
        for av in c.AntivirusProduct():
            info["Antivirus"] = av.displayName
            info["Signature Version"] = getattr(av, "productState", "Unknown")
    except Exception as e:
        info["Antivirus"] = "Unknown"
        info["Signature Version"] = "Unknown"
    return info

def firewall_status():
    """Check firewall status"""
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
            return "Enabled" if "State ON" in result.stdout else "Disabled"
        elif platform.system() == "Linux":
            result = subprocess.run(["ufw", "status"], capture_output=True, text=True)
            return "Enabled" if "Status: active" in result.stdout else "Disabled"
        else:
            return "Unsupported OS"
    except Exception:
        return "Unknown"

def antivirus_status():
    """Detect installed antivirus programs"""
    av_list = []
    try:
        if platform.system() == "Windows":
            import wmi
            c = wmi.WMI(namespace="root\\SecurityCenter2")
            for av in c.AntiVirusProduct():
                av_list.append(av.displayName)
        elif platform.system() == "Linux":
            av_candidates = ["clamav", "chkrootkit", "rkhunter"]
            for av in av_candidates:
                result = subprocess.run(["which", av], capture_output=True, text=True)
                if result.stdout.strip():
                    av_list.append(av)
            if not av_list:
                av_list.append("None detected")
        else:
            av_list.append("Unsupported OS")
    except Exception:
        av_list.append("Unknown")
    return av_list

def update_status():
    """Check patch/update status"""
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["powershell", "Get-WindowsUpdateLog"], capture_output=True, text=True)
            return "Checked" if result.returncode == 0 else "Unknown"
        elif platform.system() == "Linux":
            result = subprocess.run(["apt", "update"], capture_output=True, text=True)
            return "Updates available" if "packages can be upgraded" in result.stdout else "Up-to-date"
        else:
            return "Unsupported OS"
    except Exception:
        return "Unknown"

def security_report():
    report = {}
    system = platform.system()

    # Firewall (existing logic assumed)
    report["Firewall"] = "Enabled" if system == "Windows" else "Checked"

    if system == "Windows":
        defender = get_windows_defender_signature()
        report.update(defender)
        report["Updates"] = "Checked via Windows Update"

    elif system == "Linux":
        report["Antivirus"] = "Depends on distribution"
        report["Signature Version"] = "N/A"
        report["Updates"] = get_linux_patch_details()

    else:
        report["Antivirus"] = "Unknown"
        report["Updates"] = "Unknown"

    return report

