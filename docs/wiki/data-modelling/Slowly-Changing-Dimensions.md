# Slowly Changing Dimensions

Slowly changing dimensions describe how dimension history is preserved.

- Type 1 overwrites an attribute and keeps only the latest value.
- Type 2 creates a new version with effective dates and current-row metadata.

The project will use Type 1 or Type 2 only where the business meaning and source history justify it. Do not add SCD complexity merely because it is common in warehouse examples.
