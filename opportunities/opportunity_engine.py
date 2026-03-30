import json

def load_state():
    with open("state.json", "r") as f:
        return json.load(f)

def generate_opportunities(state):
    return [
        {
            "title": "Launch JobTap contractor onboarding funnel",
            "leverage": "Revenue",
            "effort": "Medium"
        },
        {
            "title": "Package CASA into Governance Audit Offer",
            "leverage": "Revenue + Asset",
            "effort": "Low"
        },
        {
            "title": "Build automated lead routing system",
            "leverage": "Infrastructure",
            "effort": "Medium"
        }
    ]
