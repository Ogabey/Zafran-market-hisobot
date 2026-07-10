from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine   
)
from config import DB_URL
from utils.loggers import logger
from utils.db.models import Base

engine=create_async_engine(
    url=DB_URL,
    echo=False,
)

AsyncSessionLocal=async_sessionmaker(

    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logger.info("Jadvallar yaratildi:)")

async def close_engine():
    await engine.dispose()
    logger.info("Databazaga ulanish yopildi")