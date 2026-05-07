# YARA Scanning for AI Model Artifacts

YARA is used to scan AI model files for suspicious patterns as part of the AI Security Assurance intake workflow. While AI models such as `.gguf` or `.safetensors` are not traditional executables, they may contain embedded malicious strings, obfuscated payloads, encoded commands, suspicious configuration fragments, or indicators of tampering.

Framework alignment follows the mappings defined in `../README.md` and `model-supply-chain/model-integrity-hashing.md`.

---

## Position in the Assessment Lifecycle

YARA is most effective during **Stage 1 — Model Intake**, scanning newly downloaded artifacts in the controlled intake directory before any further processing. Files that trigger YARA rules are quarantined before progressing in the intake pipeline.

---

## Example YARA Rule

```yara
rule SuspiciousModelStrings
{
    strings:
        $eval = "eval(" nocase
        $ps   = "powershell" nocase
        $enc  = /[A-Za-z0-9\/\+]{40,}/   // high-entropy string pattern

    condition:
        any of ($eval, $ps, $enc)
}
```

---

## Scan Command

```bash
yara SuspiciousModelStrings.yar ~/ai-security-labs/stage1_intake/
```

---

## Example Output (Synthetic)

```
SuspiciousModelStrings  /home/user/ai-security-labs/stage1_intake/model.bin
SuspiciousModelStrings  /home/user/ai-security-labs/stage1_intake/config.json
```

Each line indicates a rule match on the corresponding file.

---

## Result Interpretation

**No matches** — files passed the YARA scan and may proceed to ClamAV scanning and SHA-256 integrity verification.

**Matches found** — files are considered suspicious:

- Quarantine the file
- Compare hashes against trusted provider values
- Investigate which pattern triggered the rule
- Re-download from an official source if needed

---

## Role in Layered Static Analysis

YARA is used alongside ClamAV, SHA-256 hashing, and toolchain binary verification. Each tool contributes a distinct detection capability:

| Tool | Detection Type |
|---|---|
| YARA | Pattern-based — suspicious strings, structural indicators |
| ClamAV | Signature-based — known malware patterns |
| SHA-256 | Integrity-based — file tampering and modification detection |
| Toolchain verification | Trust-based — authenticity of assessment tools |
