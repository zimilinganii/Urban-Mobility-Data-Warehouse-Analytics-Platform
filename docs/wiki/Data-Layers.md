# Data Layers

## Bronze

Bronze preserves source-aligned data with minimal modification. It should retain source fidelity and ingestion metadata such as source file, ingestion timestamp, pipeline run ID, year, and month.

Example layout: `data/bronze/yellow_taxi/year=YYYY/month=MM/`.

## Silver

Silver contains validated, standardised, deduplicated, and schema-harmonised records. It uses a canonical schema and derives technical or analytical fields only when their definitions are documented.

Rejected records should be quarantined with a reason and pipeline metadata, not silently dropped.

## Gold and warehouse

Gold is the business-ready layer. In this project it is primarily the SQL Server dimensional warehouse plus curated analytics views or marts consumed by Power BI.

## Layer decision log

Open questions and implementation findings belong in [schema evolution](Schema-Evolution.md), [data quality](Data-Quality.md), and [architecture decision records](Architecture-Decision-Records.md).
