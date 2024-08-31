from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import requests
from ipaddress import IPv4Address, AddressValueError
import subprocess
import json


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
    await callback.message.answer('Напишите IP информацию о котором вы хотите узнать:')


@router.message(Ip_info_state.ip_info_st, ~Command('help', 'start', 'get_id', 'chat_gpt'))
async def ip_info_fc(message: Message, state: FSMContext):
    try:
        ip = IPv4Address(message.text)
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
        await message.answer_location(latitude = float(ip_info_json['location']['latitude']),
                                      longitude=float(ip_info_json['location']['longitude']))
    except AddressValueError:
        await message.answer('Не верный формат IP')
    except:
        await message.answer('Что-то пошло не  так попробуй еще раз')
    await state.clear()
