from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from bs4 import BeautifulSoup

from kb import ip_calc_kb, back_to_ip_calc, \
    back_to_main_menu, ip_calc_kb_wo_to_bit
from ipaddress import IPv4Address, AddressValueError, \
    IPv4Interface, NetmaskValueError
from .mask_FAQ import mask
from common_functions import main_log
import requests

router = Router(name=__name__)


class Ip_calc_state(StatesGroup):
    user_ip_address = State()
    ip_with_bit = State()


def to_bit(ip):
    return '.'.join([bin(int(x) + 256)[3:] for x in ip.split('.')])


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


@router.callback_query(Ip_calc_state.user_ip_address, F.data == 'ip_calc_back')
async def ip_calc(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await callback.message.edit_text('Это IP Калькулятор 🧮\n\n\n'
                                     'Введите IP в формате IP/маска 🔢/🎭)\n',
                                     reply_markup=ip_calc_kb)


@router.callback_query(Ip_calc_state.ip_with_bit, F.data == 'no_to_bit')
async def ip_calc_no_bit(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.user_ip_address)
    await callback.message.edit_text('Это IP Калькулятор 🧮\n\n\n'
                                     'Введите IP в формате IP/маска 🔢/🎭)\n',
                                     reply_markup=ip_calc_kb)


@router.callback_query(F.data == 'ip_calc_back')
async def ip_calc(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.user_ip_address)
    await callback.message.answer('Это IP Калькулятор 🧮\n\n\n'
                                  'Введите IP в формате IP/маска 🔢/🎭)\n',
                                  reply_markup=ip_calc_kb)


@router.callback_query(F.data == 'ip_calc')
async def ip_calc(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.user_ip_address)
    main_log(callback=callback)
    await callback.message.answer('Это IP Калькулятор 🧮\n\n\n'
                                  'Введите IP в формате IP/маска 🔢/🎭)\n',
                                  reply_markup=ip_calc_kb)


@router.callback_query(Ip_calc_state.user_ip_address, F.data == 'to_bit')
async def ip_calc_bit(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_calc_state.ip_with_bit)
    main_log(callback=callback)
    await callback.message.edit_text('Это IP Калькулятор 🧮\n\n\n'
                                     'Введите IP в формате IP/маска 🔢/🎭)\n'
                                     '<b>в Скобках будут IP в двоичном формате</b>',
                                     reply_markup=ip_calc_kb_wo_to_bit)


@router.callback_query(Ip_calc_state.user_ip_address, F.data == 'mask_faq')
async def ip_calc_mask(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await callback.message.edit_text(text=mask, reply_markup=back_to_ip_calc)


@router.callback_query(F.data == 'mask_faq')
async def ip_calc_mask(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text(text=mask)


@router.callback_query(F.data.in_({'no_to_bit', 'to_bit'}))
async def ip_calc(callback: CallbackQuery):
    main_log(callback=callback)
    await callback.message.edit_text('<blockquote>Это сообщение давно позади 😐</blockquote>')


@router.message(Ip_calc_state.user_ip_address,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def ip_calc_state(message: Message, state: FSMContext):
    main_log(message=message)
    if '/' in message.text:
        try:
            await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            ip = IPv4Interface(message.text)
            if str(ip.compressed).split("/")[-1] in [str(i) for i in range(0, 15)] + ['31', '32']:
                responce = requests.Session()

                resp = responce.post(url='https://ip-calculator.ru/subnetcalc',
                                     data={"ip": f"{ip.ip}",
                                           "mask": f'{str(ip.compressed).split("/")[-1]}',
                                           "ajax": "1"})

                soup = BeautifulSoup(resp.text, "html.parser")
                soup = soup.find_all('td')
                main_ip = soup[1].contents[0]
                ip_type = ip_address_type(soup[1].contents[0])
                short_mask = soup[5].contents[0]
                long_mask = soup[9].contents[0]
                wildcard = soup[13].contents[0]
                network = soup[17].contents[0]
                gateway = soup[25].contents[0]
                broadcast = soup[21].contents[0]
                min_ip = IPv4Address(soup[25].contents[0]) + 1
                max_ip = soup[29].contents[0]
                accessible_ip = int(str(soup[33].contents[0]).replace(',', ''))
                if str(ip.compressed).split("/")[-1] in ['31', '32']:
                    accessible_ip = int(str(soup[33].contents[0]).replace(',', ''))+1
            else:
                main_ip = ip.ip
                ip_type = ip_address_type(ip)
                short_mask = str(ip.compressed).split("/")[-1]
                long_mask = ip.netmask
                wildcard = str(ip.with_hostmask).split("/")[-1]
                network = ip.network.network_address
                gateway = list(ip.network.hosts())[0]
                broadcast = ip.network.broadcast_address
                max_ip = list(ip.network.hosts())[-1]
                min_ip = list(ip.network.hosts())[1]
                accessible_ip = int(ip.network.num_addresses) - 2
            await message.answer(f'<b>Ваш IP адрес</b> : <code>{main_ip}</code>\n\n'
                                 f'<b>Тип вашего IP</b> : <code>{ip_type}</code>\n\n'
                                 f'<b>Короткая Маска</b> : <code>{short_mask}</code>\n\n'
                                 f'<b>Длинная Маска</b> : <code>{long_mask}</code>\n\n'
                                 f'<b>Обратная маска</b> : <code>{wildcard}</code>\n\n'
                                 f'<b>Общая сеть</b> : <code>{network}</code>\n\n'
                                 f'<b>Шлюз по Умолчанию</b> : <code>{gateway}</code>\n\n'
                                 f'<b>Бродкаст адрес</b>: <code>{broadcast}</code>\n\n'
                                 f'<b>Минимальный IP</b> : <code>{min_ip}</code>\n\n'
                                 f'<b>Максимальный IP</b> : <code>{max_ip}</code>\n\n'
                                 f'<b>Всего доступных адресов в сети</b> : <code>{accessible_ip}'
                                 f'</code>\n\n'
                                 , reply_markup=back_to_main_menu)


        except AddressValueError:
            await message.answer('<b>Не корректный IP адрес</b> ⁉️\n'
                                 'Повторите ввод:',
                                 reply_markup=back_to_main_menu)
        except NetmaskValueError:
            await message.answer('<b>Не корректная Маска</b> ⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=back_to_main_menu)
        except:
            await message.answer('<b>Произошла какая-то ошибка</b> ⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=back_to_main_menu)
    else:
        await message.answer('<b>Запись Адреса не корректна</b> ⁉️\n'
                             'Повторите ввод:',
                             reply_markup=back_to_main_menu)


@router.message(Ip_calc_state.ip_with_bit,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def ip_calc_state_with_bit(message: Message, state: FSMContext):
    main_log(message=message)
    if '/' in message.text:
        try:
            await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
            ip = IPv4Interface(message.text)
            if str(ip.compressed).split("/")[-1] in [str(i) for i in range(0, 15)] + ['31', '32']:
                responce = requests.Session()

                resp = responce.post(url='https://ip-calculator.ru/subnetcalc',
                                     data={"ip": f"{ip.ip}",
                                           "mask": f'{str(ip.compressed).split("/")[-1]}',
                                           "ajax": "1"})

                soup = BeautifulSoup(resp.text, "html.parser")
                soup = soup.find_all('td')
                main_ip = soup[1].contents[0]
                ip_type = ip_address_type(soup[1].contents[0])
                short_mask = soup[5].contents[0]
                long_mask = soup[9].contents[0]
                wildcard = soup[13].contents[0]
                network = soup[17].contents[0]
                gateway = soup[25].contents[0]
                broadcast = soup[21].contents[0]
                min_ip = IPv4Address(soup[25].contents[0]) + 1
                max_ip = soup[29].contents[0]
                accessible_ip = int(str(soup[33].contents[0]).replace(',', ''))
                if str(ip.compressed).split("/")[-1] in ['31', '32']:
                    accessible_ip = int(str(soup[33].contents[0]).replace(',', ''))+1

            else:
                main_ip = ip.ip
                ip_type = ip_address_type(ip)
                short_mask = str(ip.compressed).split("/")[-1]
                long_mask = ip.netmask
                wildcard = str(ip.with_hostmask).split("/")[-1]
                network = ip.network.network_address
                gateway = list(ip.network.hosts())[0]
                broadcast = ip.network.broadcast_address
                max_ip = list(ip.network.hosts())[-1]
                min_ip = list(ip.network.hosts())[1]
                accessible_ip = int(ip.network.num_addresses) - 2
            await message.answer(f'<b>Ваш IP адрес</b> : <code>{main_ip}</code>'
                                 f'\n(<code>{to_bit(str(main_ip))}</code>)\n\n'
                                 f'<b>Тип вашего IP</b> : <code>{ip_type}</code>\n\n'
                                 f'<b>Короткая Маска</b> : <code>{short_mask}</code>\n\n'
                                 f'<b>Длинная Маска</b> : <code>{long_mask}</code>'
                                 f'\n(<code>{to_bit(long_mask)}</code>)\n\n'
                                 f'<b>Обратная маска</b> : <code>{wildcard}</code>'
                                 f'\n(<code>{to_bit(wildcard)}</code>)\n\n'
                                 f'<b>Общая сеть</b> : <code>{network}</code>'
                                 f'\n(<code>{to_bit(network)}</code>)\n\n'
                                 f'<b>Шлюз по Умолчанию</b> : <code>{gateway}</code>'
                                 f'\n(<code>{to_bit(gateway)}</code>)\n\n'
                                 f'<b>Бродкаст адрес</b>: <code>{broadcast}</code>'
                                 f'\n(<code>{to_bit(str(ip.network.broadcast_address))}</code>)\n\n'
                                 f'<b>Минимальный IP</b> : <code>{min_ip}</code>'
                                 f'\n(<code>{to_bit(str(min_ip))}</code>)\n\n'
                                 f'<b>Максимальный IP</b> : <code>{max_ip}</code>'
                                 f'\n(<code>{to_bit(max_ip)}</code>)\n\n'
                                 f'<b>Всего доступных адресов в сети</b> : <code>{accessible_ip}'
                                 f'</code>\n\n'
                                 , reply_markup=back_to_main_menu)


        except AddressValueError:
            await message.answer('<b>Не корректный IP адрес</b> ⁉️\n'
                                 'Повторите ввод:',
                                 reply_markup=back_to_main_menu)
        except NetmaskValueError:
            await message.answer('<b>Не корректная Маска</b> ⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=back_to_main_menu)
        except:
            await message.answer('<b>Произошла какая-то ошибка</b> ⁉️\n'
                                 'Повторите ввод:'
                                 , reply_markup=back_to_main_menu)
    else:
        await message.answer('<b>Запись Адреса не корректна</b> ⁉️\n'
                             'Повторите ввод:',
                             reply_markup=back_to_main_menu)
