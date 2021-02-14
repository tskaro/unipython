import sqlite3


connection = sqlite3.connect("Health_data.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Health_info (row_id INTEGER PRIMARY KEY, patient_id integer, "
               "Glucose integer, SBP integer, DBP integer, time str)")
connection.commit()
connection.close()
