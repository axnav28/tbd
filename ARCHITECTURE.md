# Architecture decisions

## Phase 0 and Phase 1/2 boundary

The scaffold established the service boundaries first. Phase 1 now contains the framework-agnostic graph, FAIR-inspired loss, Monte Carlo, and shared-node de-duplication core. Phase 2 adds choke-point ranking and a PuLP investment LP. Synthetic telemetry, database ORM models, API projections, and recommendation UI remain future work.

## Decisions

- FastAPI is the only backend service and owns the future domain/API boundary.
- PostgreSQL is included from day one, but Phase 0 performs only a connectivity health check.
- Next.js App Router is the frontend shell; its future API client will call the backend through `NEXT_PUBLIC_API_URL`.
- NetworkX, PuLP, and NumPy are now used by the Phase 1/2 domain core; SQLAlchemy and Alembic arrive with persistence work.
- Authentication is represented by a documented stub boundary, not a fake login flow.
- The frontend-design reference requested by the brief was not available in this environment; the visual system will be implemented before frontend product screens in Phase 7.

## Planned data flow

Connectors → normalized persistence → runtime NetworkX graph → FAIR/Monte Carlo quantification → bounded optimizer → API projections → frontend views. Mutations will later pass through the append-only audit boundary.
