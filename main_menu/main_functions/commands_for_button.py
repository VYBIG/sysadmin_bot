from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

commands_button = [
    [InlineKeyboardButton(text="Windows -|-", callback_data='win_command')],
    [InlineKeyboardButton(text="Linux 🐧", callback_data='ubuntu_command')],
    [InlineKeyboardButton(text="Cisco ©️", callback_data='cisco_command')],
    [InlineKeyboardButton(text="Docker 🐳", callback_data='docker_command')],
    [InlineKeyboardButton(text="K8s by kubectl 🚢", callback_data='k8s_command')]]
commands_button = InlineKeyboardMarkup(inline_keyboard=commands_button)

win_button_1 = [
    [InlineKeyboardButton(text="Windows -|-", callback_data='win_command')],
    [InlineKeyboardButton(text="Linux 🐧", callback_data='ubuntu_command')],
    [InlineKeyboardButton(text="Cisco ©️", callback_data='cisco_command')],
    [InlineKeyboardButton(text="Docker 🐳", callback_data='docker_command')],
    [InlineKeyboardButton(text="K8s by kubectl 🚢", callback_data='k8s_command')]]

win_button_1 = InlineKeyboardMarkup(inline_keyboard=win_button_1)