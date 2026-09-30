# SQL Server Warehouse

## Initial warehouse schemas

The working direction is to separate staging, dimensional warehouse, analytics views, and audit objects. Exact schema names and physical choices remain to be validated during implementation.

## Initial model hypothesis

- `FactTrip`: one row per completed taxi trip.
- `DimDate`: reusable for pickup and dropoff roles.
- `DimTime`: reusable for pickup and dropoff roles.
- `DimZone`: reusable for pickup and dropoff roles.
- `DimVendor`, `DimPaymentType`, and `DimRateCode`.
- Optional later `FactWeatherHourly` with conformed date/time dimensions.

See the [data modelling pages](data-modelling/README.md) for the design reasoning.

## Physical design topics

Constraints, surrogate keys, indexes, statistics, execution plans, partitioning, and possible columnstore experiments will be considered only after correctness and representative performance are established.
