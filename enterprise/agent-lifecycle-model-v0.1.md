# Agent Lifecycle Model v0.1

## Purpose

The GRITS Agent Lifecycle Model defines how an agent is governed from creation through retirement.

Its purpose is to reduce:

- shadow agents
- orphaned agents
- uncontrolled promotion
- stale permissions
- policy drift
- trust decay
- weak suspension and retirement handling

## What counts as an agent in v0.1

An agent is a governed software object that can process instructions and has one or more of the following:

- tool use
- workflow invocation
- access to external systems or data beyond a simple chat interaction
- delegated or semi-autonomous action
- durable identity with permissions or runtime state

## Minimum lifecycle states

| State | Meaning |
|---|---|
| Draft | being designed or edited |
| Proposed | submitted for review with initial metadata |
| Approved | accepted for controlled implementation/testing |
| Test | operating in a constrained test environment |
| Staged | production-like pre-release state |
| Production | approved for live operation |
| Restricted | allowed to exist but with narrowed permissions or scope |
| Suspended | not permitted to continue normal runtime activity |
| Retired | formally decommissioned |

## Required transition gates

| Transition | Minimum expectations |
|---|---|
| Draft -> Proposed | owner assigned, purpose stated, profile chosen, required metadata present |
| Proposed -> Approved | impact and autonomy tiers assigned, declared tool scope recorded |
| Approved -> Test | baseline controls applied, monitoring enabled, test scope defined |
| Test -> Staged | findings reviewed, failures dispositioned, evidence recorded |
| Staged -> Production | production approval complete, rollback/suspension path defined, recert date set |
| Production -> Restricted | reduced trust or narrowed permissions justified and recorded |
| Active -> Suspended | incident, owner failure, policy breach, or high-risk anomaly recorded |
| Any -> Retired | access revoked, decommission recorded, historical record retained |

## Required evidence by state

| State | Evidence |
|---|---|
| Proposed | complete metadata, owner acceptance, purpose statement |
| Approved | profile applicability, tool scope declaration, initial risk classification |
| Test | test logs, review notes, failure handling evidence |
| Staged | remediation status, approver record, readiness review |
| Production | monitoring active, trust status active, recertification set, owner valid |
| Restricted | restriction reason, narrowed scope, follow-up plan |
| Suspended | trigger evidence, accountable reviewer, reinstatement conditions |
| Retired | decommission evidence, permission removal, record archival |

## Recertification model

Every Production agent must have:

- a recertification_due date
- a last_review_date
- a valid owner
- a recorded trust_status

Recertification should be triggered by both time and change.

### Trigger examples

- owner missing or changed
- material prompt or model change
- tool scope change
- environment promotion
- repeated policy violations
- abnormal cost pattern or runaway loop condition
- prolonged inactivity with residual permissions

## v0.1 caution

This model defines the governance logic. It does not require a specific workflow engine, ticketing system, database, or control plane.
