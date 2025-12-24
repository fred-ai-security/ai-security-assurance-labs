# Static Analysis for AI Model Security

This section documents static analysis methods used to evaluate AI model files and related artifacts before execution or deployment. 

Static analysis is performed during early intake stages and prior to any model execution or red-teaming activity.

Static analysis helps identify:

- Malware embedded in model weights  
- Suspicious or malformed file structures  
- Hidden payloads inside formats such as safetensors or GGUF  
- Supply-chain tampering  
- Integrity or authenticity issues  

Static analysis is a core early-stage control in AI model intake workflows.

---

## Tools Used

### **YARA**  
Pattern-matching engine used to detect suspicious strings, metadata indicators, and malware signatures within model directories.

### **ClamAV**  
Signature-based malware scanner used to detect known malicious patterns or unwanted binaries in AI model folders.

### **SHA-256 Hashing**  
Cryptographic hashing used to establish file integrity, verify provenance, and compare files against trusted source values.

---

## Modules in This Section

- **`hashing/`** – SHA-256 hashing and integrity verification workflows.
- **`clamav/`** – Malware scanning using ClamAV with example commands and outputs.
- **`yara/`** – Pattern-based detection using YARA rules for suspicious model artifacts.
- **`sigcheck/`** – Binary signature verification for security tooling and executables.

Note: Only example commands, templates, and synthetic outputs are stored here. 
No real model artifacts, hashes, or scan logs are committed to this repository.

