"""
LLM Blueprint Synthesizer for Cynbit Phase-01 Discovery & Audit Engine.
Uses Google GenAI (Gemini 2.5 Flash) with strict Pydantic structured outputs,
and includes an intelligent deterministic fallback synthesizer when no API key is provided.
"""
import json
import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class LifecycleStagePlan(BaseModel):
    stage_number: str = Field(description="Stage number from 01 to 06")
    stage_name: str = Field(description="Cynbit Lifecycle Stage Name")
    key_deliverables: List[str] = Field(description="2-3 concrete technical deliverables tailored to the audited site")
    timeline_weeks: str = Field(description="Estimated duration in weeks, e.g., 'Week 1'")


class CynbitProductMatch(BaseModel):
    product_name: str = Field(description="Name of Cynbit SaaS or Service Pillar (e.g., Revio, TenantEase, Cynbit Studio, Custom AI Agents, Cloud Migration)")
    fit_score: int = Field(description="Fit score from 0 to 100")
    rationale: str = Field(description="Why this Cynbit offering solves the prospect's exact bottlenecks")


class ROIEstimate(BaseModel):
    metric: str = Field(description="Business or technical metric name")
    current_baseline: str = Field(description="Current observed or estimated baseline")
    projected_uplift: str = Field(description="Expected improvement after Cynbit implementation")


class DiscoveryBlueprintReport(BaseModel):
    executive_summary: str = Field(description="Concise 3-sentence executive diagnosis of the prospect's digital infrastructure")
    primary_bottlenecks: List[str] = Field(description="Top 3 high-priority technical or growth bottlenecks identified")
    recommended_ai_agents: List[str] = Field(description="2-3 custom LLM/autonomous agent workflows Cynbit can deploy for this client")
    cynbit_product_matches: List[CynbitProductMatch] = Field(description="Matched Cynbit SaaS products and service pillars")
    lifecycle_roadmap: List[LifecycleStagePlan] = Field(description="Action plan mapped strictly to Cynbit's 6-Stage Architectural Lifecycle")
    roi_projections: List[ROIEstimate] = Field(description="3 concrete ROI and performance uplift projections")


SYSTEM_PROMPT = """You are the Principal AI Solution Architect at Cynbit Technologies (Jaipur, India).
Your job is to analyze raw HTTP, DOM, Technical SEO, Cloud Security, and AI Readiness telemetry from a prospect's website and synthesize a high-converting 'Phase-01 Discovery & Architectural Blueprint'.

Always ground every finding in the provided telemetry metrics (e.g., cite exact latency, DOM node counts, missing headers, H1/meta counts, or missing JSON-LD schemas).
Map the execution roadmap strictly to Cynbit's 6-Stage Architectural Lifecycle:
01 Discovery & Audit
02 Strategy & Blueprinting
03 High-Fidelity Design
04 Technical Implementation
05 Quality & Integrity Check
06 Deployment & Evolution

Also evaluate fit for Cynbit's proprietary SaaS ecosystem where relevant:
- Revio (AI Review Assistant for e-commerce, hospitality, and service brands)
- TenantEase (Property management ecosystem for real estate & housing)
- Cynbit Studio & BitElevate (Career intelligence & enterprise engineering upskilling)
- Custom AI Automation & Cloud Infrastructure (AWS/Azure Zero-Trust & Custom LLM Agents)
"""


def generate_discovery_blueprint(
    telemetry: Dict[str, Any],
    industry: str = "Digital Business",
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Synthesizes a complete Cynbit Phase-01 Discovery Blueprint.
    Uses Gemini 2.5 Flash structured outputs if an API key is provided;
    otherwise uses a deterministic ground-truth synthesis engine.
    """
    effective_key = api_key or os.environ.get("GEMINI_API_KEY")

    if effective_key:
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=effective_key)
            clean_telemetry = {k: v for k, v in telemetry.items() if k != "text_excerpt"}
            user_prompt = "\n".join([
                f"Target Website: {telemetry.get('url')}",
                f"Client Industry: {industry}",
                "Extracted Telemetry & Scores JSON:",
                json.dumps(clean_telemetry, indent=2),
                "Page Content Excerpt:",
                telemetry.get("text_excerpt", "")[:1200],
            ])

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=DiscoveryBlueprintReport,
                    temperature=0.2,
                ),
            )
            parsed_data = json.loads(response.text)
            parsed_data["generation_mode"] = "Gemini 2.5 Flash (Structured JSON Schema)"
            return parsed_data
        except Exception as exc:
            fallback = _build_deterministic_blueprint(telemetry, industry)
            fallback["generation_mode"] = f"Deterministic Ground-Truth Engine (API Fallback: {type(exc).__name__})"
            return fallback

    blueprint = _build_deterministic_blueprint(telemetry, industry)
    blueprint["generation_mode"] = "Deterministic Rule + Telemetry Synthesis Engine (Zero-Key Mode)"
    return blueprint


def _build_deterministic_blueprint(telemetry: Dict[str, Any], industry: str) -> Dict[str, Any]:
    """Builds a rich, telemetry-grounded blueprint when running in offline/zero-key mode."""
    domain = telemetry.get("domain", "target-site.com")
    scores = telemetry.get("scores", {})
    seo = telemetry.get("seo", {})
    eng = telemetry.get("engineering", {})
    sec = telemetry.get("cloud_security", {})
    ai = telemetry.get("ai_readiness", {})

    overall = scores.get("overall", 60)
    latency = telemetry.get("latency_ms", 500)

    bottlenecks = []
    if seo.get("json_ld_count", 0) == 0 or seo.get("meta_description_length", 0) == 0:
        bottlenecks.append(
            f"Search Visibility Deficit: {seo.get('json_ld_count', 0)} JSON-LD schemas and "
            f"{seo.get('images_missing_alt', 0)}/{seo.get('total_images', 0)} images missing alt attributes limit organic discovery."
        )
    if not ai.get("has_ai_chat_widget"):
        bottlenecks.append(
            f"Unautomated Lead Capture: Relies on {ai.get('interactive_forms', 0)} static HTML form(s) with zero autonomous AI qualification or instant customer triage."
        )
    if sec.get("security_headers_passed", 0) < 4:
        bottlenecks.append(
            f"Cloud Edge Hardening Gap: Only {sec.get('security_headers_passed', 0)}/4 Zero-Trust HTTP security headers enforced on {sec.get('server_banner', 'current host')}."
        )
    if latency > 700 or eng.get("total_dom_nodes", 0) > 1200:
        bottlenecks.append(
            f"Frontend & TTFB Friction: {latency}ms initial response time with {eng.get('total_dom_nodes', 0)} DOM nodes and {eng.get('script_count', 0)} script bundles."
        )
    if not bottlenecks:
        bottlenecks.append(
            "Conversion Intelligence Opportunity: Strong baseline infrastructure can achieve 3x lead velocity by embedding interactive AI discovery agents."
        )

    lower_ind = industry.lower()
    lower_text = telemetry.get("text_excerpt", "").lower()

    product_matches = [
        {
            "product_name": "Cynbit AI Automation & Autonomous Agents",
            "fit_score": 96,
            "rationale": f"Replaces static forms on {domain} with a 24/7 RAG-grounded conversational qualification & discovery agent."
        },
        {
            "product_name": "Cynbit Technical SEO & Cloud Growth Engine",
            "fit_score": 91 if scores.get("technical_seo", 70) < 85 else 82,
            "rationale": f"Fixes schema.org JSON-LD gaps, optimizes {eng.get('script_count', 0)} scripts, and hardens AWS/Azure edge security headers."
        },
    ]

    if any(k in lower_ind or k in lower_text for k in ["retail", "commerce", "shop", "review", "wardrobe", "brand"]):
        product_matches.insert(0, {
            "product_name": "Revio (Cynbit AI Review Assistant SaaS)",
            "fit_score": 95,
            "rationale": "Automates multi-aspect sentiment analysis, review replies, and AggregateRating schema for higher e-commerce conversion."
        })
    elif any(k in lower_ind or k in lower_text for k in ["real estate", "property", "tenant", "housing", "apartments"]):
        product_matches.insert(0, {
            "product_name": "TenantEase (Cynbit Property Ecosystem SaaS)",
            "fit_score": 97,
            "rationale": "Digitizes tenant maintenance requests, automated viewing scheduling, and predictive lease management."
        })
    else:
        product_matches.append({
            "product_name": "Cynbit Studio & BitElevate Enterprise",
            "fit_score": 84,
            "rationale": "Provides architectural talent intelligence and custom enterprise workflow automation."
        })

    return {
        "executive_summary": (
            f"Live telemetry audit of {domain} ({industry}) reveals an overall Digital Maturity Score of {overall}/100 "
            f"(Technical SEO: {scores.get('technical_seo')}/100, Engineering: {scores.get('software_engineering')}/100, "
            f"Cloud Security: {scores.get('cloud_infrastructure')}/100, AI Readiness: {scores.get('ai_automation')}/100). "
            f"While the platform serves content in {latency}ms over {sec.get('server_banner')}, critical gaps in autonomous AI engagement, "
            f"structured schema markup, and edge security headers leave significant organic traffic and lead conversion on the table."
        ),
        "primary_bottlenecks": bottlenecks[:3],
        "recommended_ai_agents": [
            f"Autonomous Lead Discovery & Technical Qualification Agent embedded on {domain} primary CTAs",
            "RAG-Powered Knowledge & Support Copilot indexed on live product/service documentation",
            "Automated SEO Metadata, Alt-Text & JSON-LD Schema Generation Pipeline",
        ],
        "cynbit_product_matches": product_matches[:3],
        "lifecycle_roadmap": [
            {
                "stage_number": "01",
                "stage_name": "Discovery & Audit",
                "key_deliverables": [
                    f"Complete deep crawl of {domain} ({eng.get('total_dom_nodes')} DOM nodes analyzed on entry route)",
                    "Baseline Core Web Vitals, crawl budget, and conversion funnel drop-off telemetry",
                ],
                "timeline_weeks": "Week 1"
            },
            {
                "stage_number": "02",
                "stage_name": "Strategy & Blueprinting",
                "key_deliverables": [
                    "Design RAG vector architecture and structured JSON-LD schema specifications",
                    "Define Zero-Trust AWS/Azure CDN security header policies (CSP, HSTS, X-Frame-Options)",
                ],
                "timeline_weeks": "Week 2"
            },
            {
                "stage_number": "03",
                "stage_name": "High-Fidelity Design",
                "key_deliverables": [
                    "Prototype interactive AI Discovery Widget and high-converting landing UX flows",
                    "Design executive analytics dashboard for real-time lead & SEO attribution",
                ],
                "timeline_weeks": "Week 3"
            },
            {
                "stage_number": "04",
                "stage_name": "Technical Implementation",
                "key_deliverables": [
                    f"Refactor render-blocking scripts ({eng.get('script_count')} bundles) and inject automated SEO/alt-tag pipelines",
                    "Deploy custom LLM agent microservice with sub-second streaming inference",
                ],
                "timeline_weeks": "Weeks 4-6"
            },
            {
                "stage_number": "05",
                "stage_name": "Quality & Integrity Check",
                "key_deliverables": [
                    "Load-test AI agent concurrency (validated up to 50k+ users per Cynbit benchmark)",
                    "Verify 4/4 OWASP security headers and zero hallucination guardrails",
                ],
                "timeline_weeks": "Week 7"
            },
            {
                "stage_number": "06",
                "stage_name": "Deployment & Evolution",
                "key_deliverables": [
                    "Zero-downtime blue/green production launch with 99.9% uptime SLA monitoring",
                    "Continuous ROI telemetry tracking organic lead uplift and conversion velocity",
                ],
                "timeline_weeks": "Week 8 & Ongoing"
            },
        ],
        "roi_projections": [
            {
                "metric": "Organic Search Lead Velocity",
                "current_baseline": f"Technical SEO Score {scores.get('technical_seo')}/100 ({seo.get('json_ld_count')} schemas)",
                "projected_uplift": "+35% to +45% organic lead growth within 90 days (benchmarked on Marketing Addict case study)"
            },
            {
                "metric": "Visitor-to-Discovery Conversion Rate",
                "current_baseline": f"{ai.get('interactive_forms')} static HTML form(s), 24-48h manual reply",
                "projected_uplift": "2.8x–3.2x higher qualified pipeline via <30s autonomous AI discovery blueprints"
            },
            {
                "metric": "Page Response & Security Posture",
                "current_baseline": f"{latency}ms latency | {sec.get('security_headers_passed')}/4 security headers",
                "projected_uplift": "<350ms edge TTFB | 100% Zero-Trust header compliance & 99.9% uptime"
            },
        ],
    }
