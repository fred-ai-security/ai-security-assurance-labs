# Model Intake Workflow — Complete Example

This document presents a complete end-to-end model intake workflow used in AI Security Assurance. It outlines a staged process for securely acquiring, validating, and analyzing AI models prior to any assessment or deployment activity.

This example reflects a representative intake workflow and uses synthetic paths and outputs for demonstration purposes. Commands reflect the Ubuntu / WSL2 environment used in this lab.

**Workflow scope:**

- Secure model acquisition
- Hashing and integrity verification
- Static malware scanning (ClamAV)
- Pattern-based detection (YARA)
- Toolchain integrity validation
- Evidence collection and documentation

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MAP 1.5, MEASURE 2.2 — intake controls, artifact traceability, integrity verification |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise; AML.T0041 — Craft Adversarial Data |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; supply-chain artifact integrity |
| ISO/IEC 42001 | Clause 8 — AI system operation and artifact control |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SI-7 — Software and Information Integrity |

---

## Step 1 — Acquire the Model (Trusted Source)

Models are downloaded from verified, trusted sources using traceable methods only.

**Using HuggingFace CLI:**

```bash
huggingface-cli download microsoft/Phi-3-mini-4k-instruct --include "*.gguf"
```

**Using Ollama:**

```bash
ollama pull phi3:mini
```

After download, files are staged in a controlled intake directory:

```
~/ai-security-labs/stage1_intake/
```

---

## Step 2 — SHA-256 Hashing (Integrity Verification)

**Generate a hash for a single file:**

```bash
sha256sum ~/ai-security-labs/stage1_intake/model.gguf
```

**Generate a manifest for all files in the intake directory:**

```bash
find ~/ai-security-labs/stage1_intake -type f | xargs sha256sum > ~/ai-security-labs/hash_manifest.txt
```

The manifest serves as a tamper-evident baseline integrity record and is stored alongside intake documentation.

---

## Step 3 — YARA Scan (Pattern-Based Detection)

```bash
yara SuspiciousModelStrings.yar ~/ai-security-labs/stage1_intake/
```

Any positive match results in quarantine of the flagged artifact pending further review. The intake process does not proceed until the finding is resolved.

---

## Step 4 — ClamAV Scan (Malware Signature Detection)

```bash
clamscan -r ~/ai-security-labs/stage1_intake/
```

**Expected output:**

```
----------- SCAN SUMMARY -----------
Known viruses: 10,037,762
Infected files: 0
```

Detection of any infected file results in immediate quarantine and suspension of the intake process pending investigation.

---

## Step 5 — Toolchain Integrity Verification

Security tools are verified before use to ensure they have not been tampered with or substituted.

```bash
# Verify tool binary signatures using GPG or package manager verification
sha256sum $(which yara)
sha256sum $(which clamscan)
```

**Verification indicators:**

- Binary hash matches official published values
- Tool installed from a verified package source (apt, official release)
- No unexpected modifications to tool binaries

Mismatched or unverifiable binaries require re-acquisition from official sources before use.

---

## Step 6 — Promote Model to Verified Stage

If all checks pass, the model is promoted to the verified staging area:

```bash
mv ~/ai-security-labs/stage1_intake/model.gguf \
   ~/ai-security-labs/stage2_verified/model.gguf
```

Models that fail any check are quarantined and do not advance.

---

## Step 7 — Evidence Collection

The following evidence artifacts are produced and stored for each intake:

- Hash manifest (`hash_manifest.txt`)
- YARA scan results
- ClamAV scan output
- Toolchain verification records
- Download method, source URL, and timestamps

These materials support provenance tracking, audit requirements, and governance documentation.

---

## Step 8 — Transition to Downstream Assessment Stages

Once verified, the model advances through the remaining assessment lifecycle:

- **Stage 3 — Red Teaming:** Garak automated vulnerability scanning, PyRIT jailbreak orchestration, Promptfoo adversarial evaluation
- **Stage 4 — RAG Pipeline Security:** Retrieval poisoning, context manipulation, jailbreak-through-retrieval testing
- **Stage 5 — Agentic AI Security:** Tool call injection, goal hijacking, privilege escalation, indirect injection
- **Stage 6 — Consolidated Reporting:** Risk-tiered findings, framework-mapped controls, deployment recommendation

Only models that complete the full supply-chain intake process progress to these stages.
