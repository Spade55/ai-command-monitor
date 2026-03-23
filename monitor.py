from rules import is_dangerous
from logger import log_command

def monitor_command(command: str):
    if is_dangerous(command):
        print("WARNING: Dangerous command detected!")
        print(f"Blocked: {command}")
        log_command(command, "BLOCKED")
    else:
        print(f"Allowed: {command}")
        log_command(command, "ALLOWED")