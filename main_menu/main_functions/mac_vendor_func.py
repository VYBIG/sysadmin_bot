# https://www.macvendorlookup.com/api/v2/{MAC_Address}
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
import re
import json
from kb import exit_menu_1

session = requests.Session()
router = Router(name=__name__)


def is_valid_mac(mac):
    pattern = r'^(?:[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}|(?:[0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac))


class Mac_vendor_state(StatesGroup):
    user_mac = State()


@router.callback_query(F.data == 'mac_vendor')
async def mac_vendor(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(Mac_vendor_state.user_mac)
    await callback.message.answer('Напишите MAC-Адрес, который вы хотите опознать',
                                  reply_markup=exit_menu_1)


@router.message(Mac_vendor_state.user_mac, ~Command('help','start','get_id','chat_gpt'))
async def mac_vendor_state(message: Message, state: FSMContext):
    if is_valid_mac(str(message.text)):
        try:
            mac = session.get(url=f'https://www.macvendorlookup.com/api/v2/{str(message.text)}')
            mac_desc = mac.json()[0]
            await message.answer(text=f"Ваш Мак : {str(message.text)}\n"
                                 f"Компания : {str(mac_desc['company'])}\n"
                                 f"Адрес : {str(mac_desc['addressL1'])}\n")
        except:
            await message.answer('Мак Адрес не найден')
    else:
        await message.answer('Мак Адрес не соответствует стандартам')
    await state.clear()
