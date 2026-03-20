# Control catalog

This starter catalog is intentionally small. It is enough to anchor baselines, runtime signals, and scorecards without pretending the catalog is complete.

## Control families

| Family | Prefix | Purpose |
|---|---|---|
| Ownership | OWN | identity, accountability, review continuity |
| Lifecycle | LIF | state, transitions, recertification, retirement |
| Application and tools | APP | tool scope, execution paths, plugin control |
| Network | NET | exposure, reachability, boundary clarity |
| Secrets and host | SEC | secret handling, host hygiene, environment clarity |
| Runtime signals | SIG | monitoring, event visibility, policy-violation visibility |
| Financial | FIN | budget guardrails, runaway usage, cost anomalies |

## Initial controls

| ID | Title | Typical expectation |
|---|---|---|
| OWN-001 | Owner assigned | every managed object has a primary owner |
| OWN-002 | Deputy owner assigned | production or higher-trust objects have backup accountability |
| LIF-001 | Recertification set | active governed objects have a future review checkpoint |
| APP-001 | Tool scope declared | allowed tools or tool categories are explicitly declared |
| NET-001 | Network exposure reviewed | reachable services and management paths are deliberately reviewed |
| SEC-001 | Secrets handling recorded | the secret handling approach is documented and understood |
| SIG-001 | Monitoring enabled | meaningful runtime visibility exists for governed operation |
| SIG-002 | Policy violation visibility enabled | material policy or scope issues can be surfaced |
| FIN-001 | Cost guardrails defined | basic budget or token guardrails are set for sustained operation |
