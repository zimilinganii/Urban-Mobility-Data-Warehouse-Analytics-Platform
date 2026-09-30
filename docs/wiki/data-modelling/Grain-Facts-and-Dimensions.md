# Grain Facts and Dimensions

## Grain

Grain states exactly what one row represents. The initial hypothesis is: one `FactTrip` row equals one completed taxi trip. Every measure and key must be consistent with that statement.

## Facts

Facts contain events and measurable values such as distance, duration, fare, tip, tolls, total amount, and passenger count.

## Dimensions

Dimensions provide descriptive context such as date, time, zone, vendor, payment type, and rate code.

## Additivity questions

Trip count and many monetary totals may be additive across suitable dimensions. Averages, rates, and duration statistics must be calculated carefully rather than summed.
