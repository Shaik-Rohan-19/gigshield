"""
GigShield — Synthetic Dataset Generator
Generates 500 mock worker profiles across 5 Indian cities
for ML model training in Phase 2.
"""

import json
import random
from datetime import datetime, timedelta

random.seed(42)

CITIES = {
    "Hyderabad": {
        "zones": ["Kukatpally", "Ameerpet", "Secunderabad", "Banjara Hills", "Kondapur"],
        "zone_risk": {"Kukatpally": 87, "Ameerpet": 63, "Secunderabad": 58, "Banjara Hills": 28, "Kondapur": 45},
        "monsoon_months": [6, 7, 8, 9],
    },
    "Bengaluru": {
        "zones": ["Koramangala", "Indiranagar", "Whitefield", "Jayanagar", "Marathahalli"],
        "zone_risk": {"Koramangala": 72, "Indiranagar": 55, "Whitefield": 40, "Jayanagar": 35, "Marathahalli": 60},
        "monsoon_months": [6, 7, 8, 9, 10],
    },
    "Mumbai": {
        "zones": ["Andheri", "Bandra", "Dadar", "Thane", "Kurla"],
        "zone_risk": {"Andheri": 80, "Bandra": 65, "Dadar": 70, "Thane": 55, "Kurla": 75},
        "monsoon_months": [6, 7, 8, 9],
    },
    "Delhi": {
        "zones": ["Connaught Place", "Dwarka", "Rohini", "Lajpat Nagar", "Noida"],
        "zone_risk": {"Connaught Place": 50, "Dwarka": 45, "Rohini": 42, "Lajpat Nagar": 48, "Noida": 38},
        "monsoon_months": [7, 8, 9],
    },
    "Chennai": {
        "zones": ["Anna Nagar", "T Nagar", "Velachery", "Tambaram", "Adyar"],
        "zone_risk": {"Anna Nagar": 60, "T Nagar": 55, "Velachery": 70, "Tambaram": 45, "Adyar": 50},
        "monsoon_months": [10, 11, 12],
    },
}

PLATFORMS = ["Zomato", "Swiggy", "Both"]
WORK_HOURS = ["Morning (6AM-12PM)", "Afternoon+Evening (12PM-10PM)", "Night (6PM-2AM)", "Full Day"]
RISK_TIERS = ["Low", "Medium", "High"]


def compute_risk_tier(zone_risk, work_hours, city_data, current_month):
    score = zone_risk
    if work_hours in ["Afternoon+Evening (12PM-10PM)", "Full Day"]:
        score += 10
    if current_month in city_data["monsoon_months"]:
        score += 15
    if score >= 75:
        return "High"
    elif score >= 50:
        return "Medium"
    else:
        return "Low"


def compute_weekly_premium(base, zone_risk, month, city_data, claim_history_count):
    zone_adj = round((zone_risk / 100) * 15)
    season_adj = 10 if month in city_data["monsoon_months"] else 0
    forecast_adj = random.randint(0, 8)
    no_claim_discount = max(0, min(8, claim_history_count // 4)) * -1
    total = base + zone_adj + season_adj + forecast_adj + no_claim_discount
    return max(base, total)


def generate_worker(worker_id):
    city = random.choice(list(CITIES.keys()))
    city_data = CITIES[city]
    zone = random.choice(city_data["zones"])
    zone_risk = city_data["zone_risk"][zone]
    platform = random.choice(PLATFORMS)
    work_hours = random.choice(WORK_HOURS)

    join_date = datetime.now() - timedelta(days=random.randint(7, 365))
    current_month = datetime.now().month
    risk_tier = compute_risk_tier(zone_risk, work_hours, city_data, current_month)

    plan = "Basic" if risk_tier == "Low" else ("Premium" if risk_tier == "High" else "Standard")
    base_premiums = {"Basic": 29, "Standard": 49, "Premium": 79}
    base = base_premiums[plan]

    weeks_active = max(1, (datetime.now() - join_date).days // 7)
    claim_count = random.randint(0, min(weeks_active, 15))
    total_payout = claim_count * random.randint(150, 500)

    weekly_premium = compute_weekly_premium(base, zone_risk, current_month, city_data, claim_count)

    return {
        "worker_id": f"W{worker_id:04d}",
        "city": city,
        "zone": zone,
        "zone_risk_score": zone_risk,
        "platform": platform,
        "work_hours": work_hours,
        "risk_tier": risk_tier,
        "plan": plan,
        "base_premium": base,
        "weekly_premium": weekly_premium,
        "join_date": join_date.strftime("%Y-%m-%d"),
        "weeks_active": weeks_active,
        "claim_count": claim_count,
        "total_payout_received": total_payout,
        "no_claim_discount_eligible": claim_count == 0,
    }


def generate_dataset(n=500):
    workers = [generate_worker(i + 1) for i in range(n)]

    summary = {
        "total_workers": n,
        "by_city": {city: sum(1 for w in workers if w["city"] == city) for city in CITIES},
        "by_plan": {plan: sum(1 for w in workers if w["plan"] == plan) for plan in ["Basic", "Standard", "Premium"]},
        "by_risk_tier": {tier: sum(1 for w in workers if w["risk_tier"] == tier) for tier in RISK_TIERS},
        "avg_weekly_premium": round(sum(w["weekly_premium"] for w in workers) / n, 2),
        "avg_claim_count": round(sum(w["claim_count"] for w in workers) / n, 2),
        "generated_at": datetime.now().isoformat(),
    }

    return {"workers": workers, "summary": summary}


if __name__ == "__main__":
    print("Generating synthetic dataset — 500 worker profiles across 5 cities...")
    dataset = generate_dataset(500)

    with open("synthetic_workers.json", "w") as f:
        json.dump(dataset, f, indent=2)

    print("Done. File saved: synthetic_workers.json")
    print(f"\nSummary:")
    for key, val in dataset["summary"].items():
        if key != "generated_at":
            print(f"  {key}: {val}")
