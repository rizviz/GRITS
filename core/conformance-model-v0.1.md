# Conformance Model v0.1

## Purpose

GRITS conformance is meant to answer a practical question:

What evidence shows that this agent or LLM app is governed appropriately for its type, state, and deployment pattern?

## Conformance in v0.1

Conformance is based on five inputs:

1. object completeness
2. profile applicability
3. lifecycle-state expectations
4. baseline/control implementation status
5. evidence quality

## Result states

| Result | Meaning |
|---|---|
| Pass | required expectations are met with adequate evidence |
| Partial | some expectations are met, but material gaps remain |
| Fail | critical or multiple required expectations are missing |
| Not Applicable | the requirement does not apply to this object/profile/state |

## Evidence quality states

| Evidence state | Meaning |
|---|---|
| Verified | supported by observable data or direct validation |
| Asserted | claimed but not independently validated |
| Missing | required evidence absent |

## Conformance views

GRITS supports at least three useful views.

| View | Purpose |
|---|---|
| Deployment posture view | baseline and operational control posture for one deployment |
| Lifecycle governance view | whether the object meets expectations for its current state |
| Runtime assurance view | whether ongoing events and reviews support continued trust |

## v0.1 posture bands

| Band | Typical meaning |
|---|---|
| Baseline | minimum viable governance and hardening implemented |
| Progressing | core controls exist but gaps remain |
| Hardened | strong baseline and review discipline are in place |
| Advanced | sustained evidence, recertification, and tighter operating discipline |

## Important limit

GRITS v0.1 does not claim that a high score means a system is safe. It means the system shows stronger adherence to declared governance and runtime assurance expectations.
