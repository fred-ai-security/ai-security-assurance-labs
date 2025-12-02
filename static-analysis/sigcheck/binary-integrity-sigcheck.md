# Binary Integrity Verification Using Sigcheck

This document demonstrates how **Sigcheck** can be used to verify the authenticity and integrity of executables and binary tools used within an AI Security Assurance workflow.

While Sigcheck is **not used directly to scan model files** (e.g., `.gguf`, `.safetensors`), it plays a critical role in verifying the **tooling** involved in AI model intake, red teaming, and evaluation — including:

- Installer packages  
- Command-line utilities  
- Scanning tools (YARA, ClamAV)  
- Runtime components  
- Third-party executables used in workflows  

This supports AI supply-chain trust by ensuring no compromised or unsigned binaries are introduced into the environment.

---

## Why Sigcheck Matters

Before running any executable, especially one downloaded from GitHub or package repositories, it is important to verify:

- Whether the binary is digitally signed  
- Who the publisher is  
- Whether the certificate is valid  
- Whether the file has been tampered with  
- Whether it matches expected hash values  

Sigcheck provides these details quickly and reliably.

---

## Example Sigcheck Command

sigcheck.exe -n -i "C:\Path\To\yara64.exe"

## Example Output (Realistic)

Verified:         Signed
Signing date:     3:14 PM 01/23/2024
Publisher:        VirusTotal, LLC
Company:          VirusTotal
Description:      YARA - pattern matching tool
Product:          YARA
File version:     4.5.5.0

---

## Interpreting the Results

✔ Signed & Valid
- The binary is signed by a trusted publisher and the signature is valid.

⚠ Signed but Certificate Issues
- Signature exists but may be expired or mismatched.

❌ Unsigned or Unknown Publisher
- Indicates potential supply-chain risk:
- File may not be from the official source
- File may have been tampered with
- Potential malware risk

Such binaries should be quarantined or re-downloaded from a verified source.

---

## When to Use Sigcheck in AI Workflows

Use Sigcheck before running:
- YARA executables
- ClamAV Windows binaries
- Helper tools from GitHub
- Model conversion utilities
- Third-party scanning tools

This ensures your security tooling itself has not been compromised.

---

## Conclusion

While Sigcheck is not applied directly to model weights, it is essential for validating the integrity of the toolchain supporting AI model intake and red teaming.
Maintaining trusted binaries is a core control in a secure AI assurance pipeline.
