from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
    [InlineKeyboardButton(text="📨 Конвертер Файлов", callback_data='file_converter')],
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

ip_calc_kb = [[InlineKeyboardButton(text="🎭 Открыть Памятку Масок ", callback_data='mask_faq')],
              [InlineKeyboardButton(text="0️⃣1️⃣ Добавить IP в двоичном формате  ", callback_data='to_bit')],
              [InlineKeyboardButton(text="Вернуться Назад ⬅️", callback_data='back_menu_1')]]
back_to_ip_calc = [[InlineKeyboardButton(text="⬅️ Вернуться в IP Калькулятор", callback_data='ip_calc_back')]]

ip_calc_kb_wo_to_bit = [[InlineKeyboardButton(text="🎭Открыть Памятку Масок", callback_data='mask_faq')],
                        [InlineKeyboardButton(text="🔢 Убрать двоичный формат", callback_data='no_to_bit')],
                        [InlineKeyboardButton(text="Вернуться Назад ⬅️", callback_data='back_menu_1')]]
ip_calc_kb_wo_to_bit = InlineKeyboardMarkup(inline_keyboard=ip_calc_kb_wo_to_bit)

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
      InlineKeyboardButton(text="⬅️ Назад", callback_data='back_menu_1')]
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
      InlineKeyboardButton(text="⬅️ Назад", callback_data='back_menu_1')]
     ]

mac_convert_upper = InlineKeyboardMarkup(inline_keyboard=mac_convert_upper)
mac_convert_lower = InlineKeyboardMarkup(inline_keyboard=mac_convert_lower)

exit_convert_upper = [[InlineKeyboardButton(text="⬅️ Назад", callback_data='back_to_upper')]]
exit_convert_lower = [[InlineKeyboardButton(text="⬅️ Назад", callback_data='back_to_lower')]]

exit_convert_upper = InlineKeyboardMarkup(inline_keyboard=exit_convert_upper)
exit_convert_lower = InlineKeyboardMarkup(inline_keyboard=exit_convert_lower)

pass_gen_kb_1 = [
    [InlineKeyboardButton(text="⏩ Продолжить ", callback_data='passgen_continue')]]

pass_gen_kb_1 = InlineKeyboardMarkup(inline_keyboard=pass_gen_kb_1)

pass_gen_kb_2 = [
    [InlineKeyboardButton(text="⏩ Продолжить ", callback_data='passgen_continue_2')]]

pass_gen_kb_2 = InlineKeyboardMarkup(inline_keyboard=pass_gen_kb_2)

bit_to_byte_menu = \
    [[InlineKeyboardButton(text="Бит", callback_data='bit'),
      InlineKeyboardButton(text="Байт", callback_data='byte')],
     [InlineKeyboardButton(text="КилоБит", callback_data='kbit'),
      InlineKeyboardButton(text="КилоБайт", callback_data='kbyte')],
     [InlineKeyboardButton(text="МегаБит", callback_data='mbit'),
      InlineKeyboardButton(text="МегаБайт", callback_data='mbyte')],
     [InlineKeyboardButton(text="ГигаБит", callback_data='gbit'),
      InlineKeyboardButton(text="ГигаБайт", callback_data='gbyte')],
     [InlineKeyboardButton(text="ТераБит", callback_data='tbit'),
      InlineKeyboardButton(text="ТераБайт", callback_data='tbyte')],
     [InlineKeyboardButton(text="ПетаБит", callback_data='pbit'),
      InlineKeyboardButton(text="ПетаБайт", callback_data='pbyte')],
     [InlineKeyboardButton(text="ЭксаБит", callback_data='ebit'),
      InlineKeyboardButton(text="ЭксаБайт", callback_data='ebyte')],
     [InlineKeyboardButton(text="⬅️ Назад", callback_data='btby_back')]
     ]

bit_to_byte_table = [
    [InlineKeyboardButton(text="🈸 Таблица Преобразования", callback_data='btby_table'),
     InlineKeyboardButton(text="🔂 Начать Конвертацию", callback_data='btby_start')],
    [InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='next_menu_2')]]
bit_to_byte_back = [
    [InlineKeyboardButton(text="⬅️ Назад", callback_data='btby_back')]]

bit_to_byte_menu = InlineKeyboardMarkup(inline_keyboard=bit_to_byte_menu)
bit_to_byte_table = InlineKeyboardMarkup(inline_keyboard=bit_to_byte_table)
bit_to_byte_back = InlineKeyboardMarkup(inline_keyboard=bit_to_byte_back)

file_converter_main = [
    [InlineKeyboardButton(text="🌠 Видео ➡️ Кружочек ⭕️", callback_data='video_to_circle')],
    [InlineKeyboardButton(text="🌠 Видео/MP3 ➡️ Голосовое 🗣", callback_data='video_mp3_to_voice')],
    [InlineKeyboardButton(text="🌠 Видео ➡️ MP3 🎧", callback_data='video_to_mp3')],
    [InlineKeyboardButton(text="📃 PDF ➡️ Word 🧾", callback_data='pdf_to_word')],
    [InlineKeyboardButton(text="🏞 Heic ➡️ jpeg 🖼", callback_data='heic_to_jpeg')],
    [InlineKeyboardButton(text="🖼 jpeg ➡️ png 📰", callback_data='jpeg_to_png')],
    [InlineKeyboardButton(text="⬅️ Вернуться Назад", callback_data='next_menu_2')]]
file_converter_main = InlineKeyboardMarkup(inline_keyboard=file_converter_main)

back_to_file_converter = [[InlineKeyboardButton(text="⬅️ Вернуться обратно", callback_data='file_converter_back')]]
back_to_file_converter = InlineKeyboardMarkup(inline_keyboard=back_to_file_converter)

