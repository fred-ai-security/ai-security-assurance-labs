# Promptfoo – Scenario-Based LLM Red Teaming

Promptfoo is used to perform **scenario-driven adversarial testing** against language models.  
It evaluates how well models resist:

- Jailbreak attempts  
- Prompt injection  
- Safety filter bypasses  
- Insider threat prompts  
- Harmful or restricted task requests  
- Manipulative or misleading instructions  

Promptfoo allows for structured evaluations using YAML configuration files that define:

- The target model  
- Adversarial prompts  
- Expected behavior  
- Scoring criteria  
- Test suites  

---

## Typical Workflow

1. Create a `redteam.yaml` or similar config file.  
2. Define adversarial prompts and expected outcomes.  
3. Run Promptfoo against a local model (e.g., via Ollama).  
4. Review the evaluation results (JSON, table, or HTML).  
5. Summarize failures for risk assessment and mitigation planning.

---

## Files in This Directory

- `example-redteam-config.yaml` – Example Promptfoo configuration with common adversarial test cases.
