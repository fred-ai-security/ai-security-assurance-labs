# Garak – LLM Vulnerability Testing

Garak is used for automated vulnerability testing against language models.  
It evaluates models for:

- Jailbreak attempts  
- Prompt injection  
- Refusal bypasses  
- Toxic or harmful content generation  
- Hallucination and over-compliance behaviors  
- Undesired responses under adversarial prompts  

Garak-based testing is performed after model intake and supply-chain validation, and before final risk classification and approval decisions.

---

## Typical Workflow

1. Select a target model (local or cloud).  
2. Choose relevant probes such as jailbreak, prompt-injection, or refusal-bypass.  
3. Execute Garak and collect results in structured formats (JSON or Markdown).  
4. Interpret failures and categorize them by severity and impact.  
5. Document findings and outline potential mitigation strategies.  

---

## Files in This Directory

- `example-garak-assessment.md` – Example summary illustrating how Garak findings can be interpreted in an AI Security Assurance context.
