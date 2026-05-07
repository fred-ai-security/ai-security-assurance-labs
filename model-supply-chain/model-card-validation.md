# AI Model Card Validation and Documentation Verification

This document covers the structured approach used to validate AI model documentation during supply-chain intake. The process confirms whether a downloaded model matches its official description and whether the associated documentation demonstrates transparency, consistency, and integrity prior to any assessment or deployment workflow.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | GOVERN 1.1, MAP 1.5, MEASURE 2.5 — documentation, transparency, and traceability |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise; AML.T0053 — Training Data Poisoning |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; LLM09 — Misinformation |
| ISO/IEC 42001 | Clause 8 — Documentation and transparency requirements |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SR-4 — Provenance |

---

## Model Card Validation as a Supply-Chain Control

Model cards communicate essential information, including:

- Purpose and intended use
- Limitations and unsafe failure modes
- Training data transparency
- Risk and mitigation statements
- Version history and lineage
- Licensing requirements
- Safety and evaluation results

Incomplete, misleading, or forged documentation can conceal:

- Bias and discrimination concerns
- Unsafe or untested behaviors
- Dataset integrity issues
- Manipulated or poisoned model versions
- Incorrect versioning or provenance gaps

Model card validation is a required step in supply-chain trust and safe deployment workflows.

---

## 1. Validate the Model Card Source

**Legitimate indicators:**

- Verified or organizational accounts
- Consistent release history
- Recognizable organizations (Meta, Google, Mistral, Cohere, Microsoft, NVIDIA, etc.)
- Regular updates and meaningful commit activity

**Red flags:**

- Newly created or unverified accounts
- Sparse or missing documentation
- Missing license
- Contradictions between files and model card
- No tags, no metadata, or incomplete sections

---

## 2. Validate Model Card Structure

A well-constructed model card contains the following:

| Section | Required | Purpose |
|---|---|---|
| Model Summary | ✔ Required | Identifies the model and its purpose |
| Intended Use | ✔ Required | Defines correct and incorrect usage contexts |
| Limitations | ✔ Required | Lists failure modes and safety risks |
| Training Data | Strongly Recommended | Supports data lineage review |
| Evaluation Results | Required for high-risk models | Documents performance against benchmarks |
| Ethical Considerations | Recommended | Notes fairness, bias, and misuse risks |
| Safety Tests | Required for LLMs | Shows jailbreak and safety evaluation evidence |
| Version History / Changelog | ✔ Required | Supports release lineage verification |
| License | ✔ Required | Defines legal and usage constraints |
| Model Architecture | Optional | Provides technical clarity |
| Parameters / Size | ✔ Required | Confirms expectations for file integrity |

Missing major sections indicate documentation gaps that require risk notation.

---

## 3. Validate Versioning and Release Lineage

Every legitimate model maintains:

- Clear version identifiers
- Structured release notes
- A changelog documenting updates
- Consistent versioning across the repository

**Integrity indicators:**

- Semantic versioning
- Tag-based releases
- Matching versions across filenames and metadata
- Stable release lineage

**Red flags:**

- Versions updated without changelog entries
- Large file differences between minor versions
- Sudden or unannounced changes
- New files appearing without explanation

---

## 4. Validate Licensing and Usage Restrictions

Key elements to verify:

- Presence of a license
- Clarity on commercial and redistribution rights
- Dataset-specific license constraints
- Restrictions or obligations on downstream use

**High-risk indicators:**

- Missing or ambiguous license
- Conflicting license terms
- Mismatch between repository license and model card
- Unauthorized re-licensing in forks

---

## 5. Validate Safety Disclosures and Limitations

Model cards should include disclosures covering:

- Unsafe or harmful behaviors
- Jailbreak vulnerabilities
- Prompt-injection susceptibility
- Bias and demographic risks
- High-risk domain limitations (medical, legal, financial, cybersecurity)
- Misuse and abuse scenarios
- Robustness limitations

Exaggerated or unrealistic claims of "complete safety" are a documentation integrity concern and should be flagged.

---

## 6. Validate Alignment Between Documentation and Artifacts

Model card information must match the downloaded files. Key fields to verify:

- Model size and parameter count
- Architecture type (Transformer, Mamba, MoE, etc.)
- File list (config, tokenizer, safetensors, GGUF, vocab files)
- Published hashes, where provided

**Verification points:**

- File sizes match official published values
- No additional undocumented binaries present
- Parameter count consistent with published architecture
- No inconsistencies between naming conventions and release version

*Example finding: a model card labeled "8B parameters" delivering a file size consistent with a 7B model — flagged as a provenance inconsistency.*

---

## 7. Validate Benchmarks and Evaluation Evidence

**Legitimate benchmarks include:**

- MT-Bench, TruthfulQA, MMLU, GSM8K, ARC
- Safety evaluations (OpenAI Eval, HELM, RAI test suites)

**Red flags:**

- Claims without supporting evidence
- Benchmarks contradicting known model capabilities
- "World-best" or absolute safety claims without citations
- No evaluation results provided for high-risk use cases

---

## 8. Validate Ethical, Bias, and Risk Disclosures

Models should document:

- Sensitive data handling concerns
- Hallucination tendencies and failure modes
- Fairness limitations and demographic harm risks
- Dual-use considerations and abuse potential

Absence of ethical or risk disclosures indicates low documentation completeness and should be recorded as a finding.

---

## Model Card Validation Summary Template

This template is used for recordkeeping during intake evaluations. Only the template structure is published here — completed assessment records remain in the local assessment environment.

```markdown
# Model Card Validation Summary

**Model Name:**  
**Provider:**  
**Source URL:**  
**Version:**  
**License:**  
**Intended Use:**  
**Limitations Listed:**  
**Safety Disclosures Present:** Yes / No  
**Benchmark Results Reviewed:** Yes / No  
**Training Data Transparency:** High / Medium / Low  
**Changelog Present:** Yes / No  
**Versioning Integrity:** Good / Concerning  
**File List Matches Model Card:** Yes / No  
**Hashes Published:** Yes / No  
**Risks Noted:**  
-  
-  

**Validated By:** Frederick Baffour  
**Notes:**  
```
