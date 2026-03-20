"""
GigShield — Rule-Based Premium Calculator (Phase 1)
Same API interface as the Phase 2 XGBoost model.
Swap this file for the trained model in Phase 2 — no frontend changes needed.
"""

from datetime import datetime


ZONE_RISK_SCORES = {
    "Kukatpally": 87, "Ameerpet": 63, "Secunderabad": 58,
    "Banjara Hills": 28, "Kondapur": 45,
    "Koramangala": 72, "Indiranagar": 55, "Whitefield": 40,
    "Andheri": 80, "Bandra": 65, "Dadar": 70,
    "Connaught Place": 50, "Dwarka": 45,
    "Anna Nagar": 60, "T Nagar": 55, "Velachery": 70,
}

MONSOON_MONTHS = {
    "Hyderabad": [6, 7, 8, 9],
    "Bengaluru": [6, 7, 8, 9, 10],
    "Mumbai":    [6, 7, 8, 9],
    "Delhi":     [7, 8, 9],
    "Chennai":   [10, 11, 12],
}

BASE_PREMIUMS = {"Basic": 29, "Standard": 49, "Premium": 79}
MAX_PAYOUTS   = {"Basic": 700, "Standard": 1400, "Premium": 2500}


def calculate_premium(zone: str, city: str, plan: str, claim_history_count: int,
                       forecast_risk_score: float = 0.5) -> dict:
    """
    Calculate weekly premium for a worker.

    Args:
        zone: Worker's primary delivery zone
        city: City name
        plan: "Basic", "Standard", or "Premium"
        claim_history_count: Number of clean weeks (for no-claim discount)
        forecast_risk_score: 0.0–1.0 from IMD 7-day forecast (default 0.5)

    Returns:
        dict with total premium and per-factor breakdown
    """
    base = BASE_PREMIUMS.get(plan, 49)
    breakdown = {"base": base}

    # Zone risk adjustment
    zone_risk = ZONE_RISK_SCORES.get(zone, 50)
    zone_adj = round((zone_risk / 100) * 15)
    breakdown["zone_risk"] = zone_adj

    # Seasonal monsoon adjustment
    current_month = datetime.now().month
    city_monsoon = MONSOON_MONTHS.get(city, [6, 7, 8, 9])
    season_adj = 10 if current_month in city_monsoon else 0
    breakdown["seasonal"] = season_adj

    # 7-day forecast risk
    forecast_adj = round(forecast_risk_score * 8)
    breakdown["forecast"] = forecast_adj

    # No-claim discount (up to -₹8 after 4 clean weeks)
    no_claim_discount = min(8, claim_history_count // 4) * -1
    breakdown["no_claim_discount"] = no_claim_discount

    total = base + zone_adj + season_adj + forecast_adj + no_claim_discount
    total = max(base, total)  # Never go below base

    return {
        "plan": plan,
        "zone": zone,
        "city": city,
        "breakdown": breakdown,
        "total_premium": total,
        "max_weekly_payout": MAX_PAYOUTS[plan],
        "calculated_at": datetime.now().isoformat(),
    }


def get_risk_tier(zone: str, city: str, work_hours: str) -> str:
    """Assign risk tier at onboarding for plan recommendation."""
    zone_risk = ZONE_RISK_SCORES.get(zone, 50)
    score = zone_risk
    if "Afternoon" in work_hours or "Full Day" in work_hours:
        score += 10
    current_month = datetime.now().month
    if current_month in MONSOON_MONTHS.get(city, [6, 7, 8, 9]):
        score += 15
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    return "Low"


def recommend_plan(risk_tier: str) -> str:
    return {"Low": "Basic", "Medium": "Standard", "High": "Standard"}.get(risk_tier, "Standard")


# --- Demo ---
if __name__ == "__main__":
    result = calculate_premium(
        zone="Kukatpally",
        city="Hyderabad",
        plan="Standard",
        claim_history_count=6,
        forecast_risk_score=0.6,
    )
    print("=== Premium Calculation for Ravi ===")
    print(f"Plan:        {result['plan']}")
    print(f"Zone:        {result['zone']}")
    print(f"\nBreakdown:")
    b = result["breakdown"]
    print(f"  Base premium:         ₹{b['base']}")
    print(f"  Zone risk:            +₹{b['zone_risk']}")
    print(f"  Seasonal adjustment:  +₹{b['seasonal']}")
    print(f"  Forecast risk:        +₹{b['forecast']}")
    print(f"  No-claim discount:    {b['no_claim_discount']}₹")
    print(f"\n  Total this week:      ₹{result['total_premium']}")
    print(f"  Max weekly payout:    ₹{result['max_weekly_payout']}")

    tier = get_risk_tier("Kukatpally", "Hyderabad", "Afternoon+Evening (12PM-10PM)")
    plan = recommend_plan(tier)
    print(f"\nRisk tier: {tier} → Recommended plan: {plan}")
