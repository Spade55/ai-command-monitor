from datetime import datetime

LOG_FILE = "log.txt"

def log_event(user_input, action, decision):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"User Input: {user_input}\n")
        f.write(f"LLM Output: {action}\n")
        f.write(f"Decision: {decision['status']}\n")
        if "reason" in decision:
            f.write(f"Reason: {decision['reason']}\n")