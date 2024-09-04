from aiogram import Router
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from kb import back_to_main_menu

router = Router(name=__name__)


@router.message(Command('help'))
async def command_help_handler(message: Message, state: FSMContext) -> None:
    await state.clear()
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


@router.message(Command('chat_gpt'))
async def command_gpt(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await message.answer(f"Решим Нейросети находится в разработке! 🔜")


@router.message(Command('get_id'))
async def command_get_id(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
    await message.answer(f'Твой Телеграмм ID - {message.from_user.id}')


@router.message(Command('cancel'))
async def command_get_id(message: Message, state: FSMContext) -> None:
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
