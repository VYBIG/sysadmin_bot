import logging
import time
from sql_func import *


def main_log(message=None, callback=None, pool=None):
    sql = SQL_connect('users.db')
    if callback is not None:
        user_id = callback.from_user.id
        user_full_name = callback.from_user.full_name
        user_message = callback.data
        username = callback.from_user.username
        logging.info(
            f'time={time.asctime()}, user_id={user_id}, '
            f'user_full_name={user_full_name}, '
            f'user_pressed={user_message}, '
            f'username = {username}')
        sql.add_user('Users_action', {'Date': time.asctime(),
                                      'User_ID': user_id,
                                      'user_callback': user_message})


    elif message is not None:
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        user_message = message.text
        username = message.from_user.username
        logging.info(
            f'time={time.asctime()}, user_id={user_id}, '
            f'user_full_name={user_full_name}, '
            f'user_message={user_message}, '
            f'username = {username}')
        if sql.chusr(user_id=user_id,db='users.db'):
            sql.add_user('Users', {'User_ID': user_id,
                                   'User_Name': username,
                                   'User_Nick_Name': user_full_name})
        else:
            sql.add_user('Users_action', {'Date': time.asctime(),
                                          'User_ID': user_id,
                                          'user_message': user_message})

    elif pool is not None:
        user_id = pool.user.id
        user_full_name = pool.user.first_name
        user_message = pool.option_ids
        username = pool.user.username
        logging.info(
            f'time={time.asctime()}, user_id={user_id}, '
            f'user_full_name={user_full_name}, '
            f'user_message={user_message}, '
            f'username = {username}')
        sql.add_user('Users_action', {'Date': time.asctime(),
                                      'User_ID': user_id,
                                      'user_pool': user_message})
    elif message.file_id is not None:
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        user_message = message.file_id
        username = message.from_user.username
        logging.info(
            f'time={time.asctime()}, user_id={user_id}, '
            f'user_full_name={user_full_name}, '
            f'user_message={user_message}, '
            f'username = {username}')
        sql.add_user('Users_action', {'Date': time.asctime(),
                                      'User_ID': user_id,
                                      'user_file': user_message})


def bit_to_byte_conferter_func_add(dig, c_from, c_to):
    if 'Кило' in c_from:
        dig = dig * 1024
    elif 'Мега' in c_from:
        dig = dig * 1024 * 1024
    elif 'Гига' in c_from:
        dig = dig * 1024 * 1024 * 1024
    elif 'Тера' in c_from:
        dig = dig * 1024 * 1024 * 1024 * 1024
    elif 'Пета' in c_from:
        dig = dig * 1024 * 1024 * 1024 * 1024 * 1024
    elif 'Экса' in c_from:
        dig = dig * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    if 'Кило' in c_to:
        dig = dig / 1024
    elif 'Мега' in c_to:
        dig = dig / 1024 / 1024
    elif 'Гига' in c_to:
        dig = dig / 1024 / 1024 / 1024
    elif 'Тера' in c_to:
        dig = dig / 1024 * 1024 * 1024 * 1024
    elif 'Пета' in c_to:
        dig = dig / 1024 / 1024 * 1024 * 1024 * 1024
    elif 'Экса' in c_to:
        dig = dig / 1024 / 1024 / 1024 / 1024 / 1024 / 1024
    return dig


def bit_to_byte_conferter_func(dig, c_from, c_to):
    if c_from == c_to:
        return dig
    if 'Бит' in c_from and 'Байт' in c_to:
        dig = dig / 8
        dig = bit_to_byte_conferter_func_add(dig, c_from, c_to)
    if 'Байт' in c_from and 'Бит' in c_to:
        dig = dig * 8
        dig = bit_to_byte_conferter_func_add(dig, c_from, c_to)
    if 'Бит' in c_from and 'Бит' in c_to:
        dig = bit_to_byte_conferter_func_add(dig, c_from, c_to)
    if 'Байт' in c_from and 'Байт' in c_to:
        dig = bit_to_byte_conferter_func_add(dig, c_from, c_to)
    if dig % 10 == 0.0:
        return f'{dig:.0f}'
    else:
        return f'{dig:.2f}'
