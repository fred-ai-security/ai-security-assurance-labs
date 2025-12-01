# Garak – LLM Vulnerability Testing

Garak is used to perform automated vulnerability testing against language models.  
It evaluates models for:

- Jailbreak attempts  
- Prompt injection  
- Refusal bypasses  
- Toxic or harmful content generation  
- Hallucination and over-compliance behaviors  
- Undesired responses under adversarial prompts  

## Typical Workflow

1. Select a target model (local or cloud).  
2. Choose specific probes (e.g., jailbreak, prompt-injection, refusal-bypass).  
3. Run Garak and collect results in JSON or Markdown format.  
4. Analyze failures, categorize them by severity, and interpret risk.  
5. Prepare mitigation recommendations or guardrail strategies.

## Files in This Directory

- `example-garak-assessment.md` – Example output summary from a Garak test run  
