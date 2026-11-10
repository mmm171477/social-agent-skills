# How to use the Social Agent Skills suite

## 1. Install (2 minutes)
Python 3 for the installer (tested on 3.12); the skills themselves are markdown.
```bash
python scripts/install_skills.py --target project --project-root . --skill instagram-agent    # one skill, this project
python scripts/install_skills.py --target user                                               # all seven, for every project
```
Existing skills are skipped unless you add `--overwrite` (a backup is made). Other hosts: copy a skill folder to wherever your tool reads Agent Skills (loading in tools other than those documented is untested).

## 2. Start with the core skill
1. Install `social-media-core` and the platform skills you use.
2. Ask: "Fill in the brand brief (`references/brand-brief-template.md`) from our last 20 posts and flag what is missing."
3. Fix the gaps it lists; do not let it guess.

## 3. Use a platform skill
Pick the matching skill and start from its sample prompts (`skills/<name>/examples/sample-prompts.md`):
| Need | Skill | First prompt to try |
|---|---|---|
| Package a video | `youtube-agent` | "Package this video: <title>. 3 title/thumbnail pairs, chapters, description." |
| Carousel or Reel | `instagram-agent` | "Turn this blog post into a 7-slide carousel with alt text." |
| Short-form hooks | `tiktok-agent` | "Write 5 hooks, each from a different angle." |
| Snapchat access | `snapchat-agent` | "Do we qualify to publish through an API? Walk me through." |
| Customer messaging | `whatsapp-agent` | "Draft three order-status templates and the pre-flight check." |
| Cross-platform campaign | `social-media-core` | "Build a 4-week campaign across these platforms from this announcement." |
| Your own skill | `agent-skill-architect` | "Turn this checklist into a skill, with tests." |

## 4. Approve before anything goes live
Each skill shows the exact action (account, asset, caption, schedule) and waits. Nothing is posted by these skills; posting needs your own official, authorized tool and your approval.

## 5. Test that a skill behaves
```bash
python scripts/print_activation_cases.py youtube-agent
```
Paste each case into your agent and tick the checklist: the positive cases should follow the workflow; the negative cases (buying views, bots, bulk spam) should be refused or routed.

## 6. *(Pro, not included in the Community edition)* Use the commercial kit
See `commercial-kit/HOW-TO-USE.md` and the filled examples in `commercial-kit/samples/`.

## 7. Validate and package your own changes
```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/package_skills.py --out dist
```
