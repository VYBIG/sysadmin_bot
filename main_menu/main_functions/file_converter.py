import os
import time

from aiogram import Router, F
from aiogram.enums import ChatAction
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message, BufferedInputFile
from common_functions import main_log
from kb import file_converter_main, exit_menu_2, back_to_file_converter
from aiogram.exceptions import TelegramBadRequest
from .any_file_converter import *

router = Router(name=__name__)


class File_converter_state(StatesGroup):
    file_state_main = State()
    video_to_circle_state = State()


@router.callback_query(F.data == 'file_converter')
async def file_conv(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await callback.answer(cache_time=1)
    await state.set_state(File_converter_state.file_state_main)
    await callback.message.edit_text('Функция в Разработке',
                                     reply_markup=exit_menu_2)


# @router.callback_query(F.data == 'file_converter')
# async def file_conv(callback: CallbackQuery, state: FSMContext):
#     main_log(callback=callback)
#     await state.clear()
#     await callback.answer(cache_time=1)
#     await state.set_state(File_converter_state.file_state_main)
#     await callback.message.answer('Выбери что нужно конвертировать',
#                                   reply_markup=file_converter_main)


@router.callback_query(File_converter_state.file_state_main,
                       F.data == 'video_to_circle')
async def file_conv_vid_to_cir(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await state.set_state(File_converter_state.video_to_circle_state)
    await callback.message.edit_text('Отправьте видео длительностью не более минуты\n'
                                     'и весом не больше 50МБ ',
                                     reply_markup=back_to_file_converter)


@router.message(File_converter_state.video_to_circle_state,
                F.video,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def video_to_circle_conv(message: Message, state: FSMContext):
    main_log(message=message)
    file_id = message.video.file_id
    await message.bot.download(file_id, f"{file_id}.MP4")
    if message.video.duration >= 60:
        await message.answer('Видео Длиннее одной минуты\n'
                             'Отправьте другой или ', reply_markup=back_to_file_converter)
    elif message.video.file_size >= 50000000:
        await message.answer('Видео файл слишком большой\n'
                             'Отправьте другой или ', reply_markup=back_to_file_converter)
    else:
        await message.answer('Не много подождите, файл обрабатывается!')
        new_video_file = open(f"{video_for_circle(file_id)}.MP4", 'rb').read()
        circle_file = BufferedInputFile(new_video_file, f"circle_{file_id}.MP4")
        await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.RECORD_VIDEO_NOTE)
        try:
            await message.bot.send_video_note(message.chat.id,
                                              video_note=circle_file)

            os.remove(f"{file_id}.MP4")
            os.remove(f"circle_{file_id}.MP4")
        except TelegramBadRequest:
            os.remove(f"{file_id}.MP4")
            os.remove(f"circle_{file_id}.MP4")
            await message.answer('Я не могу отправить вам Кружочек или голосовое \n'
                                 'пока вы не поправите настройки конфиденциальности')


# @router.message(Command('sen_vid'))
# async def video_to_circle_conv(message: Message, state: FSMContext):
#     # new_video_file = open(f"{video_for_circle(file_id)}.MP4", 'rb').read()
#     new_video_file = open(f"circle_123cas.mp4", 'rb').read()
#     circle_file = BufferedInputFile(new_video_file, f"circle_123cas.MP4")
#     await message.bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.RECORD_VIDEO_NOTE)
#     await message.bot.send_video_note(message.chat.id,
#                                       video_note=circle_file)


@router.message(File_converter_state.video_to_circle_state,
                ~F.video,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def not_video_to_circle_conv(message: Message):
    await message.answer('Я ожидал видео 🥺\n'
                         'Отправьте видео или ',
                         reply_markup=back_to_file_converter)


@router.message(File_converter_state.file_state_main,
                ~Command('help', 'start', 'get_id', 'chat_gpt', 'cancel', 'get_log'))
async def why_do_you_write_me(message: Message, state: FSMContext):
    main_log(message=message)
    await state.clear()
    await state.set_state(File_converter_state.file_state_main)
    await message.answer('<b>Кто-то не умеет читать! 🤓\n'
                         'Нужно просто нажать на любую кнопку ниже ⬇️\n</b>')
    await message.answer('<b>Выбери что нужно конвертировать</b>',
                         reply_markup=file_converter_main)


@router.callback_query(F.data == 'file_converter_back')
async def file_conv_back(callback: CallbackQuery, state: FSMContext):
    main_log(callback=callback)
    await state.clear()
    await state.set_state(File_converter_state.file_state_main)
    await callback.message.edit_text('Выбери что нужно конвертировать',
                                     reply_markup=file_converter_main)


@router.callback_query(F.data.in_({'video_to_circle',
                                   'video_mp3_to_voice',
                                   'pdf_to_word',
                                   'heic_to_jpeg',
                                   'jpeg_to_png'}))
async def file_conv_no_no_no(callback: CallbackQuery, ):
    main_log(callback=callback)
    await callback.message.edit_text('<blockquote>Это сообщение давно позади 😐</blockquote>')
