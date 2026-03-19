# OpenClaw Deployment Hardening Baseline v0.1

## What this is

This is the minimum practical baseline for OpenClaw-style deployments under GRITS v0.1.

It is designed for:

- self-hosters
- home labs
- always-on local deployments
- small teams running one or several agents

It is not the whole GRITS framework. It is one adoption artifact inside GRITS.

## Why it matters

This baseline is meant to reduce the most common ways an otherwise useful deployment becomes fragile, unsafe, or expensive.

| Boundary | What can go wrong | What the baseline tries to improve |
|---|---|---|
| Network | exposed interfaces, accidental reachability, mixed-trust exposure | tighter exposure and clearer trust boundaries |
| Operator | too many admins, unclear operator trust, unsafe command use | clearer operator accountability and narrower control |
| Application | unsafe tools, plugin sprawl, unreviewed execution paths | declared tool scope and safer defaults |
| OS / Secrets | secret leakage, host hygiene gaps, environment confusion | better secret handling and cleaner host boundaries |
| Financial | runaway loops, token/context bloat, budget drain | basic guardrails and anomaly visibility |

## Baseline controls

### Network boundary

- review what interfaces and services are reachable
- avoid exposing unnecessary management surfaces publicly
- separate mixed-trust users across gateways or hosts when practical
- document network assumptions for the deployment

### Operator boundary

- assign an accountable operator or owner
- avoid shared unmanaged administrative access
- make approval authority explicit for sensitive actions
- keep operator trust boundaries narrow and intentional

### Application boundary

- declare allowed tool categories
- disable or avoid unnecessary plugins and execution paths
- review higher-risk tool use before production promotion
- capture meaningful tool invocation evidence

### OS / Secrets boundary

- do not let secrets sprawl casually through files and workspace content
- separate secrets from ordinary operator workflows when possible
- keep basic host hygiene and update discipline
- document how always-on environments are isolated from casual experimentation

### Financial boundary

- set basic cost or budget guardrails
- watch for obvious loop or runaway behavior
- review unusual context growth or repeated execution patterns
- require follow-up when spend behavior changes materially

## Minimum evidence expected

- named owner/operator
- declared tool scope
- deployment environment identified
- basic exposure review completed
- secret handling approach recorded
- budget or spend guardrails defined

## What to do next

- use the checklist script on `examples/sample-openclaw-posture.yaml`
- read the remediation sequence in `playbooks/openclaw-remediation-playbook-v0.1.md`
- score the posture using `tools/grits_scorecard_v2.py`
