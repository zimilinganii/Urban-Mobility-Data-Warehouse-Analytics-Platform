# Deployment and Environments Diagram

```mermaid
flowchart LR
  DEV[DEV database] -->|validated release| TEST[TEST database]
  TEST -->|approved release| PROD[PROD database]
  Code[GitHub repository] --> Actions[GitHub Actions]
  Actions --> DEV
  Actions --> TEST
  Actions --> PROD
```
