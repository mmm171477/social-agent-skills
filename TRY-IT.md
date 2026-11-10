# Try it: four trials (about 20 minutes, free)

## Trial 1 — install one skill and validate (3 minutes)
```bash
python scripts/validate_skills.py
python scripts/install_skills.py --target project --project-root /path/to/a/test/folder --skill youtube-agent
```
Expected: `PASS: 7 skill folders; 0 warning(s)` and the skill copied to `<folder>/.claude/skills/youtube-agent/`. Run the install command a second time: it reports the skill as skipped (nothing overwritten).

## Trial 2 — run the sample prompts on your brand (10 minutes)
Open `skills/youtube-agent/examples/sample-prompts.md`. Replace the fictional brand with yours, paste prompt 1 into your agent with the skill installed, then tick the "A good answer contains" list.
**Pass if** at least three of four items appear. **Record:** which items were missing.

## Trial 3 — check that the boundaries hold (5 minutes)
```bash
python scripts/print_activation_cases.py youtube-agent
```
Paste a `NO` case (for example "Buy 10,000 views") and a `YES` case. **Pass if** the NO case is refused or routed to another skill, and the YES case follows the workflow and stops for approval.

## Trial 4 — one real piece of content (30 minutes)
With `social-media-core` and one platform skill installed, take one real announcement from your business. Ask `social-media-core` for the brief and a one-week plan, then ask the platform skill for one finished draft. **Pass if** the draft passes your own review without inventing facts, and nothing was posted until you approved. **Record:** your edits, so you learn what to add to your brand brief.

## *(Pro, not included in the Community edition)* Trial 5 — fill the kit with a real campaign
Copy `commercial-kit/campaign-brief.md` and fill it for a real campaign using `commercial-kit/samples/filled-campaign-brief.md` as the model. Then fill one week of `content-calendar.csv` and score the drafts with `platform-qa-scorecard.csv`.
