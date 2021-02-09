import sqlite3


class User:
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        connection.commit()
        connection.close()
        if row:
            return cls(*row)

    @classmethod
    def find_by_id(cls, user_id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
        row = cursor.fetchone()
        connection.commit()
        connection.close()
        if row:
            return cls(*row)
