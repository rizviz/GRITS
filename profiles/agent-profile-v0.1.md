# Agent Profile v0.1

## Purpose

The Agent Profile tailors GRITS expectations for systems that act with partial or full autonomy, invoke tools or workflows, access external systems, or operate with durable runtime identity and permissions.

## This profile applies when

A system should usually be treated as an Agent Profile object if it has one or more of these traits:

- invokes tools or plugins
- can access systems or data beyond a simple chat exchange
- performs multi-step work with delegated action
- runs on a schedule, trigger, or persistent basis
- can materially affect cost, operations, data, or external state

## Minimum requirements

| Requirement area | Minimum expectation |
|---|---|
| identity and ownership | durable object record with owner and deputy owner |
| autonomy classification | autonomy tier assigned |
| impact classification | impact tier assigned |
| tool governance | declared tool permissions and categories |
| lifecycle governance | valid lifecycle state and recertification date |
| runtime assurance | event and evidence capture for meaningful actions |
| control posture | required baseline controls applied for deployment pattern |

## Controls that matter most in this profile

- explicit ownership
- tool scope declaration
- human approval for sensitive actions where required
- runtime monitoring and policy violation capture
- cost guardrails for loops and expansion risk
- recertification after material change

## Typical failure modes this profile tries to prevent

- shadow agents running outside review
- cloned agents with different permissions
- stale permissions retained after environment changes
- budget or token abuse from loops
- owner loss after experiments become production systems

## What to use with this profile

- [enterprise/agent-lifecycle-model-v0.1.md](../enterprise/agent-lifecycle-model-v0.1.md)
- [baselines/openclaw-deployment-hardening-baseline-v0.1.md](../baselines/openclaw-deployment-hardening-baseline-v0.1.md)
- [signals/runtime-signal-model-v0.1.md](../signals/runtime-signal-model-v0.1.md)
- [assessment/scorecard-model-v0.1.md](../assessment/scorecard-model-v0.1.md)
