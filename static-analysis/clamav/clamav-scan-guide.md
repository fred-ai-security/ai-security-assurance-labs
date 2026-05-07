# Scanning AI Model Artifacts with ClamAV

ClamAV is used to detect malware, suspicious byte patterns, or embedded payloads inside AI model artifacts such as `.gguf`, `.safetensors`, tokenizer files, and related configuration assets. Although traditionally an antivirus engine, ClamAV is applied in AI supply-chain workflows as part of a layered static analysis strategy.

Framework alignment follows the mappings defined in `../README.md` and `model-supply-chain/model-integrity-hashing.md`.

---

## Role in AI Model Security

ClamAV is not used to assess model behavior — it detects known malicious patterns embedded within model artifacts. Model files are not executable binaries, yet they may still contain embedded malicious payloads, encrypted or obfuscated data sections, indicators of compromise, tampering signatures, and known malware patterns.

ClamAV adds a signature-based detection layer before model artifacts enter evaluation or deployment workflows.

---

## Updating Virus Definitions

Prior to scanning, virus definitions are refreshed:

```bash
freshclam
```

---

## Scan Commands

**Recursively scan a directory:**

```bash
clamscan -r ~/ai-security-labs/stage1_intake/
```

**Scan a single file:**

```bash
clamscan ~/ai-security-labs/stage1_intake/model.gguf
```

---

## Example Output (Synthetic)

```
/home/user/ai-security-labs/stage1_intake/model.gguf: OK
/home/user/ai-security-labs/stage1_intake/config.json: OK
/home/user/ai-security-labs/stage1_intake/tokenizer.model: OK

----------- SCAN SUMMARY -----------
Known viruses: 10037762
Engine version: 1.5.1
Scanned directories: 1
Scanned files: 3
Infected files: 0
Data scanned: 144.23 MB
```

---

## Result Interpretation

**Clean results** — no known malware signatures detected; artifacts may proceed to the next intake stage.

**Detection events** — any detection halts the intake pipeline until remediation is completed:

- Quarantine the flagged file
- Compare file hashes against source-of-truth values
- Re-acquire from an official, trusted provider
- Document findings for audit and governance

---

## Limitations

ClamAV does not detect:

- Novel or zero-day malware
- AI-specific model manipulations
- Logical or training-data backdoors
- Adversarial triggers or poisoned parameters

ClamAV is therefore used alongside YARA pattern-matching, SHA-256 integrity verification, toolchain binary verification, and behavioral red teaming (Garak, Promptfoo, PyRIT-inspired testing).

---

## Position in the Assessment Lifecycle

- **Stage 1 — Model Intake:** detects known malware at initial acquisition
- **Stage 2 — Pre-Execution Validation:** verifies no infected artifacts enter runtimes
- **Ongoing monitoring:** periodic reassessment as artifacts are updated or moved
