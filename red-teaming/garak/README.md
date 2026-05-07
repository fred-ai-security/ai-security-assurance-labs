# Garak — LLM Vulnerability Testing

Garak is used for automated vulnerability and safety behavior testing against local language models as part of Stage 3 of the AI Security Assurance Lifecycle. All testing is performed against locally hosted models to maintain chain of custody over assessment data, prompts, and findings throughout execution.

Garak evaluates models for:

- Jailbreak susceptibility
- Prompt injection vulnerabilities
- Refusal bypass behaviors
- Toxic or harmful content generation
- Hallucination and over-compliance patterns
- Undesired responses under adversarial conditions

Garak-based testing is performed after model intake and supply-chain validation (Stages 1–2) and before RAG pipeline security assessment, agentic AI testing, and consolidated reporting (Stages 4–6).

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MEASURE 2.6 — robustness testing and adversarial evaluation |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — LLM Prompt Injection |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling; LLM06 — Sensitive Information Disclosure |
| ISO/IEC 42001 | Clause 8 — AI system testing and behavioral evaluation |
| NIST SP 800-53 | SA-11 — Developer Testing and Evaluation; CA-8 — Penetration Testing |

---

## Typical Workflow

1. Select a locally hosted target model via Ollama
2. Choose relevant probe classes (jailbreak, prompt injection, refusal bypass, toxicity)
3. Execute Garak and collect structured results (JSON and HTML report)
4. Interpret failures and categorize by severity and attack class
5. Document findings with framework mappings and mitigation recommendations

Garak executes probes across multiple attack classes simultaneously. A full assessment run covers 1,280+ probes across 10 attack classes against the target model.

---

## Files in This Directory

| File | Purpose |
|---|---|
| `example-garak-assessment.md` | Example assessment summary illustrating how Garak findings are interpreted and documented in an AI Security Assurance context |
| `jailbreak-and-prompt-injection-framework.md` | Framework reference mapping Garak jailbreak and prompt injection probe classes to OWASP LLM Top 10 (2025) and MITRE ATLAS TTPs |
