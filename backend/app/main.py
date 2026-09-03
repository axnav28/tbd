"""FastAPI entrypoint for the TBD service scaffold."""

from fastapi import FastAPI

app = FastAPI(title="TBD Cyber Risk Platform", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Return a dependency-free liveness response for local orchestration."""
    return {"status": "ok", "service": "backend", "phase": "0-scaffold"}


@app.get("/api/v1/health", tags=["system"])
def api_health() -> dict[str, str]:
    """Versioned alias consumed by the frontend shell."""
    return health()
