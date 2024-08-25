from aiogram import Router, F
from aiogram.types import CallbackQuery

from kb import exit_menu_1

router = Router(name=__name__)


@router.callback_query(F.data == 'tracert')
async def tracert(callback: CallbackQuery):
    await callback.message.edit_text('Функция в Разработке!', reply_markup=exit_menu_1)
