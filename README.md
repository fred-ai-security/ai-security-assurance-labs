# 🔐 AI Security Assurance Labs — Engineering Portfolio & Research Notebook

### By: Frederick Baffour

**AI Security Assurance • LLM Red Teaming • Model Supply-Chain Security**

> A hands-on portfolio demonstrating AI Security Assurance practices across the model lifecycle.

This repository contains practical, engineering-focused AI Security Assurance work. It demonstrates how I evaluate, test, and document AI models using real tools and repeatable workflows, rather than theoretical examples.

The labs here reflect how I approach AI model risk in real environments: verifying model provenance, validating artifacts, testing model behavior under adversarial conditions, and documenting findings clearly for security and engineering teams.

The goal of this work is to show hands-on AI Security Assurance evaluation across the model lifecycle, from intake and supply-chain checks through red-teaming, RAG pipeline security, agentic AI assessment, behavioral analysis, and structured reporting.

---

## 🧠 How to Read This Repository

This repository is intended for security engineers, AI engineers, and hiring managers evaluating applied AI Security Assurance capabilities in real-world environments.

Artifacts are structured for clarity and reproducibility while reflecting real-world AI security assurance workflows and assessment patterns.

Each section reflects common enterprise security workflows rather than hypothetical or academic examples.

Design choices emphasize clarity, reproducibility, and auditability over production optimization.

This repository is structured to mirror how AI Security Assurance work is performed in practice.

Each folder represents a distinct security domain aligned to real enterprise security functions.

Readers can explore in any order, but a recommended path is:

1. **Model Intake & Supply Chain Security**
   → `model-supply-chain/`
2. **Model Behavior & Red Teaming**
   → `red-teaming/`
3. **Monitoring, Drift, and Runtime Risk**
   → `model-monitoring/`
4. **Governance, Versioning, and Auditability**
   → `model-governance/`
5. **LLM Operations & Inference Pipelines**
   → `llm-operations/`

Each section is designed to stand alone while contributing to an end-to-end AI Security Assurance lifecycle.

---

# 🧭 What This Repository Demonstrates

This repository demonstrates an end-to-end AI Security Assurance lifecycle for assessing, validating, and governing AI systems.

### 1. **Model Supply-Chain Security**

- Trusted source verification
- SHA-256 integrity checks
- YARA static analysis
- ClamAV malware scanning
- SBOM generation (Syft / Grype)
- Provenance validation and documentation

### 2. **Security Toolchain Integrity**

- Binary signature validation using Sigcheck
- Verifying trusted sources of YARA, ClamAV, Sigcheck, and related tools
- Ensuring supply-chain trust for all security utilities

### 3. **LLM Red Teaming & Behavioral Evaluation**

- Garak automated LLM vulnerability testing (1,280 probes across 10 attack classes)
- Promptfoo adversarial evaluation with LLM-rubric assertions
- Jailbreak and prompt injection analysis
- Toxicity, hallucination, and refusal-bypass detection
- Dual-verdict evaluation logic (keyword matching + LLM judge)
- Realistic adversarial scenarios and structured mitigations

### 4. **RAG Pipeline Security Assessment**

- Retrieval poisoning and context manipulation testing
- Prompt injection via retrieved documents
- Jailbreak-through-retrieval attack scenarios
- 18-test adversarial harness with EXPLOITABLE / MITIGATED / PARTIAL verdicts
- LLM judge evaluation with confidence scoring
- Findings mapped to OWASP LLM Top 10 (2025) and MITRE ATLAS

### 5. **Agentic AI Security Assessment**

- ReAct agent attack harness covering 8 attack classes
- Tool call injection, goal hijacking, privilege escalation, and indirect injection scenarios
- 10-scenario evaluation with 100% deflection rate documented
- FastMCP server integration for agent tool security testing
- Findings mapped to MITRE ATLAS, OWASP LLM Top 10 (2025), and NIST AI RMF

### 6. **AI Risk & Model Safety Governance**

- Risk classification and criticality tiering
- NIST AI RMF alignment (Govern / Map / Measure / Manage)
- MITRE ATLAS threat mapping
- ISO/IEC 42001 governance integration
- Documentation templates and audit-ready reporting
- Severity-driven deployment recommendations (including CONDITIONAL HOLD outcomes)

### 7. **End-to-End Intake Pipeline**

Covers the entire lifecycle:

**Stage 1 — Intake & Integrity**
→ **Stage 2 — Supply-Chain Assessment**
→ **Stage 3 — Red Teaming & Behavior Testing**
→ **Stage 4 — RAG Pipeline Security**
→ **Stage 5 — Agentic AI Security**
→ **Stage 6 — Reporting, Risk, & Governance**

This end-to-end structure mirrors real enterprise AI Security Assurance workflows.

---

# 📂 Repository Structure

```
ai-security-assurance-labs/
│
├── model-supply-chain/         # Supply-chain integrity, SBOM, provenance
├── red-teaming/                # Garak, PyRIT, Promptfoo adversarial testing
│   ├── garak/
│   ├── promptfoo/
│   └── rag/                    # RAG pipeline adversarial harness
├── model-monitoring/           # Drift detection, runtime risk monitoring
├── model-governance/           # Risk classification, versioning, auditability
├── llm-operations/             # Inference pipelines, LLM operations
├── static-analysis/            # YARA, ClamAV, binary scanning
├── docs/                       # Lab setup and prerequisites
│   └── lab-setup.md
├── DEVELOPMENT_NOTES.md        # Engineering methodology and AI disclosure
├── LICENSE
└── README.md
```

---

# 🚀 How to Navigate (Start Here)

## 👥 **For Recruiters / Non-Technical Reviewers**

Start with:

- `model-supply-chain/` — how AI models are verified before use
- `red-teaming/garak/` — automated adversarial testing results
- `DEVELOPMENT_NOTES.md` — methodology and engineering decisions

These files show how AI models are evaluated end-to-end and how findings are documented.

---

## 🛡 **For Hiring Managers / Security Engineers**

Start with:

- `model-supply-chain/` — SBOM generation, provenance validation, integrity hashing
- `red-teaming/` — Garak, PyRIT, and Promptfoo adversarial harnesses
- `red-teaming/rag/` — RAG pipeline security assessment and LLM judge architecture
- `docs/lab-setup.md` — environment configuration, accepted risks, model selection rationale

These demonstrate real hands-on engineering workflows.

---

## 🔄 **For Full Lifecycle Understanding**

Review in order:

1. `model-supply-chain/` — intake and supply-chain validation
2. `red-teaming/` — base model adversarial testing
3. `red-teaming/rag/` — RAG pipeline security
4. `model-monitoring/` — drift and runtime risk
5. `model-governance/` — risk classification and governance alignment
6. `DEVELOPMENT_NOTES.md` — assessment outcomes and methodology

This shows the full AI Security Assurance lifecycle from intake through governance.

---

# 🛠️ Tools & Technologies Demonstrated

This lab uses real tools from modern AI Security Assurance engineering, including:

- **Garak** — automated LLM vulnerability testing
- **Promptfoo** — structured adversarial evaluations with LLM-rubric assertions
- **Microsoft PyRIT** — red team orchestration and jailbreak scenarios
- **YARA** — pattern-based static analysis
- **ClamAV** — malware signature scanning
- **Sigcheck** — binary signature verification
- **Syft / Grype** — SBOM generation and CVE scanning
- **SHA-256 hashing** — integrity verification
- **Ollama** — local model execution and testing
- **LangChain / ChromaDB** — RAG pipeline and vector store
- **FastMCP** — agent tool server for agentic security testing

**Frameworks & Standards**

- NIST AI RMF
- MITRE ATLAS
- OWASP LLM Top 10 (2025)
- ISO/IEC 42001
- NIST SP 800-53 Rev. 5

---

# 🎯 Purpose of This Portfolio

This repository demonstrates my ability to:

- Perform **end-to-end AI Security Assurance** across the full model lifecycle
- Design and implement **real security assessment pipelines**
- Conduct **LLM red teaming** with enterprise-grade tools
- Evaluate **RAG pipeline security** and retrieval-layer attack surfaces
- Assess **agentic AI security** across multi-tool and multi-agent architectures
- Evaluate **model safety, governance, and risk**
- Document processes in an **audit-ready, control-mapped format**
- Translate technical findings into governance controls and deployment recommendations

It reflects how I perform AI Security Assurance work in practice.

---

# 📬 Contact

**Frederick Baffour**

AI Security Assurance Engineer

LinkedIn: https://www.linkedin.com/in/frederick-baffour

Email: fbaffour@gmail.com

*Last updated: 2026*
