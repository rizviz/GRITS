# GRITS

Open lifecycle governance and runtime assurance for AI agents and LLM systems.

GRITS helps teams do two things without switching frameworks:

1. secure and govern one deployment now
2. govern agent fleets over time

It is not another abstract AI policy framework. It is an implementation-first package of profiles, baselines, lifecycle rules, runtime signals, and assessment artifacts that teams can actually use.

## Why someone would use this

| If you are... | You probably care about... | GRITS gives you... |
|---|---|---|
| running OpenClaw, NemoClaw, or similar agent runtimes | hardening quickly, reducing mistakes, seeing clear gaps | hardening baselines, remediation playbooks, scan/score/remediate workflow |
| building agents or LLM apps | knowing what controls apply without bureaucracy | Agent Profile, LLM App Profile, secure default patterns, approval and evidence expectations |
| leading platform, governance, or security at scale | ownership, lifecycle, drift, runtime monitoring, recertification | Agent Lifecycle Model, managed-object schema, runtime signal model, transition gates, scorecards |

## What you get in this repo today

### Adoption Engine track

Built for operators, builders, self-hosters, and small teams who need immediate value.

- OpenClaw deployment hardening baseline
- OpenClaw remediation playbook
- secure default presets for local dev, home lab, and always-on agents
- starter tooling to classify, check, and score systems
- sample profiles and examples

### Enterprise Reference track

Built for teams planning to govern many agents over time.

- Agent Lifecycle Model
- managed-object model for agents and LLM apps
- ownership and accountability model
- transition gates and recertification logic
- runtime signal model and evidence requirements
- assessment and scorecard model

## Start here

### Path A — I want to harden an existing agent deployment

Read these first:

1. [QUICKSTART.md](QUICKSTART.md)
2. [baselines/openclaw-deployment-hardening-baseline-v0.1.md](baselines/openclaw-deployment-hardening-baseline-v0.1.md)
3. [playbooks/openclaw-remediation-playbook-v0.1.md](playbooks/openclaw-remediation-playbook-v0.1.md)

Then run:

```bash
python tools/grits_profile_selector_v2.py examples/sample-agent-record.yaml
python tools/grits_openclaw_checklist_v2.py examples/sample-openclaw-posture.yaml
python tools/grits_scorecard_v2.py examples/sample-openclaw-posture.yaml
```

### Path B — I want to define how agents are governed over time

Read these first:

1. [enterprise/agent-lifecycle-model-v0.1.md](enterprise/agent-lifecycle-model-v0.1.md)
2. [enterprise/agent-registry-schema-v0.1.md](enterprise/agent-registry-schema-v0.1.md)
3. [signals/runtime-signal-model-v0.1.md](signals/runtime-signal-model-v0.1.md)
4. [assessment/scorecard-model-v0.1.md](assessment/scorecard-model-v0.1.md)

## What GRITS is and is not

GRITS is:

- an open framework for lifecycle governance and runtime assurance
- profile-driven and implementation-oriented
- useful at point-agent scale and fleet scale
- designed to work with broader frameworks rather than pretending they do not exist

GRITS is not:

- a new agent runtime
- a full control plane product
- a certification scheme in v0.1
- only a hardening checklist

## Framework comparison, value first

| Framework | Best used for | Where GRITS adds value | When GRITS is the faster starting point |
|---|---|---|---|
| ATF | Zero Trust governance for autonomous agents | adds profiles, baselines, lifecycle artifacts, runtime signals, and direct adoption artifacts | when builders/operators need something they can apply immediately to an existing runtime |
| NIST AI RMF | broad enterprise AI risk management and governance alignment | translates high-level outcomes into deployable controls, baselines, evidence, and assessment artifacts | when a team needs an operational package, not just a governance umbrella |
| OWASP agentic / GenAI guidance | risk identification, threat awareness, and mitigation categories | organizes those concerns into profiles, lifecycle governance, baselines, and scorecards | when a team wants one operational frame instead of separate guidance documents |
| AAGATE | control-plane-oriented continuous governance for agentic AI | provides an open framework layer that can be used without adopting a full platform architecture | when the user needs a lightweight open framework before or instead of a larger platform build |

A longer comparison is in [docs/value-first-framework-comparison-v0.1.md](docs/value-first-framework-comparison-v0.1.md).

## The GRITS structure in one view

| Layer | What it does | Primary audience |
|---|---|---|
| Core | defines terms, object model, control logic, conformance concepts | everyone |
| Profiles | tells users what applies to their system type | builders and reviewers |
| Baselines / Playbooks | shows how to deploy and remediate in real runtimes | operators and self-hosters |
| Runtime Signals | defines continuous governance evidence and event vocabulary | platform and governance teams |
| Assessment | turns evidence into findings and scorecards | security, governance, operators |

## Immediate release logic

GRITS v0.1 intentionally ships both tracks together:

- Adoption Engine proves GRITS is useful today
- Enterprise Reference proves GRITS can scale beyond one host or one agent

If GRITS shipped only baselines, it would stay a hardening pack.
If GRITS shipped only enterprise references, it would be read and ignored.

## Repository map

```text
core/         framework definitions and conformance concepts
profiles/     Agent and LLM App profiles
baselines/    deployable minimum baselines
playbooks/    remediation and operations playbooks
signals/      runtime signal and evidence model
assessment/   scorecards, findings, severity, remediation mapping
adoption/     presets and quick-start workflows
enterprise/   lifecycle, registry, ownership, transition, runtime assurance refs
tools/        starter scripts
examples/     sample records, posture files, events, and scorecards
docs/         audience-facing overview, comparison, roadmap, FAQ
```

## Who should read what first

- OpenClaw / NemoClaw user: [WHO_IS_THIS_FOR.md](WHO_IS_THIS_FOR.md) -> [QUICKSTART.md](QUICKSTART.md) -> OpenClaw baseline
- agent builder: [WHO_IS_THIS_FOR.md](WHO_IS_THIS_FOR.md) -> [profiles/agent-profile-v0.1.md](profiles/agent-profile-v0.1.md)
- enterprise platform or governance lead: lifecycle model -> registry schema -> runtime signal model

## Release boundaries for v0.1

Included now:

- lifecycle model
- managed-object model
- Agent Profile and LLM App Profile
- OpenClaw baseline and remediation playbook
- runtime signal model
- scorecard model
- starter scripts and examples

Deferred beyond v0.1:

- full control plane product design
- sector overlays
- deep agent-to-agent delegation trust model
- automated multi-runtime discovery
- certification program

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The most valuable contributions for v0.1 are:

- runtime-specific baselines
- lifecycle edge cases
- signal/event schema feedback
- example scorecards and real remediation sequences
