import socket
import subprocess
import platform
from config import DEFAULT_GATEWAY, INTERNET_TEST_HOST, INTERNET_TEST_PORT

def get_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def ping_gateway(gateway=DEFAULT_GATEWAY):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        subprocess.check_output(
            ["ping", param, "1", gateway],
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        return "Reachable"
    except subprocess.CalledProcessError:
        return "Unreachable"

def check_internet(host=INTERNET_TEST_HOST, port=INTERNET_TEST_PORT):
    try:
        socket.create_connection((host, port), timeout=3)
        return "Connected"
    except OSError:
        return "Disconnected"

def network_report():
    return {
        "IP Address": get_ip_address(),
        "Gateway Status": ping_gateway(),
        "Internet Status": check_internet()
    }
