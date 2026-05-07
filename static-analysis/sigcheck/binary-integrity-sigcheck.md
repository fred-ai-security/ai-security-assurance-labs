# Toolchain Binary Integrity Verification

Binary integrity verification confirms the authenticity of executables and security tools used within the AI Security Assurance workflow. This applies to YARA, ClamAV, and other utilities used during model intake, static analysis, and red-teaming — ensuring that the tools themselves have not been tampered with or replaced before use.

Framework alignment follows the mappings defined in `../README.md` and `model-supply-chain/model-provenance-and-trusted-sources.md`.

---

## Why Toolchain Verification Matters

Compromised security tools introduce risk at the foundation of the assessment pipeline. Verification confirms that:

- Tools originate from trusted, official sources
- Binaries have not been modified after installation
- No unauthorized substitutions have occurred
- Tool versions match expected values

---

## Verification Approach (Linux / WSL2)

On Ubuntu/WSL2, toolchain integrity is verified using hash comparison and package manager validation rather than Windows-specific signing tools.

**Verify tool binary hashes:**

```bash
# Hash the tool binary directly
sha256sum $(which yara)
sha256sum $(which clamscan)
sha256sum $(which freshclam)
```

Compare the output against official published checksums from the vendor or distribution source.

**Verify installation source:**

```bash
# Confirm tool was installed via package manager
dpkg -l yara
dpkg -l clamav
```

Tools installed via `apt` from verified repositories carry implicit distribution trust. Tools downloaded from GitHub releases should have their release checksums verified explicitly.

**Check tool version against known-good:**

```bash
yara --version
clamscan --version
```

---

## Example Output

```bash
$ sha256sum $(which clamscan)
a3f9b2c1d4e5f67890abcdef1234567890abcdef1234567890abcdef12345678  /usr/bin/clamscan

$ dpkg -l clamav
ii  clamav  1.0.3+dfsg-1  amd64  Anti-virus utility for Unix - command-line interface
```

---

## Verification Checklist

- [ ] Tool binary hash generated and recorded
- [ ] Hash compared against official published values (vendor release page or distribution)
- [ ] Tool version confirmed against expected version
- [ ] Installation source verified (package manager or signed release)
- [ ] Any discrepancies investigated before the tool is used in assessment workflows

---

## Result Interpretation

**Verified** — binary hash matches official values; tool installed from a trusted source; safe to use in the assessment pipeline.

**Mismatch or unknown source** — quarantine the tool, re-acquire from the official source, and investigate before use. Do not use unverified tools in assessment workflows.

---

## Position in the Assessment Lifecycle

Toolchain verification is performed before beginning any static analysis or red-teaming activities. Verified tools are a prerequisite for maintaining chain of custody across intake and assessment stages.
