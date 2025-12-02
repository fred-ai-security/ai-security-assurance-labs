# Promptfoo – Scenario-Based LLM Red Teaming

Promptfoo is used to perform scenario-driven adversarial evaluations against language models.  
It assesses model behavior under:

- Jailbreak attempts  
- Prompt injection  
- Safety filter bypasses  
- Insider threat scenarios  
- Harmful or restricted task requests  
- Manipulative or misleading instructions  

Promptfoo supports structured evaluations defined in YAML configuration files that specify:

- Target model  
- Adversarial prompts  
- Expected outcomes  
- Evaluation logic  
- Organized test suites  

---

## Typical Workflow

1. Create a `redteam.yaml` or equivalent configuration file.  
2. Define adversarial prompts and expected results.  
3. Execute Promptfoo against the chosen model.  
4. Review results in JSON, tabular, or HTML formats.  
5. Summarize findings for risk analysis and mitigation planning.

---

## Files in This Directory

- `example-redteam-config.yaml` – Example Promptfoo configuration with common adversarial test scenarios.
