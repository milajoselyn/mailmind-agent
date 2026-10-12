# Architecture and build plan

## Separation of concerns
1. Provider adapters: Microsoft Graph and Gmail OAuth, delta synchronization, webhook verification.
2. Normalizer: safe HTML-to-text, attachments metadata, stable message/thread identifiers.
3. Intelligence: typed intent/urgency classification, provenance-based retrieval, draft generation.
4. Policy: deterministic server-side permission decisions; draft-only default.
5. Approval: authenticated owner, draft version, expiry, one-time action.
6. Execution: queue, idempotency key, provider reconciliation, audit log.
7. Notification: Teams, Slack, SMS, WhatsApp adapters.
8. Evaluation: synthetic fixtures, security tests, classification metrics.

## Data model (planned)
tenants, users, mailboxes, messages, threads, analysis, drafts, approvals, memories, notifications, workflow_runs, audit_events, model_usage.

## Delivery milestones
- M1: prototype and unit tests (current).
- M2: PostgreSQL migrations, durable queue, auth.
- M3: one provider end-to-end, draft-only.
- M4: approval and sending with integration tests.
- M5: memory and one messaging channel.
- M6: n8n templates, remaining channels, deployment hardening.

## Definition of done for production
A user can connect a mailbox with OAuth, receive a message, inspect a contextual draft, approve a specific immutable draft version, send exactly once, and see the verified provider result and audit record. Every step must have integration and security tests.
