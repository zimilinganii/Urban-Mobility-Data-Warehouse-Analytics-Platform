# Data Quality

## Quality dimensions

Completeness, validity, consistency, uniqueness, accuracy where verifiable, timeliness, and referential integrity.

## Validation workflow

1. Profile source data.
2. Propose a rule with evidence.
3. Implement the rule in the appropriate layer.
4. Count accepted and rejected rows.
5. Quarantine rejected records with reasons.
6. Review false positives and update the decision record.

Candidate rules such as invalid locations, negative distance, invalid timestamps, missing pickup dates, and duplicates are hypotheses until source profiling supports them.

## Audit entities

`audit.PipelineRun` should capture run ID, pipeline, start/end, status, period, source file, rows read, accepted, rejected, loaded, and errors. `audit.LoadControl` should track successful batches, watermarks, and checkpoints.
