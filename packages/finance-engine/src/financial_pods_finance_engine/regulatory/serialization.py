"""Canonical UTF-8 JSON; reject unknown fields and ambiguous JSON at ingress."""

from __future__ import annotations

import json
import re
from dataclasses import fields, is_dataclass
from datetime import date
from decimal import Decimal, InvalidOperation
from hashlib import sha256
from typing import cast

from ..primitives import Currency, Money
from .contracts import (
    FactProvenance,
    RegulatoryCalculationResult,
    RegulatoryContext,
    RegulatoryFact,
    RegulatoryFactSnapshot,
    RequestMetadata,
    money,
)
from .errors import ErrorCode, RegulatoryError, fail

type Json = bool | int | str | list[Json] | dict[str, Json] | None


def object_value(value: object, field: str) -> dict[str, object]:
    if type(value) is not dict or any(type(key) is not str for key in value):
        fail(ErrorCode.INVALID_SCHEMA, field, "Expected an object with text keys")
    return cast(dict[str, object], value)


def array(value: object, field: str) -> list[object]:
    if type(value) is not list:
        fail(ErrorCode.INVALID_SCHEMA, field, "Expected an array")
    return cast(list[object], value)


def string(value: object, field: str) -> str:
    if type(value) is not str or not value.strip():
        fail(ErrorCode.INVALID_TYPE, field, "Expected nonempty text")
    return value


def exact(value: dict[str, object], names: set[str], field: str) -> None:
    missing = names - value.keys()
    if missing:
        fail(ErrorCode.MISSING_REQUIRED_FACT, field, "Missing: " + ", ".join(sorted(missing)))
    if value.keys() - names:
        fail(
            ErrorCode.INVALID_SCHEMA,
            field,
            "Unknown fields: " + ", ".join(sorted(value.keys() - names)),
        )


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in items:
        if key in result:
            fail(ErrorCode.INVALID_SCHEMA, key, "Duplicate JSON key")
        result[key] = value
    return result


def _reject_float(value: str) -> object:
    fail(ErrorCode.INVALID_TYPE, "json", "Binary float / non-finite JSON number is forbidden")


def parse_json(raw: bytes | str) -> dict[str, object]:
    try:
        value: object = json.loads(
            raw, object_pairs_hook=_pairs, parse_float=_reject_float, parse_constant=_reject_float
        )
    except (ValueError, UnicodeError) as exc:
        if isinstance(exc, RegulatoryError):
            raise
        fail(ErrorCode.INVALID_SCHEMA, "json", str(exc))
    return object_value(value, "json")


def encode(value: object) -> Json:
    if value is None or type(value) in (bool, int, str):
        return cast(Json, value)
    if type(value) is Decimal:
        if not value.is_finite():
            fail(ErrorCode.INVALID_TYPE, "decimal", "Non-finite value")
        return format(value, "f")
    if type(value) is Currency:
        return value.code
    if type(value) is date:
        return value.isoformat()
    if type(value) is Money:
        return {"amount": value.to_decimal_string(), "currency": value.currency.code}
    if type(value) in (tuple, list):
        return [encode(item) for item in cast(list[object] | tuple[object, ...], value)]
    if isinstance(value, dict):
        return {string(key, "key"): encode(item) for key, item in sorted(value.items())}
    if is_dataclass(value) and not isinstance(value, type):
        return {field.name: encode(getattr(value, field.name)) for field in fields(value)}
    fail(ErrorCode.INVALID_TYPE, "serialization", "Unsupported or mutable value")


def canonical_json(value: object) -> str:
    return json.dumps(
        encode(value), sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    )


def snapshot_hash(snapshot: RegulatoryFactSnapshot) -> str:
    # Display names, caller IDs and calculation IDs are metadata, not rule predicates.
    return sha256(
        canonical_json(
            {
                "schema_version": snapshot.schema_version,
                "fixture_version": snapshot.fixture_version,
                "context": snapshot.context,
                "facts": snapshot.facts,
            }
        ).encode("utf-8")
    ).hexdigest()


def result_to_dict(
    result: RegulatoryCalculationResult, *, include_metadata: bool = False
) -> dict[str, Json]:
    payload = cast(dict[str, Json], encode(result))
    identity = cast(dict[str, Json], payload.pop("ruleset"))
    for key in ("ruleset_id", "ruleset_version", "manifest_hash", "catalog_snapshot_id"):
        payload[key] = identity[key]
    if not include_metadata:
        payload.pop("request_metadata")
    return payload


def result_to_json(result: RegulatoryCalculationResult, *, include_metadata: bool = False) -> str:
    return canonical_json(result_to_dict(result, include_metadata=include_metadata))


def error_to_json(error: RegulatoryError) -> str:
    return canonical_json(
        {
            "code": error.code.value,
            "field_path": error.field_path,
            "message": error.message,
            "rule_refs": error.rule_refs,
            "validation_trace": error.validation_trace,
        }
    )


def decimal_text(value: object, field: str) -> Decimal:
    token = string(value, field)
    if not re.fullmatch(r"-?(0|[1-9][0-9]*)(\.[0-9]+)?", token):
        fail(ErrorCode.INVALID_TYPE, field, "Expected plain exact decimal text")
    try:
        return Decimal(token)
    except InvalidOperation:
        fail(ErrorCode.INVALID_TYPE, field, "Invalid Decimal")


def snapshot_from_dict(value: object) -> RegulatoryFactSnapshot:
    data = object_value(value, "snapshot")
    exact(data, {"schema_version", "fixture_version", "context", "facts", "metadata"}, "snapshot")
    if data["schema_version"] != "regulatory-facts.v1":
        fail(ErrorCode.INVALID_SCHEMA, "schema_version", "Unsupported fact schema")
    context = object_value(data["context"], "context")
    exact(
        context, {"jurisdiction", "regulator", "regime", "as_of_date", "ruleset_version"}, "context"
    )
    try:
        day = date.fromisoformat(string(context["as_of_date"], "as_of_date"))
        if day.isoformat() != context["as_of_date"]:
            raise ValueError("Non-canonical ISO date")
    except ValueError:
        fail(ErrorCode.INVALID_TYPE, "as_of_date", "Expected YYYY-MM-DD")
    ctx = RegulatoryContext(
        jurisdiction=string(context["jurisdiction"], "jurisdiction"),
        regulator=string(context["regulator"], "regulator"),
        regime=string(context["regime"], "regime"),
        ruleset_version=string(context["ruleset_version"], "ruleset_version"),
        as_of_date=day,
    )
    metadata = object_value(data["metadata"], "metadata")
    exact(
        metadata,
        {"case_id", "counterparty_id", "institution_id", "borrower_name", "calculation_id"},
        "metadata",
    )
    identifier = metadata["calculation_id"]
    if identifier is not None:
        identifier = string(identifier, "calculation_id")
    request = RequestMetadata(
        case_id=string(metadata["case_id"], "case_id"),
        counterparty_id=string(metadata["counterparty_id"], "counterparty_id"),
        institution_id=string(metadata["institution_id"], "institution_id"),
        borrower_name=string(metadata["borrower_name"], "borrower_name"),
        calculation_id=identifier,
    )
    facts: list[RegulatoryFact] = []
    for raw in array(data["facts"], "facts"):
        item = object_value(raw, "fact")
        exact(item, {"path", "value", "provenance"}, "fact")
        path = string(item["path"], "path")
        fact_value = item["value"]
        if type(fact_value) is dict:
            cash = object_value(fact_value, path)
            exact(cash, {"amount", "currency"}, path)
            if cash["currency"] != "USD":
                fail(ErrorCode.CURRENCY_MISMATCH, path, "Only USD is supported")
            fact_value = money(decimal_text(cash["amount"], path), Currency("USD"))
        if type(fact_value) not in (str, bool, int, Money):
            fail(
                ErrorCode.INVALID_TYPE,
                path,
                "Expected typed fact; unknown is explicit UNKNOWN text",
            )
        provenance = object_value(item["provenance"], path + ".provenance")
        exact(
            provenance,
            {"source_ref", "source_version", "assumption_id", "review_status"},
            "provenance",
        )
        if provenance["review_status"] != "APPROVED_FOR_INTERNAL_PROTOTYPE":
            fail(ErrorCode.INVALID_PROVENANCE, path, "Fact must have reviewed provenance")
        facts.append(
            RegulatoryFact(
                path=path,
                value=cast(str | bool | int | Money, fact_value),
                provenance=FactProvenance(
                    source_ref=string(provenance["source_ref"], "source_ref"),
                    source_version=string(provenance["source_version"], "source_version"),
                    assumption_id=string(provenance["assumption_id"], "assumption_id"),
                    review_status="APPROVED_FOR_INTERNAL_PROTOTYPE",
                ),
            )
        )
    return RegulatoryFactSnapshot(
        context=ctx,
        facts=tuple(facts),
        metadata=request,
        fixture_version=string(data["fixture_version"], "fixture_version"),
    )
