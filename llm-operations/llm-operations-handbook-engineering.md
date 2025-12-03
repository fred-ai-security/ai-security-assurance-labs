# LLM Operations Handbook – Engineering Edition
A Technical Reference for Model Intake, Evaluation, Red Teaming, and Operational Controls

---

## 1. Overview

This handbook defines engineering procedures, controls, and operational workflows for managing large language models (LLMs) in secure environments. It documents processes for model intake, supply-chain verification, static analysis, safety evaluation, risk classification, red teaming, and operational deployment. The objective is to establish a standardized and repeatable approach to handling third-party and internally developed models, ensuring integrity, safety, reliability, and governance alignment.

---

## 2. Model Intake Architecture

LLM intake follows a structured four-stage pipeline:

```
Stage 1 — Intake & Integrity
    ↓
Stage 2 — Supply-Chain Verification
    ↓
Stage 3 — Red Teaming & Safety Evaluation
    ↓
Stage 4 — Documentation & Deployment Decision
```

### Stage 1 — Integrity Validation
- Source verification  
- Secure download  
- SHA-256 hashing  
- YARA scanning  
- ClamAV scanning  
- Toolchain integrity checks (Sigcheck)

### Stage 2 — Supply-Chain Verification
- Model card validation  
- License and compliance checks  
- Provenance validation  
- SBOM generation and verification  
- Metadata alignment (files, parameters, architecture, versions)

### Stage 3 — Safety Testing & Red Teaming
- Functional and behavioral safety tests  
- Adversarial testing using Garak, Promptfoo, and PyRIT  
- Jailbreak, prompt injection, role manipulation, and multi-turn evaluation  
- Sensitive domain safety review  
- Hallucination and reliability analysis

### Stage 4 — Deployment Decision
- Risk scoring and classification  
- Documentation of findings  
- Approval, conditional approval, or rejection  
- Evidence retention and governance alignment

---

## 3. Model Source & Download Controls

### Allowed Sources
- Verified HuggingFace organizations  
- Official model providers  
- GitHub Releases pages from trusted vendors  
- Ollama official library entries  

### Verification Requirements
- Publisher identity and account history  
- License clarity  
- Changelog and version lineage  
- File structure consistency  
- Known-good hash comparison (if available)

---

## 4. Integrity & Static Analysis Controls

### Hashing
- SHA-256 hashing for all model artifacts  
- Manifest creation and re-verification during intake and prior to deployment  

### YARA Scanning
- Detection of suspicious strings, embedded payloads, or unauthorized patterns  

### ClamAV Scanning
- Signature-based detection of known malware  
- Applied to the full intake directory  

### Binary Verification (Sigcheck)
- Validation of scanning tools and third-party binaries  
- Signature trust evaluation  
- Publisher identity verification

---

## 5. Model Provenance Recording

Each model must have a provenance record containing:
- Source repository  
- Download method  
- File list  
- Hash values  
- File sizes  
- License summary  
- Safety disclosures  
- Verification results from intake pipeline  

Only synthetic templates are stored in the repository.

---

## 6. SBOM (Software Bill of Materials)

Tools used:
- Syft for file inventory and CycloneDX output  
- Trivy for CVE scanning  
- GGUF/safetensors metadata extraction utilities  

Required SBOM contents:
- File inventory  
- Hashes  
- Dependency list  
- Versions and metadata  
- Unexpected or suspicious files  
- CVE mapping results  

---

## 7. License & Compliance Validation

License evaluation confirms:
- License type (permissive, research-only, restrictive)  
- Redistribution terms  
- Commercial use permissions  
- Fine-tuning restrictions  
- Export controls  
- Required disclosures  
- Consistency between model card and LICENSE file  

Non-compliant models are rejected.

---

## 8. Model Card Validation Requirements

Model cards are evaluated for:
- Purpose and intended use  
- Limitations and safety disclosures  
- Training data transparency  
- Benchmark results  
- Version history  
- File list alignment  

Missing or contradictory information results in reduced trust.

---

## 9. Risk Classification & Criticality Tiering

Risk dimensions:
- Harm likelihood  
- Exploitability  
- Severity of harm  
- Domain sensitivity  
- Data sensitivity  
- Automation level  
- User impact  

Risk levels:
- Low  
- Medium  
- High  
- Critical  

Criticality tiers:
- Tier 1 — High-risk domains  
- Tier 2 — Moderate-risk enterprise functions  
- Tier 3 — Low-risk or experimental use  

---

## 10. Red Teaming Framework

### Garak
Automated probing of jailbreaks, prompt injection, toxicity, refusal inconsistencies.

### Promptfoo
Scenario-based evaluations using YAML-driven test suites, including insider threat prompts, policy bypasses, and high-risk domain scenarios.

### PyRIT
Orchestrated adversarial interactions including multi-turn manipulation, role erosion, context poisoning, and escalation scenarios.

---

## 11. Safety Evaluation Framework

Evaluations include:
1. Functional safety  
2. Behavioral safety  
3. Adversarial safety  
4. Hallucination and reliability  
5. Sensitive domain safety  

Each captures:
- Observed behaviors  
- Severity  
- Likelihood  
- Impact  
- Summary of risk  

---

## 12. Logging, Evidence, and Documentation

Retained evidence:
- Hash manifests  
- YARA results  
- ClamAV outputs  
- Sigcheck validation  
- SBOM reports  
- Risk classification  
- License evaluation  
- Model card review  
- Provenance record  

No real model logs or outputs are stored in the repository.

---

## 13. Deployment Readiness Decision

Deployment requires:
- Successful integrity checks  
- Supply-chain verification  
- SBOM validation  
- Safety evaluation  
- Red teaming results  
- Acceptable risk classification  

Possible decisions:
- Approved  
- Approved with conditions  
- Restricted use  
- Rejected  

---

## 14. Continuous Monitoring

Monitoring covers:
- Behavior drift  
- New jailbreak vectors  
- Emerging CVEs  
- Licensing changes  
- Hash modifications  
- New model releases  
- Version lineage changes  

---

## 15. Directory Placement

```
ai-security-assurance-labs/
└── llm-operations/
      └── llm-operations-handbook-engineering.md
```

---

# End of Engineering Edition
