from aiogram import Router, F
from aiogram.types import CallbackQuery
from common_functions import main_log
from kb import exit_menu_2

router = Router(name=__name__)


@router.callback_query(F.data == 'file_converter')
async def file_converter(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text('Функция в Разработке!', reply_markup=exit_menu_2)