# Skill architect playbook

## 1. Start from real work
Collect two or three real examples of the task done well, including inputs and the final output. A skill built from imagination reads as generic. Examples are the raw material.

## 2. Decide what it is
| If it is… | Build a… |
|---|---|
| a repeatable way of working, a checklist, a set of judgement rules | Skill |
| something that must act on its own, loop, or hold state | Agent (runtime) |
| a connection to an external system | Tool or connector |
| hosting, auth, scheduling | Infrastructure |
Do not label a skill as an integration. Say what the user must connect.

## 3. Write sharp activation rules
Description in one or two sentences: what it does and when to use it. Add explicit "do not activate" cases, since near-miss requests are where skills misfire.

## 4. Structure
`SKILL.md` stays short: mission, role, activate and do-not-activate, workflow, outputs, success measures, failure handling. Long material goes to `references/`; worked scenarios to `examples/`; cases to `tests/`.

## 5. Make claims testable
Every promise becomes a test case with an input and an expected behaviour (activate or not, produce this section, refuse this request). Untestable claims are removed or reworded.

## 6. Safety defaults
Approval before external side effects, least privilege, no secrets in files, idempotent retries, and "unknown" instead of invention. Copy these from a reviewed skill rather than rewriting them.

## 7. Release checklist
Front matter valid and name matches the folder · links resolve · tests listed with results · README states limits · changelog updated · ZIP verified on a clean machine · no private data.

## 8. Maintenance
Version every change; record what you checked and when; retire outdated platform facts instead of leaving them to rot.
