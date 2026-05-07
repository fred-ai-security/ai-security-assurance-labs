# SBOM and Vulnerability Scan Summary

**Tooling:** Syft (SBOM generation) + Grype (CVE scanning)

---

## Summary

An SBOM was generated to identify all components and dependencies within the model artifact directory. The SBOM was then scanned for known vulnerabilities using Grype.

This file provides a high-level summary. Detailed evidence and findings are documented in the files below:

- `sbom.cyclonedx.json` — full component inventory
- `grype-results.json` — CVE scan output and findings

Real scan outputs are stored in the local assessment environment and are not committed to this repository.
