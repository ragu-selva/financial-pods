# Security and Privacy

## Baseline
- TLS everywhere; encryption at rest.
- Least-privilege IAM.
- Secrets in managed secret store only.
- MFA for admins/SMEs; RBAC for all privileged actions.
- Tenant ID enforced in application/data access patterns.
- Audit trail for content publication, admin actions and entitlement changes.
- WAF/rate limiting and abuse protection.
- Dependency, secret, SAST and container scanning in CI.

## AI/privacy
- Minimize data sent to AI/voice providers.
- Never send enterprise learner/customer data beyond agreed provider boundary.
- Provider data-retention settings documented and configurable where supported.
- User conversation retention policy must be explicit.
- No training on customer content by us without explicit permission.

## Future enterprise readiness
SSO/SAML/OIDC, SCIM, customer-managed retention, regional data residency, dedicated tenant/VPC options and vendor security questionnaires are phase-2 requirements.
