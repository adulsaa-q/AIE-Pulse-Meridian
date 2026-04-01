import config

ACTIONS = {
    "growth_focused":  "Accelerate marketing execution — capitalize on momentum now",
    "risk_averse":     "Caution — investigate root cause before taking action",
    "stability_first": "Monitor closely — maintain current strategy, avoid overreaction",
    "efficiency_mode": "Optimize operations — review resource allocation and cost impact"
}

def apply(insights: list[dict]) -> list[dict]:
        """Adjust the recommendation based on the strategy mode in the configuration"""
        mode = config.STRATEGY_MODE
        for insight in insights:
                action = ACTIONS.get(mode,"Monitor and assess situation — no immediate action recommended")
                insight["recommendation"] = f"[{mode.upper()} MODE] {action}"
        return insights