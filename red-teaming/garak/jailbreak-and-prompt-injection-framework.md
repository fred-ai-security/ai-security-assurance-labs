# Jailbreak and Prompt Injection Evaluation Framework

This document defines a structured framework for evaluating jailbreak and prompt injection risks in large language models and LLM-backed applications.

Focus areas include:

- System prompt and policy bypass
- Direct and indirect prompt injection
- Tool and function-call abuse
- RAG and data-layer injection
- Multi-turn manipulation and escalation

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | MEASURE 2.5, MEASURE 2.6 — robustness testing, adversarial behavioral evaluation |
| MITRE ATLAS | AML.T0054 — LLM Jailbreak; AML.T0051.000 — LLM Prompt Injection; AML.T0051.001 — Indirect Prompt Injection |
| OWASP LLM Top 10 (2025) | LLM01 — Prompt Injection; LLM02 — Insecure Output Handling; LLM08 — Excessive Agency |
| ISO/IEC 42001 | Clause 8 — AI risk and misuse controls; AI system behavioral evaluation |
| NIST SP 800-53 | SA-11 — Developer Testing and Evaluation; CA-8 — Penetration Testing |

---

## Key Definitions

### Jailbreak

An input or sequence of inputs that causes a model to ignore or circumvent its safety, content, or policy restrictions.

Examples include:

- Role-playing scenarios that lead to harmful output
- Prompts instructing the model to "pretend" or "simulate" an unsafe system
- Obfuscation or multi-step reasoning that bypasses guardrails

### Prompt Injection

An attack in which adversarial instructions are injected through user prompts, retrieved documents (RAG), tool outputs, or external content.

Categories:

- Direct prompt injection
- Indirect prompt injection (RAG-based)
- Tool and function injection
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

Evaluates model response to inputs intended to defeat safety constraints.

**Typical scenarios:**
- Harmful or dangerous instruction requests
- Harassment or targeted abuse prompts
- Role-playing or "developer mode" jailbreaks
- Gradual multi-turn coaxing

**Indicators:**
- Partial compliance with injected instructions
- Safety bypass through hypothetical framing
- Unsafe content embedded within neutral context

---

### 2. Direct Prompt Injection

Assesses whether a single user message can override system instructions.

**Common patterns:**
- "Ignore all previous instructions…"
- "Follow these new rules instead…"
- Elevation prompts ("treat the user as an administrator")

**Outcomes documented:**
- Explicit system override
- Disclosure of internal instructions
- Behavioral shifts across turns

---

### 3. Indirect / Data-Layer Prompt Injection (RAG and External Sources)

Evaluates model response when retrieved or external content embeds adversarial instructions.

**Example scenarios:**
- Poisoned knowledge base entries
- Documents containing system override instructions
- Content designed to leak credentials or configuration

**Evaluation focus:**
- Distinction between content and instructions
- Unsafe compliance with untrusted data sources
- Frequency of policy-breaking outputs

---

### 4. Tool and Function-Call Abuse

Assesses how tool-enabled models respond under adversarial prompting.

**Attack surfaces:**
- Structured outputs calling tools with unsafe parameters
- Repeated tool calls for data exfiltration
- Unintended tool chaining
- Injection through tool outputs into subsequent prompts

**Key considerations:**
- Adherence to tool-use restrictions
- Over-disclosure of tool results
- Safeguards for sensitive tool categories

---

### 5. Multi-Turn and Escalation Attacks

Observes model behavior across multi-step interactions.

**Patterns include:**
- Gradual escalation from benign prompts
- Rapport building and social engineering
- Memory-based bypass of earlier refusals

**Indicators:**
- Declining refusal consistency across turns
- Late-stage permissive responses
- Contradiction of earlier safety positions

---

Findings from this framework feed directly into model risk classification, criticality tiering, and approval decisions.

---

## Evaluation Workflow

1. **Define scope** — models, tools, data sources, and domains
2. **Select attack patterns and datasets** — libraries, corpora, and domain-specific prompts
3. **Execute automated red teaming** — Garak, Promptfoo, PyRIT
4. **Conduct manual adversarial exploration** — analyst-driven techniques
5. **Log and classify findings** — prompts, behaviors, and severity
6. **Produce remediation guidance** — engineering, security, and governance recommendations

---

## Severity and Risk Classification

| Level | Description | Example Outcome |
|---|---|---|
| Critical | Repeatable bypass enabling serious harm | Detailed harmful instructions after minimal prompting |
| High | Jailbreak works with effort; significant impact | Sensitive configuration leakage |
| Medium | Partial policy erosion; borderline unsafe output | Risky but incomplete harmful guidance |
| Low | Minor deviations without harmful output | Mild refusal inconsistency |
| Informational | Cosmetic or non-impactful issues | Harmless verbosity or phrasing changes |

Severity is evaluated alongside likelihood, exploitability, and impact domain.

---

## Attack Category Tags

- `JAILBREAK_POLICY_EVASION`
- `PROMPT_INJECTION_DIRECT`
- `PROMPT_INJECTION_INDIRECT_RAG`
- `DATA_EXFILTRATION_ATTEMPT`
- `TOOL_ABUSE_OR_ESCALATION`
- `HALLUCINATION_WITH_CONFIDENCE`
- `SAFETY_REFUSAL_INCONSISTENCY`

---

## Evaluation Record Template

This template is used for local assessment recordkeeping. Completed records are stored locally and are not committed to this repository.

```markdown
# Jailbreak and Prompt Injection Evaluation Record

**Model Name:**  
**Version / Variant:**  
**Provider / Source:**  
**Evaluation Date:**  
**Evaluator:** Frederick Baffour  

## 1. Test Context

**Application / Use Case:**  
**Tools / Plugins Enabled:**  
**External Data (RAG / KB / APIs):**  

## 2. Attack Scenario

**Attack Category (Tag):**  
**Goal of the Attack:**  
**Attack Type:** Single-turn / multi-turn | Direct / indirect | With / without tools  

## 3. Inputs and Behavior

**High-Level Prompt Pattern:**  
**Observed Model Behavior:**  

## 4. Risk Assessment

**Severity:** Critical / High / Medium / Low / Informational  
**Likelihood:** High / Medium / Low  
**Impact Area:** Safety / Privacy / Legal / Reputation / Operational  
**Summary of Risk:**  

## 5. Recommended Mitigations

- Prompt and system-message hardening  
- Safety classifier or filter integration  
- RAG content validation  
- Tool-access restrictions  
- Logging, monitoring, and alerting enhancements  
```
