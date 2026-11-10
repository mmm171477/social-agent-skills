# Host-tool contract

This Skill is not an integration. The host must inject real tools and document their schemas. Map capabilities explicitly: `available`, `requires_setup`, `unsupported`, or `unknown`. Never guess tool names or API endpoints.

Minimum operations when supported: read account/profile; read media requirements; upload media; create draft; preview; publish/schedule; read publication status; read insights; record audit event.

Every write operation must accept an account/workspace identity, preview payload, approval reference, idempotency key and timeout/retry policy. Never log credentials or raw access tokens. A successful tool invocation is not proof of publication; verify provider state.