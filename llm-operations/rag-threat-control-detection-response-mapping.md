# RAG Threat → Control → Detection → Response Mapping

This document maps real-world RAG threat scenarios to preventive controls, detection signals, and incident response actions across the LLM Operations framework. It demonstrates how RAG risks are addressed end-to-end — from ingestion through monitoring and incident response.

Framework alignment follows the mappings defined in `llm-red-teaming-overview.md` and `model-risk-classification-and-criticality.md`.

---

## Threat Mapping

| Threat Scenario | Preventive Controls | Detection Signals | Response Actions | Primary Owner |
|---|---|---|---|---|
| **Indirect prompt injection via retrieved document** | Document sanitization · Instruction stripping · Context isolation blocks · System safety prefix | Injection classifier spike · Retrieved text contains override phrases · Unsafe output correlated to specific doc | Quarantine KB document · Re-scan with YARA/AV · Re-run RAG red teaming · Update sanitization rules | AI Security / Platform |
| **Knowledge base poisoning** | Ingestion allowlists · RBAC on writes · Hash tracking for documents · No direct upload APIs | Sudden embedding similarity clusters · New docs dominate retrieval results · Retrieval distribution drift | Disable ingestion pipeline · Remove poisoned documents · Rebuild embeddings · Incident report + lessons learned | Platform Security |
| **Vector embedding adversarial manipulation** | Embedding normalization · Outlier detection · Approved embedding models only | Extreme vector outliers · Retrieval anomalies across unrelated queries | Re-embed affected corpus · Tighten embedding validation · Add detection thresholds | ML Engineering |
| **Unauthorized retrieval of sensitive documents** | Metadata-based access control · Tenant isolation · Retrieval filters | Retrieval of restricted-class documents · Access attempts outside user role | Block retrieval · Rotate access tokens · Audit access logs | IAM / Security |
| **RAG-assisted data exfiltration** | Token limits · Output filtering · PII redaction · Context size caps | Long structured outputs · Repetitive extraction-like queries · High token usage spikes | Terminate session · Lock API key · Trigger IR playbook | SOC / AI Security |
| **Model instruction override through RAG content** | Prompt sandboxing · Safety prefix enforcement · Instruction stripping | Override keywords detected · Change in refusal behavior | Disable affected model route · Patch orchestration logic · Regression testing | AI Platform |
| **Hallucinations validated by retrieved content** | Source confidence thresholds · Diversity filtering · Hallucination classifiers | High-confidence incorrect outputs · Repeated factual inconsistencies | Adjust retrieval confidence · Add grounding rules · Update reliability metrics | ML Engineering |
| **Tool misuse triggered by retrieved content** | Tool allowlists · Parameter validation · Tool sandboxing | Unexpected tool calls · Abnormal tool chaining | Disable tool access · Review tool permissions · Update allowlists | AppSec |
| **Insider threat via KB manipulation** | RBAC separation (read/write) · Audit logging · Change approvals | After-hours KB updates · High-volume doc inserts | Freeze KB writes · Forensic review · Governance escalation | Governance / Security |
| **Persistent multi-turn escalation using RAG context** | Turn limits · Context window caps · Escalation detection | Progressive safety erosion · Escalating intent across turns | Force conversation reset · Apply stricter policies · Red-team replay | AI Safety |

---

## Risk Severity Reference

| Threat Scenario | Risk Severity |
|---|---|
| Indirect prompt injection via retrieved document | High |
| Knowledge base poisoning | Critical |
| Vector embedding adversarial manipulation | High |
| Unauthorized retrieval of sensitive documents | Critical |
| RAG-assisted data exfiltration | Critical |
| Model instruction override through RAG content | High |
| Hallucinations validated by retrieved content | Medium |
| Tool misuse triggered by retrieved content | High |
| Insider threat via KB manipulation | High |
| Persistent multi-turn escalation using RAG context | Medium |

Risk severity is assigned based on blast radius, ease of exploitation, difficulty of detection prior to impact, and likelihood of downstream harm.

---

## Related Controls and Playbooks

Controls, detection signals, and response actions in this mapping are implemented across:

- `secure-rag-architecture-engineering.md` — architectural controls and ingestion pipeline security
- `rag-security-hardening-guide.md` — implementation-level hardening controls
- `model-monitoring-and-telemetry-engineering.md` — monitoring signals and alerting thresholds
- `llm-incident-response-playbook.md` — incident response workflows
