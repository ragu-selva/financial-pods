# Deployment Strategy

## Environments
Local -> Preview/PR -> Dev -> Staging -> Production.

## V1 production topology
- DNS/WAF/CDN at edge.
- Static/video assets in object storage delivered through CDN.
- Next.js web and FastAPI API in container services.
- Background workers in separate autoscaled containers.
- PostgreSQL managed database with backups/PITR.
- Redis managed cache.
- Managed secrets/KMS.
- Durable workflow service for long-running media/content jobs.

## AWS reference implementation
ECS Fargate + ALB; RDS PostgreSQL; ElastiCache; S3 + CloudFront; WAF; Secrets Manager/KMS; CloudWatch plus OpenTelemetry export. Terraform manages infrastructure.

## Deployment progression
1. Single-region SaaS.
2. Multi-AZ resilience and tested DR.
3. Enterprise tenant isolation and SSO.
4. Regional/data-residency deployments where commercial demand requires.
5. Dedicated VPC/private deployment option.
6. Kubernetes only if workload scale, customer deployment, or platform requirements justify it.
