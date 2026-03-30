from casa.models import ActionIntent
from casa.gate import evaluate_intent


def run():
    selected = {
        "title": "Test write to memory",
        "touches_files": True,
        "touches_state": True,
        "touches_repo": False,
        "touches_config": False,
        "destructive": False
    }

    intent = ActionIntent(
        action=selected["title"],
        target="execution_loop",
        scope="test",
        touches_files=selected["touches_files"],
        touches_state=selected["touches_state"],
        touches_repo=selected["touches_repo"],
        touches_config=selected["touches_config"],
        destructive=selected["destructive"]
    )

    decision = evaluate_intent(intent)

    print(f"GATE: {decision.gate}")
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

    print("Executing task...")


if __name__ == "__main__":
    run()
