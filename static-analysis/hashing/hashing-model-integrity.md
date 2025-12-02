# Model Integrity Verification Using SHA-256 Hashing

This document explains how to use SHA-256 hashing to verify the integrity of AI model files such as `.gguf`, `.safetensors`, tokenizer files, and supporting assets.  
Hashing ensures that files have not been modified, tampered with, or corrupted during download, transfer, or storage.

---

## Why Hashing Matters in AI Model Security

Hashing provides a reliable way to detect:

- Silent model corruption  
- Supply-chain tampering  
- Replacement of model files with malicious versions  
- Accidental modification of files  
- Unexpected changes between testing stages  

Hashes act as a **fingerprint** for every model artifact.

If a hash changes — the file has changed.

Hashing is used during:

1. **Stage 1 – Model Intake**  
2. **Stage 2 – Pre-execution validation**  
3. **Before red teaming**  
4. **Before deployment**  
5. **Continuous monitoring**

---

## Generating SHA-256 Hashes in PowerShell

To hash a single model file:

```
Get-FileHash "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" -Algorithm SHA256
```

Example output:

```
Algorithm : SHA256
Hash : 64A1F1C338BD982F19352D0D321FA74E15E77294C8E47A31A5E6BC8F39C1A22A
Path : C:\AI_SECURITY_LABS\stage1_intake\model.gguf
```

---

## Hashing All Files in the Intake Directory

To hash all model artifacts in a directory:

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Format-Table Path, Hash
```

This produces a table with each file’s path and hash.

---

## Creating a Hash Manifest File

A “manifest” is a documented list of expected hashes for later comparison.

Create one using:

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Export-Csv "C:\AI_SECURITY_LABS\hash_manifest.csv" -NoTypeInformation
```

This file should be:

- Stored in a safe location  
- Saved in your GitHub repo if appropriate  
- Used to validate model integrity across time  

---

## Verifying Model Integrity Using the Manifest

To verify files against the manifest:

```
$manifest = Import-Csv "C:\AI_SECURITY_LABS\hash_manifest.csv"

foreach ($entry in $manifest) {
$current = Get-FileHash $entry.Path -Algorithm SHA256
if ($current.Hash -ne $entry.Hash) {
Write-Host "❌ Integrity failure: $($entry.Path)" -ForegroundColor Red
} else {
Write-Host "✔ OK: $($entry.Path)" -ForegroundColor Green
}
}
```

This compares real-time file hashes to the known-good manifest.

---

## Interpreting Results

### ✔ Matching Hashes
The file is unchanged and safe to proceed.

### ❌ Hash Mismatch
Indicates possible:

- Model tampering  
- Corruption  
- Malicious replacement  
- Incomplete download  
- Unexpected modification  

If a mismatch occurs:

- Quarantine the affected file  
- Re-download from the official provider  
- Investigate for supply-chain compromise  

---

## Best Practice: Store Hashes with the Model

For every model downloaded, store:

- The raw file  
- The SHA-256 hash  
- Source URL  
- Date acquired  
- Tool used to download (HuggingFace CLI, Ollama, etc.)

This creates strong supply-chain transparency.

---

## Conclusion

SHA-256 hashing is a foundational component of AI model integrity verification.  
When combined with ClamAV, YARA, and Sigcheck, hashing forms a complete and layered static analysis pipeline that helps prevent tampered or malicious models from entering your AI environment.

This practice aligns with industry expectations for AI Security Assurance and demonstrates a mature, evidence-based approach to model supply-chain verification.
