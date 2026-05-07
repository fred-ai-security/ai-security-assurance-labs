# Model Licensing and Compliance Verification

## Legal, Ethical, and Governance-Aligned Model Usage

This document covers the structured approach used to verify licensing and compliance requirements during AI model intake. The objective is to ensure models are used in accordance with legal, ethical, and governance-defined constraints established by the provider and applicable regulatory standards.

The verification process addresses risks related to:

- Unauthorized model usage
- Violations of license terms
- Improper redistribution of model weights
- Use of restricted models in commercial environments
- Non-compliance with responsible AI governance frameworks

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | GOVERN 1.1, MAP 1.5 — legal constraints, usage governance, and documentation |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise |
| OWASP LLM Top 10 (2025) | LLM09 — Misinformation; supply-chain documentation integrity |
| ISO/IEC 42001 | Clause 8 — Responsible AI requirements and operational constraints |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SR-4 — Provenance |
| EU AI Act | Transparency and licensing obligations for high-risk AI systems |

---

## Licensing as a Supply-Chain Control

Model licenses define permissible usage, including:

- Commercial deployment
- Redistribution
- Modification and fine-tuning
- API hosting and service integration
- Benchmark publication
- Security and safety testing

Improper or unauthorized use creates exposure to:

- Copyright or DMCA violations
- Contractual breaches
- Financial penalties
- Takedown notices
- Enterprise compliance failures

Licensing verification is a required step in supply-chain intake — models with ambiguous, missing, or non-compliant licenses are not approved for progression.

---

## 1. Identify the Model License Type

Model licenses fall into three primary categories:

### Permissive Licenses
Examples: Apache 2.0, MIT, BSD, CC-BY

These licenses typically permit modification, redistribution, and commercial usage when attribution requirements are met.

### Restrictive or Research-Only Licenses
Examples: Llama 2 License, Llama 3 License, Mistral Research License, Falcon TII License

These licenses often include restrictions on:

- Commercial deployment
- API hosting
- Re-use of weights
- Fine-tuning disclosures
- Redistribution

### Highly Restrictive Licenses
Examples: Non-commercial (NC) licenses, no-weights redistribution terms, jurisdiction-specific licenses

These licenses may prohibit commercial usage, derivative works, or redistribution entirely.

---

## 2. Validate License Alignment With Intended Use

License terms are evaluated against intended usage including:

- Commercial deployment
- Enterprise integration
- Fine-tuning or derivative work creation
- Internal or external redistribution
- Publication of benchmarks or safety evaluation results
- Security testing and red teaming

When license terms and intended usage conflict, the model is not approved for intake.

---

## 3. Validate License Location and Authenticity

License information is confirmed across all available sources:

- Model card "License" field
- LICENSE file in the repository
- GitHub release materials
- Provider documentation and website Terms of Use

**Indicators requiring further review:**

- Missing license information
- Contradictions between the model card and LICENSE file
- Forked repositories presenting altered licensing terms
- Lack of clarity on redistribution permissions

Ambiguous licensing constitutes a compliance risk and is documented as a finding.

---

## 4. Validate License Obligations

Each license type includes specific obligations that must be documented:

| License | Key Obligations |
|---|---|
| Apache 2.0 | Preservation of copyright notices; inclusion of LICENSE file |
| Llama Family | Fine-tuned model disclosure; redistribution restrictions; large-scale deployment constraints |
| Non-Commercial | Prohibition of commercial use in any form |
| Custom / Provider-Specific | Red-teaming disclosure conditions; benchmark publication restrictions; deployment prohibitions |

Obligations are recorded for audit and governance review.

---

## 5. Validate Export Controls and Geographic Restrictions

Some models are subject to:

- U.S. Export Administration Regulations (EAR)
- Jurisdiction-specific access restrictions
- Provider geo-blocking or usage limitations

Any regional or export constraints are recorded as part of intake documentation.

---

## 6. Validate Licensing Against Documentation and SBOM

Licensing information is cross-checked against model documentation and SBOM artifacts to ensure supply-chain consistency.

Key checks include:

- Alignment between LICENSE file and model card license field
- Validation that SBOM components comply with permissible licensing
- Verification that dependencies do not carry restrictive or incompatible licenses
- Consistency between documentation and licensing obligations

Any mismatch between these elements constitutes a potential compliance risk and is flagged for review.

---

## 7. License and Compliance Record

A record template is maintained to support internal audit and governance documentation. Only the template structure is stored in this repository — completed assessment records remain in the local assessment environment.

See: `model-license-evaluation-template.md`
