# Contributing

Thanks for helping improve GRITS.

## Contribution priorities for v0.1

The most useful contributions right now are:

1. runtime baselines and playbooks grounded in real deployments
2. lifecycle edge cases and governance failure modes
3. signal/event schema feedback
4. example scorecards and remediation flows
5. profile refinements that reduce ambiguity without adding bureaucracy

## Principles for contributions

- implementation over abstraction
- explicit scope over vague generality
- portability over vendor lock-in
- evidence over assertions
- simple first release over premature completeness

## Preferred contribution types

| Type | Example |
|---|---|
| baseline | runtime-specific minimum control set |
| playbook | remediation or operational sequence |
| profile | tailored applicability guidance |
| signal/event feedback | runtime event names, evidence payloads, drift triggers |
| assessment example | scorecards, findings, remediation ordering |

## What to avoid in v0.1

- turning GRITS into a full product spec
- overfitting to one runtime as if it were universal
- adding sector-specific complexity before the core stabilizes
- adding long philosophy sections without operational consequence

## How to propose a change

1. describe the problem to solve
2. say which audience benefits
3. state whether it belongs in Core, Profile, Baseline, Playbook, Signals, or Assessment
4. include concrete examples when possible
