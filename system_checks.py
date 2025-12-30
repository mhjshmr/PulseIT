import psutil
import platform
import datetime

def get_system_info():
    """
    Collects system performance and OS details
    """
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time

    system_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "RAM Usage (%)": psutil.virtual_memory().percent,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "System Uptime": str(uptime).split('.')[0]
    }

    return system_info
