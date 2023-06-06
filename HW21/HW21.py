import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Pavlo', 'Kulka', 27)")

cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Vitalii', 'Hrebennikov', 20)")

cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Kurator', 'Ksenia', 17)")

cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('John', 'Baton', 28)")

cursor.execute("INSERT INTO users (first_name, last_name, age) VALUES ('Mister', 'Smith', 350)")

conn.commit()

conn.close()