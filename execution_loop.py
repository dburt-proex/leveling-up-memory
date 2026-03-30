from casa.models import ActionIntent
from casa.gate import evaluate_intent
from opportunity_engine import load_state, generate_opportunities


def run_loop():
    state = load_state()
    options = generate_opportunities(state)

    print("\nTOP 3 MOVES:\n")
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt['title']} ({opt['leverage']})")

    choice = int(input("\nSelect option: ")) - 1
    selected = options[choice]

    intent = ActionIntent(
        action=selected["title"],
        target="execution_loop",
        scope="task_execution",
        touches_files=selected.get("touches_files", False),
        touches_state=selected.get("touches_state", False),
        touches_repo=selected.get("touches_repo", False),
        touches_config=selected.get("touches_config", False),
        destructive=selected.get("destructive", False)
    )

    decision = evaluate_intent(intent)

    print(f"\nGATE: {decision.gate}")
    print(f"REASON: {decision.reason}")
    print(f"RISK: {decision.risk_score}")

    if decision.gate == "HALT":
        print("Execution blocked by CASA.")
        return

    if decision.gate == "REVIEW":
        confirm = input("CASA requires review. Proceed? (y/n): ").strip().lower()
        if confirm != "y":
            print("Execution cancelled.")
            return

    print(f"\nExecuting: {selected['title']}")

    # Hook into your operator system here
    # execute_task(selected)


if __name__ == "__main__":
    run_loop()
