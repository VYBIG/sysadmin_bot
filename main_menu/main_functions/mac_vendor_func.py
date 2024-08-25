#https://www.macvendorlookup.com/api/v2/{MAC_Address}
from aiogram import Router, F
from aiogram.types import CallbackQuery

from kb import exit_menu_1

router = Router(name=__name__)


@router.callback_query(F.data == 'mac_vendor')
async def mac_vendor(callback: CallbackQuery):
    await callback.message.edit_text('Функция в Разработке!', reply_markup=exit_menu_1)
