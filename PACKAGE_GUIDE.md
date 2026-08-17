# Package Guide

Codex should work from the live folder `D:\Financial Ai studio\financial-pods`, not from a ZIP.

## Package purposes

### `Financial-Pods-Codex-Package.zip`

Historical intake shell created before the finalized artifacts were available. It contains mostly empty directories plus early README/intake/manifest files. Retained for provenance only; do not use it to start development.

### `Financial_Pods_Developer_Agent_Starter_Pack.zip`

Source package containing architecture notes, policies, prompts, agent skills, templates, and development guidance. The unchanged ZIP and an extracted read-only copy are retained under reference artifacts. Its root `AGENTS.md`, `ARCHITECTURE.md`, and `ROADMAP.md` do not override the live project root files.

### `financial-pods-codex-bootstrap.zip`

Snapshot of the bootstrap/handoff execution files and empty directory structure. It was useful for transport and recovery. The live project folder now supersedes it; do not extract it over the repository.

## Rule

ZIPs are archives, not working directories. The live repository is authoritative. Never overwrite the live root with an archived package.
