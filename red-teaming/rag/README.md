# RAG Adversarial Test Harness
By: Frederick Baffour

Phase 2 — LLM Red Teaming Against a Retrieval-Augmented Generation Pipeline

A hands-on adversarial test harness that runs four distinct attack classes against a local RAG pipeline, validates the results with an independent LLM judge, and exports structured findings for governance review.

I built this harness as Phase 2 of my AI Security Assurance Lifecycle. It runs end-to-end attacks against a local Retrieval-Augmented Generation pipeline and uses a separate LLM as an independent judge to verify whether each attack succeeded. The structure mirrors how I do real AI red team work — defined attack scope, repeatable execution, independent verification, and clear documentation of results.

I run this on my own lab hardware (RTX 4050, 6GB VRAM, Ubuntu / WSL2), so every test, every error, and every fix is something I have hands-on experience with.

## 🧠 What I Built and Why

I built this harness to answer four practical questions about a RAG system before it goes near production:

1. Can an attacker hijack the system through the user query? (Direct Prompt Injection)
2. Can an attacker poison the retrieval pipeline so it returns adversarial content? (Indirect Injection via Retrieval)
3. Can an attacker overwhelm the context window to bury or override the system prompt? (Context Stuffing)
4. Can an attacker jailbreak the model through retrieved documents the user thinks are trusted? (Jailbreak via Retrieved Content)

For each question, I designed test cases that map to OWASP LLM Top 10 (2025) and MITRE ATLAS TTPs, ran them against the target, and used an independent judge model to confirm the outcome.

## 🏗️ Architecture

```
User Query
    ↓
RAG Pipeline (Mistral 7B v0.3 + nomic-embed-text + ChromaDB)   ← TARGET
    ↓
RAG Response
    ↓
Llama 3.1 8B Instruct (q4_K_M)                                 ← INDEPENDENT JUDGE
    ↓
Verdict: EXPLOITABLE / PARTIAL / MITIGATED
    ↓
Findings Logger → phase2_findings.xlsx
```

I keep the judge model fully outside the RAG pipeline. It does not see the knowledge base or the vector store — only the attacker prompt and the model's response. I made this choice because a model evaluating its own output systematically under-reports failure. The pattern matches how Garak separates probes and detectors, and how Microsoft PyRIT separates targets and scorers.

## 🧰 Tools, Models & Licenses

### Models I Use

| Component | Model | License |
|---|---|---|
| RAG Target LLM | Mistral 7B v0.3 | Apache 2.0 |
| Embeddings | nomic-embed-text v1.5 | Apache 2.0 |
| LLM Judge | Llama 3.1 8B Instruct (q4_K_M) | Meta Llama 3.1 Community License |

### Supporting Stack

- Vector Store: ChromaDB
- Orchestration: LangChain (pinned to v0.2.16)
- Local Runtime: Ollama
- Hardware: RTX 4050 (6GB VRAM)
- OS: Ubuntu (WSL2)

I document the reasoning behind each model and version choice in DECISIONS.md.

## 📂 File Inventory

### Phase 1 — RAG Target System (1 file)

| File | Purpose |
|---|---|
| rag_pipeline.py | HyDE-based retrieval pipeline. Loads documents, generates embeddings, persists vectors to ChromaDB, and exposes a query interface backed by Mistral 7B. This is the system under test. |

### Phase 2 — Adversarial Harness (7 files)

| File | Attack Class | Test Cases | Framework Mapping |
|---|---|---|---|
| run_all.py | Master orchestrator | — | — |
| direct_injection.py | Direct Prompt Injection | 7 | OWASP LLM01 / MITRE AML.T0051.000 |
| retrieval_poisoning.py | Indirect Injection via Retrieval | 3 | OWASP LLM01 / MITRE AML.T0051.001 |
| context_stuffing.py | Context Window Flooding | 4 | OWASP LLM01, LLM04 / MITRE AML.T0029 |
| jailbreak_retrieval.py | Jailbreak via Retrieved Content | 4 | OWASP LLM01, LLM02 / MITRE AML.T0054 |
| llm_judge.py | Independent verdict module | — | — |
| findings_logger.py | Excel + terminal export | — | — |

Total: 18 adversarial test cases across four attack classes.

## 📊 Findings Output

The harness writes results to phase2_findings.xlsx with four sheets:

1. **Summary Dashboard** — Aggregate counts by verdict, attack class, and severity
2. **All Findings** — Per-test record with judge confidence and reasoning
3. **False Positive Analysis** — Cases where keyword matching disagrees with the judge verdict (in either direction). I added this sheet because keyword-only matching produced too many false positives in early runs and missed several semantic compliance failures the judge caught.
4. **Framework Reference** — OWASP LLM Top 10 + MITRE ATLAS + NIST AI RMF crosswalk

## 🔄 NIST AI RMF Alignment

| Function | Subcategory | How I Address It |
|---|---|---|
| GOVERN | GV-1.2 | Documented adversarial test policy applied consistently across runs |
| MAP | MP-5.1 | Attack surface and threat-actor TTPs identified for each test class |
| MEASURE | ME-2.5 | Robustness measured through repeatable adversarial testing with confidence-scored verdicts |

## 🚀 How to Run

```bash
conda activate rag_env
cd ~/rag-project/
python run_all.py
```

Output is written to `~/rag-project/findings/phase2_findings.xlsx`.

For setup details and prerequisites, see the [Lab Setup README](../../docs/lab-setup.md).

## 📝 Notes on Methodology

- I scope this harness for demonstration and methodology. It runs against a known RAG architecture with documented attacker assumptions.
- I designed the attack prompts and judge logic to be reproducible across runs.
- I refined the harness iteratively across multiple versions of the underlying lifecycle reference, driven by real assessment outputs and the errors I encountered along the way.
- I document the engineering trade-offs — model selection, judge architecture, isolation strategy for retrieval-modifying attacks, and known limitations — in DECISIONS.md.

---

*Part of the [AI Security Assurance Labs](https://github.com/fred-ai-security/ai-security-assurance-labs) portfolio. See repository root DEVELOPMENT_NOTES.md for AI-assisted development disclosure.*
