"""FastAPI entrypoint for the TBD service scaffold."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.persistence.db import wait_for_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Validate the database before serving requests when Compose enables it."""
    if os.getenv("CHECK_DATABASE_ON_STARTUP", "false").lower() == "true":
        wait_for_database(os.getenv("DATABASE_URL", ""))
    yield


app = FastAPI(title="TBD Cyber Risk Platform", version="0.1.0", lifespan=lifespan)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Return a dependency-free liveness response for local orchestration."""
    return {"status": "ok", "service": "backend", "phase": "0-scaffold"}


@app.get("/api/v1/health", tags=["system"])
def api_health() -> dict[str, str]:
    """Versioned alias consumed by the frontend shell."""
    return health()
