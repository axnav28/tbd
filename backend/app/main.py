"""FastAPI entrypoint for the TBD service scaffold."""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.persistence.db import wait_for_database
from app.api.routes import audit, compliance, graph, nl_query, optimizer, risk


@asynccontextmanager
async def lifespan(_: FastAPI):
    """Validate the database before serving requests when Compose enables it."""
    if os.getenv("CHECK_DATABASE_ON_STARTUP", "false").lower() == "true":
        wait_for_database(os.getenv("DATABASE_URL", ""))
    yield


app = FastAPI(title="TBD Cyber Risk Platform", version="0.1.0", lifespan=lifespan)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"], allow_headers=["*"])
app.include_router(risk.router, prefix="/api/v1")
app.include_router(graph.router, prefix="/api/v1")
app.include_router(optimizer.router, prefix="/api/v1")
app.include_router(compliance.router, prefix="/api/v1")
app.include_router(nl_query.router, prefix="/api/v1")
app.include_router(audit.router, prefix="/api/v1")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    """Return a dependency-free liveness response for local orchestration."""
    return {"status": "ok", "service": "backend", "phase": "0-scaffold"}


@app.get("/api/v1/health", tags=["system"])
def api_health() -> dict[str, str]:
    """Versioned alias consumed by the frontend shell."""
    return health()
