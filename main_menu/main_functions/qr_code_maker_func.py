import os
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, InputFile, BufferedInputFile
from kb import exit_menu_2
from common_functions import main_log
import qrcode

router = Router(name=__name__)


def qrcode_maker(string: str, file_name: str):
    img = qrcode.make(f"{string}")
    img.save(f"qr_{file_name}.jpeg")


class Qr_state(StatesGroup):
    qr_gen_state = State()
    to_state = State()
    count_state = State()


@router.callback_query(F.data == 'QR_code_maker')
async def qr_code_maker(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Qr_state.qr_gen_state)
    await callback.message.answer('<b>Это Генератор QR-Кодов</b>\n\n'
                                  'Напишите текст или ссылку \n'
                                  'для которой нужно сгенерировать QR-код:',
                                  reply_markup=exit_menu_2)


@router.message(Qr_state.qr_gen_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def qr_code_maker(message: Message):
    main_log(message=message)
    qrcode_maker(message.text,
                 str(message.from_user.id))
    try:
        photo = open(f"qr_{message.from_user.id}.jpeg", 'rb').read()
        photo = BufferedInputFile(photo, filename="macs.txt", )
        await message.bot.send_photo(photo=photo,
                                     chat_id=message.from_user.id)
        await message.answer(reply_markup=exit_menu_2,
                             text='Сгенерировал QR-код\n'
                                  'Вы можете написать текст '
                                  'или ссылку еще раз:')
        os.remove(f"qr_{message.from_user.id}.jpeg")
    except:
        await message.answer('Что-то пошло не так\n'
                             'Повторите ввод:',
                             reply_markup=exit_menu_2)
