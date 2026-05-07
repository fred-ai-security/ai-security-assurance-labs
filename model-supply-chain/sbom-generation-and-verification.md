# Software Bill of Materials (SBOM) for AI Model Supply-Chain Security

A Software Bill of Materials (SBOM) is an inventory of all components contained within a software or AI model package. Within AI Security Assurance, SBOMs increase visibility into:

- Model architecture metadata
- Tokenizer components
- Embedded libraries and runtimes
- Dependencies and transitive dependencies
- Build information and version lineage
- Known vulnerabilities (CVE mapping)

SBOM generation provides traceability, accurate documentation, and detection of dependency-level supply-chain risks that static file analysis alone does not surface.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MAP 1.5, MEASURE 2.2 — dependency traceability and artifact integrity |
| NIST SSDF | PW.4 — Reuse existing, well-secured software; RV.1 — Vulnerability identification |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; supply-chain integrity |
| ISO/IEC 42001 | Clause 8 — AI system operation and dependency control |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SI-7 — Software and Information Integrity |

---

## 1. Purpose of SBOMs for AI Models

AI models commonly include:

- Tokenizer vocabulary and merge files
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

**Model Artifact Inventory:**
- `model.gguf` or `model.safetensors`
- Tokenizer artifacts and vocabulary files
- Configuration files
- Native ops or auxiliary binaries

**Metadata:**
- Model name, version, and provider
- Release dates and license
- Build environment details

**Dependencies:**
- Python libraries and tokenizer dependencies
- Native libraries and compression or packaging modules

**Security Fields:**
- SHA-256 hashes and file sizes
- Expected vs. actual file list comparison
- CVE mapping for discovered dependencies

---

## 3. Toolchain

Syft is used to generate a file-level SBOM, capturing artifacts, libraries, and packaging metadata from model artifact directories. Grype is then applied to assess discovered components against known CVE databases.

| Tool | Role | Output |
|---|---|---|
| Syft | SBOM generation | CycloneDX JSON / SPDX JSON |
| Grype | CVE vulnerability scanning | JSON / text report |

---

## 4. SBOM Verification Workflow

1. Generate file inventory using Syft
2. Extract internal metadata from GGUF or safetensors files
3. Complete hash verification against integrity manifests
4. Compare expected file structure with actual artifact content
5. Perform CVE scanning using Grype against the generated SBOM
6. Map SBOM components to model card and verify consistency
7. Document findings, accepted risks, and disposition decisions

---

## 5. Example SBOM Structure (Synthetic)

The following is a synthetic example illustrating SBOM structure — real scan outputs are stored locally and not committed to this repository.

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

## 6. SBOM Validation Summary Template

```markdown
# SBOM Validation Summary

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
