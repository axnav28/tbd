"""Small normalized ORM schema for the Phase 3 synthetic seed."""

from sqlalchemy import Boolean, Float, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Asset(Base):
    __tablename__ = "assets"
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    type: Mapped[str] = mapped_column(String(64))
    synthetic: Mapped[bool] = mapped_column(Boolean, default=True)


class Vulnerability(Base):
    __tablename__ = "vulnerabilities"
    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    asset_id: Mapped[str] = mapped_column(String(64))
    cvss: Mapped[float] = mapped_column(Float)
    epss: Mapped[float] = mapped_column(Float)
    cisa_kev: Mapped[bool] = mapped_column(Boolean)
    source: Mapped[str] = mapped_column(String(100))


class Control(Base):
    __tablename__ = "controls"
    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    confidence: Mapped[str] = mapped_column(String(32))
    verified: Mapped[bool] = mapped_column(Boolean)
