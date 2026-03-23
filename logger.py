from datetime import datetime

LOG_FILE = "log.txt"

def log_command(command: str, status: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {command} -> {status}\n")
        