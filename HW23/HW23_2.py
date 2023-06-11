import sqlite3

conn = sqlite3.connect("/Users/pavlo/Documents/Python/book_store.sqlite")
cursor = conn.cursor()

query = """
SELECT purchases.id, purchases.date, users.first_name, users.last_name
FROM purchases
JOIN users ON purchases.user_id = users.id;
"""

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    purchase_id, purchase_date, first_name, last_name = row
    print(f"Purchase ID: {purchase_id}, Date: {purchase_date}, Name: {first_name} {last_name}")

conn.close()