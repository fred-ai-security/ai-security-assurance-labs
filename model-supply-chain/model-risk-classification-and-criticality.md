# AI Model Risk Classification and Criticality Assessment

## Governance-Aligned Framework for AI Supply-Chain Security

Model risk classification defines the structured evaluation of safety, reliability, and potential impact of an AI model in its intended context. It determines how the model behaves under various conditions, the likelihood and severity of harm, and the governance controls required before use.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MAP 1.5, MEASURE 2.2, MANAGE 2.2 — risk identification, scoring, and governance controls |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051 — Prompt Injection; AML.T0040 — ML Model Inference |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM06 — Sensitive Information Disclosure; LLM08 — Excessive Agency |
| ISO/IEC 42001 | Clause 6 — Risk assessment and AI impact classification |
| NIST SP 800-53 | RA-3 — Risk Assessment; SA-11 — Developer Testing and Evaluation |

---

## 1. Model Risk Classification as a Governance Control

Risk classification provides a structured assessment of possible harms arising from AI model behavior, including:

- Harmful or toxic outputs
- Biased or discriminatory responses
- Jailbreak or prompt injection exploitation
- Data leakage and sensitive information disclosure
- Unsafe domain guidance (medical, legal, financial)
- Agentic misbehavior in automation settings
- High-impact hallucinations

This assessment determines:

- Required security controls
- Required red-teaming depth
- Deployment safety level
- Governance and documentation requirements
- Whether the model is approved for use

---

## 2. Model Context and Intended Use Analysis

Risk classification begins with reviewing the model's purpose, environment, and operational context.

| Category | Considerations |
|---|---|
| Domain | Healthcare, finance, legal, hiring, critical systems |
| User Impact | Influence on individuals or high-stakes decisions |
| Automation Level | Advisory vs. autonomous operation |
| Data Sensitivity | PII, PHI, regulated or restricted data |
| Audience | Internal users, enterprise teams, public access |

**High-Risk Indicators:**

- Use in regulated or high-impact domains
- Processing of sensitive or restricted data
- High levels of automation or autonomous decision-making
- Public-facing or API-exposed deployment
- Safety-critical decision-making contexts

---

## 3. Harm Likelihood Scoring

Scores reflect the likelihood of harmful outcomes during normal model use.

| Score | Likelihood | Description |
|---|---|---|
| 1 — Low | Minimal | Harmful behavior is unlikely under normal conditions |
| 2 — Medium | Moderate | Harm is possible under specific or edge-case conditions |
| 3 — High | Elevated | Harm is likely based on design characteristics or known behavior |

**Factors considered:** hallucination rate, tendency toward unsafe outputs, toxicity generation, confidence in incorrect responses.

---

## 4. Exploitability and Misuse Exposure

Assesses how accessible the model is to adversarial manipulation.

| Score | Exposure | Description |
|---|---|---|
| 1 — Low | Restricted | Internal-only access with strong access controls |
| 2 — Medium | Limited | Shared or semi-public access with some controls |
| 3 — High | Exposed | Public-facing or API-accessible with minimal restrictions |

**Indicators:** API or remote access availability, weak safety guardrails, jailbreak susceptibility, visible system prompt exposure.

---

## 5. Severity of Harm

Evaluates the consequences of unsafe or incorrect model outputs.

| Score | Severity | Examples |
|---|---|---|
| 1 — Low | Minimal | Minor issues with no real-world effect |
| 2 — Medium | Moderate | Misleading information, reputational impact |
| 3 — High | Significant | Physical harm, legal exposure, discrimination, financial loss |

**High severity examples:** incorrect medical or legal guidance, financial fraud enablement, strong demographic bias, dangerous operational instructions.

---

## 6. AI Model Risk Matrix

Risk levels are derived by combining likelihood, exploitability, and severity scores.

| Likelihood | Exploitability | Severity | Risk Level |
|---|---|---|---|
| 1 | 1 | 1–2 | Low |
| 1–2 | 1–2 | 2 | Medium |
| 2–3 | 2–3 | 2–3 | High |
| 3 | 3 | 3 | Critical |

**Resulting controls by risk level:**

| Risk Level | Required Controls |
|---|---|
| Low | Basic intake validation |
| Medium | Static analysis + targeted red teaming |
| High | Full supply-chain review + extensive red teaming |
| Critical | Deployment restricted; executive or governance approval required |

---

## 7. Criticality Tier Classification

### Tier 1 — High Criticality

**Typical uses:** Healthcare, finance, legal and judicial, hiring and HR systems, safety-critical automation, autonomous agent workflows

**Required controls:** Full supply-chain analysis, comprehensive red teaming (Garak, PyRIT, Promptfoo), governance review, continuous monitoring

### Tier 2 — Medium Criticality

**Typical uses:** Customer support, content generation, internal productivity tools, knowledge retrieval

**Required controls:** Static analysis, targeted red teaming, risk documentation

### Tier 3 — Low Criticality

**Typical uses:** Research models, experiments, non-sensitive internal workflows

**Required controls:** Basic intake validation, hashing and provenance review

---

## 8. Model Risk Classification Summary Template

```markdown
# Model Risk Classification Summary

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
