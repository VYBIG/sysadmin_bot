from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from kb import exit_menu_2, pnc_kb, back_to_pnc
from .numbers_codes import codes
from common_functions import main_log
import requests
from bs4 import BeautifulSoup

session = requests.Session()

router = Router(name=__name__)


class Phone_number_check_state(StatesGroup):
    phone_check_state = State()


pncs = Phone_number_check_state.phone_check_state


@router.callback_query(F.data == 'phone_number')
async def phone_number(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(pncs)
    main_log(callback=callback)
    await callback.message.answer('Напишите номер телефона который хотите опознать\n\n'
                                  '<b>Формат - 7xxxxxxxxxx, 8xxxxxxxxxx</b> 📞',
                                  reply_markup=pnc_kb)


@router.callback_query(F.data == 'pnc_back')
async def phone_number(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(pncs)
    main_log(callback=callback)
    await callback.message.edit_text('Напишите номер телефона который хотите опознать\n\n'
                                     '<b>Формат - 7xxxxxxxxxx, 8xxxxxxxxxx</b> 📞',
                                     reply_markup=pnc_kb)


@router.message(pncs,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def phone_number_check(message: Message):
    main_log(message=message)
    try:
        phone = ''.join(filter(str.isdigit, message.text))
        phone = '7'+ phone[1:]
        phone_info = []
        await message.bot.send_chat_action(chat_id=message.chat.id,
                                           action=ChatAction.TYPING)
        response = session.get(f'https://apertonet.ru/zvonit/{phone}').text
        soup = BeautifulSoup(response, "html.parser")

        phone_response = soup.findAll('div', class_='apkijuquuu')
        for i in phone_response:
            phone_info.append(i.text)
        await message.answer(f'<b>Телефон</b> - <code>+{phone}</code>\n\n'
                             f'<b>Место положение</b> - <code>{phone_info[0]}</code>\n\n'
                             f'<b>Оператор связи</b> - <code>{phone_info[-1]}</code>',
                             reply_markup=exit_menu_2)
    except:
        await message.answer('Такой номер не найден\n'
                             'Повторите ввод:')


@router.callback_query(pncs, F.data == 'pnc_faq')
async def ip_calc_mask(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text(text=codes, reply_markup=back_to_pnc)


@router.callback_query(F.data == 'pnc_faq')
async def ip_calc_mask(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text(text=codes)
