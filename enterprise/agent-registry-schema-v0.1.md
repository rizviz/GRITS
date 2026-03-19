# Agent Registry Schema v0.1

## Purpose

The registry schema defines the minimum durable record required to govern an agent or LLM application over time.

The goal is not to require a specific product. The goal is to ensure each governed object has enough identity, ownership, scope, and lifecycle data to support review and runtime assurance.

## Minimum schema

| Field | Required | Notes |
|---|---|---|
| object_id | Yes | unique durable identifier |
| object_type | Yes | Agent or LLM App |
| name | Yes | human-readable object name |
| owner | Yes | primary accountable owner |
| deputy_owner | Yes | backup owner |
| business_purpose | Yes | concise intended use |
| profile_type | Yes | Agent Profile or LLM App Profile |
| autonomy_tier | Yes | local scheme permitted |
| impact_tier | Yes | local scheme permitted |
| data_sensitivity_class | Yes | local scheme permitted |
| tool_permissions | Yes | allowed tool categories/scopes |
| environment | Yes | dev/test/stage/prod equivalent |
| version | Yes | release or config version |
| lifecycle_state | Yes | GRITS lifecycle state |
| runtime_status | Yes | active/inactive/restricted/suspended/retired |
| trust_status | Yes | current trust disposition |
| last_review_date | Yes | most recent review checkpoint |
| recertification_due | Yes | next required review |

## Recommended schema extensions

| Field | Why useful |
|---|---|
| lineage_source | detect clones, forks, and inherited risk |
| incident_history_ref | track trust degradation over time |
| budget_guardrails | catch financial abuse and runaway loops |
| model_dependencies | record model/runtime dependencies |
| prompt_policy_ref | link to governing prompt or policy version |
| tool_owner_refs | clarify ownership for powerful tools |

## Required operational checks

A valid registered object should satisfy these conditions:

- has a live owner and deputy owner
- has a declared purpose and profile
- has declared tool permissions
- has a valid lifecycle state
- has a review timestamp and future recertification date

## Failure conditions this schema helps expose

- shadow objects without records
- orphaned objects without owners
- permission drift after cloning or forking
- production objects with expired review dates
- stale trust assumptions not reflected in runtime status
