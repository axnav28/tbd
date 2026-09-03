"""Minimal startup connectivity check for the PostgreSQL dependency."""

from time import sleep
import logging

import psycopg

logger = logging.getLogger("uvicorn.error")


def wait_for_database(database_url: str, attempts: int = 30, delay_seconds: float = 2.0) -> None:
    """Retry PostgreSQL readiness so backend startup is deterministic in Compose."""
    normalized_url = database_url.replace("postgresql+psycopg://", "postgresql://", 1)
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            with psycopg.connect(normalized_url) as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    cursor.fetchone()
            logger.info("PostgreSQL connection verified with SELECT 1")
            return
        except psycopg.Error as error:
            last_error = error
            sleep(delay_seconds)
    raise RuntimeError(f"PostgreSQL did not become ready after {attempts} attempts") from last_error
