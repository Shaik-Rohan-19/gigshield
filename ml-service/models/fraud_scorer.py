"""
GigShield — Rule-Based Fraud Scorer (Phase 1)
Scores each claim 0–1. Routes to auto-approve, manual review, or auto-reject.
Phase 2 replaces this with Isolation Forest + Random Forest classifier.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ClaimContext:
    worker_id: str
    zone: str
    trigger_type: str
    trigger_timestamp: datetime
    claim_timestamp: datetime
    worker_gps_zone: Optional[str]          # GPS zone at time of trigger
    orders_during_event: int                 # Orders accepted during disruption window
    zone_order_drop_pct: float              # % drop in zone-wide orders
    workers_claiming_in_zone: int           # How many workers in zone also claiming
    total_workers_in_zone: int
    claim_count_last_30_days: int
    zone_avg_claims_per_month: float


WEIGHTS = {
    "gps_mismatch":        0.30,
    "platform_activity":   0.25,
    "claim_timing":        0.20,
    "zone_density":        0.15,
    "claim_frequency":     0.10,
}

THRESHOLDS = {
    "auto_approve": 0.30,
    "manual_review_upper": 0.60,
}


def score_claim(ctx: ClaimContext) -> dict:
    signals = {}

    # Signal 1: GPS zone match
    gps_mismatch = 0.0
    if ctx.worker_gps_zone and ctx.worker_gps_zone != ctx.zone:
        gps_mismatch = 1.0
    signals["gps_mismatch"] = gps_mismatch

    # Signal 2: Platform activity (should be ~0 orders during disruption)
    platform_signal = 0.0
    if ctx.orders_during_event > 5:
        platform_signal = 1.0
    elif ctx.orders_during_event > 2:
        platform_signal = 0.5
    signals["platform_activity"] = platform_signal

    # Signal 3: Claim timing (should be within 2 hours of trigger)
    time_diff = abs((ctx.claim_timestamp - ctx.trigger_timestamp).total_seconds() / 3600)
    if time_diff > 4:
        timing_signal = 1.0
    elif time_diff > 2:
        timing_signal = 0.5
    else:
        timing_signal = 0.0
    signals["claim_timing"] = timing_signal

    # Signal 4: Zone-wide claim density
    if ctx.total_workers_in_zone > 0:
        claim_rate = ctx.workers_claiming_in_zone / ctx.total_workers_in_zone
        # Isolated claim (low density) during claimed zone-wide event = suspicious
        if claim_rate < 0.1:
            zone_signal = 0.8
        elif claim_rate > 0.5:
            zone_signal = 0.0  # Zone-wide — expected
        else:
            zone_signal = 0.3
    else:
        zone_signal = 0.5
    signals["zone_density"] = zone_signal

    # Signal 5: Historical claim frequency
    freq_ratio = ctx.claim_count_last_30_days / max(1, ctx.zone_avg_claims_per_month)
    if freq_ratio > 3:
        freq_signal = 1.0
    elif freq_ratio > 2:
        freq_signal = 0.6
    elif freq_ratio > 1.5:
        freq_signal = 0.3
    else:
        freq_signal = 0.0
    signals["claim_frequency"] = freq_signal

    # Weighted total
    fraud_score = sum(WEIGHTS[k] * signals[k] for k in WEIGHTS)
    fraud_score = round(min(1.0, max(0.0, fraud_score)), 3)

    # Routing decision
    if fraud_score < THRESHOLDS["auto_approve"]:
        decision = "AUTO_APPROVE"
    elif fraud_score <= THRESHOLDS["manual_review_upper"]:
        decision = "MANUAL_REVIEW"
    else:
        decision = "AUTO_REJECT"

    return {
        "worker_id": ctx.worker_id,
        "fraud_score": fraud_score,
        "decision": decision,
        "signals": signals,
        "weights": WEIGHTS,
        "scored_at": datetime.now().isoformat(),
    }


# --- Demo ---
if __name__ == "__main__":
    # Ravi's clean claim during rain event
    ravi = ClaimContext(
        worker_id="W0001",
        zone="Kukatpally",
        trigger_type="heavy_rainfall",
        trigger_timestamp=datetime(2024, 7, 9, 14, 47),
        claim_timestamp=datetime(2024, 7, 9, 14, 48),
        worker_gps_zone="Kukatpally",
        orders_during_event=0,
        zone_order_drop_pct=87.0,
        workers_claiming_in_zone=312,
        total_workers_in_zone=380,
        claim_count_last_30_days=2,
        zone_avg_claims_per_month=1.8,
    )

    result = score_claim(ravi)
    print("=== Fraud Score — Ravi Kumar ===")
    print(f"Score:    {result['fraud_score']}")
    print(f"Decision: {result['decision']}")
    print(f"\nSignals:")
    for k, v in result["signals"].items():
        print(f"  {k}: {v}")

    print("\n--- High-risk claim (Suresh K.) ---")
    suresh = ClaimContext(
        worker_id="W0142",
        zone="Kukatpally",
        trigger_type="heavy_rainfall",
        trigger_timestamp=datetime(2024, 7, 9, 14, 47),
        claim_timestamp=datetime(2024, 7, 9, 14, 48),
        worker_gps_zone="Secunderabad",   # Wrong zone
        orders_during_event=7,            # Still working
        zone_order_drop_pct=87.0,
        workers_claiming_in_zone=312,
        total_workers_in_zone=380,
        claim_count_last_30_days=8,       # Way above average
        zone_avg_claims_per_month=1.8,
    )
    result2 = score_claim(suresh)
    print(f"Score:    {result2['fraud_score']}")
    print(f"Decision: {result2['decision']}")
