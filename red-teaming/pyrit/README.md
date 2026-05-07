# PyRIT-Inspired Red Team Testing

This folder documents PyRIT-inspired adversarial security testing conducted as part of Stage 3 of the AI Security Assurance Lifecycle. All testing is performed against locally hosted models to maintain chain of custody over assessment data, prompts, and findings.

## Important Note on Tooling

The script in this folder (`pyrit_security_tests.py`) implements PyRIT-inspired methodology using the HuggingFace Transformers pipeline for local model inference. It follows PyRIT's core architectural patterns — defined attack categories, keyword-based harmful indicator detection, and structured JSON output — without requiring the full Microsoft PyRIT library. This approach was selected to enable fully local execution against locally hosted models with no external API dependencies.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MEASURE 2.6 — robustness testing and adversarial behavioral evaluation |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — LLM Prompt Injection; AML.T0043 — Craft Adversarial Examples |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling; LLM06 — Sensitive Information Disclosure |
| ISO/IEC 42001 | Clause 8 — AI system behavioral testing and evaluation |
| NIST SP 800-53 | SA-11 — Developer Testing and Evaluation; CA-8 — Penetration Testing |

---

## What This Testing Covers

PyRIT-inspired testing evaluates model behavior across eight adversarial attack categories:

| Category | Description |
|---|---|
| `prompt_injection` | Direct instruction override attempts |
| `jailbreak` | DAN-style and persona-based jailbreak attempts |
| `harmful_content` | Harmful or restricted content generation probes |
| `misinformation` | Medical and factual misinformation probes |
| `data_extraction` | Training data and system prompt extraction attempts |
| `role_play_bypass` | Roleplay-based safety restriction bypasses |
| `encoding_bypass` | Base64-encoded instruction injection |
| `social_engineering` | Authority-based social engineering attempts |

---

## Evaluation Architecture

Each test case produces a structured evaluation containing:

- **Generated text** — model output following the adversarial prompt
- **Harmful indicator detection** — keyword-based flagging against a defined indicator list
- **Verdict** — PASS (no harmful indicators detected) or FAIL (indicators present)
- **Summary** — aggregate results across all test cases

Results are exported to a structured JSON file for downstream reporting and lifecycle integration.

---

## Typical Workflow

1. Activate the assessment environment (`ai_security_venv`)
2. Ensure the target model is available in the local model directory
3. Execute the test script against the target model
4. Review terminal output and exported JSON results
5. Document findings with framework mappings and severity assessments
6. Integrate results into the Stage 3 consolidated findings

---

## Files in This Directory

| File | Purpose |
|---|---|
| `pyrit_security_tests.py` | PyRIT-inspired adversarial test harness — 8 attack categories against locally hosted models |
| `example-pyrit-results.md` | Synthetic example illustrating how PyRIT-inspired results are interpreted and documented |

---

## Important Notes

Real assessment outputs, model-generated responses, and JSON results files are stored locally and are not committed to this repository. The script and example document demonstrate methodology and assessment structure only.
