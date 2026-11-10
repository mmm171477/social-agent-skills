# Portability and installation

The Agent Skills format defines a folder with a required `SKILL.md` using YAML frontmatter (`name`, `description`) and optional references, scripts and assets. It does not standardize every host's discovery path, tool catalog or execution permissions.

## Claude Code

- Project: `.claude/skills/<skill-name>/`
- User: `~/.claude/skills/<skill-name>/`

## Claude.ai

The supported custom-skill upload flow is through Customize → Skills. Upload a ZIP containing the skill directory at the archive root. Availability depends on account features and code execution settings; consult the official guide.

## Other compatible hosts

Check the host's current Skill support, discovery path, frontmatter parser, script runtime and tool injection model. Keep portable content host-neutral and create small host adapters where necessary. Never claim universal compatibility based on folder format alone.

Official format: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
Claude guide: https://support.claude.com/en/articles/12512180-use-skills-in-claude

## Safe installer

From the suite root run `python scripts/install_skills.py --target project --project-root . --skill instagram-agent` or `python scripts/install_skills.py --target user --skill instagram-agent`. Omit `--skill` to install all. Existing skill folders are skipped by default. `--overwrite` first creates a timestamped backup and must be used deliberately.
