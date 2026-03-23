from flask import Flask, request, jsonify, render_template_string
from llm_agent import generate_action
from safety_guard import evaluate_action

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>LLM Safety Guard</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            padding: 40px;
        }
        input {
            width: 400px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            margin-left: 10px;
        }
        .box {
            margin-top: 30px;
            padding: 20px;
            border-radius: 10px;
            background: #1e293b;
        }
    </style>
</head>
<body>

<h1>LLM Safety Guard</h1>
<p>AI Command Monitoring System</p>

<input id="input" placeholder="Enter a command..." />
<button onclick="send()">Run</button>

<div class="box" id="result"></div>

<script>
function send() {
    const input = document.getElementById("input").value;

    fetch("/run", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: input})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = `
            <p><b>Action:</b> ${data.action}</p>
            <p><b>Target:</b> ${data.target}</p>
            <p><b>Risk:</b> ${data.risk}</p>
            <p><b>Decision:</b> ${data.decision}</p>
            <p><b>Reason:</b> ${data.reason}</p>
        `;
    });
}
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/run", methods=["POST"])
def run():
    user_input = request.json.get("text")

    action = generate_action(user_input)
    decision, reason = evaluate_action(action)

    return jsonify({
        "action": action.get("action"),
        "target": action.get("target"),
        "risk": action.get("risk_hint"),
        "decision": decision,
        "reason": reason
    })


if __name__ == "__main__":
    app.run(debug=True)