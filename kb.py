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
    [InlineKeyboardButton(text="🔂 Конвертер MAC-Адресов", callback_data='mac_converter')],
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

back_to_main_menu = [[InlineKeyboardButton(text="↩️️️ Вернуться в Основное меню", callback_data='back_to_main_menu')]]

back_to_main_menu = InlineKeyboardMarkup(inline_keyboard=back_to_main_menu)

pnc_kb = [[InlineKeyboardButton(text="☎️ Открыть Памятку кодов городов", callback_data='pnc_faq')],
          [InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='next_menu_2')]]
back_to_pnc = [[InlineKeyboardButton(text="⬅️ Вернуться в поиск номера", callback_data='pnc_back')]]

pnc_kb = InlineKeyboardMarkup(inline_keyboard=pnc_kb)
back_to_pnc = InlineKeyboardMarkup(inline_keyboard=back_to_pnc)

mac_convert_upper = \
    [[InlineKeyboardButton(text="Заглавные ✅", callback_data='upper_callback'),
      InlineKeyboardButton(text="Строчные", callback_data='lower_callback')],
     [InlineKeyboardButton(text="XX:XX:XX:XX:XX:XX", callback_data='colon_1_callback'),
      InlineKeyboardButton(text="XX.XX.XX.XX.XX.XX", callback_data='point_1_callback')],
     [InlineKeyboardButton(text="XX-XX-XX-XX-XX-XX", callback_data='hyphen_1_callback'),
      InlineKeyboardButton(text="XXXX:XXXX:XXXX", callback_data='colon_2_callback')],
     [InlineKeyboardButton(text="XXXX.XXXX.XXXX", callback_data='point_2_callback'),
      InlineKeyboardButton(text="XXXX-XXXX-XXXX", callback_data='hyphen_2_callback')],
     [InlineKeyboardButton(text="XXXXXXXXXXXX", callback_data='solid_callback'),
      InlineKeyboardButton(text="⬅️Назад", callback_data='back_menu_1')]
     ]

mac_convert_lower = \
    [[InlineKeyboardButton(text="Заглавные", callback_data='upper_callback'),
      InlineKeyboardButton(text="Строчные ✅", callback_data='lower_callback')],
     [InlineKeyboardButton(text="xx:xx:xx:xx:xx:xx", callback_data='colon_1_callback'),
      InlineKeyboardButton(text="xx.xx.xx.xx.xx.xx", callback_data='point_1_callback')],
     [InlineKeyboardButton(text="xx-xx-xx-xx-xx-xx", callback_data='hyphen_1_callback'),
      InlineKeyboardButton(text="xxxx:xxxx:xxxx", callback_data='colon_2_callback')],
     [InlineKeyboardButton(text="xxxx.xxxx.xxxx", callback_data='point_2_callback'),
      InlineKeyboardButton(text="xxxx-xxxx-xxxx", callback_data='hyphen_2_callback')],
     [InlineKeyboardButton(text="xxxxxxxxxxxx", callback_data='solid_callback'),
      InlineKeyboardButton(text="⬅️Назад", callback_data='back_menu_1')]
     ]

mac_convert_upper = InlineKeyboardMarkup(inline_keyboard=mac_convert_upper)
mac_convert_lower = InlineKeyboardMarkup(inline_keyboard=mac_convert_lower)

exit_convert_upper = [[InlineKeyboardButton(text="⬅️ Назад", callback_data='back_to_upper')]]
exit_convert_lower = [[InlineKeyboardButton(text="⬅️ Назад", callback_data='back_to_lower')]]

exit_convert_upper = InlineKeyboardMarkup(inline_keyboard=exit_convert_upper)
exit_convert_lower = InlineKeyboardMarkup(inline_keyboard=exit_convert_lower)
