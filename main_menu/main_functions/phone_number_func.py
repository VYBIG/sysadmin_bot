from aiogram import Router, F
from aiogram.types import CallbackQuery

from kb import exit_menu_2

router = Router(name=__name__)


@router.callback_query(F.data == 'phone_number')
async def phone_number(callback: CallbackQuery):
    await callback.message.edit_text('Функция в Разработке!', reply_markup=exit_menu_2)
