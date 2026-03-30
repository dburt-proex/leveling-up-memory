def evaluate_policy(intent):
    rules = []
    risk = 0.0

    if intent.destructive:
        rules.append("destructive_action")
        return "HALT", 1.0, rules

    if intent.touches_config:
        rules.append("config_change")
        return "HALT", 0.95, rules

    if intent.touches_repo:
        rules.append("repo_mutation")
        risk += 0.55

    if intent.touches_state:
        rules.append("persistent_state_mutation")
        risk += 0.35

    if intent.touches_files:
        rules.append("file_write")
        risk += 0.25

    if risk >= 0.5:
        return "REVIEW", risk, rules

    return "AUTO", risk, rules
