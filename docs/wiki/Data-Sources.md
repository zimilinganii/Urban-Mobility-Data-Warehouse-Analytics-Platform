# Data Sources

| Source | Format | Purpose | Initial contents |
|---|---|---|---|
| NYC TLC Taxi Trip Record Data | Parquet | Primary trip/event data | Times, locations, passengers, distance, fares, tips, tolls, payment, vendor |
| NYC Taxi Zone Lookup | CSV | Reference data | Location ID, borough, zone, service zone |
| Open-Meteo historical weather | JSON/API | Optional enrichment | Temperature, rain/snow, humidity, wind, conditions |

## Source investigation rules

- Start with a small representative period.
- Compare multiple historical years before finalising the canonical schema.
- Record coverage, file naming, column names, data types, nulls, duplicates, and suspicious values.
- Do not artificially dirty the source data.
- Do not assume historical schemas are identical.

## Open questions

- Which taxi product types and years are included in the first release?
- Is weather enrichment valuable enough to justify a second fact table?
- What source licensing and download documentation should be retained?
