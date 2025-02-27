from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from kb import back_to_main_menu
from aiogram.types import BufferedInputFile
from common_functions import main_log
import os

router = Router(name=__name__)


@router.message(Command('help'))
async def command_help_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
    main_log(message=message)
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await message.answer(f"Я сетевой бот, созданный чтобы помогать сетевым инженерам\n"
                         f"Вот некоторые из моих возможностей:\n"
                         f"- 🧾 <b>Производитель оборудования по MAC Адресу</b>\n"
                         f"- 🧮 <b>IP Калькулятор</b>\n"
                         f"- ↔️ <b>Конвертация Бит и Байт</b>\n"
                         f"- ✉️ <b>ping</b>\n"
                         f"и многое другое \n\n\n"
                         f"Чтобы запустить меня нажми /start\n"
                         f"Для Отмены команды нажмите /cancel или другую команду\n"
                         f"Команды будут выполняться до тех пор \n"
                         f"пока вы не нажмете /cancel\n"
                         f"или кнопку возвращения в основное меню",
                         reply_markup=back_to_main_menu)


@router.message(Command('get_id'))
async def command_get_id(message: Message, state: FSMContext) -> None:
    await state.clear()
    main_log(message=message)
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await message.answer(f'Твой Телеграмм ID - {message.from_user.id}')


@router.message(Command('cancel'))
async def command_get_id(message: Message, state: FSMContext) -> None:
    main_log(message=message)
    if await state.get_state() is None:
        await message.bot.send_chat_action(chat_id=message.chat.id,
                                           action=ChatAction.TYPING)
        await message.answer(f'Сейчас ничего не выполняется ⚠️\n\n'
                             f'Нажмите /start для вызова основного меню')
    else:
        await state.clear()
        await message.bot.send_chat_action(chat_id=message.chat.id,
                                           action=ChatAction.TYPING)
        await message.answer(f'Операция отменена ⛔️\n\n\n'
                             f'Нажмите /start для выхода в основное меню')


@router.message(Command('get_log'))
async def command_get_log(message: Message, state: FSMContext) -> None:
    await state.clear()
    main_log(message=message)
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    log = open('/root/.virtualenvs/sysadmin_bot/sysadmin_bot/sysadmins.txt', 'rb').read()
    document = BufferedInputFile(log, filename="log.txt")
    if message.chat.id == 643541689:
        await message.bot.send_document(message.chat.id, document=document)
    else:
        await message.answer('Такая команда вам не доступна ⛔️')


class Send_message_to_all(StatesGroup):
    the_message = State()
    user_list = State()


list_of_users = []
message_to_users = []


@router.message(Command('send_mes'))
async def command_send_message(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(Send_message_to_all.the_message)
    if message.chat.id == 643541689:
        await message.answer('Напишите сообщение \n'
                             'которое нужно отправить всем пользователям:')
    else:
        await message.answer('Такая команда вам не доступна ⛔️')


@router.message(Send_message_to_all.the_message,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def command_send_message_next(message: Message, state: FSMContext) -> None:
    message_to_users.append(message.text)
    message_to_users.append(message.entities)
    await state.set_state(Send_message_to_all.user_list)
    await message.answer('Напишите список пользователей \n'
                         'которым нужно отправить это сообщение\n'
                         'Телеграм ID в столбик:')


@router.message(Send_message_to_all.user_list,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def command_send_message_next_to(message: Message, state: FSMContext) -> None:
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    list_of_users.append(message.text.split('\n'))
    bad_users = []
    for user in list_of_users[0]:
        try:
            await message.bot.send_message(chat_id=int(user), text=message_to_users[0],
                                           entities=message_to_users[1], parse_mode=None
                                           )
        except:
            print(user)
            bad_users.append(f'{user}\n')
    if bad_users == []:
        await message.answer('Сообщение было доставлено всем пользователям!')
    else:
        bad_users = '\n'.join(bad_users)
        await message.answer('Сообщение было доставлено всем пользователям!\n'
                             'Кроме:\n'
                             f'<b>{bad_users}</b>'
                             f'\n'
                             f'<b>Они не подписаны на бот!</b>')
    list_of_users.clear()
    message_to_users.clear()
    await state.clear()
