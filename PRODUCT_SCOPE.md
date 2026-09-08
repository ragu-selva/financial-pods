# Product Scope

## Product

Financial Pods is an AI-native banking and financial-regulation learning product. The first learning experience is **Corporate Exposure — From Loan to Regulatory Capital** using a fictional institution, FinBank, and a fictional borrower, Alpha Manufacturing.

## V1 outcome

The initial Financial Pods release has two synchronized deliverables:

1. **Product V1 — Golden Lesson:** a learner can follow a corporate loan through exposure classification, risk-weight inputs, deterministic calculation, regulatory-capital interpretation, guided explanation, practice, and mastery evidence.
2. **Growth V1 — Social publishing launch:** approved Golden Lesson knowledge is converted into useful public Basel education that builds trust, validates demand, and leads audiences into the Financial Pods learning experience.

Both deliverables use the same reviewed source objects, deterministic examples, terminology, and correction process. Results and public claims must be reproducible, explainable, jurisdiction-aware, and supported by versioned regulatory sources.

## Target users

- Banking and finance professionals learning regulatory capital
- Risk, credit, finance, audit, and compliance practitioners
- Students and instructors seeking applied, traceable examples

## V1 capabilities, delivered incrementally

- FinBank scenario and Alpha Manufacturing case data
- Deterministic corporate-exposure domain model and calculation engine
- Versioned regulatory knowledge with citations and applicability metadata
- Interactive web lesson, calculator, checks for understanding, and progress state
- AI tutor grounded in approved lesson and regulatory material, never used as the calculation authority
- Governed content pipeline from approved source packet to canonical teaching script and channel derivatives
- At least 10 useful public Basel assets derived from the Golden Lesson for YouTube, YouTube Shorts, LinkedIn, X, and Instagram
- One clear CTA and destination for every published asset, with content IDs and basic attribution from content to product action
- Human approval, publication records, review dates, and correction/retirement paths for public regulatory content
- Quality, safety, observability, and deployment foundations

## Initial release definition

Product V1 and Growth V1 form one coordinated release. Social content may be prepared and published in parallel with the Golden Lesson build only after its claims, calculations, source status, and jurisdiction context have passed the same applicable review gates.

Manual, human-approved channel publishing is sufficient for V1. Automated platform publishing, credential management, scheduling integrations, and large-scale campaign orchestration are not release dependencies.

## Out of scope until explicitly scheduled

- Other exposure classes, trading book, market/operational risk, or enterprise capital aggregation
- Production advice, institution-specific regulatory conclusions, or automated filing
- User-supplied confidential bank data
- Native mobile apps, broad course marketplace, certification, billing, and multilingual delivery
- Automated cross-platform publishing integrations, paid-media operations, and a broad content program beyond the approved Golden Lesson derivatives

## Product principles

1. Correctness and traceability before breadth.
2. Deterministic engines own calculations; AI explains and tutors.
3. One exceptional end-to-end lesson before a large curriculum.
4. Regulatory content is jurisdiction-specific, dated, cited, and reviewable.
5. Release small validated increments; never hide uncertainty.
6. One governed knowledge system produces both paid learning and public education.

## Current boundary

Sprint 01 is historically accepted. Sprint 01 integration and hardening is the current authorized
boundary; see sprints/sprint-01-hardening/SPRINT.md. It fixes exact decimal handling, structural
provenance, and runtime immutability in the existing domain model. Sprint 02 is not active.
Regulatory classification, risk weights, EAD, RWA, capital calculations, lesson/tutor behavior,
authentication, billing, production deployment, and social publishing remain unauthorized.
