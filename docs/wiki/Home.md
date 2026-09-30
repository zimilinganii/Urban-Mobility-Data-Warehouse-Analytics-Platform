# Urban Mobility Data Platform Wiki

## Purpose

This wiki is the working guide and engineering record for the Urban Mobility Data Engineering and Dimensional Modelling Platform.

The project aims to demonstrate an end-to-end data platform, not only a dashboard: ingestion, historical processing, data quality, dimensional modelling, database engineering, testing, environment promotion, orchestration, CI/CD, and analytics.

## Current status

Planning and repository documentation. The immediate work is to investigate the real source data, establish the development workflow, and learn dimensional modelling by applying each concept to the taxi domain.

## At a glance

| Area | Current direction |
|---|---|
| Core data | NYC TLC taxi trip records |
| Optional enrichment | Taxi-zone reference data and historical weather |
| Storage layers | Bronze, Silver, Gold/warehouse |
| Warehouse | Microsoft SQL Server |
| Development | GitHub feature branches, pull requests, CI/CD |
| Environments | DEV, TEST, PROD |
| Planned tools | Python, Parquet, Flyway, dbt, Airflow, Docker, pytest, GitHub Actions, Power BI |
| Model status | Initial hypothesis; validate after profiling |

## Navigate

- [Project goals and scope](Project-Goals-and-Scope.md)
- [Architecture](Architecture.md)
- [Data sources](Data-Sources.md)
- [Data layers](Data-Layers.md)
- [Batch and backfill strategy](Batch-and-Backfill-Strategy.md)
- [Schema evolution](Schema-Evolution.md)
- [Data quality](Data-Quality.md)
- [Data modelling](data-modelling/README.md)
- [SQL Server warehouse](SQL-Server-Warehouse.md)
- [Environments](Environments.md)
- [Database migrations](Database-Migrations.md)
- [Git workflow and pull requests](Git-Workflow-and-Pull-Requests.md)
- [Testing](Testing.md)
- [CI/CD](CI-CD.md)
- [Airflow](Airflow.md)
- [dbt](dbt.md)
- [Docker](Docker.md)
- [Power BI](Power-BI.md)
- [Diagrams](diagrams/README.md)
- [Architecture decision records](Architecture-Decision-Records.md)
- [Issues, failures and lessons](Issues-Failures-and-Lessons.md)
- [Implementation roadmap](Implementation-Roadmap.md)

## Documentation status labels

- **Confirmed**: supported by implementation or observed evidence.
- **Hypothesis**: a proposed design to validate.
- **To be decided**: intentionally open.
- **Superseded**: retained for history but no longer current.
