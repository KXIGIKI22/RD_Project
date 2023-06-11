import sqlite3

conn = sqlite3.connect("/Users/pavlo/Documents/Python/book_store.sqlite")
cursor = conn.cursor()

query = """
SELECT users.id, users.first_name, users.last_name, books.title
FROM users
JOIN purchases ON users.id = purchases.user_id
JOIN books ON purchases.book_id = books.id
ORDER BY users.id;
"""

cursor.execute(query)
result = cursor.fetchall()

for row in result:
    user_id, first_name, last_name, book_title = row
    print(f"User ID: {user_id}, Name: {first_name} {last_name}, Book Title: {book_title}")

conn.close()