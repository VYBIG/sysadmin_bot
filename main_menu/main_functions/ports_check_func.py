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


# nc -vnzu 192.168.40.146 80 это udp
# nc -vnz 192.168.40.146 80 это tcp

@router.callback_query(F.data == 'ports_check')
async def ports_check(callback: CallbackQuery):
    await callback.message.edit_text('Это Сканер Портов, '
                                     'выберите по какому '
                                     'протоколу нужно сканировать порты',
                                     # reply_markup=
                                     )
