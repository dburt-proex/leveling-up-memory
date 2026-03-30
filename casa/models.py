from dataclasses import dataclass
from typing import List

@dataclass
class ActionIntent:
    action: str
    target: str
    scope: str
    touches_files: bool = False
    touches_state: bool = False
    touches_repo: bool = False
    touches_config: bool = False
    destructive: bool = False

@dataclass
class GateDecision:
    gate: str
    reason: str
    risk_score: float
    triggered_rules: List[str]
