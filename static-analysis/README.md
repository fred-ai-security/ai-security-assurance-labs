# Static Analysis for AI Model Security

This section documents static analysis methods used to evaluate AI model files and related artifacts before execution or deployment. Static analysis is performed during early intake stages and prior to any model execution or red-teaming activity.

Framework alignment follows the mappings defined in `model-supply-chain/README.md` and `model-risk-classification-and-criticality.md`.

Static analysis identifies:

- Malware embedded in model weights
- Suspicious or malformed file structures
- Hidden payloads inside formats such as safetensors or GGUF
- Supply-chain tampering
- Integrity and authenticity issues

---

## Tools in This Section

| Tool | Purpose |
|---|---|
| YARA | Pattern-matching engine for detecting suspicious strings, metadata indicators, and embedded payloads |
| ClamAV | Signature-based malware scanner for known malicious patterns in model artifact directories |
| SHA-256 Hashing | Cryptographic hashing for file integrity verification and provenance comparison |
| Toolchain Integrity | Binary verification of security tools (YARA, ClamAV) to confirm authenticity before use |

> **SBOM and CVE scanning (Syft / Grype)** are documented in `model-supply-chain/sbom-generation-and-verification.md` and `model-supply-chain/sbom-example-results.md`, where they fit architecturally within the supply-chain intake workflow.

---

## Subfolders

| Folder | Contents |
|---|---|
| `hashing/` | SHA-256 hashing and integrity verification workflows |
| `clamav/` | Malware scanning using ClamAV with example commands and outputs |
| `yara/` | Pattern-based detection using YARA rules for suspicious model artifacts |
| `sigcheck/` | Toolchain binary verification for security utilities used in intake and analysis |

Only example commands, templates, and synthetic outputs are stored here. No real model artifacts, hashes, or scan logs are committed to this repository.
