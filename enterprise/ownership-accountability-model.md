# Ownership and accountability model

## Purpose

GRITS treats ownership as a first-class governance control because orphaned agents and unclear accountability are among the highest-risk failure modes in growing agent environments.

## Minimum accountability requirements

Every governed object should have:

- a primary owner
- a deputy owner
- a defined business purpose
- a defined approval authority for sensitive changes or actions

## Why deputy owners matter

A primary owner alone is not enough for durable governance. People change roles, go inactive, or forget experimental systems that later become production-adjacent.

## Failure modes this model tries to prevent

- orphaned production agents
- shadow agents with no accountable human
- approvals performed by unclear or inappropriate actors
- stale trust assumptions after owner changes

## Minimum v0.1 rule

A Production object without a valid owner and deputy owner should not remain in strong trust standing.
