# Security policy

GRITS is a framework repository, not a production service. Security issues in this repo are most likely to relate to:

- starter scripts
- example configurations
- unsafe defaults in contributed baselines or playbooks
- secrets accidentally committed to examples or docs

## Reporting

Please report suspected security issues privately to the maintainers before opening a public issue if the report includes:

- an exploitable script defect
- a dangerous default likely to mislead users
- an example that exposes sensitive data patterns

## Scope reminder

GRITS does not claim that following a document in this repo is sufficient to make an agent or runtime safe. Local runtime context, identity, data boundaries, tooling, network posture, and operator trust assumptions still matter.
