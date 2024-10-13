import time
import random
from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, PollAnswer
from common_functions import main_log
from kb import exit_menu_2, pass_gen_kb_1

router = Router(name=__name__)


def pass_gen_func(length: int = 0,
                  digit: bool = False,
                  big_symb: bool = False,
                  small_symb: bool = False,
                  special: bool = False):
    defaul_str = ''
    digital = '1234567890'
    small_symbol = 'qwertyuiopasdfghjklzxcvbnm'
    big_symbol = small_symbol.upper()
    special_symbol = '%*_?@#$~'
    if digit:
        defaul_str += digital
    if big_symb:
        defaul_str += big_symbol
    if small_symb:
        defaul_str += small_symbol
    if special:
        defaul_str += special_symbol
    psw = ''.join([random.choice(list(defaul_str)) for x in range(length)])
    return psw


class Password_gen_st(StatesGroup):
    pass_gen_state = State()
    pool_state = State()


@router.callback_query(F.data == 'password_gen')
async def password_gen_main(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(Password_gen_st.pass_gen_state)
    main_log(callback=callback)
    await callback.message.answer(text='<b>Хотите сгенерировать пароль?</b>\n'
                                       'Напишите его длину (не больше 50 символов),\n'
                                       'после чего заполните форму',
                                  reply_markup=exit_menu_2)


@router.message(Password_gen_st.pass_gen_state,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def password_gen_count(message: Message,
                             state: FSMContext):
    main_log(message=message)
    try:
        count = int(message.text)
        await state.update_data(pass_gen_state=count)
        await state.set_state(Password_gen_st.pool_state)
        if count not in [i for i in range(1, 51)]:
            raise IndexError
        await message.answer_poll(question='Заполните форму ниже \n'
                                           'и нажмите кнопкe:'
                                           '<b>Голосовать</b>\n'
                                           f'<b>Длина пароля составляет'
                                           f' {message.text} '
                                           f'- Символов</b>',
                                  options=['Цифры 0-9',
                                           'ПРОПИСНЫЕ БУКВЫ A-Z',
                                           'строчные буквы a-z',
                                           'Спец. символы %, *, _,?, @, #, $, ~'],
                                  allows_multiple_answers=True,
                                  is_anonymous=False)
    except IndexError:
        await message.answer('Не верная длина\n'
                             'Повторите ввод:')
    except ValueError:
        await message.answer('Длина должна быть в виде числа\n'
                             'Повторите ввод:')


@router.poll_answer(Password_gen_st.pool_state)
async def pool_answers(pool: PollAnswer, state: FSMContext):
    main_log(pool=pool)
    # await state.update_data(pool_state=pool.option_ids)
    answers = dict(await state.get_data())
    message_ID = await pool.bot.send_message(chat_id=pool.user.id,
                                             text='Пароли генерируются,\n'
                                                  'пожалуйста подождите 🔄')
    await pool.bot.send_chat_action(chat_id=pool.user.id, action=ChatAction.TYPING)
    time.sleep(1)
    digit, big_symb, small_symb, special = False, False, False, False
    if 0 in pool.option_ids:
        digit = True
    if 1 in pool.option_ids:
        big_symb = True
    if 2 in pool.option_ids:
        small_symb = True
    if 3 in pool.option_ids:
        special = True
    text = ""
    for passw in range(1, 11):
        text += '<pre>' + \
                str(pass_gen_func(answers['pass_gen_state'],
                                  digit=digit,
                                  big_symb=big_symb,
                                  small_symb=small_symb,
                                  special=special)) + '</pre>' + '\n'
    await pool.bot.edit_message_text(chat_id=pool.user.id,
                                     message_id=message_ID.message_id,
                                     text='Сгенерировал 10 паролей по вашему запросу:'
                                          f'{text}',
                                     reply_markup=exit_menu_2)
    await state.clear()
