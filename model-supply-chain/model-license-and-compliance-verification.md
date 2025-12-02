# Model Licensing & Compliance Verification  
### Ensuring Legal, Ethical, and Governance-Aligned Model Usage

License and compliance verification is a mandatory component of AI supply-chain security.  
It ensures that any AI model you download, test, or integrate is being used **legally, ethically, and within the terms defined by the provider**.

This module prevents legal, reputational, and operational risks arising from:

- Unauthorized model usage  
- License violations  
- Misuse of restricted models  
- Commercial use violations  
- Redistribution violations  
- Compliance failures under governance frameworks  

This work aligns with:

- **NIST AI RMF — Govern / Map**
- **ISO/IEC 42001 — Responsible AI Requirements**
- **AI Act (EU) Transparency & Licensing Requirements**
- **MITRE ATLAS — Legal/Ethical Risks**
- **Industry Responsible AI Best Practices**

---

## 🔐 Why Licensing Verification Matters

Model licenses define what you can and cannot do, including:

- Commercial use  
- Redistribution  
- Modification  
- Fine-tuning  
- Hosting or API use  
- Benchmark publishing  
- Safety testing permissions  

Violating a license can result in:

❌ Legal exposure  
❌ DMCA violations  
❌ Financial penalties  
❌ GitHub repo takedowns  
❌ Loss of enterprise trust  

A professional AI Security Engineer **must validate licensing before model intake**.

---

# ✔️ 1. Identify the Model License Type

Models typically fall into these categories:

### **Permissive Licenses (safer for business use)**
- Apache 2.0  
- MIT  
- BSD  
- CC-BY  

**Allowed:** commercial use, modification, redistribution (with notices)

### **Restrictive / Research-Only Licenses**
- LLAMA 2 License (research/commercial restrictions)
- LLAMA 3 License
- Mistral Research License
- Falcon TII License

**May restrict:**
- Commercial use  
- API deployment  
- Redistribution  
- Benchmarks  

### **Highly Restrictive Licenses**
- NC (Non-commercial)  
- No-weights / no-distribution licenses  
- Copyright-protected training data  

**Often prohibits:**
- Business use  
- Hosting  
- Derivative models  

---

# ✔️ 2. Validate License Alignment With Intended Use

Confirm that the license permits the usage category:

| Intended Use | Common Restrictions |
|--------------|---------------------|
| **Commercial Deployment** | Many research licenses forbid this |
| **Fine-tuning** | Some licenses restrict modifications |
| **Redistribution** | Many forbid reposting weights |
| **Benchmark Publishing** | Some prohibit public eval results |
| **Enterprise Integration** | Must pass compliance + legal review |
| **Model Red Teaming** | Some licenses *require disclosure* |

If your use case is **not allowed**, the model must be rejected at intake.

---

# ✔️ 3. Validate License Location & Authenticity

Check all license locations:

- HuggingFace model card “License” field  
- LICENSE file in repo  
- GitHub release license  
- Provider documentation  
- Provider website  
- Terms of Use / Acceptable Use Pages  

**Red Flags:**
- No license provided  
- License contradicts model card  
- Forked model with a *different* license  
- Missing terms for weights redistribution  

If the license is ambiguous → classify as **“High Risk / Reject”**.

---

# ✔️ 4. Validate License Obligations

For each model, capture required obligations:

### Examples:

**Apache 2.0**
- Must include copyright notice  
- Must include LICENSE file  

**LLAMA licenses**
- You must disclose fine-tuning  
- No re-hosting weights  
- Restriction on >700M user companies  

**NC Licenses**
- No commercial use  

**Custom Licenses**
- May include red teaming disclosure clauses  
- May restrict certain benchmark reporting  
- May prohibit security testing  

Your intake workflow must enforce these terms.

---

# ✔️ 5. Validate Export Controls & Geo Restrictions

Some models are restricted by:

- U.S. EAR export controls  
- EU AI Act  
- Country-specific embargoes  
- Provider geo-blocking  

If a license forbids use in certain jurisdictions, document it.

---

# ✔️ 6. Validate License Against Model Card & SBOM

Cross-check:

| Check | Meaning |
|-------|---------|
| **License in model card matches LICENSE file?** | avoids mismatches |
| **SBOM contains only components allowed by license?** | prevents linking prohibited code |
| **Dependencies under permissible open-source licenses?** | no GPL contamination |
| **Model card disclaimers match license obligations?** | documentation alignment |

If ANY mismatch occurs, treat as a **license compliance failure**.

---

# ✔️ 7. Create a License & Compliance Record (Template Only)

A license evaluation record is required for audit and governance.

(Stored separately — you will **not** upload real model details.)

See the template in:  
`model-license-evaluation-template.md`

---

# 🗂️ Where This File Goes

```
ai-security-assurance-labs/
└── model-supply-chain/
      └── model-license-and-compliance-verification.md
```

---

# ✅ Conclusion

This module demonstrates your ability to:

- Perform responsible AI license verification  
- Detect legal and compliance risks  
- Validate alignment with intended use  
- Identify unsafe or prohibited redistribution  
- Ensure enterprise-grade governance  
- Build audit-ready documentation  

This is a core competency for AI Security, Governance, and Assurance roles.

