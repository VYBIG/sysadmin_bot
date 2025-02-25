import subprocess
from ipaddress import AddressValueError, IPv4Interface
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from common_functions import main_log
from kb import exit_menu_2

router = Router(name=__name__)


class Nslookup_state(StatesGroup):
    host_state = State()


def ns_look_up(host, ip_or_host):
    if ';' in host or '|' in host or '&' in host or '>' in host:
        raise subprocess.CalledProcessError(returncode=2, cmd=f"host {host}")
    if ip_or_host:
        return subprocess.check_output(f"host {host} " + "| grep 'has address' | awk '{ print $4 }'", shell=True)
    else:
        return subprocess.check_output(f"host {host} " + "| awk '{ print $5 }'", shell=True)


@router.callback_query(F.data == 'nslookup')
async def nslookup_main_fc(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Nslookup_state.host_state)
    main_log(callback=callback)
    await callback.message.answer('🌐 Напишите <b>IP/Доменное имя</b>\n'
                                  'которое нужно обработать:', reply_markup=exit_menu_2)


@router.message(Nslookup_state.host_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def nslookup(message: Message, state: FSMContext):
    main_log(message=message)
    try:
        IPv4Interface(message.text)
        await message.answer(f'IP <code>{message.text}</code> резолвится как:\n'
                             f'<pre>{ns_look_up(message.text, False).decode("utf-8")}</pre>',
                             reply_markup=exit_menu_2
                             )
    except AddressValueError:
        try:
            await message.answer(f'<code>{message.text}</code>соответствует адресам:\n'
                                 f'<pre>{ns_look_up(message.text, True).decode("utf-8")}</pre>',
                                 reply_markup=exit_menu_2)
        except subprocess.CalledProcessError:
            await message.answer('<b>Запись не корректна</b> ⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=exit_menu_2)

    except subprocess.CalledProcessError:
        await message.answer('<b>Запись не корректна</b> ⁉️\n'
                             'Повторите ввод:'
                             , reply_markup=exit_menu_2)


