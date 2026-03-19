# Scorecard Model v0.1

## Purpose

The GRITS scorecard turns profile applicability, lifecycle state, baseline posture, and evidence quality into a usable governance view.

It exists to answer:

- where are the most important gaps
- what should be fixed first
- what evidence is missing
- how strong is the current posture relative to the object's type and state

## Result states

| Result | Meaning |
|---|---|
| Pass | requirement met with adequate evidence |
| Partial | requirement partially met or evidence incomplete |
| Fail | requirement materially missing or contradicted |
| Not Applicable | requirement not relevant to the current object/profile/state |

## Severity bands

| Severity | Typical examples |
|---|---|
| Critical | missing owner in production, severe exposure, uncontrolled sensitive capability |
| High | over-scoped tools, expired review with active production object, missing policy violation visibility |
| Medium | weak evidence, incomplete documentation, missing lower-impact guardrails |
| Low | hygiene issues, minor consistency gaps |

## Posture bands

| Band | Meaning |
|---|---|
| Baseline | minimum viable governance and hardening present |
| Progressing | core expectations partly met but important gaps remain |
| Hardened | strong baseline and review posture in place |
| Advanced | strong evidence discipline and sustained lifecycle governance |

## Scorecard sections

A useful GRITS scorecard in v0.1 should include:

- object summary
- applicable profile
- lifecycle state
- control or requirement results
- evidence status
- severity summary
- top remediation actions
- next review / recertification checkpoint

## Important limit

The GRITS scorecard is a governance and assurance artifact. It is not a guarantee of safety.
