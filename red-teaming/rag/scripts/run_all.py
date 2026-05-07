# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Frederick Baffour
"""
run_all.py
Phase 2 — Master Attack Runner
AI Security Assurance Lifecycle — Frederick Baffour
Local Lab Environment | LangChain + ChromaDB + Ollama

USAGE:
  # Run all four attack categories
  python run_all.py

  # Run a specific attack only
  python run_all.py --attack direct
  python run_all.py --attack poison
  python run_all.py --attack stuffing
  python run_all.py --attack jailbreak

  # Skip Excel export (terminal output only)
  python run_all.py --no-excel

WHAT THIS DOES:
  1. Loads your RAG pipeline (rag_pipeline.py must be in parent directory)
  2. Runs each attack module in sequence
  3. Logs all findings to terminal in real time
  4. Exports a formatted Excel finding library on completion

ATTACK MODULES:
  Attack 1 — direct_injection.py    : Direct prompt injection via user query
  Attack 2 — retrieval_poisoning.py : Indirect injection via poisoned doc chunks
  Attack 3 — context_stuffing.py    : Context window flooding and contradiction
  Attack 4 — jailbreak_retrieval.py : Safety bypass via retrieved document content
"""

import sys
import argparse
import datetime
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────────────
PHASE2_DIR = Path(__file__).parent
sys.path.insert(0, str(PHASE2_DIR))
sys.path.insert(0, str(PHASE2_DIR.parent))

# ── Imports ───────────────────────────────────────────────────────────────────
from rag_pipeline import load_vectorstore
import findings_logger as logger

def banner():
    print(f"""
{'='*70}
  PHASE 2 — ADVERSARIAL PROMPT INJECTION HARNESS
  AI Security Assurance Lifecycle — Frederick Baffour
  Local Lab Environment | LangChain + ChromaDB + Ollama
  Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}

  ATTACK COVERAGE:
  [1] Direct Prompt Injection      — OWASP LLM01 | ATLAS AML.T0051.000
  [2] Retrieval Poisoning          — OWASP LLM01 | ATLAS AML.T0051.001
  [3] Context Stuffing             — OWASP LLM01, LLM04 | ATLAS AML.T0029
  [4] Jailbreak via Retrieved Doc  — OWASP LLM01, LLM02 | ATLAS AML.T0054

  TARGET: RAG pipeline (rag_pipeline.py)
  VECTOR STORE: ChromaDB (./chroma_db)
  LLM: mistral:v0.3 | EMBED: nomic-embed-text:v1.5
{'='*70}
""")


def run_attack(name: str, module_func, db=None, label: str = ""):
    print(f"\n{'─'*70}")
    print(f"  STARTING: {label}")
    print(f"{'─'*70}")
    try:
        return module_func(db=db)
    except Exception as e:
        print(f"[ERROR] {label} failed to run: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(
        description="Phase 2 Adversarial Harness — Frederick Baffour"
    )
    parser.add_argument(
        "--attack",
        choices=["direct", "poison", "stuffing", "jailbreak", "all"],
        default="all",
        help="Which attack to run (default: all)"
    )
    parser.add_argument(
        "--no-excel",
        action="store_true",
        help="Skip Excel export (terminal output only)"
    )
    args = parser.parse_args()

    banner()

    # ── Load shared vectorstore for attacks that use the clean RAG pipeline ───
    print("[*] Loading RAG vector store ...")
    try:
        db = load_vectorstore()
        print("[+] Vector store loaded successfully\n")
    except Exception as e:
        print(f"[ERROR] Could not load vector store: {e}")
        print("       Make sure you have run rag_pipeline.py at least once to build the store.")
        sys.exit(1)

    # ── Import attack modules ──────────────────────────────────────────────────
    import direct_injection
    import retrieval_poisoning
    import context_stuffing
    import jailbreak_retrieval

    attack_map = {
        "direct":   (direct_injection.run,    "Attack 1: Direct Prompt Injection"),
        "poison":   (retrieval_poisoning.run,  "Attack 2: Retrieval Poisoning"),
        "stuffing": (context_stuffing.run,     "Attack 3: Context Stuffing"),
        "jailbreak":(jailbreak_retrieval.run,  "Attack 4: Jailbreak via Retrieved Content"),
    }

    # ── Run selected attacks ───────────────────────────────────────────────────
    all_results = []
    if args.attack == "all":
        for key, (func, label) in attack_map.items():
            results = run_attack(key, func, db=db, label=label)
            all_results.extend(results)
    else:
        func, label = attack_map[args.attack]
        results = run_attack(args.attack, func, db=db, label=label)
        all_results.extend(results)

    # ── Final output ──────────────────────────────────────────────────────────
    logger.print_summary()

    if not args.no_excel:
        logger.export_excel()
        print(f"\n[+] Finding library saved to: {logger.EXCEL_PATH}")
        print(f"    Open in Excel or LibreOffice Calc to review.")

    print(f"\n{'='*70}")
    print(f"  Phase 2 complete. {len(all_results)} total tests executed.")
    print(f"  Next step: Review findings, document mitigations, advance to consolidated reporting.")
    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
