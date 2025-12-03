# Binary Integrity Verification Using Sigcheck

This document describes how **Sigcheck** is used to verify the authenticity and integrity of executables and binary tools within an AI Security Assurance workflow.

Sigcheck is not applied directly to model files (e.g., `.gguf`, `.safetensors`). Instead, it is used to validate the **tooling** involved in AI model intake, static analysis, and red-teaming activities, including:

- Installer packages  
- Command-line utilities  
- Scanning tools (YARA, ClamAV)  
- Runtime components  
- Third-party executables used within pipelines

Ensuring the trustworthiness of these tools helps maintain supply-chain integrity and reduces the risk of compromised binaries entering the environment.

---

## Why Sigcheck Is Important

Sigcheck verifies key security attributes of executable files, including:

- Presence of a digital signature  
- Identity of the publisher  
- Validity of the signing certificate  
- Evidence of tampering  
- Hash values for integrity checks  

This provides a reliable method for confirming that executables originate from legitimate and trusted sources.

---

## Example Sigcheck Command

```
sigcheck.exe -n -i "C:\Path\To\yara64.exe"
```

---

## Example Output (Typical)

```
Verified:         Signed
Signing date:     3:14 PM 01/23/2024
Publisher:        VirusTotal, LLC
Company:          VirusTotal
Description:      YARA - pattern matching tool
Product:          YARA
File version:     4.5.5.0
```

---

## Interpreting Results

### ✔ Signed and Valid
Indicates that the binary is signed by a trusted publisher and the signature is valid.

### ⚠ Signed but Certificate Issues
Indicates that a signature exists, but the certificate may be expired, invalid, or mismatched.

### ❌ Unsigned or Unknown Publisher
Indicates potential supply-chain risk:

- The binary may not be from an official source  
- The file may have been altered or tampered with  
- Malware or unwanted modifications may be present  

Binaries in this category should be quarantined and re-acquired from trusted sources.

---

## Common Use Cases in AI Workflows

Sigcheck is typically applied to:

- YARA executables  
- ClamAV binaries  
- Third-party security tools from GitHub  
- Model conversion utilities  
- Any external executable used within intake or analysis processes  

This ensures that supporting tools remain authentic, properly signed, and safe to execute in a security-sensitive environment.

---

## Conclusion

Sigcheck provides a critical layer of supply-chain validation by confirming the integrity and authenticity of binaries used in AI model intake, static analysis, and red-teaming workflows.  
Maintaining trusted executables is an essential control within a secure AI assurance pipeline.
