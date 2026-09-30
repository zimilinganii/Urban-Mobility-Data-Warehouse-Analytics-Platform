# Keys and Relationships

## Key principles

- Source identifiers are business/natural keys and may change or collide across systems.
- Surrogate warehouse keys allow warehouse history and stable relationships.
- Foreign keys should enforce the intended dimensional relationships.
- Unknown or unavailable dimension members need an explicit documented strategy.

## Role-playing dimensions

`DimDate`, `DimTime`, and `DimZone` can be reused in multiple roles. For example, `PickupDateKey` and `DropoffDateKey` both reference `DimDate`, while retaining different semantic meanings in the fact.
