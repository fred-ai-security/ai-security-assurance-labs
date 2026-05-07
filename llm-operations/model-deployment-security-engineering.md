# AI Model Deployment Security

This document defines engineering controls required to securely deploy AI models in production or controlled environments. It covers runtime isolation, container hardening, network boundaries, secrets management, and security controls that prevent unauthorized access, misuse, or exfiltration.

Deployment security applies after model approval and prior to production exposure. Baseline runtime hardening requirements are defined in `model-execution-runtime-security.md`.

Framework alignment follows the mappings defined in `llm-red-teaming-overview.md` and `model-risk-classification-and-criticality.md`.

---

## 1. Deployment Threat Model

AI model deployments face the following risks:

- Unauthorized model access or extraction
- Prompt injection leading to data leakage
- Model weight exfiltration through responses
- Abusive tool and function call execution
- Escalation via plugins or agents
- RAG-based data poisoning
- Supply-chain compromises
- Memory scraping or process tampering

---

## 2. Runtime Isolation Requirements

### 2.1 Containerization

Models run inside isolated containers or sandboxes with:

- Minimal OS footprint
- Read-only root filesystem
- Non-root user execution
- Locked-down capabilities
- Seccomp, AppArmor, or SELinux active

### 2.2 GPU Isolation

- Limit access using CUDA device whitelisting
- Prevent container escape (NVIDIA Container Runtime hardening)

### 2.3 Process-Level Isolation

- One model per process
- Prevent inter-process memory access
- Memory zeroization on unload
- Disable interactive shell access in production containers

---

## 3. Network and Boundary Security

### 3.1 Network Restrictions

- No outbound internet access
- Block egress by default
- Explicit allowlist for required endpoints only
- Block DNS unless required

### 3.2 API Boundary Controls

- Strict authentication on API endpoints
- JWT or service-account tokens
- Rate limiting and anomaly detection
- Request size limits

### 3.3 Segmentation

Deploy models inside isolated subnets with distinct network zones for red teaming, testing, production, and high-sensitivity environments.

---

## 4. Secrets and Configuration Management

### 4.1 Secrets Controls

Do not store secrets in model files, source code, notebooks, or container environment variables. Use dedicated secrets management:

- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- GCP Secret Manager

### 4.2 Key Rotation

- Rotate API keys used by agents or tools on a defined schedule
- Automatically revoke unused credentials

---

## 5. Model Weight Protection

AI model weights represent a high-value asset requiring dedicated controls:

- Encrypt weights at rest
- Limit filesystem read access
- Disable model download or export endpoints
- Hash and verify model files at startup against tamper-resistant reference values
- Detect unusual token patterns that may indicate extraction attempts

**Model extraction monitoring — flag:**
- Extremely long responses
- Repetitive weight-like numeric sequences
- Attempts to dump model configuration

---

## 6. Guardrails for Unsafe Domains

Before deployment, enforce built-in guardrails for:

- Violence, harassment, self-harm, extremism
- Child safety
- Medical and legal guidance
- Cybersecurity misuse
- PII leakage

A multilayer approach combines system prompts, classification filters, output redaction, and post-processing policies.

---

## 7. Supply Chain Trust at Deployment Time

Deployment includes re-verification of:

- Model hash and SBOM contents
- Provenance record
- Dependency signatures
- Container image hash
- Runtime binary signatures

A deployment pipeline fails closed if any verification mismatches.

---

## 8. Observability and Logging Integration

Every deployment must support:

- Full telemetry (input, output, metadata)
- Structured logs with immutable evidence storage
- Model version and hash tracking
- Alerts on jailbreak patterns, prompt injection, anomalous tool usage, and RAG poisoning signals

Logging follows the monitoring framework defined in `model-monitoring-and-telemetry-engineering.md`.

---

## 9. Deployment Pipeline Requirements

### 9.1 Build Stage
- Generate image → sign → scan → store hash
- Produce SBOM and validate dependencies
- Enforce code review

### 9.2 Test Stage
- Automated red-teaming (Garak, Promptfoo)
- Functional tests, safety classifier tests, logging validation

### 9.3 Approval Stage
- Human review
- Governance review for sensitive use cases
- Risk classification and tier assignment

### 9.4 Deployment Stage
- Immutable model version release
- Zero-downtime rollout with canary testing
- Immediate rollback plan

---

## 10. Runtime Controls

### 10.1 Output Controls
- PII strip filters
- Toxicity rejection
- Unsafe domain guardrails
- Hallucination detection

### 10.2 Input Controls
- Maximum prompt size
- RAG content sanitization
- Disallowed keyword detection
- Automatic prompt injection detection

### 10.3 Resource Controls
- Token limits, timeout limits, memory quotas
