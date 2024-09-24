from aiogram import Router, F
from aiogram.types import CallbackQuery

from kb import exit_menu_2
from common_functions import main_log
router = Router(name=__name__)


@router.callback_query(F.data == 'QR_code_maker')
async def qr_code_maker(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text('Функция в Разработке!', reply_markup=exit_menu_2)
