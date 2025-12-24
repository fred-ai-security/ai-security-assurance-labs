RAG Threat → Control → Detection → Response Mapping

> Learning Context:
> This mapping was created as part of my hands-on learning in AI Security Assurance and RAG system defense.
> The goal is to practice identifying real-world threat patterns and understanding how preventive controls,
> detection signals, and incident response actions connect across an AI system lifecycle.
>
> The scenarios and responses reflect industry-aligned practices and are intended as a reference framework,
> not a claim of production ownership.

(Engineering & Security Operations Edition)

This document maps real-world RAG threat scenarios to the preventive controls, detection signals, and incident response actions implemented across the LLM Operations framework.

It demonstrates how RAG risks are handled end-to-end — from ingestion through monitoring and incident response.


| Threat Scenario                                        | Preventive Controls                                                                                        | Detection Signals                                                                                                        | Response Actions                                                                                                           | Primary Owner          |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **Indirect prompt injection via retrieved document**   | • Document sanitization<br>• Instruction stripping<br>• Context isolation blocks<br>• System safety prefix | • Injection classifier spike<br>• Retrieved text contains override phrases<br>• Unsafe output correlated to specific doc | • Quarantine KB document<br>• Re-scan with YARA/AV<br>• Re-run RAG red teaming<br>• Update sanitization rules              | AI Security / Platform |
| **Knowledge base poisoning**                           | • Ingestion allowlists<br>• RBAC on writes<br>• Hash tracking for documents<br>• No direct upload APIs     | • Sudden embedding similarity clusters<br>• New docs dominate retrieval results<br>• Retrieval distribution drift        | • Disable ingestion pipeline<br>• Remove poisoned documents<br>• Rebuild embeddings<br>• Incident report + lessons learned | Platform Security      |
| **Vector embedding adversarial manipulation**          | • Embedding normalization<br>• Outlier detection<br>• Approved embedding models only                       | • Extreme vector outliers<br>• Retrieval anomalies across unrelated queries                                              | • Re-embed affected corpus<br>• Tighten embedding validation<br>• Add detection thresholds                                 | ML Engineering         |
| **Unauthorized retrieval of sensitive documents**      | • Metadata-based access control<br>• Tenant isolation<br>• Retrieval filters                               | • Retrieval of restricted-class documents<br>• Access attempts outside user role                                         | • Block retrieval<br>• Rotate access tokens<br>• Audit access logs                                                         | IAM / Security         |
| **RAG-assisted data exfiltration**                     | • Token limits<br>• Output filtering<br>• PII redaction<br>• Context size caps                             | • Long structured outputs<br>• Repetitive extraction-like queries<br>• High token usage spikes                           | • Terminate session<br>• Lock API key<br>• Trigger IR playbook                                                             | SOC / AI Security      |
| **Model instruction override through RAG content**     | • Prompt sandboxing<br>• Safety prefix enforcement<br>• Instruction stripping                              | • Override keywords detected<br>• Change in refusal behavior                                                             | • Disable affected model route<br>• Patch orchestration logic<br>• Regression testing                                      | AI Platform            |
| **Hallucinations validated by retrieved content**      | • Source confidence thresholds<br>• Diversity filtering<br>• Hallucination classifiers                     | • High-confidence incorrect outputs<br>• Repeated factual inconsistencies                                                | • Adjust retrieval confidence<br>• Add grounding rules<br>• Update reliability metrics                                     | ML Engineering         |
| **Tool misuse triggered by retrieved content**         | • Tool allowlists<br>• Parameter validation<br>• Tool sandboxing                                           | • Unexpected tool calls<br>• Abnormal tool chaining                                                                      | • Disable tool access<br>• Review tool permissions<br>• Update allowlists                                                  | AppSec                 |
| **Insider threat via KB manipulation**                 | • RBAC separation (read/write)<br>• Audit logging<br>• Change approvals                                    | • After-hours KB updates<br>• High-volume doc inserts                                                                    | • Freeze KB writes<br>• Forensic review<br>• Governance escalation                                                         | Governance / Security  |
| **Persistent multi-turn escalation using RAG context** | • Turn limits<br>• Context window caps<br>• Escalation detection                                           | • Progressive safety erosion<br>• Escalating intent across turns                                                         | • Force conversation reset<br>• Apply stricter policies<br>• Red-team replay                                               | AI Safety              |


Risk Severity: Low | Medium | High | Critical

| Threat Scenario                                  | Risk Severity |
| ------------------------------------------------ | ------------- |
| Indirect prompt injection via retrieved document | High          |
| Knowledge base poisoning                         | Critical      |
| Vector embedding adversarial manipulation        | High          |
| Unauthorized retrieval of sensitive documents    | Critical      |
| RAG-assisted data exfiltration                   | Critical      |


## Notes on Risk Severity Assignment

Risk severities are assigned based on:
- Potential blast radius (data exposure, system compromise)
- Ease of exploitation in RAG systems
- Difficulty of detection prior to impact
- Likelihood of downstream harm

Severity ratings may evolve as additional controls, monitoring signals,
or architectural constraints are introduced.


## Referenced Controls & Playbooks

Preventive, detection, and response controls in this mapping are implemented across:

- Secure RAG Architecture (Engineering Edition)
- RAG Security Hardening Guide (Engineering Edition)
- LLM Monitoring & Telemetry (Engineering Edition)
- Model Execution Runtime Security (Engineering Edition)
- LLM Incident Response Playbook


## Open Questions & Learning Areas

The following areas are under active learning and refinement:

- Practical thresholds for embedding outlier detection
- Tradeoffs between retrieval depth and hallucination risk
- Operational cost of continuous KB re-scanning
- Measuring false positives in RAG injection detection

These topics are intentionally left open for further experimentation,
red-teaming, and iteration.
