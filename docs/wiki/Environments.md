# Environments

## Initial environment model

One SQL Server instance initially hosts three logically separated databases:

```text
UrbanMobilityDW_DEV -> UrbanMobilityDW_TEST -> UrbanMobilityDW_PROD
```

DEV supports rapid development with smaller data. TEST supports integration and data-quality validation. PROD represents the stable full workload.

## Promotion rules

- Promote the same code and schema release through environments.
- Do not manually copy DEV data into PROD.
- Keep credentials, database names, and volumes in environment-specific configuration.
- Production promotion should have an explicit approval gate.
