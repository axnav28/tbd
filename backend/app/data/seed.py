"""Load generated demo records into PostgreSQL through SQLAlchemy."""

import json
import os
from pathlib import Path

from sqlalchemy import create_engine, insert

from app.persistence.models import Base, Asset, Control, Vulnerability


def seed(path: Path) -> None:
    """Create the minimal Phase 3 tables and insert one generated dataset."""
    database_url = os.getenv("DATABASE_URL", "postgresql+psycopg://tbd:tbd_local_only@localhost:5432/tbd")
    engine = create_engine(database_url)
    data = json.loads(path.read_text(encoding="utf-8"))
    Base.metadata.create_all(engine)
    with engine.begin() as connection:
        connection.execute(insert(Asset), data["assets"])
        connection.execute(insert(Vulnerability), data["vulnerabilities"])
        connection.execute(insert(Control), data["controls"])
