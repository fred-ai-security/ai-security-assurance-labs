# SBOM Generation and Vulnerability Scanning

## Supply-Chain Dependency Analysis Using Syft and Grype

This document defines the SBOM generation and vulnerability scanning process applied during AI model supply-chain intake. The objective is to surface dependency-level risk that static file analysis alone does not capture — including known CVEs in bundled libraries, licensing conflicts, and unexpected binary components.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MAP 1.5, MEASURE 2.2 — dependency risk identification and artifact integrity |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; supply-chain artifact integrity |
| ISO/IEC 42001 | Clause 8 — AI system operation and dependency control |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SI-7 — Software and Information Integrity |

---

## Toolchain

| Tool | Purpose | Output Format |
|---|---|---|
| Syft | SBOM generation from model artifacts and project directories | CycloneDX JSON / SPDX JSON |
| Grype | CVE vulnerability scanning against SBOM artifacts | JSON / text report |

---

## Workflow

1. Generate an SBOM from the model artifact or project directory using Syft
2. Scan the SBOM for known CVEs using Grype
3. Review findings against severity thresholds and artifact relevance
4. Document accepted risks, mitigations, or rejection decisions
5. Store outputs as evidence artifacts alongside intake documentation

---

## Evidence Artifacts

The following outputs are produced and stored locally for each assessed artifact:

- `sbom.cyclonedx.json` or `sbom.spdx.json` — full dependency inventory
- `grype-results.json` or `grype-results.txt` — CVE scan results
- `scan-summary.md` — summary of key findings and disposition decisions

Real scan outputs are stored in the local assessment environment and are not committed to this repository.

---

## Findings Interpretation

When reviewing SBOM and vulnerability scan results, analysis focuses on:

- **Severity threshold:** High and Critical CVEs are prioritized for immediate review
- **Relevance assessment:** Whether vulnerable packages are actually reachable or exercised by the artifact
- **Licensing conflicts:** Dependencies with restrictive or incompatible licenses flagged for compliance review
- **Unexpected components:** Undocumented binaries or scripts present in the artifact directory
- **Disposition:** Whether findings warrant mitigation, operational restrictions, or model rejection

---

## Accepted Risk Documentation

Where CVEs cannot be remediated due to hard-pinned dependencies or tool architecture constraints, findings are documented as accepted risks with full justification. Examples from this lifecycle:

| Risk ID | Component | CVE Severity | Justification |
|---|---|---|---|
| AR-001 | litellm 1.82.6 | Critical + High | Hard-pinned by Garak 0.14.1; upgrading breaks the assessment toolchain. Accepted with monitoring. |
| AR-002 | ffmpeg 8.0.1 | Critical | Binary embedded inside venv; not resolvable via pip or apt within venv scope. Accepted with documentation. |

Accepted risks are reviewed at each assessment cycle and re-evaluated if toolchain updates become available.

---

## Scan Summary Template

A structured summary is produced for each scan to support findings documentation and governance review.

```markdown
# SBOM Scan Summary

**Model / Artifact:**  
**Scan Date:**  
**Syft Version:**  
**Grype Version:**  
**SBOM Format:**  

## Findings Summary

| Severity | Count |
|---|---|
| Critical | |
| High | |
| Medium | |
| Low | |

## Key Findings

-  
-  

## Accepted Risks

-  

## Disposition

Approved / Approved with Conditions / Rejected

**Reviewed By:** Frederick Baffour  
**Notes:**  
```
