# Git Workflow and Pull Requests

## Branch model

`main` is the stable release branch. `develop` is the integration branch. Work is completed in feature branches such as `feature/data-ingestion` and `feature/star-schema`.

## Change flow

```text
Issue/task -> feature branch -> commits -> pull request -> CI checks
-> review -> merge to develop -> release pull request -> main
```

Pull requests are a learning priority: they provide a place to explain the change, inspect the diff, run checks, resolve feedback, and keep the project history understandable.
