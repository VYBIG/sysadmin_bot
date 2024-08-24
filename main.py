import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import BOT_TOKEN
from kb import *

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Привет 👋, {html.bold(message.from_user.full_name)}! Я сетевой бот помощник 💡\n\n"
                         f"Выбери функцию которую ты хочешь использовать⬇️",
                         reply_markup=main_menu_1)


@dp.callback_query(F.data == 'back_menu_1')
async def button_help(callback: CallbackQuery):
    await callback.message.edit_text(
        f"Привет 👋, {html.bold(callback.from_user.full_name)}! Я сетевой бот помощник 💡\n\n"
        f"Выбери функцию которую ты хочешь использовать⬇️",
        reply_markup=main_menu_1)


@dp.callback_query(F.data == 'next_menu_2')
async def button_help(callback: CallbackQuery):
    await callback.message.edit_text(
        f"Привет 👋, {html.bold(callback.from_user.full_name)}! Я сетевой бот помощник 💡\n\n"
        f"Выбери функцию которую ты хочешь использовать⬇️",
        reply_markup=main_menu_2)


@dp.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"Я сетевой бот, созданный чтобы помогать сетевым инженерам\n"
                         f"Вот некоторые из моих возможностей:\n"
                         f"- 🧾 <b>Производитель оборудования по MAC Адресу</b>\n"
                         f"- 🧮 <b>IP Калькулятор</b>\n"
                         f"- ↔️ <b>Конвертация Бит и Байт</b>\n"
                         f"- ✉️ <b>ping</b>\n"
                         f"и многое другое \n\n\n"
                         f"Чтобы запустить меня нажми /start")


@dp.message(Command('chat_gpt'))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"Решим Нейросети находится в разработке! 🔜")


@dp.message(Command('get_id'))
async def command_help_handler(message: Message) -> None:
    await message.answer(f'Твой Телеграмм ID - {message.from_user.id}')


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
