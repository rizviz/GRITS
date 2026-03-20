# Quickstart

This repo supports two fast starts.

## Option 1: Harden an OpenClaw-style deployment in under 15 minutes

### 1. Install the tiny tool dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Check what profile applies

```bash
python tools/grits_profile_selector_v2.py examples/sample-agent-record.yaml
```

Expected result: the system is classified as an Agent Profile candidate.

### 3. Run the OpenClaw checklist

```bash
python tools/grits_openclaw_checklist_v2.py examples/sample-openclaw-posture.yaml
```

Expected result: a short list of passes, warnings, and priority fixes.

### 4. Generate a scorecard

```bash
python tools/grits_scorecard_v2.py examples/sample-openclaw-posture.yaml
```

Expected result: a JSON scorecard with control results, severity, posture band, and top remediation actions.

### 5. Use the baseline and playbook

- baseline: [baselines/openclaw-deployment-hardening-baseline.md](baselines/openclaw-deployment-hardening-baseline.md)
- remediation: [playbooks/openclaw-remediation-playbook.md](playbooks/openclaw-remediation-playbook.md)

## Option 2: Start the lifecycle governance track

### 1. Read the lifecycle model

- [enterprise/agent-lifecycle-model.md](enterprise/agent-lifecycle-model.md)

### 2. Review the minimum agent record

- [enterprise/agent-registry-schema.md](enterprise/agent-registry-schema.md)

### 3. Review the runtime signal model

- [signals/runtime-signal-model.md](signals/runtime-signal-model.md)

### 4. Review score outputs

- [assessment/scorecard-model.md](assessment/scorecard-model.md)
- [examples/sample-scorecard.json](examples/sample-scorecard.json)

## Fast path by persona

| Persona | First three files |
|---|---|
| self-hoster or OpenClaw user | QUICKSTART -> OpenClaw baseline -> OpenClaw remediation playbook |
| agent builder | QUICKSTART -> Agent Profile -> secure default patterns |
| governance or platform lead | QUICKSTART -> Agent Lifecycle Model -> registry schema |

## What success looks like after the first pass

You should be able to answer:

- what kind of system you have
- what minimum metadata and ownership it needs
- what baseline controls apply now
- what your highest-priority gaps are
- what events and evidence you should capture over time
