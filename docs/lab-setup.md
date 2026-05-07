# Lab Setup — AI Security Assurance Labs

> **Environment:** Local Workstation | Ubuntu 24.04 (WSL2 on Windows 11) | NVIDIA RTX 4050 (6GB VRAM)

This document covers the hardware, software, and configuration prerequisites for running the assessment harnesses in this repository. All testing was performed locally to preserve chain of custody — no cloud model endpoints were used as red team targets.

---

## Hardware

| Component | Specification |
|-----------|---------------|
| Host OS | Windows 11 |
| Runtime | WSL2 (Ubuntu 24.04) |
| GPU | NVIDIA RTX 4050 Laptop — 6GB VRAM |
| External Storage | External storage (exFAT) — Ollama model store |

> **VRAM note:** The 6GB constraint is a real architectural driver throughout this lab. Model selection, quantization levels, and agent/judge isolation decisions were all made with this ceiling in mind. See `DECISIONS.md` in each module for rationale.

---

## Ollama — Local Model Stack

All models are served locally via [Ollama](https://ollama.com). Model files are stored on an external USB drive to preserve host disk space.

```bash
# Set model storage location (add to ~/.bashrc or ~/.profile)
export OLLAMA_MODELS=/mnt/d/ollama_models

# Verify Ollama is running
ollama list
```

### Pinned Models

| Role | Model | Rationale |
|------|-------|-----------|
| Red team target | `mistral:v0.3` | Lightweight, reproducible, fits within VRAM alongside judge |
| LLM judge + agent brain | `llama3.1:8b-instruct-q4_K_M` | Instruction-following quality at Q4 quantization; runs independently from target |
| Embeddings | `nomic-embed-text:v1.5` | High-quality embeddings; ChromaDB compatible |

> The judge and target models run in isolated sequential calls — not simultaneously — to stay within the 6GB VRAM envelope.

---

## Conda Environments

Two isolated environments are used to prevent dependency conflicts between assessment stages.

### `ai_security_venv` — Stages 1, 2, 3, and 6

Used for: model intake, supply-chain scanning, base model red teaming (Garak, PyRIT, Promptfoo), and consolidated reporting.

```bash
conda activate ai_security_venv
```

**Key pins:**

```
garak==0.14.1
litellm==1.82.6          # hard pin — garak 0.14.1 dependency; do not upgrade
openai>=2.0,<3.0
langchain-core>=0.2.10,<2.0.0
```

> **AR-001 (Accepted Risk):** `litellm==1.82.6` carries known CVEs that cannot be resolved without breaking `garak 0.14.1`. This is a documented accepted risk. Upgrading may impact compatibility and should be validated before any changes.

### `rag_env` — Stages 4 and 5

Used for: RAG pipeline security assessment and agentic AI security testing.

```bash
conda activate rag_env
```

**Key pins:**

```
langchain==0.2.16         # required for AgentExecutor / create_react_agent compatibility
langchain-community==0.2.x
chromadb
fastmcp
```

> **LangChain version lock:** Upgrading beyond `0.2.16` breaks the `AgentExecutor` and `create_react_agent` imports used in Stage 5. This is a known constraint — upgrading may impact compatibility and should be validated before any changes.

---

## Directory Structure

```
~/ai-security-labs/                    # BASE — lifecycle root
├── 00_Admin/                          # Golden reference docs
├── Stage_1_Intake/
├── Stage_2_Supply_Chain/
├── Stage_3_Red_Teaming/
├── Stage_4_RAG_Pipeline/
├── Stage_5_Agentic_AI/
└── Stage_6_Reporting/

~/rag-project/                         # RAG assessment working directory
└── chroma_db/                         # ChromaDB vector store

~/agent-project/                       # Agentic AI assessment working directory
```

---

## Supply-Chain Scanning Tools

Installed to `~/.local/bin/` — ensure this is on your PATH.

```bash
export PATH="$HOME/.local/bin:$PATH"

# Verify tools
syft --version
grype --version
```

| Tool | Purpose |
|------|---------|
| `syft` | SBOM generation (CycloneDX / SPDX) |
| `grype` | Vulnerability scanning against SBOM |
| `trivy` | Secrets scanning, filesystem CVE scan |

> **AR-002 (Accepted Risk):** `ffmpeg 8.0.1` binary inside the venv carries a Critical CVE (CVE-2026-40962). This is embedded in a binary — not resolvable via pip or apt within the venv scope. Documented accepted risk.

> **Trivy secrets scan:** 9 results confirmed as false positives — Garak apikey probe datasets, PyRIT scorer evaluation datasets, and PyRIT GCG Dockerfile entries. None represent real credentials.

---

## Red Teaming Tools

| Tool | Version | Usage |
|------|---------|-------|
| Garak | 0.14.1 | Automated LLM probe suite (1,280 probes across 10 attack classes) |
| PyRIT | latest | Manual red team scenarios, jailbreak orchestration |
| Promptfoo | latest | YAML-driven test harness with LLM-rubric assertions |

---

## Frameworks Referenced

All findings are mapped to the following frameworks throughout this portfolio:

- **NIST AI RMF** (GOVERN / MAP / MEASURE / MANAGE)
- **MITRE ATLAS** (AML.T0051.000, AML.T0051.001, AML.T0054, AML.T0053, AML.T0056, AML.T0041, and others)
- **OWASP LLM Top 10 (2025)**
- **NIST 800-53**
- **ISO 42001**
- **ISO 27001**

---

## Quick Start — RAG Assessment Harness

```bash
conda activate rag_env
cd ~/rag-project/
python run_all.py
```

Output: `~/rag-project/findings/phase2_findings.xlsx`

---

## Quick Start — Agentic AI Harness

```bash
conda activate rag_env
cd ~/agent-project/
# Start FastMCP server (separate terminal)
python mcp_server.py

# Run attack harness
promptfoo eval --config agentic_harness_v1.yaml
```

---

## AI-Assisted Development Disclosure

This repository was developed using AI-assisted workflows as part of the engineering process. All outputs were reviewed, validated against actual execution results, and iteratively refined.

All methodology, findings, and engineering decisions are the author's own.

See `DEVELOPMENT_NOTES.md` at the repository root for additional context.

---

*Part of the [AI Security Assurance Labs](https://github.com/fred-ai-security/ai-security-assurance-labs) portfolio by Frederick Baffour | [AssureLayer LLC](https://assurelayersec.com)*
