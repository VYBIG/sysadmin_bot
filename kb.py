from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# Функции Бота:
# чей номер телефона https://apertonet.ru/zvonit/

# Клавиатура основного меню
main_menu_1 = [
    [InlineKeyboardButton(text="🧮 IP Калькулятор", callback_data='ip_calc')],
    [InlineKeyboardButton(text="🧾 MAC Vendor", callback_data='mac_vendor')],
    [InlineKeyboardButton(text="↔️ Бит в Байт", callback_data='bit_to_byte')],
    [InlineKeyboardButton(text="✉️ Ping", callback_data='ping')],
    [InlineKeyboardButton(text="🔄 Trace route", callback_data='tracert')],
    [InlineKeyboardButton(text="📃 Информация о IP", callback_data='ip_info')],
    [InlineKeyboardButton(text="⏩ Дальше ", callback_data='next_menu_2')]]

main_menu_2 = [
    [InlineKeyboardButton(text="📲 Чей Номер телефона", callback_data='phone_number')],
    [InlineKeyboardButton(text="🔖 ДНС имя IP", callback_data='nslookup')],
    [InlineKeyboardButton(text="📶 Проверка Портов", callback_data='ports_check')],
    [InlineKeyboardButton(text="🈳 Полезные команды", callback_data='useful_command')],
    [InlineKeyboardButton(text="🔢 Генератор Паролей", callback_data='password_gen')],
    [InlineKeyboardButton(text="#️⃣ Создать QR-код", callback_data='QR_code_maker')],
    [InlineKeyboardButton(text="⏪ Назад", callback_data='back_menu_1')]]

# Клавиатура выхода в основное меню
exit_menu_1 = [[InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='back_menu_1')]]

exit_menu_2 = [[InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='next_menu_2')]]
# Запуск Клавиатуры основного меню
main_menu_1 = InlineKeyboardMarkup(inline_keyboard=main_menu_1,)
main_menu_2 = InlineKeyboardMarkup(inline_keyboard=main_menu_2)
# Запуск клавиатуры выхода в основное меню
exit_menu_1 = InlineKeyboardMarkup(inline_keyboard=exit_menu_1)
exit_menu_2 = InlineKeyboardMarkup(inline_keyboard=exit_menu_2)
