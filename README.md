# AI Command Monitoring System

A simple AI security project that simulates monitoring and controlling AI-generated commands to prevent unsafe system operations.

This project demonstrates how an AI system's outputs can be analyzed and filtered before execution to ensure system safety.

---

## Features

- **Detects unsafe commands** using rule-based filtering  
- **Blocks high-risk operations** such as file deletion or system shutdown  
- **Logs all commands** with timestamps for auditing  
- **Simulates an AI-to-system command control layer**  

---

## Example

```bash
AI Command Monitoring System Started  
Type 'exit' to quit  

Enter command: delete all files  
WARNING: Dangerous command detected!  
Blocked: delete all files  

Enter command: rm -rf  
WARNING: Dangerous command detected!  
Blocked: rm -rf  

Enter command: hello  
Allowed: hello  
```

---

## Tech Stack

- Python  
- Rule-based detection system  
- Logging system  

---

## Project Structure

```text
ai-command-monitor/
│── main.py        # Entry point of the system  
│── monitor.py     # Core monitoring logic  
│── rules.py       # Security rules and filters  
│── logger.py      # Logging system  
```

---

## How It Works

1. **Receive command** (simulating AI output)  
2. **Check against predefined security rules**  
3. If unsafe → **Blocked**  
4. Otherwise → **Allowed**  
5. **Log all actions for transparency**  

---

## How to Run

```bash
python3 main.py
```

---

## Future Improvements

- Add machine learning-based detection (instead of rule-based)  
- Introduce a whitelist system for trusted commands  
- Build a web interface for real-time monitoring  
- Integrate with real AI APIs (e.g., OpenAI) for testing  

---

## Author

Yiru Wang  
Computer Science @ University of Connecticut  
Interested in Cybersecurity & AI Security  
