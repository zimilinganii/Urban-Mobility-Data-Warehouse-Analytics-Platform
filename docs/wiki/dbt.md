# dbt

dbt is a planned SQL transformation and documentation layer, not a requirement to duplicate logic already owned by Python or T-SQL.

Possible flow:

```text
SQL Server staging -> dbt staging -> intermediate -> dimensions/facts/marts
```

The SQL Server adapter and the boundary between dbt, loading code, and migrations must be verified before the design is locked.
