import asyncio
from aiogram import Dispatcher, Bot 
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from utils.loggers import logger
from utils.db.database import create_tables, close_engine
from handlers import start, callback, register, admin 

from middleware.logger_middleware import LoggerMiddleware
from middleware.throttling_middleware import ThrottlingMiddleware


async def main():
    logger.info("-"*40)
    logger.info("Bot ishga tushurilmoqda...")

    await create_tables()

    

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.middleware(LoggerMiddleware())
    dp.message.middleware(ThrottlingMiddleware(rate_limit=1.0))


    dp.include_router(start.router)
    dp.include_router(register.router)
    dp.include_router(admin.router) 
    dp.include_router(callback.router)

    logger.info("Barcha routerlar ulandi)")
    logger.info("Polling boshlandi")
    logger.info("-"*40)

    try:
       await dp.start_polling(bot)
    finally:
       await close_engine()
       logger.info("Bot to'xtatildi")

if __name__ == '__main__':
    asyncio.run(main())