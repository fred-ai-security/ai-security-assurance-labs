# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Frederick Baffour
"""
findings_logger.py
Phase 2 — Adversarial Test Harness (v2 — LLM Judge Edition)
AI Security Assurance Lifecycle — Frederick Baffour
Local Lab Environment | LangChain + ChromaDB + Ollama

CHANGES FROM v1:
  - Now accepts judge_verdict dict from llm_judge.py
  - Stores judge reasoning and confidence in every finding
  - Excel sheet now includes Judge Verdict, Confidence, and Reasoning columns
  - False positive risk flagged in both terminal and Excel output
  - Summary table distinguishes PARTIAL from EXPLOITABLE
"""

import datetime
from pathlib import Path

try:
    import openpyxl
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    EXCEL_AVAILABLE = True
except ImportError:
    EXCEL_AVAILABLE = False
    print("[!] openpyxl not installed — Excel logging disabled. Run: pip install openpyxl")

FINDINGS_DIR = Path(__file__).parent / "findings"
FINDINGS_DIR.mkdir(exist_ok=True)
EXCEL_PATH   = FINDINGS_DIR / "phase2_findings.xlsx"

# ── Terminal colors ────────────────────────────────────────────────────────────
RED    = "\033[91m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
DIM    = "\033[2m"
RESET  = "\033[0m"

SEVERITY_COLORS = {
    "CRITICAL": RED, "HIGH": RED, "MEDIUM": YELLOW, "LOW": GREEN, "INFO": CYAN,
}
VERDICT_COLORS = {
    "EXPLOITABLE": RED, "PARTIAL": YELLOW, "MITIGATED": GREEN, "UNKNOWN": CYAN,
}

# ── Framework mappings ─────────────────────────────────────────────────────────
FRAMEWORK_MAP = {
    "Direct Prompt Injection": {
        "owasp": "LLM01:2025 — Prompt Injection",
        "atlas": "AML.T0051.000 — LLM Prompt Injection",
        "nist":  "GOVERN 1.2, MAP 5.1, MEASURE 2.5",
        "iso":   "ISO 42001 — A.6.2.3 (AI System Integrity)",
    },
    "Retrieval Poisoning": {
        "owasp": "LLM01:2025 — Prompt Injection (Indirect); LLM06 — Sensitive Info Disclosure",
        "atlas": "AML.T0051.001 — Indirect Prompt Injection; AML.T0020 — Poison Training Data",
        "nist":  "GOVERN 1.2, MAP 5.2, MEASURE 2.6, MANAGE 2.4",
        "iso":   "ISO 42001 — A.6.2.3, A.8.4 (Data Quality)",
    },
    "Context Stuffing": {
        "owasp": "LLM01:2025 — Prompt Injection; LLM04 — Model Denial of Service",
        "atlas": "AML.T0051.000 — LLM Prompt Injection; AML.T0029 — Denial of ML Service",
        "nist":  "GOVERN 1.2, MAP 5.1, MEASURE 2.5, MANAGE 3.1",
        "iso":   "ISO 42001 — A.6.2.3, A.9.1 (Availability)",
    },
    "Jailbreak via Retrieved Content": {
        "owasp": "LLM01:2025 — Prompt Injection; LLM02 — Insecure Output Handling",
        "atlas": "AML.T0051.001 — Indirect Prompt Injection; AML.T0054 — LLM Jailbreak",
        "nist":  "GOVERN 1.2, MAP 5.1, MEASURE 2.5, MANAGE 2.2",
        "iso":   "ISO 42001 — A.6.2.3, A.6.2.5 (Output Validation)",
    },
}

_findings = []


def log_finding(
    attack_type: str,
    test_name:   str,
    payload:     str,
    response:    str,
    success:     bool,
    severity:    str,
    notes:       str = "",
    judge_verdict: dict = None,
):
    """
    Log a single finding to terminal and store for Excel export.

    judge_verdict: dict from llm_judge.judge_attack() containing:
      - verdict           : EXPLOITABLE | MITIGATED | PARTIAL | UNKNOWN
      - confidence        : HIGH | MEDIUM | LOW
      - reasoning         : one-sentence explanation
      - false_positive_risk: HIGH | LOW
    """
    timestamp  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    frameworks = FRAMEWORK_MAP.get(attack_type, {})

    # ── Determine final status from judge (preferred) or keyword fallback ──────
    if judge_verdict and judge_verdict.get("verdict") not in (None, "UNKNOWN"):
        final_status     = judge_verdict["verdict"]          # EXPLOITABLE / PARTIAL / MITIGATED
        judge_confidence = judge_verdict.get("confidence", "?")
        judge_reasoning  = judge_verdict.get("reasoning", "")
        fpr              = judge_verdict.get("false_positive_risk", "?")
        judge_model      = "llama3.1:8b-instruct-q4_K_M"
    else:
        final_status     = "EXPLOITABLE" if success else "MITIGATED"
        judge_confidence = "LOW"
        judge_reasoning  = "Keyword match only — judge unavailable. Manual review required."
        fpr              = "HIGH"
        judge_model      = "keyword-fallback"

    sev_color     = SEVERITY_COLORS.get(severity.upper(), RESET)
    verdict_color = VERDICT_COLORS.get(final_status, CYAN)

    # ── Terminal output ────────────────────────────────────────────────────────
    print(f"\n{'='*70}")
    print(f"{BOLD}{sev_color}[{severity.upper()}] {attack_type} — {test_name}{RESET}")
    print(f"{'='*70}")
    print(f"  Timestamp : {timestamp}")
    print(f"\n  {BOLD}Payload:{RESET}")
    print(f"  {CYAN}{payload[:300]}{'...' if len(payload) > 300 else ''}{RESET}")
    print(f"\n  {BOLD}RAG Response:{RESET}")
    print(f"  {response[:400]}{'...' if len(response) > 400 else ''}")
    if notes:
        print(f"\n  {BOLD}Analyst Notes:{RESET} {notes}")
    print(f"\n  {BOLD}Judge Evaluation ({judge_model}):{RESET}")
    print(f"  Verdict     : {verdict_color}{BOLD}{final_status}{RESET} "
          f"{DIM}(confidence: {judge_confidence} | FP risk: {fpr}){RESET}")
    print(f"  Reasoning   : {judge_reasoning}")
    print(f"\n  {BOLD}Framework Mappings:{RESET}")
    print(f"  OWASP : {frameworks.get('owasp', 'N/A')}")
    print(f"  ATLAS : {frameworks.get('atlas', 'N/A')}")
    print(f"  NIST  : {frameworks.get('nist',  'N/A')}")
    print(f"  ISO   : {frameworks.get('iso',   'N/A')}")
    print(f"{'='*70}")

    _findings.append({
        "timestamp":        timestamp,
        "attack_type":      attack_type,
        "test_name":        test_name,
        "severity":         severity.upper(),
        "keyword_result":   "EXPLOITABLE" if success else "MITIGATED",
        "judge_verdict":    final_status,
        "judge_confidence": judge_confidence,
        "judge_reasoning":  judge_reasoning,
        "fp_risk":          fpr,
        "judge_model":      judge_model,
        "payload":          payload,
        "response":         response[:1000],
        "notes":            notes,
        "owasp":            frameworks.get("owasp", ""),
        "atlas":            frameworks.get("atlas", ""),
        "nist":             frameworks.get("nist",  ""),
        "iso":              frameworks.get("iso",   ""),
    })


def export_excel():
    if not EXCEL_AVAILABLE:
        print("[!] Skipping Excel export — openpyxl not available.")
        return
    if not _findings:
        print("[!] No findings to export.")
        return

    HEADER_FILL   = PatternFill("solid", fgColor="1F3864")
    EXPLOIT_FILL  = PatternFill("solid", fgColor="FF4444")
    PARTIAL_FILL  = PatternFill("solid", fgColor="FF9900")
    MITIG_FILL    = PatternFill("solid", fgColor="70AD47")
    UNKNOWN_FILL  = PatternFill("solid", fgColor="00B0F0")
    CRITICAL_FILL = PatternFill("solid", fgColor="FF0000")
    HIGH_FILL     = PatternFill("solid", fgColor="FF6600")
    MEDIUM_FILL   = PatternFill("solid", fgColor="FFD700")
    LOW_FILL      = PatternFill("solid", fgColor="92D050")
    ALT_FILL      = PatternFill("solid", fgColor="EBF3FB")

    VERDICT_FILLS = {
        "EXPLOITABLE": EXPLOIT_FILL,
        "PARTIAL":     PARTIAL_FILL,
        "MITIGATED":   MITIG_FILL,
        "UNKNOWN":     UNKNOWN_FILL,
    }
    SEVERITY_FILLS = {
        "CRITICAL": CRITICAL_FILL,
        "HIGH":     HIGH_FILL,
        "MEDIUM":   MEDIUM_FILL,
        "LOW":      LOW_FILL,
    }

    thin       = Side(style="thin", color="CCCCCC")
    thin_border = Border(left=thin, right=thin, top=thin, bottom=thin)

    wb = openpyxl.Workbook()

    # ── Sheet 1: Summary Dashboard ─────────────────────────────────────────────
    ws_sum       = wb.active
    ws_sum.title = "Summary Dashboard"

    ws_sum.merge_cells("A1:N1")
    t = ws_sum["A1"]
    t.value     = "Phase 2 Adversarial Harness — LLM Judge Finding Summary"
    t.font      = Font(name="Arial", size=16, bold=True, color="FFFFFF")
    t.fill      = PatternFill("solid", fgColor="1F3864")
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws_sum.row_dimensions[1].height = 35

    ws_sum.merge_cells("A2:N2")
    s = ws_sum["A2"]
    s.value     = (f"Frederick Baffour | AI Security Assurance Lifecycle | "
                   f"Judge: llama3.1:8b-instruct-q4_K_M | Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    s.font      = Font(name="Arial", size=10, italic=True, color="FFFFFF")
    s.fill      = PatternFill("solid", fgColor="2E75B6")
    s.alignment = Alignment(horizontal="center")
    ws_sum.row_dimensions[2].height = 18

    total       = len(_findings)
    exploitable = sum(1 for f in _findings if f["judge_verdict"] == "EXPLOITABLE")
    partial     = sum(1 for f in _findings if f["judge_verdict"] == "PARTIAL")
    mitigated   = sum(1 for f in _findings if f["judge_verdict"] == "MITIGATED")
    fp_caught   = sum(1 for f in _findings
                      if f["keyword_result"] == "EXPLOITABLE"
                      and f["judge_verdict"] == "MITIGATED")
    critical    = sum(1 for f in _findings if f["severity"] == "CRITICAL")

    stats = [
        ("Total Tests",    total,       "2E75B6"),
        ("Exploitable",    exploitable, "FF4444"),
        ("Partial",        partial,     "FF9900"),
        ("Mitigated",      mitigated,   "70AD47"),
        ("FP Corrected",   fp_caught,   "9933CC"),
        ("Critical",       critical,    "FF0000"),
    ]
    ws_sum.row_dimensions[4].height = 50
    for i, (label, val, color) in enumerate(stats):
        col = i * 2 + 1
        lc  = ws_sum.cell(row=3, column=col, value=label)
        lc.font      = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        lc.fill      = PatternFill("solid", fgColor=color)
        lc.alignment = Alignment(horizontal="center")
        vc  = ws_sum.cell(row=4, column=col, value=val)
        vc.font      = Font(name="Arial", size=24, bold=True, color=color)
        vc.fill      = PatternFill("solid", fgColor="F2F2F2")
        vc.alignment = Alignment(horizontal="center", vertical="center")

    # ── Sheet 2: All Findings ──────────────────────────────────────────────────
    ws       = wb.create_sheet("All Findings")
    headers  = [
        "ID", "Timestamp", "Attack Type", "Test Name", "Severity",
        "Keyword Result", "Judge Verdict", "Judge Confidence",
        "Judge Reasoning", "FP Risk", "Judge Model",
        "Payload", "RAG Response", "Analyst Notes",
        "OWASP LLM Top 10", "MITRE ATLAS", "NIST AI RMF", "ISO 42001"
    ]
    col_widths = [4, 18, 22, 25, 10, 13, 13, 13, 40, 8, 14, 40, 45, 30, 35, 40, 25, 30]

    for col, (header, width) in enumerate(zip(headers, col_widths), 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font      = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill      = HEADER_FILL
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border    = thin_border
        ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = width
    ws.row_dimensions[1].height = 30

    for row_idx, f in enumerate(_findings, 2):
        is_alt   = row_idx % 2 == 0
        row_data = [
            row_idx - 1,
            f["timestamp"],
            f["attack_type"],
            f["test_name"],
            f["severity"],
            f["keyword_result"],
            f["judge_verdict"],
            f["judge_confidence"],
            f["judge_reasoning"],
            f["fp_risk"],
            f["judge_model"],
            f["payload"],
            f["response"],
            f["notes"],
            f["owasp"],
            f["atlas"],
            f["nist"],
            f["iso"],
        ]
        for col, value in enumerate(row_data, 1):
            cell = ws.cell(row=row_idx, column=col, value=value)
            cell.font      = Font(name="Arial", size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border    = thin_border
            if is_alt:
                cell.fill = ALT_FILL

        # Severity color (col 5)
        sc       = ws.cell(row=row_idx, column=5)
        sc.fill  = SEVERITY_FILLS.get(f["severity"], PatternFill())
        sc.font  = Font(name="Arial", size=9, bold=True)
        sc.alignment = Alignment(horizontal="center", vertical="top")

        # Keyword result color (col 6)
        kc       = ws.cell(row=row_idx, column=6)
        kc.fill  = EXPLOIT_FILL if f["keyword_result"] == "EXPLOITABLE" else MITIG_FILL
        kc.font  = Font(name="Arial", size=9, bold=True, color="FFFFFF")
        kc.alignment = Alignment(horizontal="center", vertical="top")

        # Judge verdict color (col 7)
        jc       = ws.cell(row=row_idx, column=7)
        jc.fill  = VERDICT_FILLS.get(f["judge_verdict"], PatternFill())
        jc.font  = Font(name="Arial", size=9, bold=True, color="FFFFFF")
        jc.alignment = Alignment(horizontal="center", vertical="top")

        # FP risk highlight (col 10)
        fpc      = ws.cell(row=row_idx, column=10)
        if f["fp_risk"] == "HIGH":
            fpc.fill = PatternFill("solid", fgColor="FFE0E0")
            fpc.font = Font(name="Arial", size=9, bold=True, color="CC0000")

        ws.row_dimensions[row_idx].height = 65

    ws.freeze_panes = "A2"
    ws.auto_filter.ref = f"A1:R{len(_findings) + 1}"

    # ── Sheet 3: False Positive Analysis ──────────────────────────────────────
    ws_fp       = wb.create_sheet("FP Analysis")
    ws_fp.merge_cells("A1:G1")
    fp_title    = ws_fp["A1"]
    fp_title.value     = "False Positive Analysis — Keyword vs LLM Judge Comparison"
    fp_title.font      = Font(name="Arial", size=13, bold=True, color="FFFFFF")
    fp_title.fill      = PatternFill("solid", fgColor="1F3864")
    fp_title.alignment = Alignment(horizontal="center")
    ws_fp.row_dimensions[1].height = 28

    fp_headers = ["Test Name", "Attack Type", "Keyword Says", "Judge Says",
                  "Discrepancy?", "FP Risk", "Judge Reasoning"]
    fp_widths  = [30, 25, 14, 14, 12, 10, 50]
    for col, (h, w) in enumerate(zip(fp_headers, fp_widths), 1):
        cell = ws_fp.cell(row=2, column=col, value=h)
        cell.font      = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill      = PatternFill("solid", fgColor="2E75B6")
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        cell.border    = thin_border
        ws_fp.column_dimensions[openpyxl.utils.get_column_letter(col)].width = w

    for row_idx, f in enumerate(_findings, 3):
        discrepancy = f["keyword_result"] != f["judge_verdict"]
        is_alt      = row_idx % 2 == 0
        row_data    = [
            f["test_name"],
            f["attack_type"],
            f["keyword_result"],
            f["judge_verdict"],
            "YES ⚠" if discrepancy else "No",
            f["fp_risk"],
            f["judge_reasoning"],
        ]
        for col, val in enumerate(row_data, 1):
            cell = ws_fp.cell(row=row_idx, column=col, value=val)
            cell.font      = Font(name="Arial", size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border    = thin_border
            if is_alt:
                cell.fill = ALT_FILL

        # Highlight discrepancies
        if discrepancy:
            for col in range(1, 8):
                ws_fp.cell(row=row_idx, column=col).fill = PatternFill("solid", fgColor="FFF2CC")
            ws_fp.cell(row=row_idx, column=5).fill = PatternFill("solid", fgColor="FF9900")
            ws_fp.cell(row=row_idx, column=5).font = Font(name="Arial", size=9, bold=True, color="FFFFFF")

        ws_fp.row_dimensions[row_idx].height = 50

    # ── Sheet 4: Framework Reference ──────────────────────────────────────────
    ws_fw       = wb.create_sheet("Framework Reference")
    ws_fw.merge_cells("A1:E1")
    fr_t        = ws_fw["A1"]
    fr_t.value  = "Framework Control Reference — Phase 2 Attack Mappings"
    fr_t.font   = Font(name="Arial", size=13, bold=True, color="FFFFFF")
    fr_t.fill   = PatternFill("solid", fgColor="1F3864")
    fr_t.alignment = Alignment(horizontal="center")
    ws_fw.row_dimensions[1].height = 28

    fw_hdrs   = ["Attack Type", "OWASP LLM Top 10", "MITRE ATLAS", "NIST AI RMF", "ISO 42001"]
    fw_widths = [28, 45, 45, 30, 35]
    for col, (h, w) in enumerate(zip(fw_hdrs, fw_widths), 1):
        cell = ws_fw.cell(row=2, column=col, value=h)
        cell.font      = Font(name="Arial", size=10, bold=True, color="FFFFFF")
        cell.fill      = PatternFill("solid", fgColor="2E75B6")
        cell.alignment = Alignment(horizontal="center", wrap_text=True)
        cell.border    = thin_border
        ws_fw.column_dimensions[openpyxl.utils.get_column_letter(col)].width = w

    for row_idx, (attack, fw) in enumerate(FRAMEWORK_MAP.items(), 3):
        is_alt   = row_idx % 2 == 0
        row_data = [attack, fw["owasp"], fw["atlas"], fw["nist"], fw["iso"]]
        for col, val in enumerate(row_data, 1):
            cell = ws_fw.cell(row=row_idx, column=col, value=val)
            cell.font      = Font(name="Arial", size=9)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border    = thin_border
            if is_alt:
                cell.fill = ALT_FILL
        ws_fw.row_dimensions[row_idx].height = 55

    wb.save(EXCEL_PATH)
    total_exp = sum(1 for f in _findings if f["judge_verdict"] == "EXPLOITABLE")
    total_par = sum(1 for f in _findings if f["judge_verdict"] == "PARTIAL")
    total_mit = sum(1 for f in _findings if f["judge_verdict"] == "MITIGATED")
    fp_count  = sum(1 for f in _findings
                    if f["keyword_result"] == "EXPLOITABLE"
                    and f["judge_verdict"] == "MITIGATED")
    print(f"\n[+] Excel finding library saved to: {EXCEL_PATH}")
    print(f"    Judge verdicts  — Exploitable: {total_exp} | Partial: {total_par} | Mitigated: {total_mit}")
    print(f"    False positives corrected by judge: {fp_count}")


def print_summary():
    if not _findings:
        print("[!] No findings recorded.")
        return

    total     = len(_findings)
    exploited = sum(1 for f in _findings if f["judge_verdict"] == "EXPLOITABLE")
    partial   = sum(1 for f in _findings if f["judge_verdict"] == "PARTIAL")
    mitigated = sum(1 for f in _findings if f["judge_verdict"] == "MITIGATED")
    fp_caught = sum(1 for f in _findings
                    if f["keyword_result"] == "EXPLOITABLE"
                    and f["judge_verdict"] == "MITIGATED")

    print(f"\n{'='*70}")
    print(f"{BOLD}  PHASE 2 TEST RUN SUMMARY (Judge: llama3.1:8b-instruct-q4_K_M){RESET}")
    print(f"{'='*70}")
    print(f"  Total Tests          : {total}")
    print(f"  {RED}Exploitable          : {exploited}{RESET}")
    print(f"  {YELLOW}Partial              : {partial}{RESET}")
    print(f"  {GREEN}Mitigated            : {mitigated}{RESET}")
    print(f"  \033[35mFalse Positives Fixed: {fp_caught} (keyword said EXPLOITABLE, judge said MITIGATED){RESET}")
    print(f"\n  {'Attack Type':<35} {'Tests':>5} {'Exploit':>7} {'Partial':>7} {'Mitigated':>9}")
    print(f"  {'-'*65}")

    attack_types = {}
    for f in _findings:
        at = f["attack_type"]
        if at not in attack_types:
            attack_types[at] = {"total": 0, "exploited": 0, "partial": 0, "mitigated": 0}
        attack_types[at]["total"] += 1
        if f["judge_verdict"] == "EXPLOITABLE":
            attack_types[at]["exploited"] += 1
        elif f["judge_verdict"] == "PARTIAL":
            attack_types[at]["partial"] += 1
        else:
            attack_types[at]["mitigated"] += 1

    for at, s in attack_types.items():
        print(f"  {at:<35} {s['total']:>5} "
              f"{RED}{s['exploited']:>7}{RESET} "
              f"{YELLOW}{s['partial']:>7}{RESET} "
              f"{GREEN}{s['mitigated']:>9}{RESET}")
    print(f"{'='*70}\n")
