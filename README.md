# AI Command Monitoring System 🛡️

A lightweight AI security system that monitors and filters AI-generated commands to prevent unsafe system operations.

This project simulates a secure control layer between AI outputs and system execution, inspired by real-world AI safety and cybersecurity challenges.

---

## Features

* Detects unsafe commands using rule-based filtering
* Blocks high-risk operations (e.g., file deletion, system shutdown)
* Logs all commands for auditing
* Supports mock AI mode and LLM integration
* Simple web interface using Flask

---

## Example

```
Enter command: delete all files  
WARNING: Dangerous command detected  
Blocked  

Enter command: hello  
Allowed  
```

---

## Tech Stack

* Python
* Flask
* Rule-based filtering
* Logging system

---

## Project Structure

```
ai-command-monitor/
│── app.py  
│── main.py  
│── llm_agent.py  
│── safety_guard.py  
│── rules.py  
│── logger.py  
│── run.sh  
```

---

## How It Works

1. Receive command (simulated AI output)
2. Analyze intent
3. Evaluate risk
4. Block or allow
5. Log results

---

## Run

```
./run.sh
```

Open:

```
http://127.0.0.1:5000
```

---

## Author

Yiru Wang
Computer Science @ UConn
