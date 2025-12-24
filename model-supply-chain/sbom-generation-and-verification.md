# Software Bill of Materials (SBOM) for AI Model Supply-Chain Security

A Software Bill of Materials (SBOM) is an inventory of all components contained within a software or AI model package.  
Within AI Security Assurance, SBOMs increase visibility into:

- Model architecture metadata  
- Tokenizer components  
- Embedded libraries and runtimes  
- Dependencies and transitive dependencies  
- Build information and version lineage  
- Known vulnerabilities (CVE mapping)

SBOM generation enables traceability, accurate documentation, and detection of dependency-level supply-chain risks.

This approach reflects practices commonly used in enterprise AI security programs and aligns with guidance such as NIST AI RMF, SSDF, and related supply-chain security standards.

---

## 1. Purpose of SBOMs for AI Models

AI models commonly include:

- Tokenizer vocabulary and merges  
- Pre- and post-processing scripts  
- Embedded shared libraries (`.dll`, `.so`, `.dylib`)  
- Native operators and computation kernels  
- Dataset or corpus metadata  
- Quantized or fused representations  
- Build metadata from training or export pipelines  

An SBOM supports identification of:

- Suspicious embedded binaries  
- Dependencies with known CVEs  
- Unauthorized or hidden components  
- Version drift between releases  
- Unexpected or undocumented build artifacts  

SBOMs transform model artifacts from a black-box format into a verifiable, auditable structure.

---

## 2. Required Components of an AI Model SBOM

A complete SBOM contains:

### **Model Artifact Inventory**
- `model.gguf`  
- `model.safetensors`  
- Tokenizer artifacts  
- Configuration files  
- Vocabulary and merge files  
- Native ops or auxiliary binaries  

### **Metadata**
- Model name, version, and provider  
- Release dates  
- License  
- Build environment details  

### **Dependencies**
- Python libraries  
- Tokenizer dependencies  
- Native libraries  
- Compression or packaging modules  

### **Security Fields**
- SHA-256 hashes  
- File sizes  
- Expected vs. actual file list  
- CVE mapping for discovered dependencies  

---

## 3. Tools Used for SBOM Generation and Review

AI model artifacts differ from traditional software packages, so SBOM generation focuses on file inventory, embedded components, and metadata rather than executable behavior.

Tools such as Syft are used to generate a file-level SBOM, capturing artifacts, libraries, and packaging details. Vulnerability analysis tools (e.g., Grype) are then used to assess discovered components for known issues.

The emphasis is on evidence collection and review, not on tool installation or automation.

---

## 4. SBOM Verification Workflow

1. **Generate File Inventory** using Syft.  
2. **Extract Internal Metadata** from GGUF or safetensors files.  
3. **Complete Hash Verification** against integrity manifests.  
4. **Compare Expected File Structure** with actual content.  
5. **Perform CVE scanning using a vulnerability analysis tool such as Grype.** using a vulnerability analysis tool (e.g., Grype).
6. **Map SBOM Components to Model Card** and verify accuracy.  
7. **Store Only SBOM Templates** (no real model data) in repository.

This process validates both technical and governance-level integrity.

---

## 5. Example SBOM Structure (Synthetic)

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

## 6. SBOM Validation Summary (Template)

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

## 7. File Location

```
ai-security-assurance-labs/
└── model-supply-chain/
      └── sbom-generation-and-verification.md
```

---

SBOM generation and verification provide a practical mechanism for documenting model contents, identifying supply-chain risks, and improving transparency during AI model intake and evaluation.

