# Schema Evolution

Historical source files may contain renamed, added, removed, or type-changed columns. These changes must be observed through profiling rather than assumed.

## Planned approach

```text
Historical raw schemas -> version/source mapping -> canonical Silver schema
```

For each observed change, record the source period, original field, canonical field, conversion rule, missing-value behaviour, and whether the change affects comparability.

## Comparability warning

Trend analysis across years should disclose changes in source coverage, definitions, or available fields. A technically consistent canonical schema does not automatically make every historical measure comparable.
