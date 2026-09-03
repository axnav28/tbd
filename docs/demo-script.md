# Phase 0 demo script

1. Run `cp .env.example .env && docker compose up --build`.
2. Confirm `docker compose ps` shows db healthy and backend/frontend running.
3. Open `http://localhost:3000` and show EAL, VaR, confidence tags, and top contributors.
4. Open Attack paths and point out the shared VPN choke point and payment-adjacent asset.
5. Open Investment, move the budget slider, and explain the bounded recommendation.
6. Open Compliance and show the five-framework curated crosswalk.
7. Ask the graph which shared fix has leverage; click the returned citation.
8. Submit a risk-score mutation through the API, then open Audit ledger and show the verified hash chain.
9. Seed the synthetic dataset with the documented commands below and verify the counts.

## Final validation notes

The final clean-state run used `docker compose down -v --remove-orphans && docker compose up -d --build`. It verified three running services, a healthy Postgres container, backend startup log `PostgreSQL connection verified with SELECT 1`, both health endpoints, and frontend HTTP 200. The audit ledger is session-scoped in the current demo build; see `LIMITATIONS.md` for production hardening boundaries.
