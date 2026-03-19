# OpenClaw Remediation Playbook v0.1

## Purpose

This playbook helps an operator move from findings to action without reading the whole framework first.

## Use this when

- a checklist found gaps
- a deployment is moving toward always-on operation
- trust assumptions changed
- a posture score is weaker than expected

## Remediation sequence

### Step 1: Fix ownership ambiguity first

If nobody clearly owns the deployment or sensitive actions, other controls are weaker than they look.

Actions:
- name an owner
- name a deputy owner
- record who can approve sensitive actions

### Step 2: Reduce exposure next

Actions:
- review reachable services and interfaces
- remove unnecessary exposure
- separate mixed-trust users or environments where possible

### Step 3: Tighten tools and execution paths

Actions:
- inventory enabled tools/plugins
- disable what is unnecessary
- identify which tools need stronger review or approval

### Step 4: Clean up secrets and host assumptions

Actions:
- record where secrets live
- reduce casual secret sprawl
- separate ordinary workspace content from sensitive runtime material
- verify always-on deployments are not treated like a scratchpad

### Step 5: Add cost and abuse guardrails

Actions:
- set minimum spend or token guardrails
- review repeated loop behavior
- flag large context growth or repeated invocation spikes

## Priority ordering

| Finding type | Fix priority |
|---|---|
| missing owner / deputy owner | highest |
| exposed management surface | highest |
| over-scoped or undeclared tools | highest |
| secret handling ambiguity | high |
| missing runtime evidence for meaningful actions | high |
| missing cost guardrails | medium-high |
| general hygiene improvements | medium |

## What good looks like after remediation

- accountable ownership is explicit
- deployment trust boundaries are documented
- tool scope is narrower and declared
- secret handling is clearer
- cost abuse is less likely to go unnoticed
- posture score improves for reasons that are explainable
