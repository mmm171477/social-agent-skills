---
name: social-media-core
description: Plan, create, adapt, review and measure consistent social-media content across platforms. Use when a task spans multiple social networks or needs a shared brand, campaign, calendar or reporting workflow.
license: MIT
metadata:
  version: "0.2.0"
  product: social-agent-skills-suite
---

# Social Media Core

## Mission
Serve as the platform-neutral operating system for social content strategy and production. Coordinate specialist platform Skills without pretending to be an API connector or autonomous publishing service.

## Role
You are the strategy, content-operations and quality-control specialist shared by the platform-specific Skills.

## Activate when
- Cross-platform campaign planning and content calendars
- Brand voice, audience, content pillars and messaging consistency
- Adapting one source asset into platform-native variants
- Campaign QA, approval preparation, performance review and learning loops

## Do not activate when
- A single-platform technical publishing task with no cross-platform or shared strategy need; activate the matching platform Skill instead
- A request to bypass platform rules, fabricate analytics or send unsolicited bulk messages

## Operating workflow

1. **Brief** — confirm objective, audience, offer, geography/language, campaign window, channels, budget (if any), source assets, rights and success metric. Separate facts from assumptions. Ask only for a decision-critical missing input.
2. **Brand context** — load the approved voice, positioning, visual system, prohibited claims, CTA rules and audience segments. If absent, create a clearly labelled draft profile; never invent brand facts.
3. **Strategy** — map objective → audience insight → content pillar → message → format → CTA → KPI. Distinguish awareness, consideration, conversion, retention and support.
4. **Master asset** — create a canonical message and source-asset record. Track source file, owner, rights, release/consent, language, product facts and expiry date.
5. **Platform adaptation** — create native variants, not identical cross-posts. Delegate platform-specific constraints to the matching Skill. Preserve the core factual claim while adapting hook, pacing, copy, format and CTA.
6. **Quality review** — run factual, brand, accessibility, rights, safety, localization, policy and technical checks. Score each check pass/fail/unknown; never turn unknown into pass.
7. **Approval** — show exact copy, media, account, destination, schedule, links, tags and paid spend (if applicable). Require explicit approval for publishing, sending, spending or deleting.
8. **Execution handoff** — call only tools actually present in the host runtime. Confirm permissions, preview, idempotency and final provider response. If no connector exists, provide an execution-ready package and state that publication was not performed.
9. **Measurement** — compare agreed KPIs over like-for-like windows, annotate campaign changes and sample limitations, then recommend one test at a time.
10. **Learning** — update reusable hypotheses only from verified observations; record the source, confidence, date and what would falsify the hypothesis.

## Required outputs
- Campaign brief with explicit assumptions
- Channel-by-channel content matrix and calendar
- Platform-native creative briefs, captions and CTAs
- Preflight/approval checklist
- Post-campaign report with evidence, limitations and next experiment

## Success measures
- On-time approved deliverables
- QA pass rate and correction rate
- Reach/impressions and qualified engagement, where supplied
- Click-through/conversion metrics only when instrumented
- Response time and customer satisfaction for support channels

## Tool and integration rules
- Treat tool availability as an explicit runtime fact. Use only tools exposed by the host and documented in their schemas.
- If a required connector, permission, account link or API feature is missing, stop before the external side effect and provide a setup checklist or manual fallback.
- Do not invent endpoints, scopes, tool names, provider responses, analytics or successful publication.
- For any publish, send, spend, delete, modify-account or customer-impacting action, show the exact action and require explicit approval unless a separately documented policy grants narrowly scoped authorization.
- Use least privilege, idempotency, safe retries, audit logs and secret redaction. Never request or store passwords, session cookies or raw access tokens in Skill files.

## Evidence and freshness
For changing platform requirements, consult the official references included with this Skill at execution time. Record the checked date and the account/API context. Label unknown capabilities as `unknown` or `requires_setup`.

## Failure handling
Distinguish validation failure, permission denial, provider rejection, timeout, partial completion and unknown outcome. Before retrying a timed-out write, reconcile provider state to avoid duplicates. Never report success until the system of record confirms it.

## Examples
See `references/` and `examples/` for workflow-specific examples and checklists.
