# Architecture and capability boundaries

This repository contains Skills, not running agents. Use this separation when integrating them into any product:

1. **Skill layer:** `SKILL.md`, references, examples and evaluation cases. Portable domain expertise.
2. **Agent layer:** runtime identity, routing, tool selection, conversation state, concurrency, scheduling and monitoring. Host-specific.
3. **Connector layer:** official APIs, OAuth, MCP servers, webhooks and data mapping. Requires implementation and credentials.
4. **Execution layer:** queues, idempotency, retries, audit logs, approval records and observability.

Suggested composition: `social-media-core` plans and quality-checks; one specialist Skill owns platform-specific behavior; connector adapters perform real actions. Do not let the shared core claim or duplicate platform permissions.

For a new platform, create a separate specialist Skill using `templates/platform-skill-template/`, add its official source references and tests, then register it in the suite README.
