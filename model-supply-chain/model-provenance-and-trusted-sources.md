# Model Provenance and Trusted Source Verification

## Ensuring Secure, Authentic, and Verifiable AI Model Origins

Model provenance verification confirms the authenticity, integrity, and trustworthiness of third-party AI models before they enter any assessment or deployment workflow. This document defines how to confirm that a model:

- Originates from an authentic and reputable upstream source
- Has not been replaced, tampered with, or altered
- Matches official metadata and file signatures
- Is downloaded through secure and verifiable methods
- Retains documented provenance for auditing and governance

These activities mitigate risks such as fake models, poisoned files, shadow uploads, and malicious forks.

---

## Framework Alignment

| Framework | Relevant Controls |
|---|---|
| NIST AI RMF | GOVERN 1.1, MAP 1.5 — model origin, traceability, and provenance documentation |
| MITRE ATLAS | AML.T0010 — ML Supply Chain Compromise; AML.T0041 — Craft Adversarial Data |
| OWASP LLM Top 10 (2025) | LLM03 — Training Data Poisoning; supply-chain integrity |
| ISO/IEC 42001 | Clause 8 — AI system operation and artifact control |
| NIST SP 800-53 | SA-12 — Supply Chain Protection; SR-4 — Provenance |

---

## 1. Source Validation

Provenance verification begins by confirming that the publishing account is legitimate and reputable.

**Indicators of Trusted Sources:**

- Verified HuggingFace organizations
- Established providers (Meta, Google, Mistral, Microsoft, Cohere, NVIDIA)
- Long account history with consistent activity
- Complete model cards and documentation
- Significant community visibility

**Indicators of High Risk:**

- Newly created or unverified accounts
- Missing or unverified account badges
- Incomplete documentation
- Inconsistent file structure compared to official releases
- Altered safetensors or GGUF files
- Suspicious forks or missing changelogs

---

## 2. Download Method Validation

Only secure, traceable download methods are used during intake.

**Approved Methods:**

- HuggingFace CLI
- GitHub "Releases" section (signed or version-tagged releases only)
- Ollama official library

**High-Risk Methods — Not Accepted:**

- Direct file links from unknown or unverified locations
- Git LFS downloads from unverified forks
- ZIP archives with no source verification

---

## 3. Model Card and Metadata Validation

Model metadata is validated for accuracy and completeness. Key fields include:

- Model name and version number
- Release date and file list
- License and intended use
- Safety disclosures
- Provider-published checksums (when available)

Downloaded artifacts are compared against published values to identify inconsistencies.

---

## 4. File-Level Provenance Validation

### 4.1 Expected Files

The downloaded directory is verified against expected components, such as:

- `model.gguf` or `model.safetensors`
- `tokenizer.json`
- `config.json`
- `special_tokens_map.json`

### 4.2 File Size

File sizes are compared against official listings. Deviations beyond expected variance indicate potential corruption or unauthorized modification.

### 4.3 Hash Verification

Where provider-published checksums are available, SHA-256 hashes are compared to verify artifact integrity. Results are recorded in the provenance record.

---

## 5. Commit History and Release Tag Verification

For models hosted on GitHub or similar platforms:

- Review commit history for unexpected force-pushes or maintainer changes
- Accept only signed or version-tagged releases
- Reject artifacts downloaded from arbitrary commits or unverified branches

---

## 6. Provenance Metadata Recording

Each model intake produces a provenance record using a standardized template. The example below uses synthetic data for illustration — real assessment records are stored locally and not committed to this repository.

| Field | Example (Synthetic) |
|---|---|
| Model Name | Llama 3.1 8B |
| Provider | meta-llama (verified) |
| Source URL | https://huggingface.co/meta-llama/Llama-3.1-8B |
| Download Method | huggingface-cli |
| Download Date | YYYY-MM-DD |
| Hash (SHA-256) | ABC123... |
| File Size | 4.92 GB |
| Supporting Files | config.json, tokenizer.json |
| Verified By | Frederick Baffour |
| Notes | All metadata validated against published values |

Additional metadata may include license summary, provider account verification status, and a local-only model card snapshot.

---

## 7. Provenance Storage Practices

**Stored in this repository:**

- Templates and process documentation
- Synthetic examples (as above)

**Not stored in this repository:**

- Real model artifacts or hashes
- Real metadata snapshots
- Logs containing system paths or operational data

---

## 8. Provenance Verification Workflow

```
┌─────────────────────────┐
│   Trusted Source Check  │
│ (Org, badges, history)  │
└──────────────┬──────────┘
               ▼
┌──────────────────────────┐
│  Metadata Verification   │
│  (Model card, license)   │
└──────────────┬───────────┘
               ▼
┌──────────────────────────┐
│  File-Level Verification │
│  (Names, size, hashes)   │
└──────────────┬───────────┘
               ▼
┌──────────────────────────┐
│  Create Provenance Record│
│  (Template + summary)    │
└──────────────────────────┘
```
