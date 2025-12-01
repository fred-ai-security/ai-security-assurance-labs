# YARA Scanning for AI Model Artifacts

This document shows how **YARA** can be used to scan AI model–related files for suspicious patterns as part of an AI Security Assurance workflow.

While AI models (such as `.gguf` or `.safetensors`) are not traditional executables, attackers can still embed:

- Malicious or phishing strings  
- Obfuscated payloads  
- Encoded commands  
- Suspicious configuration fragments  
- Indicators of tampering  

YARA helps detect these patterns early in the model intake process.

---

## Where YARA Fits in the Model Supply Chain

YARA is most useful in **Stage 1 – Model Intake**, when we:

- Download models and supporting files  
- Store them in a controlled **intake directory** (e.g., `C:\AI_SECURITY_LABS\stage1_intake`)  
- Run static checks before any model is executed or evaluated  

If a rule fires, the file should be **quarantined** and analyzed before moving forward.

---

## Example YARA Rule (Suspicious Strings)

Below is a simple but effective example rule that checks for potentially dangerous content.

```yara
rule SuspiciousModelStrings
{
    strings:
        $eval = "eval(" nocase
        $ps   = "powershell" nocase
        $enc  = /[A-Za-z0-9\/\+]{40,}/   // high-entropy string

    condition:
        any of ($eval, $ps, $enc)
}
