# Who this is for

GRITS is deliberately built for two adjacent audiences.

## 1. Builders and operators who need immediate value

This includes:

- OpenClaw users
- NemoClaw users
- self-hosters
- tinkerers
- small agent teams
- developers shipping internal LLM apps

### What they usually care about

- can I harden this quickly
- what should I fix first
- what controls actually apply to my setup
- how do I avoid turning this into bureaucracy

### What to read first

- [QUICKSTART.md](QUICKSTART.md)
- [baselines/openclaw-deployment-hardening-baseline-v0.1.md](baselines/openclaw-deployment-hardening-baseline-v0.1.md)
- [profiles/agent-profile-v0.1.md](profiles/agent-profile-v0.1.md)

## 2. Teams planning to operate many agents over time

This includes:

- enterprise AI platform teams
- security teams
- governance teams
- enterprise architects
- operating model owners

### What they usually care about

- which agents exist
- who owns them
- what they are allowed to do
- how promotion and runtime changes are governed
- how trust decays or is renewed
- how orphaned or shadow agents are handled

### What to read first

- [enterprise/agent-lifecycle-model-v0.1.md](enterprise/agent-lifecycle-model-v0.1.md)
- [enterprise/agent-registry-schema-v0.1.md](enterprise/agent-registry-schema-v0.1.md)
- [signals/runtime-signal-model-v0.1.md](signals/runtime-signal-model-v0.1.md)

## When GRITS is probably not the right first thing

GRITS is not the best first stop if you are looking only for:

- a new runtime to run agents
- a fully managed enterprise product
- a formal certification regime
- sector-specific legal/regulatory mapping out of the box

## Why GRITS tries to serve both groups

If the framework only serves builders, it stays tactical.
If it only serves enterprise governance teams, it becomes shelfware.

GRITS exists to connect the two:

- concrete deployment baselines for adoption
- lifecycle governance references for scale
