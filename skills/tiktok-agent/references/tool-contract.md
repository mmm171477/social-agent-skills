# Host integration contract

This Skill expects host tools to be injected by the runtime. Document exact tool names, input/output schemas, permissions, rate limits and error semantics in the host adapter. Use `available`, `requires_setup`, `unsupported` or `unknown` for each capability. Never invent API endpoints or scopes. Require authorization and approval before external writes.
