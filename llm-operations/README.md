# LLM Operations

This section documents operational security controls for running and deploying LLM systems safely after a model has passed intake, supply-chain validation, and initial red-teaming.

LLM Operations focuses on runtime and production safeguards such as execution isolation, deployment hardening, monitoring and telemetry, incident response, and RAG security controls.

> This section is downstream of `model-supply-chain/` and `red-teaming/`.

---

## What This Section Covers

- Model execution runtime security (isolation, sandboxing, policy enforcement)
- Deployment security engineering controls (configuration, access control, secrets, hardening)
- Monitoring and telemetry for safety, abuse, and reliability signals
- Incident response playbooks for LLM-related security events
- Approval checklists for operational readiness
- RAG security hardening and secure architecture patterns (when applicable)

---

## Start Here (Recommended Reading Order)

### For Recruiters / Non-Technical Reviewers
- `ai-model-deployment-approval-checklist.md`
- `llm-incident-response-playbook.md`

### For Security Engineers
- `model-execution-runtime-security.md`
- `model-deployment-security-engineering.md`

### For Engineering / Platform Teams
- `model-monitoring-and-telemetry-engineering.md`
- `secure-rag-architecture-engineering.md` (if RAG is in scope)

---

## Files in This Directory

- `model-execution-runtime-security.md` — runtime isolation, guardrails, and execution controls
- `model-deployment-security-engineering.md` — deployment hardening and production security controls
- `model-monitoring-and-telemetry-engineering.md` — operational monitoring signals and telemetry practices
- `llm-incident-response-playbook.md` — incident handling workflow for LLM security events
- `ai-model-deployment-approval-checklist.md` — readiness checklist prior to deployment approval
- `rag-security-hardening-guide.md` — hardening guidance for RAG pipelines
- `secure-rag-architecture-engineering.md` — secure architecture patterns for RAG systems
- `llm-operations-handbook-*.md` — role-focused operations guidance (engineering / security / governance)

---

**Note:** Only templates, example commands, and synthetic scenarios are stored in this repository. No real logs, secrets, production paths, or sensitive operational data are committed.
