from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from kb import  ip_calc_kb, back_to_ip_calc
from ipaddress import IPv4Address, AddressValueError, \
    IPv4Interface, NetmaskValueError
from .mask_FAQ import mask
import re

router = Router(name=__name__)


class Ip_calc_state(StatesGroup):
    user_ip_address = State()


def ip_address_type(ip):
    ip = IPv4Interface(ip).ip
    if IPv4Address(ip).is_loopback:
        return 'Loopback адрес'
    if IPv4Address(ip).is_global:
        return 'Белый IP'
    if IPv4Address(ip).is_private:
        return 'Серый IP'
    if IPv4Address(ip).is_reserved:
        return 'Зарезервированный IP'
    if IPv4Address(ip).is_multicast:
        return 'Мультикаст IP'
    else:
        return 'Unknown'


@router.callback_query(F.data == 'ip_calc')
async def ip_calc(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.user_ip_address)
    if F.data == 'ip_calc_back':
        await callback.message.answer('Это IP Калькулятор 🧮\n\n\n'
                                      'Введите IP в формате IP/маска 🔢\n'
                                      'Либо введи IP без маски ℹ️\n'
                                      '(Вам будут предложены варианты масок 🎭)',
                                      reply_markup=ip_calc_kb)


@router.callback_query(F.data == 'ip_calc_back')
async def ip_calc_back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.user_ip_address)
    if F.data == 'ip_calc_back':
        await callback.message.edit_text('Это IP Калькулятор 🧮\n\n\n'
                                         'Введите IP в формате IP/маска 🔢/🎭)\n',
                                         reply_markup=ip_calc_kb)


@router.callback_query(Ip_calc_state.user_ip_address, F.data == 'mask_faq')
async def ip_calc(callback: CallbackQuery):
    await callback.message.edit_text(text=mask, reply_markup=back_to_ip_calc)


@router.callback_query(F.data == 'mask_faq')
async def ip_calc(callback: CallbackQuery):
    await callback.message.edit_text(text=mask)


@router.message(Ip_calc_state.user_ip_address,
                ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def ip_calc_state(message: Message, state: FSMContext):
    if '/' in message.text:
        try:
            ip = IPv4Interface(message.text)
            if str(ip.compressed).split("/")[-1] in ['31','32']:
                min_ip = list(ip.network.hosts())[0]
                accessible_ip = ip.network.num_addresses
            else:
                min_ip = list(ip.network.hosts())[1]
                accessible_ip = int(ip.network.num_addresses)-2
                
            await message.answer(f'<b>Ваш IP адрес</b> : <code>{ip.ip}</code>\n\n'
                                 f'<b>Тип вашего IP</b> : <code>{ip_address_type(ip)}</code>\n\n'
                                 f'<b>Короткая Маска</b> : <code>{str(ip.compressed).split("/")[-1]}</code>\n\n'
                                 f'<b>Длинная Маска</b> : <code>{ip.netmask}</code>\n\n'
                                 f'<b>Обратная маска</b> : <code>{str(ip.with_hostmask).split("/")[-1]}</code>\n\n'
                                 f'<b>Общая сеть</b> : <code>{ip.network.network_address}</code>\n\n'
                                 f'<b>Шлюз по Умолчанию</b> : <code>{list(ip.network.hosts())[0]}</code>\n\n'
                                 f'<b>Бродкаст адрес</b>: <code>{ip.network.broadcast_address}</code>\n\n'
                                 f'<b>Минимальный IP</b> : <code>{min_ip}</code>\n\n'
                                 f'<b>Максимальный IP</b> : <code>{list(ip.network.hosts())[-1]}</code>\n\n'
                                 f'<b>Всего доступных адресов в сети</b> : <code>{accessible_ip}'
                                 f'</code>\n\n'
                                 )
        except AddressValueError:
            await message.answer('Не корректный IP адрес')
        except NetmaskValueError:
            await message.answer('Не корректная Маска')
    else:
        await message.answer('Запись Адреса не корректна')
    await state.clear()
