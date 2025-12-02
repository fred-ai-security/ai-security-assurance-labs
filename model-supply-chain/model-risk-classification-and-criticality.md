# AI Model Risk Classification & Criticality Assessment
### A Governance-Grade Module for AI Supply-Chain Security

Model Risk Classification determines how risky an AI model is based on:

- What it will be used for  
- How it behaves  
- How exposed it is to adversarial misuse  
- The harm it could cause  
- How consequential failures might be  

This module is aligned with:

- NIST AI RMF  
- ISO/IEC 42001  
- MITRE ATLAS  
- Enterprise AI Governance standards  

It demonstrates your ability to perform professional AI risk triage.

---

# 🔐 Why Model Risk Classification Matters

AI models can introduce significant risks, including:

- Harmful or toxic outputs  
- Biased or discriminatory decisions  
- Jailbreak or prompt-injection exploitation  
- Data leakage or unintentional disclosures  
- Unsafe domain guidance (medical/legal/finance)  
- Agentic misbehavior in automation  
- High-impact hallucinations  

Risk classification helps determine:

✔ Required security controls  
✔ Required level of red teaming  
✔ Deployment safety level  
✔ Governance and compliance requirements  
✔ Whether the model can be approved at all  

---

# 🧩 1. Model Context & Intended Use Analysis

### Evaluate the following:

| Category | Key Questions |
|---------|---------------|
| **Domain** | Is the model used in finance, healthcare, hiring, legal, safety-critical systems? |
| **User Impact** | Could model outputs directly affect individuals? |
| **Automation Level** | Advisory only, or fully autonomous decision-making? |
| **Data Sensitivity** | Does it process PII, PHI, or restricted data? |
| **Audience** | Internal use? End users? Public usage? |

### High-Risk Indicators

- High-impact domain  
- Sensitive or regulated data  
- Human-independent automation  
- Public-facing access  
- Safety-critical outputs  

---

# 🧠 2. Harm Likelihood Scoring (NIST AI RMF)

Score how likely the model is to cause harm even when used correctly.

| Score | Likelihood | Description |
|-------|------------|-------------|
| **1** | Low | Minimal risk of harmful behavior. |
| **2** | Medium | Harm possible with certain prompts or misuse. |
| **3** | High | Harm is likely due to model design or training data. |

Factors include:

- Hallucination rate  
- Tendency for unsafe outputs  
- Toxicity generation  
- Confident but incorrect outputs  

---

# 🔓 3. Exploitability & Misuse Exposure

How easily can the model be abused?

| Score | Exposure | Description |
|-------|----------|-------------|
| **1** | Low | Internal-only, controlled access. |
| **2** | Medium | Restricted but shared environment. |
| **3** | High | Public-facing, API access, broad exposure. |

Indicators include:

- API-based access  
- Lack of guardrails  
- Visible system prompts  
- Jailbreak susceptibility  

---

# ⚠️ 4. Severity of Harm

If something goes wrong, how bad is it?

| Score | Severity | Examples |
|-------|----------|----------|
| **1** | Low | Minor errors, no real-world impact. |
| **2** | Medium | Misleading info, reputational impact, user confusion. |
| **3** | High | Physical harm, legal exposure, financial loss, discrimination. |

Examples of high severity:

- Medical misinformation  
- Financial fraud enablement  
- Highly biased or discriminatory outputs  
- Dangerous instructions  

---

# 🧮 5. AI Model Risk Matrix

Combine the three scores:

| Likelihood | Exploitability | Severity | Result |
|------------|----------------|----------|--------|
| 1 | 1 | 1–2 | **Low** |
| 1–2 | 1–2 | 2 | **Medium** |
| 2–3 | 2–3 | 2–3 | **High** |
| 3 | 3 | 3 | **Critical** |

### Risk Levels:
- **Low:** Basic controls  
- **Medium:** Static analysis + targeted red teaming  
- **High:** Full supply-chain + extensive red teaming + governance review  
- **Critical:** Deployment restricted or requires executive approval  

---

# 🛡️ 6. Criticality Classification (Tiering)

### **Tier 1 — High Criticality**
Used in:

- Healthcare  
- Finance  
- Legal/Judicial  
- Hiring/HR  
- Safety-critical automation  
- Autonomous agents  

Controls required:

✔ Full supply-chain analysis  
✔ Full red teaming (Garak, Promptfoo)  
✔ Governance sign-off  
✔ Continuous monitoring  

---

### **Tier 2 — Medium Criticality**
Common in:

- Customer support  
- Content generation  
- Internal knowledge tools  
- Summaries / productivity tasks  

Controls required:

✔ Static analysis  
✔ Partial red teaming  
✔ Risk documentation  

---

### **Tier 3 — Low Criticality**
Used for:

- Personal or research models  
- Experimental use  
- Non-sensitive internal tools  

Controls required:

✔ Basic intake validation  
✔ Hashing + provenance only  

---

# 📄 Model Risk Classification Summary Template

_Store the template only — no real model data._

```
# Model Risk Classification Summary (Template)

**Model Name:**  
**Provider:**  
**Version:**  
**Intended Use:**  
**Domain:**  
**User Impact:**  
**Data Sensitivity:**  
**Automation Level:**  
**Deployment Context:**  

### Risk Scoring
**Harm Likelihood:** Low / Medium / High  
**Exploitability:** Low / Medium / High  
**Severity of Harm:** Low / Medium / High  

### Overall Risk Level:
Low / Medium / High / Critical

### Criticality Tier:
Tier 1 / Tier 2 / Tier 3

**Justification Notes:**  
-  
-  
-  

**Validated By:** Frederick Baffour
```

---

# 📁 File Location

```
ai-security-assurance-labs/
└── model-supply-chain/
      └── model-risk-classification-and-criticality.md
```

---

# ✅ Conclusion

This module proves that you understand:

- AI risk management  
- Mapping model risks to governance controls  
- NIST AI RMF harm likelihood & severity  
- Criticality tiering  
- Deployment decision-making  
- Real-world enterprise AI assurance  

This is a **core skill** for AI Security, AI Governance, and AI Risk Engineering roles.

