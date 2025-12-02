# Static Analysis for AI Model Security

This section documents static analysis methods used to evaluate AI model files and related artifacts before execution or deployment. Static analysis helps identify:

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

## Subdirectories

- **`yara-rules-example.md`** – Example YARA rule usage for scanning model artifacts.  
- **`clamav-scan-example.md`** – Example commands and output from a ClamAV scan.  
- **`hashing-and-integrity.md`** – Demonstration of computing and validating SHA-256 file hashes.

