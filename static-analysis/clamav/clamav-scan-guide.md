# Scanning AI Model Artifacts with ClamAV

This document describes how ClamAV is used to detect malware, suspicious byte patterns, or embedded payloads inside AI model artifacts such as `.gguf`, `.safetensors`, tokenizer files, and related configuration assets.  
Although traditionally an antivirus engine, ClamAV is increasingly applied in AI supply-chain workflows as part of a layered static analysis strategy.

---

## Importance of ClamAV in AI Model Security

ClamAV is not used to assess model behavior, but to detect known malicious patterns embedded within model artifacts.

Model files are not executable binaries, yet they may still contain:

- Embedded malicious payloads  
- Encrypted or obfuscated data sections  
- Indicators of compromise  
- Tampering signatures  
- Known malware patterns  
- Suspicious binary structures  

ClamAV adds a signature-based detection layer to identify potentially harmful components before model artifacts enter evaluation or deployment workflows.

---

## Updating Virus Definitions

Prior to scanning, virus definitions are refreshed using:

```
freshclam
```

This ensures that ClamAV operates with the most recent malware signatures.

---

## Example ClamAV Scan Commands

To recursively scan a directory containing AI model artifacts:

```
clamscan -r "C:\AI_SECURITY_LABS\stage1_intake"
```

To scan a single file:

```
clamscan "C:\AI_SECURITY_LABS\stage1_intake\model.gguf"
```

---

## Example Output (Synthetic but Realistic)

```
C:\AI_SECURITY_LABS\stage1_intake\model.gguf: OK
C:\AI_SECURITY_LABS\stage1_intake\config.json: OK
C:\AI_SECURITY_LABS\stage1_intake\tokenizer.model: OK
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

### Clean Results  
Indicate that no known malware signatures were detected and the artifacts may proceed to the next stage of intake.

### Detection Events  
Any detection event halts the intake pipeline until remediation is completed.

If ClamAV flags any artifact as infected:

- The file should be quarantined  
- Hashes should be compared with source-of-truth repositories  
- Re-acquisition from an official, trusted provider is recommended  
- Findings should be documented for audit and governance  

A detection suggests overlap with known malware signatures, even in non-executable files.

---

## Limitations of ClamAV for AI Artifacts

ClamAV does not detect:

- Novel or zero-day malware  
- AI-specific malicious model manipulations  
- Logical or training-data backdoors  
- Adversarial triggers  
- Poisoned parameters or hidden behaviors  

For this reason, ClamAV is used alongside:

- YARA pattern-matching  
- SHA-256 integrity verification  
- Sigcheck signing and publisher validation  
- Manual inspection  
- Behavioral red teaming (Garak, Promptfoo, PyRIT)

---

## Position in the AI Assurance Pipeline

ClamAV is most relevant during:

1. **Stage 1 — Model Intake**  
   Detects known malware at initial acquisition.

2. **Stage 2 — Pre-Execution Validation**  
   Verifies that no infected artifacts are introduced into runtimes.

3. **Ongoing Monitoring**  
   Provides periodic reassessment as artifacts are updated or moved.

---

## Conclusion

ClamAV contributes a critical signature-based malware detection capability within AI supply-chain security workflows.  
When combined with YARA scanning, cryptographic hash verification, and broader model assurance techniques, it forms a robust early-warning layer against malicious or tampered model artifacts.  
Its inclusion within this repository reflects a mature, defense-in-depth approach to AI Security Assurance.

