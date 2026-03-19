#!/usr/bin/env python3
import json
import sys
import yaml

CONTROL_MAP = {
    "owner_present": ("OWN-001", "Critical", "Owner assigned"),
    "deputy_owner_present": ("OWN-002", "High", "Deputy owner assigned"),
    "tool_scope_declared": ("APP-001", "High", "Tool scope declared"),
    "network_exposure_reviewed": ("NET-001", "High", "Network exposure reviewed"),
    "secrets_handling_recorded": ("SEC-001", "High", "Secrets handling recorded"),
    "cost_guardrails_defined": ("FIN-001", "High", "Cost guardrails defined"),
    "monitoring_enabled": ("SIG-001", "High", "Monitoring enabled"),
    "recertification_set": ("LIF-001", "High", "Recertification date set"),
    "policy_violation_visibility": ("SIG-002", "Medium", "Policy violation visibility enabled")
}


def posture_band(pass_count: int, total: int) -> str:
    ratio = pass_count / total if total else 0
    if ratio >= 0.95:
        return "Advanced"
    if ratio >= 0.8:
        return "Hardened"
    if ratio >= 0.6:
        return "Progressing"
    return "Baseline"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/grits_scorecard_v2.py <posture.yaml>")
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    checks = data.get("checks", {}) or {}
    findings = []
    pass_count = 0
    fail_count = 0
    highest = "Low"
    severity_rank = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

    for key, (cid, severity, summary) in CONTROL_MAP.items():
        if bool(checks.get(key, False)):
            pass_count += 1
        else:
            fail_count += 1
            findings.append({
                "id": cid,
                "severity": severity,
                "result": "Fail",
                "summary": summary
            })
            if severity_rank[severity] > severity_rank[highest]:
                highest = severity

    result = {
        "object_id": data.get("object_id"),
        "profile_type": data.get("profile_type"),
        "lifecycle_state": data.get("lifecycle_state"),
        "results": {
            "pass": pass_count,
            "partial": 0,
            "fail": fail_count,
            "not_applicable": 0
        },
        "posture_band": posture_band(pass_count, len(CONTROL_MAP)),
        "highest_severity": highest,
        "top_findings": findings[:5],
        "next_actions": [item["summary"] for item in findings[:3]]
    }

    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
