# GRITS v0.1

Governance, Risk, Intelligence, Trust, and Security for implementable AI and agent systems.

GRITS is an open, implementation-first framework for operationalizing governance and security for LLM applications and agentic AI systems. It is designed for teams that need deployable controls, installable profiles, practical hardening guidance, and evidence-driven scoring rather than a policy-only checklist.

## Repository description

Open framework for implementable AI governance and security with profiles, hardening playbooks, scoring, and starter tooling for agentic and LLM application deployments.

## Why people should care

GRITS is for teams that are deploying AI now and do not have time to translate broad governance language into working controls.

What GRITS is meant to improve:

- saves time by shipping installable baselines instead of forcing teams to invent controls from scratch
- accelerates development by reducing ambiguity around approvals, tool usage, memory, ownership, and evidence
- improves trust by producing repeatable posture outputs instead of unverifiable claims
- reduces security mistakes by giving teams practical hardening playbooks and remediation paths
- improves portability by separating core controls from runtime-specific guidance
- makes customer and internal reviews easier through a common control language and scorecard

## Why OpenClaw and NemoClaw users would adopt GRITS

GRITS is not another runtime. It is the implementation layer that sits above and around runtimes.

For OpenClaw and NemoClaw style users, the immediate value is practical:

- secure defaults and baseline deployment patterns
- portable profiles for agent and LLM application types
- scan, score, and remediate workflow
- reusable hardening guidance across personal, team, and enterprise-style deployments
- visible evidence for trust, review, and customer assurance

The first wedge is simple: if a builder can harden a deployment faster, reduce mistakes, and show a posture report, GRITS is useful on day one.

## What GRITS is and is not

GRITS is:

- a control framework
- a profile system
- a set of implementation playbooks
- a scoring and assessment model
- starter tooling for adoption

GRITS is not:

- a new agent runtime
- a policy-only governance memo
- a full certification program in v0.1
- a replacement for every enterprise framework already in use

## Framework position: where GRITS fits relative to other approaches

GRITS should usually be used with broader or adjacent frameworks, not argued as their universal replacement.

### Agentic Trust Framework (ATF)

ATF is an open specification for Zero Trust governance for AI agents. It is strongest where the primary need is identity, segmentation, behavioral trust, and staged autonomy promotion. GRITS complements ATF by giving teams a lighter operational package with control IDs, deployable profiles, playbooks, remediation actions, and scorecards.

Use GRITS with ATF when:

- you want Zero Trust governance plus an implementation layer
- you need deployable hardening guidance and evidence collection
- you want a lightweight package that engineering teams can actually apply

Use GRITS instead of relying on ATF alone when:

- the immediate buyer is the builder or operator, not the enterprise governance committee
- you need one framework that covers both agents and lighter LLM apps
- you need runtime hardening playbooks now

### NIST AI RMF

NIST AI RMF is broad, voluntary, and useful for enterprise governance alignment. GRITS is narrower and more operational.

Use GRITS with NIST AI RMF when:

- you need to translate Govern, Map, Measure, and Manage into concrete controls
- you want a profile and playbook layer beneath enterprise AI governance

Use GRITS instead of relying on NIST AI RMF alone when:

- your team is small and needs practical baselines immediately
- you need deployable, profile-specific controls rather than abstract outcome statements

### OWASP GenAI / LLM / Agentic guidance

OWASP guidance is strong on risk categories, testing, and awareness. GRITS is stronger on packaging those concerns into control families, deployment profiles, playbooks, and scorecards.

Use GRITS with OWASP when:

- you want risk categories mapped to implementable controls
- you need remediation sequencing and evidence capture

Use GRITS instead of relying on OWASP guidance alone when:

- you need a lightweight operational framework instead of a threat list or testing guide
- you want deployable defaults and an adoption workflow

### AAGATE

AAGATE is positioned as a NIST AI RMF-aligned governance platform for agentic AI with a Kubernetes-native control-plane orientation. GRITS should not attempt to beat AAGATE by being broader. It should win by being lighter, more open, faster to adopt, and easier to apply to real runtimes.

Use GRITS with AAGATE when:

- you want a simpler open implementation layer around a larger assurance platform
- you need profiles, hardening playbooks, and scorecards that can exist independently of a control plane

Use GRITS instead of AAGATE when:

- adoption depends on installable artifacts and low-friction engineering usage
- the initial audience is OpenClaw/NemoClaw style builders and operators rather than platform architects

## Design principles

- implementation first
- profile driven
- minimal bureaucracy
- evidence over assertions
- portability across runtimes
- least privilege by default
- explicit trust boundaries
- human approval for sensitive actions
- open and inspectable artifacts

## Repository layout

```text
grits-v0.1/
  README.md
  LICENSE
  CONTRIBUTING.md
  SECURITY.md
  ROADMAP.md
  docs/
    overview/
      why-grits-v0.1.md
    getting-started/
      quickstart-v0.1.md
      how-to-use-grits-v0.1.md
    core/
      grits-core-v0.1.md
      control-catalog-v0.1.md
      conformance-scoring-v0.1.md
    profiles/
      agent-profile-v0.1.md
      llm-app-profile-v0.1.md
    playbooks/
      openclaw-hardening-playbook-v0.1.md
      openclaw-remediation-runbook-v0.1.md
    tooling/
      tooling-v0.1.md
    mappings/
      framework-comparison-v0.1.md
    strategy/
      adoption-wedge-v0.1.md
      strategy-framework-sync-protocol-v0.1.md
      repo-metadata-v0.1.md
  examples/
    sample-system-agent.yaml
    sample-system-llm-app.yaml
    sample-openclaw-posture.yaml
    sample-scorecard-agent.json
  tools/
    grits_profile_selector_v1.py
    grits_scorecard_v1.py
    grits_openclaw_checklist_v1.py
```

## Core deliverables in this repo

| Deliverable | What it does | Why it matters |
|---|---|---|
| GRITS Core | Defines domains, control families, IDs, conformance, maturity | Gives teams a stable control language |
| Agent Profile | Tailors controls to autonomous and semi-autonomous agents | Removes ambiguity for tool-using systems |
| LLM App Profile | Tailors controls to chat apps, copilots, RAG apps | Prevents over-engineering lighter systems |
| OpenClaw Hardening Playbook | Maps controls to real deployment actions | Delivers immediate practical value |
| Starter Tooling | Selects profile, checks posture, generates scorecard | Makes adoption fast and visible |
| Comparison Mapping | Explains where GRITS fits relative to NIST, OWASP, ATF, AAGATE | Prevents positioning confusion |
| Sync Protocol | Keeps strategy and framework work aligned | Avoids drift between vision and implementation |

## Outcomes by layer

| Layer | Outcome |
|---|---|
| Core | stable language for controls, evidence, and conformance |
| Profiles | clear applicability so teams know what actually applies |
| Playbooks | deployable hardening and remediation guidance |
| Tooling | faster adoption through executable checks and reports |
| Scoring | visible posture and prioritized remediation |

## How to use GRITS today

### Path 1: Classify and score an AI system

1. Start with `examples/sample-system-agent.yaml` or `examples/sample-system-llm-app.yaml`.
2. Run `python tools/grits_profile_selector_v1.py <system.yaml>`.
3. Pick the matching profile.
4. Record posture findings in a posture YAML file.
5. Run `python tools/grits_scorecard_v1.py <assessment.yaml>`.
6. Use the output as your initial remediation queue.

### Path 2: Harden an OpenClaw-style deployment

1. Read `docs/playbooks/openclaw-hardening-playbook-v0.1.md`.
2. Create a baseline posture file using `examples/sample-openclaw-posture.yaml`.
3. Run `python tools/grits_openclaw_checklist_v1.py examples/sample-openclaw-posture.yaml`.
4. Fix missing or weak controls.
5. Re-score with `grits_scorecard_v1.py`.

### Path 3: Use GRITS as a framework layer under other programs

1. Map enterprise requirements to GRITS control families.
2. Select the correct profile for each AI system.
3. Use playbooks for implementation.
4. Use scorecards for review and evidence.

## Quick start

Requirements:

- Python 3.10+
- `pip install -r requirements.txt`

Try it:

```bash
python tools/grits_profile_selector_v1.py examples/sample-system-agent.yaml
python tools/grits_openclaw_checklist_v1.py examples/sample-openclaw-posture.yaml
python tools/grits_scorecard_v1.py examples/sample-openclaw-posture.yaml
```

## Immediate v0.1 focus

GRITS v0.1 is intentionally narrow:

- agent systems
- LLM applications
- runtime and deployment controls
- hardening and posture scoring
- OpenClaw as the first concrete deployment playbook

## Non-goals for v0.1

- full regulatory compliance coverage
- sector-specific certification programs
- full multi-runtime auto-discovery
- cryptographic trust protocols
- exhaustive model evaluation methodology

## Next recommended contributions

- add NemoClaw deployment playbook
- add policy pack format and machine-readable control catalog
- add control-to-OWASP mapping by ID
- add sector overlays for finance, healthcare, and public sector
- add CI-friendly JSON schema validation

## References

- `docs/overview/why-grits-v0.1.md`
- `docs/getting-started/quickstart-v0.1.md`
- `docs/getting-started/how-to-use-grits-v0.1.md`
- `docs/mappings/framework-comparison-v0.1.md`
- `docs/strategy/adoption-wedge-v0.1.md`
- `docs/strategy/strategy-framework-sync-protocol-v0.1.md`
