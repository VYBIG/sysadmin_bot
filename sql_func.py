import sqlite3
import time


class SQL_connect:
    def __init__(self, connect):
        self.connect = sqlite3.connect(f'{connect}')
        self.cursor = self.connect.cursor()

    def add_user(self, table: str, data: dict):

        columns = ', '.join((column for column in data.keys()))
        values = ', '.join(('?' for _ in range(len(data))))
        raws = (data[column] for column in data.keys())
        self.cursor.execute(f'INSERT INTO {table} ({columns}) VALUES ({values})',
                            (f'{next(raws)}', f'{next(raws)}', f'{next(raws)}'))

        self.connect.commit()
        self.connect.close()

    def select_user(self, user_id):
        user = self.cursor.execute(f'SELECT * FROM Users WHERE User_ID == {user_id}')
        print(user.fetchone())
        self.connect.close()

    # def delete_user(self, user_id):
    #     pass
    @staticmethod
    def chusr(user_id,db):
        con = sqlite3.connect(f'{db}')
        curs = con.cursor()
        if curs.execute(f'SELECT * FROM Users WHERE User_ID == {user_id}') is None:
            con.close()
            return False
        else:
            con.close()
            return True
