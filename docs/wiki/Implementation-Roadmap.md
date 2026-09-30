# Implementation Roadmap

1. Confirm local tools and focused learning priorities.
2. Set up repository structure, configuration, and pull-request workflow.
3. Profile real source files and compare selected years.
4. Build parameterised Python ingestion.
5. Add partitioned Bronze storage and metadata.
6. Investigate historical schema evolution.
7. Build canonical Silver transformations.
8. Add data-quality rules, quarantine, and audit.
9. Design conceptual, logical, and physical dimensional models.
10. Build the SQL Server warehouse.
11. Add historical backfill and incremental state.
12. Add Flyway migrations and environment promotion.
13. Introduce dbt where it adds clear value.
14. Introduce Airflow orchestration.
15. Expand automated testing.
16. Dockerise services incrementally.
17. Add GitHub Actions CI/CD.
18. Build the Power BI semantic model and reports.
19. Measure and improve performance.
20. Polish documentation, diagrams, release notes, and portfolio narrative.

The first implementation milestone is intentionally small: repository setup, source profiling, and the first modelling artefacts.
