# Model Integrity Verification Using SHA-256 Hashing

SHA-256 hashing is used to verify the integrity of AI model files including `.gguf`, `.safetensors`, tokenizer files, and related assets. Hashing confirms that files have not been modified, tampered with, or corrupted during download, transfer, or storage.

Framework alignment follows the mappings defined in `../README.md` and `model-supply-chain/model-integrity-hashing.md`.

---

## Role in AI Model Security

A SHA-256 hash serves as a deterministic fingerprint for each artifact. Any change to the file produces a different hash value. Hash verification is performed at multiple points:

- Stage 1 — Model Intake
- Stage 2 — Pre-execution validation
- Red-teaming preparation
- Deployment readiness checks
- Ongoing monitoring and provenance validation

---

## Generating SHA-256 Hashes

**Hash a single file:**

```bash
sha256sum ~/ai-security-labs/stage1_intake/model.gguf
```

Example output:

```
64a1f1c338bd982f19352d0d321fa74e15e77294c8e47a31a5e6bc8f39c1a22a  model.gguf
```

**Hash all files in a directory:**

```bash
find ~/ai-security-labs/stage1_intake -type f | xargs sha256sum
```

---

## Creating a Hash Manifest

A hash manifest records expected hash values for future verification:

```bash
find ~/ai-security-labs/stage1_intake -type f | xargs sha256sum > ~/ai-security-labs/hash_manifest.txt
```

The manifest acts as a tamper-evident reference point across intake, validation, testing, and deployment stages.

---

## Verifying Files Against the Manifest

```bash
sha256sum --check ~/ai-security-labs/hash_manifest.txt
```

Example output:

```
model.gguf: OK
config.json: OK
tokenizer.model: FAILED
sha256sum: WARNING: 1 computed checksum did NOT match
```

Any `FAILED` result indicates a file has changed since the manifest was created.

---

## Result Interpretation

**Matching hashes** — file is unchanged and consistent with the expected state.

**Mismatched hashes** — indicate possible tampering, file corruption, malicious replacement, partial download failure, or unauthorized modification. Impacted files should be quarantined, re-acquired from a trusted source, and investigated for supply-chain compromise.

---

## Evidence and Audit Requirements

For each model acquired, maintain:

- Model file(s) and SHA-256 hash values
- Source URL and acquisition date
- Manifest file used in later verification steps

This supports provenance tracking and audit requirements within AI governance programs.
