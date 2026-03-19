# Runtime Signal Model v0.1

## Purpose

GRITS needs a runtime signal model because point-in-time hardening is not enough.

A governed agent or LLM app can drift after approval through:

- ownership changes
- tool scope changes
- policy drift
- cost abuse
- repeated violations
- stale trust assumptions

Runtime signals create the minimum vocabulary for continuous governance.

## Design rule

GRITS v0.1 defines the event vocabulary and evidence expectations. It does not require a specific telemetry product.

## Core signal categories

| Category | Purpose |
|---|---|
| object lifecycle | registration, update, promotion, restriction, suspension, retirement |
| approvals | approvals requested, granted, denied, expired |
| tool and scope | tool invocation, scope violation, permission drift |
| policy and trust | policy violation, trust reduction, trust renewal |
| ownership and review | owner missing, review completed, recertification due |
| financial and runtime abuse | cost threshold exceeded, runaway loop detected |

## Example event names

- agent_registered
- agent_promoted
- agent_updated
- tool_invocation
- approval_requested
- approval_denied
- policy_violation
- scope_violation
- cost_threshold_exceeded
- owner_missing
- recertification_due
- agent_suspended
- agent_retired

## Minimum event fields

| Field | Required | Description |
|---|---|---|
| event_id | Yes | unique event identifier |
| event_type | Yes | event name/category |
| object_id | Yes | governed object identifier |
| timestamp | Yes | when the event occurred |
| environment | Yes | where it occurred |
| severity | Recommended | operational significance |
| actor | Recommended | person, system, or agent initiating action |
| evidence_ref | Recommended | pointer to supporting evidence |
| notes | Optional | short human-readable context |

## Minimum runtime signals expected for higher-trust operation

- meaningful tool invocation visibility
- policy violation visibility
- owner/review expiry visibility
- cost or abuse anomaly visibility
- lifecycle transition visibility

## Why this matters

Without a runtime signal model, GRITS would remain a static baseline framework and would not support runtime assurance or trust decay over time.
