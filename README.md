# Social Agent Skills Suite

**Portable, modular Agent Skills for social-media operations — plus a general Skill Architect.**

## Start here
- `docs/BENEFITS.md`: what the suite does for you and how to judge it
- `docs/HOW-TO-USE.md`: install, first prompts, approval, testing
- `TRY-IT.md`: four free trials, about 20 minutes
- `skills/<name>/examples/sample-prompts.md`: realistic prompts with checklists

## Included skills

| Skill | Purpose |
|---|---|
| `social-media-core` | Shared strategy, campaign operations, cross-platform adaptation and QA |
| `youtube-agent` | YouTube videos, Shorts, packaging, publishing preparation and analytics |
| `instagram-agent` | Reels, Stories, feed, carousels and professional-account workflows |
| `tiktok-agent` | TikTok-native short-form creative and authorized posting workflows |
| `snapchat-agent` | Public Profile, Stories and Spotlight workflows where eligible |
| `whatsapp-agent` | WhatsApp Business support, templates, consent-aware messaging and CRM workflows |
| `agent-skill-architect` | Build, test, document, version and package Skills for any domain |

Each skill is a standalone folder with `SKILL.md`, references, examples and activation tests. The skills follow the open Agent Skills folder format; host tools and permissions remain host-specific. See [portability](docs/PORTABILITY.md).

## Quick start

### Claude Code — project install

Run the safe installer (it skips existing skills by default):

```bash
python scripts/install_skills.py --target project --project-root . --skill instagram-agent
python scripts/install_skills.py --target user --skill youtube-agent
```

Omit `--skill` to install all seven. Add `--overwrite` only after reviewing the backup/replace impact.

### Claude.ai

ZIP one skill folder and upload it from **Customize → Skills** where available. Each upload should contain the skill folder at the archive root. See the official [Claude Skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Validate and package

```bash
python scripts/validate_skills.py
python -m unittest discover -s tests -v
python scripts/package_skills.py --out dist
```

## Architecture

- **Skills** provide procedural expertise and workflows.
- **Agents/runtimes** provide orchestration, model invocation, state and lifecycle.
- **Tools/connectors/MCP** provide actual external actions and data access.

A Skill does not create API credentials, grant permissions, publish content or run continuously by itself. Every platform-specific write operation must use a real, authorized connector and be verified against the provider. See [architecture boundaries](docs/ARCHITECTURE.md).

## Safety principles

- Official and authorized integrations only; no password or session-cookie scraping.
- Explicit approval before publishing, messaging, spending or deleting.
- Consent-aware messaging and opt-out handling for WhatsApp.
- No fabricated analytics, API access, product facts or success claims.
- Idempotent writes, safe retries, auditability and secret redaction.

## Official references

Current platform capabilities change. Check the primary documentation before each connector implementation. A curated starting list is in each skill's `references/` folder and in [platform sources](docs/PLATFORM-SOURCES.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [SECURITY.md](SECURITY.md). Pull requests are welcome; compatibility claims must include reproducible test evidence.

## License

Community skills and repository files are released under the MIT License unless a file says otherwise. Brand names and platform trademarks belong to their respective owners.

---

## العربية

مجموعة مهارات مستقلة وقابلة للنقل، تشمل خمس منصات اجتماعية ونواة مشتركة ومصنعاً عاماً لإنشاء المهارات. كل مجلد قابل للتثبيت منفرداً، ولا يرتبط بمشروع Madanx. هذه الحزمة لا تتضمن مفاتيح API أو صلاحيات نشر؛ يجب ربطها بأدوات رسمية يوفّرها النظام المستضيف.
