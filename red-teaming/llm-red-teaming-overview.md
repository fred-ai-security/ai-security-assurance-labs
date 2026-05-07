# LLM Red Teaming Overview

Red teaming is treated as a structured security control applied at Stage 3 of the AI Security Assurance Lifecycle. It is designed to identify unsafe behavior, misuse potential, and adversarial weaknesses in AI models prior to approval or deployment.

Red-teaming activities focus on how models behave under adversarial, ambiguous, or stress-inducing conditions — complementing supply-chain validation (Stages 1–2) by addressing **behavioral risk** rather than artifact integrity. Results feed directly into RAG pipeline security assessment, agentic AI evaluation, risk classification, and deployment decisions (Stages 4–6).

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MEASURE 2.6 — robustness testing, adversarial evaluation, and behavioral risk assessment |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — LLM Prompt Injection; AML.T0043 — Craft Adversarial Examples |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling; LLM06 — Sensitive Information Disclosure |
| ISO/IEC 42001 | Clause 8 — AI system behavioral testing and safety evaluation |
| NIST SP 800-53 | SA-11 — Developer Testing and Evaluation; CA-8 — Penetration Testing |

---

## Objectives

Red-teaming activities target the following behavioral risk dimensions:

- Jailbreak and prompt injection vulnerabilities
- Refusal reliability and policy enforcement consistency
- Harmful, toxic, or unsafe output generation
- Susceptibility to manipulation and misuse
- Hallucination patterns in high-risk scenarios
- Model behavior under edge-case and adversarial conditions

---

## Threat Model Assumptions

Red-teaming scenarios assume:

- Malicious or curious users attempting to bypass safety guardrails
- Ambiguous prompts designed to induce unsafe behavior
- Attempts to extract restricted information or system instructions
- Efforts to manipulate role definitions or system-level constraints

Testing emphasizes realistic misuse scenarios rather than theoretical attack constructs.

---

## Red Teaming Methods

Three complementary assessment methods are applied across Stage 3:

| Method | Tool | Purpose |
|---|---|---|
| Automated probe testing | Garak | Broad vulnerability coverage across 10+ attack classes and 1,280+ probes |
| Scenario-driven evaluation | Promptfoo | Structured adversarial test cases with LLM-rubric assertions |
| PyRIT-inspired testing | Custom Transformers harness | Local adversarial evaluation across 8 attack categories with indicator-based detection |

Each method contributes distinct coverage — automated breadth (Garak), structured scenarios (Promptfoo), and targeted manual-style evaluation (PyRIT-inspired) — and results are reviewed in combination rather than in isolation.

---

## Interpretation of Findings

Red-team results are evaluated based on:

- Frequency and severity of unsafe outputs
- Consistency of refusal behavior across test variations
- Ease of exploitation under realistic conditions
- Potential real-world impact across risk domains
- Alignment with the model's documented safety claims

Findings are severity-rated and mapped to framework controls before feeding into governance decisions.

---

## Relationship to the Assessment Lifecycle

**Prerequisites (Stages 1–2):**
- Model provenance and integrity verification
- Licensing, documentation, and supply-chain validation

**Stage 3 — Red Teaming outputs:**
- Behavioral risk profile with severity-rated findings
- Framework-mapped attack class coverage
- Evidence artifacts for consolidated reporting

**Downstream stages (4–6):**
- RAG pipeline security assessment
- Agentic AI security evaluation
- Consolidated reporting, risk classification, and deployment decision
