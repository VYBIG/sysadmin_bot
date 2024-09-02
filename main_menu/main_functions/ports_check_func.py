import ipaddress
import subprocess
from subprocess import check_output, CalledProcessError
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.enums import ChatAction
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from ipaddress import IPv4Address, AddressValueError
import time

from kb import udp_tcp_prtl, exit_menu_1

router = Router(name=__name__)


class Ports_check_state(StatesGroup):
    ports_check_state_udp = State()
    ports_check_state_tcp = State()


class PortsNumberError(Exception):
    pass


class PortsCountError(Exception):
    pass


class PortsRecordError(Exception):
    pass


class SplitRecordError(Exception):
    pass


def check_ports_handler(ip_ports: str):
    count = 0
    if '/' not in ip_ports:
        raise SplitRecordError
    if "-" not in ip_ports.split('/')[1]:
        try:
            int(ip_ports.split('/')[1])
        except:
            raise PortsNumberError
        if int(ip_ports.split('/')[1]) not in [i for i in range(1, 65536)]:
            raise PortsNumberError
    if "-" in ip_ports.split('/')[1]:
        try:
            ports = ip_ports.split('/')[1].split('-')
            if int(ports[1]) - int(ports[0]) <= 0:
                raise PortsCountError

            for i in range(int(ports[0]), int(ports[-1]) + 1):
                if i not in [i for i in range(1, 65536)]:
                    raise PortsNumberError
                count += 1
            if count > 5:
                raise PortsCountError
        except:
            raise PortsNumberError


def udp_ports(ip, port):
    process = subprocess.Popen(f"nc -vnzu -w 5 {ip} {port}",
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return f'Connection to {ip} {port} port [udp/*] succeeded!'
    else:
        return f'Connect to {ip} port {port} (udp) failed'


def tcp_ports(ip, port):
    process = subprocess.Popen(f"nc -vnz -w 5 {ip} {port}",
                               shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return f'Connection to {ip} {port} port [tcp/*] succeeded!'
    else:
        return f'Connect to {ip} port {port} (tcp) failed'


@router.callback_query(F.data == 'ports_check')
async def ports_check(callback: CallbackQuery, state: FSMContext):

    await state.clear()
    await callback.answer(cache_time=1)
    await callback.message.answer('Это Сканер Портов 🔍,\n'
                                  'выберите по какому '
                                  'протоколу нужно сканировать порты:',
                                  reply_markup=udp_tcp_prtl
                                  )


@router.callback_query(F.data == 'udp_callback')
async def ports_check_udp(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ports_check_state.ports_check_state_udp)
    await callback.message.edit_text('Сканирование будет по <b>UDP</b> 🔍\n'
                                     'Введите IP и порт в формате <b>IP/PORT</b>\n'
                                     'Пример - (185.16.25.150/22) \nлибо диапазон (185.16.25.150/20-22)'
                                     'Диапазон не больше 5 портов')


@router.callback_query(F.data == 'tcp_callback')
async def ports_check_tcp(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ports_check_state.ports_check_state_tcp)
    await callback.message.edit_text('Сканирование будет по <b>TCP</b> 🔍\n'
                                     'Введите IP и порт в формате <b>IP/PORT</b>\n'
                                     'Пример - (185.16.25.150/22) \nлибо диапазон (185.16.25.150/20-22)'
                                     'Диапазон не больше 5 портов')


# Это обработчик для UDP
@router.message(Ports_check_state.ports_check_state_udp,
                ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def ports_check_fc_udp(message: Message, state: FSMContext):
    ports_check_message_udp = ""
    try:
        check_ports_handler(message.text)
        ip = message.text.split('/')
        if IPv4Address(ip[0]).is_global:
            if '-' in ip[-1]:
                message_id = await message.answer(f'Начинаю сканирование портов <b>UDP</b> {ip[-1]} у {ip[0]}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                ports = ip[-1].split('-')
                for i in range(int(ports[0]), int(ports[-1]) + 1):
                    try:
                        ports_check_message_udp += f'<blockquote>{udp_ports(ip[0], ports[i])}</blockquote>\n\n'
                    except CalledProcessError:
                        ports_check_message_udp += f"<blockquote>connect to {ip[0]} port {ports[i]} " \
                                               f"(udp) timed out:</blockquote>\n\n"
                await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                    text=ports_check_message_udp,
                                                    message_id=message_id.message_id)
            else:
                message_id = await message.answer(f'Начинаю сканирование порта <b>UDP</b> {ip[-1]} у {ip[0]}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                try:
                    await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                        text=f"<blockquote>"
                                                             f"{udp_ports(ip[0], ip[-1])}"
                                                             f"</blockquote>",
                                                        message_id=message_id.message_id)
                except CalledProcessError:
                    await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                        text=f"<blockquote>connect to "
                                                             f"{ip[0]} port {ip[-1]} "
                                                             f"(udp) timed out:</blockquote>",
                                                        message_id=message_id.message_id)

        else:
            await message.answer(f'IP-Адрес не входит в диапазон <b>Белых IP</b>')
    except AddressValueError:
        await message.answer('Не верный формат IP')
    except (PortsNumberError, PortsCountError, PortsRecordError):
        await message.answer('Не верная запись портов')
    except SplitRecordError:
        await message.answer('Не верная форма записи')

    await state.clear()


# Это обработчик для TCP
@router.message(Ports_check_state.ports_check_state_tcp,
                ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def ports_check_fc_tcp(message: Message, state: FSMContext):
    ports_check_message_tcp = ""
    try:
        check_ports_handler(message.text)
        ip = message.text.split('/')
        if IPv4Address(ip[0]).is_global:
            if '-' in ip[-1]:
                message_id = await message.answer(f'Начинаю сканирование портов <b>TCP</b> {ip[-1]} у {ip[0]}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                ports = ip[-1].split('-')
                for i in range(int(ports[0]), int(ports[-1]) + 1):
                    try:
                        ports_check_message_tcp += f'<blockquote>{tcp_ports(ip[0], ports[i])}</blockquote>\n\n'
                    except CalledProcessError:
                        ports_check_message_tcp += f"<blockquote>connect to {ip[0]} port {ports[i]} " \
                                               f"(tcp) timed out:</blockquote>\n\n"
                await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                    text=ports_check_message_tcp,
                                                    message_id=message_id.message_id)
            else:
                message_id = await message.answer(f'Начинаю сканирование порта <b>TCP</b> {ip[-1]} у {ip[0]}')
                await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                try:
                    await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                        text=f"<blockquote>"
                                                             f"{tcp_ports(ip[0], ip[-1])}"
                                                             f"</blockquote>",
                                                        message_id=message_id.message_id)
                except CalledProcessError:
                    await message.bot.edit_message_text(chat_id=message_id.chat.id,
                                                        text=f"<blockquote>connect to "
                                                             f"{ip[0]} port {ip[-1]} "
                                                             f"(tcp) timed out:</blockquote>",
                                                        message_id=message_id.message_id)

        else:
            await message.answer(f'IP-Адрес не входит в диапазон <b>Белых IP</b>')
    except AddressValueError:
        await message.answer('Не верный формат IP')
    except (PortsNumberError, PortsCountError, PortsRecordError):
        await message.answer('Не верная запись портов')
    except SplitRecordError:
        await message.answer('Не верная форма записи')

    await state.clear()
