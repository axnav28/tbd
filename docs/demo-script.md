# Phase 0 demo script

1. Run `cp .env.example .env && docker compose up --build`.
2. Open `http://localhost:3000` and show the scaffold status.
3. Open `http://localhost:8000/docs` and execute `GET /health`.
4. Explain that no risk figure is displayed until its provenance and calculation engine are implemented in later phases.
5. From the repository root, run `docker compose exec backend python -c 'from pathlib import Path; from app.data.synthetic.generate import write_dataset; write_dataset(Path("/tmp/northstar-demo.json"))'`, then seed it with `docker compose exec backend python -c 'from pathlib import Path; from app.data.seed import seed; seed(Path("/tmp/northstar-demo.json"))'`.
6. Verify the seeded counts with `docker compose exec db psql -U tbd -d tbd -c 'SELECT count(*) FROM assets;'`.
