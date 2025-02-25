import subprocess
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from ipaddress import IPv4Address, AddressValueError
import time
from kb import back_to_main_menu
from common_functions import main_log
router = Router(name=__name__)


class Ping_state(StatesGroup):
    ping_state = State()


def ping(ip):
    if ';' in ip or '|' in ip or '&' in ip or '>' in ip:
        raise subprocess.CalledProcessError(returncode=2,cmd=f"ping -c 1 {ip}")
    process = subprocess.Popen(f"ping -c 1 {ip}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return True
    elif process.returncode == 1:
        return False
    else:
        raise subprocess.CalledProcessError(returncode=2,cmd=f"ping -c 1 {ip}")


@router.callback_query(F.data == 'ping')
async def ping_main_fc(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ping_state.ping_state)
    main_log(callback=callback)
    await callback.message.answer('Напишите Хост до которого нужно проверить доступ по протоколу ICMP:')


@router.message(Ping_state.ping_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def ping_fc(message: Message, state: FSMContext):
    main_log(message=message)
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        if IPv4Address(message.text).is_global:
            await message.bot.send_chat_action(chat_id=message.chat.id,
                                               action=ChatAction.TYPING)
            time.sleep(1)
            if ping(message.text):
                await message.answer(f'{message.text} - <b>Доступен по ICMP</b> ✅',
                                     reply_markup=back_to_main_menu)
            else:
                await message.answer(f'{message.text} - <b>Не доступен по ICMP</b> ❌',
                                     reply_markup=back_to_main_menu)
        else:
            await message.answer(f'IP-Адрес не входит в диапазон <b>Белых IP</b>⁉️\n'
                                 f'Повторите ввод:',
                                 reply_markup=back_to_main_menu)
    except AddressValueError:
        try:
            await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            time.sleep(1)
            if ping(message.text):
                await message.answer(f'{message.text} - <b>Доступен по ICMP</b> ✅', 
                                     reply_markup=back_to_main_menu)
            else:
                await message.answer(f'{message.text} - <b>Не доступен по ICMP</b> ❌',
                                         reply_markup=back_to_main_menu)
        except subprocess.CalledProcessError:
            await message.answer('<b>Не правильная запись хоста </b>⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=back_to_main_menu)
    except subprocess.CalledProcessError:
        await message.answer('<b>Не правильная запись хоста </b>⁉️\n'
                             'Повторите ввод:'
                             , reply_markup=back_to_main_menu)
