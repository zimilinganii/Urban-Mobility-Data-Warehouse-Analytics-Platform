# Architecture

## Current end-to-end direction

```text
NYC TLC Parquet ─┐
Taxi-zone CSV ───┼─> Python ingestion and validation
Weather API ────┘             │
                              v
                    Bronze: source-aligned data
                              │
                              v
                    Silver: canonical validated data
                              │
                              v
               SQL Server staging -> warehouse -> marts/views
                              │
                              v
                           Power BI
```

Cross-cutting concerns are Git/GitHub, configuration, logging, audit, testing, migrations, and environment promotion.

## Component responsibilities

| Component | Responsibility |
|---|---|
| Python | Source discovery, download, ingestion utilities, validation, metadata, and loading helpers |
| Parquet | Partitioned Bronze/Silver analytical storage |
| SQL Server | Dimensional warehouse, constraints, indexes, views, and analytical SQL |
| Flyway | Versioned schema migrations and migration history |
| dbt | SQL model organisation, tests, lineage, and documentation where useful |
| Airflow | Scheduling, dependencies, retries, backfills, and workflow state |
| Docker | Reproducible local service environments as the platform matures |
| pytest | Automated Python tests |
| GitHub Actions | Pull-request checks and controlled release automation |
| Power BI | Semantic model, measures, and analysis |

## Design principles

- Build in bounded feature-sized tasks.
- Profile real data before inventing rules.
- Keep Bronze source-aligned and traceable.
- Make processing parameterised, idempotent, and restartable.
- Keep transformations in one clearly owned layer.
- Promote code and schema releases, not DEV data.
- Document decisions as the design evolves.

See [diagrams](diagrams/README.md) for diagram placeholders and [architecture decision records](Architecture-Decision-Records.md) for decisions.
