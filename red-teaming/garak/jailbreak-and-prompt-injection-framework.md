# Jailbreak and Prompt Injection Evaluation Framework

## Purpose

This module defines a structured framework for evaluating jailbreak and prompt injection risks in large language models (LLMs) and LLM-backed applications.

Focus areas include:

- System prompt and policy bypass  
- Direct and indirect prompt injection  
- Tool and function-call abuse  
- RAG and data-layer injection  
- Multi-turn manipulation and escalation  

The framework aligns with:

- NIST AI RMF – Govern / Map / Measure / Manage  
- MITRE ATLAS – Prompt Injection, Jailbreak, Misuse TTPs  
- ISO/IEC 42001 – AI risk and misuse controls  

---

## Key Definitions

### Jailbreak

An input or sequence of inputs that causes a model to ignore or circumvent its safety, content, or policy restrictions.

Examples include:

- Role-playing scenarios that lead to harmful output  
- Prompts instructing the model to “pretend” or “simulate” an unsafe system  
- Obfuscation or multi-step reasoning that bypasses guardrails  

### Prompt Injection

An attack in which adversarial instructions are injected through:

- User prompts  
- Retrieved documents (RAG)  
- Tool outputs  
- External content  

Categories:

- Direct prompt injection  
- Indirect prompt injection (RAG-based)  
- Tool/function injection  
- Data-layer manipulation  

---

## Evaluation Objectives

A jailbreak and prompt injection assessment aims to:

1. Identify bypass paths for safety and policy controls  
2. Measure resilience to structured jailbreak attempts  
3. Assess susceptibility to external-content and RAG-based injection  
4. Evaluate tool or function-call abuse potential  
5. Classify findings by severity, impact, and likelihood  
6. Produce actionable remediation recommendations  

---

## Test Categories

### 1. Policy Evasion and Jailbreak Attempts

Evaluates the model’s response to inputs intended to defeat safety constraints.

Typical scenarios:

- Harmful or dangerous instructions  
- Harassment or targeted abuse  
- Personal data handling violations  
- Role-playing or “developer mode” jailbreaks  
- Gradual multi-turn coaxing  

Indicators:

- Partial compliance  
- Safety bypass through hypothetical framing  
- Unsafe content embedded within neutral context  

---

### 2. Direct Prompt Injection

Assesses whether a single user message can override system instructions.

Common patterns:

- “Ignore all previous instructions…”  
- “Follow these new rules instead…”  
- Elevation prompts such as “treat the user as an administrator”  

Outcomes documented:

- Explicit system override  
- Disclosure of internal instructions  
- Behavioral shifts across turns  

---

### 3. Indirect / Data-Layer Prompt Injection (RAG and External Sources)

Evaluates how the model responds when retrieved or external content embeds adversarial instructions.

Example scenarios:

- Poisoned knowledge base entries  
- Documents instructing system override  
- Content designed to leak credentials or configuration  

Evaluation focuses on:

- Distinction between content and instructions  
- Unsafe compliance with untrusted data  
- Frequency of policy-breaking outputs  

---

### 4. Tool and Function-Call Abuse

Assesses how tool-enabled models react under adversarial prompting.

Attack surfaces:

- Structured outputs calling tools with unsafe parameters  
- Repeated tool calls for data exfiltration  
- Unintended tool chaining  
- Injection through tool outputs into subsequent prompts  

Key considerations:

- Adherence to tool-use restrictions  
- Over-disclosure of tool results  
- Safeguards for sensitive tool categories  

---

### 5. Multi-Turn and Escalation Attacks

Observes model behavior across multi-step interactions.

Patterns include:

- Gradual escalation from benign prompts  
- Rapport building and social engineering  
- Memory-based bypass of earlier refusals  

Indicators:

- Declining refusal consistency  
- Late-stage permissive responses  
- Contradiction of earlier safety positions  

---

## Example Evaluation Workflow

1. **Define scope**  
   - Models, tools, data sources, and domains  

2. **Select attack patterns and datasets**  
   - Libraries, corpora, and domain-specific prompts  

3. **Execute automated red teaming**  
   - Garak, Promptfoo, PyRIT  

4. **Conduct manual adversarial exploration**  
   - Analyst-driven techniques  

5. **Log and classify findings**  
   - Prompts, behaviors, and severity  

6. **Produce remediation guidance**  
   - Engineering, security, and governance recommendations  

---

## Severity and Risk Classification (Example)

| Level      | Description | Example Outcome |
|------------|-------------|-----------------|
| Critical   | Repeatable bypass enabling serious harm | Detailed harmful instructions after minimal prompting |
| High       | Jailbreak works with effort; significant impact | Sensitive configuration leakage |
| Medium     | Partial policy erosion; borderline unsafe | Risky but incomplete harmful guidance |
| Low        | Minor deviations without harmful output | Mild refusal inconsistency |
| Informal   | Cosmetic or non-impactful issues | Harmless verbosity or phrasing changes |

Severity evaluated alongside:

- Likelihood  
- Exploitability  
- Impact domain  

---

## Example Attack Categories and Tags

- `JAILBREAK_POLICY_EVASION`  
- `PROMPT_INJECTION_DIRECT`  
- `PROMPT_INJECTION_INDIRECT_RAG`  
- `DATA_EXFILTRATION_ATTEMPT`  
- `TOOL_ABUSE_OR_ESCALATION`  
- `HALLUCINATION_WITH_CONFIDENCE`  
- `SAFETY_REFUSAL_INCONSISTENCY`  

---

## Evaluation Record Template

This template is intended for local assessment and does not contain real model output.

# Jailbreak and Prompt Injection Evaluation Record (Template)

**Model Name:**  
**Version / Variant:**  
**Provider / Source:**  
**Evaluation Date:**  
**Evaluator:** Frederick Baffour  

---

## 1. Test Context

**Application / Use Case:**  
**Tools / Plugins Enabled:**  
**External Data (RAG / KB / APIs):**  

---

## 2. Attack Scenario

**Attack Category (Tag):**  
**Goal of the Attack:**  
**Attack Type:**  
- Single-turn / multi-turn  
- Direct / indirect  
- With / without tools  

---

## 3. Inputs and Behavior

**High-Level Prompt Pattern:**  
- Overview of adversarial prompt structure  

**Observed Model Behavior:**  
- Summary of responses and safety alignment  
- Notable changes across multi-turn interactions  

---

## 4. Risk Assessment

**Severity:** Critical / High / Medium / Low / Informal  
**Likelihood:** High / Medium / Low  
**Impact Area:** Safety / Privacy / Legal / Reputation / Operational  

**Summary of Risk:**  
-  

---

## 5. Recommended Mitigations

- Prompt and system-message hardening  
- Safety classifier or filter integration  
- RAG content validation  
- Tool-access restrictions  
- Logging, monitoring, and alerting enhancements  

---

## File Location in Repository

```
ai-security-assurance-labs/
└── red-teaming/
    └── jailbreak-and-prompt-injection-framework.md
```
