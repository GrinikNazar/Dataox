from fastapi import FastAPI
from app.config import settings

app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.on_event("startup")
async def on_startup():
    # - ініціалізація БД
    # - запуск scheduler
    print("Application started")


@app.on_event("shutdown")
async def on_shutdown():
    print("Application stopped")
