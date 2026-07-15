from aiogram.filters import BaseFilter
from aiogram.types import Message
from utils.db.queries import get_user
from utils.loggers import logger

class IsRegistered(BaseFilter):
    async def __call__(self, event: Message) -> bool:
        user = await get_user(event.from_user.id)
        
        if not user:
            logger.info(f"Ro'yxatdan o'tmagan user | id = {event.from_user.id}")
            
        return user is not None