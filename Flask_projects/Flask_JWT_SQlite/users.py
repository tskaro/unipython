import sqlite3


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


def find_by_username(username):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    feedback = cursor.fetchall()
    if len(feedback) == 0:
        result = None
    else:
        user_id, username, password = feedback[0]
        result = User(user_id, username, password)
    connection.commit()
    connection.close()
    return result


def find_by_id(user_id):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    feedback = cursor.fetchall()
    if len(feedback) == 0:
        result = None
    else:
        user_id, username, password = feedback[0]
        result = User(user_id, username, password)
    connection.commit()
    connection.close()
    return result


print(find_by_username('tskaro').username)
print(find_by_id(4))
