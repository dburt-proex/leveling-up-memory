import json


def load_state():
    with open("state.json", "r") as f:
        return json.load(f)


def generate_opportunities(state):
    return [
        {
            "title": "Launch JobTap contractor onboarding funnel",
            "leverage": "Revenue",
            "effort": "Medium",
            "touches_files": True,
            "touches_state": True,
            "touches_repo": False,
            "touches_config": False,
            "destructive": False
        },
        {
            "title": "Package CASA into Governance Audit Offer",
            "leverage": "Revenue + Asset",
            "effort": "Low",
            "touches_files": True,
            "touches_state": True,
            "touches_repo": False,
            "touches_config": False,
            "destructive": False
        },
        {
            "title": "Build automated lead routing system",
            "leverage": "Infrastructure",
            "effort": "Medium",
            "touches_files": True,
            "touches_state": True,
            "touches_repo": True,
            "touches_config": False,
            "destructive": False
        }
    ]
