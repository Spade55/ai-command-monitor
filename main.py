from llm_agent import generate_action
from safety_guard import evaluate_action
from logger import log_event

def main():
    print("LLM Safety Guard Started")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("User Request: ").strip()

        if user_input.lower() == "exit":
            print("Exiting system...")
            break

        action = generate_action(user_input)
        print(f"\n[LLM Output] {action}")

        decision = evaluate_action(action)
        print(f"[Safety Decision] {decision['status']}")
        if "reason" in decision:
            print(f"[Reason] {decision['reason']}")

        log_event(user_input, action, decision)
        print("-" * 40)

if __name__ == "__main__":
    main()