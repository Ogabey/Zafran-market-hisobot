from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from config import ADMIN_ID
from utils.loggers import logger

class IsAdmin(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool:
        user_id = event.from_user.id
        is_admin = str(user_id) == str(ADMIN_ID)
        
        if not is_admin:
            logger.warning(f"Ruxsatsiz kirishga urinish | id = {user_id}")
            
        return is_admin