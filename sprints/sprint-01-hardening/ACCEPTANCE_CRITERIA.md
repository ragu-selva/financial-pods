# Sprint 01 Hardening Acceptance Criteria

- [x] Branch starts at refreshed origin/main and retains original Sprint 01 commit ancestry.
- [x] Original Sprint 02 branch/commit are preserved and absent from hardening ancestry/files.
- [x] Money/Percentage validation and serialization are context independent and never round.
- [x] Existing Money addition/subtraction also preserve exact values under modified contexts.
- [x] Excess precision is rejected; approved fixture bytes and serialized values remain unchanged.
- [x] Supported provenance paths and required case-fact coverage are explicit and tested.
- [x] Malformed/nonexistent paths, duplicate paths, and invalid assumption references are rejected.
- [x] Direct constructors reject non-tuple assumptions/provenance with stable typed errors.
- [x] Regression and Hypothesis tests demonstrate fixes, including hostile Decimal contexts.
- [x] Complete task-runner verify passes: format, lint, types, tests, builds, E2E, artifact hashes.
- [x] Docker stack verification passes or its exact environmental blocker is recorded.
- [x] Historical reviews/reference artifacts are unchanged; no future-sprint features are added.
- [ ] PR targets main, distinguishes integration from hardening, and is not automatically merged.
- [ ] STATUS.md records IMPLEMENTED / VERIFIED / PLANNED / BLOCKED, PR, and hosted CI evidence.
