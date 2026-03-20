# GRITS

Open lifecycle governance and runtime assurance for AI agents and LLM systems.

GRITS helps teams do two things without switching frameworks:

1. secure and govern one deployment now
2. govern agent fleets over time

GRITS is not another abstract AI policy framework. It is an implementation-first package of profiles, baselines, lifecycle rules, runtime signals, and assessment artifacts that teams can actually use.

## Who this is for

| If you are... | You probably care about... | GRITS gives you... |
|---|---|---|
| running OpenClaw, NemoClaw, or similar agent runtimes | hardening quickly, reducing mistakes, seeing clear gaps | deployment baselines, remediation playbooks, secure defaults, scan/score/remediate workflow |
| building agents or LLM apps | knowing what controls apply without bureaucracy | Agent Profile, LLM App Profile, ownership rules, lifecycle model, practical defaults |
| leading platform, governance, or security at scale | ownership, lifecycle, drift, runtime monitoring, recertification | managed-object model, Agent Lifecycle Model, transition gates, runtime signal model, scorecards |

## What you get in this repo

### Adoption Engine track

Built for operators, builders, self-hosters, and small teams who need immediate value.

- OpenClaw deployment hardening baseline
- OpenClaw remediation playbook
- secure default patterns for local dev, home lab, and always-on agents
- starter tooling to classify, check, and score systems
- sample profiles and examples

### Enterprise Reference track

Built for teams planning to govern many agents over time.

- Agent Lifecycle Model
- managed-object model for agents and LLM apps
- ownership and accountability model
- transition gates and recertification logic
- runtime signal model and evidence requirements
- scorecard model and severity mapping

## Start here

### Path A — I want to harden an existing agent deployment

Read these first:

1. [QUICKSTART.md](QUICKSTART.md)
2. [baselines/openclaw-deployment-hardening-baseline.md](baselines/openclaw-deployment-hardening-baseline.md)
3. [playbooks/openclaw-remediation-playbook.md](playbooks/openclaw-remediation-playbook.md)

Then run:

```bash
python tools/grits_profile_selector_v2.py examples/sample-agent-record.yaml
python tools/grits_openclaw_checklist_v2.py examples/sample-openclaw-posture.yaml
python tools/grits_scorecard_v2.py examples/sample-openclaw-posture.yaml
```

### Path B — I want to define how agents are governed over time

Read these first:

1. [enterprise/agent-lifecycle-model.md](enterprise/agent-lifecycle-model.md)
2. [enterprise/agent-registry-schema.md](enterprise/agent-registry-schema.md)
3. [signals/runtime-signal-model.md](signals/runtime-signal-model.md)
4. [assessment/scorecard-model.md](assessment/scorecard-model.md)

## Why use GRITS

| Outcome | Why it matters |
|---|---|
| Saves time | teams do not have to invent lifecycle governance and deployment baselines from scratch |
| Accelerates development | builders know what controls apply without dragging in full enterprise bureaucracy |
| Promotes trust | ownership, lifecycle state, review dates, and runtime signals are made explicit |
| Improves security | hardening baselines and remediation playbooks reduce avoidable mistakes |
| Reduces drift | recertification, runtime events, and transition gates make governance continuous |
| Scales better | one agent and one thousand agents can be governed with the same framework language |

## Framework comparison, value first

| Framework | Best used for | Where GRITS adds value | When GRITS is the faster first move |
|---|---|---|---|
| ATF | Zero Trust-style governance for autonomous agents | adds deployable baselines, lifecycle artifacts, runtime signals, and adoption-ready implementation guidance | when builders or operators need something they can apply immediately to an existing runtime |
| NIST AI RMF | broad enterprise AI risk management alignment | translates high-level governance outcomes into deployable controls, baselines, evidence, and scorecards | when a team needs an operational package, not just a governance umbrella |
| OWASP agentic or GenAI guidance | risk identification, threat awareness, and mitigation categories | organizes those concerns into profiles, lifecycle governance, baselines, runtime signals, and scorecards | when a team wants one operational frame instead of separate guidance documents |
| AAGATE | platform-oriented continuous governance and control-plane thinking | provides an open framework layer that can be used without adopting a full platform architecture | when the goal is lightweight adoption, open artifacts, and runtime-agnostic structure |

A longer comparison is in [docs/comparisons.md](docs/comparisons.md).

## The GRITS structure in one view

| Layer | What it does | Primary audience |
|---|---|---|
| Core | defines terms, object model, lifecycle logic, control families, and conformance concepts | everyone |
| Profiles | tells users what applies to their system type | builders and reviewers |
| Baselines and playbooks | shows how to deploy and remediate in real runtimes | operators and self-hosters |
| Runtime signals | defines continuous governance evidence and event vocabulary | platform and governance teams |
| Assessment | turns evidence into findings and scorecards | security, governance, operators |

## Immediate release logic

GRITS ships both tracks together:

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
enterprise/   lifecycle, registry, ownership, transition, runtime assurance refs
tools/        starter scripts
examples/     sample records, posture files, events, and scorecards
docs/         audience-facing comparison, metadata, FAQ, roadmap
```

## Release boundaries

Included now:

- lifecycle model
- managed-object model
- Agent Profile and LLM App Profile
- OpenClaw baseline and remediation playbook
- runtime signal model
- scorecard model
- starter scripts and examples

Deferred beyond this starter package:

- full control-plane product design
- sector overlays
- deep agent-to-agent delegation trust model
- automated multi-runtime discovery
- certification program

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). The most valuable contributions are:

- runtime-specific baselines
- lifecycle edge cases
- signal and event schema feedback
- example scorecards and real remediation sequences
