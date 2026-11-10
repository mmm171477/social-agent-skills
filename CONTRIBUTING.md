# Contributing

1. Open an issue describing the user problem and the proposed Skill boundary.
2. Check whether an existing Skill already owns the workflow. Avoid duplicate skills.
3. Keep `SKILL.md` focused; move long reference material into `references/`.
4. Add positive and negative activation cases in `tests/activation-cases.json`.
5. Cite official primary sources for changing platform behavior and record the date checked.
6. Run `python scripts/validate_skills.py` and `python -m unittest discover -s tests -v`.
7. Include a changelog entry and explain breaking changes.

Do not submit secrets, copied proprietary materials, undocumented endpoints or unsupported compatibility claims.
