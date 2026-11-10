# agent-skill-architect — turn expertise into a tested, shippable Skill

For people who want to package a workflow they know well (in any field, not just social media) as an Agent Skill that others can install, trust and keep updated.

## What it gives you
- A guided process from brief to package: scope, activation rules, workflow, references, examples, tests and a changelog.
- **Quality gates** and a template, so a skill is reviewed against the same list every time.
- A clear split between a **skill** (instructions), an **agent** (a runtime that acts), a **tool** (a connector) and **infrastructure**, so you do not promise what you did not build.
- An evaluation template for activation and behaviour cases, and packaging and versioning guidance.

## Try it
- "Turn our onboarding checklist for new clients into a skill, with tests."
- "Audit this skill against the quality gates and list what to fix, in order."
- "Is this a skill, an agent, or a tool? Explain what I would have to build."

## You bring
The workflow knowledge, example inputs and outputs, and honest limits of what it cannot do.

## Boundaries
It produces skills and specifications. It does not build production services unless asked, and it will not invent connectors, compliance claims or passing tests.

Install: see the suite README, or `python scripts/install_skills.py --skill agent-skill-architect`.
