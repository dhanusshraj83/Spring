from fastapi import FastAPI
from app.api import auth, reports, health
from app.db.session import engine, Base
from app.core.config import settings

# Create tables at startup (for quick dev use). In production use alembic for migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PhishGuard Backend")

app.include_router(auth.router)
app.include_router(reports.router)
app.include_router(health.router)
