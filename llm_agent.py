import json
import os

# ===== MODE SETTINGS =====
# Change this to "api" when you have OpenAI API quota available.
MODE = "mock"   # options: "mock" or "api"
api_key = os.getenv("OPENAI_API_KEY")

def generate_action(user_input: str) -> dict:
    if MODE == "api":
        return generate_action_with_api(user_input)
    return generate_action_mock(user_input)


def generate_action_mock(user_input: str) -> dict:
    text = user_input.lower()

    if "delete" in text or "remove" in text:
        return {
            "action": "delete_file",
            "target": "/Downloads",
            "risk_hint": "high"
        }

    elif "shutdown" in text:
        return {
            "action": "shutdown_system",
            "target": "system",
            "risk_hint": "high"
        }

    elif "open" in text or "read" in text:
        return {
            "action": "read_file",
            "target": "notes.txt",
            "risk_hint": "low"
        }

    elif "list" in text:
        return {
            "action": "list_files",
            "target": "current_directory",
            "risk_hint": "low"
        }

    elif "write" in text or "edit" in text:
        return {
            "action": "write_file",
            "target": "notes.txt",
            "risk_hint": "medium"
        }

    else:
        return {
            "action": "unknown",
            "target": "",
            "risk_hint": "medium"
        }


def generate_action_with_api(user_input: str) -> dict:
    try:
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return {
                "action": "unknown",
                "target": "",
                "risk_hint": "medium",
                "error": "OPENAI_API_KEY is not set"
            }

        client = OpenAI(api_key=api_key)

        prompt = f"""
You are an AI system that converts user requests into structured JSON actions.

Only respond in pure JSON format. Do not include any explanation.

Available actions:
- read_file
- list_files
- write_file
- delete_file
- shutdown_system

Example output:
{{"action": "delete_file", "target": "/Downloads", "risk_hint": "high"}}

User request:
{user_input}
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        text = response.output_text.strip()

        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return {
                "action": "unknown",
                "target": "",
                "risk_hint": "medium",
                "raw_output": text
            }

    except Exception as e:
        return {
            "action": "unknown",
            "target": "",
            "risk_hint": "medium",
            "error": str(e)
        }