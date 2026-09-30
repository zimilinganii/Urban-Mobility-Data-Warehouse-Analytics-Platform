# Dimensional Model Diagram

```mermaid
erDiagram
  FACT_TRIP }o--|| DIM_DATE : pickup_date
  FACT_TRIP }o--|| DIM_DATE : dropoff_date
  FACT_TRIP }o--|| DIM_TIME : pickup_time
  FACT_TRIP }o--|| DIM_TIME : dropoff_time
  FACT_TRIP }o--|| DIM_ZONE : pickup_zone
  FACT_TRIP }o--|| DIM_ZONE : dropoff_zone
  FACT_TRIP }o--|| DIM_VENDOR : vendor
  FACT_TRIP }o--|| DIM_PAYMENT_TYPE : payment
  FACT_TRIP }o--|| DIM_RATE_CODE : rate_code
```
