# 🧭 Engineering Decisions — RAG Adversarial Test Harness

This is the record of the major engineering decisions I made while building the Phase 2 RAG adversarial test harness, the trade-offs I accepted, and the lessons I learned along the way. I wrote it for technical reviewers who want to understand *why* the harness is built the way it is and to document the reasoning behind choices that affect reproducibility and findings quality.

---

## Decision 1 — I Chose Llama 3.1 8B Instruct (q4_K_M) Over GPT-OSS 20B for the Judge

I started with GPT-OSS 20B as the LLM judge. I switched to Llama 3.1 8B Instruct (q4_K_M quantization) once I hit the VRAM ceiling.

**What happened:** GPT-OSS 20B exceeded available VRAM on my lab hardware (RTX 4050, 6GB) when I ran it concurrently with Mistral 7B as the target. Forcing the judge to swap in and out of VRAM caused 500-level errors from Ollama and produced incomplete judge verdicts on several tests. I confirmed this by re-running the same test set with a smaller judge — Llama 3.1 8B Instruct (q4_K_M) fits in 6GB alongside Mistral 7B and produces stable verdicts across all 18 test cases.

**The trade-off I accepted:** A smaller judge has less reasoning depth than GPT-OSS 20B. I mitigated this two ways: I extended the judge timeout to 120 seconds to give VRAM swap room to settle, and I added a structured PREFIX COMPLIANCE detection rule to the judge prompt to catch attacks that embed compliance markers in their output (the kind of cases where a smaller judge would otherwise miss the exploit).

---

## Decision 2 — I Kept the Judge Fully Separate from the RAG Pipeline

The judge model never touches the knowledge base, the vector store, or the system prompt. It only sees two things: the attacker's prompt and the target model's response.

**Why I did this:** A model evaluating its own output systematically under-reports failure. I want defensible findings, so the evaluator has to be independent. Garak uses the same separation between probes and detectors. Microsoft PyRIT uses it between targets and scorers. I followed the same pattern because it's the right one.

The judge returns a structured verdict (`EXPLOITABLE` / `PARTIAL` / `MITIGATED`), a confidence score, and a reasoning string for every test case.

---

## Decision 3 — I Isolated Each Retrieval-Modifying Test in Its Own Temp Directory

The retrieval poisoning and jailbreak-via-retrieval tests modify the ChromaDB store. Without isolation, ChromaDB raised `code 1032 attempt to write a readonly database` errors because the lock from the previous test had not released.

**What I did:** I rewrote those modules to use `tempfile.mkdtemp()` for a fresh ChromaDB directory per test, then `shutil.rmtree()` for forced cleanup after each test. I added a 0.5-second pause between cleanup and the next test to make sure the lock fully released before the next directory was created.

**The trade-off:** Each test runs slightly slower because of the temp setup and teardown. I accepted that because it gave me clean, independent runs without state cross-contamination — which matters more than test speed in an assurance harness.

---

## Decision 4 — I Run Two Verdict Layers Side-by-Side: Keyword and Judge

Every test case produces both a keyword-match verdict and a judge verdict, captured next to each other in the findings output.

**Why:** Keyword matching is fast but produces high false-positive rates against modern LLM responses. The judge model catches the semantic compliance failures that keyword matching misses. By logging both, I get a *False Positive Analysis* sheet that highlights every case where the two methods disagree — and that disagreement is itself a finding worth showing to a security team. Over-reliance on keyword detectors is a real enterprise weakness, and this harness surfaces it directly.

**What I learned:** I kept finding cases where keyword matching said `MITIGATED` but the judge said `EXPLOITABLE` — base64-encoded payloads, prefix-compliance attacks, gradual-escalation attacks. I also found the reverse, where keywords flagged a benign response that happened to contain a trigger string in non-exploit context. The lesson: I do not trust a single layer of detection, and neither should the systems my findings will inform.

---

## Decision 5 — I Pinned LangChain to v0.2.16

LangChain 0.3+ refactored `AgentExecutor` and `create_react_agent`, which I rely on in Stage 5 of the broader lifecycle (Agentic AI Security Assessment). Pinning to 0.2.16 keeps the full lifecycle compatible while I evaluate the migration separately. The deprecation warnings show up at runtime but they do not affect harness output, and I suppress them with `PYTHONWARNINGS=ignore`.

---

## Decision 6 — I Export Findings to Excel, Not JSON

The findings file is `phase2_findings.xlsx` with four sheets (Summary Dashboard, All Findings, False Positive Analysis, Framework Reference) — not a JSON dump.

**Why Excel:** The audience for these findings is governance, audit, and security engineering teams. They consume Excel natively. Excel gives me color-coded severity, embedded reasoning text, and direct copy/paste into compliance reports. JSON output is generated downstream by the lifecycle's `generate_mitigations_v3.py` script for programmatic consumption — I keep them as separate concerns.

---

## Decision 7 — What's In Scope, What I Deliberately Left Out

**In scope:**
- Adversarial testing of the RAG retrieval and inference layers
- Documentation of attack-class outcomes against a known target architecture
- Mapping every test to OWASP LLM Top 10 (2025), MITRE ATLAS, and NIST AI RMF

**Out of scope:**
- Testing of the embedding model itself — I treat nomic-embed-text as trusted infrastructure
- Network-level attacks against the Ollama runtime
- Attacks requiring fine-tuning or model weight access
- Production-scale stress testing or cost analysis

Keeping these boundaries explicit makes the harness easier to defend in review and easier to extend later.

---

## What I Have Not Yet Built

- The harness runs against a single target model (Mistral 7B v0.3). I plan to add multi-target comparison.
- The 18 published test cases cover four attack classes. I keep the broader adversarial prompt library I use for engagement work out of this repository.
- The judge model has its own biases. I want to add multi-judge consensus voting.
- All tests run single-tenant on local hardware. I have not modeled multi-tenant adversarial scenarios here.

---

## Development Disclosure

I developed the scripts in this directory iteratively with AI assistance (Claude, ChatGPT) under my direction. The architectural decisions, model selections, framework mappings, validation outcomes, and integration logic are my own. I reviewed and ran every script on my local hardware and validated outputs across multiple iterations. The full disclosure framing is in the repository-root [`DEVELOPMENT_NOTES.md`](../../DEVELOPMENT_NOTES.md).

---

*Frederick Baffour — AI Security Assurance Engineer*
