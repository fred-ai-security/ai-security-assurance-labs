# Model Intake Workflow — Complete Example

This document presents a complete end-to-end model intake workflow used in AI Security Assurance.  
It outlines a staged process for securely acquiring, validating, and analyzing AI models prior to use.

The workflow includes:

- Secure model acquisition  
- Hashing and integrity verification  
- Static malware scanning (ClamAV)  
- Pattern-based detection (YARA)  
- Toolchain signature validation (Sigcheck)  
- Evidence collection and documentation  

---

## 1. Download the Model (Trusted Source)

Example using HuggingFace CLI:

```
huggingface-cli download microsoft/Phi-3-mini-4k-instruct --include "*.gguf"
```

Example using Ollama:

```
ollama pull phi:latest
```

After download, files are placed in a Stage 1 intake directory such as:

```
C:\AI_SECURITY_LABS\stage1_intake
```

---

## 2. SHA-256 Hashing (Integrity Verification)

Generate a hash for a single file:

```
Get-FileHash "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" -Algorithm SHA256
```

Generate a manifest for all files:

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Export-Csv "C:\AI_SECURITY_LABS\hash_manifest.csv" -NoTypeInformation
```

The manifest serves as a baseline integrity record.

---

## 3. YARA Scan (Pattern-Based Detection)

Example command:

```
yara64.exe SuspiciousModelStrings.yar "C:\AI_SECURITY_LABS\stage1_intake"
```

Any positive match indicates that the file should be quarantined for further review.

---

## 4. ClamAV Scan (Malware Signature Detection)

Scan the intake directory recursively:

```
clamscan -r "C:\AI_SECURITY_LABS\stage1_intake"
```

Expected output example:

```
----------- SCAN SUMMARY -----------
Known viruses: 10,037,762
Infected files: 0
```

Detection of any infected file ends the intake process.

---

## 5. Toolchain Verification (Sigcheck)

Before trusting security tools, check their signatures:

```
sigcheck.exe -n -i "C:\Tools\yara\yara64.exe"
sigcheck.exe -n -i "C:\ClamAV\clamd.exe"
sigcheck.exe -n -i "C:\Tools\sigcheck\sigcheck.exe"
```

Verification indicators:

- “Verified: Signed”  
- Valid certificate chain  
- Publisher identity matches expected vendor  

Unsigned or mismatched binaries require re-acquisition from official sources.

---

## 6. Promote Model to Stage 2 (Verified Storage)

If all checks pass, the model is moved into the verified stage:

```
C:\AI_SECURITY_LABS\stage2_verified\
```

File promotion example:

```
Move-Item "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" `
          "C:\AI_SECURITY_LABS\stage2_verified\model.gguf"
```

---

## 7. Evidence Collection

Recommended evidence includes:

- Hash manifest  
- YARA scan results  
- ClamAV scan output  
- Sigcheck verification records  
- Download method and source  
- Intake date and timestamps  

These materials support provenance tracking and audit requirements.

---

## 8. Transition to Assessment (Red Teaming)

Once verified, the model advances to Stage 3 assessment activities, such as:

- Garak automated vulnerability scanning  
- Promptfoo adversarial prompt evaluations  
- Manual red-team analysis  

These assessments contribute to behavioral, adversarial, and reliability evaluation.

---

## Summary

This intake workflow provides structured controls for:

- Model supply-chain assurance  
- Integrity verification  
- Malware and pattern-based analysis  
- Toolchain validation  
- Evidence-based documentation  

The process reflects common practices in enterprise AI security and governance programs.
