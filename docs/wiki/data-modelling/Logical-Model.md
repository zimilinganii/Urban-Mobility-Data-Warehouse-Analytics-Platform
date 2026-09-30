# Logical Model

The logical model defines entities, attributes, relationships, and grain independently of physical SQL details.

## Candidate entities

`Trip` relates to pickup/dropoff `Date`, `Time`, and `Zone`, plus `Vendor`, `PaymentType`, and `RateCode`. A future `WeatherObservation` may relate through conformed date/time keys.

The model should document cardinality and optionality before tables are built. For example, a trip should have one pickup timestamp and one dropoff timestamp, while a weather observation may be optional.
