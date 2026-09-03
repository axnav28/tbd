# TBD — Continuous Cyber Risk Quantification

TBD is a demo-ready architecture for turning security telemetry into financially expressed cyber risk, bounded remediation investment, and regulatory evidence for an Indian financial institution. Phase 0 currently provides the runnable service scaffold; later phases will add the domain engines in the order defined by the product brief.

## Architecture

```text
Browser ──HTTP──> Next.js frontend ──HTTP──> FastAPI backend ──SQL──> PostgreSQL
                                              │
                                              └── domain / graph / quantification / optimization (Phase 1+)
```

## Local setup

Requirements: Docker Desktop with Compose and (for non-container development) Python 3.11+ / Node 20+.

```bash
cp .env.example .env
docker compose up --build
```

Open http://localhost:3000 for the frontend and http://localhost:8000/docs for API documentation. The frontend is the Phase 0 shell; the backend exposes a health endpoint proving service wiring.

Run the backend suite locally with `cd backend && python -m pytest`.

See [the demo walkthrough](docs/demo-script.md) and [limitations](LIMITATIONS.md).
