# AI Security Assurance Labs
### A Hands-On Framework for Model Supply-Chain Security, Static Analysis, and LLM Red Teaming

This repository is a structured collection of AI Security Assurance modules used to perform:

- Model supply-chain verification  
- Model integrity and malware scanning  
- Static analysis of AI/ML artifacts  
- LLM red teaming and automated vulnerability evaluation  
- End-to-end model intake and validation workflows  

The goal is to provide a practical, industry-aligned lab that demonstrates real-world skills in AI Security Engineering.

---

## 📂 Repository Structure

```
ai-security-assurance-labs/
│
├── model-supply-chain/ # Model intake, verification, supply-chain security
│
├── red-teaming/ # Automated & manual LLM red teaming
│ ├── garak/
│ └── promptfoo/
│
├── static-analysis/ # Malware, integrity & rule-based analysis
│ ├── clamav/
│ ├── hashing/
│ ├── sigcheck/
│ └── yara/
│
└── README.md # Main repository documentation
```

---

## 🎯 Purpose of This Repository

This repository provides a complete, real-world example of an AI Security Assurance workflow, demonstrating:

- How to securely download and process models  
- How to detect tampered or malicious model files  
- How to run static malware scanning and pattern matching  
- How to verify binary signatures and model integrity  
- How to perform automated LLM red teaming  

This structure reflects best practices used by:

- AI Security teams  
- ML Ops organizations  
- AI product engineering groups  
- AI governance & assurance programs  

---

## 🧩 High-Level Architecture

```
      ┌─────────────────────┐
      │ Model Supply Chain  │
      │  (Intake + Verify)  │
      └──────────┬──────────┘
                 ▼
     ┌───────────────────────┐
     │ Static Analysis Layer │
     │ YARA • ClamAV • Hash  │
     │ Sigcheck • Metadata   │
     └──────────┬────────────┘
                 ▼
  ┌────────────────────────────┐
  │ Red Teaming & Assessments │
  │ Garak • Promptfoo • PyRIT │
  └──────────┬────────────────┘
                 ▼
     ┌────────────────────────┐
     │ Secure Deployment /    │
     │ Model Certification     │
     └────────────────────────┘
```

Each folder in this repo corresponds to one of these security layers.

---

## 🔍 Module Overview

---

### **1. Model Supply Chain Security**
📁 **Path:** `model-supply-chain/`

Includes:

- Model intake workflow  
- Verification stages  
- Trusted source validation  
- Hashing & provenance tracking  
- Storage hygiene and evidence retention  

---

### **2. Static Analysis for AI Artifacts**
📁 **Path:** `static-analysis/`

#### Static Analysis Modules

| Module   | Description |
|----------|-------------|
| **ClamAV**   | Malware signature scanning for `.gguf`, `.safetensors`, tokenizer files |
| **Hashing**  | SHA-256 model integrity verification |
| **Sigcheck** | Validates trusted binary signatures for tools |
| **YARA**     | Rule-based detection of suspicious content |

---

### **3. LLM Red Teaming**
📁 **Path:** `red-teaming/`

#### Red Teaming Tools

| Tool        | Purpose |
|-------------|---------|
| **Garak**     | Automated LLM vulnerability scanning |
| **Promptfoo** | Red teaming using config-driven prompt test suites |

---

## 🚀 How to Use This Repository

### **1. Download a model safely**
Using HuggingFace CLI, Ollama, or trusted sources.

### **2. Move files into your Stage 1 intake folder**
Example:  
C:\AI_SECURITY_LABS\stage1_intake


### **3. Perform Static Analysis in this order**
1. **Sigcheck** → validate binary trust  
2. **Hashing** → generate & compare integrity manifest  
3. **YARA** → detect suspicious patterns  
4. **ClamAV** → scan for known malware signatures  

### **4. Perform LLM Red Teaming**
Use **Garak** or **Promptfoo** to assess model safety.

### **5. Document Results**
Export Markdown reports or store evidence in the repo.

---

## 🔗 Navigation

- **Model Supply Chain**  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/model-supply-chain

- **Static Analysis**  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/static-analysis

- **Red Teaming**  
  https://github.com/fred-ai-security/ai-security-assurance-labs/tree/main/red-teaming

---

## 🛡️ Tools Covered

- Sigcheck (Sysinternals)  
- ClamAV Antivirus Engine  
- YARA Rule Engine  
- PowerShell SHA-256 Hashing  
- Garak LLM Red Teaming Toolkit  
- Promptfoo Red Team Engine  
- Model intake integrity workflows  

---

This repository serves as a complete, professional AI Security Assurance reference implementation.
