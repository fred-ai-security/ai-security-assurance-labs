# LLM Incident Response Playbook

A security playbook for identifying, containing, analyzing, and recovering from incidents involving large language models.

---

## Purpose

This playbook defines the response steps for security, safety, or operational incidents involving LLMs. It ensures consistent, evidence-based handling of issues such as unsafe outputs, model drift, compromised inputs, tool misuse, or supply-chain anomalies.

Framework alignment follows the mappings defined in `llm-red-teaming-overview.md` and `model-risk-classification-and-criticality.md`.

---

## 1. Incident Categories

### 1.1 Unsafe Output Incidents
- Harmful, toxic, or unsafe responses
- Disallowed domain advice (medical, legal, financial)
- High-confidence hallucinations
- Biased or discriminatory outputs

### 1.2 Prompt Injection and Jailbreak Incidents
- System prompt override
- Direct or indirect prompt injection
- Multi-turn jailbreak escalation
- Unsafe tool activation

### 1.3 Data Security Incidents
- Leakage of personal data
- Model revealing internal logs, credentials, or configuration
- Unintended memorization exposure

### 1.4 Model Integrity and Supply-Chain Incidents
- Hash mismatch
- YARA or ClamAV detections
- Suspicious embedded binaries
- Unexpected model file changes

### 1.5 RAG Incidents
- Poisoned knowledge base content
- Embedded malicious instructions
- Inference-time data manipulation

### 1.6 System-Level Incidents
- Unauthorized API access
- Abuse of agent or tool-calling
- Excessive or abnormal traffic patterns

---

## 2. Severity Levels

| Level | Description |
|---|---|
| Critical | High-impact unsafe behavior, data leakage, or tool misuse with potential for major harm |
| High | Repeatable jailbreaks, strong prompt injection, or exposure of sensitive internal information |
| Medium | Partial policy erosion, unsafe edge-case outputs, or transient hallucinations |
| Low | Minor deviations, tone/style issues, benign inconsistencies |

Severity determines escalation path and response requirements.

---

## 3. Incident Response Workflow — 8 Stages

### Stage 1 — Identification

Trigger conditions:
- Unsafe or harmful output observed
- Alerts from monitoring (toxicity, policy violations)
- Repeated refusal bypass
- Strange or escalating model behavior
- Unexpected content returned from RAG
- Hash mismatch or static analysis anomaly

Actions:
- Capture the prompt (sanitized), context summary, and output
- Document when, where, and by whom it was observed
- Classify preliminary severity level

**Deliverable:** Incident ticket created; evidence folder initiated.

---

### Stage 2 — Containment

Goal: Immediately reduce further harm.

- Disable or limit access to the model
- Remove or suspend access to affected tools
- Pause RAG ingestion
- Force model routing to a safer fallback
- Lock down API keys

For supply-chain events:
- Quarantine the affected model file
- Block related file downloads

**Deliverable:** Containment confirmation logged.

---

### Stage 3 — Triage and Assessment

**Behavioral incidents:** Determine if behavior is repeatable; identify specific prompts; check for multi-turn escalation.

**Injection/jailbreak incidents:** Identify injection vector; determine if system prompts were overridden; assess persistence.

**File integrity incidents:** Re-hash all model artifacts; re-run YARA and ClamAV; inspect file structure.

**Deliverable:** Initial triage report with confirmed severity classification.

---

### Stage 4 — Full Analysis

**Behavioral analysis:** Reproduce issues in a controlled test environment using Garak and Promptfoo; check for pattern-based vulnerabilities.

**Supply-chain analysis:** Verify provenance and download logs; validate signatures and hash logs; examine SBOM for unexpected components.

**RAG-focused analysis:** Identify poisoned or malicious documents; validate retrieval filters; inspect metadata and document origins.

**System-level analysis:** Review access logs; validate API key usage; inspect model runtime logs.

**Deliverable:** Full incident analysis document.

---

### Stage 5 — Eradication

| Incident Type | Actions |
|---|---|
| Unsafe output | Improve system prompt; add safety filters; patch moderation rules |
| Jailbreak injection | Harden system prompts; add runtime prompt sanitization; enforce deny-lists |
| RAG poisoning | Remove malicious KB entries; add ingestion validation; patch metadata |
| Tool misuse | Restrict tool-call permissions; add parameter validation; add sandboxing |
| Supply-chain tampering | Remove corrupted model file; re-download from trusted source; update hash manifest |

**Deliverable:** Eradication confirmation.

---

### Stage 6 — Recovery

- Restore safe model behavior
- Validate with Garak and Promptfoo
- Test refusal patterns and safety guardrails
- Resume RAG ingestion if safe
- Re-enable tools with restrictions
- Roll back to previously approved model version if applicable

**Deliverable:** Recovery validation report.

---

### Stage 7 — Lessons Learned

Document:
- Root cause summary
- What controls failed and what worked
- Required improvements
- Updates to threat modeling

**Deliverable:** Final Incident Report.

---

### Stage 8 — Preventive Hardening

- Strengthen system prompts
- Add new YARA or ClamAV rules
- Update SBOM validation process
- Improve RAG ingestion sanitization
- Add guardrail or moderation layers
- Create new Promptfoo red-team tests
- Adjust access controls for API keys
- Add telemetry alerts for risky patterns

**Deliverable:** Preventive hardening action plan.

---

## 4. Artifacts Collected During Incidents

Each incident must collect:

- High-level prompt pattern (sanitized)
- High-level output summary
- Model version and hash
- Redacted logs and system metadata
- RAG documents returned (if applicable)
- Tool calls involved
- ClamAV/YARA output for supply-chain incidents
- Signature verification results for binaries

Artifacts must not store raw unsafe content.

---

## 5. Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MANAGE 2.2, MANAGE 3.1 — incident detection, response, and recovery |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — Prompt Injection; AML.T0010 — Supply Chain Compromise |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling; LLM03 — Training Data Poisoning |
| ISO/IEC 42001 | Clause 9 — Performance evaluation; Clause 10 — Improvement and incident controls |
| NIST SP 800-53 | IR-4 — Incident Handling; IR-6 — Incident Reporting; SI-7 — Integrity Verification |
