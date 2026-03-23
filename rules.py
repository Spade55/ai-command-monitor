HIGH_RISK_ACTIONS = [
    "delete_file",
    "shutdown_system",
    "format_disk",
    "execute_command"
]

MEDIUM_RISK_ACTIONS = [
    "write_file",
    "unknown"
]

PROTECTED_PATHS = [
    "/System",
    "/Library",
    "/Users",
    "/private"
]