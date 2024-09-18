from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.enums import ChatAction
import requests
import time
import re
import json
from kb import mac_convert_upper, mac_convert_lower, exit_convert_upper, exit_convert_lower

session = requests.Session()
router = Router(name=__name__)


class Mac_conv_state(StatesGroup):
    mac_conv_upper = State()
    mac_conv_lower = State()
    mac_conv_up = State()
    mac_conv_low = State()


def is_valid_mac(mac):
    pattern = r'^(?:[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}\.[0-9A-Fa-f]{4}|(?:[0-9A-Fa-f]{2}[-:]){5}[0-9A-Fa-f]{2})$'
    return bool(re.match(pattern, mac))


def format_mac_address(mac):
    mac = ''.join(filter(str.isalnum, mac))
    formatted_mac = ':'.join(mac[i:i + 2] for i in range(0, 12, 2))
    return formatted_mac


def mac_converter(macs: str, conv_type: str, lower_upper: bool):
    macs = macs.split('\n')
    converted_macs = ''
    for mac in macs:
        if is_valid_mac(format_mac_address(mac.strip())):
            mac = format_mac_address(mac.strip()).replace(':', '')
            if lower_upper:
                mac = mac.upper()
            else:
                mac = mac.lower()
            if conv_type == 'colon_1_callback':
                converted_macs += ':'.join(mac[i:i + 2] for i in range(0, 12, 2)) + '\n'
            elif conv_type == 'point_1_callback':
                converted_macs += '.'.join(mac[i:i + 2] for i in range(0, 12, 2)) + '\n'
            elif conv_type == 'hyphen_1_callback':
                converted_macs += '-'.join(mac[i:i + 2] for i in range(0, 12, 2)) + '\n'
            elif conv_type == 'colon_2_callback':
                converted_macs += ':'.join(mac[i:i + 4] for i in range(0, 12, 4)) + '\n'
            elif conv_type == 'point_2_callback':
                converted_macs += '.'.join(mac[i:i + 4] for i in range(0, 12, 4)) + '\n'
            elif conv_type == 'hyphen_2_callback':
                converted_macs += '-'.join(mac[i:i + 4] for i in range(0, 12, 4)) + '\n'
            elif conv_type == 'solid_callback':
                converted_macs += mac + '\n'
        else:
            converted_macs += f'"{mac}" - Ошибка форматирования\n'
    return converted_macs


@router.callback_query(F.data == 'mac_converter')
async def mac_converter_default(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Mac_conv_state.mac_conv_upper)
    await callback.message.answer('Выберете формат в который вы хотите \n'
                                  'конвертировать MAC-Адреса \n'
                                  'Так же выберите формат конвертации\n'
                                  '<b>А так же размер букв</b>\n'
                                  '(нужный отмечен ✅)',
                                  reply_markup=mac_convert_upper)


@router.callback_query(F.data.in_({'back_to_lower',
                                   'lower_callback'}))
async def mac_converter_low(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Mac_conv_state.mac_conv_lower)
    await callback.message.edit_text('Выберете формат в который вы хотите \n'
                                     'конвертировать MAC-Адреса \n'
                                     'Так же выберите формат конвертации\n'
                                     '<b>А так же размер букв</b>\n'
                                     '(нужный отмечен ✅)',
                                     reply_markup=mac_convert_lower)


@router.callback_query(F.data.in_({'back_to_upper', 'upper_callback'}))
async def mac_converter_up(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Mac_conv_state.mac_conv_upper)
    await callback.message.edit_text('Выберете формат в который вы хотите \n'
                                     'конвертировать MAC-Адреса \n'
                                     'Так же выберите формат конвертации\n'
                                     '<b>А так же размер букв</b>\n'
                                     '(нужный отмечен ✅)',
                                     reply_markup=mac_convert_upper)


@router.callback_query(Mac_conv_state.mac_conv_upper, F.data.in_({'colon_1_callback',
                                                                  'point_1_callback',
                                                                  'hyphen_1_callback',
                                                                  'colon_2_callback',
                                                                  'point_2_callback',
                                                                  'hyphen_2_callback',
                                                                  'solid_callback'}))
async def mac_converter_up_func(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'colon_1_callback':
        F.data = 'colon_1_callback'
        mac_form_up = "XX:XX:XX:XX:XX:XX"
    elif callback.data == 'point_1_callback':
        F.data = 'point_1_callback'
        mac_form_up = "XX.XX.XX.XX.XX.XX"
    elif callback.data == 'hyphen_1_callback':
        F.data = 'hyphen_1_callback'
        mac_form_up = "XX-XX-XX-XX-XX-XX"
    elif callback.data == 'colon_2_callback':
        F.data = 'colon_2_callback'
        mac_form_up = "XXXX:XXXX:XXXX"
    elif callback.data == 'point_2_callback':
        F.data = 'point_2_callback'
        mac_form_up = "XXXX.XXXX.XXXX"
    elif callback.data == 'hyphen_2_callback':
        F.data = 'hyphen_2_callback'
        mac_form_up = "XXXX-XXXX-XXXX"
    elif callback.data == 'solid_callback':
        F.data = 'solid_callback'
        mac_form_up = "XXXXXXXXXXXX"
    await state.set_state(Mac_conv_state.mac_conv_up)
    await callback.message.edit_text(f'Был выбран формат <code>{mac_form_up}</code>\n'
                                     'Напишите в стоблик свои мак адреса\n\n'
                                     'Пример:\n'
                                     '<code>FF:FF:FF:FF:FF:FF</code>\n'
                                     '<code>11:11:11:11:11:11</code>\n'
                                     '<code>22:22:22:22:22:22</code>\n\n',
                                     reply_markup=exit_convert_upper)


@router.message(Mac_conv_state.mac_conv_up,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel'))
async def mac_converter_func_up(message: Message, state: FSMContext):
    await message.answer('<b>Конвертированные MAC-Адреса:</b>\n\n'
                         f'<pre>{mac_converter(message.text, F.data, True)}</pre>',
                         reply_markup=exit_convert_upper)

    await state.clear()


@router.callback_query(Mac_conv_state.mac_conv_lower, F.data.in_({'colon_1_callback',
                                                                  'point_1_callback',
                                                                  'hyphen_1_callback',
                                                                  'colon_2_callback',
                                                                  'point_2_callback',
                                                                  'hyphen_2_callback',
                                                                  'solid_callback'}))
async def mac_converter_low_func(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'colon_1_callback':
        F.data = 'colon_1_callback'
        mac_form_low = 'xx:xx:xx:xx:xx:xx'
    elif callback.data == 'point_1_callback':
        F.data = 'point_1_callback'
        mac_form_low = "xx.xx.xx.xx.xx.xx"
    elif callback.data == 'hyphen_1_callback':
        F.data = 'hyphen_1_callback'
        mac_form_low = "xx-xx-xx-xx-xx-xx"
    elif callback.data == 'colon_2_callback':
        F.data = 'colon_2_callback'
        mac_form_low = "xxxx:xxxx:xxxx"
    elif callback.data == 'point_2_callback':
        F.data = 'point_2_callback'
        mac_form_low = "xxxx.xxxx.xxxx"
    elif callback.data == 'hyphen_2_callback':
        F.data = 'hyphen_2_callback'
        mac_form_low = "xxxx-xxxx-xxxx"
    elif callback.data == 'solid_callback':
        F.data = 'solid_callback'
        mac_form_low = "xxxxxxxxxxxx"
    await state.set_state(Mac_conv_state.mac_conv_low)
    await callback.message.edit_text(f'Был выбран формат <code>{mac_form_low}</code>\n'
                                     'Напишите в стоблик свои мак адреса\n\n'
                                     'Пример:\n'
                                     '<code>ff:ff:ff:ff:ff:ff</code>\n'
                                     '<code>11:11:11:11:11:11</code>\n'
                                     '<code>22:22:22:22:22:22</code>\n\n',
                                     reply_markup=exit_convert_lower)


@router.message(Mac_conv_state.mac_conv_low,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel'))
async def mac_converter_func_low(message: Message, state: FSMContext):
    await message.answer('<b>Конвертированные MAC-Адреса:</b>\n\n'
                         f'<pre>{mac_converter(message.text, F.data, False)}</pre>',
                         reply_markup=exit_convert_lower)

    await state.clear()
