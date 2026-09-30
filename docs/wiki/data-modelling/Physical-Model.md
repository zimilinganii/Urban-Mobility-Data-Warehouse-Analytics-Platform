# Physical Model

The physical model maps the logical design to SQL Server tables, data types, constraints, indexes, schemas, and migration files.

## Candidate tables

- `dw.FactTrip`
- `dw.DimDate`
- `dw.DimTime`
- `dw.DimZone`
- `dw.DimVendor`
- `dw.DimPaymentType`
- `dw.DimRateCode`
- `audit.PipelineRun`
- `audit.LoadControl`
- `audit.RejectedRecord`

This is a starting point, not a final DDL specification. Physical choices must follow source profiling, workload testing, and the agreed grain.
