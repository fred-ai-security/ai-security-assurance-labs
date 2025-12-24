# Model Licensing and Compliance Verification  
### Legal, Ethical, and Governance-Aligned Model Usage

This module outlines a structured approach for verifying licensing and compliance requirements during AI model intake. The objective is to ensure that models are used in accordance with legal, ethical, and governance-defined constraints established by the model provider and applicable regulatory standards.

The verification process helps prevent legal, operational, and reputational risks related to:

- Unauthorized model usage  
- Violations of license terms  
- Improper redistribution of model weights  
- Use of restricted models in commercial environments  
- Non-compliance with responsible AI governance frameworks  

This module aligns with:

- NIST AI RMF — Govern / Map  
- ISO/IEC 42001 — Responsible AI requirements  
- EU AI Act transparency and licensing considerations  
- MITRE ATLAS — Legal and ethical risk components  
- Industry-aligned responsible AI practices  

---

## Importance of Licensing Verification

Model licenses define permissible usage, including:

- Commercial deployment  
- Redistribution  
- Modification and fine-tuning  
- API hosting and service integration  
- Benchmark publication  
- Security or safety testing  

Improper or unauthorized use can create exposure to:

- Copyright or DMCA violations  
- Contractual breaches  
- Financial penalties  
- Takedown notices  
- Enterprise compliance failures  

Licensing verification forms a foundational step in AI model supply-chain assessment.

---

## 1. Identify the Model License Type

Model licenses commonly fall into these categories:

### Permissive Licenses
Examples include:
- Apache 2.0  
- MIT  
- BSD  
- CC-BY  

These licenses typically permit modification, redistribution, and commercial usage when attribution requirements are met.

### Restrictive or Research-Only Licenses
Examples include:
- Llama 2 License  
- Llama 3 License  
- Mistral Research License  
- Falcon TII License  

These licenses often include restrictions related to:

- Commercial deployment  
- API hosting  
- Re-use of weights  
- Fine-tuning disclosures  
- Redistribution limitations  

### Highly Restrictive Licenses
Examples include:
- Non-commercial (NC) licenses  
- No-weights redistribution terms  
- Licenses tied to specific usage jurisdictions  

These licenses may prohibit commercial usage, derivative works, or redistribution entirely.

---

## 2. Validate License Alignment With Intended Use

License terms define whether a model can be used for purposes such as:

- Commercial deployment  
- Enterprise integration  
- Fine-tuning or derivative work creation  
- Redistribution within internal or external environments  
- Publication of benchmarks or safety evaluation results  
- Security testing or red-teaming  

When license terms and intended usage conflict, the model cannot be approved for intake.

---

## 3. Validate License Location and Authenticity

License information should be confirmed across all available sources:

- Model card “License” field  
- LICENSE file in the repository  
- GitHub release materials  
- Provider documentation  
- Provider website or Terms of Use  

Indicators requiring further review include:

- Missing license information  
- Contradictions between the model card and LICENSE file  
- Forked repositories presenting altered licensing terms  
- Lack of clarity on redistribution permissions  

Ambiguous licensing constitutes a compliance risk.

---

## 4. Validate License Obligations

Each license type can include specific obligations related to attribution, redistribution, or operational constraints.

Examples:

### Apache 2.0  
- Preservation of copyright notices  
- Inclusion of the Apache 2.0 LICENSE file  

### Llama Family Licenses  
- Disclosure requirements for fine-tuned model variants  
- Redistribution restrictions for model weights  
- Constraints associated with large-scale deployment  

### Non-Commercial Licenses  
- Prohibition of commercial use  

### Custom or Provider-Specific Licenses  
- Conditions related to red-teaming disclosures  
- Restrictions on benchmark publication  
- Prohibitions against specific forms of deployment  

Obligations must be documented for audit and governance.

---

## 5. Validate Export Controls and Geographic Restrictions

Some models fall under:

- U.S. Export Administration Regulations (EAR)  
- Jurisdiction-specific restrictions  
- Provider geo-blocking or access limitations  

Any regional constraints must be recorded as part of intake documentation.

---

## 6. Validate Licensing Against Documentation and SBOM

Cross-checking licensing information with model documentation enhances supply-chain integrity.

Key checks include:

- Alignment between LICENSE file and model card license field  
- Validation that SBOM components comply with permissible licensing  
- Verification that dependencies avoid restrictive or incompatible licenses  
- Consistency between documentation and licensing obligations  

Any mismatch between these elements constitutes a potential compliance risk.

---

## 7. License and Compliance Record Template

A record template is maintained to support internal audit and governance documentation. Only the template is stored in the repository.

See:  
`model-license-evaluation-template.md`

---

## Repository Location

```
ai-security-assurance-labs/
└── model-supply-chain/
    └── model-license-and-compliance-verification.md
```

---

## Summary

This module establishes a governance-aligned approach for validating AI model licensing during supply-chain intake. It supports assessment of license terms, evaluation of restrictions, verification of documentation consistency, and identification of compliance-related risks. The resulting documentation enables organizations to maintain legally compliant, ethically aligned, and auditable AI model usage.
