#!/usr/bin/env python3
import sys
import yaml


def classify_system(data: dict) -> str:
    object_type = str(data.get("object_type", "")).strip().lower()
    autonomy_tier = int(data.get("autonomy_tier", 0) or 0)
    tools = data.get("tool_permissions", []) or []

    if object_type == "agent":
        return "Agent"
    if object_type == "llm app" or object_type == "llm_app":
        return "LLM App"
    if autonomy_tier > 0 or len(tools) > 1:
        return "Agent"
    return "LLM App"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python tools/grits_profile_selector_v2.py <system.yaml>")
        return 1

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    profile = classify_system(data)
    print(f"Selected profile: {profile}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
