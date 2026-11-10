# Worked example — packaging a client-onboarding checklist as a skill (illustrative)

**Source:** a consultancy's 15-step client onboarding checklist, currently a document.

1. **Brief.** Who uses it (account managers), what outcome (a client fully set up in one week), what must never happen (sending a client's data to the wrong place). Capture 3 real past onboardings as examples.
2. **Classify the pieces** (`references/agent-vs-skill-vs-tool.md`).
   - Skill: the order of steps, the questions to ask, the checks.
   - Tool: creating accounts or sending email — **not** part of the skill; documented as a requirement.
   - Agent: not needed.
3. **Write the activation rules.** Activate on "onboard a new client"; do not activate on "fix a billing error". Add both as test cases.
4. **Draft `SKILL.md`** from the template: mission, role, activate/do-not-activate, workflow with an approval step before any external action, failure handling.
5. **References and examples.** Move the long checklist to `references/`, add one worked example per past onboarding.
6. **Quality gates** (`references/skill-quality-gates.md`): front matter valid, name matches folder, every claim testable, no invented tools, links resolve.
7. **Evaluate.** Run the activation cases from `references/evaluation-template.json`; record pass or fail honestly, including the ones that failed.
8. **Package and version.** README, changelog, version 0.1.0, ZIP with the skill folder at its root; verify installation on a clean machine.

Output delivered: the skill folder, test cases with results, quality-gate report, known limits.
