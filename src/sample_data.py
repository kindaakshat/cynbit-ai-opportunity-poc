"""
Pre-loaded Realistic Benchmark Datasets for Cynbit Showcase & Client Archetypes.
Guarantees zero-setup 1-click evaluation even offline or without API keys.
"""
from typing import Dict, Any

SAMPLE_PROFILES: Dict[str, Dict[str, Any]] = {
    "cynbit.in (Cynbit Technologies Official Site)": {
        "industry": "AI Automation & Enterprise Software Agency",
        "telemetry": {
            "url": "https://www.cynbit.in/",
            "domain": "www.cynbit.in",
            "status_code": 200,
            "latency_ms": 310.4,
            "page_size_kb": 148.2,
            "seo": {
                "title": "Cynbit Technologies | AI Automation & Software Solutions Jaipur",
                "title_length": 63,
                "meta_description": "Cynbit Technologies architects the digital future with autonomous AI agents, custom software development, and scalable business platforms in Jaipur, India.",
                "meta_description_length": 155,
                "h1_count": 1,
                "h1_samples": ["Architecting the future with Software dev."],
                "h2_count": 6,
                "h2_samples": ["Foundational pillars.", "BitElevate.", "The speed of a startup.", "Architectural mastery across four domains.", "How we construct digital success."],
                "has_canonical": True,
                "og_tag_count": 5,
                "json_ld_count": 1,
                "total_images": 14,
                "images_missing_alt": 2,
            },
            "engineering": {
                "total_dom_nodes": 640,
                "script_count": 11,
                "stylesheet_count": 4,
                "has_mobile_viewport": True,
                "form_count": 2,
                "button_count": 9,
            },
            "cloud_security": {
                "is_https": True,
                "security_headers": {
                    "Strict-Transport-Security": True,
                    "Content-Security-Policy": False,
                    "X-Frame-Options": True,
                    "X-Content-Type-Options": True,
                },
                "security_headers_passed": 3,
                "server_banner": "Vercel / Edge Network",
            },
            "ai_readiness": {
                "has_ai_chat_widget": False,
                "detected_widgets": [],
                "interactive_forms": 2,
                "has_structured_knowledge_schema": True,
            },
            "text_excerpt": (
                "Cynbit Technologies: Leading AI Automation and Software Solutions Company in Jaipur, India. "
                "Cynbit Technologies architects the digital future with autonomous AI agents, custom software development, "
                "and scalable business platforms. Proprietary SaaS suite: Cynbit Studio (Career intelligence), "
                "Revio (AI Review Assistant), TenantEase (Property ecosystem). BitElevate training program."
            ),
            "scores": {
                "overall": 82,
                "technical_seo": 92,
                "software_engineering": 90,
                "cloud_infrastructure": 85,
                "ai_automation": 60,
            },
            "deterministic_findings": [
                {
                    "domain": "AI Automation",
                    "severity": "High",
                    "issue": "Static 'Start Discovery' Funnel Without Live Interactive AI Audit Agent",
                    "evidence": "0 conversational or autonomous diagnostic widgets detected on landing page; relies on static newsletter/contact forms.",
                    "fix": "Embed the Cynbit Autonomous Phase-01 Discovery Agent directly into the 'Start Discovery' CTA to convert visitors with instant technical blueprints."
                },
                {
                    "domain": "Cloud Infrastructure",
                    "severity": "Medium",
                    "issue": "Missing Strict Content-Security-Policy (CSP) Header",
                    "evidence": "HSTS, X-Frame-Options, and X-Content-Type-Options are active, but Content-Security-Policy is unset.",
                    "fix": "Add a nonce-based Content-Security-Policy header at the edge proxy to achieve 100% Zero-Trust browser hardening."
                },
                {
                    "domain": "Technical SEO & Accessibility",
                    "severity": "Low",
                    "issue": "2 Decorative/Icon Images Missing Explicit Alt Attributes",
                    "evidence": "2 of 14 <img> elements lack descriptive alt attributes.",
                    "fix": "Add descriptive alt text or aria-hidden='true' for decorative UI icons."
                }
            ]
        }
    },
    "urbanwardrobe-retail.example.com (Global Retail E-Commerce Prospect)": {
        "industry": "D2C Fashion & Global E-Commerce Retail",
        "telemetry": {
            "url": "https://urbanwardrobe-retail.example.com",
            "domain": "urbanwardrobe-retail.example.com",
            "status_code": 200,
            "latency_ms": 1480.0,
            "page_size_kb": 412.6,
            "seo": {
                "title": "Home - Urban Wardrobe",
                "title_length": 21,
                "meta_description": "",
                "meta_description_length": 0,
                "h1_count": 3,
                "h1_samples": ["Summer Sale Live!", "New Arrivals", "Trending Styles"],
                "h2_count": 12,
                "h2_samples": ["Men's Collection", "Women's Collection", "Customer Reviews"],
                "has_canonical": False,
                "og_tag_count": 1,
                "json_ld_count": 0,
                "total_images": 48,
                "images_missing_alt": 29,
            },
            "engineering": {
                "total_dom_nodes": 2340,
                "script_count": 31,
                "stylesheet_count": 9,
                "has_mobile_viewport": True,
                "form_count": 1,
                "button_count": 24,
            },
            "cloud_security": {
                "is_https": True,
                "security_headers": {
                    "Strict-Transport-Security": False,
                    "Content-Security-Policy": False,
                    "X-Frame-Options": True,
                    "X-Content-Type-Options": False,
                },
                "security_headers_passed": 1,
                "server_banner": "nginx/1.18.0",
            },
            "ai_readiness": {
                "has_ai_chat_widget": False,
                "detected_widgets": [],
                "interactive_forms": 1,
                "has_structured_knowledge_schema": False,
            },
            "text_excerpt": (
                "Urban Wardrobe Global Retail. Shop premium streetwear, seasonal collections, and accessories. "
                "Free shipping on orders over $75. Read 1,200+ customer reviews on sizing, fabric quality, and delivery speed."
            ),
            "scores": {
                "overall": 47,
                "technical_seo": 42,
                "software_engineering": 47,
                "cloud_infrastructure": 50,
                "ai_automation": 50,
            },
            "deterministic_findings": [
                {
                    "domain": "Technical SEO",
                    "severity": "High",
                    "issue": "Missing Meta Description, Canonical Tag & Product JSON-LD Schema",
                    "evidence": "0 meta description chars, no canonical link, 0 Product/AggregateRating JSON-LD blocks, 29/48 images missing alt text.",
                    "fix": "Implement automated SEO tag templates and Product + AggregateRating schema to capture Google Shopping rich snippets."
                },
                {
                    "domain": "AI Automation & SaaS Fit (Revio)",
                    "severity": "High",
                    "issue": "Unstructured Customer Reviews & No AI Shopping/Support Assistant",
                    "evidence": "1,200+ static reviews without sentiment synthesis or automated sizing/order-tracking assistant.",
                    "fix": "Integrate Cynbit's 'Revio' AI Review Assistant for automated review sentiment intelligence and deploy an autonomous sizing/order RAG agent."
                },
                {
                    "domain": "Software Engineering & Cloud",
                    "severity": "High",
                    "issue": "High TTFB Latency (1,480ms), Heavy DOM (2,340 nodes) & Legacy Single-Node Nginx",
                    "evidence": "31 render scripts, 1,480ms response latency, missing HSTS and CSP headers on nginx/1.18.0.",
                    "fix": "Migrate to AWS/Azure auto-scaling container architecture with CloudFront CDN edge caching and Zero-Trust security headers."
                }
            ]
        }
    },
    "skyline-estates.example.com (Real Estate & Property Portal Prospect)": {
        "industry": "Real Estate & Multi-Family Property Management",
        "telemetry": {
            "url": "https://skyline-estates.example.com",
            "domain": "skyline-estates.example.com",
            "status_code": 200,
            "latency_ms": 960.2,
            "page_size_kb": 275.0,
            "seo": {
                "title": "Skyline Estates | Residential & Commercial Properties",
                "title_length": 53,
                "meta_description": "Explore residential apartments, commercial offices, and rental properties managed by Skyline Estates.",
                "meta_description_length": 101,
                "h1_count": 2,
                "h1_samples": ["Find Your Next Property", "Tenant Portal Login"],
                "h2_count": 8,
                "h2_samples": ["Featured Listings", "Submit Maintenance Request", "Book a Viewing"],
                "has_canonical": True,
                "og_tag_count": 2,
                "json_ld_count": 0,
                "total_images": 32,
                "images_missing_alt": 14,
            },
            "engineering": {
                "total_dom_nodes": 1420,
                "script_count": 22,
                "stylesheet_count": 6,
                "has_mobile_viewport": True,
                "form_count": 3,
                "button_count": 15,
            },
            "cloud_security": {
                "is_https": True,
                "security_headers": {
                    "Strict-Transport-Security": True,
                    "Content-Security-Policy": False,
                    "X-Frame-Options": False,
                    "X-Content-Type-Options": True,
                },
                "security_headers_passed": 2,
                "server_banner": "Apache",
            },
            "ai_readiness": {
                "has_ai_chat_widget": False,
                "detected_widgets": [],
                "interactive_forms": 3,
                "has_structured_knowledge_schema": False,
            },
            "text_excerpt": (
                "Skyline Estates manages 450+ residential and commercial units. Tenants can submit maintenance requests "
                "via our contact form. Prospective renters can request viewing appointments manually."
            ),
            "scores": {
                "overall": 59,
                "technical_seo": 66,
                "software_engineering": 60,
                "cloud_infrastructure": 60,
                "ai_automation": 50,
            },
            "deterministic_findings": [
                {
                    "domain": "AI Automation & SaaS Fit (TenantEase)",
                    "severity": "High",
                    "issue": "Manual Maintenance Request Forms & Static Viewing Scheduling",
                    "evidence": "Relies on 3 static HTML forms for tenant maintenance and property viewings with 0 automated triage.",
                    "fix": "Onboard onto Cynbit's 'TenantEase' Property Ecosystem with AI maintenance ticket triage and automated lease/viewing workflows."
                },
                {
                    "domain": "Technical SEO",
                    "severity": "Medium",
                    "issue": "Missing RealEstateListing JSON-LD Schema & 14 Unlabeled Property Images",
                    "evidence": "0 JSON-LD blocks; 14/32 listing photos lack alt attributes.",
                    "fix": "Inject RealEstateListing structured schema and automated vision-based alt tags for property galleries."
                }
            ]
        }
    }
}
