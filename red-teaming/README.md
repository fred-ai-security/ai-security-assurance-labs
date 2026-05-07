# LLM Red Teaming

This section contains materials related to red teaming large language models as part of Stage 3 of the AI Security Assurance Lifecycle. It covers automated, scenario-driven, and PyRIT-inspired adversarial testing used to evaluate model robustness, safety alignment, and resistance to harmful or unintended behavior.

Red-teaming activities occur after model intake and supply-chain validation (Stages 1–2) and inform RAG pipeline security assessment, agentic AI evaluation, risk classification, and approval decisions (Stages 4–6).

For full methodology, framework alignment, and tool stack documentation see [`llm-red-teaming-overview.md`](./llm-red-teaming-overview.md).

---

## Subdirectories

| Folder | Contents |
|---|---|
| `garak/` | Garak configurations, synthetic assessment examples, and jailbreak/prompt injection framework |
| `promptfoo/` | Promptfoo configuration files and scenario-driven adversarial evaluation setup |
| `rag/` | RAG pipeline adversarial test harness — four attack classes, LLM judge architecture, findings output |
| `pyrit/` | PyRIT-inspired adversarial test harness — eight attack categories, local Transformers execution |
