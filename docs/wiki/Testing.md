# Testing

| Test type | Purpose |
|---|---|
| Unit | Isolated Python transformation and validation logic |
| Integration | Python, Parquet, and SQL Server interaction |
| Data quality | Required fields, valid keys, accepted values |
| Warehouse | Grain, constraints, relationships, and no orphan keys |
| Migration | Syntax, state, and expected database objects |
| End to end | Source batch through warehouse output |

Testing should grow with each feature. The first useful test is not a complete framework; it is a small repeatable check around the first bounded pipeline task.
