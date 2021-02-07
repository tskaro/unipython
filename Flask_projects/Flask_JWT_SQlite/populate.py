import sqlite3

user_list = [
    (1, "tskaro", "unilab21"),
    (2, "user2", "unilab22"),
    (3, "user3", "unilab23")
]

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users (user_id real, username text, password text)')

# cursor.execute("INSERT INTO users VALUES(1, 'tskaro1', 'unilab1')")
query_string = "INSERT INTO users VALUES(?, ?, ?)"

cursor.executemany(query_string, user_list)

connection.commit()

connection.close()
