# SBOM Example Results (Syft + Grype)

This file provides an example of SBOM evidence and how I summarize results for reviewers.

## What was done
- Generated an SBOM for a model artifact or project directory using **Syft**
- Scanned the SBOM (or the artifact) for known vulnerabilities using **Grype**

## Evidence to include (files)
Add the following outputs in this folder when available:
- `sbom.cyclonedx.json` (or `sbom.spdx.json`)
- `grype-results.json` (or `grype-results.txt`)
- Optional: `scan-summary.md` (short summary of key findings)

## How I interpret results
When reviewing SBOM + vulnerability findings, I focus on:
- High/critical CVEs in dependencies
- Whether vulnerable packages are actually relevant to the artifact
- Licensing or provenance red flags
- Unexpected binaries or scripts in the artifact
- Whether findings warrant mitigation, restrictions, or rejection

## Notes
This repository is structured to keep SBOM and scan artifacts alongside the workflow documentation so the evidence is easy to review and reproduce.
