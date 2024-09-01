from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Функции Бота:
# чей номер телефона https://apertonet.ru/zvonit/

# Клавиатура основного меню
main_menu_1 = [
    [InlineKeyboardButton(text="🧮 IP Калькулятор", callback_data='ip_calc')],
    [InlineKeyboardButton(text="🧾 MAC Vendor", callback_data='mac_vendor')],
    [InlineKeyboardButton(text="📶 Проверка Портов", callback_data='ports_check')],
    [InlineKeyboardButton(text="✉️ Ping", callback_data='ping')],
    [InlineKeyboardButton(text="🔄 Trace route", callback_data='tracert')],
    [InlineKeyboardButton(text="📃 Информация о IP", callback_data='ip_info')],
    [InlineKeyboardButton(text="⏩ Дальше ", callback_data='next_menu_2')]]

main_menu_2 = [
    [InlineKeyboardButton(text="📲 Чей Номер телефона", callback_data='phone_number')],
    [InlineKeyboardButton(text="🔖 ДНС <> IP (nslookup)", callback_data='nslookup')],
    [InlineKeyboardButton(text="↔️ Бит в Байт", callback_data='bit_to_byte')],
    [InlineKeyboardButton(text="🈳 Полезные команды", callback_data='useful_command')],
    [InlineKeyboardButton(text="🔢 Генератор Паролей", callback_data='password_gen')],
    [InlineKeyboardButton(text="#️⃣ Создать QR-код", callback_data='QR_code_maker')],
    [InlineKeyboardButton(text="⏪ Назад", callback_data='back_menu_1')]]

# Клавиатура выхода в основное меню
exit_menu_1 = [[InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='back_menu_1')]]
exit_menu_2 = [[InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='next_menu_2')]]
# Запуск Клавиатуры основного меню
main_menu_1 = InlineKeyboardMarkup(inline_keyboard=main_menu_1)
main_menu_2 = InlineKeyboardMarkup(inline_keyboard=main_menu_2)
# Запуск клавиатуры выхода в основное меню
exit_menu_1 = InlineKeyboardMarkup(inline_keyboard=exit_menu_1)
exit_menu_2 = InlineKeyboardMarkup(inline_keyboard=exit_menu_2)

ip_calc_kb = [[InlineKeyboardButton(text="🎭 Открыть Памятку Масок", callback_data='mask_faq')],
              [InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='back_menu_1')]]
back_to_ip_calc = [[InlineKeyboardButton(text="⬅️ Вернуться в IP Калькулятор", callback_data='ip_calc_back')]]

ip_calc_kb = InlineKeyboardMarkup(inline_keyboard=ip_calc_kb)
back_to_ip_calc = InlineKeyboardMarkup(inline_keyboard=back_to_ip_calc)

udp_tcp_prtl = [[InlineKeyboardButton(text="↖️ UDP", callback_data='udp_callback')],
                [InlineKeyboardButton(text="🔁 TCP", callback_data='tcp_callback')],
                [InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='back_menu_1')]]

udp_tcp_prtl = InlineKeyboardMarkup(inline_keyboard=udp_tcp_prtl)