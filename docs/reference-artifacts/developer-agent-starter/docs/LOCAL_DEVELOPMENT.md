# Local Development

## Prerequisites
- Docker/Compose
- Python toolchain
- Node.js + pnpm
- PostgreSQL + pgvector via container
- Redis via container

## Local services
`web`, `api`, `worker`, `postgres`, `redis`, `mock-ai-provider`, `mock-voice-provider`, `object-storage-emulator`.

## Development rule
Every external AI/media provider has a deterministic mock/fake implementation so CI and most local development do not require paid APIs.

## Seed
One command creates the Golden Lesson user, BCBS/U.S./SAMA/CBUAE rule fixtures, FinBank corporate loan examples, and learner mastery fixtures.
