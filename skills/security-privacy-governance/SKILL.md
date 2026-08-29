---
name: security-privacy-governance
description: Evidence-first security, privacy, secrets and data-governance engineering for FastMCP systems.
---

# Security / Privacy / Data Governance

## Mission
Treat every boundary from MCP input through application, LLM, tools, database, queues and telemetry as a security and data-governance boundary.

## Mandatory research
Identify exact versions. Read current official MCP security/specification material and exact-version FastMCP, Pydantic/PydanticAI, SQLAlchemy and provider documentation relevant to the data flow. Review OWASP guidance and applicable repository policies as supplementary evidence. Record an evidence ledger and re-check version-sensitive claims before completion.

## Data classification
Classify every input, output and persisted field as public, internal, confidential, secret, personal data or regulated/special-category data as applicable. Define purpose, owner, lawful/organizational basis where relevant, retention, deletion and allowed destinations.

## Trust boundaries
Explicitly model: MCP client → server; authentication → authorization; MCP → application; application → domain; application → LLM/provider; application → database; workers/queues; external HTTP; filesystem; telemetry. Untrusted model-generated arguments are still untrusted input. Never use prompt text, tool descriptions or annotations as an authorization mechanism.

## Secrets
Secrets must enter through a dedicated secret/configuration boundary, never source code, MCP arguments, resource URIs, prompts, logs, traces, metrics, database records or model context unless explicitly required and controlled. Prefer short-lived credentials and least privilege. Define rotation, revocation and failure behavior. Never echo credentials in errors.

## PII / sensitive data
Apply data minimization and purpose limitation. Do not send data to an LLM/provider merely because it is available to the application. Define an explicit allowlist of fields permitted to leave each trust boundary. Consider prompt injection and indirect data exfiltration whenever tools expose sensitive records or external content.

## Authorization
Authentication identifies the caller; authorization determines allowed actions and data. Enforce authorization in trusted server-side code close to the protected resource. Check tenant/user/resource scope for every access path. Do not trust client-supplied tenant IDs, user IDs or role claims without verification.

## Multi-tenancy
Every tenant-scoped query and mutation must have a server-derived tenant context. Prefer defense-in-depth with database constraints/RLS where appropriate. Test cross-tenant read/write attempts. Never rely solely on UI/tool descriptions to enforce tenant boundaries.

## LLM boundary
Treat model input/output as untrusted. Define prompt/data classification, provider retention assumptions, allowed tools, tool-result filtering, injection defenses and output validation. Never let a model choose credentials, authorization policy or unrestricted query scope. Structured outputs still require semantic validation.

## Database
Use parameterized queries/SQLAlchemy expressions. Enforce security invariants with database constraints where practical. Protect against insecure direct object references, over-broad selects, unsafe dynamic ordering/filtering and cross-tenant access. Secrets should not be persisted unless explicitly justified and protected.

## Telemetry
Follow the observability skill: redact tokens, credentials, cookies, authorization headers, prompts, sensitive payloads and raw personal data by default. Define retention/access/export policy. Test redaction negatively.

## Input/output security
Validate types, lengths, bounds, URLs, paths, identifiers and content types at boundaries. Prevent SSRF, path traversal, unsafe deserialization, command injection, SQL injection and resource exhaustion according to the actual tool capabilities. Apply allowlists for network destinations and filesystem roots when tools cross those boundaries.

## Auditability
For security-sensitive operations record actor, target, action, outcome and correlation context without recording secrets or unnecessary personal data. Separate audit records from debug logs and define retention/access.

## Failure behavior
Fail closed for authorization. Avoid leaking existence of protected resources through error differences where that matters. Ensure security checks cannot be bypassed by retries, alternate tools/resources, background workers or administrative paths.

## Testing
Threat-model each exposed capability. Test unauthorized, cross-tenant, malformed, injection, SSRF/path traversal, excessive-input and secret-leak cases. Test model/tool prompt-injection scenarios when LLMs are involved. Test authorization on direct use-case calls, not only MCP transport. Include negative telemetry tests.

## Deliverables
Data-flow/trust-boundary diagram; data inventory/classification; threat model; authorization matrix; secret lifecycle; provider data-flow policy; tenant isolation model; retention/deletion policy; audit schema; security test matrix; evidence ledger; residual risks; verification report.