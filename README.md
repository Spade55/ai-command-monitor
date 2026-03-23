# LLM Safety Guard: AI Command Monitoring System

A lightweight security system that monitors and controls AI-generated commands before execution.

This project simulates a real-world safety layer between an LLM (Large Language Model) and system-level operations, preventing unsafe or high-risk actions.

---

## Overview

As LLM-powered agents become more capable of interacting with operating systems and external tools, ensuring safe execution of generated commands is critical.

This project implements a command validation layer that:
- Interprets AI-generated actions
- Evaluates risk levels
- Enforces safety policies before execution

---

## Features

- LLM-driven command interpretation  
  Converts natural language input into structured actions (mock or API)

- Risk-aware decision engine  
  Classifies actions into low, medium, high risk levels

- Safety enforcement layer  
  BLOCKED: dangerous operations (delete, shutdown)  
  REVIEW: requires manual confirmation  
  ALLOWED: safe operations  

- Audit logging  
  Tracks all actions and decisions  

- Dual-mode architecture  
  mock mode (rule-based)  
  api mode (LLM-powered)  

---

## Example

```bash
LLM Safety Guard Started  
Type 'exit' to quit  

User Request: delete all files  

[LLM Output] {'action': 'delete_file', 'target': '/Downloads', 'risk_hint': 'high'}  
[Safety Decision] BLOCKED  
[Reason] delete_file is considered high-risk  
```

---

## System Architecture

```
User Input
    ↓
LLM Agent (mock / API)
    ↓
Structured Action (JSON)
    ↓
Safety Guard
    ↓
Decision: ALLOWED / REVIEW / BLOCKED
    ↓
Logger
```

---

## Project Structure

```
ai-command-monitor/
│── main.py            # Entry point
│── llm_agent.py       # LLM / mock action generator
│── safety_guard.py    # Decision engine
│── rules.py           # Risk rules
│── logger.py          # Logging system
```

---

## How It Works

1. User input is treated as an AI-generated command  
2. LLM agent converts input into structured JSON action  
3. Safety guard evaluates the action using predefined rules  
4. System returns decision: ALLOWED / REVIEW / BLOCKED  
5. All decisions are logged  

---

## How to Run

```bash
python3 main.py
```

---

## Future Improvements

- Prompt injection detection  
- Role-based access control (RBAC)  
- Sandbox execution environment  
- Web-based monitoring dashboard  
- Integration with real-world AI agents  

---

## Author

Yiru Wang  
Computer Science @ University of Connecticut  

Focus: AI Security · LLM Safety · Systems