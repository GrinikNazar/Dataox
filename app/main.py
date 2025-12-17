from fastapi import FastAPI
from app.config import settings

from app.db.base import Base
from app.db.session import engine


app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("Database initialized")
    # - запуск scheduler
    print("Application started")


@app.on_event("shutdown")
async def on_shutdown():
    print("Application stopped")
