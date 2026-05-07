# Secure RAG Architecture

This document defines the security controls required to build and operate secure Retrieval-Augmented Generation (RAG) systems. RAG transforms LLM behavior based on external knowledge — making it one of the highest-risk components in modern AI architecture.

The focus here is on engineering design, architectural controls, and security guardrails. This document complements the `rag-security-hardening-guide.md`, which covers implementation-level checklists. This document addresses architectural patterns and control design.

Framework alignment follows the mappings defined in `llm-red-teaming-overview.md` and `rag-threat-control-detection-response-mapping.md`.

---

## 1. Threat Model for RAG Systems

RAG architectures introduce the following primary risks:

- Poisoned or malicious documents entering the knowledge base
- Indirect prompt injection inside retrieved content
- Unauthorized access to sensitive internal documents
- RAG used as a vector for data exfiltration
- Retrieval bypassing metadata filters
- Unsafe hallucinations validated through retrieved documents
- Adversarial embeddings (vector poisoning)
- Escalation through tool-use conditioned on retrieved content

---

## 2. Core RAG Architecture Components

A secure RAG system includes:

- Document ingestion pipeline
- Pre-processing and sanitization services
- Embedding generation
- Vector database or index
- Retrieval engine
- LLM orchestrator
- Post-processing guardrails
- Logging and telemetry

---

## 3. Secure Document Ingestion Pipeline

### 3.1 Anti-Malware and Static Analysis
- ClamAV scan
- YARA rules
- File hash verification
- MIME type validation
- No executable content in Markdown or PDF uploads

### 3.2 Document Sanitization
- Remove JavaScript, embedded objects, macros, iframes
- Normalize Unicode
- Sanitize HTML (DOMPurify or equivalent)

### 3.3 Allowed File Types
Only ingest: `.txt`, `.md`, `.pdf`, `.json`

Explicitly block: `.exe`, `.dll`, `.ps1`, `.vbs`, `.html`, `.js`

---

## 4. Secure Embedding Generation

Embedding models should run:

- In isolated containers without internet access
- With strict tokenizer limits
- With checks to reject untrusted binary payloads

Prevent embedding of:
- Entire documents containing executable code
- Encrypted blobs or extremely high-entropy content
- Data embeddings designed to force retrieval misbehavior

---

## 5. Vector Database Security Controls

Vector databases are one of the highest-risk components in a RAG architecture.

**Required controls:**
- Encryption at rest and in transit (TLS 1.2+)
- Strict RBAC (read, write, admin separation)
- Metadata-based access control and row/tenant isolation
- No direct user or application queries outside the controlled retrieval service
- Disallow wildcard or broad retrieval
- Limit `top_k` results to prevent context flooding

**Poisoning detection — flag:**
- High-entropy vectors
- Outliers relative to cluster norms
- Documents using adversarial formatting patterns

---

## 6. Retrieval Pipeline Guardrails

**Apply:**
- Domain filters and metadata filters
- Strict allowlists
- PII redaction
- Content validation and classification
- Prompt-injection scanning

**Reject documents containing:**
- "Ignore previous instructions"
- "You must obey…"
- "System override"
- "Do not follow rules above"
- Hidden Unicode control characters

---

## 7. LLM Orchestration Controls

### 7.1 Prompt Sandboxing

Separate retrieved content from system instructions using structured prompt architecture:

```
SYSTEM: Follow safety rules.
CONTEXT (Read-only): {retrieved passages}
USER: {user query}
```

This pattern ensures the model receives a clear signal distinguishing trusted instructions from untrusted retrieved content.

### 7.2 Retrieval Quotas
- Maximum number of retrieved chunks per query
- Maximum combined chunk size
- Reject oversized retrieval payloads

### 7.3 Response Controls
- Toxicity filter
- PII redaction
- Hallucination minimizer
- Content moderation pre- and post-generation

---

## 8. Preventing RAG Prompt Injection

RAG prompt injection occurs when malicious content in the vector database manipulates model behavior.

**Required mitigations:**
- Strip instruction-like language from retrieved content before it enters the prompt
- Delimit retrieved content explicitly:

```
The following is untrusted retrieved content:
<<<
{chunk}
>>>
```

- Apply escape/encoding to prevent model misinterpretation
- Prohibit content that attempts to redefine system instructions, inject new policies, or impersonate admins or developers

---

## 9. Monitoring and Telemetry

Monitor:
- Retrieval patterns and embedding spikes
- Retrieval of unusually long documents
- Documents with injection patterns entering the pipeline
- Multi-turn escalation or behavior drift
- Data exfiltration patterns
- Chunks correlated with unsafe model outputs

Logs should track: query, source documents, output classification, risk score, and redaction actions.

See `model-monitoring-and-telemetry-engineering.md` and `llm-incident-response-playbook.md` for full monitoring requirements and response workflows.

---

## 10. Secure RAG Deployment Requirements

RAG should be deployed with:

- Container isolation
- No outbound internet access for retrieval or LLM inference
- Strict egress filtering
- Immutable storage for ingested documents
- Continuous re-scanning of the knowledge base
- Lineage tracking for document changes
- Versioned embeddings
- Audit-ready logging
