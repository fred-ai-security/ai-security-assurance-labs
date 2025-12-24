# LLM Incident Response Playbook
A security playbook for identifying, containing, analyzing, and recovering from incidents involving large language models (LLMs).

---

## 1. Purpose

This playbook defines the steps for responding to security, safety, or operational incidents involving LLMs. It ensures consistent, evidence-based handling of issues such as unsafe outputs, model drift, compromised inputs, tool misuse, or supply-chain anomalies.

The goal is to protect users, systems, and data while restoring safe AI operations.

---

## 2. Incident Categories

LLM-related incidents fall into six major categories:

### 2.1 Unsafe Output Incidents
- Harmful, toxic, or unsafe responses  
- Disallowed domain advice (medical, legal, financial)  
- Hallucinations with high confidence  
- Biased or discriminatory outputs  

### 2.2 Prompt Injection & Jailbreak Incidents
- System prompt override  
- Direct or indirect prompt injection  
- Multi-turn jailbreak escalation  
- Unsafe tool activation  

### 2.3 Data Security Incidents
- Leakage of personal data  
- Model revealing internal logs, credentials, or config  
- Unintended memorization exposure  

### 2.4 Model Integrity & Supply-Chain Incidents
- Hash mismatch  
- YARA/ClamAV detections  
- Suspicious embedded binaries  
- Unexpected model file changes  

### 2.5 RAG (Retrieval-Augmented Generation) Incidents
- Poisoned knowledge base content  
- Embedded malicious instructions  
- Inference-time data manipulation  

### 2.6 System-Level Incidents
- Unauthorized API access  
- Abuse of agent / tool-calling  
- Excessive or abnormal traffic patterns  

---

## 3. Severity Levels

### Critical
High-impact unsafe behavior, data leakage, or tool misuse that could cause major harm.

### High
Repeatable jailbreaks, strong prompt injection, or exposure of sensitive internal information.

### Medium
Partial policy erosion, unsafe edge-case outputs, or transient hallucinations.

### Low
Minor deviations, tone/style issues, benign inconsistencies.

Severity determines escalation path and response requirements.

---

## 4. LLM Incident Response Workflow

The workflow consists of **8 stages**, aligned to traditional IR but tuned for LLM behavior.

---

## Stage 1 — Identification

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

Deliverables:
- Incident ticket created (SOC, Security, or AI Governance system)
- Evidence folder initiated 

---

## Stage 2 — Containment

Goal: Immediately reduce further harm.

Containment measures:

- Disable or limit access to the model  
- Remove or suspend access to affected tools  
- Pause RAG ingestion  
- Force model routing to a safer fallback model  
- Lock down API keys  

For supply-chain events:

- Quarantine the affected model file  
- Block related file downloads  

Deliverable:
- Containment confirmation logged  

---

## Stage 3 — Triage & Assessment

Focus areas:

### Behavioral Incidents
- Determine if behavior is repeatable  
- Identify specific prompts that cause unsafe output  
- Check for multi-turn escalation  

### Injection/Jailbreak Incidents
- Identify injection vector  
- Determine if system prompts were overridden  
- Assess persistence of override  

### File Integrity Incidents
- Re-hash all model artifacts  
- Re-run YARA and ClamAV  
- Inspect file structure  

Deliverables:
- Initial triage report  
- Confirmed severity classification  

---

## Stage 4 — Full Analysis

Perform detailed root-cause analysis:

### Behavioral Analysis
- Reproduce issues in a controlled test environment  
- Use Garak/Promptfoo for automated reproduction  
- Check for pattern-based vulnerabilities  

### Supply-Chain Analysis
- Verify provenance and download logs  
- Validate signatures and hash logs  
- Examine SBOM for unexpected components  

### RAG-Focused Analysis
- Identify poisoned or malicious documents  
- Validate retrieval filters  
- Inspect metadata and document origins  

### System-Level Analysis
- Review access logs  
- Validate API key usage  
- Inspect model runtime logs  

Deliverable:
- Full incident analysis document  

---

## Stage 5 — Eradication

Actions based on incident type:

### Unsafe Output
- Improve system prompt  
- Add safety filters  
- Patch moderation rules  

### Jailbreak Injection
- Harden system prompts  
- Add runtime prompt sanitization  
- Enforce stronger deny-lists  

### RAG Poisoning
- Remove malicious KB entries  
- Add ingestion validation rules  
- Patch metadata or embeddings  

### Tool Misuse
- Restrict tool-call permissions  
- Add parameter validation  
- Add sandboxing or rate-limits  

### Supply-Chain Tampering
- Remove corrupted model file  
- Re-download from trusted source  
- Update hash manifest  

Deliverable:
- Eradication confirmation  

---

## Stage 6 — Recovery

Actions:
- Restore safe model behavior  
- Validate with Garak and Promptfoo  
- Test refusal patterns and safety guardrails  
- Resume RAG ingestion (if safe)  
- Re-enable tools with restrictions  
- Roll back to previously approved model version (if applicable)

Deliverable:
- Recovery validation report

---

## Stage 7 — Lessons Learned

Document:

- Root cause summary  
- What controls failed  
- What controls worked  
- Required improvements  
- Update to threat modeling  

Deliverable:
- Final Incident Report  

---

## Stage 8 — Preventive Hardening

Implement long-term controls:

- Strengthen system prompts  
- Add new YARA or ClamAV rules  
- Update SBOM validation process  
- Improve RAG ingestion sanitization  
- Add guardrail or moderation layers  
- Create new Promptfoo red-team tests  
- Adjust access controls for API keys  
- Add telemetry alerts for risky patterns  

Deliverable:
- Preventive hardening action plan  

---

## 5. Artifacts Collected During Incidents

Each incident must collect:

- High-level prompt pattern  
- High-level output summary  
- Model version and hash  
- Logs (redacted)  
- System metadata  
- RAG documents returned  
- Tool calls involved  
- ClamAV/YARA output if supply-chain incident  
- Signature verification results for binaries  

Artifacts must avoid storing real unsafe content.

---

## 6. Directory Placement

```
ai-security-assurance-labs/
└── llm-operations/
      └── llm-incident-response-playbook.md
```

---

## 7. Alignment With Standards

This playbook aligns with:

- NIST AI RMF – Measure & Manage  
- ISO/IEC 42001 – Incident and Risk Controls  
- MITRE ATLAS – Misuse Techniques  
- Secure AI red-teaming practices  
- Enterprise SOC/IR playbooks  

---

# End of Document
