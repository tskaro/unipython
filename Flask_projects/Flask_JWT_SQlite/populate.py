import sqlite3

items = [
    {"id": 1, "name": "Jedi Starfighter", "speed": 1, "arm": 1, "capacity": 15, "quantity": 11},
    {"id": 2, "name": "Starship Enterprise", "speed": 15, "arm": 9, "capacity": 3000, "quantity": 6},
    {"id": 3, "name": "Millennium Falcon", "speed": 18, "arm": 10, "capacity": 10, "quantity": 8},
    {"id": 4, "name": "super galaxy gurren lagann", "speed": 30, "arm": 10, "capacity": 10000, "quantity": 1}
]
list = []
for item in items:
    (*values,) = item.values()
    list.append((*values,))

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS ships (id INTEGER PRIMARY KEY, name text, speed integer, arm integer, capacity integer, quantity integer)')

query_string = "INSERT INTO ships VALUES(?, ?, ?, ?, ?, ?)"

cursor.executemany(query_string, list)

connection.commit()

connection.close()
