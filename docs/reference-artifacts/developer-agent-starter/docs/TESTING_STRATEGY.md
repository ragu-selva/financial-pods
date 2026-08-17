# Testing Strategy

## Pyramid
1. Domain unit tests.
2. Calculation golden tests.
3. Contract/integration tests.
4. API tests.
5. UI component tests.
6. End-to-end learner journeys.
7. AI evaluations.
8. Load/resilience tests.

## Golden calculation tests
Every finance rule used in a lesson must have reviewed expected results, boundary values, missing-data behavior, and jurisdiction/ruleset version.

## AI evaluations
Maintain a versioned evaluation set for:
- citation correctness;
- refusal to invent rules;
- tool selection;
- numerical fidelity to tool output;
- language quality English/Arabic;
- tutor pedagogy (does not immediately reveal answers in coaching mode);
- misconception detection;
- voice interruption/recovery;
- source/status distinction (current vs proposed rule).

## Release gates
No release when:
- a critical golden calculation fails;
- grounded-answer citation precision falls below agreed threshold;
- severe hallucination/regulatory-status failure is observed;
- P0/P1 security findings are open;
- core E2E learner path is red.
