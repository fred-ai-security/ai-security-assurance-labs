# AI Model Deployment Approval Checklist

This checklist defines the engineering requirements that must be met before any AI model can be deployed into testing, staging, or production environments. It validates that required security, robustness, and governance controls are in place prior to runtime exposure.

Deployment controls referenced here align with `model-deployment-security-engineering.md`. Framework alignment follows `model-risk-classification-and-criticality.md`.

---

## 1. Model Information

| Field | Value |
|---|---|
| Model Name | |
| Version / Build | |
| Provider / Source | |
| Intended Deployment Environment | Dev / Test / Staging / Prod |
| Deployment Owner | |
| Approval Date | |

---

## 2. Supply-Chain Verification

### 2.1 Download Source Validation
- [ ] Model obtained from a trusted, verified source
- [ ] Source URL recorded
- [ ] Provider account verified

### 2.2 Integrity Verification
- [ ] SHA-256 hash generated
- [ ] Hash matches expected value
- [ ] Hash manifest attached

### 2.3 Static Analysis
- [ ] YARA scan performed — no suspicious patterns detected
- [ ] ClamAV scan performed — no malware signatures detected
- [ ] Toolchain integrity verified

### 2.4 Provenance Documentation
- [ ] Provenance record completed
- [ ] Model card reviewed
- [ ] License reviewed and approved

---

## 3. Safety and Behavioral Testing

### 3.1 Functional Safety
- [ ] Output correctness validated for intended tasks
- [ ] Reasoning consistency checks completed

### 3.2 Behavioral Safety
- [ ] Toxicity testing performed
- [ ] Bias checks completed
- [ ] No harmful or disallowed outputs observed

### 3.3 Hallucination and Reliability
- [ ] Hallucination probes executed
- [ ] Overconfidence behavior documented
- [ ] Reliability meets project requirements

---

## 4. Red Teaming and Adversarial Testing

### 4.1 Automated Red Teaming
- [ ] Garak vulnerability scan completed
- [ ] Promptfoo scenario tests completed
- [ ] Findings documented and triaged

### 4.2 Manual Adversarial Testing
- [ ] Jailbreak attempts tested
- [ ] Prompt injection patterns tested
- [ ] Multi-turn escalation tested
- [ ] Refusal behavior validated

### 4.3 Risk Rating
- [ ] Severe vulnerabilities resolved
- [ ] Medium vulnerabilities mitigated or accepted with documentation
- [ ] Residual risk documented

---

## 5. RAG and Data-Layer Security (If Applicable)

- [ ] Retrieval filters validated
- [ ] No poisoned or adversarial content in knowledge base
- [ ] Input sanitization applied
- [ ] Context window safety validated
- [ ] No indirect prompt injection pathways identified

---

## 6. Tool and Plugin Safety (If Enabled)

- [ ] Tool permissions reviewed
- [ ] Tool call constraints validated
- [ ] No unsafe parameter injection pathways
- [ ] No data exfiltration pathways
- [ ] Logging and monitoring enabled for tool calls

---

## 7. Logging, Telemetry, and Monitoring

- [ ] LLM request logging enabled
- [ ] All logs immutable and tamper-evident
- [ ] Safety classifiers integrated (if required)
- [ ] Real-time alerts configured for unsafe output patterns
- [ ] Anomaly detection enabled

---

## 8. Deployment Controls

### 8.1 Access and Authentication
- [ ] Deployment behind authenticated endpoints
- [ ] API keys rotated
- [ ] RBAC and least-privilege enforced

### 8.2 Isolation and Environment Hardening
- [ ] Model runs in isolated environment
- [ ] Network restrictions applied
- [ ] No unnecessary outbound access

### 8.3 Rate Limiting and Abuse Prevention
- [ ] Rate limits configured
- [ ] Abuse detection rules enabled

---

## 9. Final Deployment Authorization

| Role | Name | Approval | Date |
|---|---|---|---|
| Security Engineer | | [ ] Approved | |
| AI Safety Reviewer | | [ ] Approved | |
| ML Engineer | | [ ] Approved | |
| Product Owner | | [ ] Approved | |

---

## 10. Required Attachments

- [ ] Hash manifest
- [ ] Garak report summary
- [ ] Promptfoo results summary
- [ ] Provenance record
- [ ] License evaluation summary
- [ ] Safety evaluation summary
- [ ] SBOM (if generated)
- [ ] Incident history and remediation summary (if re-deployment)
