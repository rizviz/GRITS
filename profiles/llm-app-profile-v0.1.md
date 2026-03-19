# LLM App Profile v0.1

## Purpose

The LLM App Profile tailors GRITS expectations for systems such as chat applications, copilots, prompt wrappers, and RAG apps that may not cross the threshold into agentic behavior.

## This profile applies when

A system is better treated as an LLM App if it is primarily:

- interactive rather than delegated
- bounded to user-driven requests
- not broadly tool-acting on its own
- lower in autonomy than a full agent

## Minimum requirements

| Requirement area | Minimum expectation |
|---|---|
| identity and ownership | durable object record with owner |
| use and purpose | clear intended use and environment |
| data classification | declared sensitivity class |
| profile classification | explicitly marked as LLM App |
| lifecycle governance | valid lifecycle state and review date |
| deployment baseline | secure defaults appropriate to the app pattern |

## Controls that typically matter most

- prompt and policy boundary clarity
- data access boundaries
- response logging where appropriate
- environment separation
- review after significant capability change

## Why this profile exists

Without this profile, teams either under-govern agent-like systems or over-bureaucratize lighter LLM applications.

GRITS v0.1 keeps the distinction explicit.
