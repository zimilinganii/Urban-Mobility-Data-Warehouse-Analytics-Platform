# Architecture Decision Records

Use this page as an index. Create one record for each significant decision and link it here.

## Record template

```markdown
# ADR NNN: Decision title

Status: Proposed | Accepted | Superseded
Date: YYYY-MM-DD

## Context
What problem or choice exists?

## Decision
What was chosen?

## Consequences
What becomes easier, harder, or constrained?

## Evidence and links
Profiling results, tests, issues, or source references.
```

## Initial records to create

- Warehouse platform: SQL Server.
- Initial environment model: three logical databases on one instance.
- Initial trip grain hypothesis.
- Bronze/Silver/Gold layer boundaries.
- Migration tool choice and promotion process.
