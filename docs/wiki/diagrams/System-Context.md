# System Context Diagram

```mermaid
flowchart LR
  TLC[NYC TLC trip data] --> Platform[Urban Mobility Data Platform]
  Zones[Taxi zone CSV] --> Platform
  Weather[Optional weather API] --> Platform
  Platform --> SQL[(SQL Server warehouse)]
  SQL --> BI[Power BI]
  Git[GitHub and CI/CD] -. governs .-> Platform
```
