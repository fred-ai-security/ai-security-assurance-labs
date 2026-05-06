# 📋 Development Methodology & Engineering Notes

### Frederick Baffour — AI Security Assurance Engineer

---

# About This Repository

This repository documents the AI Security Assurance methodology, adversarial testing workflows, RAG security assessments, governance framework alignments, and lifecycle engineering I have built and refined through hands-on lab execution.

The focus is practical AI assurance engineering: adversarial testing, RAG security evaluation, agentic AI security assessment, model supply-chain integrity, standards-aligned assessment design, and risk-oriented methodology. The work reflects iterative engineering, hands-on troubleshooting, framework-aligned assessment design, and continuous refinement across a six-stage AI assurance lifecycle.

---

# Development Methodology

I use AI-assisted development tools as part of my engineering workflow for prototyping, scripting, documentation acceleration, and iterative refinement. 

All architectural decisions, testing methodology, framework mappings, execution, troubleshooting, validation, operational tuning, and final implementation decisions are my own.

I personally executed the assessments, validated outputs, corrected failures, refined workflows, tuned configurations, interpreted findings, and iteratively improved the lifecycle based on real lab results.

---

# Engineering & Architecture Decisions

The decisions documented throughout this repository are grounded in practical AI assurance and adversarial testing objectives. Representative examples:

- Designed a six-stage AI Security Assurance Lifecycle spanning intake, supply-chain validation, red teaming, RAG pipeline testing, agentic security evaluation, and consolidated reporting
- Separated target and judge models within the RAG adversarial harness to ensure evaluation independence — a model cannot reliably evaluate its own output, and the architecture reflects that constraint
- Selected locally hosted models to maintain chain-of-custody over assessment data, prompts, and findings throughout testing
- Implemented dual-verdict logic (keyword matching + LLM judge) after confirming empirically that keyword-only detection produced unacceptable false-positive rates across both directions
- Mapped all findings and attack classes to OWASP LLM Top 10 (2025), MITRE ATLAS, NIST AI RMF, and ISO/IEC 42001 to produce audit-ready, control-mapped output
- Structured findings around severity-driven deployment recommendations — CONDITIONAL HOLD is a real outcome generated from a Critical-scored prompt injection finding, not a hypothetical
- Built reproducible local testing workflows using Ollama, LangChain, ChromaDB, Garak, Promptfoo, PyRIT, Syft, and Grype

---

# Validation & Assessment Results

The workflows in this repository were tested and refined through repeated execution cycles on local lab hardware. Testing included troubleshooting runtime failures, resolving dependency conflicts, tuning model configurations, validating assessment outputs, and correcting workflow inconsistencies discovered during execution.

Specific issues encountered and resolved during development include VRAM limitations during concurrent model execution, ChromaDB locking behavior under parallel test loads, LangChain deprecation conflicts, serialization and encoding failures, workflow orchestration inconsistencies, retrieval contamination edge cases, and false-positive detection calibration.

A complete end-to-end lifecycle execution produced the following assessment outcomes against a baseline target model:

- **Tier 1 — Base Model Red Teaming:** PASS (1,280 Garak probes, 0 failures; PyRIT 1 failure; Promptfoo 3 failures)
- **Tier 2 — RAG Pipeline Assessment:** HOLD (18 tests: 10 EXPLOITABLE, 7 MITIGATED, 1 PARTIAL — prompt firewall required)
- **Tier 3 — Agentic AI Assessment:** PASS (10 scenarios, 0 failures, 100% deflection rate)
- **Overall Deployment Recommendation:** CONDITIONAL HOLD, driven by the RAG layer

These results reflect actual assessment execution, not simulated or theoretical outputs.

---

# What Is Intentionally Not Published

Certain materials are intentionally excluded from this public repository. These include the full adversarial prompt libraries, complete findings inventories, operational attack sequences, full Promptfoo harnesses, and proprietary testing depth used for engagement work.

The purpose of this repository is to demonstrate methodology, engineering capability, workflow design, and assessment structure. Operational depth stays private — the same way a penetration testing firm publishes methodology but not its exploit inventory.

---

# Frameworks & Tooling

**Frameworks referenced:**
- NIST AI Risk Management Framework (AI RMF 1.0)
- MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)
- OWASP Top 10 for Large Language Model Applications (2025 edition)
- ISO/IEC 42001:2023 — AI Management Systems
- NIST SP 800-53 Rev. 5

**Open-source tools used:**
- Garak, Promptfoo, Microsoft PyRIT — adversarial testing
- Syft, Grype — supply-chain and CVE scanning
- LangChain, ChromaDB, Ollama — RAG pipeline and local inference
- YARA, ClamAV — static analysis

All frameworks are public standards. No proprietary methodologies belonging to other organizations are reproduced here.

---

# Lab Environment

Assessment work documented here was executed in a controlled local lab environment. Representative models and components used across lifecycle stages include Mistral 7B, Llama 3.1 8B Instruct, GPT-OSS 20B, and nomic-embed-text, hosted via Ollama on a local Ubuntu / WSL2 environment with an NVIDIA RTX 4050 GPU. Model selection across stages was driven by assessment objective, hardware constraints, and evaluation architecture requirements.

I use local execution workflows throughout the lifecycle to maintain control over assessment data, prompts, findings, and model interactions during testing.

---

# Contact

**Frederick Baffour**
AI Security Assurance Engineer
GitHub: https://github.com/fred-ai-security
LinkedIn: https://www.linkedin.com/in/frederick-baffour
Email: fbaffour@gmail.com

---

*Applies to all content in this repository unless otherwise noted.*
