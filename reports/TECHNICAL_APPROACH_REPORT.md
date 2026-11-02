# Technical Approach Report: Autonomous Phase-01 Discovery & Blueprint Engine

**Prepared by:** Akshat Dwivedi  
**Role Application:** AI/ML Engineer Intern — Cynbit Technologies  
**Date:** November 2026  

---

## 1. System Architecture & Data Pipeline

To eliminate hallucinations while delivering executive-grade consulting blueprints in under 30 seconds, the system uses a **Hybrid Neuro-Symbolic Architecture**:
1. **Deterministic Telemetry Extraction Layer (`src/auditor.py`):** Collects verifiable HTTP response metrics, security headers, and DOM structural signals.
2. **Rule-Based Scoring & Evidence Engine:** Computes reproducible 0–100 health scores across Cynbit's 4 mastery domains (*Technical SEO*, *Software Engineering*, *Cloud Infrastructure*, and *AI Automation*).
3. **Constrained LLM Blueprint Synthesizer (`src/ai_architect.py`):** Uses **Gemini 2.5 Flash** with strict **Pydantic JSON Schema enforcement** to synthesize findings into Cynbit's 6-Stage Architectural Lifecycle and match prospects to Cynbit's SaaS products (*Revio*, *TenantEase*, *Cynbit Studio*).

```
+-------------------------------------------------------------------------+
|                    USER / PROSPECT INPUT (Streamlit UI)                 |
|             Target URL (e.g., https://client.com) + Vertical            |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|        STAGE 1: LIVE TELEMETRY & DOM EXTRACTOR (src/auditor.py)         |
|  - HTTP Timing & Headers (TTFB Latency, HSTS, CSP, X-Frame-Options)     |
|  - DOM Inspection (BeautifulSoup4: Title, Meta, H1/H2, Canonical, Alt)  |
|  - Schema & Widget Detection (application/ld+json, Chat/AI SDKs)        |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|      STAGE 2: DETERMINISTIC SCORING & EVIDENCE ENGINE (0-100 Scale)     |
|  - Computes Domain Scores: SEO | Engineering | Cloud | AI Readiness     |
|  - Generates Ground-Truth Evidence Tuples (Issue, Evidence, Fix)        |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|      STAGE 3: STRUCTURED LLM ARCHITECT SYNTHESIS (src/ai_architect.py)  |
|  - Model: Gemini 2.5 Flash (response_schema=DiscoveryBlueprintReport)   |
|  - Fallback: Deterministic Telemetry Synthesizer (Zero-API-Key Mode)    |
|  - Maps to Cynbit 6-Stage Lifecycle + SaaS Product Matcher              |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|         STAGE 4: INTERACTIVE WORKBENCH & PROPOSAL EXPORT (app.py)       |
|  - 4-Domain Plotly Radar Chart, 6-Stage Roadmap Cards, Markdown Export  |
+-------------------------------------------------------------------------+
```

---

## 2. Model Selection & Justification

| Component | Selected Model / Technology | Why It Was Chosen Over Alternatives |
| :--- | :--- | :--- |
| **Primary Reasoning & Blueprint Synthesis** | **Google Gemini 2.5 Flash** (`google-genai` SDK) | **1. Sub-2s Latency:** Essential for an interactive web lead-magnet where prospects abandon pages after 10 seconds.<br>**2. Native Structured Outputs:** Supports strict `Pydantic` `response_schema` validation at the token-sampling level, guaranteeing 100% valid JSON.<br>**3. Cost Efficiency:** <$0.001 per audit, allowing Cynbit to run 10,000+ public lead audits/month for under $10. |
| **Fallback / Offline Synthesis** | **Deterministic Rule + Telemetry Engine** | Evaluators or prospects testing the repository without an API key still get a complete, telemetry-grounded blueprint with zero downtime. |
| **Phase-2 Enterprise Upgrade (Roadmap)** | **text-embedding-004 + Qdrant Vector DB** | Enables semantic retrieval over Cynbit's historical case studies (*Marketing Addict*, *Evento*, *Urban Wardrobe*) so the LLM cites the closest past client architecture. |

---

## 3. Prompt Engineering, Schema Enforcement & Guardrails

### 3.1 Grounded Context Injection (Anti-Hallucination)
Raw LLMs asked to *"audit a website URL"* frequently hallucinate metrics because they cannot inspect live HTTP headers or DOM trees directly. Our pipeline solves this by **never asking the LLM to guess site characteristics**:
- `WebTelemetryAuditor` first extracts exact quantitative evidence (`latency_ms`, `total_dom_nodes`, `json_ld_count`, `images_missing_alt`, `security_headers_passed`).
- The system prompt explicitly instructs the model: *"Always ground every finding in the provided telemetry metrics (cite exact latency, DOM node counts, missing headers, H1/meta counts, or missing JSON-LD schemas)."*

### 3.2 Strict Pydantic Output Contract
All LLM responses are constrained to the `DiscoveryBlueprintReport` Pydantic schema:
- `executive_summary: str`
- `primary_bottlenecks: List[str]`
- `recommended_ai_agents: List[str]`
- `cynbit_product_matches: List[CynbitProductMatch]` (with `fit_score: int` and `rationale: str`)
- `lifecycle_roadmap: List[LifecycleStagePlan]` (mapped to Stages `01` through `06`)
- `roi_projections: List[ROIEstimate]`

Temperature is locked at `0.2` to prioritize analytical consistency and factual grounding.

---

## 4. Production Execution Plan for Cynbit

To transition this PoC from a standalone Streamlit application into Cynbit's production infrastructure (`cynbit.in`):

1. **Microservice API Layer (Week 1):**
   - Wrap `WebTelemetryAuditor` and `generate_discovery_blueprint` in an asynchronous **FastAPI** service deployed on **AWS ECS Fargate** (or Azure Container Apps).
   - Add headless **Playwright** worker pool for client-side React/Next.js SPAs that require JavaScript hydration before DOM inspection.
2. **Caching & Rate Limiting (Week 2):**
   - Add **Redis** caching keyed by `(normalized_domain, date_bucket)` with a 24-hour TTL so repeated audits of the same prospect domain return in `<15ms` at zero LLM token cost.
   - Enforce IP and email-verified rate limiting (`5 free audits / hour / IP`) to prevent abuse.
3. **CRM & Lead Pipeline Integration (Week 3):**
   - Connect webhook outputs directly to Cynbit's internal CRM and Slack channels so whenever a prospect runs a discovery audit on `cynbit.in`, Cynbit's sales engineers receive the JSON blueprint and matched SaaS pitch (*Revio* / *TenantEase*) in real time.
4. **Observability & Evaluation (Week 4):**
   - Log all telemetry payloads, latency percentiles (`p50`, `p95`), and schema validation pass rates using OpenTelemetry + Langfuse.
