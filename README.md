# Urban Mobility Data Warehouse and Analytics Platform

This repository documents and will implement a production-style data platform built around historical NYC Taxi & Limousine Commission trip data.

The documentation is maintained in [`docs/wiki/Home.md`](docs/wiki/Home.md). It is written as a living engineering record: confirmed decisions, working hypotheses, profiling findings, failures, and lessons should be added as the project develops.

## Current status

Project planning and documentation. The first implementation focus is repository setup, source profiling, and dimensional modelling.

## Documentation

- [Wiki home](docs/wiki/Home.md)
- [Project goals and scope](docs/wiki/Project-Goals-and-Scope.md)
- [Architecture](docs/wiki/Architecture.md)
- [Data sources](docs/wiki/Data-Sources.md)
- [Data modelling](docs/wiki/data-modelling/README.md)
- [Implementation roadmap](docs/wiki/Implementation-Roadmap.md)

## Important working principle

The platform will be built in small, explainable increments. Real source data will be profiled before validation rules or final schemas are declared.
