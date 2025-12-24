# Model Integrity Verification (Hashing)

Model integrity verification ensures that AI model artifacts have not been altered, corrupted, or replaced between publication and use.

This module documents how cryptographic hashing is used as a foundational control during AI model intake to confirm artifact integrity and support auditability.

---

## Purpose of Integrity Hashing

Hashing provides a deterministic fingerprint of a file at a specific point in time.  
In AI model supply-chain security, hashing is used to:

- Detect tampering or unauthorized modification
- Confirm consistency across environments
- Support provenance and audit records
- Validate artifacts before analysis or execution

Hashing is performed prior to any red-teaming, behavioral testing, or runtime loading.

---

## Hashing Scope

Integrity hashing applies to:

- Model artifacts (e.g., `.gguf`, `.safetensors`)
- Tokenizer files
- Configuration files
- Any auxiliary binaries or scripts included with the model

All files present in the intake directory are included in the hash record.

---

## Hashing Workflow

1. Generate SHA-256 hashes for all files in the intake directory.
2. Store hashes in a manifest file associated with the intake record.
3. Compare hashes against:
   - Provider-published checksums (when available)
   - Previous verified snapshots
4. Investigate or reject artifacts if mismatches are detected.

Hash manifests are treated as evidence artifacts and referenced during later assessment stages.

---

## Evidence and Documentation

Recommended evidence includes:

- Hash manifest file (CSV or text)
- Timestamp of hash generation
- Tool and algorithm used (e.g., SHA-256)
- Validation notes or anomalies observed

Real hashes and real artifacts are stored locally and are not committed to this repository.

---

## Relationship to Other Controls

Integrity hashing supports and complements:

- Provenance verification
- SBOM generation and validation
- Static analysis (YARA, ClamAV)
- Model intake and approval decisions

Hashing is a prerequisite control within the broader model intake pipeline.

---

This module defines integrity hashing as a repeatable, auditable security control within AI supply-chain assurance workflows.
