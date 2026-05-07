# Promptfoo — Scenario-Based LLM Red Teaming

Promptfoo is used to perform scenario-driven adversarial evaluations against locally hosted language models as part of Stage 3 of the AI Security Assurance Lifecycle. All evaluations are executed against local model endpoints to maintain chain of custody over assessment data, prompts, and findings.

Findings from Promptfoo evaluations feed into safety evaluation, risk classification, and final approval decisions — used in combination with Garak automated probe results and PyRIT manual red team scenarios rather than as standalone pass/fail signals.

Promptfoo assessments evaluate model behavior under:

- Jailbreak attempts
- Prompt injection
- Safety filter bypasses
- Insider threat scenarios
- Harmful or restricted task requests
- Manipulative or misleading instructions

Promptfoo supports structured evaluations defined in YAML configuration files specifying target model, adversarial prompts, expected outcomes, evaluation logic, and organized test suites.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MEASURE 2.6 — structured adversarial evaluation and robustness testing |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — LLM Prompt Injection |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling |
| ISO/IEC 42001 | Clause 8 — AI system behavioral testing and evaluation |
| NIST SP 800-53 | SA-11 — Developer Testing and Evaluation |

---

## Typical Workflow

1. Create a `redteam.yaml` or equivalent configuration file
2. Define adversarial prompts and expected behavioral outcomes
3. Execute Promptfoo against the locally hosted target model
4. Review results in JSON, tabular, or HTML formats
5. Summarize findings for risk analysis, framework mapping, and mitigation planning

---

## Files in This Directory

| File | Purpose |
|---|---|
| `example-redteam-config.yaml` | Example Promptfoo configuration illustrating common adversarial test scenarios, LLM-rubric assertions, and structured evaluation patterns |
