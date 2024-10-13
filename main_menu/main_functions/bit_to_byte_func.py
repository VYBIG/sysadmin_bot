from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message
from kb import exit_menu_2, bit_to_byte_table, bit_to_byte_back, bit_to_byte_menu
from common_functions import main_log, bit_to_byte_conferter_func

router = Router(name=__name__)


class B2b_state(StatesGroup):
    from_state = State()
    to_state = State()
    count_state = State()


b_to_by_dict = \
    {'bit': "Бит", 'byte': "Байт",
     'kbit': "КилоБит", 'kbyte': "КилоБайт",
     'mbit': "МегаБит", 'mbyte': "МегаБайт",
     'gbit': "ГигаБит", 'gbyte': "ГигаБайт",
     'tbit': "ТераБит", 'tbyte': "ТераБайт",
     'pbit': "ПетаБит", 'pbyte': "ПетаБайт",
     'ebit': "ЭксаБит", 'ebyte': "ЭксаБайт"}


@router.callback_query(F.data == 'bit_to_byte')
async def from_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(B2b_state.from_state)
    await callback.message.answer('Это Функция Конвертации '
                                  '↔️ Бит в Байт\n'
                                  'Чтобы <b>начать конвертацию</b> '
                                  'нажмите на кнопку ниже',
                                  reply_markup=bit_to_byte_table)


@router.callback_query(F.data == 'btby_back')
async def from_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(B2b_state.from_state)
    await callback.message.edit_text('Это Функция Конвертации '
                                     '↔️ Бит в Байт\n'
                                     'Чтобы <b>начать конвертацию</b> '
                                     'нажмите на кнопку ниже',
                                     reply_markup=bit_to_byte_table)


@router.callback_query(F.data == 'btby_table')
async def from_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await callback.message \
        .edit_text('📜 Таблица соотношения единиц измерения информации\n\n'
                   '<blockquote>1 Бит - Наименьшая единица измерения\n\n'
                   '1 Байт = 8 Бит\n\n'
                   '1 Килобайт = 1024 Байт\n\n'
                   '1 Мегабайт = 1024 Килобайт\n\n'
                   '1 Гигабайт = 1024 Мегабайт\n\n'
                   '1 Терабайт = 1024 Гигабайт\n\n'
                   '——— ⬇️ Редко используемые ⬇️———\n\n'
                   '1 Петабайт = 1024 Терабайт\n\n'
                   '1 Эксабайт = 1024 Эксабайт\n\n</blockquote>',
                   reply_markup=bit_to_byte_back)


@router.callback_query(F.data == 'btby_start')
async def from_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(B2b_state.from_state)
    await callback.message.answer('<b>Бит ↔️ Байт</b>\n\n\n'
                                  'Выберете из чего переводить:',
                                  reply_markup=bit_to_byte_menu)


@router.callback_query(B2b_state.from_state,
                       F.data.in_({'bit', 'byte', 'kbit', 'kbyte',
                                   'mbit', 'mbyte', 'gbit',
                                   'gbyte', 'tbit',
                                   'tbyte', 'pbit',
                                   'pbyte', 'ebit', 'ebyte'}))
async def to_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.update_data(from_state=callback.data)
    await callback.answer(cache_time=1)
    await state.set_state(B2b_state.to_state)
    from_data = await state.get_data()
    await callback.message.edit_text(f'<blockquote>↔️ Конвертация будет из '
                                     f'{b_to_by_dict[from_data["from_state"]]}</blockquote>\n\n'
                                     '<b>Выберете во что конвертировать:</b>', reply_markup=bit_to_byte_menu)


@router.callback_query(B2b_state.to_state,
                       F.data.in_({'bit', 'byte', 'kbit', 'kbyte',
                                   'mbit', 'mbyte', 'gbit',
                                   'gbyte', 'tbit',
                                   'tbyte', 'pbit',
                                   'pbyte', 'ebit', 'ebyte'}))
async def digit_func(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await callback.answer(cache_time=1)
    await state.set_state(B2b_state.count_state)
    await state.update_data(to_state=callback.data)
    from_to_data = await state.get_data()
    await callback.message.edit_text('<blockquote>↔️ Конвертация будет из '
                                     f'{b_to_by_dict[from_to_data["from_state"]]} в '
                                     f'{b_to_by_dict[from_to_data["to_state"]]}</blockquote>\n\n'
                                     'Напишите ваше число:', reply_markup=bit_to_byte_back)


@router.message(B2b_state.count_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def bit_to_byte_func(message: Message, state: FSMContext):
    main_log(message=message)
    from_to_data = await state.get_data()
    try:
        float(message.text)
        if float(message.text) <= 0:
            raise ValueError
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
        the_count = bit_to_byte_conferter_func(float(message.text),
                                               b_to_by_dict[from_to_data["from_state"]],
                                               b_to_by_dict[from_to_data["to_state"]])
        await message.answer(f'<blockquote>↔️ Конвертация {message.text} '
                             f'{b_to_by_dict[from_to_data["from_state"]]} в '
                             f'{b_to_by_dict[from_to_data["to_state"]]}</blockquote>\n\n'
                             f'Конвертированное число : <code>{the_count}</code>'
                             f'<b> {b_to_by_dict[from_to_data["to_state"]]}</b>', reply_markup=bit_to_byte_back)
        await state.clear()
    except ValueError:
        await message.answer('<b>Число не корректное</b> ⁉️\n'
                             'Повторите ввод:'
                             , reply_markup=exit_menu_2)


@router.callback_query(F.data.in_({'bit', 'byte', 'kbit', 'kbyte',
                                   'mbit', 'mbyte', 'gbit',
                                   'gbyte', 'tbit',
                                   'tbyte', 'pbit',
                                   'pbyte', 'ebit', 'ebyte'}))
async def unknown_func_btby(callback: CallbackQuery):
    await callback.message.edit_text('Это сообщение давно позади 😐')
