import logging
import time


def main_log(message=None, callback=None):
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
    else:
        user_id = message.from_user.id
        user_full_name = message.from_user.full_name
        user_message = message.text
        username = message.from_user.username
        logging.info(
            f'time={time.asctime()}, user_id={user_id}, '
            f'user_full_name={user_full_name}, '
            f'user_message={user_message}, '
            f'username = {username}')
