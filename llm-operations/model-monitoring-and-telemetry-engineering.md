# LLM Monitoring and Telemetry

This document defines the engineering requirements for logging, telemetry, and monitoring of AI systems — including standalone LLMs, RAG pipelines, and agentic systems. Monitoring is essential for detecting unsafe behavior, policy violations, misuse attempts, and anomalies that indicate security or reliability issues.

Framework alignment follows the mappings defined in `llm-red-teaming-overview.md` and `model-risk-classification-and-criticality.md`.

---

## 1. Monitoring Objectives

A complete monitoring system addresses four goals:

**Safety Monitoring** — detect toxic, harmful, or policy-violating outputs.

**Security Monitoring** — identify jailbreaks, prompt injections, misuse attempts, and anomalous behavior.

**Reliability Monitoring** — track hallucinations, degraded performance, and instability.

**Audit and Forensics** — provide evidence for incident response, compliance, and governance reviews.

---

## 2. What Must Be Logged

### 2.1 Input Telemetry
- User prompts, system prompts, retrieved RAG content
- Tool and function call inputs
- Metadata: user ID, session ID, timestamp, context length

### 2.2 Output Telemetry
- Final model response
- Refusals and safety warnings
- Classifier scores (toxicity, PII, jailbreak risk)
- Tool and function call outputs

### 2.3 Operational Telemetry
- Latency, token counts, resource usage (CPU/GPU/memory)
- Model version and hash
- Embedding model version (for RAG pipelines)

### 2.4 Security Telemetry
- Jailbreak and prompt injection attempts detected
- RAG poisoning indicators
- Unexpected tool calls
- Unauthorized domain queries
- High-risk content generation events

---

## 3. Redaction and Privacy Controls

Before storing logs:

- [ ] Strip PII and PHI where possible
- [ ] Mask user-entered sensitive fields
- [ ] Hash user identifiers for auditing without exposure
- [ ] Enforce retention periods
- [ ] Encrypt logs at rest and in transit

---

## 4. Safety Classifiers and Output Filters

Monitoring integrates safety classifiers detecting:

- Toxic language, harassment, hate speech
- Sexual content, violence, extremism
- Medical or legal advice generation
- Self-harm indications
- Sensitive personal data
- High-risk cybersecurity content

Required classifier output fields:

```
toxicity_score:
jailbreak_score:
pii_detection:
hallucination_likelihood:
```

Any score exceeding defined thresholds triggers an alert.

---

## 5. Real-Time Alerting and Thresholds

### 5.1 Alert Types

Alerts should be generated for:

- Jailbreak attempts exceeding session threshold
- Any confirmed prompt injection
- Any detected PII leakage
- High-severity safety violations
- Unauthorized tool usage
- RAG document injection attempts
- Sudden spikes in hallucination classifier scores

### 5.2 Severity Levels

| Level | Action |
|---|---|
| Critical | Mandatory human review |
| High | Automated blocking and escalation |
| Medium | Log and monitoring dashboard |
| Low | Informational |

---

## 6. RAG Pipeline Monitoring

### 6.1 RAG-Specific Telemetry

Log:
- Document IDs retrieved and similarity scores
- Knowledge base source and owner
- Sanitization rules applied
- Adversarial patterns flagged

### 6.2 RAG-Specific Alerts

Alert on:
- Retrieval of unapproved or suspicious documents
- High similarity to known adversarial examples
- Rapid "override system" patterns from retrieved content
- Retrieved documents containing embedded instructions

---

## 7. Tool and Function Call Monitoring

For agentic or tool-enabled systems, log:

- Tool name, parameters, input data, output data
- Whether the call was expected or anomalous

Alert on:
- Dangerous tool invocations (filesystem, network requests)
- Abnormal tool call frequency
- Large or unexpected data exfiltration patterns

---

## 8. Anomaly Detection

Implement anomaly detection over:

- User behavior and token usage patterns
- Query embeddings and output distributions
- Retrieval patterns and tool call sequences

Anomaly types to detect:

- Sudden change in model refusal rate
- Abnormally high hallucination rate
- Unusual combination of retrieved documents
- Behavioral drift across sessions

---

## 9. Logging Architecture Requirements

### Ingestion Layer
- Event collector with structured logs (JSON preferred)
- Filtering and redaction at source

### Processing Layer
- Safety classifier scoring
- Rule-based detectors
- Anomaly detection models

### Storage Layer
- Encrypted blob storage or secure log store
- Append-only architecture (immutable logs)
- Time-series database for metrics

### Dashboarding Layer
- Session-level and system-level dashboards (Grafana, Kibana, CloudWatch, Datadog)

### Alerting Layer
- PagerDuty, email, or Slack integration

---

## 10. Monitoring Requirements Checklist

**Safety:**
- [ ] Output classification
- [ ] Toxicity detection
- [ ] PII detection
- [ ] Jailbreak risk scoring

**Security:**
- [ ] Prompt injection detection
- [ ] RAG poisoning detection
- [ ] Tool misuse detection
- [ ] Unauthorized access attempts

**Reliability:**
- [ ] Hallucination monitoring
- [ ] Latency and error tracking
- [ ] Token usage spikes

**Governance:**
- [ ] Model version tracking
- [ ] Audit logging
- [ ] Immutable evidence storage
- [ ] Retention policy enforcement

---

Monitoring outputs feed directly into `llm-incident-response-playbook.md` and governance approval workflows.
