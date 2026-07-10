from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from utils.db.database import AsyncSessionLocal 
from utils.db.models import User
from utils.loggers import logger


async def add_user(tg_id: int, full_name: str, phone: str):
    async with AsyncSessionLocal() as session:  
        stmt = insert(User).values(
            tg_id=tg_id,
            full_name=full_name,
            phone=phone 
        ).on_conflict_do_nothing(index_elements=["tg_id"]) 
        await session.execute(stmt)
        await session.commit()
        logger.info(f"Foydalanuvchi saqlandi | id={tg_id} | ism={full_name}")


async def get_user(tg_id: int) -> User | None: 
    async with AsyncSessionLocal() as session: 
        result = await session.execute(
            select(User).where(User.tg_id == tg_id) 
        )
        user = result.scalar_one_or_none()
        if user:
            logger.debug(f"Foydalanuvchi topildi | id={tg_id}")
        else:
            logger.debug(f"Foydalanuvchi topilmadi | id={tg_id}")
        return user



async def get_all_users() -> list[User]: 
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(User)) 
        return result.scalars().all() 



async def delete_user(tg_id: int):
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(User).where(User.tg_id == tg_id) 
        )
        user = result.scalar_one_or_none() 
        if user: 
            await session.delete(user)
            await session.commit()
            logger.info(f"Foydalanuvchi o'chirildi | id={tg_id}") 
            







