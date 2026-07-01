import asyncio
from aiogram import Dispatcher, Bot 
from config import BOT_TOKEN
from handlers import start
from handlers import start, callback


async def main():
    bot=Bot(token=BOT_TOKEN)
    dp=Dispatcher()
    dp.include_router(start.router)
    dp.include_router(callback.router)
    await dp.start_polling(bot)

if __name__== '__main__':
    asyncio.run(main())     