from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from aiogram.enums import ChatAction
from ipaddress import IPv4Address, AddressValueError, IPv4Interface
import subprocess
import json
from kb import back_to_main_menu
from common_functions import main_log


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


def cURL(url):
    return subprocess.check_output(['curl', url])


router = Router(name=__name__)

session = requests.Session()


class Ip_info_state(StatesGroup):
    ip_info_st = State()


@router.callback_query(F.data == 'ip_info')
async def ip_info_main(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Ip_info_state.ip_info_st)
    main_log(callback=callback)
    await callback.message.answer('Напишите IP информацию о котором вы хотите узнать:')


@router.message(Ip_info_state.ip_info_st,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def ip_info_fc(message: Message, state: FSMContext):
    main_log(message=message)
    try:
        ip = IPv4Address(message.text)
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        if ip_address_type(ip) in ['Loopback адрес', 'Серый IP', 'Мультикаст IP']:
            await message.answer('<b>О данном IP нету информации</b> ⁉️',
                                 reply_markup=back_to_main_menu)

        else:
            ip_info_json = json.loads(cURL(f'https://ipcheck.me/ru/{ip}'))
            await message.answer(f'<b>IP адрес</b> : <code>{ip_info_json["ip"]}</code>\n\n'
                                 f'<b>Компания</b> : <code>{ip_info_json["network"]["asn_organization"]}</code>\n\n'
                                 f'<b>Континент</b> : <code>{ip_info_json["location"]["continent"]}</code>\n\n'
                                 f'<b>Страна</b> : <code>{ip_info_json["location"]["country"]}</code>\n\n'
                                 f'<b>Регион</b> : <code>{ip_info_json["location"]["subdivision_1_name"]}</code>\n\n'
                                 f'<b>Город</b> : <code>{ip_info_json["location"]["city_name"]}</code>\n\n'
                                 f'<b>Временная зона</b> : <code>{ip_info_json["timezone"]["zone_name"]}</code>\n\n'
                                 f'<b>Общая Сеть</b> : <code>{ip_info_json["network"]["cidr"]}</code>\n\n'
                                 f'<b>ASN</b>: <code>{ip_info_json["network"]["asn"]}</code>\n\n'
                                 f'<b>Домен</b> : <code>{ip_info_json["country"]["tld"]}</code>\n\n'
                                 )
            await message.answer_location(latitude=float(ip_info_json['location']['latitude']),
                                          longitude=float(ip_info_json['location']['longitude']))
    except AddressValueError:
        await message.answer('<b>Не верный формат IP</b> ⁉️\n'
                             'Повторите ввод:',
                             reply_markup=back_to_main_menu)
    except:
        await message.answer('<b>О данном IP нету информации</b> ⁉️',
                             reply_markup=back_to_main_menu)
