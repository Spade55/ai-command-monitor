from rules import HIGH_RISK_ACTIONS, MEDIUM_RISK_ACTIONS, PROTECTED_PATHS

def evaluate_action(action: dict) -> dict:
    action_type = action.get("action", "")
    target = action.get("target", "")

    # High-risk action type
    if action_type in HIGH_RISK_ACTIONS:
        return {
            "status": "BLOCKED",
            "reason": f"{action_type} is considered high-risk"
        }

    # Protected paths
    if isinstance(target, str):
        for path in PROTECTED_PATHS:
            if path and path in target:
                return {
                    "status": "BLOCKED",
                    "reason": f"target path '{target}' is protected"
                }

    # Medium-risk action type
    if action_type in MEDIUM_RISK_ACTIONS:
        return {
            "status": "REVIEW",
            "reason": f"{action_type} requires manual confirmation"
        }

    # Default allow
    return {
        "status": "ALLOWED"
    }