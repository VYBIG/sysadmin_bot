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
from common_functions import main_log
from kb import exit_menu_1,back_to_main_menu

router = Router(name=__name__)


def ping(ip):
    process = subprocess.Popen(f"ping -c 1 {ip}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return True
    elif process.returncode == 1:
        return False
    else:
        raise subprocess.CalledProcessError(returncode=2,cmd=f"ping -c 1 {ip}")


class Tracert_state(StatesGroup):
    tracert_state = State()


def trace_route(host):
    return subprocess.check_output(f'traceroute -I -m 12 {host}',shell=True)


@router.callback_query(F.data == 'tracert')
async def tracert(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Tracert_state.tracert_state)
    main_log(callback=callback)
    await callback.message.answer('Введите Хост для Трассировки:')


@router.message(Tracert_state.tracert_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def tracert_fc(message: Message, state: FSMContext):
    main_log(message=message)
    try:
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        ping(message.text)
        try:
            if not IPv4Address(message.text).is_global:
                await message.answer('Хост не входит в диапазон <b>Белых IP</b> ⁉️'
                                     'Повторите ввод:'
                                     ,reply_markup=back_to_main_menu)
                await state.clear()
            else:
                messageID = await message.answer(f'Начинаю Трассировку до {message.text}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await message.bot.edit_message_text(chat_id=messageID.chat.id,
                                                    text=f"<blockquote>"
                                                         f"{trace_route(message.text).decode('utf-8')}"
                                                         f"</blockquote>",
                                                    message_id=messageID.message_id
                                                    ,reply_markup=back_to_main_menu)
        except ipaddress.AddressValueError:
            messageID = await message.answer(f'Начинаю Трассировку до {message.text}')
            await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            await message.bot.edit_message_text(chat_id=messageID.chat.id,
                                                text=f"<blockquote>"
                                                     f"{trace_route(message.text).decode('utf-8')}"
                                                     f"</blockquote>",
                                                message_id=messageID.message_id,
                                                reply_markup=back_to_main_menu)

    except subprocess.CalledProcessError:
        await message.answer('<b>Не правильная запись хоста</b> ⁉️\n'
                             'Повторите ввод:',
                             reply_markup=back_to_main_menu)
