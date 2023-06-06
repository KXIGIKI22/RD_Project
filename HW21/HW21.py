import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO users (first_name, last_name, age) 
VALUES ('Pavlo', 'Kulka', 27),
        ('Vitalii', 'Hrebennikov', 20),
        ....")

conn.commit()

conn.close()