# CI/CD

## Continuous integration

Pull requests should eventually run dependency installation, formatting/lint checks, pytest, migration validation, and applicable data/dbt tests.

## Promotion

```text
Merge/release -> DEV deployment -> tests -> TEST promotion
-> integration tests -> approval -> PROD deployment
```

GitHub Actions is the automation engine. Flyway remains responsible for database migration execution and history.

## Status

To be implemented after the first pipeline and migration workflows exist.
