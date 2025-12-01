# Static Analysis for AI Model Security

This section documents static analysis techniques used to evaluate AI model files and related artifacts before running or deploying them. Static analysis helps identify:

- Malware embedded in model weights  
- Suspicious file structures  
- Hidden payloads (e.g., inside safetensors or GGUF files)  
- Supply-chain tampering  
- Integrity or authenticity issues  

Static analysis is one of the earliest and most important steps in AI model intake workflows.

## Tools Used

### 🔹 YARA  
Used to scan model directories for suspicious strings, patterns, and malware signatures.

### 🔹 ClamAV  
Used to detect malware, unwanted files, or suspicious binaries inside model folders.

### 🔹 SHA256 Hashing  
Used to verify integrity and compare downloaded model files against trusted values.

## Subdirectories

- `yara-rules-example.md` – Example of using YARA rules to scan model artifacts.  
- `clamav-scan-example.md` – Example results and commands for running ClamAV.  
- `hashing-and-integrity.md` – Demonstration of verifying file integrity using SHA256 hashing.
