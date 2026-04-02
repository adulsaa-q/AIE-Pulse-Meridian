import config

# คำแนะนำเชิงกลยุทธ์ แยกตาม (mode, signal_type)
ACTIONS = {
    ("growth_focused",  "ACCELERATION"): "Accelerate marketing execution — capitalize on momentum now",
    ("growth_focused",  "DECLINE"):      "Investigate decline urgently — reassess growth strategy",
    ("growth_focused",  "ANOMALY"):      "Extreme movement detected — pause and validate data before acting",
    ("risk_averse",     "ACCELERATION"): "Validate before scaling — confirm signal sustainability",
    ("risk_averse",     "DECLINE"):      "Caution — investigate root cause before taking action",
    ("risk_averse",     "ANOMALY"):      "Halt non-critical activities — investigate extreme anomaly immediately",
    ("stability_first", "ACCELERATION"): "Monitor closely — avoid overreaction to positive signal",
    ("stability_first", "DECLINE"):      "Review and stabilize — address decline before it compounds",
    ("stability_first", "ANOMALY"):      "Escalate to leadership — anomaly exceeds normal variance",
    ("efficiency_mode", "ACCELERATION"): "Optimize resource allocation to amplify this growth",
    ("efficiency_mode", "DECLINE"):      "Review cost structure — reduce exposure in declining area",
    ("efficiency_mode", "ANOMALY"):      "Audit operations immediately — extreme variance detected",
}

def apply(insights: list[dict]) -> list[dict]:
    """กำหนด recommendation ให้แต่ละ insight ตาม strategy mode และประเภท signal"""
    mode = config.STRATEGY_MODE
    for insight in insights:
        signal_type = insight.get("signal_type", "")
        action = ACTIONS.get(
            (mode, signal_type),
            "Monitor and assess situation — no immediate action recommended"
        )
        insight["recommendation"] = f"[{mode.upper()}] {action}"
    return insights
