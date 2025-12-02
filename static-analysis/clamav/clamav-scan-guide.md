# Scanning AI Model Artifacts with ClamAV

This document explains how **ClamAV** can be used to detect malware, suspicious byte patterns, or embedded payloads inside AI model files such as `.gguf`, `.safetensors`, tokenizer data, and supporting configuration files.

ClamAV is traditionally an antivirus engine, but it is increasingly used in AI supply-chain workflows as part of a layered static analysis process.

---

## Why ClamAV Matters for AI Model Security

Even though model files are not executables, they can still contain:

- Embedded malicious payloads  
- Encrypted or obfuscated data blobs  
- Indicators of compromise  
- Signs of tampering  
- Known malware signatures  
- Suspicious binary sections  

ClamAV adds a defensive layer by leveraging a large signature database to identify potentially harmful content.

This helps ensure malicious data does not enter your AI evaluation or deployment pipeline.

---

## Updating ClamAV Virus Definitions

Before scanning, update the virus database using:

```
freshclam
```

This ensures the engine uses the most current malware signatures.

---

## Example ClamAV Scan Command

To scan a model file or directory:

```
clamscan -r "C:\AI_SECURITY_LABS\stage1_intake"
```

Where:

- `clamscan` = ClamAV scanner  
- `-r` = recursive scan  
- Path = directory containing AI model files  

You can also scan a single file:

```
clamscan "C:\AI_SECURITY_LABS\stage1_intake\model.gguf"
```
---

## Example Output (Realistic)

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

## Interpreting Results

### ✔ No Infected Files  
The model files show no known malware signatures and can move to the next stage of intake.

### ⚠ Infected Files Found  
If ClamAV reports any file as infected:

- **Quarantine the file immediately**  
- Do NOT load it into a model runtime  
- Compare file hashes with the source repository  
- Re-download from an official model provider  
- Consider notifying the team or platform  

ClamAV alerts indicate known malware patterns — even inside non-executable formats.

---

## Limitations of ClamAV for AI Models

ClamAV provides useful detection, but it cannot find everything:

- Unknown malware or zero-day payloads  
- Novel AI-specific tampering  
- Embedded logical backdoors  
- Adversarial triggers  
- Hidden model manipulations  

This is why ClamAV should be combined with:

- YARA scanning  
- File hash verification  
- Sigcheck validation  
- Manual inspection  
- Behavioral red teaming (Garak, Promptfoo, PyRIT)  

---

## Where ClamAV Fits in Your AI Assurance Pipeline

ClamAV is most effective in:

1. **Stage 1 – Model Intake**  
   Identify known malware inside newly downloaded files.

2. **Stage 2 – Pre-Execution Validation**  
   Confirm the model files are clean before being run.

3. **Ongoing Monitoring**  
   Re-scan anytime files are modified, updated, or moved.

---

## Conclusion

ClamAV adds an important layer of static malware detection to your AI model supply-chain security. When combined with YARA, Sigcheck, and proper hash verification, it forms a robust early-warning system that reduces the risk of malicious model artifacts entering your environment.

Its integration into your repository demonstrates a practical and mature approach to AI Security Assurance.
