from fastapi import FastAPI
from sqlalchemy import text

from app.api import test_routes, user_routes
from app.core import settings
from app.database import engine

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
)

app.include_router(test_routes.router)
app.include_router(user_routes.router)


@app.get("/", tags=["default"])
def root():
    return {"message": "API running"}


@app.get("/health/db", tags=["Health"])
def check_database():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
