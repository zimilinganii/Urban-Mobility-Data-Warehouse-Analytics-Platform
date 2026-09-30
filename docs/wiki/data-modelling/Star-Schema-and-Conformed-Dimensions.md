# Star Schema and Conformed Dimensions

A star schema places a central fact table around descriptive dimensions so analytical queries remain understandable and efficient.

The initial design favours a star over a snowflake unless real requirements justify additional normalisation. `DimDate` and `DimZone` should be conformed if future facts, such as weather, use the same definitions and keys.

The choice is driven by analytical usability and correctness, not by demonstrating terminology.
