# Batch and Backfill Strategy

## Planned modes

- Develop with approximately one year.
- Expand to multiple years to expose schema and performance issues.
- Run a controlled historical backfill from the selected start year.
- Process new months incrementally after the backfill.

## Required properties

- Parameters for year, month, or a year range.
- Independent partition status so failed periods can be rerun.
- Idempotent loads: rerunning a successful period must not create duplicates.
- Pipeline-run and load-control records.
- Clear distinction between source download, transformation, and warehouse load failures.

## Example interface

```text
python ingest.py --year 2009
python ingest.py --year 2024 --month 6
python ingest.py --start-year 2009 --end-year 2026
```

These commands are design examples until the implementation is created.
