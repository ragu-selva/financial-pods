# Release Process

1. Merge through reviewed pull request.
2. CI builds immutable images/assets and produces SBOM/artifacts.
3. Deploy to staging automatically.
4. Run smoke, integration, AI eval and Golden Lesson E2E suites.
5. Product/SME acceptance for affected content/calculations.
6. Promote the exact build to production.
7. Run post-deploy smoke/canary checks.
8. Monitor errors, latency, AI quality and cost.
9. Roll back through previous immutable deployment if thresholds breach.

Regulatory lesson publication is independent from application release and follows its own versioned content approval workflow.
