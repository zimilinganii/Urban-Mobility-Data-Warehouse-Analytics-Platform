# Data Modelling

Data modelling is the first focused learning area. Each concept should be learned, applied to the taxi domain, tested against real data, and documented as a decision or hypothesis.

## Pages

- [Conceptual model](Conceptual-Model.md)
- [Logical model](Logical-Model.md)
- [Physical model](Physical-Model.md)
- [Grain, facts and dimensions](Grain-Facts-and-Dimensions.md)
- [Keys and relationships](Keys-and-Relationships.md)
- [Star schema and conformed dimensions](Star-Schema-and-Conformed-Dimensions.md)
- [Slowly changing dimensions](Slowly-Changing-Dimensions.md)
- [Modelling decisions](Modelling-Decisions.md)

## Current hypothesis

One `FactTrip` row represents one completed taxi trip. Pickup and dropoff dates, times, and zones are role-playing references to shared dimensions. Validate this against source profiling and the questions Power BI must answer.
