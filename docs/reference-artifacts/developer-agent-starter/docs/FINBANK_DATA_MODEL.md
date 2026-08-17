# FinBank Synthetic Digital Bank

## Purpose
Provide a consistent synthetic bank and customer/product universe across Basel, ALM, FTP, profitability, liquidity, reporting and financial-crime Pods.

## Core dimensions
- legal_entity
- business_unit
- customer / counterparty
- product
- facility
- account
- collateral / guarantee
- currency
- geography
- rating / score
- regulatory classification
- cash-flow schedule
- GL/accounting mapping
- reporting mapping

## V1 corporate loan fixture
Include exposure amount, commitment/drawn status, borrower type, revenue, external/internal rating fields, default flag, collateral, country, currency, maturity, jurisdiction and expected classifications under each approved rule pack.

## Data philosophy
Synthetic data must be realistic enough to support banking workflows but contain no real customer information. Every learning fixture has a seed/version for reproducibility.
