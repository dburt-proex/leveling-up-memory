from casa.models import GateDecision
from casa.policy import evaluate_policy


def evaluate_intent(intent):
    gate, risk, rules = evaluate_policy(intent)
    reason = f"{gate} due to: {', '.join(rules) if rules else 'low-risk action'}"
    return GateDecision(
        gate=gate,
        reason=reason,
        risk_score=risk,
        triggered_rules=rules
    )
