# Managed Object Model v0.1

## Why this exists

Lifecycle governance fails if the governed object is undefined.

GRITS treats agents and LLM applications as managed objects. That means each one must have a durable record, an accountable owner, a defined purpose, declared scope, and a lifecycle state.

## Managed object types in v0.1

| Type | Description |
|---|---|
| Agent | a software object that can use tools, access data, invoke workflows, or act with partial or full autonomy |
| LLM App | a governed LLM-based system such as a chatbot, copilot, prompt wrapper, or RAG app that may not meet the threshold for agent autonomy |

## Minimum required fields

| Field | Required | Description |
|---|---|---|
| object_id | Yes | durable unique identifier |
| object_type | Yes | Agent or LLM App |
| name | Yes | human-readable name |
| owner | Yes | accountable owner |
| deputy_owner | Yes | backup accountable owner |
| business_purpose | Yes | intended use and reason for existence |
| profile_type | Yes | applicable GRITS profile |
| autonomy_tier | Yes | degree of permitted independence |
| impact_tier | Yes | operational or business criticality |
| data_sensitivity_class | Yes | expected data handling level |
| tool_permissions | Yes | allowed tools or tool categories |
| environment | Yes | dev, test, stage, prod, or equivalent |
| version | Yes | current version reference |
| lifecycle_state | Yes | current governance state |
| runtime_status | Yes | active, inactive, restricted, suspended, retired |
| trust_status | Yes | current trust posture |
| last_review_date | Yes | last formal review checkpoint |
| recertification_due | Yes | next required trust review date |

## Recommended fields

| Field | Description |
|---|---|
| lineage_source | parent, clone, or fork source |
| incident_history_ref | references to known incidents |
| budget_guardrails | spending or token budget constraints |
| model_dependencies | primary model/runtime dependencies |
| tool_owner_refs | accountable owner for high-risk tools |

## Required properties of a managed object

A governed object must be:

- identifiable
- attributable to a human owner
- classifiable by profile
- classifiable by autonomy and impact
- bounded by declared tool/data scope
- placeable in a lifecycle state
- reviewable over time

## Failure cases this model is meant to prevent

- shadow agents with no registry record
- orphaned agents with no live owner
- cloned/forked agents with undeclared permission changes
- stale agents still running with expired trust assumptions
- agents in production without recertification windows

## Notes for v0.1

GRITS does not require a specific database or registry implementation in v0.1. The framework requires the object model, not a mandatory platform.