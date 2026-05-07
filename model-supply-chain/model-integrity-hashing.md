# Model Integrity Verification (Hashing)

Model integrity verification ensures that AI model artifacts have not been altered, corrupted, or replaced between publication and use. This document covers how cryptographic hashing is used as a foundational control during AI model intake to confirm artifact integrity and support chain-of-custody requirements.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MAP 1.5, MEASURE 2.2 — artifact traceability and integrity verification |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise; AML.T0041 — Craft Adversarial Data |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning |
| ISO/IEC 42001 | Clause 8 — AI system operation and artifact control |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SI-7 — Software, Firmware, and Information Integrity |

---

## Purpose of Integrity Hashing

Hashing provides a deterministic fingerprint of each artifact at a defined point in time. In AI model supply-chain security, hashing is used to:

- Detect tampering or unauthorized modification
- Confirm consistency across environments
- Support provenance and audit records
- Validate artifacts before analysis or execution

Hashing is performed prior to any red teaming, behavioral testing, or runtime loading.

---

## Hashing Scope

Integrity hashing applies to all files present in the intake directory, including:

- Model artifacts (`.gguf`, `.safetensors`)
- Tokenizer files
- Configuration files
- Any auxiliary binaries or scripts included with the model

---

## Hashing Workflow

1. Generate SHA-256 hashes for all files in the intake directory
2. Store hashes in a manifest file associated with the intake record
3. Compare hashes against:
   - Provider-published checksums (when available)
   - Previous verified snapshots
4. Investigate or reject artifacts if mismatches are detected

Hash manifests are treated as evidence artifacts and referenced during later assessment stages.

---

## Evidence and Documentation

Recommended evidence artifacts include:

- Hash manifest file (CSV or structured text)
- Timestamp of hash generation
- Tool and algorithm used (SHA-256)
- Validation notes or anomalies observed

Real hashes and real artifacts are stored locally and are not committed to this repository.

---

## Relationship to Other Controls

Integrity hashing supports and complements:

- Provenance verification
- SBOM generation and CVE scanning (Syft / Grype)
- Static analysis (YARA, ClamAV)
- Model intake and approval decisions

Hashing is a prerequisite control — artifacts that fail integrity verification do not proceed to any further assessment stage.
