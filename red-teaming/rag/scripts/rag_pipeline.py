# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Frederick Baffour
"""
RAG Pipeline - Phase 1: Core Build (v7 - HyDE Edition)
Local Lab Environment | LangChain + ChromaDB + Ollama
AI Security Assurance Lifecycle - Frederick Baffour

WHAT IS HyDE (Hypothetical Document Embeddings)?
=================================================
Standard RAG embeds the USER QUERY and finds similar document chunks.
The problem: user queries use different vocabulary than document content.

  User asks : "Tell me about Baffour Enterprise Corporation"
  Doc chunk  : "BEC is a privately held, minority-owned enterprise..."
  → Low similarity → wrong chunk retrieved

HyDE solves this by adding one step before retrieval:
  Step 1: Ask the LLM to write a HYPOTHETICAL ANSWER to the query
  Step 2: Embed the hypothetical answer (not the raw query)
  Step 3: Use that embedding to find similar real document chunks

  User asks  : "Tell me about Baffour Enterprise Corporation"
  HyDE writes: "Baffour Enterprise Corporation (BEC) is a technology
               company that provides cybersecurity and AI services..."
  Doc chunk  : "BEC is a privately held, minority-owned enterprise..."
  → HIGH similarity → correct chunk retrieved

The hypothetical answer doesn't need to be accurate — it just needs to
use the same vocabulary and structure as real document content. The
actual answer still comes from the retrieved real chunks, not the
hypothetical document.

SECURITY NOTE FOR PHASE 2:
The HyDE generation step is itself an LLM call — which means it is
a NEW attack surface. A prompt injection in the user query could
potentially manipulate the hypothetical document generation to produce
embeddings that retrieve attacker-chosen chunks. This is worth testing.
"""

import sys
from pathlib import Path
from collections import Counter

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# ── Config ─────────────────────────────────────────────────────────────────────
OLLAMA_BASE_URL       = "http://127.0.0.1:11434"
EMBED_MODEL           = "nomic-embed-text:v1.5"
LLM_MODEL             = "mistral:v0.3"
CHROMA_DIR            = "./chroma_db"
DOCS_DIR              = "./docs"
CHUNK_SIZE            = 500
CHUNK_OVERLAP         = 100
RETRIEVER_K           = 5
RETRIEVER_FETCH_K     = 25
RETRIEVER_SEARCH_TYPE = "mmr"

# ── HyDE prompt — instructs LLM to write a hypothetical answer ─────────────────
# The key insight: this answer will be EMBEDDED, not shown to the user.
# It just needs to sound like it came from the target documents.
HYDE_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""Write a short, factual passage that would answer the following question.
Write it as if it came from a technical document or company profile.
Do not say you are generating a hypothetical document.
Just write the passage directly. Keep it under 150 words.

Question: {question}

Passage:"""
)

# ── Final answer prompt ────────────────────────────────────────────────────────
RAG_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a helpful assistant. Use ONLY the context below to answer.
If the context does not contain the answer, say "I don't know based on the provided documents."

Context:
{context}

Question: {question}

Answer:"""
)


def load_documents(docs_dir: str) -> list:
    path = Path(docs_dir)
    if not path.exists():
        path.mkdir(parents=True)
        sample = path / "sample_policy.txt"
        sample.write_text(
            "ACME Corp Security Policy v1.0\n\n"
            "1. All employees must use MFA on corporate systems.\n"
            "2. Passwords must be at least 16 characters.\n"
            "3. Sensitive data must be encrypted at rest using AES-256.\n"
            "4. Access to production systems requires manager approval.\n"
            "5. Security incidents must be reported within 1 hour.\n"
        )
        print(f"[+] Created sample doc at {sample}")

    loaders = []
    for txt in path.glob("**/*.txt"):
        loaders.append(TextLoader(str(txt)))
    for pdf in path.glob("**/*.pdf"):
        loaders.append(PyPDFLoader(str(pdf)))

    if not loaders:
        print("[-] No documents found in ./docs")
        sys.exit(1)

    docs = []
    for loader in loaders:
        try:
            docs.extend(loader.load())
        except Exception as e:
            print(f"[!] Could not load {loader}: {e}")

    print(f"[+] Loaded {len(docs)} page(s) from {docs_dir}")
    return docs


def chunk_documents(docs: list) -> list:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ".", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    print(f"[+] Split into {len(chunks)} chunks "
          f"(size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP})")

    source_counts = Counter(
        Path(c.metadata.get("source", "unknown")).name
        for c in chunks
    )
    print(f"\n[+] Chunk distribution:")
    for source, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        bar = "█" * min(count // 5, 50)
        pct = count / len(chunks) * 100
        print(f"    {source:<45} {count:>5} chunks ({pct:4.1f}%) {bar}")
    print()
    return chunks


def build_vectorstore(chunks: list) -> Chroma:
    print(f"[+] Embedding with model: {EMBED_MODEL} via Ollama ...")
    embeddings = OllamaEmbeddings(model=EMBED_MODEL, base_url=OLLAMA_BASE_URL)
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )
    print(f"[+] Vector store saved to {CHROMA_DIR}")
    return db


def load_vectorstore() -> Chroma:
    embeddings = OllamaEmbeddings(model=EMBED_MODEL, base_url=OLLAMA_BASE_URL)
    db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    print(f"[+] Loaded existing vector store from {CHROMA_DIR}")
    return db


def format_docs(docs: list) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_chain(db: Chroma):
    """
    Build a HyDE-enhanced RAG chain.

    Pipeline flow:
      user query
          │
          ▼
      HyDE LLM (mistral:v0.3)
      generates hypothetical answer
          │
          ▼
      Embed hypothetical answer
      (nomic-embed-text:v1.5)
          │
          ▼
      ChromaDB similarity search
      → retrieves real document chunks
          │
          ▼
      Format retrieved chunks as context
          │
          ▼
      RAG LLM (mistral:v0.3)
      answers using REAL context only
          │
          ▼
      Final answer to user
    """
    llm = OllamaLLM(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0.1,
    )

    embeddings = OllamaEmbeddings(
        model=EMBED_MODEL,
        base_url=OLLAMA_BASE_URL,
    )

    retriever = db.as_retriever(
        search_type=RETRIEVER_SEARCH_TYPE,
        search_kwargs={"k": RETRIEVER_K, "fetch_k": RETRIEVER_FETCH_K},
    )

    # ── HyDE retrieval chain ──────────────────────────────────────────────────
    # Step 1: Generate hypothetical document from query
    # Step 2: Embed hypothetical document
    # Step 3: Use embedding to retrieve real chunks
    def hyde_retrieve(question: str) -> list:
        """Generate a hypothetical answer, embed it, retrieve real chunks."""
        # Generate hypothetical passage
        hyde_chain   = HYDE_PROMPT | llm | StrOutputParser()
        hypothetical = hyde_chain.invoke({"question": question})

        # Embed the hypothetical passage
        hypo_embedding = embeddings.embed_query(hypothetical)

        # Use the embedding to retrieve real document chunks
        real_docs = db.similarity_search_by_vector(
            hypo_embedding,
            k=RETRIEVER_K,
        )
        return real_docs

    # ── Full RAG chain ─────────────────────────────────────────────────────────
    def full_chain(question: str) -> dict:
        real_docs = hyde_retrieve(question)
        context   = format_docs(real_docs)
        answer    = (RAG_PROMPT | llm | StrOutputParser()).invoke(
            {"context": context, "question": question}
        )
        return {"answer": answer, "sources": real_docs}

    print(f"[+] HyDE RAG chain ready")
    print(f"    HyDE model  : {LLM_MODEL} (hypothetical doc generation)")
    print(f"    Embed model : {EMBED_MODEL}")
    print(f"    Answer model: {LLM_MODEL}")
    print(f"    Retriever   : {RETRIEVER_SEARCH_TYPE.upper()} "
          f"k={RETRIEVER_K} fetch_k={RETRIEVER_FETCH_K}")

    return full_chain


def query(chain_fn, question: str) -> dict:
    result = chain_fn(question)
    return {
        "question": question,
        "answer":   result["answer"],
        "sources": [
            {
                "source":  Path(doc.metadata.get("source", "unknown")).name,
                "content": doc.page_content[:200],
            }
            for doc in result["sources"]
        ],
    }


def print_result(result: dict):
    print("\n" + "=" * 60)
    print(f"Q: {result['question']}")
    print(f"\nA: {result['answer']}")
    print("\n--- Retrieved Chunks ---")
    for i, src in enumerate(result["sources"], 1):
        print(f"[{i}] {src['source']}")
        print(f"    {src['content']} ...")
    print("=" * 60)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="RAG Pipeline v7 HyDE - AI Security Assurance Lifecycle"
    )
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument("--query",   type=str, default=None)
    parser.add_argument("--no-hyde", action="store_true",
                        help="Disable HyDE (use standard similarity retrieval)")
    args = parser.parse_args()

    chroma_exists = Path(CHROMA_DIR).exists() and any(Path(CHROMA_DIR).iterdir())
    if args.rebuild or not chroma_exists:
        docs   = load_documents(DOCS_DIR)
        chunks = chunk_documents(docs)
        db     = build_vectorstore(chunks)
    else:
        db = load_vectorstore()

    chain_fn = build_rag_chain(db)

    if args.query:
        result = query(chain_fn, args.query)
        print_result(result)
        return

    print("\n[RAG REPL — HyDE Mode] Type your question. Commands: :rebuild :quit\n")
    while True:
        try:
            user_input = input("Query> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[+] Exiting.")
            break
        if not user_input:
            continue
        if user_input == ":quit":
            break
        if user_input == ":rebuild":
            docs   = load_documents(DOCS_DIR)
            chunks = chunk_documents(docs)
            db     = build_vectorstore(chunks)
            chain_fn = build_rag_chain(db)
            continue
        result = query(chain_fn, user_input)
        print_result(result)


if __name__ == "__main__":
    main()
