# Modelling Decisions

This page records modelling decisions before they become physical schema.

## Open decisions

- Confirm the exact trip grain after profiling.
- Decide which source identifiers are degenerate dimensions or ordinary attributes.
- Decide whether vendor and rate-code history requires SCD treatment.
- Confirm whether weather becomes a separate fact or an enrichment attribute.
- Confirm required date/time grain and time-zone handling.

Use the [ADR template](../Architecture-Decision-Records.md) for decisions with wider architectural consequences.
