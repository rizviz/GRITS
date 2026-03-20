#!/usr/bin/env python3
import sys
import yaml

CHECKS = [
    ("owner_present", "Owner assigned"),
    ("deputy_owner_present", "Deputy owner assigned"),
    ("tool_scope_declared", "Tool scope declared"),
    ("network_exposure_reviewed", "Network exposure reviewed"),
    ("secrets_handling_recorded", "Secrets handling recorded"),
    ("cost_guardrails_defined", "Cost guardrails defined"),
    ("monitoring_enabled", "Monitoring enabled"),
    ("recertification_set", "Recertification date set"),
    ("policy_violation_visibility", "Policy violation visibility enabled"),
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/grits_openclaw_checklist_v2.py <posture.yaml>")
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    checks = data.get("checks", {}) or {}

    passed = 0
    warned = 0
    for key, label in CHECKS:
        state = bool(checks.get(key, False))
        if state:
            print(f"PASS  - {label}")
            passed += 1
        else:
            print(f"WARN  - {label}")
            warned += 1

    print(f"\nSummary: {passed} passed, {warned} warnings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
