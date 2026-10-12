# Security Policy

MailMind is an early prototype and is **not suitable for production mailbox access**.

## Reporting vulnerabilities

Please avoid public disclosure of exploit details or secrets. Contact the repository maintainer privately through GitHub.

## Non-negotiable production controls

- Draft-only by default. LLM output never authorizes sends.
- OAuth least-privilege scopes, secure credential storage, and token rotation.
- Verified owner identity and version-bound, expiring approval records.
- Tenant isolation, audit logs, retention and deletion controls.
- Provider webhook signature validation, replay prevention, idempotency.
- Prompt-injection resistance: email text and attachments are untrusted data.
- Outbound send reconciliation before retries.
- Never expose full email bodies or secrets in routine logs.
