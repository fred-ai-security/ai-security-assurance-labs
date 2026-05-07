# LLM Operations

This section documents operational security controls for running and deploying LLM systems safely after a model has passed intake, supply-chain validation, and red-teaming (Stages 1–3).

LLM Operations covers runtime and production safeguards — execution isolation, deployment hardening, monitoring and telemetry, incident response, RAG security controls, and deployment approval.

> This section is downstream of `model-supply-chain/` and `red-teaming/`.

---

## Files in This Directory

| File | Purpose |
|---|---|
| `model-execution-runtime-security.md` | Runtime isolation, sandboxing, and execution controls |
| `model-deployment-security-engineering.md` | Deployment hardening, boundary controls, and production security |
| `model-monitoring-and-telemetry-engineering.md` | Operational monitoring signals, telemetry architecture, and alerting |
| `llm-incident-response-playbook.md` | 8-stage incident handling workflow for LLM security events |
| `ai-model-deployment-approval-checklist.md` | Engineering readiness checklist prior to deployment authorization |
| `rag-security-hardening-guide.md` | Implementation-level hardening controls for RAG pipelines |
| `secure-rag-architecture-engineering.md` | Architectural patterns and security controls for RAG system design |
| `rag-threat-control-detection-response-mapping.md` | RAG threat scenarios mapped to preventive controls, detection signals, and response actions |

---

**Note:** Only templates, example commands, and synthetic scenarios are stored in this repository. No real logs, secrets, production paths, or sensitive operational data are committed.
