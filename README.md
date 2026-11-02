# ⚡ Cynbit Autonomous Phase-01 Discovery & Blueprint Engine

**AI/ML Engineer Intern Technical Assessment — Cynbit Technologies**  
**Candidate:** Akshat Dwivedi (B.Tech CSE, Manipal University Jaipur)

---

## 📌 Executive Overview

This repository contains the complete submission for the **Cynbit AI/ML Engineer Intern Practical Assessment**:
1. 📄 **[AI Opportunity Report (`reports/AI_OPPORTUNITY_REPORT.md`)](reports/AI_OPPORTUNITY_REPORT.md):** Comprehensive ecosystem analysis of Cynbit Technologies (`cynbit.in`) across its Custom IT/AI Agency pillar, Proprietary SaaS Suite (**Revio**, **TenantEase**, **Cynbit Studio**), and **BitElevate**, identifying 4 high-ROI AI opportunities and deep-diving into the **Autonomous Phase-01 Discovery & Technical SEO Audit Engine**.
2. 💻 **Working AI/ML Proof of Concept (`app.py`, `src/`):** A modular Python + Streamlit application that scrapes live website HTTP/DOM telemetry, scores the prospect across Cynbit's 4 mastery domains (*Technical SEO*, *Software Engineering*, *Cloud Infrastructure*, *AI Automation*), matches Cynbit SaaS products, and synthesizes a custom **6-Stage Architectural Lifecycle Blueprint** using **Gemini 2.5 Flash** (with a built-in zero-key deterministic fallback engine).
3. 🛠️ **[Technical Approach Report (`reports/TECHNICAL_APPROACH_REPORT.md`)](reports/TECHNICAL_APPROACH_REPORT.md):** Detailed documentation of the hybrid neuro-symbolic architecture, model choices, Pydantic prompt engineering guardrails, and AWS/Azure production roadmap.

---

## 🚀 Quickstart (Run Locally in 60 Seconds)

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/cynbit-ai-opportunity-poc.git
cd cynbit-ai-opportunity-poc

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the interactive Streamlit Workbench
streamlit run app.py
```

> **Note for Evaluators:** The app includes a **🚀 1-Click Benchmark Demo Mode** pre-loaded with telemetry for `cynbit.in` and two representative client archetypes (*E-Commerce Retail* & *Real Estate Portal*), plus a **🌐 Live Website URL Scraper**. It runs out-of-the-box **without requiring an API key**, and automatically upgrades to live **Gemini 2.5 Flash** structured synthesis if a `GEMINI_API_KEY` is entered in the sidebar.

---

## 📂 Repository Structure

```text
cynbit-ai-opportunity-poc/
├── app.py                                # Interactive Streamlit Discovery Workbench
├── requirements.txt                      # Python dependencies
├── push_with_clean_commits.sh            # 1-command script to create 6 atomic Git commits & push
├── push_with_clean_commits.bat           # Windows batch script for 6 atomic Git commits & push
├── reports/
│   ├── AI_OPPORTUNITY_REPORT.md          # Deliverable 1: Cynbit AI Opportunity Analysis
│   └── TECHNICAL_APPROACH_REPORT.md      # Deliverable 3: Architecture, Models & Execution Plan
└── src/
    ├── __init__.py
    ├── auditor.py                        # Live HTTP/DOM Telemetry Scraper & 4-Domain Scorer
    ├── ai_architect.py                   # Gemini 2.5 Flash Pydantic Synthesizer + Fallback Engine
    └── sample_data.py                    # Benchmark datasets for instant zero-setup evaluation
```
