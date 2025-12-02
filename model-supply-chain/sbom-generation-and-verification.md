# Software Bill of Materials (SBOM) for AI Model Supply-Chain Security

A Software Bill of Materials (SBOM) is a detailed inventory of all components inside a software or AI model package.  
For AI Security Assurance, SBOMs provide visibility into:

- Model architecture metadata  
- Tokenizer components  
- Embedded libraries or runtimes  
- Dependencies and transitive dependencies  
- Build information and version lineage  
- Known vulnerabilities (CVE mapping)

This module ensures models entering your environment are fully documented, traceable, and scanned against known risks — preventing dependency-level supply-chain attacks.

This aligns with:

- **NIST AI RMF — Govern / Map / Measure**  
- **NIST SP 800-218 Secure Software Development Framework (SSDF)**  
- **EO 14028 — Minimum SBOM Requirements**  
- **ISO/IEC 42001 — AI Management System**  
- **MITRE ATLAS — Supply Chain TTPs**

---

## 🔐 Why SBOMs Matter for AI Models

AI models increasingly contain:

- Tokenizer vocabularies  
- Pre/post-processing scripts  
- Embedded shared libraries (`.dll`, `.so`, `.dylib`)  
- Native ops & kernels  
- Dataset metadata  
- Build metadata  
- Quantized or fused binaries  

A model SBOM helps identify:

❌ Suspicious embedded binaries  
❌ Dependencies with known CVEs  
❌ Malicious or unauthorized components  
❌ Drift between model versions  
❌ Hidden build steps or unsafe scripts  

Without an SBOM, model artifacts become a **black box** — impossible to audit or verify.

---

## ✔️ 1. What Goes Into an AI Model SBOM

A complete AI model SBOM documents:

### **Model Artifact Inventory**
- `model.gguf`  
- `model.safetensors`  
- `tokenizer.model`  
- Config JSON files  
- Vocab / merges files  
- Native ops / kernels  

### **Metadata**
- Model name & version  
- Provider  
- Training/release dates  
- License  
- Build environment metadata  

### **Dependencies**
- Python libraries (if packaged)  
- Tokenizer dependencies  
- Native libraries  
- Compression/packaging formats  

### **Security Fields**
- SHA-256 hashes  
- File sizes  
- Expected vs actual file count  
- CVE mapping for dependencies  

---

## ✔️ 2. Tools for Generating SBOMs

AI models are not traditional executables — so multiple tools are recommended.

---

### **1. Syft (Anchore) — Best for File-Level SBOMs**

Detects:

- File inventory  
- Embedded libraries  
- Build metadata  
- Python/Conda packages  

**Install (Windows):**
```
choco install syft
```

**Generate SBOM (JSON):**
```
syft C:\AI_SECURITY_LABS\stage1_intake -o json > sbom.json
```

**CycloneDX (governance-compliant):**
```
syft C:\AI_SECURITY_LABS\stage1_intake -o cyclonedx-json > sbom-cdx.json
```

---

### **2. GGUF / Safetensors Internal Metadata**

These formats contain embedded metadata.

**GGUF:**
```
gguf-tools inspect model.gguf > gguf_metadata.txt
```

**Safetensors:**
```
python - << EOF
import safetensors
print("Metadata extraction coming soon...")
EOF
```

---

### **3. Trivy — CVE Scanning**
Scans folder for vulnerable libraries.

```
trivy fs C:\AI_SECURITY_LABS\stage1_intake > vulnerability_report.txt
```

---

## ✔️ 3. SBOM Verification Workflow

1. **Generate File Inventory (Syft)**  
   Identify all files + metadata.

2. **Extract Internal Metadata**  
   Compare GGUF / safetensors metadata to the model card.

3. **Perform Hash Verification**  
   Ensure SBOM hashes match `hash_manifest.csv`.

4. **Compare Against Expected Model Structure**  
   - File count  
   - File type  
   - File size  

5. **Perform CVE Scan (Trivy)**  
   Identify vulnerable or risky dependencies.

6. **Match SBOM Components to the Model Card**  
   Ensure no undocumented files or suspicious binaries.

7. **Store SBOM Artifact**  
   Only store **templates** in GitHub — never real model data.

---

## ✔️ 4. Example SBOM Structure (Synthetic)

*(No real model data — safe for GitHub)*

```json
{
  "model": {
    "name": "Llama 3.1 8B",
    "version": "8B-instruct",
    "provider": "meta-llama",
    "license": "LLAMA3 License"
  },
  "artifacts": [
    {
      "file": "model.gguf",
      "hash_sha256": "ABC123...",
      "size": "4.92 GB"
    },
    {
      "file": "tokenizer.model",
      "hash_sha256": "DEF456...",
      "size": "32 MB"
    }
  ],
  "dependencies": [
    {
      "name": "sentencepiece",
      "version": "0.1.99",
      "cve": null
    }
  ],
  "security": {
    "unexpected_binaries": [],
    "cve_findings": []
  }
}
```

---

## 📄 SBOM Validation Summary Template (Store the Template Only)

```
# SBOM Validation Summary (Template)

**Model Name:**  
**Provider:**  
**Version:**  
**Source URL:**  
**SBOM File:** sbom.json / sbom-cdx.json  
**Hash Verification:** Pass / Fail  
**Unexpected Components:** Yes / No  
**CVE Scan Performed:** Yes / No  
**High-Risk Findings:**  
-  
-  
**Metadata Matches Model Card:** Yes / No  
**Notes:**  

**Validated By:** Frederick Baffour
```

---

## 🗂️ Where This File Goes

```
ai-security-assurance-labs/
└── model-supply-chain/
      └── sbom-generation-and-verification.md
```

---

## ✅ Conclusion

This module demonstrates a professional, governance-grade approach to AI model SBOM generation and verification.  
It ensures component transparency, detects hidden risks, and strengthens AI supply-chain security by aligning with modern compliance frameworks such as NIST AI RMF, ISO 42001, and EO 14028.

---

