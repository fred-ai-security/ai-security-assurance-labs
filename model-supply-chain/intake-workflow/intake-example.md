# Model Intake Workflow — Complete Example

This walkthrough demonstrates a full end-to-end model intake workflow used in AI Security Assurance.  
It shows how to safely download, verify, and analyze an AI model before it is used in any environment.

This workflow includes:

- Secure model acquisition  
- Hashing & integrity checks  
- Static malware scanning (ClamAV)  
- Pattern-based detection (YARA)  
- Toolchain signature validation (Sigcheck)  
- Evidence collection & documentation  

---

## 1. Download the Model (Trusted Source Only)

Example using HuggingFace CLI:

```
huggingface-cli download microsoft/Phi-3-mini-4k-instruct --include "*.gguf"
```

Or using Ollama:

```
ollama pull phi:latest
```

Move the downloaded file into your **Stage 1 intake directory**:

```
C:\AI_SECURITY_LABS\stage1_intake
```

---

## 2. Run SHA-256 Hashing (Integrity Verification)

Generate the hash:

```
Get-FileHash "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" -Algorithm SHA256
```

Generate manifest for all files:

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Export-Csv "C:\AI_SECURITY_LABS\hash_manifest.csv" -NoTypeInformation
```

Store manifest in your repo or evidence folder.

---

## 3. Run YARA Scan (Suspicious Patterns)

Example:

```
yara64.exe SuspiciousModelStrings.yar "C:\AI_SECURITY_LABS\stage1_intake"
```

If YARA produces **any hits**, quarantine the file.

---

## 4. Run ClamAV Scan (Malware Signatures)

Scan the intake directory:

```
clamscan -r "C:\AI_SECURITY_LABS\stage1_intake"
```

Expect output like:

```
----------- SCAN SUMMARY -----------
Known viruses: 10,037,762
Infected files: 0
```

If anything is detected → stop the workflow.

---

## 5. Validate Toolchain Integrity (Sigcheck)

Before trusting your scanning tools, verify they are signed:

```
sigcheck.exe -n -i "C:\Tools\yara\yara64.exe"
sigcheck.exe -n -i "C:\ClamAV\clamd.exe"
sigcheck.exe -n -i "C:\Tools\sigcheck\sigcheck.exe"
```

Look for:

- “Verified: Signed”
- A valid certificate
- Publisher matches expected vendor  

If not → re-download from official source.

---

## 6. Move Model to “Verified” Storage (Stage 2)

If all checks passed:

```
C:\AI_SECURITY_LABS\stage2_verified\
```

Create the directory if it doesn’t exist.

Move the clean model:

```
Move-Item "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" `
          "C:\AI_SECURITY_LABS\stage2_verified\model.gguf"
```

---

## 7. Evidence Collection

Recommended to store:

- Hash manifest  
- YARA results  
- ClamAV scan output  
- Sigcheck validation  
- Download source  
- Date/time of intake  

This forms a **model provenance record** used by AI Governance and ML Ops teams.

---

## 8. Next Step: LLM Red Teaming

Once the model is verified & trusted:

You may proceed with:

- Garak scans  
- Promptfoo evaluations  
- Manual adversarial prompts  

This is **Stage 3 — Assessment** of your pipeline.

---

# ✔ Summary

This workflow demonstrates:

- Supply-chain security  
- Malware detection & static analysis  
- Model integrity protection  
- Toolchain trust validation  
- Evidence-based AI Assurance  

This example mirrors the real processes used by enterprise AI Security teams.

