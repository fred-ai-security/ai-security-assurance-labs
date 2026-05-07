# Model Intake & Assurance Pipeline

This document outlines the structured workflow used to evaluate AI models during intake and validation. The pipeline spans six stages — from initial acquisition through consolidated reporting — and ensures only verified, assessed models progress into downstream use.

---

## Stage 1 — Intake and Integrity

**Objective:** Establish a verified, tamper-evident baseline before any further assessment.

Models are staged in a controlled, quarantined intake environment to prevent premature execution and ensure all validation steps are completed prior to runtime exposure.
- Compute and record SHA-256 hashes for all model artifacts
- Run YARA scans using general and model-specific rules
- Run ClamAV scans across the full staging directory

**Outcome:** Initial integrity is confirmed, or the model is flagged and quarantined pending review.

---

## Stage 2 — Supply-Chain Assessment

**Objective:** Validate model provenance, dependency health, and metadata authenticity.

- Generate a Software Bill of Materials (SBOM) using **Syft**
- Scan SBOM artifacts for known CVEs using **Grype**
- Review published model metadata, documentation, and model card fields
- Validate file hashes and signatures against upstream source values
- Confirm authenticity of the source repository and publisher identity
- Validate version history and release lineage for consistency

**Focus:** Detect tampering, unauthorized modifications, dependency-level risk, or inconsistencies in provenance.

---

## Stage 3 — Red Teaming and Behavioral Evaluation

**Objective:** Assess model behavior under adversarial, stress, and edge-case conditions.

- Use **Garak** for automated vulnerability and safety behavior testing across probe classes
- Use **PyRIT** for targeted jailbreak orchestration and manual adversarial scenarios
- Use **Promptfoo** for structured adversarial prompt evaluation with LLM-rubric assertions

Behavioral evaluation focuses on:

- Jailbreak and policy-evasion success rates
- Safety-filter bypass indicators
- Sensitive data leakage behavior
- Toxic or harmful content generation rates
- Hallucination frequency and severity

**Outcome:** Behavioral risk profile established with severity-scored findings.

---

## Stage 4 — RAG Pipeline Security Assessment

**Objective:** Evaluate the retrieval layer as an attack surface independent of base model behavior.

- Test for retrieval poisoning and context manipulation vulnerabilities
- Evaluate prompt injection via retrieved documents
- Assess jailbreak-through-retrieval attack viability
- Run structured adversarial harness with LLM judge evaluation

**Outcome:** RAG-layer risk profile with EXPLOITABLE / MITIGATED / PARTIAL verdicts per test case.

---

## Stage 5 — Agentic AI Security Assessment

**Objective:** Evaluate security posture of agent architectures and tool-use surfaces.

- Test tool call injection, goal hijacking, and indirect injection scenarios
- Assess privilege escalation and constraint bypass under adversarial conditions
- Evaluate multi-tool and orchestration attack surfaces
- Run structured 10-scenario harness across 8 attack classes

**Outcome:** Agent security posture documented with deflection rates and control gap identification.

---

## Stage 6 — Consolidated Reporting and Deployment Decision

**Objective:** Synthesize findings across all stages into a risk-tiered deployment recommendation.

- Aggregate findings from all prior stages
- Map risks to NIST AI RMF, MITRE ATLAS, OWASP LLM Top 10 (2025), ISO/IEC 42001, and NIST SP 800-53
- Produce consolidated output including:
  - Severity and likelihood ratings
  - Impact analysis across CIA triad
  - Recommended mitigations and controls
  - Final deployment decision

**Possible Outcomes:**

| Decision | Description |
|---|---|
| **Approved** | Model passes all tiers; cleared for use |
| **Conditional Hold** | Critical findings in one or more tiers; controls or mitigations required before use |
| **Rejected** | Findings indicate unacceptable risk; model is not approved for use |

---

## Framework Alignment

All stages of this pipeline map to the following frameworks:

| Framework | Application |
|---|---|
| NIST AI RMF | GOVERN, MAP, MEASURE, MANAGE functions applied across all six stages |
| MITRE ATLAS | TTP mapping for adversarial findings (Stages 3–5) |
| OWASP LLM Top 10 (2025) | Attack class alignment for red team and RAG findings |
| ISO/IEC 42001 | Governance and operational control alignment |
| NIST SP 800-53 | Supply-chain and access control mapping (Stages 1–2) |
