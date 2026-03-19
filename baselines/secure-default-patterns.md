# Secure default patterns

These patterns are meant to reduce accidental exposure and governance drift for early GRITS users.

## Pattern 1: Local development

Use when:
- one builder is experimenting locally
- no durable production operation is intended

Defaults:
- non-production environment marking
- narrow tool set
- no sensitive external integrations by default
- explicit owner even for solo builds
- short review window before continued use

## Pattern 2: Home lab

Use when:
- a self-hoster runs one or several persistent agents
- mixed experimentation and real use may coexist

Defaults:
- clearer separation between test and always-on workloads
- explicit trust boundary for operators
- reduced exposed surfaces
- minimal event capture for meaningful actions
- cost guardrails for persistent workloads

## Pattern 3: Always-on deployment

Use when:
- an agent or app stays active continuously
- production-like availability is expected

Defaults:
- accountable owner and deputy owner
- baseline monitoring and runtime event capture
- declared tool scope
- recertification date required
- suspension path defined

## Why these patterns exist

They make GRITS feel usable early instead of forcing every user to start from a blank governance design.