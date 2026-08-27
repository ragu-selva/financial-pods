# Financial Pods finance engine

This package contains the Sprint 01 framework-independent domain model for the synthetic FinBank /
Alpha Manufacturing case.

It owns exact money and percentage primitives, typed identifiers, assumptions, provenance, the
institution/counterparty/product/facility/exposure model, strict versioned serialization, and the
approved fixture loader.

It deliberately contains no regulatory classification, risk weights, EAD, RWA, capital logic,
jurisdiction adapters, web framework, database, Redis, or LLM integration.
