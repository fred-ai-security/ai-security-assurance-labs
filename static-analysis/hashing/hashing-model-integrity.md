# Model Integrity Verification Using SHA-256 Hashing

This document describes how SHA-256 hashing is used to verify the integrity of AI model files, including `.gguf`, `.safetensors`, tokenizer files, and related assets.  
Hashing ensures that files have not been modified, tampered with, or corrupted during download, transfer, or storage.

---

## Importance of Hashing in AI Model Security

Cryptographic hashing provides a reliable method to detect:

- Silent file corruption  
- Supply-chain tampering  
- Replacement of model artifacts with malicious versions  
- Accidental modification  
- Unexpected drift between evaluation stages  

A SHA-256 hash serves as a unique fingerprint for each artifact.  
If a file’s hash changes, the file itself has changed.

Hash verification is typically performed at multiple points, including:

- Stage 1 — Model Intake  
- Stage 2 — Pre-execution validation  
- Red-teaming preparation  
- Deployment readiness checks  
- Ongoing monitoring and provenance validation  

---

## Generating SHA-256 Hashes in PowerShell

To hash a single file:

```
Get-FileHash "C:\AI_SECURITY_LABS\stage1_intake\model.gguf" -Algorithm SHA256
```

Example output:

```
Algorithm : SHA256
Hash      : 64A1F1C338BD982F19352D0D321FA74E15E77294C8E47A31A5E6BC8F39C1A22A
Path      : C:\AI_SECURITY_LABS\stage1_intake\model.gguf
```

---

## Hashing All Files in a Directory

To generate hashes for all artifacts in an intake directory:

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Format-Table Path, Hash
```

This produces a structured table of each file and its SHA-256 fingerprint.

---

## Creating a Hash Manifest

A hash manifest documents the expected hash values for future verification.

```
Get-ChildItem "C:\AI_SECURITY_LABS\stage1_intake" |
Get-FileHash -Algorithm SHA256 |
Export-Csv "C:\AI_SECURITY_LABS\hash_manifest.csv" -NoTypeInformation
```

The manifest acts as a reference point to ensure artifacts remain unchanged across stages such as intake, validation, testing, and deployment.

---

## Verifying Files Against the Manifest

To verify model integrity using the stored manifest:

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

This loop compares real-time file hashes to known-good values.

---

## Interpreting Verification Results

### Matching Hashes  
Indicate that the file is unchanged and consistent with the expected state.

### Mismatched Hashes  
Suggest possible:

- Tampering  
- File corruption  
- Malicious replacement  
- Partial or failed downloads  
- Unauthorized modification  

Impacted files should be quarantined, re-acquired from a trusted source, and investigated for supply-chain compromise.

---

## Best Practices for Integrity Evidence

For each model acquired, maintain:

- Model file(s)  
- SHA-256 hash values  
- Source URL  
- Date and method of acquisition  
- Manifest file used in later verification steps  

This supports provenance tracking and audit requirements within AI governance programs.

---

## Conclusion

SHA-256 hashing is a foundational component of AI model integrity verification.  
Combined with YARA, ClamAV, and Sigcheck, hashing enables a layered static analysis approach that reduces the risk of introducing tampered or malicious artifacts into AI evaluation or deployment pipelines.  
This aligns with industry expectations for robust AI Security Assurance and modern supply-chain risk management.

