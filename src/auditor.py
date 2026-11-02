"""
Live Web Telemetry Extractor & Deterministic Technical Scoring Engine
for Cynbit Phase-01 Discovery & Audit Automation.
"""
import re
import time
from urllib.parse import urlparse
from typing import Dict, Any, List
import requests
from bs4 import BeautifulSoup


class WebTelemetryAuditor:
    """Scrapes and evaluates a target URL across Cynbit's 4 core mastery domains."""

    DEFAULT_HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/128.0.0.0 Safari/537.36 CynbitAuditBot/1.0"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    def __init__(self, timeout: int = 12):
        self.timeout = timeout

    @staticmethod
    def normalize_url(url: str) -> str:
        url = url.strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url

    def extract_telemetry(self, url: str) -> Dict[str, Any]:
        """Performs live HTTP & DOM inspection and computes deterministic domain scores."""
        norm_url = self.normalize_url(url)
        parsed = urlparse(norm_url)
        domain = parsed.netloc or norm_url

        start_ts = time.perf_counter()
        response = requests.get(
            norm_url,
            headers=self.DEFAULT_HEADERS,
            timeout=self.timeout,
            allow_redirects=True,
        )
        latency_ms = round((time.perf_counter() - start_ts) * 1000, 1)

        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        headers = {k.lower(): v for k, v in response.headers.items()}

        # 1. Technical SEO Signals
        title_tag = soup.find("title")
        title_text = title_tag.get_text(strip=True) if title_tag else ""

        meta_desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
        meta_desc = meta_desc_tag.get("content", "").strip() if meta_desc_tag else ""

        canonical_tag = soup.find("link", attrs={"rel": re.compile(r"canonical", re.I)})
        has_canonical = bool(canonical_tag and canonical_tag.get("href"))

        og_tags = soup.find_all("meta", attrs={"property": re.compile(r"^og:", re.I)})
        json_ld_scripts = soup.find_all("script", attrs={"type": "application/ld+json"})

        h1_tags = [h.get_text(strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)]
        h2_tags = [h.get_text(strip=True) for h in soup.find_all("h2") if h.get_text(strip=True)]

        images = soup.find_all("img")
        total_images = len(images)
        images_missing_alt = sum(1 for img in images if not img.get("alt", "").strip())

        # 2. Software Engineering & DOM Signals
        scripts = soup.find_all("script")
        stylesheets = soup.find_all("link", attrs={"rel": re.compile(r"stylesheet", re.I)})
        forms = soup.find_all("form")
        buttons = soup.find_all("button")
        total_dom_nodes = len(soup.find_all(True))
        page_size_kb = round(len(response.content) / 1024, 1)

        viewport_tag = soup.find("meta", attrs={"name": re.compile(r"^viewport$", re.I)})
        has_viewport = bool(viewport_tag)

        # 3. Cloud Infrastructure & Zero-Trust Security Signals
        is_https = response.url.startswith("https://")
        security_headers = {
            "Strict-Transport-Security": "strict-transport-security" in headers,
            "Content-Security-Policy": "content-security-policy" in headers,
            "X-Frame-Options": "x-frame-options" in headers,
            "X-Content-Type-Options": "x-content-type-options" in headers,
        }
        server_banner = headers.get("server", "Undisclosed / Custom Edge")

        # 4. AI Automation & Conversion Signals
        lower_html = html.lower()
        chat_widget_keywords = [
            "intercom", "drift", "tawk.to", "crisp.chat", "zendesk",
            "chatbot", "hubspot", "freshchat", "voiceflow", "botpress"
        ]
        detected_chat_widgets = [kw for kw in chat_widget_keywords if kw in lower_html]
        has_ai_assistant = len(detected_chat_widgets) > 0

        # Extract visible text summary for LLM grounding
        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()
        visible_text = " ".join(soup.get_text(separator=" ", strip=True).split())
        text_excerpt = visible_text[:2800]

        telemetry = {
            "url": response.url,
            "domain": domain,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "page_size_kb": page_size_kb,
            "seo": {
                "title": title_text,
                "title_length": len(title_text),
                "meta_description": meta_desc,
                "meta_description_length": len(meta_desc),
                "h1_count": len(h1_tags),
                "h1_samples": h1_tags[:3],
                "h2_count": len(h2_tags),
                "h2_samples": h2_tags[:5],
                "has_canonical": has_canonical,
                "og_tag_count": len(og_tags),
                "json_ld_count": len(json_ld_scripts),
                "total_images": total_images,
                "images_missing_alt": images_missing_alt,
            },
            "engineering": {
                "total_dom_nodes": total_dom_nodes,
                "script_count": len(scripts),
                "stylesheet_count": len(stylesheets),
                "has_mobile_viewport": has_viewport,
                "form_count": len(forms),
                "button_count": len(buttons),
            },
            "cloud_security": {
                "is_https": is_https,
                "security_headers": security_headers,
                "security_headers_passed": sum(security_headers.values()),
                "server_banner": server_banner,
            },
            "ai_readiness": {
                "has_ai_chat_widget": has_ai_assistant,
                "detected_widgets": detected_chat_widgets,
                "interactive_forms": len(forms),
                "has_structured_knowledge_schema": len(json_ld_scripts) > 0,
            },
            "text_excerpt": text_excerpt,
        }

        telemetry["scores"] = self.compute_domain_scores(telemetry)
        telemetry["deterministic_findings"] = self.generate_deterministic_findings(telemetry)
        return telemetry

    @staticmethod
    def compute_domain_scores(t: Dict[str, Any]) -> Dict[str, int]:
        """Calculates 0-100 health scores across Cynbit's 4 architectural domains."""
        # 1. Technical SEO Score
        seo = t["seo"]
        seo_score = 40
        if 15 <= seo["title_length"] <= 70:
            seo_score += 15
        elif seo["title_length"] > 0:
            seo_score += 8
        if 70 <= seo["meta_description_length"] <= 170:
            seo_score += 15
        elif seo["meta_description_length"] > 0:
            seo_score += 7
        if seo["h1_count"] == 1:
            seo_score += 10
        elif seo["h1_count"] > 1:
            seo_score += 4
        if seo["has_canonical"]:
            seo_score += 8
        if seo["og_tag_count"] >= 3:
            seo_score += 6
        if seo["json_ld_count"] >= 1:
            seo_score += 6
        if seo["total_images"] > 0 and (seo["images_missing_alt"] / seo["total_images"]) > 0.3:
            seo_score -= 10
        seo_score = max(15, min(100, seo_score))

        # 2. Software Engineering Score
        eng = t["engineering"]
        eng_score = 55
        if eng["has_mobile_viewport"]:
            eng_score += 15
        if t["latency_ms"] < 600:
            eng_score += 15
        elif t["latency_ms"] < 1400:
            eng_score += 8
        else:
            eng_score -= 10
        if eng["total_dom_nodes"] < 900:
            eng_score += 10
        elif eng["total_dom_nodes"] > 2000:
            eng_score -= 10
        if eng["script_count"] <= 20:
            eng_score += 5
        else:
            eng_score -= 8
        eng_score = max(20, min(100, eng_score))

        # 3. Cloud Infrastructure & Zero-Trust Security Score
        sec = t["cloud_security"]
        cloud_score = 35
        if sec["is_https"]:
            cloud_score += 25
        cloud_score += sec["security_headers_passed"] * 10
        cloud_score = max(15, min(100, cloud_score))

        # 4. AI Automation Readiness Score
        ai = t["ai_readiness"]
        ai_score = 35
        if ai["has_ai_chat_widget"]:
            ai_score += 30
        if ai["has_structured_knowledge_schema"]:
            ai_score += 20
        if ai["interactive_forms"] > 0:
            ai_score += 15
        ai_score = max(20, min(100, ai_score))

        overall = round((seo_score + eng_score + cloud_score + ai_score) / 4)
        return {
            "overall": overall,
            "technical_seo": seo_score,
            "software_engineering": eng_score,
            "cloud_infrastructure": cloud_score,
            "ai_automation": ai_score,
        }

    @staticmethod
    def generate_deterministic_findings(t: Dict[str, Any]) -> List[Dict[str, str]]:
        """Produces rule-based technical findings grounded in HTTP/DOM evidence."""
        findings = []
        seo = t["seo"]
        sec = t["cloud_security"]
        eng = t["engineering"]
        ai = t["ai_readiness"]

        if seo["meta_description_length"] == 0:
            findings.append({
                "domain": "Technical SEO",
                "severity": "High",
                "issue": "Missing Meta Description Tag",
                "evidence": "meta[name='description'] length is 0 chars.",
                "fix": "Inject dynamic, keyword-targeted meta descriptions (120-160 chars) across all route templates."
            })
        if seo["json_ld_count"] == 0:
            findings.append({
                "domain": "Technical SEO & AI Readiness",
                "severity": "High",
                "issue": "No JSON-LD Structured Data Schema Detected",
                "evidence": "0 <script type='application/ld+json'> blocks found in DOM.",
                "fix": "Deploy Organization, Product/Service, and FAQPage JSON-LD schemas to boost rich-snippet CTR and AI search indexing."
            })
        if seo["h1_count"] != 1:
            findings.append({
                "domain": "Technical SEO",
                "severity": "Medium",
                "issue": f"Suboptimal H1 Heading Hierarchy ({seo['h1_count']} H1 tags found)",
                "evidence": f"Detected {seo['h1_count']} H1 elements instead of a single semantic primary heading.",
                "fix": "Enforce a strict single-H1 semantic hierarchy per view to improve search crawler topical clarity."
            })
        if seo["images_missing_alt"] > 0:
            findings.append({
                "domain": "Technical SEO & Accessibility",
                "severity": "Medium",
                "issue": f"{seo['images_missing_alt']} of {seo['total_images']} Images Missing Alt Attributes",
                "evidence": f"{seo['images_missing_alt']} <img> elements lack descriptive alt text.",
                "fix": "Automate alt-tag generation using a vision-language captioning pipeline in the CMS."
            })
        if sec["security_headers_passed"] < 3:
            missing_hdrs = [k for k, v in sec["security_headers"].items() if not v]
            findings.append({
                "domain": "Cloud Infrastructure",
                "severity": "High",
                "issue": "Incomplete Zero-Trust HTTP Security Headers",
                "evidence": f"Missing headers: {', '.join(missing_hdrs)}.",
                "fix": "Configure AWS CloudFront / Azure Front Door edge policies to enforce HSTS, CSP, and X-Frame-Options."
            })
        if not ai["has_ai_chat_widget"]:
            findings.append({
                "domain": "AI Automation",
                "severity": "High",
                "issue": "No Autonomous Conversational or Lead-Qualification Agent Detected",
                "evidence": f"0 conversational AI widgets detected; relies on {ai['interactive_forms']} static HTML form(s).",
                "fix": "Deploy a custom RAG-powered Cynbit Autonomous Agent for 24/7 instant discovery, lead qualification, and booking."
            })
        if eng["script_count"] > 20 or t["latency_ms"] > 900:
            findings.append({
                "domain": "Software Engineering",
                "severity": "Medium",
                "issue": "JavaScript Bundle & TTFB Latency Optimization Opportunity",
                "evidence": f"{eng['script_count']} <script> tags loaded; initial response latency {t['latency_ms']} ms.",
                "fix": "Defer non-critical third-party scripts, implement code-splitting, and cache static assets at the CDN edge."
            })

        return findings
