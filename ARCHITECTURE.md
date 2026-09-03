# Architecture decisions

## Phase 0 through Phase 3 boundary

The scaffold established the service boundaries first. Phase 1 contains the framework-agnostic graph, FAIR-inspired loss, Monte Carlo, and shared-node de-duplication core. Phase 2 adds choke-point ranking and a PuLP investment LP. Phase 3 adds normalized ingestion records, control integrity checks, a regenerable synthetic dataset, and SQLAlchemy seed models. API projections and recommendation UI remain future work.

## Decisions

- FastAPI is the only backend service and owns the future domain/API boundary.
- PostgreSQL is included from day one. Compose health-checks Postgres, and the backend independently retries a real `SELECT 1` connection before serving.
- Next.js App Router is the frontend shell; its future API client will call the backend through `NEXT_PUBLIC_API_URL`.
- NetworkX, PuLP, NumPy, SQLAlchemy, and Alembic are used by the Phase 1–3 core.
- Authentication is represented by a documented stub boundary, not a fake login flow.
- The frontend-design reference requested by the brief was not available in this environment; the visual system will be implemented before frontend product screens in Phase 7.

## Planned data flow

Connectors → normalized persistence → runtime NetworkX graph → FAIR/Monte Carlo quantification → bounded optimizer → API projections → frontend views. Mutations will later pass through the append-only audit boundary.
