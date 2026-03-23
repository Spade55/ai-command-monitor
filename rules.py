DANGEROUS_KEYWORDS = [
    "rm -rf",
    "delete",
    "shutdown",
    "format",
    "wipe",
    "kill",
    "drop database",
    "truncate",
    "remove all"
]

def is_dangerous(command: str) -> bool:
    command = command.lower()
    return any(keyword in command for keyword in DANGEROUS_KEYWORDS)