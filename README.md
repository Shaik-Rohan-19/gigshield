# GigShield — AI-Powered Parametric Income Insurance for Food Delivery Partners

**Guidewire DEVTrails 2026 | University Hackathon**
**Team:** Cloud-4C · Koneru Lakshmaiah University
**Persona:** Food Delivery Partners — Zomato / Swiggy
**Phase 1 Submission Deadline:** March 20, End of Day

> 🎥 **2-Minute Video:** [Insert your video link here — YouTube / Loom / Google Drive]
> 🔗 **Live Prototype:** Open `prototype/index.html` in any browser — no install needed

---

## Table of Contents

1. [Problem Statement](#1-problem-statement)
2. [What is GigShield?](#2-what-is-gigshield)
3. [Persona & Scenarios](#3-persona--scenarios)
4. [Application Workflow](#4-application-workflow)
5. [Weekly Premium Model](#5-weekly-premium-model)
6. [Parametric Triggers](#6-parametric-triggers)
7. [Platform Choice — Web or Mobile](#7-platform-choice--web-or-mobile)
8. [AI/ML Integration Plan](#8-aiml-integration-plan)
9. [Tech Stack](#9-tech-stack)
10. [How to Run the Prototype](#10-how-to-run-the-prototype)
11. [Development Plan](#11-development-plan)
12. [Coverage Scope & Exclusions](#12-coverage-scope--exclusions)

---

## 1. Problem Statement

India has over 5 million gig delivery workers. They are the backbone of platforms like Zomato, Swiggy, Zepto, and Amazon — but they have no financial protection against external disruptions they cannot control.

When heavy rain hits Hyderabad, a delivery partner loses ₹400–₹700 in a single day. When a city-wide bandh is called, they lose a full day's income overnight. When a heat wave forces platform zone suspensions, they sit at home with zero earnings.

There is no sick leave. No employer compensation. No government scheme. When disruptions occur, gig workers bear the full financial loss alone.

**GigShield solves this** — an AI-enabled parametric insurance platform that detects external disruptions automatically, verifies them across multiple data sources, scores each claim for fraud, and pays out to the worker's UPI account within 2 hours. Zero forms. Zero phone calls. Zero effort from the worker.

---

## 2. What is GigShield?

GigShield is a **weekly parametric income insurance platform** built exclusively for food delivery partners on Zomato and Swiggy.

**Parametric** means we don't ask "what did you lose?" — we ask "did this measurable event happen?" If rainfall exceeds 35mm/hr in the worker's zone for 30+ minutes, the payout triggers automatically. No assessment. No adjuster. No waiting.

**Weekly pricing** aligns with how delivery workers actually get paid — Zomato and Swiggy disburse partner earnings every Monday. Insurance that deducts weekly from that same cycle is insurance workers will actually keep renewing.

**AI-powered** means the premium is not static — it is recalculated each week based on the worker's zone risk, seasonal forecast, and personal claim history. Fraud detection runs in milliseconds using GPS, platform activity, and zone-wide patterns before any payout is released.

---

## 3. Persona & Scenarios

### Our Persona — Ravi Kumar, 27

Ravi is a Swiggy delivery partner based in **Kukatpally, Hyderabad**. He works 10 hours a day, 6 days a week, earning ₹600–₹800 on a good day. His weekly take-home from Swiggy is ₹3,500–₹4,500, paid every Monday.

He uses a budget Android phone, transacts daily on UPI, and gets information via WhatsApp. He will not install a new app for a non-essential service. He will not fill out a long form. If something takes more than 3 taps, he abandons it.

---

### Scenario 1 — Heavy Rain Disruption

Kukatpally receives 62mm of rainfall. Swiggy suspends the zone. Orders dry up.

**What GigShield does — automatically:**

1. Trigger engine detects 62mm/hr via OpenWeatherMap (threshold: 35mm/hr)
2. Cross-validates with IMD's rainfall advisory — confirmed
3. Swiggy order volume in zone drops 87% — second signal confirmed
4. Fraud score computed: GPS ✓ · Zone match ✓ · Zone-wide pattern ✓ · Score: 0.12 — auto-approved
5. ₹350 credited to ravi.kumar@oksbi within 2 hours
6. Push notification: *"Heavy rain detected in your zone. ₹350 credited. Stay safe."*

Ravi did nothing. Money showed up.

---

### Scenario 2 — Extreme Heat Wave

IMD issues heat wave advisory — temperature hits 43°C. Swiggy reduces active zones.

1. IMD Heat Watch RSS triggers — temp >42°C during peak hours confirmed
2. 4 hours of peak work affected → ₹240 credited proportionally

---

### Scenario 3 — City-Wide Bandh

A sudden local bandh is declared. All zones halted.

1. Government alert API + NewsAPI confirms bandh covering Ravi's zone
2. Order drop >70% across all Hyderabad zones — cross-validation confirmed
3. 847 GigShield workers get batch claims initiated simultaneously
4. Ravi receives ₹500 (full-day Standard plan coverage) before noon

---

### Scenario 4 — Normal Week

No disruption. ₹60 deducted Monday 7 AM. Ravi's dashboard shows: *"Covered for ₹1,400 this week."*

---

## 4. Application Workflow

```
ONBOARDING
──────────
Worker opens PWA via WhatsApp link (no app download)
     ↓
Phone + OTP verification
     ↓
Zone selection + working hours
     ↓
AI risk profiling → recommended plan + personalised premium
     ↓
UPI AutoPay setup (NACH mandate, ₹/week every Monday)
     ↓
Policy activated

LIVE MONITORING (24/7)
───────────────────────
Trigger engine polls 5 APIs every 15 minutes
     ↓
Threshold breached?
   NO  → continue polling
   YES → cross-validate with second data source
           ↓
         Both confirmed? → compute fraud score per worker in zone

CLAIM & PAYOUT (automated)
──────────────────────────
Score < 0.3   → AUTO-APPROVE  → UPI payout via Razorpay
Score 0.3–0.6 → MANUAL REVIEW → Admin approves / rejects
Score > 0.6   → AUTO-REJECT   → Account flagged
     ↓
Worker notified via push notification
Dashboard updated — weekly balance reduced by payout amount
Monday: new premium deducted, new week of coverage begins
```

### Worker-Facing Screens

| Screen | Purpose |
|--------|---------|
| Onboarding (5 steps) | Phone → OTP → Zone/Hours → Plan → UPI AutoPay |
| Dashboard | Coverage status, weekly balance, premium breakdown, alerts |
| Claims tracker | All payouts with trigger type, amount, fraud score |
| Policy details | Plan, triggers covered, renewal date, pause option |

### Admin-Facing Screens

| Screen | Purpose |
|--------|---------|
| Analytics dashboard | Premiums, payouts, loss ratio, zone performance |
| Live trigger monitor | Real-time disruption alerts across all zones |
| Claims queue | Manual review items with fraud signals |
| Fraud monitor | Flagged accounts, anomaly patterns |
| Zone risk map | Risk scores per zone, claim heatmap |
| AI forecast | Predicted payout range for next 7 days |

---

## 5. Weekly Premium Model

### Why Weekly Pricing?

Zomato and Swiggy pay delivery partners every Monday. Weekly insurance that deducts from the same cycle removes the friction of a monthly upfront cost. Workers cannot commit ₹240/month when they are not sure what next week looks like. Weekly pricing = zero renewal friction = higher retention.

### Base Tiers

| Plan | Weekly Premium | Max Weekly Payout | Daily Cap |
|------|---------------|-------------------|-----------|
| Basic | ₹29 | ₹700 | ₹100 |
| **Standard (recommended)** | **₹49** | **₹1,400** | **₹200** |
| Premium | ₹79 | ₹2,500 | ₹350 |

### AI-Driven Weekly Adjustment

Every Monday at 6 AM the ML model recalculates each worker's premium:

| Factor | Data Source | Range |
|--------|-------------|-------|
| Zone flood/waterlogging history | IMD historical records | +₹0 to +₹15 |
| Seasonal monsoon probability | IMD monthly outlook | +₹0 to +₹10 |
| 7-day disruption forecast | IMD 7-day forecast | +₹0 to +₹8 |
| City AQI rolling average | CPCB API | +₹0 to +₹6 |
| Personal no-claim discount | Internal claims DB | −₹2 to −₹8 |

### Ravi's Premium This Week

```
Base (Standard):               ₹49
Zone risk — Kukatpally:       +₹8
Monsoon season — July:        +₹5
7-day forecast — 3 rain days: +₹4
No-claim discount (6 weeks):  −₹6
──────────────────────────────────
Total this week:               ₹60
```

Full breakdown visible in the worker dashboard. No hidden adjustments.

### Premium Collection

- Deducted every **Monday at 7 AM** via UPI AutoPay (NACH mandate)
- Set up once at onboarding — never needs to be repeated
- Workers can pause for up to **2 weeks per quarter**
- Mid-week joins are prorated

---

## 6. Parametric Triggers

Every trigger requires **two independent signals** before a payout is initiated — preventing false payouts from API glitches.

### Trigger 1 — Heavy Rainfall

| | |
|--|--|
| **Primary API** | OpenWeatherMap API (free tier) |
| **Secondary API** | IMD Rainfall Advisory (public feed) |
| **Threshold** | >35mm/hr sustained for 30+ minutes |
| **Cross-validation** | IMD advisory issued OR Swiggy zone order drop >60% |
| **Payout** | ₹150–₹350 by duration and tier |
| **Why 35mm/hr?** | Platforms actively suspend zones above this level — operational reality, not a guess |

### Trigger 2 — Extreme Heat Wave

| | |
|--|--|
| **Primary API** | OpenWeatherMap current conditions |
| **Secondary API** | IMD Heat Watch Alerts (RSS feed) |
| **Threshold** | >42°C during 10 AM–4 PM (peak delivery hours) |
| **Payout** | ₹100–₹280 proportional to hours affected |
| **Why 42°C?** | IMD heat wave classification + point where platforms visibly reduce zones |

### Trigger 3 — Severe Air Pollution

| | |
|--|--|
| **Primary API** | CPCB AQI API — api.data.gov.in (free, government) |
| **Threshold** | AQI >300 (Hazardous) for 4+ continuous hours |
| **Payout** | ₹100–₹200 per day |
| **Why AQI 300?** | CPCB recommends no outdoor activity — platforms in Delhi NCR already pause at this level |

### Trigger 4 — Flood / Waterlogging

| | |
|--|--|
| **Primary API** | IMD Flood Watch API |
| **Secondary API** | GHMC (Hyderabad) civic body public alerts |
| **Threshold** | Official flood or waterlogging advisory for worker's zone |
| **Payout** | ₹250–₹500 per day |
| **Note** | Separate from rain — moderate rain causing waterlogging still triggers payout |

### Trigger 5 — Curfew / Bandh / Zone Closure

| | |
|--|--|
| **Primary API** | Government emergency alerts API |
| **Secondary API** | NewsAPI (free tier) — bandh, curfew, strike sentiment |
| **Threshold** | Official curfew or verified bandh for 3+ hours |
| **Cross-validation** | Govt/news signal AND >60% platform order drop |
| **Payout** | ₹200–₹600 by duration |

---

## 7. Platform Choice — Web or Mobile

### Decision: Progressive Web App (PWA)

Ravi has a budget Android phone with 4–6 GB storage. Half of it is used by Zomato/Swiggy, WhatsApp, and Google Maps. He will not install another app for something he does not yet trust.

But if Swiggy sends him a WhatsApp link saying *"Tap here to protect your income — no download needed"*, he will tap it. That frictionless entry is only possible with a PWA.

| Factor | PWA | Native App |
|--------|-----|-----------|
| Installation required | No — opens in browser | Yes — Play Store |
| Storage on device | ~0.5 MB | 20–50 MB |
| Works on any Android | Yes | Requires Android 5.0+ |
| Push notifications | Yes (FCM) | Yes |
| Offline support | Yes (service workers) | Yes |
| Admin desktop view | Same codebase | Separate build needed |
| App store delays | None | 2–5 days per update |
| Update delivery | Instant, silent | Requires user to update |

Worker-facing: mobile-first, 360px optimised, large tap targets.
Admin-facing: same codebase serves the desktop analytics dashboard.

---

## 8. AI/ML Integration Plan

AI/ML is in the core loop — not decoration. Each module delivers a rule-based version in Phase 1 and upgrades to a trained ML model in Phase 2 without changing the API interface.

### Module 1 — Dynamic Premium Calculator

| | |
|--|--|
| **Phase 1** | Rule-based scoring formula |
| **Phase 2** | XGBoost / LightGBM regression model |
| **Inputs** | Zone risk score, seasonal index, 7-day IMD forecast, claim history, AQI rolling average |
| **Output** | Weekly ₹ premium with per-factor breakdown |
| **Retrain** | Weekly, using last 30 days of claims data |

### Module 2 — Risk Profiler (Onboarding)

| | |
|--|--|
| **Phase 1** | Rule-based tier assignment from zone + hours + city |
| **Phase 2** | Random Forest classifier |
| **Output** | Risk tier (Low/Medium/High) + recommended plan |

### Module 3 — Fraud Detection Engine

| | |
|--|--|
| **Phase 1** | Rule-based weighted scoring on 5 signals |
| **Phase 2** | Isolation Forest + Random Forest classifier |

**5 fraud signals:**

| Signal | What We Check | Weight |
|--------|--------------|--------|
| GPS zone match | Was worker's device in the affected zone? | High |
| Platform activity | Did worker show zero orders in disruption window? | High |
| Claim timing | Was claim within valid disruption window? | Medium |
| Zone claim density | Zone-wide pattern or isolated claim? | High |
| Historical claim rate | Frequency vs zone average? | Medium |

**Score routing:**
```
Score < 0.3   → AUTO-APPROVE  → Payout released immediately
Score 0.3–0.6 → MANUAL REVIEW → Admin reviews within 4 hours
Score > 0.6   → AUTO-REJECT   → Account flagged
```

### Module 4 — Disruption Forecaster (Phase 3)

| | |
|--|--|
| **Model** | LSTM time-series |
| **Purpose** | Predict next week's payout range by zone |
| **Used for** | Insurer reserve planning · worker upgrade prompts · premium adjustment |

### Phase 1 AI/ML Deliverables

| File | Description | Status |
|------|-------------|--------|
| `ml-service/models/premium_calculator.py` | Rule-based premium formula | In progress |
| `ml-service/models/fraud_scorer.py` | Rule-based fraud signal skeleton | In progress |
| `ml-service/data/synthetic_data_gen.py` | 500 mock worker profiles, 5 cities | In progress |
| `data/zone_risk_scores.json` | Pre-computed zone risk data, Hyderabad | In progress |

---

## 9. Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | React.js + Tailwind CSS (PWA) | Mobile-first, no app store, offline support |
| Backend | Node.js + Express | Lightweight REST APIs, real-time polling |
| Database | PostgreSQL | Structured insurance/claims data |
| Cache | Redis | Real-time trigger state storage |
| ML Service | Python + FastAPI | Independent microservice |
| Premium model | XGBoost / LightGBM | Industry standard for tabular ML |
| Fraud model | Isolation Forest + Random Forest | Anomaly detection + classification |
| Forecast model | LSTM (Phase 3) | Time-series disruption prediction |
| Weather | OpenWeatherMap API (free tier) | Reliable, good Indian city coverage |
| AQI | CPCB API — api.data.gov.in (free) | Official government AQI data |
| IMD alerts | IMD public feeds (RSS + HTTP) | Flood, heat, rainfall advisories |
| News/bandh | NewsAPI (free tier) | Curfew/bandh sentiment detection |
| Payments | Razorpay Test Mode | Realistic UPI AutoPay simulation |
| Notifications | Firebase Cloud Messaging | Push notifications — free tier |
| Auth | OTP via fast2sms (free tier) | What delivery workers use daily |
| Hosting | Vercel (frontend) + Render (backend) | Free tiers, fast deployment |

### Repository Structure

```
gigshield/
├── prototype/
│   └── index.html              ← OPEN THIS to see the working prototype
│
├── frontend/                   # React PWA (Phase 2)
│   └── src/
│       ├── pages/
│       │   ├── Onboarding.jsx
│       │   ├── Dashboard.jsx
│       │   ├── ClaimStatus.jsx
│       │   └── AdminDashboard.jsx
│       └── services/api.js
│
├── backend/                    # Node.js + Express (Phase 2)
│   ├── routes/
│   │   ├── auth.js
│   │   ├── policy.js
│   │   ├── triggers.js         ← Parametric trigger engine
│   │   ├── claims.js
│   │   └── payouts.js
│   └── services/
│       ├── weatherService.js   ← OpenWeatherMap polling
│       ├── aqiService.js       ← CPCB AQI
│       ├── imdService.js       ← IMD alerts
│       ├── newsService.js      ← NewsAPI bandh detection
│       └── fraudService.js     ← Calls ML fraud scorer
│
├── ml-service/                 # Python + FastAPI
│   ├── api/main.py             ← /premium /fraud-score /forecast
│   ├── models/
│   │   ├── premium_calculator.py
│   │   ├── fraud_scorer.py
│   │   └── forecast_model.py
│   └── data/
│       └── synthetic_data_gen.py
│
├── data/
│   └── zone_risk_scores.json
│
├── WORKFLOW.md                 ← Full system documentation
└── README.md                   ← This file
```

---

## 10. How to Run the Prototype

### Option A — Instant (no install required)

```bash
# Clone the repo
git clone https://github.com/cloud-4c/gigshield.git
cd gigshield

# Open the prototype directly in your browser
open prototype/index.html
# or on Windows:
start prototype/index.html
```

That's it. The prototype is a single self-contained HTML file.

### What You'll See

| Tab | What it shows |
|-----|--------------|
| **Dashboard** | Ravi's live coverage, premium breakdown, recent payouts, weather alert |
| **Onboarding** | Full 5-step worker sign-up flow — click through each step |
| **Live Triggers** | 5 trigger status bars + 3 simulate buttons (rain/heat/bandh) |
| **Claims** | Complete claims history with fraud scores |
| **Admin** | Insurer dashboard — metrics, zone risk, fraud review queue |

### Key Interactions to Demo

1. **Simulate Rain** → Triggers screen → "🌧️ Trigger Now" → watch toast notifications → disruption modal → click "Simulate Payout ₹350" → success modal
2. **Onboarding flow** → click through all 5 steps → watch coverage activate
3. **Fraud review** → Admin tab → approve or reject flagged claims
4. **Weather alert** → Dashboard → click the yellow alert banner

### Option B — Run with a local server

```bash
cd gigshield/prototype
python3 -m http.server 8080
# Open http://localhost:8080 in your browser
```

---

## 11. Development Plan

### Phase 1 — Ideation & Foundation (March 4–20) ← Current

| Task | Status |
|------|--------|
| Persona research + 4 real-world scenarios | Done |
| 5 triggers defined with API sources and thresholds | Done |
| Weekly premium model with dynamic adjustment formula | Done |
| Platform decision (PWA) justified | Done |
| README.md — full Phase 1 submission document | Done |
| WORKFLOW.md — complete system documentation | Done |
| Prototype — single-file interactive demo | Done |
| Synthetic dataset (500 worker profiles, 5 cities) | In progress |
| Premium calculator Python script | In progress |
| Live API integrations tested (OpenWeatherMap + CPCB) | In progress |
| Fraud signal schema + DB design | In progress |
| Figma wireframes | Planned |
| 2-minute strategy video | Planned |

### Phase 2 — Automation & Protection (March 21 – April 4)

| Task | Description |
|------|-------------|
| Full onboarding flow | Live PWA, 5 steps, under 3 minutes |
| ML premium engine | XGBoost replaces rule-based script |
| 5 live trigger integrations | Real APIs, 15-minute polling |
| Auto-claim pipeline | Trigger → fraud score → approve/reject |
| Mock UPI payouts | Razorpay test mode |
| Worker dashboard | Coverage, balance, claims, alerts |
| 2-minute demo video | Full working prototype walkthrough |

### Phase 3 — Scale & Optimise (April 5–17)

| Task | Description |
|------|-------------|
| Advanced fraud detection | GPS spoofing + syndicate pattern detection |
| LSTM forecasting model | Predict next week's payout range |
| Insurer admin dashboard | Loss ratios, zone map, fraud queue, AI forecast |
| Full end-to-end simulation | Rain trigger → payout, live demo |
| 5-minute demo video | Complete platform walkthrough |
| Final pitch deck (PDF) | Persona, AI architecture, business viability |

---

## 12. Coverage Scope & Exclusions

### What GigShield Covers

Income lost because a verifiable, external, measurable event made it impossible or unsafe to work.

| Event | Covered | Trigger Source |
|-------|---------|---------------|
| Heavy rainfall >35mm/hr | Yes | OpenWeatherMap + IMD |
| Extreme heat >42°C during peak hours | Yes | IMD Heat Watch |
| Hazardous AQI >300 for 4+ hours | Yes | CPCB AQI API |
| Official flood/waterlogging advisory | Yes | IMD + civic body |
| Official curfew or verified bandh | Yes | Govt alert + NewsAPI |

### What GigShield Does NOT Cover

As mandated by the problem statement — strictly excluded:

| Item | Status |
|------|--------|
| Vehicle repairs or maintenance | Excluded |
| Health or medical expenses | Excluded |
| Accident compensation | Excluded |
| Life insurance | Excluded |
| Income loss from personal decisions | Excluded |
| Slow business days with no trigger event | Excluded |

---

## Why GigShield Wins

**1. Zero effort from the worker.** Ravi never files a claim. The money just appears. For someone managing 10-hour days on a bike in the Hyderabad heat, removing all friction is not a feature — it is the product.

**2. Priced for the person, not a category.** Weekly premium recalculated every Monday using real zone data, real forecasts, and Ravi's own history. He pays ₹60 in July and might pay ₹51 in February.

**3. Fraud detection built for parametric.** Fraud prevention in parametric insurance cannot happen after the payout. Our fraud score runs five delivery-specific signals in under 30 seconds — before a single rupee leaves the system.

---

*GigShield — Because every delivery partner deserves a safety net.*

*Built for Guidewire DEVTrails 2026 — Seed. Scale. Soar.*

*Team Cloud-4C · Koneru Lakshmaiah University ·Vijayawada*
