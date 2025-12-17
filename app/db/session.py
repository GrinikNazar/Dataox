from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from app.config import settings

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.db_user}:"
    f"{settings.db_password}@"
    f"{settings.db_host}:{settings.db_port}/"
    f"{settings.db_name}"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
