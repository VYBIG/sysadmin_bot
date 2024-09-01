import ipaddress
import subprocess
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from ipaddress import IPv4Address, AddressValueError
import time

from kb import exit_menu_1

router = Router(name=__name__)


def check(host):
    return subprocess.check_output(f'host {host}',shell=True)


class Tracert_state(StatesGroup):
    tracert_state = State()


def trace_route(host):
    return subprocess.check_output(f'traceroute -I -m 12 {host}',shell=True)


@router.callback_query(F.data == 'tracert')
async def tracert(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Tracert_state.tracert_state)
    await callback.message.answer('Введите Хост для Трассировки:')


@router.message(Tracert_state.tracert_state, ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def tracert_fc(message: Message, state: FSMContext):
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        check(message.text)
        try:
            if not IPv4Address(message.text).is_global:
                await message.answer('Хост не входит в диапазон <b>Белых IP</b>')
                await state.clear()
            else:
                messageID = await message.answer(f'Начинаю Трассировку до {message.text}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await message.bot.edit_message_text(chat_id=messageID.chat.id,
                                                    text=trace_route(message.text).decode('utf-8'),
                                                    message_id=messageID.message_id)
        except ipaddress.AddressValueError:
            messageID = await message.answer(f'Начинаю Трассировку до {message.text}')
            await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            await message.bot.edit_message_text(chat_id=messageID.chat.id,
                                                text=trace_route(message.text).decode('utf-8'),
                                                message_id=messageID.message_id)

    except subprocess.CalledProcessError:
        await message.answer('Не правильная запись хоста')
    await state.clear()
