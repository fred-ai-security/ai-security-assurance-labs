# AI Model Risk Classification and Criticality Assessment  
### Governance-Aligned Framework for AI Supply-Chain Security

Model risk classification evaluates the safety, reliability, and potential impact of an AI model in its intended context. 
It determines how the model behaves under various conditions, the likelihood and severity of harm, and the governance controls required before use.

This module aligns with:

- NIST AI RMF  
- ISO/IEC 42001  
- MITRE ATLAS  
- Enterprise AI Governance Standards  

---

## 1. Purpose of Model Risk Classification

Risk classification provides a structured assessment of possible harms arising from AI model behavior, including:

- Harmful or toxic outputs  
- Biased or discriminatory responses  
- Jailbreak or prompt-injection exploitation  
- Data leakage  
- Unsafe domain guidance (medical, legal, financial)  
- Agentic misbehavior in automation settings  
- High-impact hallucinations  

This assessment determines:

- Required security controls  
- Required red-teaming depth  
- Deployment safety level  
- Governance and documentation needs  
- Whether the model can be approved for use  

---

## 2. Model Context and Intended Use Analysis

Risk classification begins with reviewing the model's purpose, environment, and operational context.

### Evaluation Criteria

| Category | Considerations |
|---------|----------------|
| **Domain** | Healthcare, finance, legal, hiring, critical systems |
| **User Impact** | Influence on individuals or decisions |
| **Automation Level** | Advisory vs. autonomous operation |
| **Data Sensitivity** | PII, PHI, regulated data |
| **Audience** | Internal users, enterprise teams, public access |

### High-Risk Indicators

- Use in regulated or high-impact domains  
- Processing sensitive or restricted data  
- High levels of automation  
- Public-facing deployment  
- Safety-critical decision-making  

---

## 3. Harm Likelihood Scoring (NIST AI RMF)

Scores indicate how likely a model is to generate harmful outcomes during normal use.

| Score | Likelihood | Description |
|-------|------------|-------------|
| **1 – Low** | Minimal potential for harmful behavior |
| **2 – Medium** | Harm possible under specific conditions |
| **3 – High** | Harm likely due to design or known behavior |

Factors considered:

- Hallucination rate  
- Tendency toward unsafe outputs  
- Toxicity generation  
- Confidence levels in incorrect responses  

---

## 4. Exploitability and Misuse Exposure

Assess how accessible the model is to adversarial manipulation.

| Score | Exposure | Description |
|-------|----------|-------------|
| **1 – Low** | Restricted, internal-only access |
| **2 – Medium** | Limited shared access |
| **3 – High** | Public or API-exposed model |

Indicators:

- API or remote access  
- Weak safety guardrails  
- Jailbreak susceptibility  
- Visibility of internal instructions  

---

## 5. Severity of Harm

Evaluates the consequences of unsafe or incorrect outputs.

| Score | Severity | Examples |
|-------|----------|----------|
| **1 – Low** | Minor issues with no real-world effect |
| **2 – Medium** | Misleading information or reputational impact |
| **3 – High** | Physical harm, legal exposure, discrimination, financial loss |

Examples of high severity:

- Incorrect medical or legal guidance  
- Financial fraud enablement  
- Strong demographic bias  
- Dangerous instructions  

---

## 6. AI Model Risk Matrix

Risk levels are derived by combining likelihood, exploitability, and severity.

| Likelihood | Exploitability | Severity | Risk Level |
|------------|----------------|----------|------------|
| 1 | 1 | 1–2 | **Low** |
| 1–2 | 1–2 | 2 | **Medium** |
| 2–3 | 2–3 | 2–3 | **High** |
| 3 | 3 | 3 | **Critical** |

### Resulting Levels

- **Low:** Basic intake controls  
- **Medium:** Static analysis + targeted red teaming  
- **High:** Full supply-chain review + extensive red teaming  
- **Critical:** Deployment restricted; executive or governance approval required  

---

## 7. Criticality Tier Classification

### **Tier 1 — High Criticality**
Typical Uses:
- Healthcare  
- Finance  
- Legal and judicial domains  
- Hiring and HR systems  
- Safety-critical automation  
- Autonomous agent workflows  

Required Controls:
- Full supply-chain analysis  
- Comprehensive red teaming (Garak, Promptfoo)  
- Governance review  
- Continuous monitoring  

---

### **Tier 2 — Medium Criticality**
Typical Uses:
- Customer support  
- Content generation  
- Internal productivity tools  
- Knowledge retrieval  

Required Controls:
- Static analysis  
- Partial red teaming  
- Risk documentation  

---

### **Tier 3 — Low Criticality**
Typical Uses:
- Research models  
- Experiments  
- Non-sensitive internal workflows  

Required Controls:
- Basic intake validation  
- Hashing and provenance review  

---

## 8. Model Risk Classification Summary Template

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

**Validated By:** Frederick Baffour
```

---

## 9. File Location

```
ai-security-assurance-labs/
└── model-supply-chain/
      └── model-risk-classification-and-criticality.md
```

---

## Conclusion

This module establishes a structured approach for evaluating AI model criticality and determining the appropriate level of governance, security controls, and red-teaming rigor.  
It supports enterprise-grade decision-making for AI deployment across sensitive and high-impact environments.
