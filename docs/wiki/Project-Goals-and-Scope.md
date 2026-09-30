# Project Goals and Scope

## Aim

Build a small production-style data platform that ingests real NYC taxi data, transforms it through governed data layers, loads a SQL Server dimensional warehouse, and exposes trustworthy analytical data to Power BI.

## In scope

- Parameterised historical batch processing and monthly incremental processing.
- Bronze raw/source-aligned storage and Silver validated, canonical storage.
- Gold represented by a SQL Server dimensional warehouse and analytics views.
- Source profiling, schema evolution, validation, quarantine, audit, and restartability.
- Fact and dimension modelling, including grain, keys, role-playing dimensions, and slowly changing dimensions where justified.
- DEV, TEST, and PROD configuration and controlled promotion.
- Version-controlled database migrations.
- Automated tests, orchestration, CI/CD, and operational documentation.
- Power BI consumption of the curated warehouse.

## Out of scope for the initial core

Kafka, Kubernetes, Terraform, cloud deployment, Databricks, Snowflake, Flink, Data Mesh, Data Vault, and Spark unless a real scale or engineering need emerges. These technologies are not goals by themselves.

## Portfolio outcome

The finished project should show that its owner can design, build, test, operate, explain, and improve an end-to-end data platform.

## Success criteria

1. A selected source period can be processed repeatably from source to warehouse.
2. Historical partitions can be backfilled and rerun without duplicate loads.
3. Data-quality decisions are based on observed source data.
4. Warehouse tables have documented grain, keys, relationships, and measures.
5. Schema changes are promoted through version-controlled migrations.
6. A Power BI model can answer the agreed analytical questions.
7. The repository explains important decisions and known limitations.

## Current assumptions

The initial FactTrip hypothesis is one row per completed taxi trip. It is not final until source profiling and analytical requirements confirm it.
