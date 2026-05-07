# Model Supply-Chain Security

## Overview

This section documents how AI models are obtained, validated, and reviewed prior to use. It establishes a structured intake workflow for ensuring trust, integrity, and security across all stages of model acquisition — before any model progresses to red teaming, behavioral evaluation, or deployment.

---

## Scope

This section addresses the following components:

- Secure model acquisition and controlled staging
- Integrity verification through SHA-256 hashing
- Static analysis of model files using YARA and ClamAV
- SBOM generation and CVE scanning using Syft and Grype
- Metadata and documentation review for supply-chain assurance
- Provenance validation and trusted-source verification
- A staged intake workflow from initial acquisition through approval

See `intake-pipeline-overview.md` for the full pipeline.

---

## Supply-Chain Focus Areas

### 1. Acquisition and Staging

Models are staged in a controlled intake location to prevent premature use and ensure all verification steps are completed before runtime exposure.

### 2. Integrity Verification

SHA-256 hashing is used to validate that downloaded artifacts match expected values from trusted sources. Integrity manifests are stored alongside evaluation documentation to support auditability and chain-of-custody requirements.

### 3. Static File Analysis

Malware and anomaly detection is conducted using:

- **YARA** — rule-based pattern matching for structural and behavioral signatures
- **ClamAV** — signature-based malware scanning against model artifacts

These checks identify tampering, malicious payloads, or unexpected structural patterns inside model files before they are used in any assessment or inference workflow.

### 4. SBOM Generation and CVE Scanning

Software Bill of Materials (SBOM) artifacts are generated using **Syft** and scanned for known vulnerabilities using **Grype**. This step surfaces dependency-level risk that static file analysis alone does not capture.

### 5. Metadata and Documentation Review

Key metadata fields — including model card details, file inventories, versioning, release notes, and licensing — are validated against the upstream source. This step supports traceability, licensing review, and alignment with AI governance and risk management requirements.

### 6. Provenance and Trusted-Source Verification

Model origin, provider authenticity, and release lineage are reviewed to confirm the model has not been replaced, altered, or sourced from an unverified distribution point.

### 7. Staged Intake Workflow

Supply-chain assessment is structured as the first two stages of a six-stage AI Security Assurance Lifecycle:

- **Stage 1 — Intake & Integrity:** Acquisition, staging, hashing, and initial file validation
- **Stage 2 — Supply-Chain Assessment:** Provenance review, SBOM generation, CVE scanning, static analysis, and metadata validation
- **Stage 3 — Red Teaming & Behavioral Evaluation:** Adversarial testing against the validated model
- **Stage 4 — RAG Pipeline Security:** Retrieval-layer attack surface assessment
- **Stage 5 — Agentic AI Security:** Agent tool and orchestration attack testing
- **Stage 6 — Reporting & Governance:** Consolidated findings, risk classification, and deployment recommendation

Each stage supports auditability and produces documented outputs that feed the next stage.

---

## Framework Alignment

Supply-chain security work in this section maps to the following frameworks:

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | GOVERN 1.1, MAP 1.5, MANAGE 2.2 |
| MITRE ATLAS | AML.T0041 — Craft Adversarial Data; AML.T0010 — ML Supply Chain Compromise |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; LLM05 — Improper Output Handling |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SR-3 — Supply Chain Controls |
| ISO/IEC 42001 | Clause 8 — AI System Operation and Control |

---

## Role in the Lifecycle

This section functions as the foundation for all downstream assessment work. Only models that complete the full supply-chain intake process progress into red teaming, RAG pipeline evaluation, or agentic security testing. This ensures that behavioral and adversarial assessments are conducted on verified, trusted artifacts.
