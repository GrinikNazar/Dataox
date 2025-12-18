from fastapi import FastAPI
from app.config import settings
import asyncio
from sqlalchemy.exc import OperationalError
from contextlib import asynccontextmanager
from app.db.base import Base
from app.db.session import engine
from app.scheduler import start_scheduler, scheduler


async def init_db(retries: int = 10, delay: int = 2):
    for attempt in range(retries):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("Database initialized")
            return
        except OperationalError as e:
            print(f"DB not ready (attempt {attempt + 1}/{retries})")
            await asyncio.sleep(delay)

    raise RuntimeError("Database is not available")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    start_scheduler()
    yield
    scheduler.shutdown()


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan,
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


# @app.on_event("startup")
# async def on_startup():
#     await init_db()
#     start_scheduler()
#     print("Application started")


@app.on_event("shutdown")
async def on_shutdown():
    print("Application stopped")
