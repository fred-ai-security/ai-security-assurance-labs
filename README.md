# AI Security Assurance Labs
### A Hands-On Framework for Model Supply-Chain Security, Static Analysis, and LLM Red Teaming

This repository contains a structured collection of AI Security Assurance modules focused on:

- Model supply-chain verification  
- Model integrity and malware scanning  
- Static analysis of AI/ML artifacts  
- LLM red teaming and automated vulnerability evaluation  
- End-to-end model intake and validation workflows  

The repository demonstrates practical, industry-aligned approaches used in AI Security Engineering.

---

## 📂 Repository Structure

```
ai-security-assurance-labs/
│
├── model-supply-chain/   # Model intake, verification, supply-chain security
│
├── red-teaming/          # Automated and manual LLM red teaming
│   ├── garak/
│   └── promptfoo/
│
├── static-analysis/      # Malware, integrity, and rule-based analysis
│   ├── clamav/
│   ├── hashing/
│   ├── sigcheck/
│   └── yara/
│
└── README.md             # Main repository documentation
```

---

## 🎯 Purpose

The repository provides a complete example of an AI Security Assurance workflow, including:

- Secure model download and intake  
- Detection of tampered or malicious model files  
- Static malware scanning and pattern matching  
- Verification of binary signatures and model integrity  
- Automated LLM red teaming and vulnerability discovery  

The structure aligns with practices used by AI Security teams, ML Ops groups, and AI governance functions.

---

## 🧩 High-Level Architecture

```
      ┌─────────────────────┐
      │ Model Supply Chain  │
      │   (Intake + Verify) │
      └──────────┬──────────┘
                 ▼
     ┌─────────────────────────┐
     │ Static Analysis Layer   │
     │ YARA • ClamAV • Hashing │
     │ Sigcheck • Metadata     │
     └──────────┬──────────────┘
                 ▼
  ┌────────────────────────────────┐
  │ Red Teaming & Assessments      │
  │ Garak • Promptfoo • PyRIT      │
  └──────────┬─────────────────────┘
                 ▼
     ┌────────────────────────────┐
     │ Secure Deployment /        │
     │ Model Certification         │
     └────────────────────────────┘
```

Each repository module corresponds to one layer of this security pipeline.

---

## 🔍 Module Overview

### **1. Model Supply Chain Security**
📁 `model-supply-chain/`

Includes:

- Model intake workflow  
- Verification and provenance stages  
- Trusted source validation  
- Hash integrity checks  
- Storage hygiene and evidence retention  

---

### **2. Static Analysis**
📁 `static-analysis/`

| Module      | Description |
|-------------|-------------|
| **ClamAV**   | Malware signature scanning for `.gguf`, `.safetensors`, and tokenizer files |
| **Hashing**  | SHA-256 integrity verification |
| **Sigcheck** | Binary signature validation |
| **YARA**     | Rule-based detection of suspicious or anomalous content |

---

### **3. LLM Red Teaming**
📁 `red-teaming/`

| Tool        | Purpose |
|-------------|---------|
| **Garak**     | Automated LLM vulnerability scanning |
| **Promptfoo** | Config-driven prompt testing and red teaming |

---

## 🚀 Workflow Summary

### **Model Intake**
Performed through trusted sources such as HuggingFace CLI, GitHub releases, or Ollama.

### **Static Analysis Sequence**
1. Sigcheck  
2. Hash integrity verification  
3. YARA scanning  
4. ClamAV scanning  

### **Red Teaming**
Evaluation using Garak and Promptfoo to identify jailbreak, prompt injection, and unsafe output patterns.

### **Documentation**
Markdown reports and evidence are stored in the repository as templates and examples.

---

## 🔗 Navigation

- Model Supply Chain  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/model-supply-chain

- Static Analysis  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/static-analysis

- Red Teaming  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/red-teaming

---

## 🛡️ Tools Represented

- Sigcheck (Sysinternals)  
- ClamAV Antivirus Engine  
- YARA Rule Engine  
- PowerShell SHA-256 hashing  
- Garak LLM Red Teaming Toolkit  
- Promptfoo Red Team Engine  
- Model intake integrity workflows  

---

This repository serves as a comprehensive AI Security Assurance reference implementation covering supply-chain validation, static analysis, and adversarial testing.
