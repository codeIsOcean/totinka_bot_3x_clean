# скачиваем необходимые библиотеки: Aiogram 3x, sqlalchemy, asyncpg, openai, python-dotenv
import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await dp.start_polling(bot)




if __name__=='__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass