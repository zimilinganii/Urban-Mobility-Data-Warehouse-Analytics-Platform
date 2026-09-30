# Database Migrations

Database changes will be version controlled and applied by Flyway rather than copied manually between SSMS windows.

Example sequence:

```text
V001__create_schemas.sql
V002__create_audit_tables.sql
V003__create_dimensions.sql
V004__create_fact_trip.sql
V005__add_indexes.sql
```

The same migration set should be validated in DEV, tested in TEST, and promoted to PROD. Flyway history in each database records what has been applied.
