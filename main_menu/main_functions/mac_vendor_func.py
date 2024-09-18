from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
import re
import json
from kb import exit_menu_1, back_to_main_menu

session = requests.Session()
router = Router(name=__name__)


def is_valid_mac(mac):
    pattern = r'^(?:[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}|(?:[0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac))


def format_mac_address(mac):
    mac = ''.join(filter(str.isalnum, mac)).upper()
    formatted_mac = ':'.join(mac[i:i + 2] for i in range(0, 12, 2))
    return formatted_mac


class Mac_vendor_state(StatesGroup):
    user_mac = State()


@router.callback_query(F.data == 'mac_vendor')
async def mac_vendor(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Mac_vendor_state.user_mac)
    await callback.message.answer('Напишите MAC-Адрес, который вы хотите опознать:')


@router.message(Mac_vendor_state.user_mac, ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel'))
async def mac_vendor_state(message: Message, state: FSMContext):
    mac = format_mac_address(str(message.text))
    if is_valid_mac(mac):
        try:
            mac = session.get(url=f'https://www.macvendorlookup.com/api/v2/{mac}')
            mac_desc = mac.json()[0]
            await message.answer(text=f"Ваш Мак : <code>{str(message.text)}</code>\n"
                                      f"Компания : <code>{str(mac_desc['company'])}</code>\n"
                                      f"Адрес : <code>{str(mac_desc['addressL1'])}</code>\n"
                                 , reply_markup=back_to_main_menu)
        except:
            await message.answer('<b>Мак Адрес не найден</b> ⁉️\n'
                                 'Повторите ввод:',
                                 reply_markup=back_to_main_menu)
    else:
        await message.answer('<b>Мак Адрес не соответствует стандартам</b> ⁉️\n'
                             'Повторите ввод:',
                             reply_markup=back_to_main_menu)
