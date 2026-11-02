"""
Cynbit AI Discovery & Architectural Blueprint Engine (PoC)
Interactive Streamlit Workbench for Cynbit Technologies AI/ML Engineer Intern Assessment.
Author: Akshat Dwivedi
"""
import json
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from src.auditor import WebTelemetryAuditor
from src.sample_data import SAMPLE_PROFILES
from src.ai_architect import generate_discovery_blueprint

st.set_page_config(
    page_title="Cynbit AI Discovery & Blueprint Engine",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 1.6rem 2rem;
        border-radius: 12px;
        color: #f8fafc;
        margin-bottom: 1.2rem;
        border-left: 6px solid #38bdf8;
    }
    .main-header h1 {
        margin: 0;
        font-size: 1.85rem;
        color: #f8fafc;
    }
    .main-header p {
        margin: 0.35rem 0 0 0;
        color: #94a3b8;
        font-size: 0.98rem;
    }
    .stage-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-top: 4px solid #0284c7;
        border-radius: 8px;
        padding: 1rem;
        height: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="main-header">
        <h1>⚡ Cynbit Autonomous Phase-01 Discovery & Blueprint Engine</h1>
        <p>AI/ML Proof of Concept — Automating Technical SEO, Cloud Security & AI Readiness Audits into Cynbit's 6-Stage Architectural Lifecycle</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.header("⚙️ Audit Configuration")
    mode = st.radio(
        "Execution Mode",
        options=[
            "🚀 1-Click Benchmark Demo (Instant)",
            "🌐 Live Website URL Audit (Real-Time Scraper)",
        ],
        index=0,
    )

    if mode == "🚀 1-Click Benchmark Demo (Instant)":
        selected_profile = st.selectbox(
            "Select Benchmark Prospect",
            options=list(SAMPLE_PROFILES.keys()),
        )
        default_industry = SAMPLE_PROFILES[selected_profile]["industry"]
        industry_input = st.text_input("Client Industry / Vertical", value=default_industry)
    else:
        live_url = st.text_input("Enter Target Website URL", value="https://www.cynbit.in")
        industry_input = st.text_input(
            "Client Industry / Vertical",
            value="AI Automation & Software Engineering",
        )

    st.divider()
    st.subheader("🧠 LLM Synthesis Engine")
    gemini_api_key = st.text_input(
        "Gemini API Key (Optional)",
        type="password",
        help="Provide a Google Gemini API key for live Gemini 2.5 Flash Pydantic synthesis, or leave blank to use the built-in Deterministic Telemetry Synthesis Engine.",
    )
    st.caption(
        "💡 **Zero-Setup Guarantee:** Works out-of-the-box without an API key using our deterministic rule + telemetry synthesis fallback."
    )

    run_btn = st.button("⚡ Run Phase-01 Discovery Audit", type="primary", use_container_width=True)

if "audit_result" not in st.session_state or run_btn:
    with st.spinner("Inspecting DOM telemetry, security headers, SEO schemas & synthesizing Cynbit 6-Stage Blueprint..."):
        if mode == "🚀 1-Click Benchmark Demo (Instant)":
            profile_data = SAMPLE_PROFILES[selected_profile]
            telemetry = profile_data["telemetry"]
            industry = industry_input
        else:
            auditor = WebTelemetryAuditor(timeout=12)
            try:
                telemetry = auditor.extract_telemetry(live_url)
                industry = industry_input
            except Exception as e:
                st.warning(f"Live scrape encountered restriction ({e}). Falling back to Cynbit benchmark telemetry.")
                telemetry = SAMPLE_PROFILES["cynbit.in (Cynbit Technologies Official Site)"]["telemetry"]
                industry = industry_input

        blueprint = generate_discovery_blueprint(
            telemetry=telemetry,
            industry=industry,
            api_key=gemini_api_key if gemini_api_key.strip() else None,
        )
        st.session_state["audit_result"] = {
            "telemetry": telemetry,
            "blueprint": blueprint,
            "industry": industry,
        }

result = st.session_state["audit_result"]
telemetry = result["telemetry"]
blueprint = result["blueprint"]
scores = telemetry["scores"]

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Overall Digital Maturity", f"{scores['overall']} / 100", "Cynbit Benchmark")
col2.metric("Technical SEO Score", f"{scores['technical_seo']} / 100", f"{telemetry['seo']['json_ld_count']} JSON-LD Schemas")
col3.metric("Software Engineering", f"{scores['software_engineering']} / 100", f"{telemetry['latency_ms']} ms TTFB")
col4.metric("Cloud & Zero-Trust", f"{scores['cloud_infrastructure']} / 100", f"{telemetry['cloud_security']['security_headers_passed']}/4 Headers")
col5.metric("AI Automation Readiness", f"{scores['ai_automation']} / 100", "Agent Opportunity" if not telemetry["ai_readiness"]["has_ai_chat_widget"] else "Active Widget")

st.caption(f"**Target Audited:** `{telemetry['url']}`  |  **Synthesis Engine:** `{blueprint.get('generation_mode')}`")

tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Executive Blueprint & 6-Stage Roadmap",
    "🔍 Deep Technical Telemetry & Findings",
    "🧩 Cynbit SaaS & AI Agent Matcher",
    "📄 Export Proposal & Raw JSON",
])

with tab1:
    left_col, right_col = st.columns([1.45, 1])

    with left_col:
        st.subheader("Executive Architectural Diagnosis")
        st.info(blueprint["executive_summary"])

        st.subheader("🚨 Primary Technical & Growth Bottlenecks")
        for idx, b in enumerate(blueprint["primary_bottlenecks"], 1):
            st.markdown(f"**{idx}.** {b}")

        st.subheader("📈 Projected Client ROI Uplift")
        roi_df = pd.DataFrame(blueprint["roi_projections"])
        roi_df.columns = ["Target Metric", "Current Audited Baseline", "Projected Cynbit Impact"]
        st.dataframe(roi_df, use_container_width=True, hide_index=True)

    with right_col:
        st.subheader("4-Domain Mastery Radar")
        categories = [
            "Technical SEO",
            "Software Engineering",
            "Cloud & Security",
            "AI Automation",
        ]
        current_vals = [
            scores["technical_seo"],
            scores["software_engineering"],
            scores["cloud_infrastructure"],
            scores["ai_automation"],
        ]
        target_vals = [95, 94, 96, 92]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=current_vals + [current_vals[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name="Audited Baseline",
            line_color="#0284c7",
        ))
        fig.add_trace(go.Scatterpolar(
            r=target_vals + [target_vals[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name="Post-Cynbit Target",
            line_color="#10b981",
            opacity=0.45,
        ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            margin=dict(l=30, r=30, t=20, b=20),
            height=340,
        )
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.subheader("🏗️ Custom Cynbit 6-Stage Architectural Lifecycle Roadmap")
    stages = blueprint["lifecycle_roadmap"]
    row1 = st.columns(3)
    row2 = st.columns(3)
    grid_cols = row1 + row2

    for idx, stage in enumerate(stages[:6]):
        with grid_cols[idx]:
            deliverables_md = "".join([f"<li>{d}</li>" for d in stage["key_deliverables"]])
            st.markdown(
                f"""
                <div class="stage-card">
                    <h4 style="margin:0; color:#0284c7;">{stage['stage_number']} — {stage['stage_name']}</h4>
                    <p style="font-size:0.82rem; color:#64748b; margin:0.2rem 0 0.6rem 0;">⏱️ {stage['timeline_weeks']}</p>
                    <ul style="font-size:0.88rem; padding-left:1.1rem; margin:0;">{deliverables_md}</ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

with tab2:
    st.subheader("Deterministic Ground-Truth Findings")
    findings = telemetry.get("deterministic_findings", [])
    if findings:
        findings_df = pd.DataFrame(findings)
        findings_df.columns = ["Domain", "Severity", "Identified Issue", "DOM / HTTP Evidence", "Recommended Architectural Fix"]
        st.dataframe(findings_df, use_container_width=True, hide_index=True)
    else:
        st.success("All baseline deterministic checks passed!")

    c_seo, c_eng, c_sec = st.columns(3)
    with c_seo:
        st.markdown("#### 🔎 Technical SEO Signals")
        st.json(telemetry["seo"])
    with c_eng:
        st.markdown("#### 💻 Engineering & DOM Metrics")
        st.json(telemetry["engineering"])
    with c_sec:
        st.markdown("#### 🛡️ Cloud & Security Posture")
        st.json(telemetry["cloud_security"])

with tab3:
    st.subheader("🎯 Matched Cynbit SaaS Products & Service Pillars")
    p_cols = st.columns(len(blueprint["cynbit_product_matches"]))
    for idx, match in enumerate(blueprint["cynbit_product_matches"]):
        with p_cols[idx]:
            st.metric(label=match["product_name"], value=f"{match['fit_score']}% Match")
            st.write(match["rationale"])

    st.divider()
    st.subheader("🤖 Recommended Autonomous AI Agents to Build for This Client")
    for idx, agent in enumerate(blueprint["recommended_ai_agents"], 1):
        st.success(f"**Agent {idx}:** {agent}")

with tab4:
    st.subheader("📥 Download Client-Ready Discovery Report")
    md_export = f"""# Cynbit Phase-01 Discovery & Architectural Blueprint
**Audited URL:** {telemetry['url']}
**Industry:** {result['industry']}
**Overall Digital Maturity Score:** {scores['overall']}/100

## Executive Summary
{blueprint['executive_summary']}

## Primary Bottlenecks
""" + "\n".join([f"- {b}" for b in blueprint["primary_bottlenecks"]]) + """

## Recommended AI Agents
""" + "\n".join([f"- {a}" for a in blueprint["recommended_ai_agents"]])

    st.download_button(
        label="⬇️ Download Markdown Proposal (.md)",
        data=md_export,
        file_name=f"cynbit_discovery_blueprint_{telemetry['domain']}.md",
        mime="text/markdown",
    )
    st.markdown("#### Full Structured Audit Payload (JSON)")
    st.json(result)
