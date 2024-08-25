from aiogram import Router, F
from aiogram.enums import ChatAction, ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.text_decorations import html_decoration

from kb import main_menu_1, main_menu_2

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await message.answer(f"Привет 👋, <b>{message.from_user.full_name}</b>! Я сетевой бот помощник 💡\n\n"
                         f"Выбери функцию которую ты хочешь использовать⬇️",
                         reply_markup=main_menu_1,parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'back_menu_1')
async def back_menu_1_func(callback: CallbackQuery):
    await callback.message.edit_text(
        f"Привет 👋, <b>{callback.from_user.full_name}</b>! Я сетевой бот помощник 💡\n\n"
        f"Выбери функцию которую ты хочешь использовать⬇️",
        reply_markup=main_menu_1)


@router.callback_query(F.data == 'next_menu_2')
async def next_menu_2_func(callback: CallbackQuery):
    await callback.message.edit_text(
        f"Привет 👋, <b>{callback.from_user.full_name}</b>! Я сетевой бот помощник 💡\n\n"
        f"Выбери функцию которую ты хочешь использовать⬇️",
        reply_markup=main_menu_2)
