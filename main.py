import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import BOT_TOKEN
from main_menu import router
from aiogram.types import Message, CallbackQuery

dp = Dispatcher()
dp.include_router(router)


async def main() -> None:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="sysadmins.txt",filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
