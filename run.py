import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main
from config import TOKEN


async def main():
    """Main function to run bot"""
    await async_main()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit()')
