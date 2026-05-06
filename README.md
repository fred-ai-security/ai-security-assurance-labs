# 🔐 AI Security Assurance Labs — Engineering Portfolio

### By: Frederick Baffour

**AI Security Assurance • LLM Red Teaming • RAG Security • Model Supply-Chain Security**

> A hands-on portfolio demonstrating AI Security Assurance practices across the model lifecycle — from supply-chain validation through adversarial testing, RAG pipeline security, and governance-aligned reporting.

This repository contains practical, engineering-focused AI Security Assurance work. It demonstrates how I evaluate, test, and document AI models using real tools and repeatable workflows, across the full assurance lifecycle.

The labs here reflect how I approach AI model risk in real environments: verifying model provenance, validating artifacts, testing model behavior under adversarial conditions, assessing RAG pipeline security, and documenting findings clearly for security and engineering teams.

---

## 🧠 How to Read This Repository

This repository is intended for security engineers, AI engineers, and hiring managers evaluating applied AI Security Assurance capabilities.

Each section reflects operational enterprise security workflows rather than hypothetical or academic examples. Design choices emphasize clarity, reproducibility, and auditability. The repository is structured to mirror how AI Security Assurance work is performed in practice — from intake and supply-chain checks through red teaming, RAG pipeline assessment, and structured reporting.

Each folder represents a distinct security domain aligned to real enterprise security functions. Readers can explore in any order, but the recommended path is:

1. **Model Intake & Supply Chain Security** → `model-supply-chain/`
2. **Model Behavior & Red Teaming** → `red-teaming/`
3. **RAG Pipeline Security Assessment** → `red-teaming/rag/`
4. **Monitoring, Drift, and Runtime Risk** → `model-monitoring/`
5. **Governance, Versioning, and Auditability** → `model-governance/`

Each section is designed to stand alone while contributing to an end-to-end AI Security Assurance lifecycle.

---

# 🧭 What This Repository Demonstrates

This repository demonstrates an end-to-end AI Security Assurance lifecycle for assessing, validating, and governing AI systems.

### 1. **Model Supply-Chain Security**

* Trusted source verification
* SHA-256 integrity checks
* YARA static analysis
* ClamAV malware scanning
* SBOM generation (Syft / Grype)
* Provenance validation and documentation

### 2. **Security Toolchain Integrity**

* Binary signature validation using Sigcheck
* Verifying trusted sources of YARA, ClamAV, Sigcheck, and related tools
* Ensuring supply-chain trust for all security utilities

### 3. **LLM Red Teaming & Behavioral Evaluation**

* Garak automated LLM vulnerability testing
* Promptfoo adversarial evaluation
* Jailbreak and prompt injection analysis
* Toxicity, hallucination, and refusal-bypass detection
* Realistic adversarial scenarios and mitigations

### 4. **RAG Pipeline Security Assessment**

* End-to-end adversarial harness against a local Retrieval-Augmented Generation pipeline
* Four attack classes: Direct Prompt Injection, Retrieval Poisoning, Context Stuffing, Jailbreak via Retrieved Content
* Independent LLM-as-judge evaluation (target/judge separation pattern)
* Dual-verdict logic (keyword + LLM judge) with false-positive analysis
* Framework-mapped findings exported to structured Excel output
* Full engineering decision record in `DECISIONS.md`

### 5. **AI Risk & Model Safety**

* Risk classification and criticality tiering
* NIST AI RMF alignment (Govern / Map / Measure / Manage)
* MITRE ATLAS threat mapping
* ISO/IEC 42001 governance integration
* Documentation templates and audit-ready reporting

### 6. **End-to-End Assurance Lifecycle**

Covers the entire lifecycle:

**Stage 1 — Intake & Integrity** → **Stage 2 — Supply-Chain Assessment** → **Stage 3 — Red Teaming & Behavior Testing** → **Stage 4 — RAG Pipeline Assessment** → **Stage 5 — Reporting, Risk, & Governance**

This end-to-end structure mirrors real enterprise AI Security Assurance workflows.

---

# 📂 Repository Structure

```
ai-security-assurance-labs/
│
├── DEVELOPMENT_NOTES.md          ← Development methodology & disclosure
│
├── model-supply-chain/
│   ├── intake-pipeline-overview.md
│   ├── model-provenance-verification.md
│   ├── model-integrity-hashing.md
│   ├── sbom-generation-and-verification.md
│   ├── yara-scan-example.md
│   ├── clamav-scan-example.md
│   └── sigcheck-binary-verification.md
│
├── red-teaming/
│   ├── garak/
│   │   └── example-garak-assessment.md
│   ├── promptfoo/
│   │   └── example-redteam-config.yaml
│   ├── rag/                       ← RAG Pipeline Security Assessment
│   │   ├── README.md              ← Architecture, methodology, framework mapping
│   │   ├── DECISIONS.md           ← Engineering trade-offs and judgment record
│   │   └── scripts/
│   │       ├── rag_pipeline.py    ← Phase 1: HyDE-based RAG target
│   │       ├── run_all.py         ← Master attack orchestrator
│   │       ├── direct_injection.py
│   │       ├── retrieval_poisoning.py
│   │       ├── context_stuffing.py
│   │       ├── jailbreak_retrieval.py
│   │       ├── llm_judge.py       ← Independent LLM verdict module
│   │       └── findings_logger.py ← Structured Excel findings export
│   ├── llm-red-teaming-overview.md
│   └── model-safety-evaluation-framework.md
│
├── model-monitoring/
├── model-governance/
├── llm-operations/
└── static-analysis/
```

---

# 🚀 How to Navigate (Start Here)

## 👥 **For Recruiters / Non-Technical Reviewers**

Start with:

* `model-supply-chain/intake-pipeline-overview.md`
* `red-teaming/garak/example-garak-assessment.md`
* `DEVELOPMENT_NOTES.md`

These files show how AI models are evaluated end-to-end and how findings are documented.

---

## 🛡 **For Hiring Managers / Security Engineers**

Start with:

* `model-supply-chain/sbom-generation-and-verification.md`
* `red-teaming/garak/example-garak-assessment.md`
* `red-teaming/rag/README.md` — RAG adversarial harness architecture and methodology
* `red-teaming/rag/DECISIONS.md` — Engineering trade-offs and judgment record
* `red-teaming/rag/scripts/` — Running adversarial harness code

These demonstrate real hands-on engineering workflows with framework-mapped findings and structured outputs.

---

## 🔄 **For Full Lifecycle Understanding**

Review in sequence:

* `DEVELOPMENT_NOTES.md` — Methodology, engineering ownership, validation record
* `model-supply-chain/intake-pipeline-overview.md`
* `red-teaming/model-safety-evaluation-framework.md`
* `red-teaming/rag/README.md` + `DECISIONS.md`

This covers the full AI Security Assurance methodology from intake → red teaming → RAG assessment → governance.

---

# 🛠️ Tools & Technologies Demonstrated

This lab uses real tools from modern AI Security Assurance engineering:

* **Garak** — automated LLM vulnerability testing
* **Promptfoo** — structured adversarial evaluations
* **Microsoft PyRIT** — Python Risk Identification Toolkit for generative AI
* **YARA** — pattern-based static analysis
* **ClamAV** — malware signature scanning
* **Sigcheck** — binary signature verification
* **Syft / Grype** — SBOM and CVE scanning
* **LangChain** — RAG pipeline orchestration
* **ChromaDB** — vector store for retrieval testing
* **Ollama** — local model execution and testing
* **HuggingFace CLI** — trusted model intake

**Frameworks & Standards Referenced**

* NIST AI Risk Management Framework (AI RMF 1.0)
* MITRE ATLAS (Adversarial Threat Landscape for AI Systems)
* OWASP Top 10 for Large Language Model Applications (2025)
* ISO/IEC 42001:2023
* NIST SP 800-53 Rev. 5

---

# 🎯 Purpose of This Portfolio

This repository demonstrates my ability to:

* Perform **end-to-end AI Security Assurance** across the model lifecycle
* Translate technical findings into **governance controls and deployment recommendations**
* Design and execute **RAG pipeline adversarial assessments** with independent LLM-as-judge evaluation
* Conduct **LLM red teaming** with enterprise-grade tools and structured findings
* Evaluate **model safety, governance, and risk** with audit-ready output
* Document engineering decisions and trade-offs in **reproducible, defensible** formats

It reflects how I perform AI Security Assurance work in operational environments.

---

# 📬 Contact

**Frederick Baffour**  
AI Security Assurance Engineer  
LinkedIn: [linkedin.com/in/frederick-baffour](https://www.linkedin.com/in/frederick-baffour)  
GitHub: [github.com/fred-ai-security](https://github.com/fred-ai-security)  
Email: fbaffour@gmail.com  

*Last updated: 2026*

> Note: This repository is a personal AI Security Assurance lab and engineering portfolio. Artifacts are intentionally scoped for public demonstration and do not include proprietary client data, private prompt libraries, or production system configurations.
