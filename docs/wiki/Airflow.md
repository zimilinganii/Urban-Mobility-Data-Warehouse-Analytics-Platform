# Airflow

Airflow will orchestrate work after the underlying Python and SQL pipeline works manually.

The planned flow is:

```text
Discover batch -> Download source -> Bronze -> Validate schema
-> Silver -> Data quality -> Load SQL Server -> dbt/models
-> Warehouse tests -> Update audit
```

The learning focus is DAGs, task dependencies, retries, schedules, catchup/backfill, connections, and limited XCom use. Airflow should coordinate work, not replace the functions that perform it.
