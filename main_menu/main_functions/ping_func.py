import subprocess
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from ipaddress import IPv4Address, AddressValueError
import time
router = Router(name=__name__)


class Ping_state(StatesGroup):
    ping_state = State()


def ping(ip):
    process = subprocess.Popen(f"ping -c 1 {ip}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return True
    else:
        return False


@router.callback_query(F.data == 'ping')
async def ping_main_fc(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ping_state.ping_state)
    await callback.message.answer('Напишите IP до которого нужно проверить доступ по протоколу ICMP:')


@router.message(Ping_state.ping_state, ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def ping_fc(message: Message, state: FSMContext):
    try:
        ip = IPv4Address(message.text)
        if ip.is_global:
            await message.bot.send_chat_action(chat_id=message.chat.id,
                                               action=ChatAction.TYPING)
            time.sleep(4)
            if ping(ip):

                await message.answer(f'{ip} - <b>Доступен</b> ✅')
            else:
                await message.answer(f'{ip} - <b>Не доступен</b> ❌')
        else:
            await message.answer(f'IP-Адрес не входит в диапазон <b>Белых IP</b>',)

    except AddressValueError:
        await message.answer('Не верный формат IP')
    await state.clear()
